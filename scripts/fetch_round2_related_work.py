#!/usr/bin/env python3
"""Fetch a second citation/reference expansion from high-relevance candidates.

Input is the first-pass candidate CSV. The script selects a conservative set of
finance + LLM/agent/benchmark candidates, fetches Semantic Scholar citations and
references by paperId, and writes a manifest plus raw edge table.
"""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any


BASE_URL = "https://api.semanticscholar.org/graph/v1"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "processed" / "expansion_candidates_preliminary.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "round2_related_work_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "round2_related_work_manifest.csv"

BASE_COLUMNS = [
    "paperId",
    "title",
    "year",
    "citationCount",
    "venue",
    "authors",
    "doi",
    "arxiv",
    "url",
    "abstract",
    "intents",
    "isInfluential",
    "citation_or_reference",
]

EDGE_COLUMNS = [
    "source_round",
    "source_rank",
    "source_title",
    "source_year",
    "source_category",
    "source_score",
    "source_citationCount",
    "source_seed_hit_count",
    "source_paperId",
] + BASE_COLUMNS

MANIFEST_COLUMNS = [
    "source_round",
    "source_rank",
    "source_title",
    "source_year",
    "source_category",
    "source_score",
    "source_citationCount",
    "source_seed_hit_count",
    "source_paperId",
    "status",
    "citation_count",
    "reference_count",
    "related_count",
    "error",
]

ROUND2_MODEL_TERMS = {
    "large language model",
    "llm",
    "gpt",
    "chatgpt",
    "foundation model",
    "language model",
    "generative ai",
    "agent",
    "rag",
    "retrieval",
    "instruction",
    "benchmark",
    "reasoning",
    "finbert",
    "bert",
}

EXCLUDE_TITLE_TERMS = {
    "open challenge",
    "good debt or bad debt",
    "domain adaption",
    "impact of news on the commodity market",
}


def to_int(value: str, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def load_api_keys(path: Path) -> list[str]:
    payload = json.loads(path.expanduser().read_text(encoding="utf-8"))
    keys = [str(key).strip() for key in payload.get("api_keys", []) if str(key).strip()]
    if not keys:
        raise RuntimeError(f"No api_keys found in {path}")
    return keys


class SemanticScholarClient:
    def __init__(self, api_keys: list[str], min_interval_seconds: float = 1.0) -> None:
        self.api_keys = list(dict.fromkeys(api_keys))
        self.min_interval_seconds = max(min_interval_seconds, 1.0)
        self.next_allowed = [0.0 for _ in self.api_keys]
        self.next_index = 0
        self.request_count = 0

    def _acquire_key(self) -> tuple[int, str]:
        while True:
            now = time.monotonic()
            for offset in range(len(self.api_keys)):
                idx = (self.next_index + offset) % len(self.api_keys)
                if now >= self.next_allowed[idx]:
                    self.next_index = (idx + 1) % len(self.api_keys)
                    return idx, self.api_keys[idx]
            time.sleep(max(0.01, min(self.next_allowed) - now))

    def get_json(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        query = urllib.parse.urlencode(params, doseq=True)
        url = f"{BASE_URL}{path}?{query}"
        for attempt in range(6):
            idx, key = self._acquire_key()
            request = urllib.request.Request(
                url, headers={"x-api-key": key, "Accept": "application/json"}
            )
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    self.next_allowed[idx] = time.monotonic() + self.min_interval_seconds
                    self.request_count += 1
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")
                self.next_allowed[idx] = time.monotonic() + self.min_interval_seconds
                self.request_count += 1
                if exc.code == 429 and attempt < 5:
                    retry_after = exc.headers.get("Retry-After")
                    delay = float(retry_after) if retry_after else self.min_interval_seconds
                    self.next_allowed[idx] = time.monotonic() + max(delay, self.min_interval_seconds)
                    continue
                if 500 <= exc.code < 600 and attempt < 5:
                    time.sleep(max(self.min_interval_seconds, 2**attempt))
                    continue
                raise RuntimeError(f"HTTP {exc.code} for {url}: {body}") from exc
            except urllib.error.URLError as exc:
                if attempt < 5:
                    time.sleep(max(self.min_interval_seconds, 2**attempt))
                    continue
                raise RuntimeError(f"Network error for {url}: {exc}") from exc
        raise RuntimeError(f"Request failed after retries: {url}")


def split_terms(value: str) -> set[str]:
    return {term.strip().lower() for term in (value or "").split(";") if term.strip()}


def select_round2_seeds(rows: list[dict[str, str]], limit: int) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for row in rows:
        rank = to_int(row.get("rank", "0"))
        year = to_int(row.get("year", "0"))
        hits = to_int(row.get("seed_hit_count", "0"))
        model_terms = split_terms(row.get("model_terms", ""))
        title = (row.get("title") or "").lower()

        if rank > 90 or hits < 5 or not row.get("paperId"):
            continue
        if any(term in title for term in EXCLUDE_TITLE_TERMS):
            continue
        if not (model_terms & ROUND2_MODEL_TERMS):
            continue
        if year < 2023 and "finbert" not in title:
            continue
        selected.append(row)
        if len(selected) >= limit:
            break
    return selected


def paper_to_row(edge: dict[str, Any], paper_key: str, relation_label: str) -> dict[str, str]:
    paper = edge.get(paper_key) or {}
    external = paper.get("externalIds") or {}
    authors = "; ".join(
        author.get("name", "").strip()
        for author in paper.get("authors") or []
        if isinstance(author, dict) and author.get("name")
    )
    intents = "; ".join(intent for intent in edge.get("intents") or [] if intent)
    return {
        "paperId": paper.get("paperId") or "",
        "title": paper.get("title") or "",
        "year": paper.get("year") if paper.get("year") is not None else "",
        "citationCount": paper.get("citationCount")
        if paper.get("citationCount") is not None
        else "",
        "venue": paper.get("venue") or "",
        "authors": authors,
        "doi": external.get("DOI") or "",
        "arxiv": external.get("ArXiv") or "",
        "url": paper.get("url") or "",
        "abstract": paper.get("abstract") or "",
        "intents": intents,
        "isInfluential": str(bool(edge.get("isInfluential", False))),
        "citation_or_reference": relation_label,
    }


def fetch_relation_rows(
    client: SemanticScholarClient,
    source_paper_id: str,
    endpoint: str,
    paper_key: str,
    relation_label: str,
) -> list[dict[str, str]]:
    fields = ",".join(
        [
            "intents",
            "isInfluential",
            f"{paper_key}.paperId",
            f"{paper_key}.title",
            f"{paper_key}.year",
            f"{paper_key}.citationCount",
            f"{paper_key}.venue",
            f"{paper_key}.authors",
            f"{paper_key}.externalIds",
            f"{paper_key}.url",
            f"{paper_key}.abstract",
        ]
    )
    rows: list[dict[str, str]] = []
    offset = 0
    while offset < 10000:
        payload = client.get_json(
            f"/paper/{source_paper_id}/{endpoint}",
            {"offset": offset, "limit": 1000, "fields": fields},
        )
        for edge in payload.get("data") or []:
            rows.append(paper_to_row(edge, paper_key, relation_label))
        next_offset = payload.get("next")
        if next_offset is None:
            break
        offset = to_int(str(next_offset), 10000)
    return rows


def source_prefix(row: dict[str, str]) -> dict[str, str]:
    return {
        "source_round": "round2",
        "source_rank": row.get("rank", ""),
        "source_title": row.get("title", ""),
        "source_year": row.get("year", ""),
        "source_category": row.get("category", ""),
        "source_score": row.get("score", ""),
        "source_citationCount": row.get("citationCount", ""),
        "source_seed_hit_count": row.get("seed_hit_count", ""),
        "source_paperId": row.get("paperId", ""),
    }


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    with Path(args.input).open(newline="", encoding="utf-8-sig") as f:
        candidates = list(csv.DictReader(f))
    seeds = select_round2_seeds(candidates, args.limit)
    client = SemanticScholarClient(load_api_keys(Path(args.api_keys_file)), args.min_interval_seconds)

    all_edges: list[dict[str, str]] = []
    manifest: list[dict[str, str]] = []
    for index, seed in enumerate(seeds, start=1):
        prefix = source_prefix(seed)
        record = {**prefix, "status": "", "citation_count": "", "reference_count": "", "related_count": "", "error": ""}
        try:
            citations = fetch_relation_rows(
                client, seed["paperId"], "citations", "citingPaper", "citation"
            )
            references = fetch_relation_rows(
                client, seed["paperId"], "references", "citedPaper", "reference"
            )
            for row in citations + references:
                all_edges.append({**prefix, **row})
            record.update(
                {
                    "status": "ok",
                    "citation_count": str(len(citations)),
                    "reference_count": str(len(references)),
                    "related_count": str(len(citations) + len(references)),
                }
            )
            print(
                f"[{index}/{len(seeds)}] ok rank={seed['rank']} "
                f"citations={len(citations)} references={len(references)} "
                f"{seed['title'][:80]}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            record.update({"status": "error", "error": str(exc)})
            print(f"[{index}/{len(seeds)}] error rank={seed['rank']}: {exc}", flush=True)
        manifest.append(record)

    write_csv(Path(args.output_edges), all_edges, EDGE_COLUMNS)
    write_csv(Path(args.output_manifest), manifest, MANIFEST_COLUMNS)
    print(f"selected={len(seeds)}")
    print(f"edges={len(all_edges)}")
    print(f"manifest_status={dict(Counter(row['status'] for row in manifest))}")
    print(f"requests={client.request_count}")


if __name__ == "__main__":
    main()

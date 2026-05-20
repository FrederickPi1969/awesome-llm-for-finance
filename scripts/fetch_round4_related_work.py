#!/usr/bin/env python3
"""Fetch a fourth citation/reference expansion from strong round-3 candidates."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from fetch_round2_related_work import (
    EDGE_COLUMNS,
    MANIFEST_COLUMNS,
    SemanticScholarClient,
    fetch_relation_rows,
    load_api_keys,
    to_int,
    write_csv,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "processed" / "round3_expansion_candidates.csv"
DEFAULT_CURATED = ROOT / "data" / "processed" / "curated_papers.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "round4_related_work_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "round4_related_work_manifest.csv"

FINANCE_TITLE_TERMS = [
    "finance",
    "financial",
    "stock",
    "investment",
    "invest",
    "trading",
    "market",
    "equity",
    "portfolio",
    "accounting",
    "credit",
    "bond",
    "asset",
    "robo-advisory",
]

LLM_TITLE_TERMS = [
    "large language",
    "llm",
    "gpt",
    "chatgpt",
    "finbert",
    "bondbert",
    "rag",
    "retrieval",
    "agent",
    "generative ai",
    "foundation model",
    "language model",
    "benchmark",
    "reasoning",
]

EXCLUDE_TITLE_TERMS = [
    "good debt or bad debt",
    "finrl",
    "deep reinforcement learning framework",
    "financial reinforcement learning",
]


def norm(value: str) -> str:
    return " ".join((value or "").lower().split())


def load_existing_curated(path: Path) -> tuple[set[str], set[str]]:
    if not path.exists():
        return set(), set()
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    titles = {norm(row.get("title", "")) for row in rows if row.get("title")}
    paper_ids = {row.get("paperId", "") for row in rows if row.get("paperId")}
    return titles, paper_ids


def select_round4_seeds(
    rows: list[dict[str, str]], curated_titles: set[str], curated_ids: set[str], limit: int
) -> list[dict[str, str]]:
    selected = []
    for row in rows:
        title = (row.get("title") or "").lower()
        title_key = norm(row.get("title", ""))
        paper_id = row.get("paperId", "")
        year = to_int(row.get("year", "0"))
        citations = to_int(row.get("citationCount", "0"))
        hits = to_int(row.get("seed_hit_count", "0"))
        rank = to_int(row.get("rank", "9999"))

        if rank > 120 or not paper_id:
            continue
        if title_key in curated_titles or paper_id in curated_ids:
            continue
        if any(term in title for term in EXCLUDE_TITLE_TERMS):
            continue
        if not any(term in title for term in FINANCE_TITLE_TERMS):
            continue
        if not any(term in title for term in LLM_TITLE_TERMS):
            continue
        if year < 2024 and citations < 25:
            continue
        if hits < 2 and citations < 10:
            continue
        selected.append(row)
        if len(selected) >= limit:
            break
    return selected


def source_prefix(row: dict[str, str], index: int) -> dict[str, str]:
    return {
        "source_round": "round4",
        "source_rank": str(index),
        "source_title": row.get("title", ""),
        "source_year": row.get("year", ""),
        "source_category": row.get("category", ""),
        "source_score": row.get("score", ""),
        "source_citationCount": row.get("citationCount", ""),
        "source_seed_hit_count": row.get("seed_hit_count", ""),
        "source_paperId": row.get("paperId", ""),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--curated", default=str(DEFAULT_CURATED))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    with Path(args.input).open(newline="", encoding="utf-8-sig") as f:
        candidates = list(csv.DictReader(f))
    curated_titles, curated_ids = load_existing_curated(Path(args.curated))
    seeds = select_round4_seeds(candidates, curated_titles, curated_ids, args.limit)
    client = SemanticScholarClient(load_api_keys(Path(args.api_keys_file)), args.min_interval_seconds)

    all_edges: list[dict[str, str]] = []
    manifest: list[dict[str, str]] = []
    for index, seed in enumerate(seeds, start=1):
        prefix = source_prefix(seed, index)
        record = {
            **prefix,
            "status": "",
            "citation_count": "",
            "reference_count": "",
            "related_count": "",
            "error": "",
        }
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
                f"[{index}/{len(seeds)}] ok citations={len(citations)} "
                f"references={len(references)} {seed['title'][:80]}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            record.update({"status": "error", "error": str(exc)})
            print(f"[{index}/{len(seeds)}] error {seed['title'][:80]}: {exc}", flush=True)
        manifest.append(record)

    write_csv(Path(args.output_edges), all_edges, EDGE_COLUMNS)
    write_csv(Path(args.output_manifest), manifest, MANIFEST_COLUMNS)
    print(f"selected={len(seeds)}")
    print(f"edges={len(all_edges)}")
    print(f"requests={client.request_count}")


if __name__ == "__main__":
    main()

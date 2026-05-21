#!/usr/bin/env python3
"""Focused citation/reference expansion from the highest-cited trading agent paper."""

from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
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
DEFAULT_CURATED_TAXONOMY = ROOT / "data" / "processed" / "curated_papers_by_taxonomy.csv"
DEFAULT_FIRST_ROUND_EDGES = ROOT / "data" / "raw" / "semantic_scholar_related_work_edges.csv"
DEFAULT_OUTPUT_SEEDS = ROOT / "data" / "processed" / "trading_agent_focus_finmem_seed_candidates.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "trading_agent_focus_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "trading_agent_focus_manifest.csv"

TRADING_TERMS = [
    "trading",
    "trade",
    "stock",
    "market",
    "investment",
    "investor",
    "portfolio",
    "alpha",
    "quant",
    "quantitative",
    "asset",
    "equity",
    "crypto",
    "forex",
    "earnings",
    "financial",
    "finance",
]

AGENT_LLM_TERMS = [
    "agent",
    "agents",
    "multi-agent",
    "agentic",
    "large language",
    "llm",
    "gpt",
    "language model",
    "generative ai",
    "foundation model",
]

EXCLUDE_TITLE_TERMS = [
    "prompt injection",
    "security bench",
    "security risks",
    "attacks and defenses",
    "personal finances",
    "consumer choice",
    "good debt or bad debt",
    "finrl",
    "deep reinforcement learning framework",
    "deep reinforcement learning library",
    "moving average",
    "macd",
]

CANDIDATE_COLUMNS = [
    "rank",
    "title",
    "year",
    "category",
    "score",
    "citationCount",
    "seed_hit_count",
    "seed_citation_hits",
    "seed_reference_hits",
    "influential_edge_hits",
    "venue",
    "authors",
    "doi",
    "arxiv",
    "url",
    "paperId",
    "matched_seed_ids",
    "matched_seed_titles",
    "finance_terms",
    "model_terms",
    "abstract",
]


def norm(value: str) -> str:
    return " ".join((value or "").lower().split())


def has_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in terms)


def matched_terms(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    return sorted({term for term in terms if term in lowered})


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def find_focus_anchor(rows: list[dict[str, str]]) -> dict[str, str]:
    candidates = []
    for row in rows:
        if row.get("taxonomy_category") != "Agents and Multi-Agent Systems":
            continue
        title = row.get("title", "").lower()
        if not has_any(title, ["trading", "trade", "stock", "investment", "portfolio", "market"]):
            continue
        candidates.append(row)
    if not candidates:
        raise RuntimeError("No trading-agent anchor found in taxonomy CSV")
    return max(candidates, key=lambda row: to_int(row.get("citationCount", "0")))


def existing_keys(rows: list[dict[str, str]]) -> tuple[set[str], set[str]]:
    titles = {norm(row.get("title", "")) for row in rows if row.get("title")}
    paper_ids = {row.get("paperId", "") for row in rows if row.get("paperId")}
    return titles, paper_ids


def candidate_category(row: dict[str, str]) -> str:
    title = row.get("title", "").lower()
    if "survey" in title or "review" in title:
        return "Surveys"
    if "rag" in title or "retrieval" in title:
        return "RAG and search"
    if "benchmark" in title or "eval" in title:
        return "Benchmarks and datasets"
    if has_any(title, ["agent", "agents", "multi-agent", "agentic"]):
        return "Financial agents"
    return "Trading and investment"


def build_focus_seed_candidates(
    anchor: dict[str, str],
    edges: list[dict[str, str]],
    existing_titles: set[str],
    existing_ids: set[str],
    limit: int,
) -> list[dict[str, str]]:
    rows = []
    anchor_title = anchor["title"]
    for edge in edges:
        if edge.get("source_title") != anchor_title:
            continue
        title = edge.get("title", "")
        title_key = norm(title)
        paper_id = edge.get("paperId", "")
        if not title_key or title_key in existing_titles or (paper_id and paper_id in existing_ids):
            continue
        title_lower = title.lower()
        text = f"{title} {edge.get('abstract', '')}"
        if any(term in title_lower for term in EXCLUDE_TITLE_TERMS):
            continue
        if not has_any(title_lower, TRADING_TERMS):
            continue
        if not has_any(title_lower, AGENT_LLM_TERMS):
            continue
        year = to_int(edge.get("year", "0"))
        citations = to_int(edge.get("citationCount", "0"))
        if year and year < 2024:
            continue
        trading_matches = matched_terms(title, TRADING_TERMS)
        model_matches = matched_terms(title, AGENT_LLM_TERMS)
        recency_bonus = 4 if year >= 2025 else 2
        relation_bonus = 2 if edge.get("citation_or_reference") == "citation" else 0.5
        score = math.log10(citations + 1) * 3 + len(trading_matches) * 2 + len(model_matches) * 2 + recency_bonus + relation_bonus
        rows.append(
            {
                "title": " ".join(title.split()),
                "year": edge.get("year", ""),
                "category": candidate_category(edge),
                "score": f"{score:.2f}",
                "citationCount": edge.get("citationCount", ""),
                "seed_hit_count": "1",
                "seed_citation_hits": "1" if edge.get("citation_or_reference") == "citation" else "0",
                "seed_reference_hits": "1" if edge.get("citation_or_reference") == "reference" else "0",
                "influential_edge_hits": "1" if edge.get("isInfluential") == "True" else "0",
                "venue": edge.get("venue", ""),
                "authors": edge.get("authors", ""),
                "doi": edge.get("doi", ""),
                "arxiv": edge.get("arxiv", ""),
                "url": edge.get("url", ""),
                "paperId": paper_id,
                "matched_seed_ids": "FINMEM-1",
                "matched_seed_titles": anchor_title,
                "finance_terms": "; ".join(trading_matches),
                "model_terms": "; ".join(model_matches),
                "abstract": edge.get("abstract", ""),
            }
        )
    rows.sort(
        key=lambda row: (
            -float(row["score"]),
            -to_int(row.get("citationCount", "0")),
            row.get("title", "").lower(),
        )
    )
    for rank, row in enumerate(rows[:limit], start=1):
        row["rank"] = str(rank)
    return rows[:limit]


def source_prefix(row: dict[str, str]) -> dict[str, str]:
    return {
        "source_round": "trading_agent_focus",
        "source_rank": row.get("rank", ""),
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
    parser.add_argument("--curated-taxonomy", default=str(DEFAULT_CURATED_TAXONOMY))
    parser.add_argument("--first-round-edges", default=str(DEFAULT_FIRST_ROUND_EDGES))
    parser.add_argument("--output-seeds", default=str(DEFAULT_OUTPUT_SEEDS))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--limit", type=int, default=14)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    taxonomy_rows = load_csv(Path(args.curated_taxonomy))
    anchor = find_focus_anchor(taxonomy_rows)
    curated_titles, curated_ids = existing_keys(taxonomy_rows)
    first_round_edges = load_csv(Path(args.first_round_edges))
    seeds = build_focus_seed_candidates(
        anchor, first_round_edges, curated_titles, curated_ids, args.limit
    )
    write_csv(Path(args.output_seeds), seeds, CANDIDATE_COLUMNS)

    client = SemanticScholarClient(load_api_keys(Path(args.api_keys_file)), args.min_interval_seconds)
    all_edges: list[dict[str, str]] = []
    manifest: list[dict[str, str]] = []
    for index, seed in enumerate(seeds, start=1):
        prefix = source_prefix(seed)
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
                f"references={len(references)} {seed['title'][:90]}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            record.update({"status": "error", "error": str(exc)})
            print(f"[{index}/{len(seeds)}] error {seed['title'][:90]}: {exc}", flush=True)
        manifest.append(record)

    write_csv(Path(args.output_edges), all_edges, EDGE_COLUMNS)
    write_csv(Path(args.output_manifest), manifest, MANIFEST_COLUMNS)
    print(f"anchor={anchor['title']}")
    print(f"selected={len(seeds)}")
    print(f"edges={len(all_edges)}")
    print(f"manifest_status={dict(Counter(row['status'] for row in manifest))}")
    print(f"requests={client.request_count}")


if __name__ == "__main__":
    main()

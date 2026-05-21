#!/usr/bin/env python3
"""Focused citation/reference expansion for financial report analysis work."""

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
DEFAULT_OUTPUT_SEEDS = ROOT / "data" / "processed" / "report_analysis_focus_seed_candidates.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "report_analysis_focus_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "report_analysis_focus_manifest.csv"

INPUT_EDGE_PATHS = [
    ROOT / "data" / "raw" / "semantic_scholar_related_work_edges.csv",
    ROOT / "data" / "raw" / "round2_related_work_edges.csv",
]

ANCHOR_TITLES = {
    "Financial Statement Analysis with Large Language Models",
    "Financial Report Chunking for Effective Retrieval Augmented Generation",
    "DocFinQA: A Long-Context Financial Reasoning Dataset",
    "SEC-QA: A Systematic Benchmark for Evaluating Long-Context Question Answering on SEC Filings",
    "SECQUE: A Benchmark for Evaluating Question-Answering on SEC Filings",
    "Fin-RATE: Financial Report Analytics and Tracking Evaluation for Large Language Models",
    "FinRpt: Financial Report Understanding and Generation Benchmark",
    "XBRL Agent: Leveraging Large Language Models for Financial Report Analysis",
}

REPORT_TERMS = [
    "financial statement",
    "financial statements",
    "annual report",
    "annual reports",
    "financial report",
    "financial reports",
    "earnings report",
    "earnings reports",
    "earnings call",
    "earnings calls",
    "10-k",
    "10-q",
    "sec filing",
    "sec filings",
    "filing",
    "filings",
    "xbrl",
    "disclosure",
    "disclosures",
    "accounting",
    "audit",
    "fundamental analysis",
    "balance sheet",
    "income statement",
    "cash flow",
    "md&a",
    "edgar",
]

LLM_TERMS = [
    "large language",
    "llm",
    "gpt",
    "chatgpt",
    "language model",
    "generative ai",
    "foundation model",
    "rag",
    "retrieval",
    "question answering",
    "qa",
    "reasoning",
    "benchmark",
    "agent",
]

EXCLUDE_TITLE_TERMS = [
    "flashattention",
    "technical analysis of the financial markets",
    "finrl",
    "reinforcement learning library",
    "consumer choice",
    "personal finances",
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
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


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
    if "question answering" in title or " qa" in title or "reasoning" in title:
        return "Benchmarks and datasets"
    if "xbrl" in title or "tag" in title:
        return "Reports, filings, and risk"
    return "Reports, filings, and risk"


def build_focus_seed_candidates(
    edges: list[dict[str, str]],
    existing_titles: set[str],
    existing_ids: set[str],
    limit: int,
) -> list[dict[str, str]]:
    grouped: dict[str, dict[str, object]] = {}
    for edge in edges:
        if edge.get("source_title") not in ANCHOR_TITLES:
            continue
        title = " ".join(edge.get("title", "").split())
        title_key = norm(title)
        paper_id = edge.get("paperId", "")
        if not title_key or title_key in existing_titles or (paper_id and paper_id in existing_ids):
            continue
        title_lower = title.lower()
        text = f"{title} {edge.get('abstract', '')}"
        if any(term in title_lower for term in EXCLUDE_TITLE_TERMS):
            continue
        if not has_any(text, REPORT_TERMS):
            continue
        if not has_any(text, LLM_TERMS):
            continue
        year = to_int(edge.get("year", "0"))
        citations = to_int(edge.get("citationCount", "0"))
        if year and year < 2023 and citations < 25:
            continue
        key = paper_id or title_key
        if key not in grouped:
            grouped[key] = {
                "base": edge,
                "source_titles": set(),
                "relations": Counter(),
                "influential_hits": 0,
            }
        item = grouped[key]
        item["source_titles"].add(edge.get("source_title", ""))  # type: ignore[union-attr]
        item["relations"][edge.get("citation_or_reference", "")] += 1  # type: ignore[index]
        if edge.get("isInfluential") == "True":
            item["influential_hits"] = int(item["influential_hits"]) + 1

    rows = []
    for item in grouped.values():
        edge = item["base"]
        if not isinstance(edge, dict):
            continue
        title = " ".join(edge.get("title", "").split())
        text = f"{title} {edge.get('abstract', '')}"
        year = to_int(edge.get("year", "0"))
        citations = to_int(edge.get("citationCount", "0"))
        report_matches = matched_terms(text, REPORT_TERMS)
        model_matches = matched_terms(text, LLM_TERMS)
        relations = item["relations"]
        if not isinstance(relations, Counter):
            relations = Counter()
        hit_count = len(item["source_titles"])  # type: ignore[arg-type]
        recency_bonus = 4 if year >= 2025 else 2 if year >= 2023 else 0
        score = (
            math.log10(citations + 1) * 3
            + len(report_matches) * 2
            + len(model_matches) * 2
            + hit_count * 3
            + recency_bonus
            + relations.get("citation", 0) * 2
            + relations.get("reference", 0) * 0.5
            + int(item["influential_hits"]) * 1.5
        )
        rows.append(
            {
                "title": title,
                "year": edge.get("year", ""),
                "category": candidate_category(edge),
                "score": f"{score:.2f}",
                "citationCount": edge.get("citationCount", ""),
                "seed_hit_count": str(hit_count),
                "seed_citation_hits": str(relations.get("citation", 0)),
                "seed_reference_hits": str(relations.get("reference", 0)),
                "influential_edge_hits": str(item["influential_hits"]),
                "venue": edge.get("venue", ""),
                "authors": edge.get("authors", ""),
                "doi": edge.get("doi", ""),
                "arxiv": edge.get("arxiv", ""),
                "url": edge.get("url", ""),
                "paperId": edge.get("paperId", ""),
                "matched_seed_ids": "REPORT-ANALYSIS-FOCUS",
                "matched_seed_titles": "; ".join(sorted(item["source_titles"])),  # type: ignore[arg-type]
                "finance_terms": "; ".join(report_matches),
                "model_terms": "; ".join(model_matches),
                "abstract": edge.get("abstract", ""),
            }
        )

    rows.sort(
        key=lambda row: (
            -float(row["score"]),
            -to_int(row.get("seed_hit_count", "0")),
            -to_int(row.get("citationCount", "0")),
            row.get("title", "").lower(),
        )
    )
    for rank, row in enumerate(rows[:limit], start=1):
        row["rank"] = str(rank)
    return rows[:limit]


def source_prefix(row: dict[str, str]) -> dict[str, str]:
    return {
        "source_round": "report_analysis_focus",
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
    parser.add_argument("--output-seeds", default=str(DEFAULT_OUTPUT_SEEDS))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--limit", type=int, default=16)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    taxonomy_rows = load_csv(Path(args.curated_taxonomy))
    curated_titles, curated_ids = existing_keys(taxonomy_rows)
    edges: list[dict[str, str]] = []
    for path in INPUT_EDGE_PATHS:
        edges.extend(load_csv(path))
    seeds = build_focus_seed_candidates(edges, curated_titles, curated_ids, args.limit)
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
    print(f"anchors={len(ANCHOR_TITLES)}")
    print(f"selected={len(seeds)}")
    print(f"edges={len(all_edges)}")
    print(f"manifest_status={dict(Counter(row['status'] for row in manifest))}")
    print(f"requests={client.request_count}")


if __name__ == "__main__":
    main()

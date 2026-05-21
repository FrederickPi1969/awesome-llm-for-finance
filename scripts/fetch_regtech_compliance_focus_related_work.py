#!/usr/bin/env python3
"""Focused citation/reference expansion for RegTech, compliance, audit, and model risk."""

from __future__ import annotations

import argparse
import csv
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
DEFAULT_OUTPUT_ANCHORS = ROOT / "data" / "processed" / "regtech_compliance_focus_anchor_candidates.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "regtech_compliance_focus_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "regtech_compliance_focus_manifest.csv"

ANCHOR_TITLES = {
    "Large Language Model in Financial Regulatory Interpretation",
    "Agentic AI Systems Applied to tasks in Financial Services: Modeling and model risk management crews",
    "Standard Benchmarks Fail -- Auditing LLM Agents in Finance Must Prioritize Risk",
    "FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs",
    "Automating Financial Statement Audits with Large Language Models",
    "Responsible Innovation: A Strategic Framework for Financial LLM Integration",
    "LLMs for Financial Advisement: A Fairness and Efficacy Study in Personal Decision Making",
    "FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain",
}

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


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def norm(value: str) -> str:
    return " ".join((value or "").lower().split())


def anchor_rows(curated_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    title_set = {norm(title) for title in ANCHOR_TITLES}
    rows = []
    seen = set()
    for row in curated_rows:
        title_key = norm(row.get("title", ""))
        if title_key not in title_set or not row.get("paperId") or row.get("paperId") in seen:
            continue
        seen.add(row["paperId"])
        rows.append(row)
    rows.sort(key=lambda row: (-to_int(row.get("citationCount", "0")), row.get("title", "")))
    for rank, row in enumerate(rows, start=1):
        row["rank"] = str(rank)
    return rows


def anchor_candidate_row(row: dict[str, str]) -> dict[str, str]:
    return {
        "rank": row.get("rank", ""),
        "title": row.get("title", ""),
        "year": row.get("approx_year", ""),
        "category": row.get("primary_category", ""),
        "score": "",
        "citationCount": row.get("citationCount", ""),
        "seed_hit_count": "",
        "seed_citation_hits": "",
        "seed_reference_hits": "",
        "influential_edge_hits": "",
        "venue": row.get("venue", ""),
        "authors": row.get("authors", ""),
        "doi": row.get("doi", ""),
        "arxiv": row.get("arxiv", ""),
        "url": row.get("source_url", ""),
        "paperId": row.get("paperId", ""),
        "matched_seed_ids": "REGTECH-COMPLIANCE-ANCHOR",
        "matched_seed_titles": row.get("title", ""),
        "finance_terms": "regtech; compliance; audit; model risk; financial regulation",
        "model_terms": "large language model; llm; agent; benchmark",
        "abstract": row.get("abstract", ""),
    }


def source_prefix(row: dict[str, str]) -> dict[str, str]:
    return {
        "source_round": "regtech_compliance_focus",
        "source_rank": row.get("rank", ""),
        "source_title": row.get("title", ""),
        "source_year": row.get("approx_year", ""),
        "source_category": row.get("primary_category", ""),
        "source_score": "",
        "source_citationCount": row.get("citationCount", ""),
        "source_seed_hit_count": "",
        "source_paperId": row.get("paperId", ""),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--curated-taxonomy", default=str(DEFAULT_CURATED_TAXONOMY))
    parser.add_argument("--output-anchors", default=str(DEFAULT_OUTPUT_ANCHORS))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    anchors = anchor_rows(load_csv(Path(args.curated_taxonomy)))
    write_csv(Path(args.output_anchors), [anchor_candidate_row(row) for row in anchors], CANDIDATE_COLUMNS)

    client = SemanticScholarClient(load_api_keys(Path(args.api_keys_file)), args.min_interval_seconds)
    all_edges: list[dict[str, str]] = []
    manifest: list[dict[str, str]] = []
    for index, anchor in enumerate(anchors, start=1):
        prefix = source_prefix(anchor)
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
                client, anchor["paperId"], "citations", "citingPaper", "citation"
            )
            references = fetch_relation_rows(
                client, anchor["paperId"], "references", "citedPaper", "reference"
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
                f"[{index}/{len(anchors)}] ok citations={len(citations)} "
                f"references={len(references)} {anchor['title'][:90]}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            record.update({"status": "error", "error": str(exc)})
            print(f"[{index}/{len(anchors)}] error {anchor['title'][:90]}: {exc}", flush=True)
        manifest.append(record)

    write_csv(Path(args.output_edges), all_edges, EDGE_COLUMNS)
    write_csv(Path(args.output_manifest), manifest, MANIFEST_COLUMNS)
    print(f"selected={len(anchors)}")
    print(f"edges={len(all_edges)}")
    print(f"manifest_status={dict(Counter(row['status'] for row in manifest))}")
    print(f"requests={client.request_count}")


if __name__ == "__main__":
    main()

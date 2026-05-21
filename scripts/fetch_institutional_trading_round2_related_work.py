#!/usr/bin/env python3
"""Second focused expansion for institutional trading and investment papers."""

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
DEFAULT_CURATED = ROOT / "data" / "processed" / "curated_papers.csv"
DEFAULT_OUTPUT_ANCHORS = ROOT / "data" / "processed" / "institutional_trading_round2_anchor_candidates.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "institutional_trading_round2_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "institutional_trading_round2_manifest.csv"

ANCHOR_TITLES = {
    "From Natural Language to Executable Option Strategies via Large Language Models",
    "Dynamic Hedging Strategies in Derivatives Markets with LLM-Driven Sentiment and News Analytics",
    "StockSim: A Dual-Mode Order-Level Simulator for Evaluating Multi-Agent LLMs in Financial Markets",
    "PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage",
    "Can large language models effectively process and execute financial trading instructions?",
    "QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies",
    "AlphaForgeBench: Benchmarking End-to-End Trading Strategy Design with Large Language Models",
    "PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data",
    "The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction",
    "A Multi-Agent Orchestration Framework for Venture Capital Due Diligence",
    "Application of Startup Success Prediction Models and Business Document Extraction Using Large Language Models to Enhance Due Diligence Efficiency",
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


def norm(value: str) -> str:
    return " ".join((value or "").lower().split())


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def anchor_rows(curated_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    title_set = {norm(title) for title in ANCHOR_TITLES}
    rows = []
    seen = set()
    for row in curated_rows:
        title_key = norm(row.get("title", ""))
        paper_id = row.get("paperId", "")
        if title_key not in title_set or not paper_id or paper_id in seen:
            continue
        seen.add(paper_id)
        rows.append(dict(row))
    rows.sort(key=lambda row: (-to_int(row.get("citationCount", "0")), row.get("title", "")))
    for rank, row in enumerate(rows, start=1):
        row["round2_anchor_rank"] = str(rank)
    return rows


def anchor_candidate_row(row: dict[str, str]) -> dict[str, str]:
    return {
        "rank": row.get("round2_anchor_rank", ""),
        "title": row.get("title", ""),
        "year": row.get("approx_year", ""),
        "category": row.get("primary_category", ""),
        "score": row.get("score", ""),
        "citationCount": row.get("citationCount", ""),
        "seed_hit_count": row.get("seed_hit_count", ""),
        "seed_citation_hits": "",
        "seed_reference_hits": "",
        "influential_edge_hits": "",
        "venue": row.get("venue", ""),
        "authors": row.get("authors", ""),
        "doi": row.get("doi", ""),
        "arxiv": row.get("arxiv", ""),
        "url": row.get("source_url", ""),
        "paperId": row.get("paperId", ""),
        "matched_seed_ids": "INSTITUTIONAL-TRADING-ROUND2-ANCHOR",
        "matched_seed_titles": row.get("title", ""),
        "finance_terms": "options; derivatives; hedging; execution; order book; venture capital; due diligence",
        "model_terms": "large language model; llm; agent; benchmark; reasoning",
        "abstract": row.get("abstract", ""),
    }


def source_prefix(row: dict[str, str]) -> dict[str, str]:
    return {
        "source_round": "institutional_trading_round2",
        "source_rank": row.get("round2_anchor_rank", ""),
        "source_title": row.get("title", ""),
        "source_year": row.get("approx_year", ""),
        "source_category": row.get("primary_category", ""),
        "source_score": row.get("score", ""),
        "source_citationCount": row.get("citationCount", ""),
        "source_seed_hit_count": row.get("seed_hit_count", ""),
        "source_paperId": row.get("paperId", ""),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--curated", default=str(DEFAULT_CURATED))
    parser.add_argument("--output-anchors", default=str(DEFAULT_OUTPUT_ANCHORS))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    anchors = anchor_rows(load_csv(Path(args.curated)))
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

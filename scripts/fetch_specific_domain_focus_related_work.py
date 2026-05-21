#!/usr/bin/env python3
"""Focused search and citation/reference expansion for specific finance domains.

This pass targets narrower application areas that broad finance-LLM expansion
often misses: industry/sector analysis, investment research reports, supply
chain finance/risk, and ETF/asset-allocation workflows.
"""

from __future__ import annotations

import argparse
import csv
import math
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from fetch_round2_related_work import (
    BASE_URL,
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
DEFAULT_OUTPUT_SEARCH = ROOT / "data" / "processed" / "specific_domain_focus_search_candidates.csv"
DEFAULT_OUTPUT_EDGES = ROOT / "data" / "raw" / "specific_domain_focus_edges.csv"
DEFAULT_OUTPUT_MANIFEST = ROOT / "data" / "raw" / "specific_domain_focus_manifest.csv"

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

SEARCH_QUERIES = [
    # Industry / sector / investment research reports.
    "large language models financial industry analysis",
    "large language models sector analysis finance",
    "large language models investment research reports finance",
    "large language models market analysis investment reports",
    "large language models equity research financial analysis",
    "large language models fundamental analysis company analysis",
    "LLM based macro and sector asset allocation finance",
    "CN-Buzz2Portfolio Chinese-market dataset benchmark LLM macro sector asset allocation",
    "Commercial Real Estate AI Text-Evaluation CREATE large language model sector trading signal",
    # Supply chain finance and risk.
    "large language models supply chain finance",
    "large language models supply chain risk finance",
    "supply chain risk large language model annual reports",
    "Measuring Firm-Level Supply Chain Risk Using A Generative Large Language Model",
    "Supply Chain Risk Measurement and Resilience Insights from Large Language Models",
    "predicting repayment risk supply chain finance large language models",
    "LARD-SC large language model supply chain risk identification",
    # ETF and ETF-adjacent asset allocation.
    "large language models ETF finance",
    "large language models exchange traded fund finance",
    "FinBERT ETF financial returns SPY",
    "large language models ETF portfolio allocation",
    "LLM crowds investment signals S&P 500 ETF SPY",
]

DOMAIN_TERMS = {
    "industry_sector": [
        "industry analysis",
        "sector analysis",
        "sector",
        "industry",
        "equity research",
        "investment research",
        "research report",
        "market analysis",
        "company analysis",
        "fundamental analysis",
        "commercial real estate",
        "asset allocation",
        "macro",
    ],
    "supply_chain": [
        "supply chain",
        "supply-chain",
        "supply chain finance",
        "supply chain risk",
        "repayment risk",
        "firm-level supply chain",
        "resilience",
    ],
    "etf": [
        "etf",
        "exchange traded fund",
        "exchange-traded fund",
        "spy",
        "sector rotation",
        "portfolio allocation",
    ],
}

FINANCE_TERMS = [
    "finance",
    "financial",
    "investment",
    "investing",
    "market",
    "stock",
    "equity",
    "portfolio",
    "asset",
    "returns",
    "risk",
    "annual report",
    "quarterly report",
    "corporate",
    "company",
    "firm",
    "bank",
    "fund",
    "etf",
    "supply chain finance",
]

MODEL_TERMS = [
    "large language model",
    "large language models",
    "llm",
    "gpt",
    "chatgpt",
    "generative ai",
    "foundation model",
    "language model",
    "finbert",
    "bert",
    "rag",
    "retrieval",
    "agent",
    "benchmark",
    "prompt",
]

EXCLUDE_TITLE_TERMS = [
    "software supply chain",
    "package supply chain",
    "code generation",
    "blockchain-based supply chain finance",
    "medical",
    "healthcare",
    "education",
    "large language model market research report",
    "large language model market analysis",
    "global strategic business report",
]


def norm(value: str) -> str:
    return " ".join((value or "").lower().split())


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def external_id(paper: dict[str, Any], name: str) -> str:
    external = paper.get("externalIds") or {}
    return str(external.get(name) or "")


def authors_to_text(paper: dict[str, Any]) -> str:
    return "; ".join(
        author.get("name", "").strip()
        for author in paper.get("authors") or []
        if isinstance(author, dict) and author.get("name")
    )


def contains_terms(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    return sorted({term for term in terms if term in lowered})


def domain_hits(text: str) -> dict[str, list[str]]:
    return {domain: contains_terms(text, terms) for domain, terms in DOMAIN_TERMS.items()}


def category_for_text(text: str) -> str:
    hits = domain_hits(text)
    if hits["supply_chain"]:
        return "Supply chain finance and risk"
    if hits["etf"]:
        return "ETF and asset allocation"
    if hits["industry_sector"]:
        return "Industry, sector, and investment research"
    return "Specific finance domains"


def paper_url(paper: dict[str, Any]) -> str:
    if paper.get("url"):
        return str(paper["url"])
    arxiv = external_id(paper, "ArXiv")
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}"
    return ""


def search_papers(client: SemanticScholarClient, query: str, limit: int) -> list[dict[str, Any]]:
    fields = ",".join(
        [
            "paperId",
            "title",
            "year",
            "citationCount",
            "venue",
            "authors",
            "externalIds",
            "url",
            "abstract",
        ]
    )
    payload = client.get_json(
        "/paper/search",
        {"query": query, "limit": limit, "fields": fields},
    )
    return [paper for paper in payload.get("data") or [] if isinstance(paper, dict)]


def score_paper(paper: dict[str, Any], query_hits: int, matched_queries: list[str]) -> tuple[float, list[str], list[str], dict[str, list[str]]]:
    title = str(paper.get("title") or "")
    abstract = str(paper.get("abstract") or "")
    text = f"{title} {abstract}"
    title_lower = title.lower()
    finance_matches = contains_terms(text, FINANCE_TERMS)
    model_matches = contains_terms(text, MODEL_TERMS)
    hits = domain_hits(text)
    domain_match_count = sum(len(values) for values in hits.values())
    year = to_int(str(paper.get("year") or "0"))
    citations = to_int(str(paper.get("citationCount") or "0"))
    recency_bonus = 4 if year >= 2025 else 3 if year >= 2024 else 1 if year >= 2021 else 0
    title_bonus = 0
    if any(term in title_lower for term in ["supply chain", "sector", "industry", "etf", "investment research", "asset allocation"]):
        title_bonus += 4
    if any(term in title_lower for term in ["large language", "llm", "gpt", "generative ai", "finbert"]):
        title_bonus += 4
    score = (
        math.log10(citations + 1) * 2.0
        + query_hits * 2.0
        + len(finance_matches) * 1.1
        + len(model_matches) * 1.5
        + domain_match_count * 1.8
        + recency_bonus
        + title_bonus
    )
    if matched_queries:
        score += min(len(matched_queries), 4) * 0.8
    return score, finance_matches, model_matches, hits


def is_candidate(paper: dict[str, Any], finance_matches: list[str], model_matches: list[str], hits: dict[str, list[str]]) -> bool:
    title = str(paper.get("title") or "").lower()
    text = f"{title} {paper.get('abstract') or ''}".lower()
    year = to_int(str(paper.get("year") or "0"))
    if not paper.get("paperId") or not title:
        return False
    if any(term in title for term in EXCLUDE_TITLE_TERMS):
        return False
    if year and year < 2020:
        return False
    if not finance_matches:
        return False
    if not model_matches:
        return False
    if not any(hits.values()):
        return False
    # Avoid generic LLM market-size consulting reports; we want papers.
    if "large language model market" in text and "finance" not in text:
        return False
    return True


def candidate_row(
    paper: dict[str, Any],
    rank: int,
    score: float,
    finance_matches: list[str],
    model_matches: list[str],
    matched_queries: list[str],
    hits: dict[str, list[str]],
) -> dict[str, str]:
    title = str(paper.get("title") or "")
    abstract = str(paper.get("abstract") or "")
    text = f"{title} {abstract}"
    domains = [domain for domain, values in hits.items() if values]
    return {
        "rank": str(rank),
        "title": " ".join(title.split()),
        "year": str(paper.get("year") or ""),
        "category": category_for_text(text),
        "score": f"{score:.2f}",
        "citationCount": str(paper.get("citationCount") if paper.get("citationCount") is not None else ""),
        "seed_hit_count": str(len(matched_queries)),
        "seed_citation_hits": "0",
        "seed_reference_hits": "0",
        "influential_edge_hits": "0",
        "venue": str(paper.get("venue") or ""),
        "authors": authors_to_text(paper),
        "doi": external_id(paper, "DOI"),
        "arxiv": external_id(paper, "ArXiv"),
        "url": paper_url(paper),
        "paperId": str(paper.get("paperId") or ""),
        "matched_seed_ids": "; ".join(domains),
        "matched_seed_titles": "; ".join(matched_queries),
        "finance_terms": "; ".join(finance_matches),
        "model_terms": "; ".join(model_matches),
        "abstract": abstract,
    }


def source_prefix(row: dict[str, str]) -> dict[str, str]:
    return {
        "source_round": "specific_domain_focus",
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
    parser.add_argument("--curated", default=str(DEFAULT_CURATED))
    parser.add_argument("--output-search", default=str(DEFAULT_OUTPUT_SEARCH))
    parser.add_argument("--output-edges", default=str(DEFAULT_OUTPUT_EDGES))
    parser.add_argument("--output-manifest", default=str(DEFAULT_OUTPUT_MANIFEST))
    parser.add_argument("--api-keys-file", required=True)
    parser.add_argument("--search-limit-per-query", type=int, default=20)
    parser.add_argument("--anchor-limit", type=int, default=14)
    parser.add_argument("--min-interval-seconds", type=float, default=1.0)
    args = parser.parse_args()

    curated_titles = {norm(row.get("title", "")) for row in load_csv(Path(args.curated))}
    client = SemanticScholarClient(load_api_keys(Path(args.api_keys_file)), args.min_interval_seconds)

    grouped: dict[str, dict[str, Any]] = {}
    query_by_paper: dict[str, list[str]] = defaultdict(list)
    for query in SEARCH_QUERIES:
        for paper in search_papers(client, query, args.search_limit_per_query):
            paper_id = str(paper.get("paperId") or "")
            title_key = norm(str(paper.get("title") or ""))
            if not paper_id or title_key in curated_titles:
                continue
            if paper_id not in grouped:
                grouped[paper_id] = paper
            query_by_paper[paper_id].append(query)

    scored_rows: list[tuple[float, dict[str, str]]] = []
    for paper_id, paper in grouped.items():
        matched_queries = query_by_paper[paper_id]
        score, finance_matches, model_matches, hits = score_paper(paper, len(matched_queries), matched_queries)
        if not is_candidate(paper, finance_matches, model_matches, hits):
            continue
        scored_rows.append(
            (
                score,
                candidate_row(
                    paper,
                    0,
                    score,
                    finance_matches,
                    model_matches,
                    matched_queries,
                    hits,
                ),
            )
        )

    scored_rows.sort(
        key=lambda item: (
            -item[0],
            -to_int(item[1].get("citationCount", "0")),
            item[1].get("title", "").lower(),
        )
    )
    search_candidates = []
    for rank, (_, row) in enumerate(scored_rows, start=1):
        row["rank"] = str(rank)
        search_candidates.append(row)
    write_csv(Path(args.output_search), search_candidates, CANDIDATE_COLUMNS)

    anchors = search_candidates[: args.anchor_limit]
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
    print(f"queries={len(SEARCH_QUERIES)}")
    print(f"search_candidates={len(search_candidates)}")
    print(f"selected={len(anchors)}")
    print(f"edges={len(all_edges)}")
    print(f"manifest_status={dict(Counter(row['status'] for row in manifest))}")
    print(f"requests={client.request_count}")


if __name__ == "__main__":
    main()

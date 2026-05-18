#!/usr/bin/env python3
"""Build the initial Awesome LLM for Finance catalog artifacts."""

from __future__ import annotations

import csv
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEED_PATH = ROOT / "data" / "processed" / "seed_papers_enriched.csv"
EDGES_PATH = ROOT / "data" / "raw" / "semantic_scholar_related_work_edges.csv"
CANDIDATES_PATH = ROOT / "data" / "processed" / "expansion_candidates_preliminary.csv"
LONG_LIST_PATH = ROOT / "data" / "processed" / "related_work_relevance_longlist.csv"
README_PATH = ROOT / "README.md"
PLAN_PATH = ROOT / "docs" / "collection_plan.md"


STRONG_FINANCE_TERMS = [
    "finance",
    "financial",
    "stock",
    "equity",
    "investment",
    "investing",
    "trading",
    "market",
    "portfolio",
    "asset",
    "analyst",
    "bank",
    "banking",
    "credit",
    "sec",
    "10-k",
    "10-q",
    "edgar",
    "annual report",
    "earnings",
    "call transcript",
    "xbrl",
    "risk",
    "disclosure",
    "accounting",
    "corporate",
    "valuation",
    "cfa",
    "fund",
    "fintech",
]

WEAK_FINANCE_TERMS = [
    "risk",
    "market",
    "return",
    "returns",
    "volatility",
    "sentiment",
]

FINANCE_TERMS = STRONG_FINANCE_TERMS + WEAK_FINANCE_TERMS

MODEL_TERMS = [
    "large language model",
    "llm",
    "gpt",
    "chatgpt",
    "language model",
    "generative ai",
    "foundation model",
    "transformer",
    "bert",
    "finbert",
    "prompt",
    "instruction",
    "rag",
    "retrieval",
    "agent",
    "reasoning",
    "question answering",
    "qa",
    "benchmark",
    "dataset",
    "numerical reasoning",
    "natural language processing",
    "text mining",
]

GENERIC_FOUNDATION_TITLES = {
    "attention is all you need",
    "bert: pre-training of deep bidirectional transformers for language understanding",
    "language models are few-shot learners",
    "training language models to follow instructions with human feedback",
    "retrieval-augmented generation for knowledge-intensive nlp tasks",
    "adam: a method for stochastic optimization",
    "deep residual learning for image recognition",
}


def norm(value: str) -> str:
    return " ".join((value or "").lower().split())


def to_int(value: str, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def contains_any(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    matches = []
    for term in terms:
        pattern = rf"(?<![a-z0-9]){re.escape(term.lower())}(?![a-z0-9])"
        if re.search(pattern, lowered):
            matches.append(term)
    return matches


def category_for(row: dict[str, str]) -> str:
    text = f"{row.get('title', '')} {row.get('abstract', '')}".lower()
    title = row.get("title", "").lower()
    if "survey" in title:
        return "Surveys"
    if any(term in text for term in ["agent", "multi-agent", "autonomous"]):
        return "Financial agents"
    if any(term in text for term in ["trading", "stock", "portfolio", "investment", "return", "market"]):
        return "Trading and investment"
    if any(term in text for term in ["sec", "10-k", "10-q", "edgar", "xbrl", "disclosure", "annual report"]):
        return "Reports, filings, and risk"
    if any(term in text for term in ["benchmark", "dataset", "evaluation", "exam", "question answering", "qa"]):
        return "Benchmarks and datasets"
    if any(term in text for term in ["finbert", "fingpt", "bloomberggpt", "financial language model"]):
        return "Financial language models"
    return "Other relevant work"


def seed_category(seed: dict[str, str]) -> str:
    category = seed.get("primary_category", "")
    paper_type = seed.get("paper_type", "")
    text = f"{category} {paper_type} {seed.get('title', '')}".lower()
    if "survey" in text:
        return "Surveys"
    if any(term in text for term in ["benchmark", "dataset", "qa", "exam", "reasoning"]):
        return "Benchmarks and datasets"
    if "agent" in text:
        return "Financial agents"
    if any(term in text for term in ["trading", "stock", "investment", "portfolio", "allocation"]):
        return "Trading and investment"
    if any(term in text for term in ["sec", "xbrl", "risk", "report", "statement", "filing"]):
        return "Reports, filings, and risk"
    if "llm" in text or "model" in text:
        return "Financial language models"
    return "Other"


def markdown_link(title: str, url: str) -> str:
    return f"[{title}]({url})" if url else title


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def build_candidates(seeds: list[dict[str, str]], edges: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    seed_titles = {norm(row.get("title", "")) for row in seeds}
    seed_ids = {row.get("resolved_paperId", "") for row in seeds if row.get("resolved_paperId")}
    grouped: dict[str, dict[str, object]] = {}

    for edge in edges:
        title_key = norm(edge.get("title", ""))
        paper_id = edge.get("paperId", "")
        if not title_key:
            continue
        if title_key in seed_titles or (paper_id and paper_id in seed_ids):
            continue
        key = paper_id or title_key
        if key not in grouped:
            grouped[key] = {
                "base": edge,
                "source_titles": set(),
                "source_ids": set(),
                "relations": Counter(),
                "influential_hits": 0,
            }
        item = grouped[key]
        item["source_titles"].add(edge.get("source_title", ""))  # type: ignore[union-attr]
        item["source_ids"].add(edge.get("source_index", ""))  # type: ignore[union-attr]
        item["relations"][edge.get("citation_or_reference", "")] += 1  # type: ignore[index]
        if edge.get("isInfluential") == "True":
            item["influential_hits"] = int(item["influential_hits"]) + 1

    rows: list[dict[str, str]] = []
    for item in grouped.values():
        base = item["base"]  # type: ignore[assignment]
        if not isinstance(base, dict):
            continue
        text = f"{base.get('title', '')} {base.get('abstract', '')}"
        title_key = norm(base.get("title", ""))
        strong_finance_matches = contains_any(text, STRONG_FINANCE_TERMS)
        weak_finance_matches = contains_any(text, WEAK_FINANCE_TERMS)
        finance_matches = strong_finance_matches + weak_finance_matches
        model_matches = contains_any(text, MODEL_TERMS)
        hit_count = len(item["source_ids"])  # type: ignore[arg-type]
        citation_count = to_int(base.get("citationCount", "0"))
        year = to_int(base.get("year", "0"))
        finance_score = len(set(finance_matches))
        model_score = len(set(model_matches))

        title_finance_matches = contains_any(base.get("title", ""), STRONG_FINANCE_TERMS)
        is_relevant = bool(strong_finance_matches) and (
            bool(model_matches) or hit_count >= 2 or "sentiment" in finance_matches
        )
        if not title_finance_matches and len(set(strong_finance_matches)) < 2 and hit_count < 3:
            is_relevant = False
        if title_key in GENERIC_FOUNDATION_TITLES:
            is_relevant = False
        if not is_relevant:
            continue

        relation_counter = item["relations"]  # type: ignore[assignment]
        if not isinstance(relation_counter, Counter):
            relation_counter = Counter()
        recency_bonus = 3 if year >= 2023 else 1 if year >= 2020 else 0
        score = (
            math.log10(citation_count + 1) * 2.0
            + hit_count * 4.0
            + to_int(str(item["influential_hits"])) * 1.5
            + finance_score * 1.4
            + model_score * 1.0
            + recency_bonus
            + relation_counter.get("reference", 0) * 0.6
        )
        rows.append(
            {
                "title": base.get("title", ""),
                "year": base.get("year", ""),
                "citationCount": base.get("citationCount", ""),
                "venue": base.get("venue", ""),
                "authors": base.get("authors", ""),
                "doi": base.get("doi", ""),
                "arxiv": base.get("arxiv", ""),
                "url": base.get("url", ""),
                "abstract": base.get("abstract", ""),
                "category": category_for(base),
                "score": f"{score:.2f}",
                "seed_hit_count": str(hit_count),
                "seed_citation_hits": str(relation_counter.get("citation", 0)),
                "seed_reference_hits": str(relation_counter.get("reference", 0)),
                "influential_edge_hits": str(item["influential_hits"]),
                "matched_seed_ids": "; ".join(sorted(item["source_ids"], key=lambda x: to_int(x))),  # type: ignore[arg-type]
                "matched_seed_titles": "; ".join(sorted(item["source_titles"])),  # type: ignore[arg-type]
                "finance_terms": "; ".join(sorted(set(finance_matches))),
                "model_terms": "; ".join(sorted(set(model_matches))),
                "paperId": base.get("paperId", ""),
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
    for rank, row in enumerate(rows, start=1):
        row["rank"] = str(rank)
    return rows[:200], rows


def write_readme(seeds: list[dict[str, str]], candidates: list[dict[str, str]]) -> None:
    seed_by_category: dict[str, list[dict[str, str]]] = defaultdict(list)
    for seed in seeds:
        seed_by_category[seed_category(seed)].append(seed)

    category_order = [
        "Surveys",
        "Financial language models",
        "Benchmarks and datasets",
        "Reports, filings, and risk",
        "Trading and investment",
        "Financial agents",
        "Other",
    ]
    candidate_highlights = candidates[:40]

    lines = [
        "# Awesome LLM for Finance",
        "",
        "A curated reading list for large language models in finance: financial-domain LLMs, benchmarks, SEC filing analysis, financial reasoning, trading agents, investment research, and professional finance evaluation.",
        "",
        "> Status: preliminary public seed. The current catalog starts from 58 seed papers and one systematic Semantic Scholar pass over papers that cite them and papers they cite.",
        "",
        "## Data Files",
        "",
        "- `data/processed/seed_papers_enriched.csv`: seed papers with Semantic Scholar metadata, citation counts, links, and abstracts.",
        "- `data/processed/expansion_candidates_preliminary.csv`: top 200 candidate additions discovered from citation/reference expansion.",
        "- `data/processed/related_work_relevance_longlist.csv`: longer relevance-filtered candidate list for manual review.",
        "- `data/raw/semantic_scholar_related_work_edges.csv`: raw citation/reference edges from the first expansion pass.",
        "- `data/raw/semantic_scholar_manifest.csv`: per-seed retrieval status and edge counts.",
        "",
        "## Collection Method",
        "",
        "1. Start with the seed CSV in `data/raw/seed_papers_original.csv`.",
        "2. Resolve seed papers through Semantic Scholar, preferring arXiv ids when available.",
        "3. Fetch both citations and references for each resolved seed paper.",
        "4. Remove existing seed papers from the candidate pool.",
        "5. Rank candidate additions by finance/LLM relevance terms, number of seed-paper connections, citation count, influential-edge hits, and recency.",
        "",
        "See `docs/collection_plan.md` for the planned multi-round expansion workflow.",
        "",
        "## Seed Papers",
        "",
    ]

    for category in category_order:
        items = seed_by_category.get(category, [])
        if not items:
            continue
        lines.extend([f"### {category}", ""])
        for row in sorted(items, key=lambda x: (x.get("priority", "P9"), x.get("approx_year", ""), x.get("title", ""))):
            url = row.get("source_url") or row.get("semantic_scholar_url")
            year = row.get("approx_year") or row.get("resolved_year")
            citation = row.get("citationCount") or "n/a"
            short = row.get("short_name") or row.get("title")
            lines.append(
                f"- {markdown_link(row.get('title', ''), url)} ({year}) "
                f"- `{row.get('priority', '')}` - citations: {citation} - {short}"
            )
        lines.append("")

    lines.extend(["## Preliminary Candidate Additions", ""])
    for row in candidate_highlights:
        url = row.get("url")
        arxiv = row.get("arxiv")
        if not url and arxiv:
            url = f"https://arxiv.org/abs/{arxiv}"
        lines.append(
            f"- {markdown_link(row.get('title', ''), url)} ({row.get('year', 'n.d.')}) "
            f"- {row.get('category')} - citations: {row.get('citationCount', '0')} "
            f"- seed hits: {row.get('seed_hit_count')}"
        )
    lines.extend(
        [
            "",
            "## Contributing",
            "",
            "Open an issue or pull request with title, year, link, category, and a short note explaining why the paper belongs in the list. High-signal additions should either be finance-specific LLM work, a core financial NLP benchmark/dataset, or a highly cited foundation paper directly used by multiple finance LLM papers.",
            "",
            "## Attribution",
            "",
            "Paper metadata in `data/` was collected from the seed CSV and the Semantic Scholar Graph API. Abstracts and third-party metadata remain subject to their original rights and provider terms.",
            "",
        ]
    )
    README_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_plan() -> None:
    PLAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    PLAN_PATH.write_text(
        """# Collection Plan

## Objective

Build a high-impact public Awesome-style repository for Large Language Models in Finance.

## Round 0: Seed Consolidation

- Normalize the original seed CSV.
- Resolve each seed paper against Semantic Scholar.
- Store citation counts, venues, authors, URLs, and abstracts.
- Keep unresolved/manual-check rows instead of dropping them.

## Round 1: Citation and Reference Expansion

- For each resolved seed, collect papers that cite it and papers it references.
- Aggregate duplicate papers across all seeds.
- Score candidates using seed hit count, citation count, influential edge hits, finance/LLM keyword evidence, and recency.
- Export a preliminary top-200 candidate CSV for manual review.

## Round 2: Manual Curation

- Promote true finance-specific LLM papers into the main README.
- Split generic foundation-model papers into a background section only when they are repeatedly cited by the finance LLM literature.
- Check abstracts and titles for false positives, especially generic NLP, vision, and optimization papers.

## Round 3: Deeper Expansion

- Re-run citation/reference expansion on accepted candidate additions.
- Add venue, code, dataset, model, benchmark, and task tags.
- Add GitHub/model/dataset links where available.
- Create issue templates for community submissions.

## Review Criteria

- Direct relevance to LLMs, foundation models, agents, or language-centric reasoning in finance.
- Finance-specific datasets, benchmarks, or evaluation protocols.
- High citation count or repeated appearance across multiple seed-paper neighborhoods.
- Practical importance for a repository reader building systems for SEC filings, financial QA, trading, research reports, risk analytics, or professional finance reasoning.
""",
        encoding="utf-8",
    )


def main() -> None:
    seeds = read_csv(SEED_PATH)
    edges = read_csv(EDGES_PATH)
    candidates, longlist = build_candidates(seeds, edges)
    columns = [
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
    write_csv(CANDIDATES_PATH, candidates, columns)
    write_csv(LONG_LIST_PATH, longlist, columns)
    write_readme(seeds, candidates)
    write_plan()
    print(f"seeds={len(seeds)}")
    print(f"edges={len(edges)}")
    print(f"candidates={len(candidates)}")
    print(f"longlist={len(longlist)}")
    print(f"wrote={CANDIDATES_PATH}")


if __name__ == "__main__":
    main()

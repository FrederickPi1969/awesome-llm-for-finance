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
ROUND2_EDGES_PATH = ROOT / "data" / "raw" / "round2_related_work_edges.csv"
ROUND2_MANIFEST_PATH = ROOT / "data" / "raw" / "round2_related_work_manifest.csv"
CANDIDATES_PATH = ROOT / "data" / "processed" / "expansion_candidates_preliminary.csv"
LONG_LIST_PATH = ROOT / "data" / "processed" / "related_work_relevance_longlist.csv"
ROUND2_CANDIDATES_PATH = ROOT / "data" / "processed" / "round2_expansion_candidates.csv"
CURATED_PATH = ROOT / "data" / "processed" / "curated_papers.csv"
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
    "regulatory",
    "regulation",
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
    if any(term in text for term in ["finbert", "fingpt", "bloomberggpt", "finllm", "financial language model", "financial chat model", "financial assistant"]):
        return "Financial language models"
    if any(term in text for term in ["agent", "multi-agent", "autonomous"]):
        return "Financial agents"
    if any(term in text for term in ["trading", "stock", "portfolio", "investment", "return", "market"]):
        return "Trading and investment"
    if any(term in text for term in ["sec", "10-k", "10-q", "edgar", "xbrl", "disclosure", "annual report"]):
        return "Reports, filings, and risk"
    if any(term in text for term in ["benchmark", "dataset", "evaluation", "exam", "question answering", "qa"]):
        return "Benchmarks and datasets"
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
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def normalize_round2_edges(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized = []
    for row in rows:
        normalized.append(
            {
                "source_index": f"R2-{row.get('source_rank', '')}",
                "source_signature": f"round2:{row.get('source_paperId', '')}",
                "source_title": row.get("source_title", ""),
                "source_year": row.get("source_year", ""),
                "source_domain": row.get("source_category", ""),
                "source_tag": "round2",
                "resolved_source_paperId": row.get("source_paperId", ""),
                "resolved_source_title": row.get("source_title", ""),
                "output_csv": "round2_related_work_edges.csv",
                "paperId": row.get("paperId", ""),
                "title": row.get("title", ""),
                "year": row.get("year", ""),
                "citationCount": row.get("citationCount", ""),
                "venue": row.get("venue", ""),
                "authors": row.get("authors", ""),
                "doi": row.get("doi", ""),
                "arxiv": row.get("arxiv", ""),
                "url": row.get("url", ""),
                "abstract": row.get("abstract", ""),
                "intents": row.get("intents", ""),
                "isInfluential": row.get("isInfluential", ""),
                "citation_or_reference": row.get("citation_or_reference", ""),
            }
        )
    return normalized


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


def round2_manifest_as_seed_rows(manifest_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in manifest_rows:
        if row.get("status") != "ok":
            continue
        rows.append(
            {
                "title": row.get("source_title", ""),
                "resolved_title": row.get("source_title", ""),
                "resolved_paperId": row.get("source_paperId", ""),
            }
        )
    return rows


def priority_for(row: dict[str, str]) -> str:
    citations = to_int(row.get("citationCount", "0"))
    score = float(row.get("score", "0") or 0)
    hits = to_int(row.get("seed_hit_count", "0"))
    year = to_int(row.get("year", "0"))
    if citations >= 100 or score >= 60 or hits >= 10:
        return "P0"
    if citations >= 25 or score >= 42 or year >= 2024:
        return "P1"
    return "P2"


def paper_url(row: dict[str, str]) -> str:
    if row.get("url"):
        return row["url"]
    if row.get("arxiv"):
        return f"https://arxiv.org/abs/{row['arxiv']}"
    return ""


def short_name(title: str) -> str:
    title = " ".join((title or "").split())
    cleaned = re.sub(r"^A |^An |^The ", "", title).strip()
    return cleaned[:80]


def curated_row_from_candidate(row: dict[str, str], status: str) -> dict[str, str]:
    category = row.get("category") or category_for(row)
    seed_hits = row.get("seed_hit_count", "0")
    source_titles = row.get("matched_seed_titles", "")
    return {
        "list_status": status,
        "priority": priority_for(row),
        "primary_category": category,
        "title": " ".join(row.get("title", "").split()),
        "short_name": short_name(row.get("title", "")),
        "approx_year": row.get("year", ""),
        "paper_type": category,
        "primary_relevance": category,
        "key_use_for_systematic_survey": (
            f"Discovered through citation/reference expansion; connected to {seed_hits} source papers."
        ),
        "source_url": paper_url(row),
        "notes": f"Discovery status: {status}. Source links: {source_titles[:500]}",
        "citationCount": row.get("citationCount", ""),
        "seed_hit_count": seed_hits,
        "score": row.get("score", ""),
        "authors": row.get("authors", ""),
        "venue": row.get("venue", ""),
        "doi": row.get("doi", ""),
        "arxiv": row.get("arxiv", ""),
        "paperId": row.get("paperId", ""),
        "abstract": row.get("abstract", ""),
    }


def curated_row_from_seed(row: dict[str, str]) -> dict[str, str]:
    return {
        "list_status": "seed",
        "priority": row.get("priority", ""),
        "primary_category": seed_category(row),
        "title": row.get("title", ""),
        "short_name": row.get("short_name", ""),
        "approx_year": row.get("approx_year", "") or row.get("resolved_year", ""),
        "paper_type": row.get("paper_type", ""),
        "primary_relevance": row.get("primary_relevance", ""),
        "key_use_for_systematic_survey": row.get("key_use_for_systematic_survey", ""),
        "source_url": row.get("source_url", "") or row.get("semantic_scholar_url", ""),
        "notes": row.get("notes", ""),
        "citationCount": row.get("citationCount", ""),
        "seed_hit_count": "",
        "score": "",
        "authors": row.get("authors", ""),
        "venue": row.get("venue", ""),
        "doi": row.get("doi", ""),
        "arxiv": row.get("arxiv", ""),
        "paperId": row.get("resolved_paperId", ""),
        "abstract": row.get("abstract", ""),
    }


def build_curated_papers(
    seeds: list[dict[str, str]],
    combined_candidates: list[dict[str, str]],
    round2_manifest_rows: list[dict[str, str]],
    round2_candidates: list[dict[str, str]],
) -> list[dict[str, str]]:
    curated: list[dict[str, str]] = []
    seen_titles = set()
    seen_ids = set()

    def add(row: dict[str, str]) -> None:
        title_key = norm(row.get("title", ""))
        paper_id = row.get("paperId", "")
        is_seed = row.get("list_status") == "seed"
        if not title_key or title_key in seen_titles or (paper_id and paper_id in seen_ids and not is_seed):
            return
        seen_titles.add(title_key)
        if paper_id:
            seen_ids.add(paper_id)
        curated.append(row)

    for seed in seeds:
        add(curated_row_from_seed(seed))

    by_paper_id = {row.get("paperId", ""): row for row in combined_candidates if row.get("paperId")}
    by_title = {norm(row.get("title", "")): row for row in combined_candidates}

    for manifest in round2_manifest_rows:
        if manifest.get("status") != "ok":
            continue
        source = by_paper_id.get(manifest.get("source_paperId", "")) or by_title.get(
            norm(manifest.get("source_title", ""))
        )
        if source:
            add(curated_row_from_candidate(source, "round1_promoted_seed_for_round2"))

    def should_promote_round2(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        category = candidate.get("category", "")
        year = to_int(candidate.get("year", "0"))
        citations = to_int(candidate.get("citationCount", "0"))
        score = float(candidate.get("score", "0") or 0)
        hits = to_int(candidate.get("seed_hit_count", "0"))
        model_terms = set(term.strip() for term in candidate.get("model_terms", "").split(";") if term.strip())
        strong_llm_terms = {
            "large language model",
            "llm",
            "gpt",
            "chatgpt",
            "foundation model",
            "generative ai",
            "rag",
            "retrieval",
            "agent",
            "instruction",
            "reasoning",
            "finbert",
            "bert",
        }
        background_keep = any(term in title for term in ["finbert", "flue", "flang", "www'18"])
        if background_keep and citations >= 100 and hits >= 4:
            return True
        title_finance_terms = [
            "fin",
            "finance",
            "financial",
            "stock",
            "investment",
            "invest",
            "trading",
            "market",
            "equity",
            "portfolio",
            "regulatory",
            "business",
            "wall street",
        ]
        title_llm_terms = [
            "large language",
            "llm",
            "gpt",
            "finbert",
            "fingpt",
            "rag",
            "retrieval",
            "agent",
            "generative ai",
            "foundation model",
            "language model",
            "benchmark",
        ]
        if not any(term in title for term in title_finance_terms):
            return False
        if not any(term in title for term in title_llm_terms):
            return False
        if category == "Other relevant work":
            return any(term in title for term in ["large language", "llm", "financial assistant", "rag", "retrieval"])
        if year < 2023:
            return False
        if not (model_terms & strong_llm_terms):
            return False
        return (score >= 34 and hits >= 2) or citations >= 25

    round2_promoted = 0
    for candidate in round2_candidates:
        if round2_promoted >= 40:
            break
        if should_promote_round2(candidate):
            add(curated_row_from_candidate(candidate, "round2_promoted"))
            round2_promoted += 1
    return curated


def write_readme(
    seeds: list[dict[str, str]],
    candidates: list[dict[str, str]],
    curated: list[dict[str, str]],
    round2_candidates: list[dict[str, str]],
) -> None:
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
    lines = [
        "# Awesome LLM for Finance",
        "",
        "A curated reading list for large language models in finance: financial-domain LLMs, benchmarks, SEC filing analysis, financial reasoning, trading agents, investment research, and professional finance evaluation.",
        "",
        "> Status: expanding public seed. The current catalog starts from 58 seed papers, one first-pass citation/reference expansion, and a second pass over 40 high-relevance finance LLM candidates.",
        "",
        "## Data Files",
        "",
        "- `data/processed/curated_papers.csv`: expanded curated list combining the original seeds and promoted additions.",
        "- `data/processed/seed_papers_enriched.csv`: seed papers with Semantic Scholar metadata, citation counts, links, and abstracts.",
        "- `data/processed/expansion_candidates_preliminary.csv`: top 200 candidate additions discovered from citation/reference expansion.",
        "- `data/processed/round2_expansion_candidates.csv`: top 200 candidate additions discovered from the second-round expansion.",
        "- `data/processed/related_work_relevance_longlist.csv`: longer relevance-filtered candidate list for manual review.",
        "- `data/raw/semantic_scholar_related_work_edges.csv`: raw citation/reference edges from the first expansion pass.",
        "- `data/raw/round2_related_work_edges.csv`: raw citation/reference edges from the second expansion pass.",
        "- `data/raw/semantic_scholar_manifest.csv`: per-seed retrieval status and edge counts.",
        "- `data/raw/round2_related_work_manifest.csv`: per-round-2-seed retrieval status and edge counts.",
        "",
        "## Collection Method",
        "",
        "1. Start with the seed CSV in `data/raw/seed_papers_original.csv`.",
        "2. Resolve seed papers through Semantic Scholar, preferring arXiv ids when available.",
        "3. Fetch both citations and references for each resolved seed paper.",
        "4. Promote high-confidence first-pass candidates as second-round seeds.",
        "5. Fetch citations and references for those promoted candidates.",
        "6. Rank candidate additions by finance/LLM relevance terms, number of source-paper connections, citation count, influential-edge hits, and recency.",
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

    curated_additions_by_category: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in curated:
        if row.get("list_status") == "seed":
            continue
        curated_additions_by_category[row.get("primary_category") or "Other"].append(row)

    lines.extend(["## Expanded Curated Additions", ""])
    for category in category_order + ["Other relevant work"]:
        items = curated_additions_by_category.get(category, [])
        if not items:
            continue
        lines.extend([f"### {category}", ""])
        for row in sorted(
            items,
            key=lambda x: (
                x.get("priority", "P9"),
                -to_int(x.get("citationCount", "0")),
                x.get("title", ""),
            ),
        ):
            lines.append(
                f"- {markdown_link(row.get('title', ''), row.get('source_url', ''))} "
                f"({row.get('approx_year', 'n.d.')}) - `{row.get('priority', '')}` "
                f"- citations: {row.get('citationCount', '0')} "
                f"- {row.get('list_status', '')}"
            )
        lines.append("")

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

## Round 2: High-Relevance Candidate Expansion

- Select high-confidence first-round candidates that are clearly finance-specific and LLM-, agent-, RAG-, FinBERT-, or benchmark-related.
- Fetch citations and references for those promoted candidates.
- Export `round2_related_work_edges.csv` and `round2_expansion_candidates.csv`.
- Promote a conservative subset into `curated_papers.csv`.

## Round 3: Manual Curation

- Check abstracts and titles for false positives, especially generic financial NLP, reinforcement learning, and non-finance RAG papers.
- Split older financial NLP benchmarks into a background section when they are useful but not LLM-specific.
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
    first_round_edges = read_csv(EDGES_PATH)
    round2_edges = normalize_round2_edges(read_csv(ROUND2_EDGES_PATH))
    edges = first_round_edges + round2_edges
    round2_manifest_rows = read_csv(ROUND2_MANIFEST_PATH)
    candidates, longlist = build_candidates(seeds, edges)
    round2_seed_rows = round2_manifest_as_seed_rows(round2_manifest_rows)
    round2_candidates, _round2_longlist = build_candidates(
        seeds + round2_seed_rows, round2_edges
    )
    curated = build_curated_papers(seeds, longlist, round2_manifest_rows, round2_candidates)
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
    write_csv(ROUND2_CANDIDATES_PATH, round2_candidates, columns)
    curated_columns = [
        "list_status",
        "priority",
        "primary_category",
        "title",
        "short_name",
        "approx_year",
        "paper_type",
        "primary_relevance",
        "key_use_for_systematic_survey",
        "source_url",
        "notes",
        "citationCount",
        "seed_hit_count",
        "score",
        "authors",
        "venue",
        "doi",
        "arxiv",
        "paperId",
        "abstract",
    ]
    write_csv(CURATED_PATH, curated, curated_columns)
    write_readme(seeds, candidates, curated, round2_candidates)
    write_plan()
    print(f"seeds={len(seeds)}")
    print(f"first_round_edges={len(first_round_edges)}")
    print(f"round2_edges={len(round2_edges)}")
    print(f"edges={len(edges)}")
    print(f"candidates={len(candidates)}")
    print(f"round2_candidates={len(round2_candidates)}")
    print(f"longlist={len(longlist)}")
    print(f"curated={len(curated)}")
    print(f"wrote={CANDIDATES_PATH}")


if __name__ == "__main__":
    main()

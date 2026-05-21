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
ROUND3_EDGES_PATH = ROOT / "data" / "raw" / "round3_related_work_edges.csv"
ROUND3_MANIFEST_PATH = ROOT / "data" / "raw" / "round3_related_work_manifest.csv"
ROUND4_EDGES_PATH = ROOT / "data" / "raw" / "round4_related_work_edges.csv"
ROUND4_MANIFEST_PATH = ROOT / "data" / "raw" / "round4_related_work_manifest.csv"
TRADING_AGENT_FOCUS_EDGES_PATH = ROOT / "data" / "raw" / "trading_agent_focus_edges.csv"
TRADING_AGENT_FOCUS_MANIFEST_PATH = ROOT / "data" / "raw" / "trading_agent_focus_manifest.csv"
REPORT_ANALYSIS_FOCUS_EDGES_PATH = ROOT / "data" / "raw" / "report_analysis_focus_edges.csv"
REPORT_ANALYSIS_FOCUS_MANIFEST_PATH = ROOT / "data" / "raw" / "report_analysis_focus_manifest.csv"
REGTECH_COMPLIANCE_FOCUS_EDGES_PATH = ROOT / "data" / "raw" / "regtech_compliance_focus_edges.csv"
REGTECH_COMPLIANCE_FOCUS_MANIFEST_PATH = ROOT / "data" / "raw" / "regtech_compliance_focus_manifest.csv"
SPECIFIC_DOMAIN_FOCUS_EDGES_PATH = ROOT / "data" / "raw" / "specific_domain_focus_edges.csv"
SPECIFIC_DOMAIN_FOCUS_MANIFEST_PATH = ROOT / "data" / "raw" / "specific_domain_focus_manifest.csv"
SPECIFIC_DOMAIN_ROUND2_EDGES_PATH = ROOT / "data" / "raw" / "specific_domain_round2_edges.csv"
SPECIFIC_DOMAIN_ROUND2_MANIFEST_PATH = ROOT / "data" / "raw" / "specific_domain_round2_manifest.csv"
SPECIFIC_DOMAIN_ROUND3_EDGES_PATH = ROOT / "data" / "raw" / "specific_domain_round3_edges.csv"
SPECIFIC_DOMAIN_ROUND3_MANIFEST_PATH = ROOT / "data" / "raw" / "specific_domain_round3_manifest.csv"
INSTITUTIONAL_TRADING_FOCUS_EDGES_PATH = ROOT / "data" / "raw" / "institutional_trading_focus_edges.csv"
INSTITUTIONAL_TRADING_FOCUS_MANIFEST_PATH = ROOT / "data" / "raw" / "institutional_trading_focus_manifest.csv"
INSTITUTIONAL_TRADING_ROUND2_EDGES_PATH = ROOT / "data" / "raw" / "institutional_trading_round2_edges.csv"
INSTITUTIONAL_TRADING_ROUND2_MANIFEST_PATH = ROOT / "data" / "raw" / "institutional_trading_round2_manifest.csv"
INSTITUTIONAL_TRADING_ROUND3_EDGES_PATH = ROOT / "data" / "raw" / "institutional_trading_round3_edges.csv"
INSTITUTIONAL_TRADING_ROUND3_MANIFEST_PATH = ROOT / "data" / "raw" / "institutional_trading_round3_manifest.csv"
CANDIDATES_PATH = ROOT / "data" / "processed" / "expansion_candidates_preliminary.csv"
LONG_LIST_PATH = ROOT / "data" / "processed" / "related_work_relevance_longlist.csv"
ROUND2_CANDIDATES_PATH = ROOT / "data" / "processed" / "round2_expansion_candidates.csv"
ROUND3_CANDIDATES_PATH = ROOT / "data" / "processed" / "round3_expansion_candidates.csv"
ROUND4_CANDIDATES_PATH = ROOT / "data" / "processed" / "round4_expansion_candidates.csv"
TRADING_AGENT_FOCUS_SEEDS_PATH = ROOT / "data" / "processed" / "trading_agent_focus_finmem_seed_candidates.csv"
TRADING_AGENT_FOCUS_CANDIDATES_PATH = ROOT / "data" / "processed" / "trading_agent_focus_expansion_candidates.csv"
REPORT_ANALYSIS_FOCUS_SEEDS_PATH = ROOT / "data" / "processed" / "report_analysis_focus_seed_candidates.csv"
REPORT_ANALYSIS_FOCUS_CANDIDATES_PATH = ROOT / "data" / "processed" / "report_analysis_focus_expansion_candidates.csv"
REGTECH_COMPLIANCE_FOCUS_ANCHORS_PATH = ROOT / "data" / "processed" / "regtech_compliance_focus_anchor_candidates.csv"
REGTECH_COMPLIANCE_FOCUS_CANDIDATES_PATH = ROOT / "data" / "processed" / "regtech_compliance_focus_expansion_candidates.csv"
SPECIFIC_DOMAIN_FOCUS_SEARCH_PATH = ROOT / "data" / "processed" / "specific_domain_focus_search_candidates.csv"
SPECIFIC_DOMAIN_FOCUS_CANDIDATES_PATH = ROOT / "data" / "processed" / "specific_domain_focus_expansion_candidates.csv"
SPECIFIC_DOMAIN_ROUND2_ANCHORS_PATH = ROOT / "data" / "processed" / "specific_domain_round2_anchor_candidates.csv"
SPECIFIC_DOMAIN_ROUND2_CANDIDATES_PATH = ROOT / "data" / "processed" / "specific_domain_round2_expansion_candidates.csv"
SPECIFIC_DOMAIN_ROUND3_ANCHORS_PATH = ROOT / "data" / "processed" / "specific_domain_round3_anchor_candidates.csv"
SPECIFIC_DOMAIN_ROUND3_CANDIDATES_PATH = ROOT / "data" / "processed" / "specific_domain_round3_expansion_candidates.csv"
INSTITUTIONAL_TRADING_FOCUS_SEARCH_PATH = ROOT / "data" / "processed" / "institutional_trading_focus_search_candidates.csv"
INSTITUTIONAL_TRADING_FOCUS_CANDIDATES_PATH = ROOT / "data" / "processed" / "institutional_trading_focus_expansion_candidates.csv"
INSTITUTIONAL_TRADING_ROUND2_ANCHORS_PATH = ROOT / "data" / "processed" / "institutional_trading_round2_anchor_candidates.csv"
INSTITUTIONAL_TRADING_ROUND2_CANDIDATES_PATH = ROOT / "data" / "processed" / "institutional_trading_round2_expansion_candidates.csv"
INSTITUTIONAL_TRADING_ROUND3_ANCHORS_PATH = ROOT / "data" / "processed" / "institutional_trading_round3_anchor_candidates.csv"
INSTITUTIONAL_TRADING_ROUND3_CANDIDATES_PATH = ROOT / "data" / "processed" / "institutional_trading_round3_expansion_candidates.csv"
CURATED_PATH = ROOT / "data" / "processed" / "curated_papers.csv"
TAXONOMY_PATH = ROOT / "data" / "processed" / "curated_papers_by_taxonomy.csv"
README_PATH = ROOT / "README.md"


TAXONOMY_ORDER = [
    "Surveys and Reviews",
    "Foundation and Domain Language Models",
    "Benchmarks and Evaluation Suites",
    "Financial QA, Reasoning, and Table Understanding",
    "Reports, Filings, Accounting, and Risk",
    "Trading, Investment, and Portfolio Management",
    "Agents and Multi-Agent Systems",
    "RAG, Search, and Knowledge Systems",
    "Multimodal and Multilingual Finance",
    "Professional, Regulatory, and Advisory Applications",
]

TAXONOMY_DESCRIPTIONS = {
    "Surveys and Reviews": "Survey, review, taxonomy, and overview papers that map the finance LLM landscape.",
    "Foundation and Domain Language Models": "Financial-domain LLMs, FinBERT-style models, instruction tuning, and domain adaptation work.",
    "Benchmarks and Evaluation Suites": "General finance LLM benchmarks, evaluation suites, exams, leaderboards, and broad task collections.",
    "Financial QA, Reasoning, and Table Understanding": "Question answering, numerical reasoning, financial table/text reasoning, and discrete reasoning tasks.",
    "Reports, Filings, Accounting, and Risk": "SEC filings, annual reports, XBRL, accounting, credit/risk, disclosure, and document analytics.",
    "Trading, Investment, and Portfolio Management": "Stock prediction, trading, alpha, portfolio construction, allocation, investment reports, and market analysis.",
    "Agents and Multi-Agent Systems": "Financial LLM agents, trading agents, multi-agent markets, agent benchmarks, and autonomous workflows.",
    "RAG, Search, and Knowledge Systems": "Retrieval-augmented generation, search, knowledge grounding, knowledge graphs, and document retrieval systems.",
    "Multimodal and Multilingual Finance": "Multimodal, multilingual, bilingual, and non-English financial LLM resources and evaluations.",
    "Professional, Regulatory, and Advisory Applications": "CFA/professional exams, financial advice, regulatory interpretation, compliance, and human-facing advisory settings.",
}

TRADING_SUBTHEME_ORDER = [
    "Alpha Mining and Factor Discovery",
    "Derivatives, Options, and Structured Products",
    "Market Simulation and Execution Infrastructure",
    "Market Microstructure, Execution, and Prediction Markets",
    "Private Markets, VC, and Due Diligence",
    "Wealth, Advisory, and Personal Investing",
    "Portfolio, ETF, and Asset Allocation",
    "Trading Agents and Strategy Generation",
    "Stock Prediction and Market Forecasting",
    "Investment Research and Financial Analysis",
    "Not Trading Focused",
]

TRADING_SUBTHEME_DESCRIPTIONS = {
    "Alpha Mining and Factor Discovery": "LLM-driven alpha discovery, formulaic factor mining, interpretable factors, and alpha decay control.",
    "Derivatives, Options, and Structured Products": "Options, derivatives, hedging, payoff reasoning, structured products, and volatility-surface tasks.",
    "Market Simulation and Execution Infrastructure": "Limit-order-book simulators, high-fidelity market simulators, and background execution/HFT infrastructure used to evaluate trading agents.",
    "Market Microstructure, Execution, and Prediction Markets": "Order-level trading, execution agents, slippage, liquidity, transaction costs, prediction markets, and latency arbitrage.",
    "Private Markets, VC, and Due Diligence": "Venture capital, startup success prediction, private equity, private-market due diligence, and investment memo workflows.",
    "Wealth, Advisory, and Personal Investing": "Financial advisors, robo-advisory, investor profiling, suitability, private-investor risk, and portfolio advice.",
    "Portfolio, ETF, and Asset Allocation": "Portfolio construction, ETF/sector/macro allocation, and allocation rationale generation.",
    "Trading Agents and Strategy Generation": "LLM trading agents, multi-agent trading, strategy generation, backtesting, and executable trading instructions.",
    "Stock Prediction and Market Forecasting": "Stock-return prediction, market forecasting, sentiment-driven prediction, and general return-predictability tasks.",
    "Investment Research and Financial Analysis": "Equity research, investment reports, financial analysis workflows, and analyst-style systems.",
    "Not Trading Focused": "Papers outside the current trading/investment focus.",
}


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
    "supply chain finance",
    "supply chain risk",
    "sector allocation",
    "sector analysis",
    "industry analysis",
    "equity research",
    "research report",
    "etf",
    "exchange-traded fund",
    "option",
    "options",
    "derivative",
    "derivatives",
    "structured product",
    "structured products",
    "hedging",
    "volatility surface",
    "order book",
    "limit order book",
    "market microstructure",
    "execution",
    "slippage",
    "transaction cost",
    "high frequency",
    "hft",
    "robo-advisor",
    "wealth management",
    "investment advice",
    "private equity",
    "venture capital",
    "alternative assets",
    "private market",
    "private markets",
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


def normalize_round_edges(rows: list[dict[str, str]], round_label: str, output_csv: str) -> list[dict[str, str]]:
    normalized = []
    for row in rows:
        normalized.append(
            {
                "source_index": f"{round_label.upper()}-{row.get('source_rank', '')}",
                "source_signature": f"{round_label}:{row.get('source_paperId', '')}",
                "source_title": row.get("source_title", ""),
                "source_year": row.get("source_year", ""),
                "source_domain": row.get("source_category", ""),
                "source_tag": round_label,
                "resolved_source_paperId": row.get("source_paperId", ""),
                "resolved_source_title": row.get("source_title", ""),
                "output_csv": output_csv,
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


def manifest_as_seed_rows(manifest_rows: list[dict[str, str]]) -> list[dict[str, str]]:
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


def curated_as_seed_rows(curated: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        {
            "title": row.get("title", ""),
            "resolved_title": row.get("title", ""),
            "resolved_paperId": row.get("paperId", ""),
        }
        for row in curated
        if row.get("title")
    ]


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


def assign_taxonomy_category(row: dict[str, str]) -> str:
    title = norm(row.get("title", ""))
    abstract = norm(row.get("abstract", ""))
    category = norm(row.get("primary_category", ""))
    paper_type = norm(row.get("paper_type", ""))
    relevance = norm(row.get("primary_relevance", ""))
    signal = f"{title} {category} {paper_type} {relevance}"
    padded_signal = f" {signal} "

    def has_any(terms: list[str], where: str = signal) -> bool:
        return any(term in where for term in terms)

    def has_rag_signal() -> bool:
        return has_any(
            [
                "retrieval",
                "retrieval-augmented",
                "finsearch",
                "financial search",
                "search and reasoning",
                "knowledge graph",
                "knowledge grounding",
                "grounding",
                "chunking",
                "document retrieval",
                "text embedding",
                "claim verification",
                "fact-checking",
                "grounded",
            ],
            signal,
        ) or " rag " in padded_signal

    def has_qa_signal() -> bool:
        return has_any(
            [
                "question answering",
                "question-answering",
                "numerical reasoning",
                "quantitative reasoning",
                "discrete reasoning",
                "table-text",
                "table text",
                "textual data",
                "chain-of-thought",
                "reasoning over financial",
                "financial reasoning",
                "finqa",
                "convfinqa",
                "docfinqa",
                "tat-qa",
                "tat-llm",
                "multihiertt",
                "finchain",
                "bizbench",
            ],
            signal,
        ) or " qa " in padded_signal or " table " in padded_signal or " tables " in padded_signal

    def is_agent_work() -> bool:
        return has_any(
            [
                "agent",
                "agents",
                "multi-agent",
                "multi agent",
                "agentic",
                "autonomous",
                "crews",
            ],
            signal,
        )

    def is_trading_or_investment() -> bool:
        return has_any(
            [
                "trading",
                "trade",
                "stock",
                "stocks",
                "portfolio",
                "investment",
                "investor",
                "investing",
                "alpha",
                "return prediction",
                "stock return",
                "stock price",
                "market timing",
                "equity",
                "asset allocation",
                "sector allocation",
                "sector asset allocation",
                "macro and sector asset allocation",
                "sector-specific financial news",
                "wall street",
                "earnings reports",
                "quantitative investment",
                "fund investment",
                "hedge-fund",
                "fundamental analysis",
                "equity research",
                "investment research",
                "research report",
                "research reports",
                "industry classification",
                "industry analysis",
                "sector analysis",
                "etf",
                "exchange traded fund",
                "exchange-traded fund",
                "option",
                "options",
                "derivative",
                "derivatives",
                "structured product",
                "structured products",
                "hedging",
                "volatility surface",
                "implied volatility",
                "order book",
                "limit order book",
                "market microstructure",
                "execution",
                "slippage",
                "transaction cost",
                "high frequency",
                "hft",
                "prediction market",
                "prediction markets",
                "robo-advisor",
                "robo advisor",
                "wealth management",
                "investment advice",
                "financial advice",
                "investor profiling",
                "private equity",
                "venture capital",
                "due diligence",
                "private market",
                "private markets",
                "alternative asset",
                "alternative assets",
                "commercial real estate",
                "forecasting",
                "financial market",
                "sentiment trading",
                "crypto",
                "cryptocurrency",
                "forex",
            ],
            signal,
        ) or " market " in padded_signal or " markets " in padded_signal or " factor " in padded_signal or " factors " in padded_signal or " valuation " in padded_signal

    # 1. Surveys are primarily navigational and should stay together. Avoid
    # matching bare "taxonomy" because some task papers build taxonomies.
    if has_any(["survey", "review", "overview", "scoping review", "systematic review"], title) or "survey" in category:
        return "Surveys and Reviews"

    # 2. Professional/regulatory/advisory work is defined by the decision-maker
    # context, not by generic words such as "professional" alone.
    if has_any(
        [
            "cfa",
            "chartered financial analyst",
            "financial advisor",
            "financial advisement",
            "advisory",
            "regulatory interpretation",
            "regulation",
            "compliance",
            "mock cfa",
            "financial literacy",
            "model risk management",
        ],
        signal,
    ):
        return "Professional, Regulatory, and Advisory Applications"

    # 3. RAG, retrieval, search, grounding, and knowledge systems are a
    # first-class systems theme when explicitly named.
    if has_rag_signal():
        return "RAG, Search, and Knowledge Systems"

    # 4. Filing/report/accounting/risk document analytics should not be absorbed
    # by agent or RAG labels when the data object is the main contribution.
    if has_any(
        [
            "sec filing",
            "sec filings",
            "10-k",
            "10-q",
            "edgar",
            "xbrl",
            "annual report",
            "financial report",
            "financial reports",
            "filing",
            "filings",
            "accounting",
            "audit",
            "auditing",
            "disclosure",
            "disclosures",
            "credit risk",
            "risk extraction",
            "risk quantification",
            "material risks",
            "loan descriptions",
            "supply chain finance",
            "supply chain risk",
            "supply-chain risk",
            "repayment risk",
            "firm-level supply chain",
            "banking",
            "financial statement",
            "financial statements",
            "fundamental analysis",
            "taxonomy-aligned risk",
        ],
        signal,
    ):
        return "Reports, Filings, Accounting, and Risk"

    # 5. QA/reasoning/table-understanding papers form a clear task family. This
    # catches finance QA datasets before broad benchmark or RAG labels.
    if has_qa_signal():
        return "Financial QA, Reasoning, and Table Understanding"

    # 6. Agents are a distinct systems theme. Reports, QA, and professional
    # papers have already been separated above.
    if is_agent_work():
        return "Agents and Multi-Agent Systems"

    # 7. Trading/investment and market tasks. Put task-focused prediction,
    # allocation, valuation, and portfolio papers here even when they use RAG or
    # fine-tuning as a technique.
    if is_trading_or_investment() or category == "trading and investment":
        return "Trading, Investment, and Portfolio Management"

    # 8. Multimodal/multilingual resources are a cross-cutting theme, but useful
    # enough to be a first-class bucket for browsing.
    if has_any(
        [
            "multimodal",
            "multi-modal",
            "vision-language",
            "vlm",
            "chart",
            "image-centric",
            "multilingual",
            "bilingual",
            "chinese",
            "spanish",
            "arabic",
            "greek",
            "japanese",
            "low-resource",
            "non-english",
            "cross-lingual",
            "cflue",
        ],
        signal,
    ):
        return "Multimodal and Multilingual Finance"

    # 9. Domain models and fine-tuning/instruction-tuning papers.
    if has_any(
        [
            "bloomberggpt",
            "fingpt",
            "finbert",
            "bondbert",
            "finllm",
            "finllms",
            "financial language model",
            "financial large language model",
            "financial chat model",
            "financial assistant",
            "domain pre-trained",
            "pre-trained financial",
            "instruction tuning",
            "fine-tuning",
            "fine tuning",
            "instruct-",
            "open finllm",
            "leaderboard",
            "domain adaptation",
            "domain adaption",
            "financial communications",
            "sentiment analysis",
            "text classification",
        ],
        signal,
    ):
        return "Foundation and Domain Language Models"

    # 10. Broad benchmarks and evaluation collections.
    if has_any(
        [
            "benchmark",
            "evaluation",
            "evaluating",
            "eval",
            "dataset",
            "datasets",
            "exam",
            "leaderboard",
            "test",
            "task collection",
        ],
        signal,
    ):
        return "Benchmarks and Evaluation Suites"

    return "Benchmarks and Evaluation Suites"


def assign_trading_subtheme(row: dict[str, str]) -> str:
    title = norm(row.get("title", ""))
    short_name = norm(row.get("short_name", ""))
    abstract = norm(row.get("abstract", ""))
    category = norm(row.get("primary_category", ""))
    narrow_signal = f"{title} {short_name} {category}"
    full_signal = f"{narrow_signal} {abstract}"

    def has_any(terms: list[str], text: str = narrow_signal) -> bool:
        return any(term in text for term in terms)

    # The subtheme tags are intentionally high precision. Broad surveys,
    # foundation models, QA benchmarks, and report-analysis papers often mention
    # trading words in passing; they should not inflate the trading taxonomy.
    if has_any(
        [
            "large language models in finance: a survey",
            "bridging language models and financial analysis",
            "financeqa",
            "finsheet-bench",
            "famma:",
            "mme-finance",
            "financebench",
            "open finllm leaderboard",
        ]
    ):
        return "Not Trading Focused"

    if category == "derivatives, options, and structured products":
        if has_any(
            [
                "option",
                "options",
                "derivative",
                "derivatives",
                "structured product",
                "structured products",
                "hedging",
                "volatility surface",
                "implied volatility",
                "payoff",
                "deltahedge",
            ]
        ):
            return "Derivatives, Options, and Structured Products"
        return "Not Trading Focused"

    if category == "market microstructure and execution":
        if has_any(
            [
                "jax-lob",
                "abides",
                "simulator",
                "simulation",
                "environment",
                "infrastructure",
            ]
        ):
            return "Market Simulation and Execution Infrastructure"
        if has_any(
            [
                "alpha mining",
                "factor mining",
                "formulaic alpha",
                "factor discovery",
                "alphaforge",
            ]
        ):
            return "Alpha Mining and Factor Discovery"
        return "Market Microstructure, Execution, and Prediction Markets"

    if category == "private markets and alternative assets":
        if has_any(["finsheet-bench", "spreadsheet"]):
            return "Not Trading Focused"
        return "Private Markets, VC, and Due Diligence"

    if category == "wealth, advisory, and personal investing":
        return "Wealth, Advisory, and Personal Investing"

    if category == "etf and asset allocation":
        return "Portfolio, ETF, and Asset Allocation"

    if category == "industry, sector, and investment research":
        return "Investment Research and Financial Analysis"

    if has_any(
        [
            "alpha mining",
            "alpha decay",
            "factor mining",
            "factor generation",
            "formulaic factor",
            "formulaic alpha",
            "interpretable financial factors",
            "factor discovery",
            "alpha jungle",
            "alphaagent",
            "alphaprobe",
            "alphacrafter",
            "quantaalpha",
            "factorengine",
            "factormad",
        ]
    ):
        return "Alpha Mining and Factor Discovery"

    if has_any(
        [
            "option",
            "options",
            "derivative",
            "derivatives",
            "structured product",
            "structured products",
            "hedging",
            "volatility surface",
            "implied volatility",
            "payoff",
            "deltahedge",
        ]
    ):
        return "Derivatives, Options, and Structured Products"

    if has_any(
        [
            "jax-lob",
            "abides",
            "limit order book simulator",
            "order-level simulator",
            "market simulation",
            "market simulator",
            "simulation environment",
            "high-fidelity multi-agent market simulation",
        ]
    ):
        return "Market Simulation and Execution Infrastructure"

    if has_any(
        [
            "order book",
            "limit order book",
            "market microstructure",
            "execution",
            "slippage",
            "transaction cost",
            "market impact",
            "liquidity",
            "high frequency",
            "hft",
            "latency arbitrage",
            "prediction market",
            "prediction markets",
            "polymarket",
            "lob-bench",
            "tradefm",
        ]
    ):
        return "Market Microstructure, Execution, and Prediction Markets"

    if has_any(
        [
            "venture capital",
            "startup success",
            "start-up success",
            "private equity",
            "private market",
            "private markets",
            "due diligence",
            "deal screening",
            "investment memo",
            "alternative asset",
            "alternative assets",
            "real estate finance",
            "commercial real estate",
        ]
    ):
        return "Private Markets, VC, and Due Diligence"

    if has_any(
        [
            "robo-advisor",
            "robo advisor",
            "financial advisor",
            "financial advice",
            "investment advice",
            "investor profiling",
            "suitability",
            "wealth management",
            "retirement planning",
            "portfolio recommendation",
            "private investors",
        ]
    ):
        return "Wealth, Advisory, and Personal Investing"

    if has_any(
        [
            "portfolio",
            "asset allocation",
            "sector allocation",
            "portfolio construction",
            "etf",
            "exchange-traded fund",
            "exchange traded fund",
            "macro and sector asset allocation",
        ]
    ):
        return "Portfolio, ETF, and Asset Allocation"

    trading_agent_terms = [
        "trading agent",
        "trading agents",
        "stockagent",
        "tradearena",
        "tradingagents",
        "finagent",
        "hedgeagents",
        "forexagent",
        "quantagent",
        "livetradebench",
        "tradetrap",
        "trading strategy",
        "trading strategies",
        "algorithmic trading",
        "executable trading",
        "trading instruction",
        "trading instructions",
        "strategy generation",
        "backtesting",
    ]
    if has_any(trading_agent_terms):
        return "Trading Agents and Strategy Generation"

    if category == "financial agents" and has_any(
        [
            "multi-agent",
            "multi agent",
        ],
        full_signal,
    ):
        if has_any(trading_agent_terms, full_signal):
            return "Trading Agents and Strategy Generation"

    if has_any(
        [
            "stock prediction",
            "stock price",
            "stock return",
            "return prediction",
            "asset-return prediction",
            "market forecasting",
            "market forecast",
            "forecast stock",
            "predict stock",
            "sentiment trading",
            "stock movement",
            "stock movements",
        ]
    ):
        return "Stock Prediction and Market Forecasting"

    if has_any(
        [
            "equity research",
            "investment research",
            "financial analysis",
            "investment analysis",
            "research report",
            "research reports",
            "fundamental analysis",
            "analyst",
            "investment management",
        ]
    ):
        return "Investment Research and Financial Analysis"

    if category == "trading and investment":
        if has_any(
            [
                "stock",
                "equity",
                "market",
                "return",
                "investment",
                "investing",
                "portfolio",
                "trading",
                "alpha",
                "forecast",
            ]
        ):
            return "Investment Research and Financial Analysis"

    return "Not Trading Focused"


def apply_taxonomy(curated: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in curated:
        enriched = dict(row)
        enriched["taxonomy_category"] = assign_taxonomy_category(row)
        enriched["taxonomy_description"] = TAXONOMY_DESCRIPTIONS[enriched["taxonomy_category"]]
        enriched["trading_subtheme"] = assign_trading_subtheme(row)
        enriched["trading_subtheme_description"] = TRADING_SUBTHEME_DESCRIPTIONS[
            enriched["trading_subtheme"]
        ]
        rows.append(enriched)

    if len(rows) != len(curated):
        raise RuntimeError(f"taxonomy row count mismatch: {len(rows)} != {len(curated)}")
    missing = [row for row in rows if not row.get("taxonomy_category")]
    if missing:
        raise RuntimeError(f"taxonomy assignment missing for {len(missing)} rows")
    return rows


def build_curated_papers(
    seeds: list[dict[str, str]],
    combined_candidates: list[dict[str, str]],
    round2_manifest_rows: list[dict[str, str]],
    round2_candidates: list[dict[str, str]],
    round3_manifest_rows: list[dict[str, str]] | None = None,
    round3_candidates: list[dict[str, str]] | None = None,
    round4_manifest_rows: list[dict[str, str]] | None = None,
    round4_candidates: list[dict[str, str]] | None = None,
    trading_focus_seed_candidates: list[dict[str, str]] | None = None,
    trading_focus_candidates: list[dict[str, str]] | None = None,
    report_focus_seed_candidates: list[dict[str, str]] | None = None,
    report_focus_candidates: list[dict[str, str]] | None = None,
    regtech_focus_candidates: list[dict[str, str]] | None = None,
    specific_domain_search_candidates: list[dict[str, str]] | None = None,
    specific_domain_focus_candidates: list[dict[str, str]] | None = None,
    specific_domain_round2_candidates: list[dict[str, str]] | None = None,
    specific_domain_round3_candidates: list[dict[str, str]] | None = None,
    institutional_trading_search_candidates: list[dict[str, str]] | None = None,
    institutional_trading_focus_candidates: list[dict[str, str]] | None = None,
    institutional_trading_round2_candidates: list[dict[str, str]] | None = None,
    institutional_trading_round3_candidates: list[dict[str, str]] | None = None,
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

    round3_manifest_rows = round3_manifest_rows or []
    round3_candidates = round3_candidates or []
    round4_manifest_rows = round4_manifest_rows or []
    round4_candidates = round4_candidates or []
    trading_focus_seed_candidates = trading_focus_seed_candidates or []
    trading_focus_candidates = trading_focus_candidates or []
    report_focus_seed_candidates = report_focus_seed_candidates or []
    report_focus_candidates = report_focus_candidates or []
    regtech_focus_candidates = regtech_focus_candidates or []
    specific_domain_search_candidates = specific_domain_search_candidates or []
    specific_domain_focus_candidates = specific_domain_focus_candidates or []
    specific_domain_round2_candidates = specific_domain_round2_candidates or []
    specific_domain_round3_candidates = specific_domain_round3_candidates or []
    institutional_trading_search_candidates = institutional_trading_search_candidates or []
    institutional_trading_focus_candidates = institutional_trading_focus_candidates or []
    institutional_trading_round2_candidates = institutional_trading_round2_candidates or []
    institutional_trading_round3_candidates = institutional_trading_round3_candidates or []

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

    for manifest in round3_manifest_rows:
        if manifest.get("status") != "ok":
            continue
        source = by_paper_id.get(manifest.get("source_paperId", "")) or by_title.get(
            norm(manifest.get("source_title", ""))
        )
        if source:
            add(curated_row_from_candidate(source, "round2_promoted_seed_for_round3"))

    def should_promote_round3(candidate: dict[str, str]) -> bool:
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
            "benchmark",
        }
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
        if year < 2023:
            return False
        if not any(term in title for term in title_finance_terms):
            return False
        if not any(term in title for term in title_llm_terms):
            return False
        if not (model_terms & strong_llm_terms):
            return False
        if category == "Other relevant work":
            return citations >= 10 and hits >= 2 and any(
                term in title for term in ["large language", "llm", "rag", "retrieval", "agent"]
            )
        return (score >= 30 and hits >= 2) or (citations >= 15 and hits >= 2) or citations >= 50

    round3_promoted = 0
    for candidate in round3_candidates:
        if round3_promoted >= 35:
            break
        if should_promote_round3(candidate):
            add(curated_row_from_candidate(candidate, "round3_promoted"))
            round3_promoted += 1

    def should_promote_round4_source(manifest: dict[str, str]) -> bool:
        title = manifest.get("source_title", "").lower()
        rank = to_int(manifest.get("source_rank", "999"))
        year = to_int(manifest.get("source_year", "0"))
        citations = to_int(manifest.get("source_citationCount", "0"))
        hits = to_int(manifest.get("source_seed_hit_count", "0"))
        if rank > 20 or year < 2024:
            return False
        title_llm_terms = [
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
        if not any(term in title for term in title_llm_terms):
            return False
        return hits >= 3 or citations >= 5

    round4_source_promoted = 0
    for manifest in round4_manifest_rows:
        if round4_source_promoted >= 15:
            break
        if manifest.get("status") != "ok":
            continue
        if not should_promote_round4_source(manifest):
            continue
        source = by_paper_id.get(manifest.get("source_paperId", "")) or by_title.get(
            norm(manifest.get("source_title", ""))
        )
        if source:
            add(curated_row_from_candidate(source, "round3_promoted_seed_for_round4"))
            round4_source_promoted += 1

    def should_promote_round4(candidate: dict[str, str]) -> bool:
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
            "benchmark",
        }
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
            "accounting",
            "credit",
            "bond",
            "asset",
            "robo-advisory",
        ]
        title_llm_terms = [
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
        if year < 2024 and citations < 50:
            return False
        if not any(term in title for term in title_finance_terms):
            return False
        if not any(term in title for term in title_llm_terms):
            return False
        if not (model_terms & strong_llm_terms):
            return False
        if category == "Other relevant work":
            return citations >= 8 and hits >= 2 and any(
                term in title for term in ["large language", "llm", "rag", "retrieval", "agent", "gpt"]
            )
        return (score >= 26 and hits >= 2) or (citations >= 10 and hits >= 2) or citations >= 25

    round4_promoted = 0
    for candidate in round4_candidates:
        if round4_promoted >= 12:
            break
        if should_promote_round4(candidate):
            add(curated_row_from_candidate(candidate, "round4_promoted"))
            round4_promoted += 1

    def should_promote_trading_focus(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        year = to_int(candidate.get("year", "0"))
        citations = to_int(candidate.get("citationCount", "0"))
        score = float(candidate.get("score", "0") or 0)
        hits = to_int(candidate.get("seed_hit_count", "0"))
        title_finance_terms = [
            "finance",
            "financial",
            "stock",
            "investment",
            "invest",
            "trading",
            "trade",
            "market",
            "equity",
            "portfolio",
            "alpha",
            "quant",
            "asset",
            "crypto",
            "forex",
            "earnings",
        ]
        title_agent_terms = [
            "large language",
            "llm",
            "gpt",
            "agent",
            "multi-agent",
            "agentic",
            "language model",
            "generative ai",
        ]
        excluded = [
            "prompt injection",
            "security",
            "consumer choice",
            "personal finances",
            "finrl",
            "deep reinforcement learning framework",
            "moving average",
        ]
        if year < 2024 and citations < 50:
            return False
        if any(term in title for term in excluded):
            return False
        if not any(term in title for term in title_finance_terms):
            return False
        if not any(term in title for term in title_agent_terms):
            return False
        return citations >= 2 or score >= 14 or hits >= 2

    trading_focus_promoted = 0
    for candidate in trading_focus_seed_candidates + trading_focus_candidates:
        if trading_focus_promoted >= 18:
            break
        if should_promote_trading_focus(candidate):
            add(curated_row_from_candidate(candidate, "trading_agent_focus_promoted"))
            trading_focus_promoted += 1

    def should_promote_report_focus(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        text = f"{title} {candidate.get('abstract', '').lower()}"
        year = to_int(candidate.get("year", "0"))
        citations = to_int(candidate.get("citationCount", "0"))
        score = float(candidate.get("score", "0") or 0)
        hits = to_int(candidate.get("seed_hit_count", "0"))
        report_terms = [
            "financial statement",
            "financial statements",
            "financial report",
            "financial reports",
            "annual report",
            "annual reports",
            "earnings report",
            "earnings reports",
            "earnings call",
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
            "edgar",
        ]
        report_title_terms = [
            "financial statement",
            "financial statements",
            "financial report",
            "financial reports",
            "financial nlp",
            "financial question answering",
            "financial research reporting",
            "financial documents",
            "standardized documents",
            "earnings",
            "10-k",
            "10-q",
            "sec",
            "xbrl",
            "filing",
            "filings",
            "disclosure",
            "accounting",
            "audit",
            "kpi",
            "edinet",
            "document-level numerical reasoning",
        ]
        llm_terms = [
            "large language",
            "llm",
            "gpt",
            "chatgpt",
            "language model",
            "rag",
            "retrieval",
            "question answering",
            "reasoning",
            "benchmark",
            "agent",
        ]
        excluded = [
            "legal, and medical",
            "medical documents",
            "generic",
            "software engineering",
            "personal finances",
            "marketing",
            "digital governance",
        ]
        if year < 2023:
            return False
        if any(term in title for term in excluded):
            return False
        if not any(term in title for term in report_title_terms):
            return False
        if not any(term in text for term in report_terms):
            return False
        if not any(term in text for term in llm_terms):
            return False
        return citations >= 2 or score >= 18 or hits >= 2

    report_focus_promoted = 0
    for candidate in report_focus_seed_candidates + report_focus_candidates:
        if report_focus_promoted >= 22:
            break
        if should_promote_report_focus(candidate):
            add(curated_row_from_candidate(candidate, "report_analysis_focus_promoted"))
            report_focus_promoted += 1

    def should_promote_regtech_focus(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        text = f"{title} {candidate.get('abstract', '').lower()}"
        year = to_int(candidate.get("year", "0"))
        citations = to_int(candidate.get("citationCount", "0"))
        score = float(candidate.get("score", "0") or 0)
        hits = to_int(candidate.get("seed_hit_count", "0"))
        finance_terms = [
            "finance",
            "financial",
            "bank",
            "banking",
            "credit",
            "lending",
            "accounting",
            "audit",
            "auditing",
            "investment",
            "investor",
            "regulatory",
            "regulation",
            "compliance",
            "fintech",
        ]
        finance_title_terms = [
            "finance",
            "financial",
            "bank",
            "banking",
            "bfsi",
            "credit",
            "lending",
            "accounting",
            "audit",
            "auditing",
            "investment",
            "investor",
            "retirement",
            "fintech",
            "sme",
            "structured finance",
        ]
        regtech_terms = [
            "regulatory",
            "regulation",
            "compliance",
            "model risk",
            "risk management",
            "audit",
            "auditing",
            "trustworthiness",
            "trustworthy",
            "fairness",
            "bias",
            "responsible",
            "accounting",
            "financial advisement",
            "financial advice",
            "advisor",
            "supervisory",
            "aml",
            "kyc",
        ]
        regtech_title_terms = [
            "regulatory",
            "regulation",
            "compliance",
            "model risk",
            "risk management",
            "risk identification",
            "audit",
            "auditing",
            "trustworthiness",
            "trustworthy",
            "fairness",
            "bias",
            "responsible",
            "financial advisement",
            "financial advice",
            "financial advisor",
            "financial advisors",
            "retirement",
            "anomaly detection",
            "safety",
            "safe",
            "governance",
            "banking",
            "accounting",
            "underlying asset review",
            "underlying asset reviews",
        ]
        llm_terms = [
            "large language",
            "llm",
            "gpt",
            "chatgpt",
            "language model",
            "generative ai",
            "foundation model",
            "agent",
            "benchmark",
        ]
        excluded = [
            "healthcare",
            "medical",
            "legal domain",
            "software engineering",
            "generic",
            "supply chain",
            "education",
            "marketing",
            "digital governance",
            "business intelligence",
        ]
        if year < 2023:
            return False
        if any(term in title for term in excluded):
            return False
        if not any(term in title for term in finance_title_terms):
            return False
        if not any(term in title for term in regtech_title_terms):
            return False
        if not any(term in text for term in finance_terms):
            return False
        if not any(term in text for term in regtech_terms):
            return False
        if not any(term in text for term in llm_terms):
            return False
        return citations >= 2 or score >= 16 or hits >= 2

    regtech_focus_promoted = 0
    for candidate in regtech_focus_candidates:
        if regtech_focus_promoted >= 20:
            break
        if should_promote_regtech_focus(candidate):
            add(curated_row_from_candidate(candidate, "regtech_compliance_focus_promoted"))
            regtech_focus_promoted += 1

    def should_promote_specific_domain_focus(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        text = f"{title} {candidate.get('abstract', '').lower()}"
        venue = candidate.get("venue", "").lower()
        year = to_int(candidate.get("year", "0"))
        citations = to_int(candidate.get("citationCount", "0"))
        score = float(candidate.get("score", "0") or 0)
        hits = to_int(candidate.get("seed_hit_count", "0"))
        llm_terms = [
            "large language",
            "llm",
            "gpt",
            "chatgpt",
            "generative ai",
            "language model",
            "finbert",
            "retrieval",
            "retrieve-augmented",
            "agent",
            "benchmark",
        ]
        finance_terms = [
            "finance",
            "financial",
            "investment",
            "investing",
            "market",
            "equity",
            "portfolio",
            "asset",
            "stock",
            "returns",
            "repayment risk",
            "firm",
            "annual report",
            "company",
        ]
        strong_titles = [
            "cn-buzz2portfolio",
            "leveraging internet-sourced text data for financial analytics in supply chain finance",
            "from text to risk: predicting repayment risk in supply chain finance",
            "measuring firm-level supply chain risk using a generative large language model",
            "benchmarking large language models for supply chain risk identification",
            "event identification for supply chain risk management through news analysis",
            "equity research chatbot using llm",
            "measuring corporate risk using large language model embeddings",
            "finkario: event-enhanced automated construction of financial knowledge graph",
            "finbert2: a specialized bidirectional encoder",
            "your ai, not your view",
            "shield: llm-driven schema induction",
            "fine-tuning and explaining finbert for sector-specific financial news",
            "measuring climate risk with chatgpt",
            "sentiment-driven prediction of financial returns",
        ]
        excluded_titles = [
            "large language model supply chain",
            "understanding large language model supply chain",
            "bloomberggpt: revolutionizing finance",
            "from defi to intelligent supply chain finance",
            "industrial applications of large language models",
            "machine learning in supply chain management",
            "development and implementation of systems based on llm in finance",
            "ai applications in project-based supply chain coordination",
            "the potential of large language models in supply chain management",
            "utilizing large language models for text-based industry classification",
            "enhancing equity research with ai: a langchain-based news analysis framework",
            "active vs passive investing",
            "potential of large language models in blockchain-based supply chain finance",
        ]
        noise_terms = [
            "software supply chain",
            "model supply chain",
            "llm supply chain",
            "security perspective",
            "vulnerabilities",
            "quantum finance prospects",
            "blockchain-based supply chain finance",
            "global strategic business report",
            "market research report",
            "high school science",
            "white paper",
        ]
        supply_chain_finance_titles = [
            "supply chain finance",
            "repayment risk",
            "firm-level supply chain risk",
            "supply chain risk identification",
            "supply chain risk management through news analysis",
            "supply chain disruptions",
            "supply chain risk early warning",
        ]
        sector_investment_titles = [
            "sector asset allocation",
            "macro and sector asset allocation",
            "sector-specific financial news",
            "equity research",
            "investment analysis",
            "financial analytics",
            "financial returns",
            "etf",
            "exchange-traded fund",
        ]
        if year < 2024:
            return False
        if any(term in title for term in excluded_titles):
            return False
        if any(term in title for term in noise_terms) or any(term in venue for term in ["high school science"]):
            return False
        if not any(term in text for term in llm_terms):
            return False
        if any(term in title for term in strong_titles):
            return True
        if not any(term in text for term in finance_terms):
            return False
        has_supply_chain_finance = any(term in title for term in supply_chain_finance_titles) and (
            "finance" in text or "financial" in text or "annual report" in text or "market value" in text
        )
        has_sector_investment = any(term in title for term in sector_investment_titles)
        if not (has_supply_chain_finance or has_sector_investment):
            return False
        return citations >= 2 or score >= 28 or hits >= 2

    specific_domain_promoted = 0
    for candidate in specific_domain_search_candidates + specific_domain_focus_candidates:
        if specific_domain_promoted >= 18:
            break
        if should_promote_specific_domain_focus(candidate):
            add(curated_row_from_candidate(candidate, "specific_domain_focus_promoted"))
            specific_domain_promoted += 1

    def should_promote_specific_domain_round2(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        critic_approved_titles = [
            "findkg: dynamic knowledge graphs with large language models for detecting global trends in financial markets",
            "finripple: aligning large language models with financial market for event ripple effect awareness",
            "risk factor extraction in financial disclosures via a knowledge graph-enhanced language model",
            "finkg: a core financial knowledge graph for financial analysis",
            "naturekg: an ontology and knowledge graph for nature finance with a text2cypher application",
        ]
        return any(term in title for term in critic_approved_titles)

    specific_domain_round2_promoted = 0
    for candidate in specific_domain_round2_candidates:
        if specific_domain_round2_promoted >= 12:
            break
        if should_promote_specific_domain_round2(candidate):
            add(curated_row_from_candidate(candidate, "specific_domain_round2_promoted"))
            specific_domain_round2_promoted += 1

    def should_promote_specific_domain_round3(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        critic_approved_titles = [
            "finreflectkg: agentic construction and evaluation of financial knowledge graphs",
            "fincare: financial causal analysis with reasoning and evidence",
            "modal-adaptive knowledge-enhanced graph-based financial prediction from monetary policy conference calls with llm",
            "interpreting fedspeak with confidence: a llm-based uncertainty-aware framework guided by monetary policy transmission paths",
            "exploring the in-context learning capabilities of llms for money laundering detection in financial graphs",
        ]
        return any(term in title for term in critic_approved_titles)

    specific_domain_round3_promoted = 0
    for candidate in specific_domain_round3_candidates:
        if specific_domain_round3_promoted >= 8:
            break
        if should_promote_specific_domain_round3(candidate):
            add(curated_row_from_candidate(candidate, "specific_domain_round3_promoted"))
            specific_domain_round3_promoted += 1

    def should_promote_institutional_trading_focus(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        text = f"{title} {candidate.get('abstract', '').lower()}"
        venue = candidate.get("venue", "").lower()
        year = to_int(candidate.get("year", "0"))
        llm_terms = [
            "large language",
            "llm",
            "gpt",
            "chatgpt",
            "generative ai",
            "language model",
            "agent",
            "benchmark",
            "rag",
            "retrieval",
            "reasoning",
        ]
        critic_style_whitelist = [
            "polybench: benchmarking llm forecasting and trading capabilities on live prediction market data",
            "dynamic hedging strategies in derivatives markets with llm-driven sentiment and news analytics",
            "finsheet-bench: from simple lookups to complex reasoning, where llms break on financial spreadsheets",
            "financeqa: a benchmark for evaluating financial analysis capabilities of large language models",
            "biased echoes: large language models reinforce investment biases and increase portfolio risks of private investors",
            "the gaining paths to investment success: information-driven llm graph reasoning for venture capital prediction",
            "stocksim: a dual-mode order-level simulator for evaluating multi-agent llms in financial markets",
            "a multi-agent orchestration framework for venture capital due diligence",
            "from natural language to executable option strategies via large language models",
            "a multi-agent approach to investor profiling using large language models",
            "polyswarm: a multi-agent large language model framework for prediction market trading and latency arbitrage",
            "alphaforgebench: benchmarking end-to-end trading strategy design with large language models",
            "agent trading arena: a study on numerical understanding in llm-based agents",
            "can large language models effectively process and execute financial trading instructions?",
            "quantcode-bench: a benchmark for evaluating the ability of large language models to generate executable algorithmic trading strategies",
            "deepfinllm: an intelligent financial advisor unleashing strategic insights with large language models",
            "chatgpt as a financial advisor: a re-examination",
            "llm-guided evolutionary strategy generation for quantitative trading",
            "mm-drex: multimodal-driven dynamic routing of llm experts for financial trading",
            "application of startup success prediction models and business document extraction using large language models to enhance due diligence efficiency",
        ]
        excluded = [
            "treatment options",
            "dermatological",
            "clinical",
            "medical",
            "melanoma",
            "nutrition",
            "inpatient",
            "eda",
            "chip",
            "system-on-chip",
            "energy trading",
            "electricity trading",
            "carbon trading",
            "cancer drug",
            "option pricing error mitigation",
            "arbitrage-aware 3d implied volatility",
            "deep bsde",
            "expected utility insight",
            "currency hedging strategies",
            "causes of indian investor",
            "portfolio dollarization",
            "student-scientists",
            "gender and racial bias",
        ]
        if year and year < 2024:
            return False
        if any(term in title for term in excluded) or "student-scientists" in venue:
            return False
        if not any(term in text for term in llm_terms):
            return False
        return any(term in title for term in critic_style_whitelist)

    institutional_trading_promoted = 0
    for candidate in institutional_trading_search_candidates + institutional_trading_focus_candidates:
        if institutional_trading_promoted >= 22:
            break
        if should_promote_institutional_trading_focus(candidate):
            add(curated_row_from_candidate(candidate, "institutional_trading_focus_promoted"))
            institutional_trading_promoted += 1

    def should_promote_institutional_trading_round2(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        critic_review_whitelist = [
            "deltahedge: a multi-agent framework for portfolio options optimization",
            "alphaagent: llm-driven alpha mining with regularized exploration to counteract alpha decay",
            "navigating the alpha jungle: an llm-powered mcts framework for formulaic factor mining",
            "can large language models mine interpretable financial factors more effectively?",
            "jax-lob: a gpu-accelerated limit order book simulator to unlock large scale reinforcement learning for trading",
            "abides: towards high-fidelity multi-agent market simulation",
            "a fused large language model for predicting startup success",
            "beyond isolated investor: predicting startup success via roleplay-based collective agents",
            "finagent: a multimodal foundation agent for financial trading",
        ]
        return any(term in title for term in critic_review_whitelist)

    institutional_trading_round2_promoted = 0
    for candidate in institutional_trading_round2_candidates:
        if institutional_trading_round2_promoted >= 12:
            break
        if should_promote_institutional_trading_round2(candidate):
            add(curated_row_from_candidate(candidate, "institutional_trading_round2_promoted"))
            institutional_trading_round2_promoted += 1

    def should_promote_institutional_trading_round3(candidate: dict[str, str]) -> bool:
        title = candidate.get("title", "").lower()
        critic_review_whitelist = [
            "multi-agent llm framework for formulaic alpha generation and selection in quantitative trading",
            "quantaalpha: an evolutionary framework for llm-driven alpha mining",
            "alphaprobe: alpha mining via principled retrieval and on-graph biased evolution",
            "factorengine: a program-level knowledge-infused factor mining framework for quantitative investment",
            "cognitive alpha mining via llm-driven code-based evolution",
            "factormad: a multi-agent debate framework based on large language models for interpretable stock alpha factor mining",
            "alphacrafter: a full-stack multi-agent framework for cross-sectional quantitative trading",
            "tradefm: a generative foundation model for trade-flow and market microstructure",
            "lob-bench: benchmarking generative ai for finance - an application to limit order book data",
            "strategic complexity and behavioral distortion: retail investing under large language model augmentation",
        ]
        return any(term in title for term in critic_review_whitelist)

    institutional_trading_round3_promoted = 0
    for candidate in institutional_trading_round3_candidates:
        if institutional_trading_round3_promoted >= 12:
            break
        if should_promote_institutional_trading_round3(candidate):
            add(curated_row_from_candidate(candidate, "institutional_trading_round3_promoted"))
            institutional_trading_round3_promoted += 1
    return curated


def write_readme(
    seeds: list[dict[str, str]],
    candidates: list[dict[str, str]],
    curated: list[dict[str, str]],
    round2_candidates: list[dict[str, str]],
    taxonomy_rows: list[dict[str, str]],
) -> None:
    taxonomy_by_category: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in taxonomy_rows:
        taxonomy_by_category[row["taxonomy_category"]].append(row)

    lines = [
        "# Awesome LLM for Finance",
        "",
        "A curated reading list for large language models in finance: financial-domain LLMs, benchmarks, SEC filing analysis, financial reasoning, trading agents, investment research, and professional finance evaluation.",
        "",
        "## Taxonomy",
        "",
        "Each paper is assigned to exactly one primary category. The taxonomy is intentionally a partition: the total number of papers in the categories below equals the total rows in `data/processed/curated_papers.csv`.",
        "",
    ]
    for category in TAXONOMY_ORDER:
        count = len(taxonomy_by_category.get(category, []))
        lines.append(f"- **{category}** ({count}) - {TAXONOMY_DESCRIPTIONS[category]}")
    lines.extend(
        [
            "",
            "## Trading Subthemes",
            "",
            "Trading and investment papers are also tagged with a finer `trading_subtheme` field in `data/processed/curated_papers_by_taxonomy.csv`. These high-precision tags separate the current collection into more useful institutional-investing slices; broad finance papers are tagged `Not Trading Focused` and omitted from the counts below.",
            "",
        ]
    )
    for subtheme in TRADING_SUBTHEME_ORDER:
        if subtheme == "Not Trading Focused":
            continue
        count = sum(1 for row in taxonomy_rows if row.get("trading_subtheme") == subtheme)
        if count:
            lines.append(f"- **{subtheme}** ({count}) - {TRADING_SUBTHEME_DESCRIPTIONS[subtheme]}")
    lines.extend(
        [
            "",
            "## Contents",
            "",
        ]
    )
    for category in TAXONOMY_ORDER:
        count = len(taxonomy_by_category.get(category, []))
        anchor = category.lower().replace("&", "").replace(",", "").replace(" ", "-")
        lines.append(f"- [{category}](#{anchor}) ({count})")
    lines.extend(
        [
            "",
            "## Papers by Theme",
            "",
        ]
    )

    for category in TAXONOMY_ORDER:
        items = taxonomy_by_category.get(category, [])
        if not items:
            continue
        lines.extend([f"### {category}", ""])
        for row in sorted(
            items,
            key=lambda x: (
                x.get("priority", "P9"),
                -to_int(x.get("citationCount", "0")),
                x.get("approx_year", ""),
                x.get("title", ""),
            ),
        ):
            lines.append(
                f"- {markdown_link(row.get('title', ''), row.get('source_url', ''))} "
                f"({row.get('approx_year', 'n.d.')}) - `{row.get('priority', '')}` "
                f"- citations: {row.get('citationCount', '0')}"
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
            "Paper titles, links, citation counts, abstracts, and third-party metadata remain subject to their original rights and provider terms.",
            "",
        ]
    )
    README_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    seeds = read_csv(SEED_PATH)
    first_round_edges = read_csv(EDGES_PATH)
    round2_edges = normalize_round_edges(read_csv(ROUND2_EDGES_PATH), "round2", "round2_related_work_edges.csv")
    round3_edges = normalize_round_edges(read_csv(ROUND3_EDGES_PATH), "round3", "round3_related_work_edges.csv")
    round4_edges = normalize_round_edges(read_csv(ROUND4_EDGES_PATH), "round4", "round4_related_work_edges.csv")
    trading_focus_edges = normalize_round_edges(
        read_csv(TRADING_AGENT_FOCUS_EDGES_PATH),
        "trading_agent_focus",
        "trading_agent_focus_edges.csv",
    )
    report_focus_edges = normalize_round_edges(
        read_csv(REPORT_ANALYSIS_FOCUS_EDGES_PATH),
        "report_analysis_focus",
        "report_analysis_focus_edges.csv",
    )
    regtech_focus_edges = normalize_round_edges(
        read_csv(REGTECH_COMPLIANCE_FOCUS_EDGES_PATH),
        "regtech_compliance_focus",
        "regtech_compliance_focus_edges.csv",
    )
    specific_domain_focus_edges = normalize_round_edges(
        read_csv(SPECIFIC_DOMAIN_FOCUS_EDGES_PATH),
        "specific_domain_focus",
        "specific_domain_focus_edges.csv",
    )
    specific_domain_round2_edges = normalize_round_edges(
        read_csv(SPECIFIC_DOMAIN_ROUND2_EDGES_PATH),
        "specific_domain_round2",
        "specific_domain_round2_edges.csv",
    )
    specific_domain_round3_edges = normalize_round_edges(
        read_csv(SPECIFIC_DOMAIN_ROUND3_EDGES_PATH),
        "specific_domain_round3",
        "specific_domain_round3_edges.csv",
    )
    institutional_trading_focus_edges = normalize_round_edges(
        read_csv(INSTITUTIONAL_TRADING_FOCUS_EDGES_PATH),
        "institutional_trading_focus",
        "institutional_trading_focus_edges.csv",
    )
    institutional_trading_round2_edges = normalize_round_edges(
        read_csv(INSTITUTIONAL_TRADING_ROUND2_EDGES_PATH),
        "institutional_trading_round2",
        "institutional_trading_round2_edges.csv",
    )
    institutional_trading_round3_edges = normalize_round_edges(
        read_csv(INSTITUTIONAL_TRADING_ROUND3_EDGES_PATH),
        "institutional_trading_round3",
        "institutional_trading_round3_edges.csv",
    )
    edges = (
        first_round_edges
        + round2_edges
        + round3_edges
        + round4_edges
        + trading_focus_edges
        + report_focus_edges
        + regtech_focus_edges
        + specific_domain_focus_edges
        + specific_domain_round2_edges
        + specific_domain_round3_edges
        + institutional_trading_focus_edges
        + institutional_trading_round2_edges
        + institutional_trading_round3_edges
    )
    round2_manifest_rows = read_csv(ROUND2_MANIFEST_PATH)
    round3_manifest_rows = read_csv(ROUND3_MANIFEST_PATH)
    round4_manifest_rows = read_csv(ROUND4_MANIFEST_PATH)
    trading_focus_manifest_rows = read_csv(TRADING_AGENT_FOCUS_MANIFEST_PATH)
    trading_focus_seed_candidates = read_csv(TRADING_AGENT_FOCUS_SEEDS_PATH)
    report_focus_manifest_rows = read_csv(REPORT_ANALYSIS_FOCUS_MANIFEST_PATH)
    report_focus_seed_candidates = read_csv(REPORT_ANALYSIS_FOCUS_SEEDS_PATH)
    regtech_focus_manifest_rows = read_csv(REGTECH_COMPLIANCE_FOCUS_MANIFEST_PATH)
    specific_domain_focus_manifest_rows = read_csv(SPECIFIC_DOMAIN_FOCUS_MANIFEST_PATH)
    specific_domain_search_candidates = read_csv(SPECIFIC_DOMAIN_FOCUS_SEARCH_PATH)
    specific_domain_round2_manifest_rows = read_csv(SPECIFIC_DOMAIN_ROUND2_MANIFEST_PATH)
    specific_domain_round3_manifest_rows = read_csv(SPECIFIC_DOMAIN_ROUND3_MANIFEST_PATH)
    institutional_trading_focus_manifest_rows = read_csv(INSTITUTIONAL_TRADING_FOCUS_MANIFEST_PATH)
    institutional_trading_search_candidates = read_csv(INSTITUTIONAL_TRADING_FOCUS_SEARCH_PATH)
    institutional_trading_round2_manifest_rows = read_csv(INSTITUTIONAL_TRADING_ROUND2_MANIFEST_PATH)
    institutional_trading_round3_manifest_rows = read_csv(INSTITUTIONAL_TRADING_ROUND3_MANIFEST_PATH)
    candidates, longlist = build_candidates(seeds, edges)
    round2_seed_rows = manifest_as_seed_rows(round2_manifest_rows)
    round2_candidates, _round2_longlist = build_candidates(
        seeds + round2_seed_rows, round2_edges
    )
    curated_before_round3 = build_curated_papers(seeds, longlist, round2_manifest_rows, round2_candidates)
    round3_seed_rows = manifest_as_seed_rows(round3_manifest_rows)
    round3_candidates, _round3_longlist = build_candidates(
        seeds + curated_as_seed_rows(curated_before_round3) + round3_seed_rows,
        round3_edges,
    )
    curated_before_round4 = build_curated_papers(
        seeds,
        longlist + round2_candidates + round3_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
    )
    round4_seed_rows = manifest_as_seed_rows(round4_manifest_rows)
    round4_candidates, _round4_longlist = build_candidates(
        seeds + curated_as_seed_rows(curated_before_round4) + round4_seed_rows,
        round4_edges,
    )
    curated_before_trading_focus = build_curated_papers(
        seeds,
        longlist + round2_candidates + round3_candidates + round4_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
    )
    trading_focus_seed_rows = manifest_as_seed_rows(trading_focus_manifest_rows)
    trading_focus_candidates, _trading_focus_longlist = build_candidates(
        seeds + curated_as_seed_rows(curated_before_trading_focus) + trading_focus_seed_rows,
        trading_focus_edges,
    )
    curated_before_report_focus = build_curated_papers(
        seeds,
        longlist + round2_candidates + round3_candidates + round4_candidates + trading_focus_seed_candidates + trading_focus_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
    )
    report_focus_seed_rows = manifest_as_seed_rows(report_focus_manifest_rows)
    report_focus_candidates, _report_focus_longlist = build_candidates(
        seeds + curated_as_seed_rows(curated_before_report_focus) + report_focus_seed_rows,
        report_focus_edges,
    )
    curated_before_regtech_focus = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
    )
    regtech_focus_seed_rows = manifest_as_seed_rows(regtech_focus_manifest_rows)
    regtech_focus_candidates, _regtech_focus_longlist = build_candidates(
        seeds + curated_as_seed_rows(curated_before_regtech_focus) + regtech_focus_seed_rows,
        regtech_focus_edges,
    )
    curated_before_specific_domain_focus = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
    )
    specific_domain_focus_seed_rows = manifest_as_seed_rows(specific_domain_focus_manifest_rows)
    specific_domain_focus_candidates, _specific_domain_focus_longlist = build_candidates(
        seeds + curated_as_seed_rows(curated_before_specific_domain_focus) + specific_domain_focus_seed_rows,
        specific_domain_focus_edges,
    )
    curated_before_specific_domain_round2 = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates
        + specific_domain_search_candidates
        + specific_domain_focus_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
        specific_domain_search_candidates,
        specific_domain_focus_candidates,
    )
    specific_domain_round2_seed_rows = manifest_as_seed_rows(specific_domain_round2_manifest_rows)
    specific_domain_round2_candidates, _specific_domain_round2_longlist = build_candidates(
        seeds
        + curated_as_seed_rows(curated_before_specific_domain_round2)
        + specific_domain_round2_seed_rows,
        specific_domain_round2_edges,
    )
    curated_before_specific_domain_round3 = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates
        + specific_domain_search_candidates
        + specific_domain_focus_candidates
        + specific_domain_round2_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
        specific_domain_search_candidates,
        specific_domain_focus_candidates,
        specific_domain_round2_candidates,
    )
    specific_domain_round3_seed_rows = manifest_as_seed_rows(specific_domain_round3_manifest_rows)
    specific_domain_round3_candidates, _specific_domain_round3_longlist = build_candidates(
        seeds
        + curated_as_seed_rows(curated_before_specific_domain_round3)
        + specific_domain_round3_seed_rows,
        specific_domain_round3_edges,
    )
    curated_before_institutional_trading_focus = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates
        + specific_domain_search_candidates
        + specific_domain_focus_candidates
        + specific_domain_round2_candidates
        + specific_domain_round3_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
        specific_domain_search_candidates,
        specific_domain_focus_candidates,
        specific_domain_round2_candidates,
        specific_domain_round3_candidates,
    )
    institutional_trading_focus_seed_rows = manifest_as_seed_rows(institutional_trading_focus_manifest_rows)
    institutional_trading_focus_candidates, _institutional_trading_focus_longlist = build_candidates(
        seeds
        + curated_as_seed_rows(curated_before_institutional_trading_focus)
        + institutional_trading_focus_seed_rows,
        institutional_trading_focus_edges,
    )
    curated_before_institutional_trading_round2 = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates
        + specific_domain_search_candidates
        + specific_domain_focus_candidates
        + specific_domain_round2_candidates
        + specific_domain_round3_candidates
        + institutional_trading_search_candidates
        + institutional_trading_focus_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
        specific_domain_search_candidates,
        specific_domain_focus_candidates,
        specific_domain_round2_candidates,
        specific_domain_round3_candidates,
        institutional_trading_search_candidates,
        institutional_trading_focus_candidates,
    )
    institutional_trading_round2_seed_rows = manifest_as_seed_rows(institutional_trading_round2_manifest_rows)
    institutional_trading_round2_candidates, _institutional_trading_round2_longlist = build_candidates(
        seeds
        + curated_as_seed_rows(curated_before_institutional_trading_round2)
        + institutional_trading_round2_seed_rows,
        institutional_trading_round2_edges,
    )
    curated_before_institutional_trading_round3 = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates
        + specific_domain_search_candidates
        + specific_domain_focus_candidates
        + specific_domain_round2_candidates
        + specific_domain_round3_candidates
        + institutional_trading_search_candidates
        + institutional_trading_focus_candidates
        + institutional_trading_round2_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
        specific_domain_search_candidates,
        specific_domain_focus_candidates,
        specific_domain_round2_candidates,
        specific_domain_round3_candidates,
        institutional_trading_search_candidates,
        institutional_trading_focus_candidates,
        institutional_trading_round2_candidates,
    )
    institutional_trading_round3_seed_rows = manifest_as_seed_rows(institutional_trading_round3_manifest_rows)
    institutional_trading_round3_candidates, _institutional_trading_round3_longlist = build_candidates(
        seeds
        + curated_as_seed_rows(curated_before_institutional_trading_round3)
        + institutional_trading_round3_seed_rows,
        institutional_trading_round3_edges,
    )
    curated = build_curated_papers(
        seeds,
        longlist
        + round2_candidates
        + round3_candidates
        + round4_candidates
        + trading_focus_seed_candidates
        + trading_focus_candidates
        + report_focus_seed_candidates
        + report_focus_candidates
        + regtech_focus_candidates
        + specific_domain_search_candidates
        + specific_domain_focus_candidates
        + specific_domain_round2_candidates
        + specific_domain_round3_candidates
        + institutional_trading_search_candidates
        + institutional_trading_focus_candidates
        + institutional_trading_round2_candidates
        + institutional_trading_round3_candidates,
        round2_manifest_rows,
        round2_candidates,
        round3_manifest_rows,
        round3_candidates,
        round4_manifest_rows,
        round4_candidates,
        trading_focus_seed_candidates,
        trading_focus_candidates,
        report_focus_seed_candidates,
        report_focus_candidates,
        regtech_focus_candidates,
        specific_domain_search_candidates,
        specific_domain_focus_candidates,
        specific_domain_round2_candidates,
        specific_domain_round3_candidates,
        institutional_trading_search_candidates,
        institutional_trading_focus_candidates,
        institutional_trading_round2_candidates,
        institutional_trading_round3_candidates,
    )
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
    write_csv(ROUND3_CANDIDATES_PATH, round3_candidates, columns)
    write_csv(ROUND4_CANDIDATES_PATH, round4_candidates, columns)
    write_csv(TRADING_AGENT_FOCUS_CANDIDATES_PATH, trading_focus_candidates, columns)
    write_csv(REPORT_ANALYSIS_FOCUS_CANDIDATES_PATH, report_focus_candidates, columns)
    write_csv(REGTECH_COMPLIANCE_FOCUS_CANDIDATES_PATH, regtech_focus_candidates, columns)
    write_csv(SPECIFIC_DOMAIN_FOCUS_CANDIDATES_PATH, specific_domain_focus_candidates, columns)
    write_csv(SPECIFIC_DOMAIN_ROUND2_CANDIDATES_PATH, specific_domain_round2_candidates, columns)
    write_csv(SPECIFIC_DOMAIN_ROUND3_CANDIDATES_PATH, specific_domain_round3_candidates, columns)
    write_csv(INSTITUTIONAL_TRADING_FOCUS_CANDIDATES_PATH, institutional_trading_focus_candidates, columns)
    write_csv(INSTITUTIONAL_TRADING_ROUND2_CANDIDATES_PATH, institutional_trading_round2_candidates, columns)
    write_csv(INSTITUTIONAL_TRADING_ROUND3_CANDIDATES_PATH, institutional_trading_round3_candidates, columns)
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
    taxonomy_rows = apply_taxonomy(curated)
    taxonomy_columns = curated_columns + [
        "taxonomy_category",
        "taxonomy_description",
        "trading_subtheme",
        "trading_subtheme_description",
    ]
    write_csv(TAXONOMY_PATH, taxonomy_rows, taxonomy_columns)
    write_readme(seeds, candidates, curated, round2_candidates, taxonomy_rows)
    print(f"seeds={len(seeds)}")
    print(f"first_round_edges={len(first_round_edges)}")
    print(f"round2_edges={len(round2_edges)}")
    print(f"round3_edges={len(round3_edges)}")
    print(f"round4_edges={len(round4_edges)}")
    print(f"trading_agent_focus_edges={len(trading_focus_edges)}")
    print(f"report_analysis_focus_edges={len(report_focus_edges)}")
    print(f"regtech_compliance_focus_edges={len(regtech_focus_edges)}")
    print(f"specific_domain_focus_edges={len(specific_domain_focus_edges)}")
    print(f"specific_domain_round2_edges={len(specific_domain_round2_edges)}")
    print(f"specific_domain_round3_edges={len(specific_domain_round3_edges)}")
    print(f"institutional_trading_focus_edges={len(institutional_trading_focus_edges)}")
    print(f"institutional_trading_round2_edges={len(institutional_trading_round2_edges)}")
    print(f"institutional_trading_round3_edges={len(institutional_trading_round3_edges)}")
    print(f"edges={len(edges)}")
    print(f"candidates={len(candidates)}")
    print(f"round2_candidates={len(round2_candidates)}")
    print(f"round3_candidates={len(round3_candidates)}")
    print(f"round4_candidates={len(round4_candidates)}")
    print(f"trading_agent_focus_candidates={len(trading_focus_candidates)}")
    print(f"report_analysis_focus_candidates={len(report_focus_candidates)}")
    print(f"regtech_compliance_focus_candidates={len(regtech_focus_candidates)}")
    print(f"specific_domain_focus_search_candidates={len(specific_domain_search_candidates)}")
    print(f"specific_domain_focus_candidates={len(specific_domain_focus_candidates)}")
    print(f"specific_domain_round2_candidates={len(specific_domain_round2_candidates)}")
    print(f"specific_domain_round3_candidates={len(specific_domain_round3_candidates)}")
    print(f"institutional_trading_focus_search_candidates={len(institutional_trading_search_candidates)}")
    print(f"institutional_trading_focus_candidates={len(institutional_trading_focus_candidates)}")
    print(f"institutional_trading_round2_candidates={len(institutional_trading_round2_candidates)}")
    print(f"institutional_trading_round3_candidates={len(institutional_trading_round3_candidates)}")
    print(f"longlist={len(longlist)}")
    print(f"curated={len(curated)}")
    print(f"taxonomy={len(taxonomy_rows)}")
    print(f"wrote={CANDIDATES_PATH}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Retag existing paper summaries without regenerating summaries.

This script preserves summary text fields and only updates tagging metadata:
tags, tag_facets, evidence_type, summary_coverage, tagging_confidence, and
tagging_schema_version. Generated summary artifacts remain git-ignored.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
import unicodedata
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_JSONL = ROOT / "data" / "processed" / "paper_summaries.jsonl"
SUMMARY_CSV = ROOT / "data" / "processed" / "paper_summaries.csv"
SUMMARY_REPORT = ROOT / "reports" / "paper_summaries.md"
DEFAULT_MODEL = os.environ.get("LOCAL_LLM_MODEL", "Qwen/Qwen3.6-35B-A3B")
DEFAULT_BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://192.168.50.18:31969/v1")
DEFAULT_TOKEN = os.environ.get("LOCAL_LLM_TOKEN", "1969")
TAGGING_SCHEMA_VERSION = "controlled-facets-v1"


TEXT_SUMMARY_FIELDS = {
    "one_sentence_summary",
    "detailed_summary",
    "research_problem",
    "core_contributions",
    "data_and_experiments",
    "important_abstract_and_results",
    "deliverables",
    "method",
    "taxonomy_rationale",
    "survey_relevance_notes",
    "paywall_or_full_text_notes",
    "limitations_or_caveats",
}

TAG_FIELDS = {
    "tags",
    "tag_facets",
    "evidence_type",
    "summary_coverage",
    "tagging_confidence",
    "tagging_schema_version",
}

FORBIDDEN_TAGS = {
    "finance",
    "financial",
    "financial nlp",
    "llm",
    "large language model",
    "large language models",
    "machine learning",
    "artificial intelligence",
    "research",
    "paper",
    "study",
    "survey",
    "risk management",
    "financial analysis",
    "financial reasoning",
    "financial agents",
    "llm agents",
    "llm finance",
    "quantitative finance",
    "financial rag",
    "rag",
    "not trading focused",
    "gpt-4",
    "gpt-4o",
    "llama-3",
    "llama 3",
    "qwen",
    "qwen3",
    "chatgpt",
}

TAG_SYNONYMS = {
    "llms": "llm",
    "large language model": "llm",
    "large language models": "llm",
    "retrieval augmented generation": "rag",
    "retrieval-augmented generation": "rag",
    "multi agent": "multi-agent systems",
    "multi agent systems": "multi-agent systems",
    "multi-agent system": "multi-agent systems",
    "portfolio construction": "portfolio optimization",
    "qa": "financial question answering",
    "financial qa": "financial question answering",
    "question answering": "financial question answering",
    "orderbook": "limit order book",
    "order book": "limit order book",
    "high frequency trading": "high-frequency trading",
    "few shot learning": "few-shot learning",
    "zero shot learning": "zero-shot learning",
    "chain-of-thought": "chain of thought",
    "parameter efficient fine tuning": "parameter-efficient fine-tuning",
    "alpha factor mining": "alpha mining",
    "factor discovery": "alpha mining",
    "factor generation": "alpha mining",
}

ALLOWED_FACETS = {
    "task": {
        "alpha mining",
        "algorithmic trading",
        "benchmarking",
        "credit scoring",
        "derivatives hedging",
        "due diligence",
        "earnings analysis",
        "equity research",
        "execution analysis",
        "factor modeling",
        "financial question answering",
        "forecasting",
        "fraud detection",
        "investment advisory",
        "market simulation",
        "portfolio optimization",
        "regulatory reporting",
        "risk extraction",
        "sentiment analysis",
        "spreadsheet reasoning",
        "startup prediction",
        "stock prediction",
        "strategy generation",
        "xbrl tagging",
    },
    "method": {
        "agent debate",
        "agentic workflow",
        "backtesting",
        "chain of thought",
        "domain adaptation",
        "fine-tuning",
        "graph reasoning",
        "instruction tuning",
        "knowledge graph",
        "mcts",
        "multi-agent systems",
        "multimodal modeling",
        "prompt engineering",
        "rag",
        "reinforcement learning",
        "retrieval",
        "semantic parsing",
        "symbolic regression",
        "time-series modeling",
        "tool use",
    },
    "asset_class": {
        "bonds",
        "commodities",
        "crypto",
        "derivatives",
        "equities",
        "etfs",
        "forex",
        "mutual funds",
        "options",
        "prediction markets",
        "private markets",
        "public reits",
        "structured products",
        "venture capital",
    },
    "market_context": {
        "a-share market",
        "china market",
        "cross-sectional equities",
        "earnings season",
        "high-frequency trading",
        "institutional investing",
        "market microstructure",
        "portfolio management",
        "retail investing",
        "sector allocation",
        "supply chain finance",
        "us equities",
    },
    "data_source": {
        "10-k filings",
        "annual reports",
        "earnings calls",
        "financial statements",
        "limit order book",
        "market prices",
        "news",
        "ohlc data",
        "private company data",
        "sec filings",
        "social media",
        "tables",
        "xbrl",
    },
    "evaluation": {
        "ablation study",
        "accuracy",
        "backtest",
        "drawdown",
        "hit ratio",
        "information ratio",
        "live benchmark",
        "market impact",
        "portfolio returns",
        "risk-adjusted returns",
        "sharpe ratio",
        "transaction costs",
    },
    "deliverable": {
        "benchmark",
        "dataset",
        "framework",
        "leaderboard",
        "literature review",
        "model",
        "open source",
        "simulator",
        "taxonomy",
        "trading agent",
    },
    "risk_issue": {
        "bias",
        "data leakage",
        "hallucination",
        "look-ahead bias",
        "model risk",
        "overfitting",
        "privacy",
        "regulatory compliance",
        "tail risk",
    },
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def flatten(value: Any) -> str:
    if isinstance(value, list):
        return " | ".join(str(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return "" if value is None else str(value)


def normalize_tag(tag: Any, allow_generic: bool = False) -> str:
    text = unicodedata.normalize("NFKD", str(tag)).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = text.replace("_", " ").replace("/", " ")
    text = re.sub(r"[^a-z0-9+\- ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -")
    text = TAG_SYNONYMS.get(text, text)
    if not text or len(text.split()) > 4:
        return ""
    if re.fullmatch(r"(gpt|llama|qwen|claude|gemini|mistral)[a-z0-9 .\-]*", text):
        return ""
    if not allow_generic and text in FORBIDDEN_TAGS:
        return ""
    return text


def normalize_tag_list(tags: Any, *, allow_generic: bool = False, max_items: int = 6) -> list[str]:
    raw = tags if isinstance(tags, list) else []
    output: list[str] = []
    seen: set[str] = set()
    for tag in raw:
        clean = normalize_tag(tag, allow_generic=allow_generic)
        if clean and clean not in seen:
            output.append(clean)
            seen.add(clean)
        if len(output) >= max_items:
            break
    return output


def coverage_for(row: dict[str, Any]) -> str:
    text_chars = int(row.get("text_char_count") or 0)
    input_chars = int(row.get("model_input_char_count") or 0)
    if text_chars <= 2_000:
        return "abstract_or_fragment"
    if input_chars and text_chars > input_chars:
        return "first_50k_chars"
    return "full_extracted_text"


def confidence_for(row: dict[str, Any], facets: dict[str, list[str]]) -> str:
    coverage = row.get("summary_coverage") or coverage_for(row)
    facet_count = sum(len(v) for v in facets.values())
    if coverage == "abstract_or_fragment" or facet_count < 5:
        return "low"
    if coverage == "first_50k_chars" or facet_count < 9:
        return "medium"
    return "high"


def build_prompt(row: dict[str, Any]) -> str:
    controlled_vocab = {key: sorted(value) for key, value in ALLOWED_FACETS.items()}
    prompt_input = {
        "title": row.get("title", ""),
        "year": row.get("year", ""),
        "taxonomy_category": row.get("taxonomy_category", ""),
        "trading_subtheme": row.get("trading_subtheme", ""),
        "trading_investment_relevance": row.get("trading_investment_relevance", ""),
        "summary_coverage": coverage_for(row),
        "one_sentence_summary": row.get("one_sentence_summary", ""),
        "detailed_summary": row.get("detailed_summary", ""),
        "research_problem": row.get("research_problem", ""),
        "core_contributions": row.get("core_contributions", []),
        "data_and_experiments": row.get("data_and_experiments", []),
        "important_abstract_and_results": row.get("important_abstract_and_results", []),
        "deliverables": row.get("deliverables", []),
        "method": row.get("method", []),
        "limitations_or_caveats": row.get("limitations_or_caveats", []),
    }
    return f"""Retag this paper for a trading/investment-focused Awesome LLM for Finance repository.

Return JSON only. Do not change or rewrite the summary. Use only the supplied paper summary fields.

Task contract:
- Produce controlled multi-facet tags for search and clustering.
- Prefer controlled vocabulary values exactly when they fit.
- Use the controlled vocabulary for tag_facets. Put essential non-vocabulary tags only in specific_tags.
- Tags must describe task, method, asset/market, data source, evaluation, deliverable, or risk issue.
- Do not include broad tags such as: {sorted(FORBIDDEN_TAGS)}.
- Do not include classification-state tags like "not trading focused"; relevance is already a field.
- Do not include author names, venue names, years, or model/provider names such as GPT-4, ChatGPT, Qwen, Llama, Gemini, Claude.
- Do not force trading tags onto survey, governance, ESG, compliance, or generic finance papers. Use only directly supported market/asset tags.
- For survey/review/overview papers, evidence_type must be "survey"; only tag asset_class/market_context when the survey is specifically about that market.
- For trading/investment papers, include concrete market terms when supported: options, hedging, alpha mining, order book, execution, market impact, portfolio optimization, startup due diligence, private markets, venture capital prediction.
- For broad finance/ESG/compliance papers, keep tags precise and do not force them into trading.
- evidence_type must be one of: empirical, benchmark, case study, conceptual, survey, infrastructure.

Output schema:
{{
  "tag_facets": {{
    "task": ["0-5 tags"],
    "method": ["0-5 tags"],
    "asset_class": ["0-4 tags"],
    "market_context": ["0-4 tags"],
    "data_source": ["0-5 tags"],
    "evaluation": ["0-5 tags"],
    "deliverable": ["0-4 tags"],
    "risk_issue": ["0-4 tags"]
  }},
  "specific_tags": ["0-6 extra specific tags not already covered by facets"],
  "evidence_type": "empirical|benchmark|case study|conceptual|survey|infrastructure"
}}

Controlled vocabulary:
{json.dumps(controlled_vocab, ensure_ascii=False, indent=2)}

Paper summary input:
{json.dumps(prompt_input, ensure_ascii=False, indent=2)}
"""


def local_llm_json(prompt: str, model: str, base_url: str, token: str, timeout: int = 180) -> tuple[dict[str, Any] | None, str]:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a strict controlled-vocabulary paper tagging engine. Return valid JSON only."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
        "max_tokens": 1300,
        "chat_template_kwargs": {"enable_thinking": False},
    }
    request = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
        content = json.loads(raw)["choices"][0]["message"]["content"].strip()
    except Exception as exc:
        return None, f"llm_call_failed: {exc}"
    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1 and end > start:
        content = content[start : end + 1]
    try:
        return json.loads(content), content
    except json.JSONDecodeError as exc:
        return None, f"json_parse_failed: {exc}: {content[:500]}"


def normalize_facets(payload: dict[str, Any]) -> dict[str, list[str]]:
    raw_facets = payload.get("tag_facets") if isinstance(payload.get("tag_facets"), dict) else {}
    facets: dict[str, list[str]] = {}
    for facet, allowed in ALLOWED_FACETS.items():
        values = normalize_tag_list(raw_facets.get(facet, []), allow_generic=False, max_items=6)
        facets[facet] = [value for value in values if value in allowed][:6]
    return facets


def combine_tags(facets: dict[str, list[str]], specific_tags: Any) -> list[str]:
    combined: list[str] = []
    seen: set[str] = set()
    priority = [
        "task",
        "asset_class",
        "market_context",
        "method",
        "data_source",
        "evaluation",
        "deliverable",
        "risk_issue",
    ]
    for facet in priority:
        for tag in facets.get(facet, []):
            clean = normalize_tag(tag)
            if clean and clean not in seen:
                combined.append(clean)
                seen.add(clean)
    for tag in normalize_tag_list(specific_tags, max_items=6):
        if tag not in seen:
            combined.append(tag)
            seen.add(tag)
    return combined[:20]


def add_unique(values: list[str], tag: str) -> None:
    if tag not in values:
        values.append(tag)


def remove_values(values: list[str], tags: set[str]) -> None:
    values[:] = [value for value in values if value not in tags]


def deterministic_enrich_facets(
    row: dict[str, Any],
    facets: dict[str, list[str]],
    evidence_type: str,
) -> dict[str, list[str]]:
    """Enforce high-confidence tagging rules found during pilot review."""
    text = " ".join(
        str(row.get(field, ""))
        for field in [
            "title",
            "taxonomy_category",
            "trading_subtheme",
            "detailed_summary",
            "research_problem",
            "data_and_experiments",
            "method",
            "deliverables",
        ]
    ).lower()
    title = str(row.get("title", "")).lower()

    if evidence_type == "survey":
        add_unique(facets["deliverable"], "literature review")
        market_title_terms = {
            "stock",
            "trading",
            "investment",
            "portfolio",
            "equity",
            "equities",
            "market",
            "alpha",
            "hedge",
            "option",
            "derivative",
            "venture capital",
            "startup",
        }
        if not any(term in title for term in market_title_terms):
            facets["asset_class"] = []
            facets["market_context"] = []
            remove_values(
                facets["evaluation"],
                {"backtest", "sharpe ratio", "portfolio returns", "risk-adjusted returns", "drawdown"},
            )

    if any(term in text for term in ["limit order book", "order book", "lob-", " lob ", "market microstructure"]):
        add_unique(facets["data_source"], "limit order book")
        add_unique(facets["market_context"], "market microstructure")
        remove_values(facets["data_source"], {"ohlc data"})

    if any(term in text for term in ["option", "options", "derivative", "derivatives", "structured product"]):
        add_unique(facets["asset_class"], "options")
        add_unique(facets["asset_class"], "derivatives")
    if "hedg" in text and any(term in text for term in ["option", "options", "derivative", "derivatives"]):
        add_unique(facets["task"], "derivatives hedging")

    if any(term in text for term in ["venture capital", "vc ", "startup", "start-up", "private market"]):
        add_unique(facets["asset_class"], "venture capital")
        add_unique(facets["asset_class"], "private markets")
    if any(term in text for term in ["due diligence", "investment memo", "startup evaluation", "venture capital"]):
        add_unique(facets["task"], "due diligence")
    if any(term in text for term in ["startup prediction", "startup success", "venture outcome"]):
        add_unique(facets["task"], "startup prediction")

    if any(term in text for term in ["alpha mining", "alpha factor", "factor mining", "factor discovery"]):
        add_unique(facets["task"], "alpha mining")
        add_unique(facets["task"], "factor modeling")

    if "xbrl" in text:
        add_unique(facets["task"], "xbrl tagging")
        add_unique(facets["data_source"], "xbrl")
        add_unique(facets["data_source"], "sec filings")

    if any(term in text for term in ["spreadsheet", "worksheet", "excel"]):
        add_unique(facets["task"], "spreadsheet reasoning")
        add_unique(facets["data_source"], "tables")

    if "earnings call" in text:
        add_unique(facets["task"], "earnings analysis")
        add_unique(facets["data_source"], "earnings calls")

    for facet in facets:
        facets[facet] = [value for value in facets[facet] if value in ALLOWED_FACETS[facet]][:6]
    return facets


def infer_evidence_type(row: dict[str, Any], candidate: str | None = None) -> str:
    title = str(row.get("title", "")).lower()
    category = str(row.get("taxonomy_category", "")).lower()
    deliverables = " ".join(str(x) for x in row.get("deliverables", [])).lower()
    text = " ".join(
        str(row.get(field, ""))
        for field in ["title", "detailed_summary", "method", "data_and_experiments"]
    ).lower()
    if "surveys and reviews" in category or any(word in title for word in ["survey", "review", "overview", "scoping review"]):
        return "survey"
    if any(word in title for word in ["abides", "jax-lob"]) or "simulator" in deliverables:
        return "infrastructure"
    if "benchmark" in title or "benchmark" in deliverables or "benchmark" in category:
        return "benchmark"
    if "case study" in text:
        return "case study"
    if any(word in text for word in ["conceptual framework", "strategic framework", "does not empirically"]):
        return "conceptual"
    if candidate in {"empirical", "benchmark", "case study", "conceptual", "survey", "infrastructure"}:
        return candidate
    return "empirical"


def fallback_tags(row: dict[str, Any]) -> tuple[dict[str, list[str]], list[str], str]:
    text = " ".join(
        str(row.get(field, ""))
        for field in ["title", "taxonomy_category", "trading_subtheme", "detailed_summary", "method"]
    ).lower()
    facets = {facet: [] for facet in ALLOWED_FACETS}
    rules = [
        ("task", "alpha mining", ["alpha", "factor mining"]),
        ("task", "portfolio optimization", ["portfolio", "asset allocation"]),
        ("task", "stock prediction", ["stock prediction", "stock movement"]),
        ("task", "strategy generation", ["strategy generation", "trading strategy"]),
        ("task", "financial question answering", ["question answering", "qa"]),
        ("task", "xbrl tagging", ["xbrl"]),
        ("task", "due diligence", ["due diligence"]),
        ("task", "derivatives hedging", ["hedging", "option"]),
        ("method", "multi-agent systems", ["multi-agent", "agent"]),
        ("method", "rag", ["rag", "retrieval"]),
        ("method", "reinforcement learning", ["reinforcement learning"]),
        ("method", "fine-tuning", ["fine-tuning", "finetuning"]),
        ("asset_class", "equities", ["stock", "equity", "equities"]),
        ("asset_class", "options", ["option"]),
        ("asset_class", "venture capital", ["venture capital", "startup"]),
        ("market_context", "market microstructure", ["order book", "microstructure"]),
        ("data_source", "10-k filings", ["10-k"]),
        ("data_source", "earnings calls", ["earnings call"]),
        ("data_source", "news", ["news"]),
        ("data_source", "market prices", ["price", "ohlc"]),
        ("evaluation", "backtest", ["backtest"]),
        ("evaluation", "sharpe ratio", ["sharpe"]),
        ("deliverable", "benchmark", ["benchmark"]),
        ("deliverable", "framework", ["framework"]),
        ("risk_issue", "look-ahead bias", ["look-ahead"]),
        ("risk_issue", "hallucination", ["hallucination"]),
    ]
    for facet, tag, needles in rules:
        if any(needle in text for needle in needles) and tag not in facets[facet]:
            facets[facet].append(tag)
    evidence = infer_evidence_type(row)
    facets = deterministic_enrich_facets(row, facets, evidence)
    tags = combine_tags(facets, [])
    return facets, tags, evidence


def retag_one(row: dict[str, Any], model: str, base_url: str, token: str) -> dict[str, Any]:
    prompt = build_prompt(row)
    payload, error = local_llm_json(prompt, model=model, base_url=base_url, token=token)
    if payload is None:
        facets, tags, evidence_type = fallback_tags(row)
        row["tagging_error"] = error
    else:
        facets = normalize_facets(payload)
        evidence_type = infer_evidence_type(row, normalize_tag(payload.get("evidence_type", "")))
        facets = deterministic_enrich_facets(row, facets, evidence_type)
        tags = combine_tags(facets, payload.get("specific_tags", []))
        if len(tags) < 10:
            fallback_facets, fallback_extra, _ = fallback_tags(row)
            for facet, values in fallback_facets.items():
                for value in values:
                    if value not in facets[facet]:
                        facets[facet].append(value)
            facets = deterministic_enrich_facets(row, facets, evidence_type)
            tags = combine_tags(facets, fallback_extra)
    row["tag_facets"] = facets
    row["tags"] = tags[:20]
    row["evidence_type"] = evidence_type
    row["summary_coverage"] = coverage_for(row)
    row["tagging_confidence"] = confidence_for(row, facets)
    row["tagging_schema_version"] = TAGGING_SCHEMA_VERSION
    return row


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "paper_key",
        "title",
        "year",
        "taxonomy_category",
        "trading_subtheme",
        "summary_schema_version",
        "tagging_schema_version",
        "summary_status",
        "one_sentence_summary",
        "detailed_summary",
        "research_problem",
        "core_contributions",
        "data_and_experiments",
        "important_abstract_and_results",
        "deliverables",
        "method",
        "taxonomy_rationale",
        "survey_relevance_notes",
        "paywall_or_full_text_notes",
        "limitations_or_caveats",
        "tag_facets",
        "tags",
        "evidence_type",
        "summary_coverage",
        "tagging_confidence",
        "trading_investment_relevance",
        "summary_confidence",
        "text_char_count",
        "model_input_char_count",
        "source_url",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: flatten(row.get(field, "")) for field in fieldnames})


def write_report(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = ["# Paper Summaries", ""]
    for row in rows:
        if row.get("summary_status") != "ok":
            continue
        lines.extend(
            [
                f"## {row.get('title', '')}",
                "",
                f"- Year: {row.get('year', '')}",
                f"- Category: {row.get('taxonomy_category', '')}",
                f"- Trading subtheme: {row.get('trading_subtheme', '')}",
                f"- Evidence type: {row.get('evidence_type', '')}",
                f"- Summary coverage: {row.get('summary_coverage', '')}",
                f"- Tags: {', '.join(row.get('tags', []))}",
                f"- Tag facets: {json.dumps(row.get('tag_facets', {}), ensure_ascii=False, sort_keys=True)}",
                f"- One-line summary: {row.get('one_sentence_summary', '')}",
                "",
                "### Detailed Summary",
                "",
                row.get("detailed_summary", ""),
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=SUMMARY_JSONL)
    parser.add_argument("--output", type=Path, default=SUMMARY_JSONL)
    parser.add_argument("--csv-output", type=Path, default=SUMMARY_CSV)
    parser.add_argument("--report-output", type=Path, default=SUMMARY_REPORT)
    parser.add_argument("--pilot-output", type=Path, default=None)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--ids-file", type=Path, default=None)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--token", default=DEFAULT_TOKEN)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rows = read_jsonl(args.input)
    selected_keys: set[str] | None = None
    if args.ids_file:
        selected_keys = {line.strip() for line in args.ids_file.read_text(encoding="utf-8").splitlines() if line.strip()}
    selected: list[dict[str, Any]] = []
    for row in rows:
        if selected_keys is not None and row.get("paper_key") not in selected_keys:
            continue
        selected.append(row)
        if args.limit and len(selected) >= args.limit:
            break

    before = {row["paper_key"]: {field: json.dumps(row.get(field, None), sort_keys=True, ensure_ascii=False) for field in TEXT_SUMMARY_FIELDS} for row in rows}
    updated_by_key: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(selected, start=1):
        print(f"[retag] {index}/{len(selected)} {row.get('title')}", flush=True)
        updated_by_key[row["paper_key"]] = retag_one(dict(row), args.model, args.base_url, args.token)
        if args.sleep:
            time.sleep(args.sleep)

    updated_rows = [updated_by_key.get(row["paper_key"], row) for row in rows]
    after = {row["paper_key"]: {field: json.dumps(row.get(field, None), sort_keys=True, ensure_ascii=False) for field in TEXT_SUMMARY_FIELDS} for row in updated_rows}
    changed_summary = [key for key in before if before[key] != after[key]]
    if changed_summary:
        raise SystemExit(f"Refusing to write because summary fields changed: {changed_summary[:5]}")

    if args.pilot_output:
        write_jsonl(args.pilot_output, list(updated_by_key.values()))
    if not args.dry_run:
        write_jsonl(args.output, updated_rows)
        write_csv(args.csv_output, updated_rows)
        write_report(args.report_output, updated_rows)
    print(f"retagged={len(updated_by_key)}", flush=True)
    print(f"output={args.output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

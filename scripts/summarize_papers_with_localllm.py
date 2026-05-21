#!/usr/bin/env python3
"""Download papers, extract text, and summarize with Frederick's Local LLM.

Generated PDFs, extracted text, and summary reports are local artifacts. They
are ignored by git because they may contain copyrighted paper text.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "processed" / "curated_papers_by_taxonomy.csv"
PAPER_DIR = ROOT / "data" / "papers"
PDF_DIR = PAPER_DIR / "pdf"
TEXT_DIR = PAPER_DIR / "text"
MANUAL_DIR = PAPER_DIR / "manual"
DOWNLOAD_MANIFEST = ROOT / "data" / "processed" / "paper_download_manifest.csv"
MANUAL_NEEDED = ROOT / "data" / "processed" / "papers_needing_manual_download.csv"
SUMMARY_JSONL = ROOT / "data" / "processed" / "paper_summaries.jsonl"
SUMMARY_CSV = ROOT / "data" / "processed" / "paper_summaries.csv"
SUMMARY_FAILURES = ROOT / "data" / "processed" / "paper_summary_failures.csv"
SUMMARY_REPORT = ROOT / "reports" / "paper_summaries.md"
TEXT_MANIFEST = ROOT / "data" / "processed" / "paper_text_manifest.csv"
SUMMARY_SCHEMA_VERSION = "detailed-en-v3"

LOCAL_LLM_BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "http://192.168.50.18:31969/v1")
LOCAL_LLM_TOKEN = os.environ.get("LOCAL_LLM_TOKEN", "1969")
LOCAL_LLM_MODEL = os.environ.get("LOCAL_LLM_MODEL", "Qwen/Qwen3.6-35B-A3B")


def norm(value: str | None) -> str:
    return (value or "").strip()


def slugify(text: str, max_len: int = 84) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return (text[:max_len].strip("-") or "paper")


def paper_key(row: dict[str, str]) -> str:
    identity = norm(row.get("paperId")) or norm(row.get("arxiv")) or norm(row.get("doi")) or norm(row.get("title"))
    digest = hashlib.sha1(identity.encode("utf-8")).hexdigest()[:10]
    return f"{slugify(norm(row.get('title')), 72)}-{digest}"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def arxiv_pdf_url(arxiv_id: str) -> str:
    clean = arxiv_id.strip()
    clean = re.sub(r"^arXiv:", "", clean, flags=re.I)
    return f"https://arxiv.org/pdf/{clean}.pdf"


def source_pdf_candidates(row: dict[str, str]) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    arxiv = norm(row.get("arxiv"))
    source_url = norm(row.get("source_url"))

    if arxiv:
        candidates.append(("arxiv_id", arxiv_pdf_url(arxiv)))

    if source_url:
        url = source_url
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc.lower()
        path = parsed.path

        if "arxiv.org" in host:
            arxiv_match = re.search(r"/(?:abs|html|pdf)/([^/?#]+)", path)
            if arxiv_match:
                candidates.append(("arxiv_url", arxiv_pdf_url(arxiv_match.group(1).replace(".pdf", ""))))
        elif url.lower().endswith(".pdf"):
            candidates.append(("direct_pdf", url))
        elif "aclanthology.org" in host and not url.lower().endswith(".pdf"):
            candidates.append(("acl_pdf_guess", url.rstrip("/") + ".pdf"))

    # Keep order but remove duplicate URLs.
    seen: set[str] = set()
    unique: list[tuple[str, str]] = []
    for source, url in candidates:
        if url not in seen:
            unique.append((source, url))
            seen.add(url)
    return unique


def semantic_scholar_open_pdf(row: dict[str, str], timeout: int = 30) -> tuple[str, str] | None:
    paper_id = norm(row.get("paperId"))
    if not paper_id:
        return None
    fields = urllib.parse.quote("openAccessPdf,externalIds")
    url = f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(paper_id)}?fields={fields}"
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-llm-for-finance/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception:
        return None
    pdf_url = ((payload.get("openAccessPdf") or {}).get("url") or "").strip()
    if pdf_url:
        return ("semantic_scholar_openAccessPdf", pdf_url)
    return None


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False


def download_pdf(url: str, target: Path, timeout: int = 90) -> tuple[bool, str]:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".download")
    if tmp.exists():
        tmp.unlink()
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--retry",
        "2",
        "--connect-timeout",
        "15",
        "--max-time",
        str(timeout),
        "-A",
        "Mozilla/5.0 awesome-llm-for-finance",
        "-o",
        str(tmp),
        url,
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    except OSError as exc:
        return False, f"curl_failed: {exc}"
    if result.returncode != 0:
        tmp.unlink(missing_ok=True)
        return False, f"curl_exit_{result.returncode}: {result.stderr.strip()[:300]}"
    if not is_pdf(tmp):
        tmp.unlink(missing_ok=True)
        return False, "downloaded_content_not_pdf"
    tmp.replace(target)
    return True, "ok"


def manual_pdf_path(row: dict[str, str]) -> Path | None:
    key = paper_key(row)
    candidates = [
        MANUAL_DIR / f"{key}.pdf",
        MANUAL_DIR / f"{norm(row.get('paperId'))}.pdf",
        MANUAL_DIR / f"{slugify(norm(row.get('title')), 96)}.pdf",
    ]
    for path in candidates:
        if path.exists() and is_pdf(path):
            return path
    return None


def ensure_download(row: dict[str, str], s2_sleep: float = 1.0, force: bool = False) -> dict[str, Any]:
    key = paper_key(row)
    pdf_path = PDF_DIR / f"{key}.pdf"
    if pdf_path.exists() and is_pdf(pdf_path) and not force:
        return {
            "paper_key": key,
            "title": row.get("title", ""),
            "download_status": "downloaded",
            "pdf_path": str(pdf_path.relative_to(ROOT)),
            "download_source": "existing",
            "download_url": "",
            "error": "",
        }

    manual = manual_pdf_path(row)
    if manual:
        PDF_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(manual, pdf_path)
        return {
            "paper_key": key,
            "title": row.get("title", ""),
            "download_status": "downloaded",
            "pdf_path": str(pdf_path.relative_to(ROOT)),
            "download_source": "manual",
            "download_url": str(manual.relative_to(ROOT)),
            "error": "",
        }

    attempts = source_pdf_candidates(row)
    s2_candidate = semantic_scholar_open_pdf(row)
    if s2_candidate:
        attempts.append(s2_candidate)
        if s2_sleep:
            time.sleep(s2_sleep)

    errors: list[str] = []
    for source, url in attempts:
        ok, message = download_pdf(url, pdf_path)
        if ok:
            return {
                "paper_key": key,
                "title": row.get("title", ""),
                "download_status": "downloaded",
                "pdf_path": str(pdf_path.relative_to(ROOT)),
                "download_source": source,
                "download_url": url,
                "error": "",
            }
        errors.append(f"{source}:{message}")

    return {
        "paper_key": key,
        "title": row.get("title", ""),
        "download_status": "needs_manual_download",
        "pdf_path": "",
        "download_source": "",
        "download_url": "",
        "error": " | ".join(errors)[:1000] or "no_pdf_candidate",
        "source_url": row.get("source_url", ""),
        "doi": row.get("doi", ""),
        "arxiv": row.get("arxiv", ""),
        "paperId": row.get("paperId", ""),
    }


def extract_text(pdf_path: Path, text_path: Path) -> tuple[bool, str, int]:
    text_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        from pypdf import PdfReader
    except Exception as exc:
        return False, f"missing_pypdf: {exc}", 0

    try:
        reader = PdfReader(str(pdf_path))
        chunks: list[str] = []
        for index, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            if page_text.strip():
                chunks.append(f"\n\n[Page {index + 1}]\n{page_text.strip()}")
        text = "\n".join(chunks).strip()
    except Exception as exc:
        return False, f"pdf_extract_failed: {exc}", 0

    if not text:
        return False, "empty_extracted_text", 0
    text_path.write_text(text, encoding="utf-8")
    return True, "ok", len(text)


def load_existing_summaries(path: Path) -> set[str]:
    done: set[str] = set()
    if not path.exists():
        return done
    with path.open(encoding="utf-8") as f:
        for line in f:
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                continue
            if payload.get("summary_status") != "ok":
                continue
            key = payload.get("paper_key")
            if key:
                done.add(str(key))
    return done


def prune_summary_jsonl(path: Path) -> None:
    if not path.exists():
        return
    ok_by_key: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("summary_status") == "ok" and row.get("paper_key"):
                ok_by_key[str(row["paper_key"])] = row
    with path.open("w", encoding="utf-8") as f:
        for row in ok_by_key.values():
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def remove_summaries_for_keys(path: Path, keys: set[str]) -> None:
    if not path.exists() or not keys:
        return
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if str(row.get("paper_key", "")) not in keys:
                rows.append(row)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def available_models(base_url: str, token: str, timeout: int = 30) -> set[str]:
    req = urllib.request.Request(
        base_url.rstrip("/") + "/models",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return {item["id"] for item in payload.get("data", []) if "id" in item}


def ensure_model_available(model: str, base_url: str, token: str) -> None:
    models = available_models(base_url, token)
    if model not in models:
        sample = ", ".join(sorted(models)[:12])
        raise SystemExit(
            f"Requested Local LLM model is unavailable: {model}. "
            f"Available sample: {sample}"
        )


def truncate_text(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    head = int(max_chars * 0.72)
    tail = max_chars - head
    return text[:head] + "\n\n[... middle omitted for length ...]\n\n" + text[-tail:]


def build_prompt(row: dict[str, str], paper_text: str, max_chars: int) -> str:
    metadata = {
        "title": row.get("title", ""),
        "year": row.get("approx_year", ""),
        "authors": row.get("authors", ""),
        "venue": row.get("venue", ""),
        "primary_category": row.get("primary_category", ""),
        "taxonomy_category": row.get("taxonomy_category", ""),
        "trading_subtheme": row.get("trading_subtheme", ""),
        "abstract_from_catalog": row.get("abstract", ""),
    }
    doc = truncate_text(paper_text, max_chars)
    return f"""Create a detailed structured paper summary for our Awesome LLM for Finance collection.

Requirements:
- Return a JSON object only. Do not output Markdown or any extra explanation.
- Write all summary fields in English.
- Do not invent claims that are not supported by the provided metadata or paper text.
- The detailed_summary must be useful for survey writing and must add value beyond the abstract.
- detailed_summary must be 250-500 English tokens when the downloaded text contains enough detail. Fewer than 250 tokens is too short and should be treated as invalid unless the downloaded text is severely incomplete. It must never exceed 500 English tokens.
- Write detailed_summary as three paragraphs inside one JSON string. Each paragraph should be 90-150 English tokens when the text supports it: paragraph 1 for research problem and positioning, paragraph 2 for method/data/experiments, paragraph 3 for findings/use cases/limitations. Use "\\n\\n" between paragraphs.
- The complete tags list must be at most 200 English tokens.
- Each core field must include concrete methods, data/experiments, results, finance use cases, or limitations when available. Avoid generic filler.
- Give each paper 10 to 20 high-quality tags.
- paywall_or_full_text_notes must be based only on the provided text. If the downloaded text appears to be a complete paper, extract useful full-text details beyond the abstract. If not available, write "Not available from downloaded text".
- If the paper is not strictly about trading/investment but is useful for a finance LLM survey, explain that boundary instead of overstating relevance.

Tag quality rules:
- Tags must be lowercase English noun phrases, 1-4 words each, ASCII where possible.
- Use spaces, not underscores. Avoid punctuation unless it is standard in a term, e.g. "10-k", "xbrl", "rag".
- Avoid generic tags such as "finance", "machine learning", "artificial intelligence", "large language models", "research", or "paper" unless the paper is specifically about that concept as a contribution.
- Normalize synonyms consistently: use "llm" not "large language model"; "rag" not "retrieval augmented generation"; "multi-agent systems" not "multi agent"; "portfolio optimization" not "portfolio construction" unless construction is the paper's own term; "alpha mining" for factor discovery; "market microstructure" for order-book/execution work; "financial question answering" for QA benchmarks.
- Prefer tags that capture task, asset/market, method, data type, and evaluation target, e.g. "alpha mining", "order book", "earnings calls", "10-k filings", "portfolio optimization", "sentiment trading", "financial rag", "xbrl analysis", "agentic workflow".
- Avoid duplicates and near-duplicates in the same paper, e.g. do not include both "rag" and "financial rag" unless both are needed.
- Do not include authors, venue names, years, or broad taxonomy labels as tags.

JSON schema:
{{
  "one_sentence_summary": "One specific sentence stating what the paper does and its main conclusion.",
  "detailed_summary": "Three compact English paragraphs separated by \\n\\n, 250-500 English tokens when enough text is available, never above 500. Cover the research problem, method/data/experiments, findings/use cases/limitations.",
  "research_problem": "The specific finance/LLM problem addressed, in 2-4 sentences.",
  "core_contributions": ["4-7 concrete contribution bullets. Do not merely say 'proposes a framework'."],
  "data_and_experiments": ["3-6 bullets covering data sources, market/asset scope, benchmarks, experimental design, metrics, or noting that the paper is survey/conceptual."],
  "important_abstract_and_results": ["5-8 bullets covering important results, quantitative findings, comparisons, and business meaning when present."],
  "deliverables": ["2-6 bullets covering datasets, models, benchmarks, code, systems, taxonomies, or conceptual frameworks."],
  "method": ["4-8 bullets explaining the pipeline, model, agents, retrieval, optimization, statistical tests, or evaluation."],
  "taxonomy_rationale": "2-4 sentences explaining why this paper belongs to the given taxonomy_category and trading_subtheme.",
  "survey_relevance_notes": ["3-6 bullets explaining how this paper should be used in a survey and which section/theme it supports."],
  "paywall_or_full_text_notes": ["2-5 bullets with useful full-text details beyond the abstract, or Not available from downloaded text."],
  "limitations_or_caveats": ["3-6 bullets covering limitations, threats to validity, external-validity risk, data gaps, or deployment caveats."],
  "tags": ["10-20 normalized lowercase English tags"],
  "trading_investment_relevance": "high|medium|low",
  "summary_confidence": "high|medium|low"
}}

Metadata:
{json.dumps(metadata, ensure_ascii=False, indent=2)}

Paper text, truncated to at most {max_chars} characters:
<<<PAPER_TEXT
{doc}
PAPER_TEXT
"""


def local_llm_json(prompt: str, model: str, base_url: str, token: str, timeout: int = 180) -> tuple[dict[str, Any] | None, str]:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a precise research-paper summarizer. Return valid JSON only.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
        "max_tokens": 3600,
        "chat_template_kwargs": {"enable_thinking": False},
    }
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
        content = json.loads(raw)["choices"][0]["message"]["content"]
    except Exception as exc:
        return None, f"llm_call_failed: {exc}"

    cleaned = content.strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end != -1 and end > start:
        cleaned = cleaned[start : end + 1]
    try:
        return json.loads(cleaned), content
    except json.JSONDecodeError as exc:
        return None, f"json_parse_failed: {exc}: {content[:1000]}"


def estimated_tokens(text: Any) -> int:
    if not isinstance(text, str):
        return 0
    return len(re.findall(r"\S+", text))


def summarize_one(
    row: dict[str, str],
    download: dict[str, Any],
    max_chars: int,
    model: str,
    base_url: str,
    token: str,
) -> dict[str, Any]:
    key = download["paper_key"]
    pdf_path = ROOT / download.get("pdf_path", "")
    text_path = TEXT_DIR / f"{key}.txt"
    if text_path.exists():
        text = text_path.read_text(encoding="utf-8", errors="replace")
        extract_status = "existing"
        extract_error = ""
    else:
        ok, message, chars = extract_text(pdf_path, text_path)
        if not ok:
            return {
                "paper_key": key,
                "title": row.get("title", ""),
                "summary_status": "extract_failed",
                "error": message,
                "download_status": download.get("download_status", ""),
            }
        text = text_path.read_text(encoding="utf-8", errors="replace")
        extract_status = "extracted"
        extract_error = ""

    prompt = build_prompt(row, text, max_chars=max_chars)
    summary, raw_or_error = local_llm_json(prompt, model=model, base_url=base_url, token=token)
    if summary is None:
        return {
            "paper_key": key,
            "title": row.get("title", ""),
            "summary_status": "llm_failed",
            "error": raw_or_error,
            "download_status": download.get("download_status", ""),
            "extract_status": extract_status,
        }
    if len(text) >= 10_000 and estimated_tokens(summary.get("detailed_summary", "")) < 250:
        retry_prompt = (
            prompt
            + "\n\nYour previous detailed_summary was too short. Regenerate the full JSON. "
            + "The detailed_summary must be 250-500 English tokens and must include concrete "
            + "method, data/experiment, result, finance-use-case, and caveat details. "
            + "Write it as three compact paragraphs separated by \\n\\n."
        )
        retry_summary, retry_error = local_llm_json(retry_prompt, model=model, base_url=base_url, token=token)
        if retry_summary is not None:
            summary = retry_summary
        else:
            summary["quality_warning"] = retry_error

    summary["tags"] = normalize_tags(summary.get("tags", []), row)

    return {
        "paper_key": key,
        "title": row.get("title", ""),
        "year": row.get("approx_year", ""),
        "source_url": row.get("source_url", ""),
        "taxonomy_category": row.get("taxonomy_category", ""),
        "trading_subtheme": row.get("trading_subtheme", ""),
        "download_status": download.get("download_status", ""),
        "download_source": download.get("download_source", ""),
        "pdf_path": download.get("pdf_path", ""),
        "text_path": str(text_path.relative_to(ROOT)),
        "text_char_count": len(text),
        "model_input_char_count": min(len(text), max_chars),
        "summary_schema_version": SUMMARY_SCHEMA_VERSION,
        "summary_status": "ok",
        "extract_status": extract_status,
        "extract_error": extract_error,
        "model": model,
        **summary,
    }


def flatten(value: Any) -> str:
    if isinstance(value, list):
        return " | ".join(str(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return "" if value is None else str(value)


GENERIC_TAGS = {
    "finance",
    "financial",
    "machine learning",
    "artificial intelligence",
    "large language models",
    "large language model",
    "research",
    "paper",
    "study",
    "survey",
    "finance ai",
    "financial ai",
}

TAG_SYNONYMS = {
    "large language model": "llm",
    "large language models": "llm",
    "llms": "llm",
    "llm survey": "literature review",
    "financial llm": "domain-specific llm",
    "financial llms": "domain-specific llm",
    "retrieval augmented generation": "rag",
    "retrieval-augmented generation": "rag",
    "financial retrieval augmented generation": "financial rag",
    "financial retrieval-augmented generation": "financial rag",
    "multi agent systems": "multi-agent systems",
    "multi-agent system": "multi-agent systems",
    "multi agent": "multi-agent systems",
    "factor discovery": "alpha mining",
    "factor generation": "alpha mining",
    "alpha factor mining": "alpha mining",
    "stock factor mining": "alpha mining",
    "portfolio construction": "portfolio optimization",
    "qa": "financial question answering",
    "financial qa": "financial question answering",
    "finance qa": "financial question answering",
    "question answering": "financial question answering",
    "finqa": "financial question answering",
    "xbrl": "xbrl analysis",
    "10k filings": "10-k filings",
    "10 k filings": "10-k filings",
    "orderbook": "order book",
    "limit order book": "order book",
}


def normalize_tag(tag: Any) -> str:
    text = unicodedata.normalize("NFKD", str(tag)).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = text.replace("_", " ").replace("/", " ")
    text = re.sub(r"[^a-z0-9+\- ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -")
    text = TAG_SYNONYMS.get(text, text)
    if text in GENERIC_TAGS:
        return ""
    if not text or len(text.split()) > 4:
        return ""
    return text


def normalize_tags(tags: Any, row: dict[str, str]) -> list[str]:
    raw = tags if isinstance(tags, list) else []
    normalized: list[str] = []
    seen: set[str] = set()
    for tag in raw:
        clean = normalize_tag(tag)
        if clean and clean not in seen:
            normalized.append(clean)
            seen.add(clean)
        if len(normalized) >= 20:
            return normalized

    fallback_terms = [
        row.get("trading_subtheme", ""),
        row.get("taxonomy_category", ""),
        row.get("primary_category", ""),
    ]
    for term in fallback_terms:
        for piece in re.split(r"[,;/|]", term):
            clean = normalize_tag(piece)
            if clean and clean not in seen:
                normalized.append(clean)
                seen.add(clean)
            if len(normalized) >= 10:
                return normalized[:20]
    return normalized[:20]


def write_summary_csv(jsonl_path: Path, csv_path: Path) -> None:
    rows: list[dict[str, Any]] = []
    if not jsonl_path.exists():
        return
    with jsonl_path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    fieldnames = [
        "paper_key",
        "title",
        "year",
        "taxonomy_category",
        "trading_subtheme",
        "summary_schema_version",
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
        "tags",
        "trading_investment_relevance",
        "summary_confidence",
        "text_char_count",
        "model_input_char_count",
        "source_url",
    ]
    csv_rows = [{key: flatten(row.get(key, "")) for key in fieldnames} for row in rows]
    write_csv(csv_path, csv_rows, fieldnames)


def write_markdown_report(jsonl_path: Path, report_path: Path) -> None:
    if not jsonl_path.exists():
        return
    rows: list[dict[str, Any]] = []
    with jsonl_path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    report_path.parent.mkdir(parents=True, exist_ok=True)
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
                f"- One-line summary: {row.get('one_sentence_summary', '')}",
                "",
                "### Detailed Summary",
                "",
                row.get("detailed_summary", ""),
                "",
                "### Research Problem",
                "",
                row.get("research_problem", ""),
                "",
                "### Core Contributions",
                "",
                flatten(row.get("core_contributions", [])),
                "",
                "### Data and Experiments",
                "",
                flatten(row.get("data_and_experiments", [])),
                "",
                "### Main Results",
                "",
                flatten(row.get("important_abstract_and_results", [])),
                "",
                f"- Deliverables: {flatten(row.get('deliverables', []))}",
                f"- Method: {flatten(row.get('method', []))}",
                f"- Taxonomy rationale: {row.get('taxonomy_rationale', '')}",
                f"- Survey relevance: {flatten(row.get('survey_relevance_notes', []))}",
                f"- Limitations: {flatten(row.get('limitations_or_caveats', []))}",
                f"- Tags: {', '.join(row.get('tags', []))}",
                "",
            ]
        )
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--limit", type=int, default=0, help="Process only the first N selected papers.")
    parser.add_argument("--start", type=int, default=0, help="Start offset after reading the CSV.")
    parser.add_argument("--max-chars", type=int, default=50_000)
    parser.add_argument("--download-only", action="store_true")
    parser.add_argument("--extract-only", action="store_true")
    parser.add_argument("--summarize-only", action="store_true")
    parser.add_argument("--only-missing", action="store_true", help="Skip papers already present in paper_summaries.jsonl.")
    parser.add_argument("--force-download", action="store_true")
    parser.add_argument("--model", default=LOCAL_LLM_MODEL)
    parser.add_argument("--base-url", default=LOCAL_LLM_BASE_URL)
    parser.add_argument("--token", default=LOCAL_LLM_TOKEN)
    parser.add_argument("--s2-sleep", type=float, default=1.0)
    args = parser.parse_args()

    if args.max_chars > 50_000:
        raise SystemExit("--max-chars must be <= 50000 for this project pipeline")
    if not args.download_only and not args.extract_only:
        ensure_model_available(args.model, args.base_url, args.token)

    rows = read_rows(args.input)
    if args.start:
        rows = rows[args.start :]
    if args.limit:
        rows = rows[: args.limit]

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    MANUAL_DIR.mkdir(parents=True, exist_ok=True)

    prune_summary_jsonl(SUMMARY_JSONL)
    if not args.only_missing and not args.download_only and not args.extract_only:
        selected_keys = {paper_key(row) for row in rows}
        remove_summaries_for_keys(SUMMARY_JSONL, selected_keys)
    done = load_existing_summaries(SUMMARY_JSONL) if args.only_missing else set()
    manifest_rows: list[dict[str, Any]] = []
    manual_rows: list[dict[str, Any]] = []
    text_rows: list[dict[str, Any]] = []
    failure_rows: list[dict[str, Any]] = []

    SUMMARY_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with SUMMARY_JSONL.open("a", encoding="utf-8") as out:
        for index, row in enumerate(rows, start=1 + args.start):
            key = paper_key(row)
            if key in done:
                print(f"[skip] {index}: {row.get('title')}", flush=True)
                continue
            print(f"[paper] {index}: {row.get('title')}", flush=True)

            if args.summarize_only:
                pdf_path = PDF_DIR / f"{key}.pdf"
                download = {
                    "paper_key": key,
                    "title": row.get("title", ""),
                    "download_status": "downloaded" if pdf_path.exists() else "missing_pdf",
                    "pdf_path": str(pdf_path.relative_to(ROOT)) if pdf_path.exists() else "",
                    "download_source": "existing",
                }
            else:
                download = ensure_download(row, s2_sleep=args.s2_sleep, force=args.force_download)

            manifest_rows.append(download)
            if download.get("download_status") != "downloaded":
                manual_rows.append(download)
                print(f"  download: {download.get('download_status')} {download.get('error', '')[:160]}", flush=True)
                continue
            print(f"  download: {download.get('download_source')} -> {download.get('pdf_path')}", flush=True)

            if args.extract_only:
                text_path = TEXT_DIR / f"{key}.txt"
                ok, message, chars = extract_text(ROOT / download["pdf_path"], text_path)
                text_rows.append(
                    {
                        "paper_key": key,
                        "title": row.get("title", ""),
                        "extract_status": "ok" if ok else "failed",
                        "text_path": str(text_path.relative_to(ROOT)) if ok else "",
                        "text_char_count": chars,
                        "error": "" if ok else message,
                    }
                )
                print(f"  extract: {'ok' if ok else 'failed'} chars={chars} {message}", flush=True)
                continue

            if args.download_only:
                continue

            summary = summarize_one(
                row,
                download,
                max_chars=args.max_chars,
                model=args.model,
                base_url=args.base_url,
                token=args.token,
            )
            if summary.get("summary_status") == "ok":
                out.write(json.dumps(summary, ensure_ascii=False) + "\n")
                out.flush()
            else:
                failure_rows.append(summary)
            print(f"  summary: {summary.get('summary_status')}", flush=True)

    manifest_fields = [
        "paper_key",
        "title",
        "download_status",
        "pdf_path",
        "download_source",
        "download_url",
        "error",
        "source_url",
        "doi",
        "arxiv",
        "paperId",
    ]
    if manifest_rows:
        write_csv(DOWNLOAD_MANIFEST, manifest_rows, manifest_fields)
    if manual_rows:
        write_csv(MANUAL_NEEDED, manual_rows, manifest_fields)
    elif MANUAL_NEEDED.exists():
        MANUAL_NEEDED.unlink()

    if text_rows:
        write_csv(
            TEXT_MANIFEST,
            text_rows,
            ["paper_key", "title", "extract_status", "text_path", "text_char_count", "error"],
        )
    if failure_rows:
        write_csv(
            SUMMARY_FAILURES,
            failure_rows,
            ["paper_key", "title", "summary_status", "error", "download_status", "extract_status"],
        )
    if not args.download_only and not args.extract_only:
        write_summary_csv(SUMMARY_JSONL, SUMMARY_CSV)
        write_markdown_report(SUMMARY_JSONL, SUMMARY_REPORT)

    print(f"download_manifest={DOWNLOAD_MANIFEST}", flush=True)
    if manual_rows:
        print(f"manual_needed={MANUAL_NEEDED} ({len(manual_rows)})", flush=True)
    if text_rows:
        print(f"text_manifest={TEXT_MANIFEST}", flush=True)
    if failure_rows:
        print(f"summary_failures={SUMMARY_FAILURES} ({len(failure_rows)})", flush=True)
    if not args.download_only and not args.extract_only:
        print(f"summaries={SUMMARY_JSONL}", flush=True)
        print(f"summary_csv={SUMMARY_CSV}", flush=True)
        print(f"summary_report={SUMMARY_REPORT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Try harder to find PDFs for papers that need manual download.

This is intentionally conservative: it downloads only PDF responses from public
paper/metadata endpoints and writes a local audit trail. Generated PDFs and
manifests are ignored by git.
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from summarize_papers_with_localllm import MANUAL_DIR, ROOT, is_pdf, paper_key, slugify


INPUT = ROOT / "data" / "processed" / "papers_needing_manual_download.csv"
OUT = ROOT / "data" / "processed" / "manual_pdf_search_manifest.csv"

USER_AGENT = "Mozilla/5.0 awesome-llm-for-finance"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fetch_json(url: str, timeout: int = 30) -> dict[str, Any] | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception:
        return None


def fetch_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except Exception:
        return ""


def doi_url(doi: str) -> str:
    return "https://doi.org/" + doi.strip()


def arxiv_from_doi(doi: str) -> str:
    match = re.search(r"10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})(?:v[0-9]+)?", doi, re.I)
    return match.group(1) if match else ""


def openalex_candidates(row: dict[str, str]) -> list[str]:
    doi = row.get("doi", "").strip()
    title = row.get("title", "").strip()
    urls: list[str] = []
    if doi:
        api = "https://api.openalex.org/works/" + urllib.parse.quote(doi_url(doi), safe="") + "?mailto=frederickpi@example.com"
        payload = fetch_json(api)
        if payload:
            urls.extend(location_urls(payload))
    if not urls and title:
        params = urllib.parse.urlencode({"search": title, "per-page": 3, "mailto": "frederickpi@example.com"})
        payload = fetch_json("https://api.openalex.org/works?" + params)
        for result in (payload or {}).get("results", []):
            urls.extend(location_urls(result))
    return urls


def location_urls(payload: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    open_access = payload.get("open_access") or {}
    if open_access.get("oa_url"):
        urls.append(open_access["oa_url"])
    locations = []
    for key in ("best_oa_location", "primary_location"):
        if payload.get(key):
            locations.append(payload[key])
    locations.extend(payload.get("locations") or [])
    for loc in locations:
        if not isinstance(loc, dict):
            continue
        for key in ("pdf_url", "landing_page_url"):
            if loc.get(key):
                urls.append(loc[key])
    return urls


def crossref_candidates(row: dict[str, str]) -> list[str]:
    doi = row.get("doi", "").strip()
    if not doi:
        return []
    payload = fetch_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))
    message = (payload or {}).get("message") or {}
    urls: list[str] = []
    for link in message.get("link") or []:
        if "pdf" in (link.get("content-type", "") + link.get("URL", "")).lower():
            urls.append(link.get("URL", ""))
    return [url for url in urls if url]


def pattern_candidates(row: dict[str, str]) -> list[str]:
    doi = row.get("doi", "").strip()
    arxiv = row.get("arxiv", "").strip() or arxiv_from_doi(doi)
    title = row.get("title", "").strip()
    urls: list[str] = []
    if arxiv:
        clean = re.sub(r"^arXiv:", "", arxiv, flags=re.I)
        urls.extend(
            [
                f"https://arxiv.org/pdf/{clean}.pdf",
                f"https://export.arxiv.org/pdf/{clean}.pdf",
            ]
        )
    if doi:
        urls.append(doi_url(doi))
        lowered = doi.lower()
        if lowered.startswith("10.18653/v1/"):
            acl_id = doi.split("/")[-1]
            urls.append(f"https://aclanthology.org/{acl_id}.pdf")
        if lowered.startswith("10.1145/"):
            urls.append(f"https://dl.acm.org/doi/pdf/{doi}")
        if lowered.startswith("10.1109/"):
            urls.append(f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={ieee_arnumber_from_doi(doi)}")
        if lowered.startswith("10.3390/"):
            urls.extend(mdpi_candidates_from_doi(doi))
        if lowered.startswith("10.3389/"):
            urls.append(frontiers_pdf_url(doi))
        if lowered.startswith("10.1371/journal.pone."):
            urls.append(f"https://journals.plos.org/plosone/article/file?id={doi}&type=printable")
    if "PIXIU" in title and "Comprehensive Benchmark" in title:
        urls.append("https://arxiv.org/pdf/2306.05443.pdf")
    if title.startswith("Are ChatGPT and GPT-4 General-Purpose Solvers"):
        urls.append("https://arxiv.org/pdf/2305.05862.pdf")
    if title.startswith("RiskLabs:"):
        urls.append("https://arxiv.org/pdf/2404.07452.pdf")
    if title.startswith("Bloated Disclosures"):
        urls.append("https://export.arxiv.org/pdf/2306.10224.pdf")
    if title.startswith("Chain-of-Alpha"):
        urls.append("https://arxiv.org/pdf/2508.06312.pdf")
    return [url for url in urls if url and "arnumber=None" not in url]


def ieee_arnumber_from_doi(doi: str) -> str | None:
    text = fetch_text(doi_url(doi))
    for pattern in (r'"arnumber"\s*:\s*"([0-9]+)"', r"arnumber=([0-9]+)", r"/document/([0-9]+)"):
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None


def mdpi_candidates_from_doi(doi: str) -> list[str]:
    text = fetch_text(doi_url(doi))
    urls: list[str] = []
    for match in re.finditer(r'href="([^"]+/(?:pdf|article_deployments/pdf)[^"]*)"', text):
        url = urllib.parse.urljoin("https://www.mdpi.com/", match.group(1).replace("&amp;", "&"))
        urls.append(url)
    return urls


def frontiers_pdf_url(doi: str) -> str:
    parts = doi.split("/")
    journal = parts[0].split(".")[-1] if parts else ""
    article = parts[-1]
    return f"https://www.frontiersin.org/journals/artificial-intelligence/articles/{doi}/pdf"


def expand_landing_page(url: str) -> list[str]:
    candidates: list[str] = []
    text = fetch_text(url)
    if not text:
        return candidates
    for pattern in (
        r'href="([^"]+\.pdf(?:\?[^"]*)?)"',
        r'citation_pdf_url" content="([^"]+)"',
        r'content="([^"]+\.pdf(?:\?[^"]*)?)"',
    ):
        for match in re.finditer(pattern, text, flags=re.I):
            candidates.append(urllib.parse.urljoin(url, match.group(1).replace("&amp;", "&")))
    return candidates


def download_pdf(url: str, target: Path, timeout: int = 90) -> tuple[bool, str]:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".search-download")
    tmp.unlink(missing_ok=True)
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--retry",
        "1",
        "--connect-timeout",
        "15",
        "--max-time",
        str(timeout),
        "--http1.1",
        "-A",
        USER_AGENT,
        "-o",
        str(tmp),
        url,
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if result.returncode != 0:
        tmp.unlink(missing_ok=True)
        return False, f"curl_exit_{result.returncode}: {result.stderr.strip()[:220]}"
    if not is_pdf(tmp):
        tmp.unlink(missing_ok=True)
        return False, "not_pdf"
    tmp.replace(target)
    return True, "ok"


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        item = item.strip()
        if item and item not in seen:
            out.append(item)
            seen.add(item)
    return out


def main() -> int:
    rows = read_rows(INPUT)
    MANUAL_DIR.mkdir(parents=True, exist_ok=True)
    audit: list[dict[str, str]] = []
    for index, row in enumerate(rows, 1):
        key = paper_key(row)
        target = MANUAL_DIR / f"{key}.pdf"
        if target.exists() and is_pdf(target):
            audit.append({"paper_key": key, "title": row["title"], "status": "already_manual", "url": str(target), "error": ""})
            continue
        print(f"[{index}/{len(rows)}] {row['title']}", flush=True)
        base_candidates = unique(pattern_candidates(row) + openalex_candidates(row) + crossref_candidates(row))
        candidates = list(base_candidates)
        for candidate in base_candidates[:8]:
            if not candidate.lower().endswith(".pdf") and "pdf" not in candidate.lower() and "stamp.jsp" not in candidate.lower():
                candidates.extend(expand_landing_page(candidate)[:5])
        status = "not_found"
        found_url = ""
        last_error = ""
        for url in unique(candidates):
            ok, message = download_pdf(url, target)
            if ok:
                print(f"  found: {url}", flush=True)
                status = "downloaded"
                found_url = url
                last_error = ""
                break
            last_error = message
        audit.append({"paper_key": key, "title": row["title"], "status": status, "url": found_url, "error": last_error})
        if status != "downloaded":
            print(f"  missing: {last_error}", flush=True)
        time.sleep(0.3)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["paper_key", "title", "status", "url", "error"])
        writer.writeheader()
        writer.writerows(audit)
    print(f"manifest={OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Download hand-verified PDF URLs for papers missed by metadata search."""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path

from summarize_papers_with_localllm import MANUAL_DIR, ROOT, is_pdf, paper_key


INPUT = ROOT / "data" / "processed" / "papers_needing_manual_download.csv"

URLS = {
    "Financial Statement Analysis with Large Language Models": "https://arxiv.org/pdf/2407.17866v2",
    "A Comprehensive Review of Generative AI in Finance": "https://mdpi-res.com/d_attachment/fintech/fintech-03-00025/article_deploy/fintech-03-00025.pdf",
    "TAT-LLM: A Specialized Language Model for Discrete Reasoning over Financial Tabular and Textual Data": "https://arxiv.org/pdf/2401.13223.pdf",
    "WWW'18 Open Challenge: Financial Opinion Mining and Question Answering": "https://andrefreitas.org/papers/www_fiqa_2018.pdf",
    "A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification": "https://arxiv.org/pdf/2411.02476.pdf",
    "Large Language Models for Financial and Investment Management: Applications and Benchmarks": "https://web.media.mit.edu/~xdong/paper/jpm24b.pdf",
    "FinBERT-FOMC: Fine-Tuned FinBERT Model with Sentiment Focus Method for Enhancing Sentiment Analysis of FOMC Minutes": "https://www.alexandria.unisg.ch/server/api/core/bitstreams/1d94cc0d-30b9-4d0d-9131-8e8c20c46837/content",
    "Self-explanatory and Retrieval-augmented LLMs for Financial Sentiment Analysis": "https://dr.ntu.edu.sg/server/api/core/bitstreams/93213649-e91e-415e-851d-d33490e0a02d/content",
    "Comparative Investigation of GPT and FinBERT’s Sentiment Analysis Performance in News Across Different Sectors": "https://mdpi-res.com/d_attachment/electronics/electronics-14-01090/article_deploy/electronics-14-01090.pdf",
    "Bloated Disclosures: Can ChatGPT Help Investors Process Information?": "https://arxiv.org/pdf/2306.10224v2",
    "Forecasting the S&P 500 Index Using Mathematical-Based Sentiment Analysis and Deep Learning Models: A FinBERT Transformer Model and LSTM": "https://mdpi-res.com/d_attachment/axioms/axioms-12-00835/article_deploy/axioms-12-00835.pdf",
    "Evaluating Retrieval-Augmented Generation Models for Financial Report Question and Answering": "https://mdpi-res.com/d_attachment/applsci/applsci-14-09318/article_deploy/applsci-14-09318.pdf",
    "Fine-Tuning and Explaining FinBERT for Sector-Specific Financial News: A Reproducible Workflow": "https://mdpi-res.com/d_attachment/electronics/electronics-14-04680/article_deploy/electronics-14-04680.pdf",
    "LLM-Guided Evolutionary Strategy Generation for Quantitative Trading": "https://arxiv.org/pdf/2501.02321.pdf",
    "ChatGPT as a Financial Advisor: A Re-Examination": "https://mdpi-res.com/d_attachment/jrfm/jrfm-18-00664/article_deploy/jrfm-18-00664.pdf",
    "Strategic Complexity and Behavioral Distortion: Retail Investing Under Large Language Model Augmentation": "https://mdpi-res.com/d_attachment/ijfs/ijfs-13-00210/article_deploy/ijfs-13-00210.pdf",
    "Large Language Models for Financial Knowledge Extraction Analytical Insights and Corporate Planning Support": "https://drpress.org/ojs/index.php/mmaa/article/download/32153",
    "An Evaluation of Reasoning Capabilities of Large Language Models in Financial Sentiment Analysis": "https://www.sentic.net/llm-reasoning-capabilities-in-financial-sentiment-analysis.pdf",
    "A Review on Large Language Models and Generative AI in Banking": "https://www.scitepress.org/Papers/2025/134726/134726.pdf",
    "MME-Finance: A Multimodal Finance Benchmark for Expert-level Understanding and Reasoning": "https://arxiv.org/pdf/2411.03314.pdf",
    "DeepFinLLM: an intelligent financial advisor unleashing strategic insights with large language models": "https://assets-eu.researchsquare.com/files/rs-6376312/v1_covered_c4ba219a-d330-4104-8734-412cf765510c.pdf",
    "Application of Startup Success Prediction Models and Business Document Extraction Using Large Language Models to Enhance Due Diligence Efficiency": "https://easychair.org/publications/preprint/lpWh/download",
}


def rows() -> list[dict[str, str]]:
    with INPUT.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def download(url: str, target: Path) -> tuple[bool, str]:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".known-download")
    tmp.unlink(missing_ok=True)
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--http1.1",
        "--connect-timeout",
        "15",
        "--max-time",
        "90",
        "-A",
        "Mozilla/5.0 awesome-llm-for-finance",
        "-o",
        str(tmp),
        url,
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if result.returncode != 0:
        tmp.unlink(missing_ok=True)
        return False, f"curl_exit_{result.returncode}: {result.stderr.strip()[:200]}"
    if not is_pdf(tmp):
        tmp.unlink(missing_ok=True)
        return False, "not_pdf"
    tmp.replace(target)
    return True, "ok"


def main() -> int:
    by_title = {row["title"]: row for row in rows()}
    for title, url in URLS.items():
        row = by_title.get(title)
        if not row:
            print(f"[missing row] {title}")
            continue
        target = MANUAL_DIR / f"{paper_key(row)}.pdf"
        if target.exists() and is_pdf(target):
            print(f"[exists] {title}")
            continue
        ok, message = download(url, target)
        print(f"[{'ok' if ok else 'fail'}] {title} :: {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

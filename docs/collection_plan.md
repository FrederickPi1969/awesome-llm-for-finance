# Collection Plan

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

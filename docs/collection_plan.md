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

## Round 2: High-Relevance Candidate Expansion

- Select high-confidence first-round candidates that are clearly finance-specific and LLM-, agent-, RAG-, FinBERT-, or benchmark-related.
- Fetch citations and references for those promoted candidates.
- Export `round2_related_work_edges.csv` and `round2_expansion_candidates.csv`.
- Promote a conservative subset into `curated_papers.csv`.

## Round 3: Manual Curation

- Select high-confidence second-round promoted candidates that are recent, finance-specific, and LLM-, RAG-, agent-, benchmark-, or FinBERT-related.
- Fetch citations and references for those promoted candidates.
- Export `round3_related_work_edges.csv` and `round3_expansion_candidates.csv`.
- Promote a conservative subset into `curated_papers.csv`.

## Round 4: Manual Curation

- Select strong round-3 candidates that are not yet curated and still clearly finance-specific and LLM-, RAG-, agent-, benchmark-, or FinBERT-related.
- Fetch citations and references for those candidates.
- Export `round4_related_work_edges.csv` and `round4_expansion_candidates.csv`.
- Promote a conservative subset into `curated_papers.csv`.

## Round 5: Manual Curation

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

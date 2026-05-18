# Collection Plan

## Objective

Build a high-impact public Awesome-style repository for Large Language Models in Finance, with an adjacent strategy/geoeconomics/governance track where it strengthens the finance and decision-making narrative.

## Round 0: Seed Consolidation

- Normalize the original seed CSV.
- Resolve each seed paper against Semantic Scholar.
- Store citation counts, venues, authors, URLs, and abstracts.
- Keep unresolved/manual-check rows instead of dropping them.

Current status: complete for the original 58-paper finance seed list and for the
110-paper combined finance plus strategy/geoeconomics/governance seed list.

## Round 1: Citation and Reference Expansion

- For each resolved seed, collect papers that cite it and papers it references.
- Aggregate duplicate papers across all seeds.
- Score candidates using seed hit count, citation count, influential edge hits, finance/LLM keyword evidence, and recency.
- Export a preliminary top-200 candidate CSV for manual review.

Current 110-seed pass: 65 high-confidence/high-priority seeds expanded, 9,454
raw edges collected, 3,815 relevance-filtered candidates exported, 405 domain
additions separated from 20 generic foundation/context papers.

## Round 2: Manual Curation

- Promote true finance-specific LLM papers into the main README.
- Promote geoeconomics, forecasting, governance, and strategy papers only when
  they support the repository's "LLMs for financial/strategic decision-making"
  thesis.
- Split generic foundation-model papers into a background section only when they
  are repeatedly cited by the finance LLM literature.
- Check abstracts and titles for false positives, especially generic NLP, vision,
  optimization, and broad "AI governance" papers.

## Round 3: Deeper Expansion

- Re-run citation/reference expansion on accepted candidate additions.
- Add venue, code, dataset, model, benchmark, and task tags.
- Add GitHub/model/dataset links where available.
- Create issue templates for community submissions.
- Add an `accepted`/`deferred` decision column after manual review so later
  expansions can use only accepted additions as second-order seeds.

## Review Criteria

- Direct relevance to LLMs, foundation models, agents, or language-centric reasoning in finance.
- Finance-specific datasets, benchmarks, or evaluation protocols.
- High citation count or repeated appearance across multiple seed-paper neighborhoods.
- Practical importance for a repository reader building systems for SEC filings, financial QA, trading, research reports, risk analytics, or professional finance reasoning.

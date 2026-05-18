# Awesome LLM for Finance

A curated reading list for large language models in finance: financial-domain LLMs, benchmarks, SEC filing analysis, financial reasoning, trading agents, investment research, professional finance evaluation, and adjacent strategy/geoeconomics/governance work.

> Status: preliminary public seed. The current catalog started from 58 finance seed papers and now includes a second 110-seed expansion pass that adds finance plus geopolitics/geoeconomics/governance seeds.

## Latest Expansion Pass

The `110` data files are the current working set for the next curation round.

- Seeds inspected: 110
- Seeds resolved in Semantic Scholar: 100
- Seeds expanded through citations and references: 65 high-confidence/high-priority matches
- Raw citation/reference edges collected: 9,454
- Relevance-filtered longlist candidates: 3,815
- Curated preliminary additions for human review: 405
- Foundation/context papers separated from domain additions: 20

Primary review file: `data/processed/curated_additions_preliminary_110.csv`.

## Data Files

- `data/processed/seed_papers_enriched.csv`: seed papers with Semantic Scholar metadata, citation counts, links, and abstracts.
- `data/processed/expansion_candidates_preliminary.csv`: top 200 candidate additions discovered from citation/reference expansion.
- `data/processed/related_work_relevance_longlist.csv`: longer relevance-filtered candidate list for manual review.
- `data/raw/seed_papers_original_110.csv`: normalized combined finance plus strategy/geoeconomics/governance seed list.
- `data/processed/seed_papers_enriched_110.csv`: 110-seed enrichment with abstracts, citation counts, and match status.
- `data/processed/curated_additions_preliminary_110.csv`: preliminary non-seed candidate additions after duplicate and foundation-paper filtering.
- `data/processed/foundation_context_papers_110.csv`: generic foundation/model papers that are useful context but should not dominate the Awesome list.
- `data/processed/related_work_longlist_110.csv`: broader candidate longlist before curation filtering.
- `data/raw/semantic_scholar_related_work_edges_110.csv`: raw 110-seed citation/reference edge table.
- `data/processed/run_summary_110.json`: run statistics for the 110-seed expansion pass.
- `data/raw/semantic_scholar_related_work_edges.csv`: raw citation/reference edges from the first expansion pass.
- `data/raw/semantic_scholar_manifest.csv`: per-seed retrieval status and edge counts.

## Collection Method

1. Start with seed CSVs in `data/raw/seed_papers_original.csv` and `data/raw/seed_papers_original_110.csv`.
2. Resolve seed papers through Semantic Scholar and keep match confidence for manual inspection.
3. Fetch both citations and references for high-confidence, high-priority resolved seed papers.
4. Remove existing seed papers and near-duplicate title variants from the candidate pool.
5. Split generic foundation-model context papers from domain-specific additions.
6. Rank candidate additions by topic relevance, number of seed-paper connections, citation count, and recency.

See `docs/collection_plan.md` for the planned multi-round expansion workflow.

## Seed Papers

### Surveys

- [Large Language Models in Finance: A Survey](https://arxiv.org/abs/2311.10723) (2023) - `P0` - citations: 425 - LLMs in Finance Survey
- [A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges](https://arxiv.org/abs/2406.11903) (2024) - `P0` - citations: 145 - Financial Applications Survey
- [A Survey of Large Language Models in Finance: FinLLMs](https://arxiv.org/abs/2402.02315) (2024) - `P0` - citations: 147 - FinLLMs Survey
- [Large Language Model Agent in Financial Trading: A Survey](https://arxiv.org/abs/2408.06361) (2024) - `P1` - citations: 66 - LLM Trading Agent Survey
- [From Deep Learning to Large Language Models: A Survey of Artificial Intelligence in Quantitative Investment](https://arxiv.org/html/2503.21422v1) (2025) - `P1` - citations: 21 - AI in Quant Investment Survey
- [The New Quant: A Survey of Large Language Models in Stock Return Prediction and Investment Decision-Making](https://arxiv.org/html/2510.05533v1) (2025) - `P1` - citations: 2 - The New Quant
- [Bridging Language Models and Financial Analysis: A Survey of Datasets, Models, and Applications](https://arxiv.org/html/2503.22693) (2025) - `P2` - citations: 6 - Bridging LMs and Financial Analysis

### Financial language models

- [BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564) (2023) - `P0` - citations: 1294 - BloombergGPT
- [FinGPT: Open-Source Financial Large Language Models](https://arxiv.org/abs/2306.06031) (2023) - `P0` - citations: 380 - FinGPT

### Benchmarks and datasets

- [FinQA: A Dataset of Numerical Reasoning over Financial Data](https://arxiv.org/abs/2109.00122) (2021) - `P0` - citations: 648 - FinQA
- [TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance](https://arxiv.org/abs/2105.07624) (2021) - `P0` - citations: 500 - TAT-QA
- [ConvFinQA: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering](https://arxiv.org/abs/2210.03849) (2022) - `P0` - citations: 226 - ConvFinQA
- [MultiHiertt: Numerical Reasoning over Multi Hierarchical Tabular and Textual Data](https://arxiv.org/abs/2206.01347) (2022) - `P0` - citations: 168 - MultiHiertt
- [FinanceBench: A New Benchmark for Financial Question Answering](https://arxiv.org/abs/2311.11944) (2023) - `P0` - citations: 208 - FinanceBench
- [PIXIU: A Large Language Model, Instruction Data and Evaluation Benchmark for Finance](https://arxiv.org/abs/2306.05443) (2023) - `P0` - citations: 268 - PIXIU / FinMA
- [DocFinQA: A Long-Context Financial Reasoning Dataset](https://arxiv.org/html/2401.06915v2) (2024) - `P0` - citations: 61 - DocFinQA
- [FinBen: A Holistic Financial Benchmark for Large Language Models](https://arxiv.org/abs/2402.12659) (2024) - `P0` - citations: 143 - FinBen
- [InvestorBench: A Benchmark for Large Language Model Agents in Financial Decision-Making](https://arxiv.org/abs/2412.18174) (2024) - `P0` - citations: 39 - InvestorBench
- [FinRpt: Financial Report Understanding and Generation Benchmark](https://arxiv.org/html/2511.07322v1) (2025) - `P0` - citations: 2 - FinRpt
- [FinTagging: A Full-Scope Table-Aware XBRL Tagging Benchmark with LLMs](https://arxiv.org/abs/2505.20650) (2025) - `P0` - citations: 2 - FinTagging
- [Fin-RATE: Financial Report Analytics and Tracking Evaluation for Large Language Models](https://arxiv.org/abs/2602.07294) (2026) - `P0` - citations: 2 - Fin-RATE
- [BBT-Fin: Comprehensive Construction of Chinese Financial Domain Pre-trained Language Model, Corpus and Benchmark](https://arxiv.org/abs/2302.09432) (2023) - `P1` - citations: 82 - BBT-Fin
- [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2308.09975) (2023) - `P1` - citations: 63 - FinEval
- [A Preliminary Look at the State of the Art of Large Language Models on Chartered Financial Analyst Exams](https://aclanthology.org/2024.emnlp-industry.80/) (2024) - `P1` - citations: 8 - LLMs on CFA Exams Preliminary
- [BizBench: A Quantitative Reasoning Benchmark for Business and Finance](https://aclanthology.org/2024.acl-long.452.pdf) (2024) - `P1` - citations: 27 - BizBench
- [FinDABench: Benchmarking Financial Data Analysis Ability of Large Language Models](https://arxiv.org/abs/2401.02982) (2024) - `P1` - citations: 12 - FinDABench
- [Golden Touchstone: A Comprehensive Bilingual Benchmark for Evaluating Financial Large Language Models](https://arxiv.org/html/2411.06272v1) (2024) - `P1` - citations: 5 - Golden Touchstone
- [SEC-QA: A Systematic Benchmark for Evaluating Long-Context Question Answering on SEC Filings](https://arxiv.org/html/2406.14394v1) (2024) - `P1` - citations: 15 - SEC-QA
- [Advanced Financial Reasoning at Scale: Large Language Models on Chartered Financial Analyst Level III](https://arxiv.org/abs/2507.02954) (2025) - `P1` - citations: 3 - LLMs on CFA Level III
- [Can Large Language Models Tackle the Chartered Financial Analyst Exam?](https://arxiv.org/abs/2509.04468) (2025) - `P1` - citations: 2 - LLMs and CFA Exam
- [FLaME: A Holistic Benchmark for Financial Language Models](https://arxiv.org/abs/2506.15846) (2025) - `P1` - citations: 1 - FLaME
- [FinSphere: A Conversational Stock Analysis Agent based on Large Language Models](https://arxiv.org/abs/2501.12399) (2025) - `P1` - citations: 1 - FinSphere
- [Finance Agent Benchmark: Evaluating Language Model Agents as Financial Assistants](https://arxiv.org/abs/2508.00828) (2025) - `P1` - citations: 26 - Finance Agent Benchmark
- [FinanceReasoning: A Financial Benchmark for Large Reasoning Models](https://arxiv.org/html/2506.05828) (2025) - `P1` - citations: 17 - FinanceReasoning
- [SECQUE: A Benchmark for Evaluating Question-Answering on SEC Filings](https://arxiv.org/abs/2504.04596) (2025) - `P1` - citations: 6 - SECQUE
- [StockBench: Can Large Language Models Beat the Stock Market?](https://arxiv.org/html/2510.02209v2) (2025) - `P1` - citations: 15 - StockBench
- [FinTradeBench: A Comprehensive Benchmark for Fundamental and Technical Analysis in Financial Trading](https://arxiv.org/abs/2603.19225) (2026) - `P1` - citations: 2 - FinTradeBench
- [Taxonomy-Aligned Risk Extraction from 10-K Filings](https://arxiv.org/abs/2601.15247) (2026) - `P1` - citations: 0 - Taxonomy-Aligned Risk Extraction
- [Large Language Model Evaluation on Financial Benchmarks](https://research.ibm.com/publications/large-language-model-evaluation-on-financial-benchmarks) (2024) - `P2` - citations: 7 - IBM Financial Benchmark Evaluation
- [FLAME: Financial Large Language Model Evaluation System in Chinese](https://arxiv.org/abs/2501.06211) (2025) - `P2` - citations: 7 - FLAME Chinese Evaluation

### Reports, filings, and risk

- [Financial Statement Analysis with Large Language Models](https://arxiv.org/abs/2407.17866) (2024) - `P0` - citations: 70 - FSA with LLMs
- [The Structure of Financial Equity Research Reports](https://arxiv.org/abs/2407.18327) (2024) - `P0` - citations: 0 - Equity Research Report Structure

### Trading and investment

- [Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models](https://arxiv.org/abs/2304.07619) (2023) - `P1` - citations: 312 - ChatGPT Return Predictability
- [AI in Investment Analysis: Large Language Models for Equity Stock Ratings](https://arxiv.org/abs/2411.00856) (2024) - `P1` - citations: 14 - LLMs for Equity Stock Ratings
- [StockGPT: A GenAI Model for Stock Prediction and Trading](https://arxiv.org/abs/2404.05101) (2024) - `P1` - citations: 17 - StockGPT
- [Can LLM-Based Financial Investing Strategies Outperform?](https://arxiv.org/abs/2505.07078) (2025) - `P1` - citations: 14 - LLM Investing Strategies
- [Decision-Informed Neural Networks with Large Language Model Integration for Portfolio Optimization](https://ideas.repec.org/p/arx/papers/2502.00828.html) (2025) - `P1` - citations: 12 - Decision-Informed Portfolio Optimization
- [Leveraging Large Language Models for Top-Down Sector Allocation](https://arxiv.org/html/2503.09647v5) (2025) - `P1` - citations: 3 - LLMs for Sector Allocation
- [Task-Adaptive Large Language Models to Generate Human-Persuasive Investment Reports](https://aclanthology.org/2025.finnlp-2.23.pdf) (2025) - `P1` - citations: 0 - Task-Adaptive Investment Reports
- [The Wall Street Neophyte: A Zero-Shot Analysis of ChatGPT over Multimodal Stock Movement Prediction Challenges](https://arxiv.org/abs/2304.05351) (2023) - `P2` - citations: 77 - The Wall Street Neophyte
- [Leveraging Large Language Models for Institutional Investment Management](https://arxiv.org/abs/2411.19515) (2024) - `P2` - citations: 3 - LLMs for Institutional Investment Management
- [Your AI, Not Your View: The Bias of Large Language Models in Investment Analysis](https://arxiv.org/html/2507.20957v4) (2025) - `P2` - citations: 11 - Your AI, Not Your View

### Financial agents

- [FinMem: A Performance-Enhanced Large Language Model Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743) (2023) - `P0` - citations: 177 - FinMem
- [FinRobot: AI Agent for Equity Research and Valuation with Large Language Models](https://arxiv.org/abs/2411.08804) (2024) - `P0` - citations: 13 - FinRobot Equity Research
- [FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models](https://arxiv.org/abs/2405.14767) (2024) - `P0` - citations: 41 - FinRobot Platform
- [TradingAgents: Multi-Agents Large Language Models for Financial Trading](https://arxiv.org/abs/2412.20138) (2024) - `P0` - citations: 139 - TradingAgents
- [XBRL Agent: Leveraging Large Language Models for Financial Report Analysis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4993495) (2024) - `P0` - citations: 17 - XBRL Agent
- [Quantifying Material Risks from Textual Disclosures in Financial Statements using Large Language Model Agents](https://www.bis.org/ifc/publ/ifcb65_09_rh.pdf) (2025) - `P1` - citations: n/a - Quantifying Material Risks

## Preliminary Candidate Additions

- [FinBERT: Financial Sentiment Analysis with Pre-trained Language Models](https://www.semanticscholar.org/paper/7102bb3fe73bd057ff161d9db5214a267c1ef312) (2019) - Benchmarks and datasets - citations: 946 - seed hits: 15
- [WWW'18 Open Challenge: Financial Opinion Mining and Question Answering](https://www.semanticscholar.org/paper/7191680b572ee7145f1a9d95ff11ab1ff44259f3) (2018) - Benchmarks and datasets - citations: 421 - seed hits: 15
- [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://www.semanticscholar.org/paper/c86a70ff639707e647da3a429fe8e1e5c04415f5) (2024) - Financial agents - citations: 152 - seed hits: 12
- [XuanYuan 2.0: A Large Chinese Financial Chat Model with Hundreds of Billions Parameters](https://www.semanticscholar.org/paper/6783b17fe4328f48403f57009a73f784de09f645) (2023) - Other relevant work - citations: 160 - seed hits: 13
- [Advancing Financial Engineering with Foundation Models: Progress, Applications, and Challenges](https://www.semanticscholar.org/paper/390a6229243d7cc42bf756fc9564b9c48dd43b6f) (2025) - Benchmarks and datasets - citations: 3 - seed hits: 15
- [When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain](https://www.semanticscholar.org/paper/0882a2b2787b35dbcc6e341c953d964b77abd4df) (2022) - Benchmarks and datasets - citations: 157 - seed hits: 13
- [InvestLM: A Large Language Model for Investment using Financial Domain Instruction Tuning](https://www.semanticscholar.org/paper/844bc3b26b5c63ec3b251ae634c194dcfb41a7d2) (2023) - Trading and investment - citations: 115 - seed hits: 10
- [FinBERT: A Pretrained Language Model for Financial Communications](https://www.semanticscholar.org/paper/3578a7792904e6af3db8ffefdff86ab6a387c7c3) (2020) - Reports, filings, and risk - citations: 347 - seed hits: 11
- [Revolutionizing Finance with LLMs: An Overview of Applications and Insights](https://www.semanticscholar.org/paper/3d6197e4ab55a3a2785ce5934e48cfbe9fe9bf04) (2024) - Trading and investment - citations: 163 - seed hits: 10
- [Towards Competent AI for Fundamental Analysis in Finance: A Benchmark Dataset and Evaluation](https://www.semanticscholar.org/paper/3543d2e5874a9021cf53bb1db33e95af8fd0b924) (2025) - Trading and investment - citations: 1 - seed hits: 12
- [CFGPT: Chinese Financial Assistant with Large Language Model](https://www.semanticscholar.org/paper/a9eb336485e148d0a3f5010693d7752facba2875) (2023) - Benchmarks and datasets - citations: 20 - seed hits: 10
- [Good debt or bad debt: Detecting semantic orientations in economic texts](https://www.semanticscholar.org/paper/4211bff1388da30a3b7dfd35d6aef2032900ca5c) (2013) - Other relevant work - citations: 652 - seed hits: 9
- [DISC-FinLLM: A Chinese Financial Large Language Model based on Multiple Experts Fine-tuning](https://www.semanticscholar.org/paper/814f0b1658c49c79bc32f3d2b89045de007871c6) (2023) - Benchmarks and datasets - citations: 78 - seed hits: 9
- [LiveTradeBench: Seeking Real-World Alpha with Large Language Models](https://www.semanticscholar.org/paper/9b8944c299cd7ce32db8bf187b96b508bede49d1) (2025) - Financial agents - citations: 10 - seed hits: 9
- [Learning to Trade Like an Expert: Cognitive Fine-Tuning for Stable Financial Reasoning in Language Models](https://www.semanticscholar.org/paper/2692d9218c08789944132d22a78ec437baffd075) (2026) - Financial agents - citations: 0 - seed hits: 11
- [Standard Benchmarks Fail -- Auditing LLM Agents in Finance Must Prioritize Risk](https://www.semanticscholar.org/paper/e06f72ec485c85472d1380d5667adb417635c981) (2025) - Financial agents - citations: 9 - seed hits: 10
- [Mixing It Up: The Cocktail Effect of Multi-Task Fine-Tuning on LLM Performance - A Case Study in Finance](https://www.semanticscholar.org/paper/20461f6987f1846beb1cae0863d2aac35cba76fe) (2024) - Benchmarks and datasets - citations: 14 - seed hits: 9
- [Will LLMs be Professional at Fund Investment? DeepFund: A Live Arena Perspective](https://www.semanticscholar.org/paper/67c606df1d20ee804ce586f3aa899652b2639781) (2025) - Financial agents - citations: 2 - seed hits: 10
- [Impact of News on the Commodity Market: Dataset and Results](https://www.semanticscholar.org/paper/f987bf3b41ab98e1c755973c89f783ef445ab31a) (2020) - Trading and investment - citations: 99 - seed hits: 8
- [FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](https://www.semanticscholar.org/paper/d9f3ba8b48b68304b611e7d87c3d3ccf9abab32c) (2025) - Financial agents - citations: 18 - seed hits: 9
- [Domain Adaption of Named Entity Recognition to Support Credit Risk Assessment](https://www.semanticscholar.org/paper/44ee91d83d3b804780d8ec43ee5af0e41d3b0787) (2015) - Other relevant work - citations: 130 - seed hits: 9
- [No Language is an Island: Unifying Chinese and English in Financial Large Language Models, Instruction Data, and Benchmarks](https://www.semanticscholar.org/paper/eb419b57023d7de3284b182a5b680195c9095040) (2024) - Benchmarks and datasets - citations: 11 - seed hits: 9
- [Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment](https://www.semanticscholar.org/paper/f56ff0c8f868716244d1c0d490a72f762f1ab64a) (2025) - Surveys - citations: 11 - seed hits: 9
- [FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation](https://www.semanticscholar.org/paper/1717ec916c1e092facaaeb22fd8fe26b172eb388) (2025) - Trading and investment - citations: 17 - seed hits: 7
- [Unlocking Data Value in Finance: A Study on Distillation and Difficulty-Aware Training](https://www.semanticscholar.org/paper/2781595bb5eb65d89c966feec9f560805d610738) (2026) - Benchmarks and datasets - citations: 1 - seed hits: 10
- [FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](https://www.semanticscholar.org/paper/e28e933ed53de3f0097077fa5384d22ce5e959a3) (2024) - Benchmarks and datasets - citations: 53 - seed hits: 8
- [Empowering Many, Biasing a Few: Generalist Credit Scoring through Large Language Models](https://www.semanticscholar.org/paper/997d1e4c21fb62150f9b6379cdfe12521f0a318c) (2023) - Benchmarks and datasets - citations: 23 - seed hits: 7
- [Open-FinLLMs: Open Multimodal Large Language Models for Financial Applications](https://www.semanticscholar.org/paper/32b18218fa5b48b935b247c0746410b2a2c46a06) (2024) - Benchmarks and datasets - citations: 48 - seed hits: 9
- [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://www.semanticscholar.org/paper/95264f2fd070e9ee21dd2d36196a69c91a63e852) (2023) - Financial agents - citations: 94 - seed hits: 6
- [Time Travel is Cheating: Going Live with DeepFund for Real-Time Fund Investment Benchmarking](https://www.semanticscholar.org/paper/cd7438a5c5d731d744e9fce51bf702c6d3a8ffbd) (2025) - Financial agents - citations: 10 - seed hits: 6
- [Bridging finance and AI: a comprehensive survey of large language models in financial system](https://www.semanticscholar.org/paper/353fde0ffd73490827182e906bd67ed576fb417a) (2025) - Surveys - citations: 5 - seed hits: 10
- [Responsible Innovation: A Strategic Framework for Financial LLM Integration](https://www.semanticscholar.org/paper/3a48e315facb5115eacea25faf2cc32caa01d53b) (2025) - Trading and investment - citations: 10 - seed hits: 7
- [Large Language Model Agents for Investment Management: Foundations, Benchmarks, and Research Frontiers](https://www.semanticscholar.org/paper/a5a80a83cf865a0f854332b02ec26353d436c036) (2025) - Financial agents - citations: 5 - seed hits: 6
- [Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English](https://www.semanticscholar.org/paper/16c6af5ba8989a70c84567549effd2fd7932d2ec) (2024) - Benchmarks and datasets - citations: 16 - seed hits: 8
- [From Scores to Skills: A Cognitive Diagnosis Framework for Evaluating Financial Large Language Models](https://www.semanticscholar.org/paper/ba13b3744678596741204a69dd337360d52cd85d) (2025) - Benchmarks and datasets - citations: 3 - seed hits: 9
- [Financial Report Chunking for Effective Retrieval Augmented Generation](https://www.semanticscholar.org/paper/c072d217732edb066de2192ab9ad6b02aec9c7a0) (2024) - Reports, filings, and risk - citations: 70 - seed hits: 8
- [AlphaFin: Benchmarking Financial Analysis with Retrieval-Augmented Stock-Chain Framework](https://www.semanticscholar.org/paper/3a6bdf724da556ca534a9786b7a9f3f0adc567f7) (2024) - Trading and investment - citations: 68 - seed hits: 7
- [A Comprehensive Review of Generative AI in Finance](https://www.semanticscholar.org/paper/bc2dc0afd73c3a39ea750f48a7a5ee98178c48e6) (2024) - Reports, filings, and risk - citations: 33 - seed hits: 9
- [FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets](https://www.semanticscholar.org/paper/bd09391fbd124dc0c0a6be5d0ab2eb5d9c43fbac) (2023) - Reports, filings, and risk - citations: 113 - seed hits: 7
- [FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](https://www.semanticscholar.org/paper/7efaf134965a957bedc73a60a0083699fd791e16) (2025) - Benchmarks and datasets - citations: 9 - seed hits: 9

## Contributing

Open an issue or pull request with title, year, link, category, and a short note explaining why the paper belongs in the list. High-signal additions should either be finance-specific LLM work, a core financial NLP benchmark/dataset, or a highly cited foundation paper directly used by multiple finance LLM papers.

## Attribution

Paper metadata in `data/` was collected from the seed CSV and the Semantic Scholar Graph API. Abstracts and third-party metadata remain subject to their original rights and provider terms.

# Awesome LLM for Finance

A curated reading list for large language models in finance: financial-domain LLMs, benchmarks, SEC filing analysis, financial reasoning, trading agents, investment research, and professional finance evaluation.

> Status: expanding public seed. The current catalog starts from 58 seed papers plus three Semantic Scholar citation/reference expansion rounds over high-relevance finance LLM candidates.

## Data Files

- `data/processed/curated_papers.csv`: expanded curated list combining the original seeds and promoted additions.
- `data/processed/seed_papers_enriched.csv`: seed papers with Semantic Scholar metadata, citation counts, links, and abstracts.
- `data/processed/expansion_candidates_preliminary.csv`: top 200 candidate additions discovered from citation/reference expansion.
- `data/processed/round2_expansion_candidates.csv`: top 200 candidate additions discovered from the second-round expansion.
- `data/processed/round3_expansion_candidates.csv`: top 200 candidate additions discovered from the third-round expansion.
- `data/processed/related_work_relevance_longlist.csv`: longer relevance-filtered candidate list for manual review.
- `data/raw/semantic_scholar_related_work_edges.csv`: raw citation/reference edges from the first expansion pass.
- `data/raw/round2_related_work_edges.csv`: raw citation/reference edges from the second expansion pass.
- `data/raw/round3_related_work_edges.csv`: raw citation/reference edges from the third expansion pass.
- `data/raw/semantic_scholar_manifest.csv`: per-seed retrieval status and edge counts.
- `data/raw/round2_related_work_manifest.csv`: per-round-2-seed retrieval status and edge counts.
- `data/raw/round3_related_work_manifest.csv`: per-round-3-seed retrieval status and edge counts.

## Collection Method

1. Start with the seed CSV in `data/raw/seed_papers_original.csv`.
2. Resolve seed papers through Semantic Scholar, preferring arXiv ids when available.
3. Fetch both citations and references for each resolved seed paper.
4. Promote high-confidence first-pass and second-pass candidates as deeper expansion seeds.
5. Fetch citations and references for those promoted candidates.
6. Rank candidate additions by finance/LLM relevance terms, number of source-paper connections, citation count, influential-edge hits, and recency.

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

## Expanded Curated Additions

### Surveys

- [Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment](https://www.semanticscholar.org/paper/f56ff0c8f868716244d1c0d490a72f762f1ab64a) (2025) - `P0` - citations: 11 - round1_promoted_seed_for_round2
- [A Survey on Large Language Models for Critical Societal Domains: Finance, Healthcare, and Law](https://www.semanticscholar.org/paper/c631a5458bfb0d86053af2258c219825477ba4f6) (2024) - `P1` - citations: 98 - round2_promoted
- [Integrating Large Language Models in Financial Investments and Market Analysis: A Survey](https://www.semanticscholar.org/paper/6e8331657256fdc8f83dd534fcdbf12dfa375359) (2025) - `P1` - citations: 7 - round3_promoted

### Financial language models

- [FinBERT: Financial Sentiment Analysis with Pre-trained Language Models](https://www.semanticscholar.org/paper/7102bb3fe73bd057ff161d9db5214a267c1ef312) (2019) - `P0` - citations: 946 - round1_promoted_seed_for_round2
- [FinBERT : A Large Language Model for Extracting Information from Financial Text†](https://www.semanticscholar.org/paper/8798b3a01c29fe0ce45a271bedd934787343dfb5) (2022) - `P0` - citations: 561 - round2_promoted
- [FinBERT: A Pretrained Language Model for Financial Communications](https://www.semanticscholar.org/paper/3578a7792904e6af3db8ffefdff86ab6a387c7c3) (2020) - `P0` - citations: 347 - round1_promoted_seed_for_round2
- [FinBERT: A Pre-trained Financial Language Representation Model for Financial Text Mining](https://www.semanticscholar.org/paper/df0498605d5131098237e37914b402b67fea3936) (2020) - `P0` - citations: 286 - round2_promoted
- [XuanYuan 2.0: A Large Chinese Financial Chat Model with Hundreds of Billions Parameters](https://www.semanticscholar.org/paper/6783b17fe4328f48403f57009a73f784de09f645) (2023) - `P0` - citations: 160 - round1_promoted_seed_for_round2
- [When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain](https://www.semanticscholar.org/paper/0882a2b2787b35dbcc6e341c953d964b77abd4df) (2022) - `P0` - citations: 157 - round2_promoted
- [Transforming Sentiment Analysis in the Financial Domain with ChatGPT](https://www.semanticscholar.org/paper/3c4f1244301577cffff9affc73690669725e7e08) (2023) - `P0` - citations: 149 - round3_promoted
- [Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning of General-Purpose Large Language Models](https://www.semanticscholar.org/paper/087a2f4cfea227be944f576f1f049e329316acac) (2023) - `P0` - citations: 128 - round2_promoted
- [FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets](https://www.semanticscholar.org/paper/bd09391fbd124dc0c0a6be5d0ab2eb5d9c43fbac) (2023) - `P0` - citations: 113 - round1_promoted_seed_for_round2
- [FinGPT: Democratizing Internet-scale Data for Financial Large Language Models](https://www.semanticscholar.org/paper/6121fb3e393597e02481a516f0035f06ec9a5836) (2023) - `P0` - citations: 105 - round2_promoted
- [DISC-FinLLM: A Chinese Financial Large Language Model based on Multiple Experts Fine-tuning](https://www.semanticscholar.org/paper/814f0b1658c49c79bc32f3d2b89045de007871c6) (2023) - `P0` - citations: 78 - round1_promoted_seed_for_round2
- [Open-FinLLMs: Open Multimodal Large Language Models for Financial Applications](https://www.semanticscholar.org/paper/32b18218fa5b48b935b247c0746410b2a2c46a06) (2024) - `P0` - citations: 48 - round1_promoted_seed_for_round2
- [CFGPT: Chinese Financial Assistant with Large Language Model](https://www.semanticscholar.org/paper/a9eb336485e148d0a3f5010693d7752facba2875) (2023) - `P0` - citations: 20 - round1_promoted_seed_for_round2
- [Sentiment trading with large language models](https://www.semanticscholar.org/paper/f0f339d02a94d9609fc30561e72b3fe1ad83bca4) (2024) - `P1` - citations: 78 - round3_promoted
- [Forecasting the S&P 500 Index Using Mathematical-Based Sentiment Analysis and Deep Learning Models: A FinBERT Transformer Model and LSTM](https://www.semanticscholar.org/paper/21870c270fd33369b664f216ef6669b200ee331a) (2023) - `P1` - citations: 62 - round3_promoted
- [Hybrid LSTM and GRU for Cryptocurrency Price Forecasting Based on Social Network Sentiment Analysis Using FinBERT](https://www.semanticscholar.org/paper/2b24d46f381954757a9f9bdd8635b38630f403d6) (2023) - `P1` - citations: 30 - round2_promoted
- [FinBERT-FOMC: Fine-Tuned FinBERT Model with Sentiment Focus Method for Enhancing Sentiment Analysis of FOMC Minutes](https://www.semanticscholar.org/paper/fbd0999cfb30d0bf20641323baaaa5882f651c22) (2023) - `P1` - citations: 28 - round2_promoted
- [RA-CFGPT: Chinese financial assistant with retrieval-augmented large language model](https://www.semanticscholar.org/paper/39c473ced3121883ec747e92175d29e44a1237c9) (2024) - `P1` - citations: 23 - round2_promoted
- [Comparative Investigation of GPT and FinBERT’s Sentiment Analysis Performance in News Across Different Sectors](https://www.semanticscholar.org/paper/83d5a3100782b9803f9e25fbc41d1fbf9e98bed1) (2025) - `P1` - citations: 14 - round3_promoted

### Benchmarks and datasets

- [WWW'18 Open Challenge: Financial Opinion Mining and Question Answering](https://www.semanticscholar.org/paper/7191680b572ee7145f1a9d95ff11ab1ff44259f3) (2018) - `P0` - citations: 421 - round2_promoted
- [Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? A Study on Several Typical Tasks](https://www.semanticscholar.org/paper/f377b99a5f77ef94c736912dbdfe4108f4b22b69) (2023) - `P0` - citations: 114 - round1_promoted_seed_for_round2
- [FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](https://www.semanticscholar.org/paper/e28e933ed53de3f0097077fa5384d22ce5e959a3) (2024) - `P0` - citations: 53 - round1_promoted_seed_for_round2
- [Empowering Many, Biasing a Few: Generalist Credit Scoring through Large Language Models](https://www.semanticscholar.org/paper/997d1e4c21fb62150f9b6379cdfe12521f0a318c) (2023) - `P0` - citations: 23 - round1_promoted_seed_for_round2
- [Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English](https://www.semanticscholar.org/paper/16c6af5ba8989a70c84567549effd2fd7932d2ec) (2024) - `P0` - citations: 16 - round1_promoted_seed_for_round2
- [Mixing It Up: The Cocktail Effect of Multi-Task Fine-Tuning on LLM Performance - A Case Study in Finance](https://www.semanticscholar.org/paper/20461f6987f1846beb1cae0863d2aac35cba76fe) (2024) - `P0` - citations: 14 - round1_promoted_seed_for_round2
- [No Language is an Island: Unifying Chinese and English in Financial Large Language Models, Instruction Data, and Benchmarks](https://www.semanticscholar.org/paper/eb419b57023d7de3284b182a5b680195c9095040) (2024) - `P0` - citations: 11 - round1_promoted_seed_for_round2
- [FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](https://www.semanticscholar.org/paper/7efaf134965a957bedc73a60a0083699fd791e16) (2025) - `P0` - citations: 9 - round1_promoted_seed_for_round2
- [Advancing Financial Engineering with Foundation Models: Progress, Applications, and Challenges](https://www.semanticscholar.org/paper/390a6229243d7cc42bf756fc9564b9c48dd43b6f) (2025) - `P0` - citations: 3 - round1_promoted_seed_for_round2
- [From Scores to Skills: A Cognitive Diagnosis Framework for Evaluating Financial Large Language Models](https://www.semanticscholar.org/paper/ba13b3744678596741204a69dd337360d52cd85d) (2025) - `P0` - citations: 3 - round1_promoted_seed_for_round2
- [Unlocking Data Value in Finance: A Study on Distillation and Difficulty-Aware Training](https://www.semanticscholar.org/paper/2781595bb5eb65d89c966feec9f560805d610738) (2026) - `P0` - citations: 1 - round1_promoted_seed_for_round2
- [PIXIU: A Comprehensive Benchmark, Instruction Dataset and Large Language Model for Finance](https://www.semanticscholar.org/paper/dc7ee44dc2904228c0da316f6b35ddb6a15f4f63) (2023) - `P1` - citations: 70 - round2_promoted
- [Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? An Examination on Several Typical Tasks](https://www.semanticscholar.org/paper/45d325884a5169df06e41288717b7a78c07bedb7) (2023) - `P1` - citations: 51 - round2_promoted
- [Can GPT models be Financial Analysts? An Evaluation of ChatGPT and GPT-4 on mock CFA Exams](https://www.semanticscholar.org/paper/ec2c330301fa8a9f4b6357d9ca630bf5bcd50996) (2023) - `P1` - citations: 28 - round3_promoted
- [Benchmarking Large Language Models on CFLUE - A Chinese Financial Language Understanding Evaluation Dataset](https://www.semanticscholar.org/paper/21c22e2a16e3e6a95cc8900d687f3f0d14bd2f64) (2024) - `P1` - citations: 27 - round2_promoted
- [A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification](https://www.semanticscholar.org/paper/e94fa7016d7e9814399e42480512a2a8bb73972e) (2025) - `P1` - citations: 26 - round2_promoted
- [An Evaluation of Reasoning Capabilities of Large Language Models in Financial Sentiment Analysis](https://www.semanticscholar.org/paper/4a54ae690a0a1a2613031d31247d312545b86f04) (2024) - `P1` - citations: 18 - round3_promoted
- [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://www.semanticscholar.org/paper/5f520e8f20b3063307d174c8bc530317ed0d5a2a) (2025) - `P1` - citations: 18 - round2_promoted
- [BizFinBench: A Business-Driven Real-World Financial Benchmark for Evaluating LLMs](https://www.semanticscholar.org/paper/9de263bfddf6888f928bc66837f1dd788289de13) (2025) - `P1` - citations: 17 - round2_promoted
- [Exploring Large Language Models for Financial Applications: Techniques, Performance, and Challenges with FinMA](https://www.semanticscholar.org/paper/35d835d43450af4348ee49c8f7097b7ab9c3ecd0) (2025) - `P1` - citations: 2 - round2_promoted

### Reports, filings, and risk

- [Financial Report Chunking for Effective Retrieval Augmented Generation](https://www.semanticscholar.org/paper/c072d217732edb066de2192ab9ad6b02aec9c7a0) (2024) - `P0` - citations: 70 - round1_promoted_seed_for_round2
- [A Comprehensive Review of Generative AI in Finance](https://www.semanticscholar.org/paper/bc2dc0afd73c3a39ea750f48a7a5ee98178c48e6) (2024) - `P0` - citations: 33 - round1_promoted_seed_for_round2
- [TAT-LLM: A Specialized Language Model for Discrete Reasoning over Financial Tabular and Textual Data](https://www.semanticscholar.org/paper/b714baccfd4997ef6c14cbff3d8b4921493d7446) (2024) - `P0` - citations: 26 - round1_promoted_seed_for_round2
- [A Scoping Review of ChatGPT Research in Accounting and Finance](https://www.semanticscholar.org/paper/93cf2624dc11b38457f603ff8c345c5f3fc9d52b) (2024) - `P1` - citations: 75 - round3_promoted
- [Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning](https://www.semanticscholar.org/paper/95d638e7705ec561382268405bc488df4c26c7f7) (2025) - `P1` - citations: 66 - round2_promoted
- [FinNLI: Novel Dataset for Multi-Genre Financial Natural Language Inference Benchmarking](https://www.semanticscholar.org/paper/f22b17e68fc846fd660951807862a78adc08525f) (2025) - `P1` - citations: 4 - round2_promoted

### Trading and investment

- [Enhancing Financial Sentiment Analysis via Retrieval Augmented Large Language Models](https://www.semanticscholar.org/paper/1b860394dfec26d9c350889006e37fe56731f77e) (2023) - `P0` - citations: 191 - round1_promoted_seed_for_round2
- [Revolutionizing Finance with LLMs: An Overview of Applications and Insights](https://www.semanticscholar.org/paper/3d6197e4ab55a3a2785ce5934e48cfbe9fe9bf04) (2024) - `P0` - citations: 163 - round1_promoted_seed_for_round2
- [Temporal Data Meets LLM - Explainable Financial Time Series Forecasting](https://www.semanticscholar.org/paper/681253389d2cc27103753749f4c7556699d55471) (2023) - `P0` - citations: 121 - round2_promoted
- [InvestLM: A Large Language Model for Investment using Financial Domain Instruction Tuning](https://www.semanticscholar.org/paper/844bc3b26b5c63ec3b251ae634c194dcfb41a7d2) (2023) - `P0` - citations: 115 - round1_promoted_seed_for_round2
- [AlphaFin: Benchmarking Financial Analysis with Retrieval-Augmented Stock-Chain Framework](https://www.semanticscholar.org/paper/3a6bdf724da556ca534a9786b7a9f3f0adc567f7) (2024) - `P0` - citations: 68 - round1_promoted_seed_for_round2
- [FinLlama: Financial Sentiment Classification for Algorithmic Trading Applications](https://www.semanticscholar.org/paper/15b0a6ccb198b2936e36266be992da78a29953fd) (2024) - `P0` - citations: 29 - round1_promoted_seed_for_round2
- [Responsible Innovation: A Strategic Framework for Financial LLM Integration](https://www.semanticscholar.org/paper/3a48e315facb5115eacea25faf2cc32caa01d53b) (2025) - `P0` - citations: 10 - round1_promoted_seed_for_round2
- [Evaluating Financial Intelligence in Large Language Models: Benchmarking SuperInvesting AI with LLM Engines](https://www.semanticscholar.org/paper/a64372654025158c2cbb49dd6194c17e967256f0) (2026) - `P0` - citations: 1 - round1_promoted_seed_for_round2
- [Towards Competent AI for Fundamental Analysis in Finance: A Benchmark Dataset and Evaluation](https://www.semanticscholar.org/paper/3543d2e5874a9021cf53bb1db33e95af8fd0b924) (2025) - `P0` - citations: 1 - round1_promoted_seed_for_round2
- [ChatGPT Informed Graph Neural Network for Stock Movement Prediction](https://www.semanticscholar.org/paper/d3ba770fa1f48458b7ccbc88307b942cfb751a36) (2023) - `P1` - citations: 82 - round3_promoted
- [Can ChatGPT improve investment decisions? From a portfolio management perspective](https://www.semanticscholar.org/paper/2516b8d7f61da0fac219cf00f488a7d8d3d7d5c7) (2024) - `P1` - citations: 72 - round3_promoted
- [Deficiency of Large Language Models in Finance: An Empirical Examination of Hallucination](https://www.semanticscholar.org/paper/5838b56f2c7ca3dd946428dae07bdc26a9265c67) (2023) - `P1` - citations: 63 - round2_promoted
- [Bloated Disclosures: Can ChatGPT Help Investors Process Information?](https://www.semanticscholar.org/paper/af16b6f8146432e9437c1dd9b8320ee24ac63455) (2023) - `P1` - citations: 56 - round3_promoted
- [Can Large Language Models beat wall street? Evaluating GPT-4’s impact on financial decision-making with MarketSenseAI](https://www.semanticscholar.org/paper/a25a6a7dabe6621e5e74cccdc3963aea947d2d20) (2024) - `P1` - citations: 53 - round2_promoted
- [Harnessing Earnings Reports for Stock Predictions: A QLoRA-Enhanced LLM Approach](https://www.semanticscholar.org/paper/31e6b91ed8eb6f5fe8703301fc439fd1af160132) (2024) - `P1` - citations: 53 - round3_promoted
- [FinVis-GPT: A Multimodal Large Language Model for Financial Chart Analysis](https://www.semanticscholar.org/paper/0edcd1ce1d44359e8bf255b7216b9b56fa2cea33) (2023) - `P1` - citations: 34 - round2_promoted
- [Assessing Look-Ahead Bias in Stock Return Predictions Generated by GPT Sentiment Analysis](https://www.semanticscholar.org/paper/af42ae531ad0c41518fcf3a382e6e9f1ba465601) (2023) - `P1` - citations: 29 - round2_promoted
- [GPT-InvestAR: Enhancing Stock Investment Strategies through Annual Report Analysis with Large Language Models](https://www.semanticscholar.org/paper/110052b69ccbcc280b1a806c4e0bf876e6a5b116) (2023) - `P1` - citations: 29 - round2_promoted
- [Ploutos: Towards interpretable stock movement prediction with financial large language model](https://www.semanticscholar.org/paper/fc4968617eae1d875a77ed0372be8f2e6118440a) (2024) - `P1` - citations: 21 - round3_promoted
- [FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation](https://www.semanticscholar.org/paper/1717ec916c1e092facaaeb22fd8fe26b172eb388) (2025) - `P1` - citations: 17 - round1_promoted_seed_for_round2
- [Fine-Tuning Large Language Models for Stock Return Prediction Using Newsflow](https://www.semanticscholar.org/paper/f6c0a84ac1f1fe79cfde96f4e163d0d69f9c06cb) (2024) - `P1` - citations: 17 - round3_promoted
- [Leveraging Large Language Models and Retrieval-Augmented Generation for Enhanced Multi-Asset Portfolio Construction](https://www.semanticscholar.org/paper/32e3b82aee29adbca2e826d8cebf06c3f6178038) (2025) - `P1` - citations: 2 - round2_promoted
- [Large Language Models for Financial Knowledge Extraction Analytical Insights and Corporate Planning Support](https://www.semanticscholar.org/paper/8dd640e8c2d469fb7a1d3286a0d7b14175b9234f) (2025) - `P1` - citations: 1 - round3_promoted
- [Exploring the Synergy of Quantitative Factors and Newsflow Representations from Large Language Models for Stock Return Prediction](https://www.semanticscholar.org/paper/88f47a944ab8b957c86393b0900b3d93161473cd) (2025) - `P1` - citations: 0 - round2_promoted
- [Integrating Stock Features and Global Information via Large Language Models for Enhanced Stock Return Prediction](https://www.semanticscholar.org/paper/0fc94e0c7fea54407e9cf4e4fcbc5487be883b61) (2023) - `P2` - citations: 20 - round3_promoted

### Financial agents

- [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://www.semanticscholar.org/paper/c86a70ff639707e647da3a429fe8e1e5c04415f5) (2024) - `P0` - citations: 152 - round1_promoted_seed_for_round2
- [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://www.semanticscholar.org/paper/0b41a6899c29a04e1217e6cc80a3d915ea18e2d8) (2024) - `P0` - citations: 135 - round2_promoted
- [Designing Heterogeneous LLM Agents for Financial Sentiment Analysis](https://www.semanticscholar.org/paper/be4468df16aacad6dbb74f1d98ada26ddbd7dba5) (2024) - `P0` - citations: 115 - round3_promoted
- [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://www.semanticscholar.org/paper/95264f2fd070e9ee21dd2d36196a69c91a63e852) (2023) - `P0` - citations: 94 - round1_promoted_seed_for_round2
- [FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](https://www.semanticscholar.org/paper/d9f3ba8b48b68304b611e7d87c3d3ccf9abab32c) (2025) - `P0` - citations: 18 - round1_promoted_seed_for_round2
- [LiveTradeBench: Seeking Real-World Alpha with Large Language Models](https://www.semanticscholar.org/paper/9b8944c299cd7ce32db8bf187b96b508bede49d1) (2025) - `P0` - citations: 10 - round1_promoted_seed_for_round2
- [Time Travel is Cheating: Going Live with DeepFund for Real-Time Fund Investment Benchmarking](https://www.semanticscholar.org/paper/cd7438a5c5d731d744e9fce51bf702c6d3a8ffbd) (2025) - `P0` - citations: 10 - round1_promoted_seed_for_round2
- [Standard Benchmarks Fail -- Auditing LLM Agents in Finance Must Prioritize Risk](https://www.semanticscholar.org/paper/e06f72ec485c85472d1380d5667adb417635c981) (2025) - `P0` - citations: 9 - round1_promoted_seed_for_round2
- [Large Language Model Agents for Investment Management: Foundations, Benchmarks, and Research Frontiers](https://www.semanticscholar.org/paper/a5a80a83cf865a0f854332b02ec26353d436c036) (2025) - `P0` - citations: 5 - round1_promoted_seed_for_round2
- [FinBloom: Knowledge Grounding Large Language Model with Real-time Financial Data](https://www.semanticscholar.org/paper/fc21838d747b1b51bc8ef7022e3652d4407263d9) (2025) - `P0` - citations: 2 - round1_promoted_seed_for_round2
- [Will LLMs be Professional at Fund Investment? DeepFund: A Live Arena Perspective](https://www.semanticscholar.org/paper/67c606df1d20ee804ce586f3aa899652b2639781) (2025) - `P0` - citations: 2 - round1_promoted_seed_for_round2
- [Learning to Trade Like an Expert: Cognitive Fine-Tuning for Stable Financial Reasoning in Language Models](https://www.semanticscholar.org/paper/2692d9218c08789944132d22a78ec437baffd075) (2026) - `P0` - citations: 0 - round1_promoted_seed_for_round2
- [Learning to Generate Explainable Stock Predictions using Self-Reflective Large Language Models](https://www.semanticscholar.org/paper/a734edb6c3d70eec77ddb4504b2df87c3b74b77c) (2024) - `P1` - citations: 61 - round3_promoted
- [CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading](https://www.semanticscholar.org/paper/41e49f3e7cef50ec4b1fc4b2fe4dd3ba04ef3b9f) (2024) - `P1` - citations: 36 - round3_promoted
- [Enhancing Investment Analysis: Optimizing AI-Agent Collaboration in Financial Research](https://www.semanticscholar.org/paper/77ef9666a5fff2e5a0c68b59cabae8295c9739e2) (2024) - `P1` - citations: 36 - round2_promoted
- [Advancing innovation in financial stability: A comprehensive review of ai agent frameworks, challenges and applications](https://www.semanticscholar.org/paper/0ad50aa8e57901e59e959e2f2c0b6d221a0cf8cd) (2025) - `P1` - citations: 32 - round3_promoted
- [Automate Strategy Finding with LLM in Quant investment](https://www.semanticscholar.org/paper/1b31930e05ba75daf9dafb409242b53af663db66) (2024) - `P1` - citations: 32 - round2_promoted
- [Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations](https://www.semanticscholar.org/paper/5479040a44a53b9a7f58d97a91c79349e54e1976) (2023) - `P1` - citations: 32 - round3_promoted
- [HedgeAgents: A Balanced-aware Multi-agent Financial Trading System](https://www.semanticscholar.org/paper/701cd738cbdeb49b9cd9f2de3ee90d61d066faf5) (2025) - `P1` - citations: 31 - round2_promoted
- [Large Language Models for Financial and Investment Management: Applications and Benchmarks](https://www.semanticscholar.org/paper/f88c22f58d60dbfcceb2057bed44799f1f515980) (2024) - `P1` - citations: 30 - round2_promoted
- [When AI Meets Finance (StockAgent): Large Language Model-based Stock Trading in Simulated Real-world Environments](https://www.semanticscholar.org/paper/c8eabdc81e4c6d972336408d1a0a7dccfddece5f) (2024) - `P1` - citations: 30 - round2_promoted
- [MarS: a Financial Market Simulation Engine Powered by Generative Foundation Model](https://www.semanticscholar.org/paper/ef0cf7ac825cdea530ea5842314acea2532b5759) (2024) - `P1` - citations: 26 - round2_promoted
- [FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://www.semanticscholar.org/paper/c6e145e7e9e6a6e82e898d6e96997461cd5ec608) (2025) - `P1` - citations: 23 - round2_promoted
- [Agentic AI Systems Applied to tasks in Financial Services: Modeling and model risk management crews](https://www.semanticscholar.org/paper/32c3e7b6dfe4f7a0c265e56243ed71e67ec113f0) (2025) - `P1` - citations: 19 - round3_promoted
- [GPT's idea of stock factors](https://www.semanticscholar.org/paper/1d0d08d8255fca583cba525f0299d3a792c5133f) (2024) - `P1` - citations: 17 - round3_promoted
- [DianJin-R1: Evaluating and Enhancing Financial Reasoning in Large Language Models](https://www.semanticscholar.org/paper/9f7336aff4d63695ffbc7bbab23140bbc1cc9346) (2025) - `P1` - citations: 15 - round3_promoted
- [Large Language Models in equity markets: applications, techniques, and insights](https://www.semanticscholar.org/paper/b1553a62bd4fbf76ad6a41f05a1a4a5a13e862ad) (2025) - `P1` - citations: 12 - round2_promoted
- [MASS: Multi-Agent Simulation Scaling for Portfolio Construction](https://www.semanticscholar.org/paper/82804209a776b25f019c6a6082917eca98c0d5d9) (2025) - `P1` - citations: 9 - round3_promoted
- [FinArena: A Human-Agent Collaboration Framework for Financial Market Analysis and Forecasting](https://www.semanticscholar.org/paper/f18b6564594bc3f3326ba174416e7e7d9e61f2db) (2025) - `P1` - citations: 8 - round2_promoted
- [AI Agents in Finance and Fintech: A Scientific Review of Agent-Based Systems, Applications, and Future Horizons](https://www.semanticscholar.org/paper/9669e94896a7f774bdf149a87fd06a6e39f9a830) (2025) - `P1` - citations: 2 - round3_promoted
- [A Review of Large Language Models for Stock Price Forecasting from a Hedge-Fund Perspective](https://www.semanticscholar.org/paper/bb7ac50bcca09e26e3b273cc2e8da0656f37150c) (2026) - `P1` - citations: 0 - round3_promoted
- [P1GPT: a multi-agent LLM workflow module for multi-modal financial information analysis](https://www.semanticscholar.org/paper/5afed2970be135f7a3fae1d8864f53c39c32ee29) (2025) - `P1` - citations: 0 - round3_promoted

### Other relevant work

- [LLMs for Financial Advisement: A Fairness and Efficacy Study in Personal Decision Making](https://www.semanticscholar.org/paper/1dddc3cdca26cd434d48110f8d73674bb7f63c4f) (2023) - `P1` - citations: 53 - round2_promoted
- [RiskLabs: Predicting Financial Risk Using Large Language Model Based on Multi-Sources Data](https://www.semanticscholar.org/paper/79ad2001981acc7f24f70cdd8307821b70289fb9) (2024) - `P1` - citations: 35 - round3_promoted
- [Large Language Model in Financial Regulatory Interpretation](https://www.semanticscholar.org/paper/cda483cdf8c4c7a020def02f5523101558c78cca) (2024) - `P1` - citations: 12 - round2_promoted
- [Multimodal retrieval-augmented generation for financial documents: image-centric analysis of charts and tables with large language models](https://www.semanticscholar.org/paper/7cf98ce56b91fd97d664a2ec2f9f2e24c232a378) (2025) - `P1` - citations: 6 - round2_promoted


## Contributing

Open an issue or pull request with title, year, link, category, and a short note explaining why the paper belongs in the list. High-signal additions should either be finance-specific LLM work, a core financial NLP benchmark/dataset, or a highly cited foundation paper directly used by multiple finance LLM papers.

## Attribution

Paper metadata in `data/` was collected from the seed CSV and the Semantic Scholar Graph API. Abstracts and third-party metadata remain subject to their original rights and provider terms.

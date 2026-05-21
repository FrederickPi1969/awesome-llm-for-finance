# Awesome LLM for Finance

A curated reading list for large language models in finance: financial-domain LLMs, benchmarks, SEC filing analysis, financial reasoning, trading agents, investment research, and professional finance evaluation.

> Status: expanding public seed. The current catalog starts from 58 seed papers, four broad Semantic Scholar citation/reference expansion rounds, focused FinMem trading-agent, financial report analysis, RegTech/compliance, and multi-step specific-domain deep-dives.

## Taxonomy

Each paper is assigned to exactly one primary category. The taxonomy is intentionally a partition: the total number of papers in the categories below equals the total rows in `data/processed/curated_papers.csv`.

- **Surveys and Reviews** (20) - Survey, review, taxonomy, and overview papers that map the finance LLM landscape.
- **Foundation and Domain Language Models** (21) - Financial-domain LLMs, FinBERT-style models, instruction tuning, and domain adaptation work.
- **Benchmarks and Evaluation Suites** (18) - General finance LLM benchmarks, evaluation suites, exams, leaderboards, and broad task collections.
- **Financial QA, Reasoning, and Table Understanding** (12) - Question answering, numerical reasoning, financial table/text reasoning, and discrete reasoning tasks.
- **Reports, Filings, Accounting, and Risk** (39) - SEC filings, annual reports, XBRL, accounting, credit/risk, disclosure, and document analytics.
- **Trading, Investment, and Portfolio Management** (68) - Stock prediction, trading, alpha, portfolio construction, allocation, investment reports, and market analysis.
- **Agents and Multi-Agent Systems** (71) - Financial LLM agents, trading agents, multi-agent markets, agent benchmarks, and autonomous workflows.
- **RAG, Search, and Knowledge Systems** (28) - Retrieval-augmented generation, search, knowledge grounding, knowledge graphs, and document retrieval systems.
- **Multimodal and Multilingual Finance** (17) - Multimodal, multilingual, bilingual, and non-English financial LLM resources and evaluations.
- **Professional, Regulatory, and Advisory Applications** (14) - CFA/professional exams, financial advice, regulatory interpretation, compliance, and human-facing advisory settings.

## Trading Subthemes

Trading and investment papers are also tagged with a finer `trading_subtheme` field in `data/processed/curated_papers_by_taxonomy.csv`. These tags separate the current collection into more useful institutional-investing slices.

- **Alpha Mining and Factor Discovery** (11) - LLM-driven alpha discovery, formulaic factor mining, interpretable factors, and alpha decay control.
- **Derivatives, Options, and Structured Products** (21) - Options, derivatives, hedging, payoff reasoning, structured products, and volatility-surface tasks.
- **Market Simulation and Execution Infrastructure** (7) - Limit-order-book simulators, high-fidelity market simulators, and execution/HFT infrastructure used to evaluate trading agents.
- **Market Microstructure, Execution, and Prediction Markets** (20) - Order-level trading, execution agents, slippage, liquidity, transaction costs, prediction markets, and latency arbitrage.
- **Private Markets, VC, and Due Diligence** (7) - Venture capital, startup success prediction, private equity, private-market due diligence, and investment memo workflows.
- **Wealth, Advisory, and Personal Investing** (16) - Financial advisors, robo-advisory, investor profiling, suitability, private-investor risk, and portfolio advice.
- **Portfolio, ETF, and Asset Allocation** (34) - Portfolio construction, ETF/sector/macro allocation, and allocation rationale generation.
- **Trading Agents and Strategy Generation** (34) - LLM trading agents, multi-agent trading, strategy generation, backtesting, and executable trading instructions.
- **Stock Prediction and Market Forecasting** (14) - Stock-return prediction, market forecasting, sentiment-driven prediction, and general return-predictability tasks.
- **Investment Research and Financial Analysis** (48) - Equity research, investment reports, financial analysis workflows, and analyst-style systems.

## Contents

- [Surveys and Reviews](#surveys-and-reviews) (20)
- [Foundation and Domain Language Models](#foundation-and-domain-language-models) (21)
- [Benchmarks and Evaluation Suites](#benchmarks-and-evaluation-suites) (18)
- [Financial QA, Reasoning, and Table Understanding](#financial-qa-reasoning-and-table-understanding) (12)
- [Reports, Filings, Accounting, and Risk](#reports-filings-accounting-and-risk) (39)
- [Trading, Investment, and Portfolio Management](#trading-investment-and-portfolio-management) (68)
- [Agents and Multi-Agent Systems](#agents-and-multi-agent-systems) (71)
- [RAG, Search, and Knowledge Systems](#rag-search-and-knowledge-systems) (28)
- [Multimodal and Multilingual Finance](#multimodal-and-multilingual-finance) (17)
- [Professional, Regulatory, and Advisory Applications](#professional-regulatory-and-advisory-applications) (14)

## Papers by Theme

### Surveys and Reviews

- [Large Language Models in Finance: A Survey](https://arxiv.org/abs/2311.10723) (2023) - `P0` - citations: 425 - seed
- [Revolutionizing Finance with LLMs: An Overview of Applications and Insights](https://www.semanticscholar.org/paper/3d6197e4ab55a3a2785ce5934e48cfbe9fe9bf04) (2024) - `P0` - citations: 163 - expanded
- [A Survey of Large Language Models in Finance: FinLLMs](https://arxiv.org/abs/2402.02315) (2024) - `P0` - citations: 147 - seed
- [A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges](https://arxiv.org/abs/2406.11903) (2024) - `P0` - citations: 145 - seed
- [A Comprehensive Review of Generative AI in Finance](https://www.semanticscholar.org/paper/bc2dc0afd73c3a39ea750f48a7a5ee98178c48e6) (2024) - `P0` - citations: 33 - expanded
- [Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment](https://www.semanticscholar.org/paper/f56ff0c8f868716244d1c0d490a72f762f1ab64a) (2025) - `P0` - citations: 11 - expanded
- [A Survey on Large Language Models for Critical Societal Domains: Finance, Healthcare, and Law](https://www.semanticscholar.org/paper/c631a5458bfb0d86053af2258c219825477ba4f6) (2024) - `P1` - citations: 98 - expanded
- [A Scoping Review of ChatGPT Research in Accounting and Finance](https://www.semanticscholar.org/paper/93cf2624dc11b38457f603ff8c345c5f3fc9d52b) (2024) - `P1` - citations: 75 - expanded
- [Large Language Model Agent in Financial Trading: A Survey](https://arxiv.org/abs/2408.06361) (2024) - `P1` - citations: 66 - seed
- [Advancing innovation in financial stability: A comprehensive review of ai agent frameworks, challenges and applications](https://www.semanticscholar.org/paper/0ad50aa8e57901e59e959e2f2c0b6d221a0cf8cd) (2025) - `P1` - citations: 32 - expanded
- [From Deep Learning to Large Language Models: A Survey of Artificial Intelligence in Quantitative Investment](https://arxiv.org/html/2503.21422v1) (2025) - `P1` - citations: 21 - seed
- [Enhancing the Efficiency and Accuracy of Underlying Asset Reviews in Structured Finance: The Application of Multi-agent Framework](https://www.semanticscholar.org/paper/ed5fbcd360497715a8c42b130cfbe4b85e6d0dc1) (2024) - `P1` - citations: 8 - focused expansion
- [A Comprehensive Review of Gen AI Agents: Applications and Frameworks in Finance, Investments and Risk Domains](https://www.semanticscholar.org/paper/475f97cb4636acfb86112da16b66fab182bb46c9) (2025) - `P1` - citations: 7 - expanded
- [Integrating Large Language Models in Financial Investments and Market Analysis: A Survey](https://www.semanticscholar.org/paper/6e8331657256fdc8f83dd534fcdbf12dfa375359) (2025) - `P1` - citations: 7 - expanded
- [A Review on Large Language Models and Generative AI in Banking](https://www.semanticscholar.org/paper/ef91f3a0eb0cdc0d9fdc39e5bcf94189aea0513b) (2025) - `P1` - citations: 5 - focused expansion
- [Interpretable LLMs for Credit Risk: A Systematic Review and Taxonomy](https://www.semanticscholar.org/paper/18296b1ee7bc4c70bd5d44503f705f1b535c712d) (2025) - `P1` - citations: 4 - expanded
- [AI Agents in Finance and Fintech: A Scientific Review of Agent-Based Systems, Applications, and Future Horizons](https://www.semanticscholar.org/paper/9669e94896a7f774bdf149a87fd06a6e39f9a830) (2025) - `P1` - citations: 2 - expanded
- [The New Quant: A Survey of Large Language Models in Stock Return Prediction and Investment Decision-Making](https://arxiv.org/html/2510.05533v1) (2025) - `P1` - citations: 2 - seed
- [A Review of Large Language Models for Stock Price Forecasting from a Hedge-Fund Perspective](https://www.semanticscholar.org/paper/bb7ac50bcca09e26e3b273cc2e8da0656f37150c) (2026) - `P1` - citations: 0 - expanded
- [Bridging Language Models and Financial Analysis: A Survey of Datasets, Models, and Applications](https://arxiv.org/html/2503.22693) (2025) - `P2` - citations: 6 - seed

### Foundation and Domain Language Models

- [BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564) (2023) - `P0` - citations: 1294 - seed
- [FinBERT: Financial Sentiment Analysis with Pre-trained Language Models](https://www.semanticscholar.org/paper/7102bb3fe73bd057ff161d9db5214a267c1ef312) (2019) - `P0` - citations: 946 - expanded
- [FinBERT : A Large Language Model for Extracting Information from Financial Text†](https://www.semanticscholar.org/paper/8798b3a01c29fe0ce45a271bedd934787343dfb5) (2022) - `P0` - citations: 561 - expanded
- [FinGPT: Open-Source Financial Large Language Models](https://arxiv.org/abs/2306.06031) (2023) - `P0` - citations: 380 - seed
- [FinBERT: A Pretrained Language Model for Financial Communications](https://www.semanticscholar.org/paper/3578a7792904e6af3db8ffefdff86ab6a387c7c3) (2020) - `P0` - citations: 347 - expanded
- [FinBERT: A Pre-trained Financial Language Representation Model for Financial Text Mining](https://www.semanticscholar.org/paper/df0498605d5131098237e37914b402b67fea3936) (2020) - `P0` - citations: 286 - expanded
- [PIXIU: A Large Language Model, Instruction Data and Evaluation Benchmark for Finance](https://arxiv.org/abs/2306.05443) (2023) - `P0` - citations: 268 - seed
- [When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain](https://www.semanticscholar.org/paper/0882a2b2787b35dbcc6e341c953d964b77abd4df) (2022) - `P0` - citations: 157 - expanded
- [Transforming Sentiment Analysis in the Financial Domain with ChatGPT](https://www.semanticscholar.org/paper/3c4f1244301577cffff9affc73690669725e7e08) (2023) - `P0` - citations: 149 - expanded
- [Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning of General-Purpose Large Language Models](https://www.semanticscholar.org/paper/087a2f4cfea227be944f576f1f049e329316acac) (2023) - `P0` - citations: 128 - expanded
- [FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets](https://www.semanticscholar.org/paper/bd09391fbd124dc0c0a6be5d0ab2eb5d9c43fbac) (2023) - `P0` - citations: 113 - expanded
- [FinGPT: Democratizing Internet-scale Data for Financial Large Language Models](https://www.semanticscholar.org/paper/6121fb3e393597e02481a516f0035f06ec9a5836) (2023) - `P0` - citations: 105 - expanded
- [Mixing It Up: The Cocktail Effect of Multi-Task Fine-Tuning on LLM Performance - A Case Study in Finance](https://www.semanticscholar.org/paper/20461f6987f1846beb1cae0863d2aac35cba76fe) (2024) - `P0` - citations: 14 - expanded
- [From Scores to Skills: A Cognitive Diagnosis Framework for Evaluating Financial Large Language Models](https://www.semanticscholar.org/paper/ba13b3744678596741204a69dd337360d52cd85d) (2025) - `P0` - citations: 3 - expanded
- [FinBERT-FOMC: Fine-Tuned FinBERT Model with Sentiment Focus Method for Enhancing Sentiment Analysis of FOMC Minutes](https://www.semanticscholar.org/paper/fbd0999cfb30d0bf20641323baaaa5882f651c22) (2023) - `P1` - citations: 28 - expanded
- [A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification](https://www.semanticscholar.org/paper/e94fa7016d7e9814399e42480512a2a8bb73972e) (2025) - `P1` - citations: 26 - expanded
- [An Evaluation of Reasoning Capabilities of Large Language Models in Financial Sentiment Analysis](https://www.semanticscholar.org/paper/4a54ae690a0a1a2613031d31247d312545b86f04) (2024) - `P1` - citations: 18 - expanded
- [Open FinLLM Leaderboard: Towards Financial AI Readiness](https://www.semanticscholar.org/paper/06526d7f7bb077b92f73a2a01480304377a63463) (2025) - `P1` - citations: 15 - expanded
- [Comparative Investigation of GPT and FinBERT’s Sentiment Analysis Performance in News Across Different Sectors](https://www.semanticscholar.org/paper/83d5a3100782b9803f9e25fbc41d1fbf9e98bed1) (2025) - `P1` - citations: 14 - expanded
- [Reasoning or Overthinking: Evaluating Large Language Models on Financial Sentiment Analysis](https://www.semanticscholar.org/paper/e6135f05d90ca1e7a23118aa2a8fc7d86be76d3b) (2025) - `P1` - citations: 6 - expanded
- [FLaME: A Holistic Benchmark for Financial Language Models](https://arxiv.org/abs/2506.15846) (2025) - `P1` - citations: 1 - seed

### Benchmarks and Evaluation Suites

- [FinBen: A Holistic Financial Benchmark for Large Language Models](https://arxiv.org/abs/2402.12659) (2024) - `P0` - citations: 143 - seed
- [Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? A Study on Several Typical Tasks](https://www.semanticscholar.org/paper/f377b99a5f77ef94c736912dbdfe4108f4b22b69) (2023) - `P0` - citations: 114 - expanded
- [Empowering Many, Biasing a Few: Generalist Credit Scoring through Large Language Models](https://www.semanticscholar.org/paper/997d1e4c21fb62150f9b6379cdfe12521f0a318c) (2023) - `P0` - citations: 23 - expanded
- [Advancing Financial Engineering with Foundation Models: Progress, Applications, and Challenges](https://www.semanticscholar.org/paper/390a6229243d7cc42bf756fc9564b9c48dd43b6f) (2025) - `P0` - citations: 3 - expanded
- [Unlocking Data Value in Finance: A Study on Distillation and Difficulty-Aware Training](https://www.semanticscholar.org/paper/2781595bb5eb65d89c966feec9f560805d610738) (2026) - `P0` - citations: 1 - expanded
- [PIXIU: A Comprehensive Benchmark, Instruction Dataset and Large Language Model for Finance](https://www.semanticscholar.org/paper/dc7ee44dc2904228c0da316f6b35ddb6a15f4f63) (2023) - `P1` - citations: 70 - expanded
- [Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? An Examination on Several Typical Tasks](https://www.semanticscholar.org/paper/45d325884a5169df06e41288717b7a78c07bedb7) (2023) - `P1` - citations: 51 - round2_promoted_seed_for_round3
- [RiskLabs: Predicting Financial Risk Using Large Language Model Based on Multi-Sources Data](https://www.semanticscholar.org/paper/79ad2001981acc7f24f70cdd8307821b70289fb9) (2024) - `P1` - citations: 35 - expanded
- [BizFinBench: A Business-Driven Real-World Financial Benchmark for Evaluating LLMs](https://www.semanticscholar.org/paper/9de263bfddf6888f928bc66837f1dd788289de13) (2025) - `P1` - citations: 17 - expanded
- [FinanceReasoning: A Financial Benchmark for Large Reasoning Models](https://arxiv.org/html/2506.05828) (2025) - `P1` - citations: 17 - seed
- [Modal-adaptive Knowledge-enhanced Graph-based Financial Prediction from Monetary Policy Conference Calls with LLM](https://www.semanticscholar.org/paper/1e77ad3c89173c3c6e622c4935025442bcd5907f) (2024) - `P1` - citations: 14 - focused expansion
- [FinDABench: Benchmarking Financial Data Analysis Ability of Large Language Models](https://arxiv.org/abs/2401.02982) (2024) - `P1` - citations: 12 - seed
- [Advancing Anomaly Detection: Non-Semantic Financial Data Encoding With Large Language Models](https://www.semanticscholar.org/paper/c3aa9fb3366773efcded68170feb90bed301869a) (2024) - `P1` - citations: 10 - focused expansion
- [Exploring Large Language Models for Financial Applications: Techniques, Performance, and Challenges with FinMA](https://www.semanticscholar.org/paper/35d835d43450af4348ee49c8f7097b7ab9c3ecd0) (2025) - `P1` - citations: 2 - expanded
- [Evaluating LLMs in Finance Requires Explicit Bias Consideration](https://www.semanticscholar.org/paper/1744469bb8a5a2c5b462cc5d1f33ce621ab35424) (2026) - `P1` - citations: 2 - focused expansion
- [RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?](https://www.semanticscholar.org/paper/ec42863c5326fd635a0b0e2f3163af4035699dbb) (2026) - `P1` - citations: 2 - expanded
- [Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs](https://www.semanticscholar.org/paper/96a8eb94d07faf1b207c74132fb4a0d3358fa0bf) (2025) - `P1` - citations: 1 - focused expansion
- [Large Language Model Evaluation on Financial Benchmarks](https://research.ibm.com/publications/large-language-model-evaluation-on-financial-benchmarks) (2024) - `P2` - citations: 7 - seed

### Financial QA, Reasoning, and Table Understanding

- [FinQA: A Dataset of Numerical Reasoning over Financial Data](https://arxiv.org/abs/2109.00122) (2021) - `P0` - citations: 648 - seed
- [TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance](https://arxiv.org/abs/2105.07624) (2021) - `P0` - citations: 500 - seed
- [WWW'18 Open Challenge: Financial Opinion Mining and Question Answering](https://www.semanticscholar.org/paper/7191680b572ee7145f1a9d95ff11ab1ff44259f3) (2018) - `P0` - citations: 421 - expanded
- [ConvFinQA: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering](https://arxiv.org/abs/2210.03849) (2022) - `P0` - citations: 226 - seed
- [FinanceBench: A New Benchmark for Financial Question Answering](https://arxiv.org/abs/2311.11944) (2023) - `P0` - citations: 208 - seed
- [MultiHiertt: Numerical Reasoning over Multi Hierarchical Tabular and Textual Data](https://arxiv.org/abs/2206.01347) (2022) - `P0` - citations: 168 - seed
- [DocFinQA: A Long-Context Financial Reasoning Dataset](https://arxiv.org/html/2401.06915v2) (2024) - `P0` - citations: 61 - seed
- [FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](https://www.semanticscholar.org/paper/7efaf134965a957bedc73a60a0083699fd791e16) (2025) - `P0` - citations: 9 - expanded
- [Learning to Trade Like an Expert: Cognitive Fine-Tuning for Stable Financial Reasoning in Language Models](https://www.semanticscholar.org/paper/2692d9218c08789944132d22a78ec437baffd075) (2026) - `P0` - citations: 0 - expanded
- [BizBench: A Quantitative Reasoning Benchmark for Business and Finance](https://aclanthology.org/2024.acl-long.452.pdf) (2024) - `P1` - citations: 27 - seed
- [FAMMA: A Benchmark for Financial Domain Multilingual Multimodal Question Answering](https://www.semanticscholar.org/paper/1fca4660e5cdc872b8e2b3883457766c9e954a88) (2024) - `P1` - citations: 19 - expanded
- [DianJin-R1: Evaluating and Enhancing Financial Reasoning in Large Language Models](https://www.semanticscholar.org/paper/9f7336aff4d63695ffbc7bbab23140bbc1cc9346) (2025) - `P1` - citations: 15 - expanded

### Reports, Filings, Accounting, and Risk

- [Financial Statement Analysis with Large Language Models](https://arxiv.org/abs/2407.17866) (2024) - `P0` - citations: 70 - seed
- [TAT-LLM: A Specialized Language Model for Discrete Reasoning over Financial Tabular and Textual Data](https://www.semanticscholar.org/paper/b714baccfd4997ef6c14cbff3d8b4921493d7446) (2024) - `P0` - citations: 26 - expanded
- [XBRL Agent: Leveraging Large Language Models for Financial Report Analysis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4993495) (2024) - `P0` - citations: 17 - seed
- [Standard Benchmarks Fail -- Auditing LLM Agents in Finance Must Prioritize Risk](https://www.semanticscholar.org/paper/e06f72ec485c85472d1380d5667adb417635c981) (2025) - `P0` - citations: 9 - expanded
- [FinRpt: Financial Report Understanding and Generation Benchmark](https://arxiv.org/html/2511.07322v1) (2025) - `P0` - citations: 2 - seed
- [FinTagging: A Full-Scope Table-Aware XBRL Tagging Benchmark with LLMs](https://arxiv.org/abs/2505.20650) (2025) - `P0` - citations: 2 - seed
- [Fin-RATE: Financial Report Analytics and Tracking Evaluation for Large Language Models](https://arxiv.org/abs/2602.07294) (2026) - `P0` - citations: 2 - seed
- [Towards Competent AI for Fundamental Analysis in Finance: A Benchmark Dataset and Evaluation](https://www.semanticscholar.org/paper/3543d2e5874a9021cf53bb1db33e95af8fd0b924) (2025) - `P0` - citations: 1 - expanded
- [The Structure of Financial Equity Research Reports](https://arxiv.org/abs/2407.18327) (2024) - `P0` - citations: 0 - seed
- [Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning](https://www.semanticscholar.org/paper/95d638e7705ec561382268405bc488df4c26c7f7) (2025) - `P1` - citations: 66 - expanded
- [Bloated Disclosures: Can ChatGPT Help Investors Process Information?](https://www.semanticscholar.org/paper/af16b6f8146432e9437c1dd9b8320ee24ac63455) (2023) - `P1` - citations: 56 - expanded
- [GPT-InvestAR: Enhancing Stock Investment Strategies through Annual Report Analysis with Large Language Models](https://www.semanticscholar.org/paper/110052b69ccbcc280b1a806c4e0bf876e6a5b116) (2023) - `P1` - citations: 29 - expanded
- [Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and Accounting Tasks](https://www.semanticscholar.org/paper/128a8fdc8d15dcb2827eb75fab898e260f2e485c) (2025) - `P1` - citations: 26 - focused expansion
- [SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions](https://www.semanticscholar.org/paper/7b29d5ddee07066355ede470cb325603b7bc6c0e) (2024) - `P1` - citations: 17 - focused expansion
- [SEC-QA: A Systematic Benchmark for Evaluating Long-Context Question Answering on SEC Filings](https://arxiv.org/html/2406.14394v1) (2024) - `P1` - citations: 15 - seed
- [Measuring Firm-Level Supply Chain Risk Using A Generative Large Language Model](https://www.semanticscholar.org/paper/74de4e2c66b47539377eedf2726dad5c93a5b3ee) (2025) - `P1` - citations: 15 - focused expansion
- [Generative AI Solutions to Empower Financial Firms](https://www.semanticscholar.org/paper/6aa25a7fba787219fc7af14411f42b43d2eda1a9) (2024) - `P1` - citations: 12 - expanded
- [Event Identification for Supply Chain Risk Management Through News Analysis by Using Large Language Models](https://www.semanticscholar.org/paper/0754dff6096217daf0150f2b5f4114c89b9bb49e) (2024) - `P1` - citations: 7 - focused expansion
- [FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs](https://www.semanticscholar.org/paper/fe525530756c4b3a7d020c98dfbe75d8e0cc2b11) (2025) - `P1` - citations: 7 - focused expansion
- [Leveraging Internet-Sourced Text Data for Financial Analytics in Supply Chain Finance: A Large Language Model-Enhanced Text Mining Workflow](https://www.semanticscholar.org/paper/7ad8e6d84f7ce6145a15852fa19c370c0d485eb0) (2025) - `P1` - citations: 6 - focused expansion
- [SECQUE: A Benchmark for Evaluating Question-Answering on SEC Filings](https://arxiv.org/abs/2504.04596) (2025) - `P1` - citations: 6 - seed
- [Automating Financial Statement Audits with Large Language Models](https://www.semanticscholar.org/paper/0ce70fbf8d7128801adfd9626fc56b49201b62e1) (2025) - `P1` - citations: 4 - focused expansion
- [EDINET-Bench: Evaluating LLMs on Complex Financial Tasks using Japanese Financial Statements](https://www.semanticscholar.org/paper/e41a4abbb067bcb6fbc7dfebf8d4a20573b4e84e) (2025) - `P1` - citations: 4 - focused expansion
- [FinNLI: Novel Dataset for Multi-Genre Financial Natural Language Inference Benchmarking](https://www.semanticscholar.org/paper/f22b17e68fc846fd660951807862a78adc08525f) (2025) - `P1` - citations: 4 - expanded
- [Measuring climate risk with ChatGPT: the influence of firms market value within supply chains in China](https://www.semanticscholar.org/paper/ee3198dcf12dee9baf58134f3bb92ac7b75052d9) (2025) - `P1` - citations: 4 - focused expansion
- [A Scalable Data-Driven Framework for Systematic Analysis of SEC 10-K Filings Using Large Language Models](https://www.semanticscholar.org/paper/164c6a7606fc03d63d3836cd8b3a3234d09d37d4) (2024) - `P1` - citations: 3 - focused expansion
- [Language Models Fine-Tuning for Automatic Format Reconstruction of SEC Financial Filings](https://www.semanticscholar.org/paper/6ac39e68e162e27f2ca0f7345390112b91f69e1f) (2024) - `P1` - citations: 3 - focused expansion
- [Benchmarking large language models for supply chain risk identification: an extended evaluation within the LARD-SC framework](https://www.semanticscholar.org/paper/0258d13e84238957c3821d1ce76716aa2b4facff) (2025) - `P1` - citations: 3 - focused expansion
- [Evaluating Large Language Models (LLMs) in Financial NLP: A Comparative Study on Financial Report Analysis](https://www.semanticscholar.org/paper/9152606cc3f27124d96f12388e14e67ba3ac3f29) (2025) - `P1` - citations: 3 - focused expansion
- [Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows](https://www.semanticscholar.org/paper/9b4b712e7daffd0566593006b5e3340f957b0563) (2025) - `P1` - citations: 3 - focused expansion
- [HiFi-KPI: A Dataset for Hierarchical KPI Extraction from Earnings Filings](https://www.semanticscholar.org/paper/f28343ca4663f21b9901c599c9a4a5fae7d81047) (2025) - `P1` - citations: 1 - focused expansion
- [ALERA: An Entropy-Based LLM Multi-Agent Framework for Dynamic Risk Quantification in Quantitative Investing](https://www.semanticscholar.org/paper/12cf7474ba0c98d7c376fe4e47847d1ef35de14f) (2025) - `P1` - citations: 0 - expanded
- [From text to risk: Predicting repayment risk in supply chain finance with deep learning and large language models](https://www.semanticscholar.org/paper/aafaa3ae79682cac015ceddb4c9e9f68cce7a09a) (2025) - `P1` - citations: 0 - focused expansion
- [Quantifying Material Risks from Textual Disclosures in Financial Statements using Large Language Model Agents](https://www.bis.org/ifc/publ/ifcb65_09_rh.pdf) (2025) - `P1` - citations:  - seed
- [Detecting Semantic Mismatches in XBRL Tag Mapping for SEC 10-K Filings: A Text Comparison and Historical Consistency Analysis](https://www.semanticscholar.org/paper/e123ec052cb2aab036fb0ace58991d3cacb4a013) (2026) - `P1` - citations: 0 - focused expansion
- [Document-Level Numerical Reasoning across Single and Multiple Tables in Financial Reports](https://www.semanticscholar.org/paper/53d7cd998e6ec4794422688c0a2c3e2cd70025d2) (2026) - `P1` - citations: 0 - focused expansion
- [Measuring Corporate Risk Using Large Language Model Embeddings: Evidence on Corporate Climate Risk and Supply Chain Restructuring](https://www.semanticscholar.org/paper/ce2c5883b3610ce8523d17b515578bdf5f3b1e97) (2026) - `P1` - citations: 0 - focused expansion
- [Taxonomy-Aligned Risk Extraction from 10-K Filings](https://arxiv.org/abs/2601.15247) (2026) - `P1` - citations: 0 - seed
- [Financial Numeric Extreme Labelling: A Dataset and Benchmarking for XBRL Tagging](https://www.semanticscholar.org/paper/8ac0f32488bd01f7dc74c859ba1afb195498b333) (2023) - `P2` - citations: 16 - focused expansion

### Trading, Investment, and Portfolio Management

- [From fiction to fact: the growing role of generative AI in business and finance](https://www.semanticscholar.org/paper/916ffbf18036025e71d9384ea5a726a95f08589d) (2023) - `P0` - citations: 134 - expanded
- [Temporal Data Meets LLM - Explainable Financial Time Series Forecasting](https://www.semanticscholar.org/paper/681253389d2cc27103753749f4c7556699d55471) (2023) - `P0` - citations: 121 - expanded
- [InvestLM: A Large Language Model for Investment using Financial Domain Instruction Tuning](https://www.semanticscholar.org/paper/844bc3b26b5c63ec3b251ae634c194dcfb41a7d2) (2023) - `P0` - citations: 115 - expanded
- [FinLlama: Financial Sentiment Classification for Algorithmic Trading Applications](https://www.semanticscholar.org/paper/15b0a6ccb198b2936e36266be992da78a29953fd) (2024) - `P0` - citations: 29 - expanded
- [Responsible Innovation: A Strategic Framework for Financial LLM Integration](https://www.semanticscholar.org/paper/3a48e315facb5115eacea25faf2cc32caa01d53b) (2025) - `P0` - citations: 10 - expanded
- [Evaluating Financial Intelligence in Large Language Models: Benchmarking SuperInvesting AI with LLM Engines](https://www.semanticscholar.org/paper/a64372654025158c2cbb49dd6194c17e967256f0) (2026) - `P0` - citations: 1 - expanded
- [Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models](https://arxiv.org/abs/2304.07619) (2023) - `P1` - citations: 312 - seed
- [ChatGPT Informed Graph Neural Network for Stock Movement Prediction](https://www.semanticscholar.org/paper/d3ba770fa1f48458b7ccbc88307b942cfb751a36) (2023) - `P1` - citations: 82 - expanded
- [Sentiment trading with large language models](https://www.semanticscholar.org/paper/f0f339d02a94d9609fc30561e72b3fe1ad83bca4) (2024) - `P1` - citations: 78 - expanded
- [Can ChatGPT improve investment decisions? From a portfolio management perspective](https://www.semanticscholar.org/paper/2516b8d7f61da0fac219cf00f488a7d8d3d7d5c7) (2024) - `P1` - citations: 72 - expanded
- [Deficiency of Large Language Models in Finance: An Empirical Examination of Hallucination](https://www.semanticscholar.org/paper/5838b56f2c7ca3dd946428dae07bdc26a9265c67) (2023) - `P1` - citations: 63 - expanded
- [Forecasting the S&P 500 Index Using Mathematical-Based Sentiment Analysis and Deep Learning Models: A FinBERT Transformer Model and LSTM](https://www.semanticscholar.org/paper/21870c270fd33369b664f216ef6669b200ee331a) (2023) - `P1` - citations: 62 - expanded
- [Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment](https://www.semanticscholar.org/paper/ba622a5136681f25ceead6815c932fbcfbde0429) (2023) - `P1` - citations: 57 - expanded
- [Can Large Language Models beat wall street? Evaluating GPT-4’s impact on financial decision-making with MarketSenseAI](https://www.semanticscholar.org/paper/a25a6a7dabe6621e5e74cccdc3963aea947d2d20) (2024) - `P1` - citations: 53 - expanded
- [Harnessing Earnings Reports for Stock Predictions: A QLoRA-Enhanced LLM Approach](https://www.semanticscholar.org/paper/31e6b91ed8eb6f5fe8703301fc439fd1af160132) (2024) - `P1` - citations: 53 - expanded
- [LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction](https://www.semanticscholar.org/paper/7185f24f33de547954baa0c71cafaf41786e81ba) (2024) - `P1` - citations: 48 - expanded
- [Innovative Sentiment Analysis and Prediction of Stock Price Using FinBERT, GPT-4 and Logistic Regression: A Data-Driven Approach](https://www.semanticscholar.org/paper/65def91046a328ccb3ae305316bf8ba993817aef) (2024) - `P1` - citations: 39 - expanded
- [FinVis-GPT: A Multimodal Large Language Model for Financial Chart Analysis](https://www.semanticscholar.org/paper/0edcd1ce1d44359e8bf255b7216b9b56fa2cea33) (2023) - `P1` - citations: 34 - expanded
- [A Fused Large Language Model for Predicting Startup Success](https://www.semanticscholar.org/paper/ca1d86ce8cbc26d46a9ec6c698ec3576eac5fcae) (2024) - `P1` - citations: 34 - focused expansion
- [Can ChatGPT Plan Your Retirement?: Generative AI and Financial Advice](https://www.semanticscholar.org/paper/d45c2ea9320fd1967c77e97073c3ffe3a7da7dbc) (2024) - `P1` - citations: 32 - focused expansion
- [Hybrid LSTM and GRU for Cryptocurrency Price Forecasting Based on Social Network Sentiment Analysis Using FinBERT](https://www.semanticscholar.org/paper/2b24d46f381954757a9f9bdd8635b38630f403d6) (2023) - `P1` - citations: 30 - expanded
- [Assessing Look-Ahead Bias in Stock Return Predictions Generated by GPT Sentiment Analysis](https://www.semanticscholar.org/paper/af42ae531ad0c41518fcf3a382e6e9f1ba465601) (2023) - `P1` - citations: 29 - expanded
- [Large Language Model Adaptation for Financial Sentiment Analysis](https://www.semanticscholar.org/paper/4bbc278bc27a399bda7bc3015d2f38bd34f8dff7) (2024) - `P1` - citations: 24 - expanded
- [Ploutos: Towards interpretable stock movement prediction with financial large language model](https://www.semanticscholar.org/paper/fc4968617eae1d875a77ed0372be8f2e6118440a) (2024) - `P1` - citations: 21 - expanded
- [Fine-Tuning Large Language Models for Stock Return Prediction Using Newsflow](https://www.semanticscholar.org/paper/f6c0a84ac1f1fe79cfde96f4e163d0d69f9c06cb) (2024) - `P1` - citations: 17 - expanded
- [StockGPT: A GenAI Model for Stock Prediction and Trading](https://arxiv.org/abs/2404.05101) (2024) - `P1` - citations: 17 - seed
- [AI in Investment Analysis: Large Language Models for Equity Stock Ratings](https://arxiv.org/abs/2411.00856) (2024) - `P1` - citations: 14 - seed
- [ECC Analyzer: Extracting Trading Signal from Earnings Conference Calls using Large Language Model for Stock Volatility Prediction](https://www.semanticscholar.org/paper/09eb8ced2d6b0ef04d9dff80b593213086331711) (2024) - `P1` - citations: 14 - focused expansion
- [Can LLM-Based Financial Investing Strategies Outperform?](https://arxiv.org/abs/2505.07078) (2025) - `P1` - citations: 14 - seed
- [FinanceQA: A Benchmark for Evaluating Financial Analysis Capabilities of Large Language Models](https://www.semanticscholar.org/paper/5f8fe6f3b3b8c0b80ca29b806f7709b70fc9530e) (2025) - `P1` - citations: 14 - focused expansion
- [Decision-Informed Neural Networks with Large Language Model Integration for Portfolio Optimization](https://ideas.repec.org/p/arx/papers/2502.00828.html) (2025) - `P1` - citations: 12 - seed
- [Trading-R1: Financial Trading with LLM Reasoning via Reinforcement Learning](https://www.semanticscholar.org/paper/d9cb5bb3ef2a2f352ac571b7ead452a4256da192) (2025) - `P1` - citations: 12 - focused expansion
- [Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining](https://www.semanticscholar.org/paper/5a0c9fe6746ac535917fe17797f3d2d689f3f35f) (2025) - `P1` - citations: 11 - focused expansion
- [ECC Analyzer: Extract Trading Signal from Earnings Conference Calls using Large Language Model for Stock Performance Prediction](https://www.semanticscholar.org/paper/6fedc49097f302e4d7deb04fb51ada81c27c9a64) (2024) - `P1` - citations: 8 - focused expansion
- [Chain-of-Alpha: Unleashing the Power of Large Language Models for Alpha Mining in Quantitative Trading](https://www.semanticscholar.org/paper/d392598fbffaae986b15695b24611205be2e6ec3) (2025) - `P1` - citations: 8 - focused expansion
- [FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness](https://www.semanticscholar.org/paper/ae31ca9344da43928a894bf9641b199290a109f6) (2025) - `P1` - citations: 7 - focused expansion
- [LOB-Bench: Benchmarking Generative AI for Finance - an Application to Limit Order Book Data](https://www.semanticscholar.org/paper/80e111a3da98a87e170f797c6dee988871d78b1c) (2025) - `P1` - citations: 7 - focused expansion
- [FinBERT2: A Specialized Bidirectional Encoder for Bridging the Gap in Finance-Specific Deployment of Large Language Models](https://www.semanticscholar.org/paper/fc1a94c865f4ba58f0da35f6a377b4f37eb2c356) (2025) - `P1` - citations: 5 - focused expansion
- [Leveraging Large Language Models for Top-Down Sector Allocation](https://arxiv.org/html/2503.09647v5) (2025) - `P1` - citations: 3 - seed
- [Interpreting Fedspeak with Confidence: A LLM-Based Uncertainty-Aware Framework Guided by Monetary Policy Transmission Paths](https://www.semanticscholar.org/paper/b0baf442a5ba9092ee8464451f2e1f9f78744bf6) (2025) - `P1` - citations: 2 - focused expansion
- [The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction](https://www.semanticscholar.org/paper/79da23d856daac76b4f051523b8f09abd903e31f) (2025) - `P1` - citations: 2 - focused expansion
- [FinTradeBench: A Comprehensive Benchmark for Fundamental and Technical Analysis in Financial Trading](https://arxiv.org/abs/2603.19225) (2026) - `P1` - citations: 2 - seed
- [Application of Startup Success Prediction Models and Business Document Extraction Using Large Language Models to Enhance Due Diligence Efficiency](https://www.semanticscholar.org/paper/0e6bf5048fb7307a03ac3ceb4398be7c64ee09b6) (2024) - `P1` - citations: 1 - focused expansion
- [BondBERT: What we learn when assigning sentiment in the bond market](https://www.semanticscholar.org/paper/21015b352de7fa3ecaa804345bab13b6e1693c44) (2025) - `P1` - citations: 1 - expanded
- [FinCARE: Financial Causal Analysis with Reasoning and Evidence](https://www.semanticscholar.org/paper/ccb9c36b4ae6a404b968c4c3cbd140967c4d61f4) (2025) - `P1` - citations: 1 - focused expansion
- [Fine-Tuning and Explaining FinBERT for Sector-Specific Financial News: A Reproducible Workflow](https://www.semanticscholar.org/paper/0099ce22044724b6e13fc4f246ebd7b78a0b2b72) (2025) - `P1` - citations: 1 - focused expansion
- [Large Language Models for Financial Knowledge Extraction Analytical Insights and Corporate Planning Support](https://www.semanticscholar.org/paper/8dd640e8c2d469fb7a1d3286a0d7b14175b9234f) (2025) - `P1` - citations: 1 - expanded
- [MM-DREX: Multimodal-Driven Dynamic Routing of LLM Experts for Financial Trading](https://www.semanticscholar.org/paper/d1370c155148e2fe7605895460beb9ecb2f378b6) (2025) - `P1` - citations: 1 - focused expansion
- [The recent history of large language model in investment and portfolio management: is it a revolution in finance?](https://www.semanticscholar.org/paper/e23021a2ab136fa32d80fe211b0714d72b6b2dbe) (2025) - `P1` - citations: 1 - expanded
- [PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data](https://www.semanticscholar.org/paper/eb4c32849244870d5ed63f8f76355860edcdb4c5) (2026) - `P1` - citations: 1 - focused expansion
- [Navigating Complexity: GPT-4's Performance in Predicting Earnings and Stock Returns in China's A-Share Market](https://www.semanticscholar.org/paper/72fb0ae13fd11664293735cb678a5874175734f9) (2024) - `P1` - citations: 0 - focused expansion
- [Sentiment-driven prediction of financial returns: a Bayesian-enhanced FinBERT approach](https://www.semanticscholar.org/paper/317d7890d7feb66e5f6a9ece0e8fd09736fce136) (2024) - `P1` - citations: 0 - focused expansion
- [Can large language models effectively process and execute financial trading instructions?](https://www.semanticscholar.org/paper/26fb85af13ddd480b009f5b4456a35a39a4e2982) (2025) - `P1` - citations: 0 - focused expansion
- [Dynamic Hedging Strategies in Derivatives Markets with LLM-Driven Sentiment and News Analytics](https://www.semanticscholar.org/paper/c0558de2b272a9597383da1c73df6b059c87b075) (2025) - `P1` - citations: 0 - focused expansion
- [Exploring the Synergy of Quantitative Factors and Newsflow Representations from Large Language Models for Stock Return Prediction](https://www.semanticscholar.org/paper/88f47a944ab8b957c86393b0900b3d93161473cd) (2025) - `P1` - citations: 0 - expanded
- [LLM-Guided Evolutionary Strategy Generation for Quantitative Trading](https://www.semanticscholar.org/paper/af6aee2405f1caad07f697dbd7e2e3614223d9d9) (2025) - `P1` - citations: 0 - focused expansion
- [Task-Adaptive Large Language Models to Generate Human-Persuasive Investment Reports](https://aclanthology.org/2025.finnlp-2.23.pdf) (2025) - `P1` - citations: 0 - seed
- [AlphaForgeBench: Benchmarking End-to-End Trading Strategy Design with Large Language Models](https://www.semanticscholar.org/paper/38c9044df9377ea3ba62e82b30f52c7c5b07587b) (2026) - `P1` - citations: 0 - focused expansion
- [CN-Buzz2Portfolio: A Chinese-Market Dataset and Benchmark for LLM-Based Macro and Sector Asset Allocation from Daily Trending Financial News](https://www.semanticscholar.org/paper/7897014ae2caeee70d65df37ba8e5ed2bb3c4aee) (2026) - `P1` - citations: 0 - focused expansion
- [FinReasoning: A Hierarchical Benchmark for Reliable Financial Research Reporting](https://www.semanticscholar.org/paper/13f2f65f72b72da24b20b209ec803b1fa0e36871) (2026) - `P1` - citations: 0 - focused expansion
- [FinSheet-Bench: From Simple Lookups to Complex Reasoning, Where LLMs Break on Financial Spreadsheets](https://www.semanticscholar.org/paper/2bcc14eeb7350ea0132299d101e9b5c6139d5f4f) (2026) - `P1` - citations: 0 - focused expansion
- [From Natural Language to Executable Option Strategies via Large Language Models](https://www.semanticscholar.org/paper/dfdef151624d19f2bd6d8003f13dd5c9c2bc60ae) (2026) - `P1` - citations: 0 - focused expansion
- [LLM-Based Intelligent Risk Identification for SMEs: A Comparative Study of Prompt Engineering Strategies](https://www.semanticscholar.org/paper/ed4f58c05aa6e7c132a8be192ae6855d1eb993b4) (2026) - `P1` - citations: 0 - focused expansion
- [QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies](https://www.semanticscholar.org/paper/e27229889ba49ebfd44f4b914a2cc27768474900) (2026) - `P1` - citations: 0 - focused expansion
- [The Wall Street Neophyte: A Zero-Shot Analysis of ChatGPT over Multimodal Stock Movement Prediction Challenges](https://arxiv.org/abs/2304.05351) (2023) - `P2` - citations: 77 - seed
- [Integrating Stock Features and Global Information via Large Language Models for Enhanced Stock Return Prediction](https://www.semanticscholar.org/paper/0fc94e0c7fea54407e9cf4e4fcbc5487be883b61) (2023) - `P2` - citations: 20 - expanded
- [Your AI, Not Your View: The Bias of Large Language Models in Investment Analysis](https://arxiv.org/html/2507.20957v4) (2025) - `P2` - citations: 11 - seed
- [Leveraging Large Language Models for Institutional Investment Management](https://arxiv.org/abs/2411.19515) (2024) - `P2` - citations: 3 - seed

### Agents and Multi-Agent Systems

- [FinMem: A Performance-Enhanced Large Language Model Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743) (2023) - `P0` - citations: 177 - seed
- [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://www.semanticscholar.org/paper/c86a70ff639707e647da3a429fe8e1e5c04415f5) (2024) - `P0` - citations: 152 - expanded
- [TradingAgents: Multi-Agents Large Language Models for Financial Trading](https://arxiv.org/abs/2412.20138) (2024) - `P0` - citations: 139 - seed
- [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://www.semanticscholar.org/paper/0b41a6899c29a04e1217e6cc80a3d915ea18e2d8) (2024) - `P0` - citations: 135 - expanded
- [Designing Heterogeneous LLM Agents for Financial Sentiment Analysis](https://www.semanticscholar.org/paper/be4468df16aacad6dbb74f1d98ada26ddbd7dba5) (2024) - `P0` - citations: 115 - expanded
- [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://www.semanticscholar.org/paper/95264f2fd070e9ee21dd2d36196a69c91a63e852) (2023) - `P0` - citations: 94 - expanded
- [FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models](https://arxiv.org/abs/2405.14767) (2024) - `P0` - citations: 41 - seed
- [InvestorBench: A Benchmark for Large Language Model Agents in Financial Decision-Making](https://arxiv.org/abs/2412.18174) (2024) - `P0` - citations: 39 - seed
- [FinRobot: AI Agent for Equity Research and Valuation with Large Language Models](https://arxiv.org/abs/2411.08804) (2024) - `P0` - citations: 13 - seed
- [LiveTradeBench: Seeking Real-World Alpha with Large Language Models](https://www.semanticscholar.org/paper/9b8944c299cd7ce32db8bf187b96b508bede49d1) (2025) - `P0` - citations: 10 - expanded
- [Time Travel is Cheating: Going Live with DeepFund for Real-Time Fund Investment Benchmarking](https://www.semanticscholar.org/paper/cd7438a5c5d731d744e9fce51bf702c6d3a8ffbd) (2025) - `P0` - citations: 10 - expanded
- [Large Language Model Agents for Investment Management: Foundations, Benchmarks, and Research Frontiers](https://www.semanticscholar.org/paper/a5a80a83cf865a0f854332b02ec26353d436c036) (2025) - `P0` - citations: 5 - expanded
- [Will LLMs be Professional at Fund Investment? DeepFund: A Live Arena Perspective](https://www.semanticscholar.org/paper/67c606df1d20ee804ce586f3aa899652b2639781) (2025) - `P0` - citations: 2 - expanded
- [ABIDES: Towards High-Fidelity Multi-Agent Market Simulation](https://www.semanticscholar.org/paper/2262d43178de9d16b90f622624a0a59906c309fd) (2020) - `P1` - citations: 86 - focused expansion
- [Learning to Generate Explainable Stock Predictions using Self-Reflective Large Language Models](https://www.semanticscholar.org/paper/a734edb6c3d70eec77ddb4504b2df87c3b74b77c) (2024) - `P1` - citations: 61 - expanded
- [CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading](https://www.semanticscholar.org/paper/41e49f3e7cef50ec4b1fc4b2fe4dd3ba04ef3b9f) (2024) - `P1` - citations: 36 - expanded
- [Enhancing Investment Analysis: Optimizing AI-Agent Collaboration in Financial Research](https://www.semanticscholar.org/paper/77ef9666a5fff2e5a0c68b59cabae8295c9739e2) (2024) - `P1` - citations: 36 - round2_promoted_seed_for_round3
- [INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](https://www.semanticscholar.org/paper/03039fbfcc6d46c2d52ec039f923990d4c95de85) (2025) - `P1` - citations: 36 - expanded
- [Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations](https://www.semanticscholar.org/paper/5479040a44a53b9a7f58d97a91c79349e54e1976) (2023) - `P1` - citations: 32 - expanded
- [Automate Strategy Finding with LLM in Quant investment](https://www.semanticscholar.org/paper/1b31930e05ba75daf9dafb409242b53af663db66) (2024) - `P1` - citations: 32 - expanded
- [HedgeAgents: A Balanced-aware Multi-agent Financial Trading System](https://www.semanticscholar.org/paper/701cd738cbdeb49b9cd9f2de3ee90d61d066faf5) (2025) - `P1` - citations: 31 - expanded
- [Large Language Models for Financial and Investment Management: Applications and Benchmarks](https://www.semanticscholar.org/paper/f88c22f58d60dbfcceb2057bed44799f1f515980) (2024) - `P1` - citations: 30 - expanded
- [When AI Meets Finance (StockAgent): Large Language Model-based Stock Trading in Simulated Real-world Environments](https://www.semanticscholar.org/paper/c8eabdc81e4c6d972336408d1a0a7dccfddece5f) (2024) - `P1` - citations: 30 - expanded
- [JAX-LOB: A GPU-Accelerated limit order book simulator to unlock large scale reinforcement learning for trading](https://www.semanticscholar.org/paper/a8d9846e3faa0d496c0ce08b31499cf3aebca94a) (2023) - `P1` - citations: 26 - focused expansion
- [MarS: a Financial Market Simulation Engine Powered by Generative Foundation Model](https://www.semanticscholar.org/paper/ef0cf7ac825cdea530ea5842314acea2532b5759) (2024) - `P1` - citations: 26 - expanded
- [AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](https://www.semanticscholar.org/paper/aa7d10e820e607f7af146d2ee7a03d41841ff2cb) (2025) - `P1` - citations: 26 - focused expansion
- [Finance Agent Benchmark: Evaluating Language Model Agents as Financial Assistants](https://arxiv.org/abs/2508.00828) (2025) - `P1` - citations: 26 - seed
- [FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://www.semanticscholar.org/paper/c6e145e7e9e6a6e82e898d6e96997461cd5ec608) (2025) - `P1` - citations: 23 - expanded
- [GPT's idea of stock factors](https://www.semanticscholar.org/paper/1d0d08d8255fca583cba525f0299d3a792c5133f) (2024) - `P1` - citations: 17 - expanded
- [StockBench: Can Large Language Models Beat the Stock Market?](https://arxiv.org/html/2510.02209v2) (2025) - `P1` - citations: 15 - seed
- [Can Large Language Models Mine Interpretable Financial Factors More Effectively? A Neural-Symbolic Factor Mining Agent Model](https://www.semanticscholar.org/paper/798467c14bd05df92408a58072d1af39b7e06a7b) (2024) - `P1` - citations: 14 - focused expansion
- [Can Large Language Models Trade? Testing Financial Theories with LLM Agents in Market Simulations](https://www.semanticscholar.org/paper/e97ab13fb2a142c61a2c1192d097e98e6662a7ac) (2025) - `P1` - citations: 14 - focused expansion
- [MarketSenseAI 2.0: Enhancing Stock Analysis Through LLM Agents](https://www.semanticscholar.org/paper/f937b109dbc2bb4c831af3b63487bf001834cef0) (2025) - `P1` - citations: 13 - expanded
- [Large Language Models in equity markets: applications, techniques, and insights](https://www.semanticscholar.org/paper/b1553a62bd4fbf76ad6a41f05a1a4a5a13e862ad) (2025) - `P1` - citations: 12 - expanded
- [When Agents Trade: Live Multi-Market Trading Benchmark for LLM Agents](https://www.semanticscholar.org/paper/efbbb0b34d1f07b1c2c3cc2eda3ddec0d9136180) (2025) - `P1` - citations: 11 - expanded
- [MASS: Multi-Agent Simulation Scaling for Portfolio Construction](https://www.semanticscholar.org/paper/82804209a776b25f019c6a6082917eca98c0d5d9) (2025) - `P1` - citations: 9 - expanded
- [FinArena: A Human-Agent Collaboration Framework for Financial Market Analysis and Forecasting](https://www.semanticscholar.org/paper/f18b6564594bc3f3326ba174416e7e7d9e61f2db) (2025) - `P1` - citations: 8 - expanded
- [QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading](https://www.semanticscholar.org/paper/23aab54ccfd0b5ac0f9995a02ebb7d0765ce4914) (2025) - `P1` - citations: 7 - focused expansion
- [StockSim: A Dual-Mode Order-Level Simulator for Evaluating Multi-Agent LLMs in Financial Markets](https://www.semanticscholar.org/paper/336c89f0dadae33e79c1730e2f62f78ad4c3fffe) (2025) - `P1` - citations: 5 - focused expansion
- [TradingGroup: A Multi-Agent Trading System with Self-Reflection and Data-Synthesis](https://www.semanticscholar.org/paper/0b49f889237966c002165ae9af2be864187a02d2) (2025) - `P1` - citations: 5 - focused expansion
- [DeltaHedge: A Multi-Agent Framework for Portfolio Options Optimization](https://www.semanticscholar.org/paper/8d945047c842438ded67ed1e3e212271d40dcf0f) (2025) - `P1` - citations: 4 - focused expansion
- [Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents](https://www.semanticscholar.org/paper/95f225d1e545977115c535bcd696025a043e590e) (2025) - `P1` - citations: 3 - focused expansion
- [FactorMAD: A Multi-Agent Debate Framework Based on Large Language Models for Interpretable Stock Alpha Factor Mining](https://www.semanticscholar.org/paper/4a6015774ecfab2fd75ef7fa936a88ef7338daf9) (2025) - `P1` - citations: 3 - focused expansion
- [ATLAS: Adaptive Trading with LLM AgentS Through Dynamic Prompt Optimization and Multi-Agent Coordination](https://www.semanticscholar.org/paper/be8e14fdedf1b3edd32ae453e524f5b5ee727a7e) (2025) - `P1` - citations: 2 - focused expansion
- [Cognitive Alpha Mining via LLM-Driven Code-Based Evolution](https://www.semanticscholar.org/paper/0bcbc6fc6d7c872cbc98c8a0d0bcec053d21e02a) (2025) - `P1` - citations: 2 - focused expansion
- [From Earnings Calls to Investment Reports: Evaluating Role-based Multi-Agent LLM Systems](https://www.semanticscholar.org/paper/2e2247c23e3582030950b08828074d23ba4fa86f) (2025) - `P1` - citations: 2 - focused expansion
- [To Trade or Not to Trade: An Agentic Approach to Estimating Market Risk Improves Trading Decisions](https://www.semanticscholar.org/paper/c5580a444dfd0cd80dc915fc7d1da7061a4855d7) (2025) - `P1` - citations: 2 - focused expansion
- [Trade in Minutes! Rationality-Driven Agentic System for Quantitative Financial Trading](https://www.semanticscholar.org/paper/c78c601e1fff91dd466cc0ee78db27654e604111) (2025) - `P1` - citations: 2 - expanded
- [TradeTrap: Are LLM-based Trading Agents Truly Reliable and Faithful?](https://www.semanticscholar.org/paper/f85ceb388f4252862609da9d5bab478a116e2ed3) (2025) - `P1` - citations: 2 - focused expansion
- [Equity Research Chatbot Using LLM: A Responsive Agent for Investment Research](https://www.semanticscholar.org/paper/7bb4a5e42968d11762bd82b57b0f68797235bb21) (2024) - `P1` - citations: 1 - focused expansion
- [Beyond Isolated Investor: Predicting Startup Success via Roleplay-Based Collective Agents](https://www.semanticscholar.org/paper/79d817735b4da4bb0103593698d923fb7102461a) (2025) - `P1` - citations: 1 - focused expansion
- [FinSphere: A Conversational Stock Analysis Agent based on Large Language Models](https://arxiv.org/abs/2501.12399) (2025) - `P1` - citations: 1 - seed
- [Strategic Complexity and Behavioral Distortion: Retail Investing Under Large Language Model Augmentation](https://www.semanticscholar.org/paper/a0dc01bc2e145a521b4682df0719a167730cf3d0) (2025) - `P1` - citations: 1 - focused expansion
- [Design and Empirical Study of a Large Language Model-Based Multi-Agent Investment System for Chinese Public REITs](https://www.semanticscholar.org/paper/4f1188a5073c4d475eb959e1a667ad5bc7cb2f1e) (2026) - `P1` - citations: 1 - focused expansion
- [QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining](https://www.semanticscholar.org/paper/3821672c3b0665b1250e1fffabb20283f1d8cda6) (2026) - `P1` - citations: 1 - focused expansion
- [Signal or Noise in Multi-Agent LLM-based Stock Recommendations?](https://www.semanticscholar.org/paper/a3f2d5e7cafe1dd5672fadcddfc72135107c57c2) (2026) - `P1` - citations: 1 - focused expansion
- [Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks](https://www.semanticscholar.org/paper/d9d5b834ed8657fafdf851da941c52c73edd6ce5) (2026) - `P1` - citations: 1 - focused expansion
- [Agentic Portfolio Construction: A Multi-Agent Architecture for LLM-Driven Financial Asset Allocation](https://www.semanticscholar.org/paper/618884efc04556c0efaf82273066b58b7a25abe1) (2025) - `P1` - citations: 0 - expanded
- [AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](https://www.semanticscholar.org/paper/b2785ebbb4b014c2cf1e48e3914ddf986f14195b) (2025) - `P1` - citations: 0 - focused expansion
- [Artificial Intelligence for Quantitative Finance: A RAG-Augmented Multi-Agent Framework for Robust Equity Strategy Discovery](https://www.semanticscholar.org/paper/70103bfb66cae1c281a7d0f8dd063dffedd7715b) (2025) - `P1` - citations: 0 - focused expansion
- [Multi-Agent LLM Framework for Formulaic Alpha Generation and Selection in Quantitative Trading](https://www.semanticscholar.org/paper/d3cc99f0143c24012b376c5250c7bc88c1f011a5) (2025) - `P1` - citations: 0 - focused expansion
- [P1GPT: a multi-agent LLM workflow module for multi-modal financial information analysis](https://www.semanticscholar.org/paper/5afed2970be135f7a3fae1d8864f53c39c32ee29) (2025) - `P1` - citations: 0 - expanded
- [PyFi: Toward Pyramid-like Financial Image Understanding for VLMs via Adversarial Agents](https://www.semanticscholar.org/paper/21c8f3c47dcf6d0fbe010fe44283654791c9da79) (2025) - `P1` - citations: 0 - expanded
- [A Multi-Agent Orchestration Framework for Venture Capital Due Diligence](https://www.semanticscholar.org/paper/3e11f028e0cc4481d66006fd43d4252db5cc3ee9) (2026) - `P1` - citations: 0 - focused expansion
- [AlphaCrafter: A Full-Stack Multi-Agent Framework for Cross-Sectional Quantitative Trading](https://www.semanticscholar.org/paper/14de51b7dde5eb7474df0cadf50e6623a5b6676f) (2026) - `P1` - citations: 0 - focused expansion
- [FALLMAS: An LLM-Based Multi-Agent System for Automated Financial Analysis and Strategic Reporting](https://www.semanticscholar.org/paper/e8fc98f85d07fc06da515f21b8d4da458edf2bf6) (2026) - `P1` - citations: 0 - expanded
- [FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment](https://www.semanticscholar.org/paper/dd21f3602898d4510ecf5bf0053cf4e131887c71) (2026) - `P1` - citations: 0 - focused expansion
- [ForexAgent: Identifying Trading Strategies in Forex Markets with Large Language Models](https://www.semanticscholar.org/paper/cd2378d01fae5331b77a9ee02a19acf32c92b2f8) (2026) - `P1` - citations: 0 - expanded
- [PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage](https://www.semanticscholar.org/paper/f0673b21eb152c62ba4c7afe881718bfb6e25789) (2026) - `P1` - citations: 0 - focused expansion
- [TradeFM: A Generative Foundation Model for Trade-flow and Market Microstructure](https://www.semanticscholar.org/paper/0712ecdd042d258ef049ce838494b04d9c4728cd) (2026) - `P1` - citations: 0 - focused expansion
- [When Agents Trade: Live Multi-Market Trading Arena for LLM Agents](https://www.semanticscholar.org/paper/f1763b12c3557fcc9ce23f9dfada2003094d7c24) (2026) - `P1` - citations: 0 - focused expansion

### RAG, Search, and Knowledge Systems

- [Enhancing Financial Sentiment Analysis via Retrieval Augmented Large Language Models](https://www.semanticscholar.org/paper/1b860394dfec26d9c350889006e37fe56731f77e) (2023) - `P0` - citations: 191 - expanded
- [Financial Report Chunking for Effective Retrieval Augmented Generation](https://www.semanticscholar.org/paper/c072d217732edb066de2192ab9ad6b02aec9c7a0) (2024) - `P0` - citations: 70 - expanded
- [AlphaFin: Benchmarking Financial Analysis with Retrieval-Augmented Stock-Chain Framework](https://www.semanticscholar.org/paper/3a6bdf724da556ca534a9786b7a9f3f0adc567f7) (2024) - `P0` - citations: 68 - expanded
- [FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](https://www.semanticscholar.org/paper/d9f3ba8b48b68304b611e7d87c3d3ccf9abab32c) (2025) - `P0` - citations: 18 - expanded
- [FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation](https://www.semanticscholar.org/paper/1717ec916c1e092facaaeb22fd8fe26b172eb388) (2025) - `P0` - citations: 17 - expanded
- [FinBloom: Knowledge Grounding Large Language Model with Real-time Financial Data](https://www.semanticscholar.org/paper/fc21838d747b1b51bc8ef7022e3652d4407263d9) (2025) - `P0` - citations: 2 - expanded
- [OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain](https://www.semanticscholar.org/paper/f489b07797a877c77a9111bab448355046df2885) (2024) - `P1` - citations: 35 - expanded
- [Evaluating Retrieval-Augmented Generation Models for Financial Report Question and Answering](https://www.semanticscholar.org/paper/d65ee8821d767f6c2aeffd253ba2e0789400e819) (2024) - `P1` - citations: 31 - focused expansion
- [FinDKG: Dynamic Knowledge Graphs with Large Language Models for Detecting Global Trends in Financial Markets](https://www.semanticscholar.org/paper/330623f783928b9d552d3a29b263f002d30599c2) (2024) - `P1` - citations: 26 - focused expansion
- [RA-CFGPT: Chinese financial assistant with retrieval-augmented large language model](https://www.semanticscholar.org/paper/39c473ced3121883ec747e92175d29e44a1237c9) (2024) - `P1` - citations: 23 - expanded
- [Optimizing Retrieval Strategies for Financial Question Answering Documents in Retrieval-Augmented Generation Systems](https://www.semanticscholar.org/paper/8c321c3a2cb7737d23014879096bd709b01e44c5) (2025) - `P1` - citations: 12 - focused expansion
- [FinReflectKG: Agentic Construction and Evaluation of Financial Knowledge Graphs](https://www.semanticscholar.org/paper/4d26d0109757232d159d47d0b0a7e5b725bf9775) (2025) - `P1` - citations: 10 - focused expansion
- [MultiFinRAG: An Optimized Multimodal Retrieval-Augmented Generation Framework for Financial Question Answering](https://www.semanticscholar.org/paper/ea74733ca093249374874aa7bc316f8d1e9df599) (2025) - `P1` - citations: 9 - focused expansion
- [Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents](https://www.semanticscholar.org/paper/a42d65d63e9200ce863f9c3531d202ce6ab98c78) (2025) - `P1` - citations: 8 - focused expansion
- [Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering](https://www.semanticscholar.org/paper/8eb917ff7a8516f078f035cfce166b3a82c32cd9) (2025) - `P1` - citations: 6 - focused expansion
- [Multimodal retrieval-augmented generation for financial documents: image-centric analysis of charts and tables with large language models](https://www.semanticscholar.org/paper/7cf98ce56b91fd97d664a2ec2f9f2e24c232a378) (2025) - `P1` - citations: 6 - expanded
- [Fin-Rag A Rag System for Financial Documents](https://www.semanticscholar.org/paper/6ac2a38111550231bbd11815b3cae80230403e40) (2025) - `P1` - citations: 5 - focused expansion
- [FinKario: Event-Enhanced Automated Construction of Financial Knowledge Graph](https://www.semanticscholar.org/paper/4626559140e39e14c238296fbf365a918864a681) (2025) - `P1` - citations: 4 - focused expansion
- [Leveraging Large Language Models and Retrieval-Augmented Generation for Enhanced Multi-Asset Portfolio Construction](https://www.semanticscholar.org/paper/32e3b82aee29adbca2e826d8cebf06c3f6178038) (2025) - `P1` - citations: 2 - expanded
- [Self-explanatory and Retrieval-augmented LLMs for Financial Sentiment Analysis](https://www.semanticscholar.org/paper/73751a05de189c28abdf18adaf340d77e50259af) (2025) - `P1` - citations: 2 - expanded
- [FinVault: Benchmarking Financial Agent Safety in Execution-Grounded Environments](https://www.semanticscholar.org/paper/85fe86932cb8563be3b28fabc01fa01cc9e77b6f) (2026) - `P1` - citations: 1 - focused expansion
- FinAgent: A multimodal foundation agent for financial trading: Data-retrieval data-mining, policy-generation, and trading (2024) - `P1` - citations:  - focused expansion
- [Advancing Retrieval-Augmented Generation for Financial Question Answering](https://www.semanticscholar.org/paper/c1e75f6f1819ef2b0ebad2f9f4b290cc7c4a3b65) (2025) - `P1` - citations: 0 - focused expansion
- [NatureKG: an ontology and knowledge graph for nature finance with a Text2Cypher application](https://www.semanticscholar.org/paper/d45721e1412296bee277dfa6ac831d630da7c424) (2025) - `P1` - citations: 0 - focused expansion
- [AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution](https://www.semanticscholar.org/paper/e07b61330198b48a3fa6be2a9944f39f1f72bbef) (2026) - `P1` - citations: 0 - focused expansion
- [Decomposing Retrieval Failures in RAG for Long-Document Financial Question Answering](https://www.semanticscholar.org/paper/c16e8450de9afc9a39248ce87bb1922bb855c961) (2026) - `P1` - citations: 0 - focused expansion
- [Risk Factor Extraction in Financial Disclosures via a Knowledge Graph-Enhanced Language Model](https://www.semanticscholar.org/paper/ce7b615098491b4686d7f34df8a80e0fe3aa186c) (2026) - `P1` - citations: 0 - focused expansion
- [FinKG: A Core Financial Knowledge Graph for Financial Analysis](https://www.semanticscholar.org/paper/9eb95d26abac2f94ce353de53f33ad29d2973996) (2023) - `P2` - citations: 15 - focused expansion

### Multimodal and Multilingual Finance

- [XuanYuan 2.0: A Large Chinese Financial Chat Model with Hundreds of Billions Parameters](https://www.semanticscholar.org/paper/6783b17fe4328f48403f57009a73f784de09f645) (2023) - `P0` - citations: 160 - expanded
- [DISC-FinLLM: A Chinese Financial Large Language Model based on Multiple Experts Fine-tuning](https://www.semanticscholar.org/paper/814f0b1658c49c79bc32f3d2b89045de007871c6) (2023) - `P0` - citations: 78 - expanded
- [FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](https://www.semanticscholar.org/paper/e28e933ed53de3f0097077fa5384d22ce5e959a3) (2024) - `P0` - citations: 53 - expanded
- [Open-FinLLMs: Open Multimodal Large Language Models for Financial Applications](https://www.semanticscholar.org/paper/32b18218fa5b48b935b247c0746410b2a2c46a06) (2024) - `P0` - citations: 48 - expanded
- [CFGPT: Chinese Financial Assistant with Large Language Model](https://www.semanticscholar.org/paper/a9eb336485e148d0a3f5010693d7752facba2875) (2023) - `P0` - citations: 20 - expanded
- [Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English](https://www.semanticscholar.org/paper/16c6af5ba8989a70c84567549effd2fd7932d2ec) (2024) - `P0` - citations: 16 - expanded
- [No Language is an Island: Unifying Chinese and English in Financial Large Language Models, Instruction Data, and Benchmarks](https://www.semanticscholar.org/paper/eb419b57023d7de3284b182a5b680195c9095040) (2024) - `P0` - citations: 11 - expanded
- [BBT-Fin: Comprehensive Construction of Chinese Financial Domain Pre-trained Language Model, Corpus and Benchmark](https://arxiv.org/abs/2302.09432) (2023) - `P1` - citations: 82 - seed
- [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2308.09975) (2023) - `P1` - citations: 63 - seed
- [PreBit - A multimodal model with Twitter FinBERT embeddings for extreme price movement prediction of Bitcoin](https://www.semanticscholar.org/paper/d63a0780f80a0d87f7fa83fb2ad8eb63398a6c3b) (2022) - `P1` - citations: 52 - expanded
- [MME-Finance: A Multimodal Finance Benchmark for Expert-level Understanding and Reasoning](https://www.semanticscholar.org/paper/001f61a948d2652eae8107653ff5f80f5f1ac712) (2025) - `P1` - citations: 30 - expanded
- [Benchmarking Large Language Models on CFLUE - A Chinese Financial Language Understanding Evaluation Dataset](https://www.semanticscholar.org/paper/21c22e2a16e3e6a95cc8900d687f3f0d14bd2f64) (2024) - `P1` - citations: 27 - expanded
- [FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](https://www.semanticscholar.org/paper/086c9e9a679ccf4dd7d0cb49d6efa629b1f0109c) (2025) - `P1` - citations: 23 - expanded
- [Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance](https://www.semanticscholar.org/paper/5f520e8f20b3063307d174c8bc530317ed0d5a2a) (2025) - `P1` - citations: 18 - expanded
- [Multimodal Financial Foundation Models (MFFMs): Progress, Prospects, and Challenges](https://www.semanticscholar.org/paper/290fe5dfb5d33902c9311aaead75201747acc4d8) (2025) - `P1` - citations: 7 - expanded
- [Golden Touchstone: A Comprehensive Bilingual Benchmark for Evaluating Financial Large Language Models](https://arxiv.org/html/2411.06272v1) (2024) - `P1` - citations: 5 - seed
- [FLAME: Financial Large Language Model Evaluation System in Chinese](https://arxiv.org/abs/2501.06211) (2025) - `P2` - citations: 7 - seed

### Professional, Regulatory, and Advisory Applications

- [LLMs for Financial Advisement: A Fairness and Efficacy Study in Personal Decision Making](https://www.semanticscholar.org/paper/1dddc3cdca26cd434d48110f8d73674bb7f63c4f) (2023) - `P1` - citations: 53 - expanded
- [Can GPT models be Financial Analysts? An Evaluation of ChatGPT and GPT-4 on mock CFA Exams](https://www.semanticscholar.org/paper/ec2c330301fa8a9f4b6357d9ca630bf5bcd50996) (2023) - `P1` - citations: 28 - expanded
- [Are Generative AI Agents Effective Personalized Financial Advisors?](https://www.semanticscholar.org/paper/a84878025b6569857b6deb7eb2b9ae15eed347a4) (2025) - `P1` - citations: 27 - focused expansion
- [Agentic AI Systems Applied to tasks in Financial Services: Modeling and model risk management crews](https://www.semanticscholar.org/paper/32c3e7b6dfe4f7a0c265e56243ed71e67ec113f0) (2025) - `P1` - citations: 19 - expanded
- [Large Language Model in Financial Regulatory Interpretation](https://www.semanticscholar.org/paper/cda483cdf8c4c7a020def02f5523101558c78cca) (2024) - `P1` - citations: 12 - expanded
- [Biased echoes: Large language models reinforce investment biases and increase portfolio risks of private investors](https://www.semanticscholar.org/paper/725a338b09f9c7ec7160410ff051f395460d38b0) (2025) - `P1` - citations: 9 - focused expansion
- [A Preliminary Look at the State of the Art of Large Language Models on Chartered Financial Analyst Exams](https://aclanthology.org/2024.emnlp-industry.80/) (2024) - `P1` - citations: 8 - seed
- [Advanced Financial Reasoning at Scale: Large Language Models on Chartered Financial Analyst Level III](https://arxiv.org/abs/2507.02954) (2025) - `P1` - citations: 3 - seed
- [Can Large Language Models Tackle the Chartered Financial Analyst Exam?](https://arxiv.org/abs/2509.04468) (2025) - `P1` - citations: 2 - seed
- [DeepFinLLM: an intelligent financial advisor unleashing strategic insights with large language models](https://www.semanticscholar.org/paper/28646b0499caa84b86c2e79c2a52a32f33380161) (2025) - `P1` - citations: 2 - focused expansion
- [A Multi-Agent Approach to Investor Profiling Using Large Language Models](https://www.semanticscholar.org/paper/4274cb66827019545cf7b9dae51441f4ad523552) (2025) - `P1` - citations: 1 - focused expansion
- [ChatGPT as a Financial Advisor: A Re-Examination](https://www.semanticscholar.org/paper/b7d2ba0daaaf62229b734a350c6ca552ec336412) (2025) - `P1` - citations: 1 - focused expansion
- [Model Risk Management in Finance: The Role of Agentic Systems in Risk Mitigation](https://www.semanticscholar.org/paper/5d7e850f00c05fceaca6629468aa7da30269ed51) (2025) - `P1` - citations: 0 - focused expansion
- [Can LLMs be Good Financial Advisors?: An Initial Study in Personal Decision Making for Optimized Outcomes](https://www.semanticscholar.org/paper/d1bb97ac84e81b10f3a60d7c634c6c0c26437072) (2023) - `P2` - citations: 23 - focused expansion

## Data Files

- `data/processed/curated_papers.csv`: expanded curated list combining the original seeds and promoted additions.
- `data/processed/curated_papers_by_taxonomy.csv`: the same curated list with one mutually exclusive taxonomy category per paper plus trading/investment subtheme tags.
- `data/processed/seed_papers_enriched.csv`: seed papers with Semantic Scholar metadata, citation counts, links, and abstracts.
- `data/processed/expansion_candidates_preliminary.csv`: top 200 candidate additions discovered from citation/reference expansion.
- `data/processed/round2_expansion_candidates.csv`: top 200 candidate additions discovered from the second-round expansion.
- `data/processed/round3_expansion_candidates.csv`: top 200 candidate additions discovered from the third-round expansion.
- `data/processed/round4_expansion_candidates.csv`: top 200 candidate additions discovered from the fourth-round expansion.
- `data/processed/trading_agent_focus_finmem_seed_candidates.csv`: focused seed candidates from the FinMem trading-agent neighborhood.
- `data/processed/trading_agent_focus_expansion_candidates.csv`: candidate additions discovered from the focused FinMem trading-agent deep-dive.
- `data/processed/report_analysis_focus_seed_candidates.csv`: focused seed candidates from financial report analysis neighborhoods.
- `data/processed/report_analysis_focus_expansion_candidates.csv`: candidate additions discovered from the focused financial report analysis deep-dive.
- `data/processed/regtech_compliance_focus_anchor_candidates.csv`: focused anchors for RegTech, compliance, audit, and model-risk expansion.
- `data/processed/regtech_compliance_focus_expansion_candidates.csv`: candidate additions discovered from the focused RegTech/compliance deep-dive.
- `data/processed/specific_domain_focus_search_candidates.csv`: direct Semantic Scholar search candidates for industry/sector analysis, supply-chain finance/risk, and ETF/asset-allocation workflows.
- `data/processed/specific_domain_focus_expansion_candidates.csv`: candidate additions discovered from the focused specific-domain deep-dive.
- `data/processed/specific_domain_round2_anchor_candidates.csv`: Critic-approved anchors for the second specific-domain deep-dive.
- `data/processed/specific_domain_round2_expansion_candidates.csv`: candidate additions discovered from the second specific-domain deep-dive.
- `data/processed/specific_domain_round3_anchor_candidates.csv`: Critic-approved anchors for the third specific-domain deep-dive.
- `data/processed/specific_domain_round3_expansion_candidates.csv`: candidate additions discovered from the third specific-domain deep-dive.
- `data/processed/institutional_trading_focus_search_candidates.csv`: direct Semantic Scholar search candidates for derivatives/options, execution/microstructure, investment advisory, and private/alternative assets.
- `data/processed/institutional_trading_focus_expansion_candidates.csv`: candidate additions discovered from the focused institutional trading/investment deep-dive.
- `data/processed/institutional_trading_round2_anchor_candidates.csv`: anchors for the second institutional trading/investment deep-dive.
- `data/processed/institutional_trading_round2_expansion_candidates.csv`: candidate additions discovered from the second institutional trading/investment deep-dive.
- `data/processed/institutional_trading_round3_anchor_candidates.csv`: anchors for the third institutional trading/investment deep-dive.
- `data/processed/institutional_trading_round3_expansion_candidates.csv`: candidate additions discovered from the third institutional trading/investment deep-dive.
- `data/processed/related_work_relevance_longlist.csv`: longer relevance-filtered candidate list for manual review.
- `data/raw/semantic_scholar_related_work_edges.csv`: raw citation/reference edges from the first expansion pass.
- `data/raw/round2_related_work_edges.csv`: raw citation/reference edges from the second expansion pass.
- `data/raw/round3_related_work_edges.csv`: raw citation/reference edges from the third expansion pass.
- `data/raw/round4_related_work_edges.csv`: raw citation/reference edges from the fourth expansion pass.
- `data/raw/trading_agent_focus_edges.csv`: raw citation/reference edges from the focused FinMem trading-agent deep-dive.
- `data/raw/report_analysis_focus_edges.csv`: raw citation/reference edges from the focused financial report analysis deep-dive.
- `data/raw/regtech_compliance_focus_edges.csv`: raw citation/reference edges from the focused RegTech/compliance deep-dive.
- `data/raw/specific_domain_focus_edges.csv`: raw citation/reference edges from the focused specific-domain deep-dive.
- `data/raw/specific_domain_round2_edges.csv`: raw citation/reference edges from the second specific-domain deep-dive.
- `data/raw/specific_domain_round3_edges.csv`: raw citation/reference edges from the third specific-domain deep-dive.
- `data/raw/institutional_trading_focus_edges.csv`: raw citation/reference edges from the focused institutional trading/investment deep-dive.
- `data/raw/institutional_trading_round2_edges.csv`: raw citation/reference edges from the second institutional trading/investment deep-dive.
- `data/raw/institutional_trading_round3_edges.csv`: raw citation/reference edges from the third institutional trading/investment deep-dive.
- `data/raw/semantic_scholar_manifest.csv`: per-seed retrieval status and edge counts.
- `data/raw/round2_related_work_manifest.csv`: per-round-2-seed retrieval status and edge counts.
- `data/raw/round3_related_work_manifest.csv`: per-round-3-seed retrieval status and edge counts.
- `data/raw/round4_related_work_manifest.csv`: per-round-4-seed retrieval status and edge counts.
- `data/raw/trading_agent_focus_manifest.csv`: per-focused-seed retrieval status and edge counts.
- `data/raw/report_analysis_focus_manifest.csv`: per-report-analysis-focused-seed retrieval status and edge counts.
- `data/raw/regtech_compliance_focus_manifest.csv`: per-RegTech/compliance-focused-anchor retrieval status and edge counts.
- `data/raw/specific_domain_focus_manifest.csv`: per-specific-domain-focused-anchor retrieval status and edge counts.
- `data/raw/specific_domain_round2_manifest.csv`: per-second-specific-domain-focused-anchor retrieval status and edge counts.
- `data/raw/specific_domain_round3_manifest.csv`: per-third-specific-domain-focused-anchor retrieval status and edge counts.
- `data/raw/institutional_trading_focus_manifest.csv`: per-institutional-trading-focused-anchor retrieval status and edge counts.
- `data/raw/institutional_trading_round2_manifest.csv`: per-second-institutional-trading-focused-anchor retrieval status and edge counts.
- `data/raw/institutional_trading_round3_manifest.csv`: per-third-institutional-trading-focused-anchor retrieval status and edge counts.

## Collection Method

1. Start with the seed CSV in `data/raw/seed_papers_original.csv`.
2. Resolve seed papers through Semantic Scholar, preferring arXiv ids when available.
3. Fetch both citations and references for each resolved seed paper.
4. Promote high-confidence candidates from prior passes as deeper expansion seeds.
5. Fetch citations and references for those promoted candidates.
6. Run a focused deep-dive from the highest-cited trading-agent seed, FinMem, to capture recent LLM trading-agent work.
7. Run a focused financial report analysis deep-dive over financial statement analysis, SEC filing QA, report chunking, XBRL, and report-generation anchors.
8. Run a focused RegTech/compliance deep-dive over regulatory interpretation, model risk, audit, trustworthiness, and financial advisement anchors.
9. Run a focused specific-domain deep-dive over industry/sector analysis, supply-chain finance/risk, investment research, and ETF/asset-allocation anchors.
10. Run a Critic-approved second specific-domain deep-dive over corporate/supply-chain risk, financial knowledge graphs, sector intelligence, and finance-specific model deployment anchors.
11. Run a Critic-approved third specific-domain deep-dive over financial knowledge graphs, risk-factor extraction, event ripple effects, and nature-finance graph intelligence anchors.
12. Run a focused institutional trading/investment deep-dive over derivatives/options, execution/microstructure, investment advisory, and private/alternative assets.
13. Run a second institutional trading/investment deep-dive over options/hedging, order-level execution, prediction markets, and VC due-diligence anchors.
14. Run a third institutional trading/investment deep-dive over factor mining, market simulation infrastructure, options optimization, and VC startup-success anchors.
15. Rank candidate additions by finance/LLM relevance terms, number of source-paper connections, citation count, influential-edge hits, and recency.

See `docs/collection_plan.md` for the planned multi-round expansion workflow.

## Contributing

Open an issue or pull request with title, year, link, category, and a short note explaining why the paper belongs in the list. High-signal additions should either be finance-specific LLM work, a core financial NLP benchmark/dataset, or a highly cited foundation paper directly used by multiple finance LLM papers.

## Attribution

Paper metadata in `data/` was collected from the seed CSV and the Semantic Scholar Graph API. Abstracts and third-party metadata remain subject to their original rights and provider terms.

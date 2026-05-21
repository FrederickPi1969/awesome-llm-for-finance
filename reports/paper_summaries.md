# Paper Summaries

## Large Language Models in Finance: A Survey

- Year: 2023
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, spreadsheet reasoning, options, derivatives, fine-tuning, multi-agent systems, news, tables, accuracy, literature review, framework, hallucination, bias
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["news", "tables"], "deliverable": ["literature review", "framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "multi-agent systems"], "risk_issue": ["hallucination", "bias"], "task": ["sentiment analysis", "financial question answering", "spreadsheet reasoning"]}
- One-line summary: This survey synthesizes the state-of-the-art in applying large language models to finance, reviewing solution architectures from zero-shot to custom pretraining, proposing a cost-aware decision framework for adoption, and highlighting limitations regarding hallucination and bias.

### Detailed Summary

The paper addresses the growing intersection of large language models and financial applications, aiming to provide a practical roadmap for researchers and practitioners. It positions LLMs as transformative tools for tasks ranging from trading and risk modeling to customer service, emphasizing their ability to leverage pretraining knowledge, perform complex reasoning, and orchestrate multi-agent tool use. The survey covers the evolution from traditional AI to LLMs, detailing how zero-shot, few-shot, fine-tuning, and from-scratch pretraining approaches offer varying degrees of domain adaptation and performance. It specifically highlights the trade-offs between using proprietary APIs, open-source models, and custom-trained systems, noting that while LLMs excel in flexibility and common-sense reasoning, they require careful selection based on data availability, compute resources, and privacy constraints.

The methodology involves a comprehensive review of existing literature and case studies, categorizing LLM solutions into four levels of complexity: zero-shot, few-shot, tool-augmented/fine-tuned, and from-scratch training. The authors evaluate specific models such as FinMA, FinGPT, BloombergGPT, and Fin-T5, analyzing their performance on financial classification tasks (e.g., sentiment analysis, news headline classification) and generative tasks (e.g., question answering, summarization). Experiments cited in the survey demonstrate that fine-tuned and pre-trained finance-specific models significantly outperform general-purpose LLMs in classification tasks, with BloombergGPT achieving an average score of 62.51 compared to 54.35 for BLOOM176B. The paper also provides a decision framework that maps use-case constraints to appropriate LLM strategies, including cost estimates for development and deployment, helping practitioners navigate the balance between performance and resource investment.

Key findings indicate that while fine-tuned finance LLMs show superior performance in classification, their generative capabilities often lag behind general models like GPT-4, suggesting a need for higher-quality domain datasets. The survey identifies critical limitations, including the risk of hallucination, bias, and regulatory challenges, which necessitate safeguards like retrieval-augmented generation and content censorship. It concludes that LLMs are most valuable for tasks requiring reasoning, orchestration, or handling unstructured data where labeled examples are scarce. The paper serves as a foundational reference for understanding the current landscape, offering concrete guidance on model selection, evaluation metrics, and ethical considerations, while acknowledging that for simple, well-defined tasks with ample data, traditional machine learning may remain more cost-effective and reliable.

## A Survey of Large Language Models in Finance: FinLLMs

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, stock prediction, financial question answering, equity research, earnings analysis, instruction tuning, prompt engineering, fine-tuning, sec filings, news, earnings calls, accuracy, benchmark, dataset, literature review, hallucination, privacy, model comparison, evaluation metrics
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "news", "earnings calls"], "deliverable": ["benchmark", "dataset", "literature review"], "evaluation": ["accuracy"], "market_context": [], "method": ["instruction tuning", "prompt engineering", "fine-tuning"], "risk_issue": ["hallucination", "privacy"], "task": ["sentiment analysis", "stock prediction", "financial question answering", "equity research", "earnings analysis"]}
- One-line summary: This survey provides a comprehensive overview of Financial Large Language Models (FinLLMs), comparing their evolution from general-domain models, analyzing training techniques, evaluating performance across six benchmark tasks, and identifying challenges and future directions for the field.

### Detailed Summary

The paper addresses the gap in comprehensive reviews of Financial Large Language Models (FinLLMs) by providing a holistic survey of their development, techniques, and applications. It positions FinLLMs as an emerging field distinct from general-domain LLMs, tracing the chronological evolution from early Pre-trained Language Models (PLMs) like BERT to modern generative models. The authors aim to consolidate scattered research into a unified framework, covering the transition from discriminative financial PLMs to generative FinLLMs, and highlighting the specific challenges of applying LLMs to the financial domain, such as data privacy, hallucination, and the need for domain-specific evaluation metrics. This work serves as a foundational reference for researchers and practitioners seeking to understand the landscape of FinLLMs, their capabilities, and their limitations in real-world financial applications.

The methodology involves a systematic comparison of four financial PLMs (FinBERT-19/20/21, FLANG) and four FinLLMs (BloombergGPT, FinMA, InvestLM, FinGPT). The authors analyze five key techniques: continual pre-training, domain-specific pre-training from scratch, mixed-domain pre-training, mixed-domain LLMs with prompt engineering, and instruction fine-tuned LLMs. They evaluate these models across six standard financial NLP benchmarks: Sentiment Analysis, Text Classification, Named Entity Recognition, Question Answering, Stock Movement Prediction, and Text Summarization. The experimental design includes reviewing performance metrics (F1, Accuracy, ROUGE) and comparing FinLLMs against task-specific State-of-the-Art (SOTA) models and general-purpose models like GPT-4. Additionally, the paper introduces eight advanced financial NLP tasks and associated datasets to address gaps in current evaluation suites, such as Relation Extraction, Event Detection, and Multimodal understanding.

Key findings indicate that while general-domain LLMs like GPT-4 show impressive performance on complex tasks like Question Answering and Stock Movement Prediction, task-specific SOTA models often still outperform FinLLMs in specialized areas like Summarization. The survey highlights that mixed-domain pre-training and instruction fine-tuning are critical for enhancing FinLLM capabilities. Significant challenges identified include the scarcity of high-quality, multimodal financial datasets, the risk of hallucination, privacy concerns with proprietary data, and the lack of expert-driven evaluation metrics. The paper concludes by emphasizing the need for Retrieval Augmented Generation (RAG) to improve reliability and the importance of developing robust FinLLM frameworks for applications in robo-advisory, quantitative trading, and document understanding, while noting that current FinLLMs are not yet ready to fully replace human experts in high-stakes financial decision-making.

## A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, market simulation, options, derivatives, fine-tuning, instruction tuning, multi-agent systems, time-series modeling, sec filings, news, benchmark, dataset, taxonomy, literature review, look-ahead bias, data leakage, agent debate
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "dataset", "taxonomy", "literature review"], "evaluation": [], "market_context": [], "method": ["fine-tuning", "instruction tuning", "multi-agent systems", "time-series modeling"], "risk_issue": ["look-ahead bias", "data leakage"], "task": ["sentiment analysis", "financial question answering", "market simulation"]}
- One-line summary: This survey provides a comprehensive review of large language models in finance, categorizing applications into linguistic tasks, sentiment analysis, time series, reasoning, and agent-based modeling, while detailing specific models, datasets, benchmarks, and critical challenges like lookahead bias and data pollution.

### Detailed Summary

This paper addresses the rapid integration of large language models (LLMs) into the financial sector, aiming to bridge the gap between academic research and practical implementation. It positions LLMs as transformative tools capable of handling complex contextual understanding, transfer learning flexibility, and real-time analysis, which are crucial for modern financial decision-making. The survey distinguishes itself by offering a holistic view that covers not only technical advancements but also the broader implications for industry practices, legal concerns, and ethical deployment, filling a void left by previous surveys that focused narrowly on models or benchmarks without addressing practical challenges.

The methodology involves a systematic categorization of existing literature into five key application areas: linguistic tasks (summarization, extraction, NER), sentiment analysis, financial time series analysis, financial reasoning (planning, recommendation, decision support), and agent-based modeling. The authors analyze specific financial LLMs such as FinBERT, BloombergGPT, and Llama variants, discussing their pre-training strategies, fine-tuning techniques like instruction tuning and LoRA, and zero-shot capabilities. The paper compiles a comprehensive collection of datasets, model assets, and benchmarks, providing a resource guide for researchers. It also details experimental designs in various sub-domains, highlighting the shift from traditional deep learning to LLM-driven approaches in tasks like anomaly detection and multi-agent simulations.

Key findings indicate that LLMs significantly enhance performance in textual analysis and sentiment quantification, with specialized models outperforming general-domain counterparts in financial contexts. The survey highlights the emergence of agent-based modeling for simulating market behaviors and automated financial processes. However, it identifies critical limitations including lookahead bias in backtesting, data pollution, signal decay, and interpretability issues. The paper concludes by outlining future research directions, emphasizing the need for robust benchmarking, ethical guidelines, and solutions to legal and privacy concerns, thereby facilitating the safe and effective adoption of LLMs in the financial ecosystem.

## The New Quant: A Survey of Large Language Models in Stock Return Prediction and Investment Decision-Making

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: stock prediction, portfolio optimization, sentiment analysis, earnings analysis, equities, portfolio management, market microstructure, agentic workflow, tool use, knowledge graph, sec filings, earnings calls, news, limit order book, backtest, market impact, transaction costs, literature review, taxonomy, hallucination
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "earnings calls", "news", "limit order book"], "deliverable": ["literature review", "taxonomy"], "evaluation": ["backtest", "market impact", "transaction costs"], "market_context": ["portfolio management", "market microstructure"], "method": ["agentic workflow", "tool use", "knowledge graph"], "risk_issue": ["hallucination", "look-ahead bias", "data leakage"], "task": ["stock prediction", "portfolio optimization", "sentiment analysis", "earnings analysis"]}
- One-line summary: This survey synthesizes over fifty primary studies to propose a task-centered taxonomy for large language models in equity return prediction and trading, emphasizing the transition from feature-centric text mining to end-to-end agentic decision systems with rigorous evaluation standards.

### Detailed Summary

The paper addresses the emerging paradigm of the "new quant," where large language models transform unstructured financial information into evidence-grounded signals and executable investment decisions. It positions this shift as a move from traditional feature-centric text mining to end-to-end decision systems that read heterogeneous disclosures, generate auditable hypotheses, and interact with external tools. The survey consolidates insights from domain-specific surveys and more than fifty primary studies published between 2023 and 2025, focusing specifically on equity return prediction and trading with portfolio construction. It aims to provide a structured understanding of how upstream natural language processing components feed tradable signals, addressing the gap between academic research and production-ready quantitative investing.

The authors propose a comprehensive task-centered taxonomy that categorizes LLM capabilities into sentiment and opinion extraction, information extraction and knowledge graphs, numerical question answering, summarization, multimodal analysis, and agentic workflows. The methodology involves synthesizing empirical evidence on predictability, reviewing design patterns that improve faithfulness such as retrieval-augmented generation and tool-verified numerics, and analyzing how these signals integrate into portfolio construction under exposure, turnover, and capacity controls. The survey assesses existing benchmarks and datasets, highlighting the need for time-safe evaluation protocols that report costs, latency, and capacity, while also examining challenges like temporal leakage, hallucination, and deployment economics.

Key findings indicate that language-derived views on news, filings, and earnings calls can predict returns, but evaluation practices often lack trading standards regarding leakage control and market microstructure realism. The paper highlights that retrieval-first prompting and tool-verified numerics significantly improve faithfulness and reduce hallucination risks. It outlines specific use cases for agentic systems that coordinate tools for research, backtesting, and execution, emphasizing the separation of signal generation from portfolio allocation. Limitations discussed include temporal leakage in pretrained models, data coverage gaps, and the need for interpretability and governance. The survey concludes with recommendations for standardizing evaluation, building auditable pipelines, and advancing multilingual research to ensure robust, risk-controlled performance in practice.

## Large Language Model Agent in Financial Trading: A Survey

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: survey
- Summary coverage: full_extracted_text
- Tags: alpha mining, strategy generation, factor modeling, spreadsheet reasoning, equities, crypto, us equities, china market, agent debate, backtesting, reinforcement learning, 10-k filings, news, social media, ohlc data, tables, backtest, sharpe ratio, drawdown, taxonomy
- Tag facets: {"asset_class": ["equities", "crypto"], "data_source": ["10-k filings", "news", "social media", "ohlc data", "tables"], "deliverable": ["taxonomy", "literature review"], "evaluation": ["backtest", "sharpe ratio", "drawdown"], "market_context": ["us equities", "china market"], "method": ["agent debate", "backtesting", "reinforcement learning"], "risk_issue": ["overfitting"], "task": ["alpha mining", "strategy generation", "factor modeling", "spreadsheet reasoning"]}
- One-line summary: This survey systematically reviews 27 studies on LLM-powered trading agents, categorizing them into 'LLM as Trader' and 'LLM as Alpha Miner' architectures, analyzing their data inputs, evaluation metrics, and identifying key limitations such as short backtesting periods and lack of cost considerations.

### Detailed Summary

This paper addresses the emerging research area of using Large Language Models as autonomous agents in financial trading. It aims to map the landscape of LLM trading agents by answering three core questions: common architectures, data inputs, and current performance/limitations. The authors conducted a systematic review of 27 relevant papers, identifying this as the first comprehensive survey of LLM agents specifically for financial trading, distinguishing it from general LLM finance surveys by focusing on the agent paradigm and decision-making loops.

The authors categorize agent architectures into two main types: 'LLM as a Trader,' which directly generates buy/sell/hold signals, and 'LLM as an Alpha Miner,' which uses LLMs to generate alpha factors for downstream quantitative systems. Within the trader category, they further classify approaches into news-driven, reflection-driven (using memory and reflection modules), debate-driven (multi-agent debate), and reinforcement learning-driven methods. Data inputs are analyzed across four types: numerical (prices, volumes), textual (fundamental reports, news, social media), visual (charts), and simulated environments. Experiments primarily involve backtesting on US and Chinese stock markets, using metrics like cumulative return, Sharpe ratio, and maximum drawdown, often comparing against rule-based or deep learning baselines.

Key findings indicate that LLM agents generally outperform baselines in backtesting, achieving annualized returns of 15-30% over strong baselines. However, significant limitations exist: most studies rely on closed-source models, use short backtesting periods (median 1.3 years), ignore trading costs, and lack rigorous ablation studies on reasoning processes. The survey highlights that while LLMs excel at processing unstructured text, they struggle with numerical reasoning and high-frequency trading due to latency. Future directions include integrating multimodal data, exploring open-source models, and developing more robust evaluation frameworks that account for market frictions and ethical risks.

## From Deep Learning to Large Language Models: A Survey of Artificial Intelligence in Quantitative Investment

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: alpha mining, portfolio optimization, sentiment analysis, stock prediction, factor modeling, equities, portfolio management, agentic workflow, financial statements, news, tables, accuracy, hit ratio, literature review, taxonomy, hallucination, overfitting, regulatory compliance, quantitative investment, alpha strategy pipeline
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "news", "tables"], "deliverable": ["literature review", "taxonomy"], "evaluation": ["accuracy", "hit ratio"], "market_context": ["portfolio management"], "method": ["agentic workflow"], "risk_issue": ["hallucination", "overfitting", "regulatory compliance"], "task": ["alpha mining", "portfolio optimization", "sentiment analysis", "stock prediction", "factor modeling"]}
- One-line summary: This survey systematically reviews the evolution of quantitative investment from traditional statistical models to deep learning and large language models, focusing on how AI enhances the alpha strategy pipeline across data processing, prediction, and execution.

### Detailed Summary

The paper addresses the need for a unified framework to understand the integration of artificial intelligence into quantitative investment, specifically alpha strategies. It positions the field as evolving through three stages: traditional human-crafted features and statistical models, the rise of deep learning for scalable pattern recognition, and the current emergence of large language models (LLMs) that enable autonomous agents to process unstructured data and support self-iterative workflows. The authors aim to bridge the gap between isolated technical studies and a holistic view of the quant pipeline, highlighting practical challenges and future directions for AI-driven alpha generation.

The methodology involves a comprehensive literature review structured around the standard alpha investment pipeline: data processing, model prediction, portfolio optimization, and order execution. The authors categorize financial data into numerical, relational, alternative, and simulation types, analyzing how deep learning techniques like graph neural networks and transformers handle these modalities. For LLMs, the survey examines their dual roles as predictors for financial time series and as agents for tasks such as sentiment analysis, factor mining, and automated trading. The paper synthesizes existing works to compare the strengths and weaknesses of each technological stage, emphasizing the shift from supervised learning to agentic, reasoning-based systems.

Key findings indicate that while deep learning has significantly improved predictive accuracy by capturing complex non-linear patterns, it often suffers from interpretability issues and overfitting risks. LLMs offer new capabilities in handling multimodal data and generating alpha signals through natural language reasoning, but their practical deployment is still nascent due to latency, hallucination risks, and the need for robust evaluation benchmarks. The survey concludes that the future of quant investment lies in hybrid systems that combine the precision of deep learning with the reasoning and automation capabilities of LLMs, though significant challenges in data quality, regulatory compliance, and real-world validation remain.

## BloombergGPT: A Large Language Model for Finance

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, spreadsheet reasoning, equities, institutional investing, fine-tuning, domain adaptation, sec filings, news, tables, accuracy, model, dataset, data leakage, foundation model, proprietary data, tokenization
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "tables"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["fine-tuning", "domain adaptation"], "risk_issue": ["data leakage"], "task": ["sentiment analysis", "financial question answering", "spreadsheet reasoning"]}
- One-line summary: BloombergGPT is a 50 billion parameter language model trained on a mixed corpus of 363 billion financial tokens and 345 billion general tokens, demonstrating superior performance on financial benchmarks while maintaining competitive general NLP capabilities.

### Detailed Summary

The paper addresses the lack of large language models specialized for the financial domain, noting that while general LLMs exist, they often underperform on complex financial tasks due to domain-specific terminology and data structures. The authors position BloombergGPT as a solution that bridges the gap between general-purpose models and narrow domain models by adopting a mixed-training approach. This strategy aims to achieve best-in-class results on financial benchmarks without sacrificing performance on general language understanding tasks, thereby providing a versatile tool for financial technology applications ranging from sentiment analysis to question answering.

The core methodology involves training a 50 billion parameter decoder-only transformer model based on the BLOOM architecture. The training dataset, termed FinPile, comprises 363 billion tokens of curated financial data—including web content, news, company filings (10-K/10-Q), press releases, and proprietary Bloomberg data—augmented with 345 billion tokens from public datasets like The Pile, C4, and Wikipedia. The model utilizes a custom Unigram tokenizer with a 131,072 vocabulary size to improve tokenization efficiency for financial text. Training was conducted on 64 A100 GPUs using AdamW optimization, cosine decay learning rates, and activation checkpointing, following Chinchilla scaling laws to determine the optimal parameter-to-token ratio given the compute budget.

Evaluation results indicate that BloombergGPT significantly outperforms existing models on open financial benchmarks and internal sentiment analysis tasks, validating the efficacy of the mixed-data training strategy. The model also maintains competitive performance on general LLM benchmarks such as MMLU and BIG-bench Hard. The paper provides extensive details on the training process, including troubleshooting pathological gradient norms and learning rate adjustments. However, the model is not publicly released due to the proprietary nature of the financial data, and the authors highlight limitations regarding the potential for data leakage in temporal evaluations and the computational costs associated with training such large models.

## FinGPT: Open-Source Financial Large Language Models

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, investment advisory, equities, portfolio management, fine-tuning, reinforcement learning, retrieval, news, social media, sec filings, accuracy, ablation study, benchmark, dataset, framework, open source, data leakage, parameter-efficient fine-tuning, market-driven alignment, financial nlp library
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media", "sec filings"], "deliverable": ["benchmark", "dataset", "framework", "open source"], "evaluation": ["accuracy", "ablation study"], "market_context": ["portfolio management"], "method": ["fine-tuning", "reinforcement learning", "retrieval"], "risk_issue": ["data leakage"], "task": ["sentiment analysis", "investment advisory"]}
- One-line summary: FinGPT introduces an open-source, data-centric framework for financial LLMs that utilizes lightweight LoRA fine-tuning and market-driven reinforcement learning to achieve superior financial sentiment analysis compared to proprietary and baseline models.

### Detailed Summary

The paper addresses the critical need for accessible, transparent, and cost-effective financial large language models (FinLLMs) by introducing FinGPT, an open-source framework. It highlights the unique challenges of the financial domain, including high temporal sensitivity, constant dynamism, and low signal-to-noise ratios, which make proprietary models like BloombergGPT inaccessible to many researchers. FinGPT democratizes access by providing a full-stack, data-centric pipeline that emphasizes rigorous data curation, real-time processing, and lightweight adaptation techniques, aiming to foster innovation within the open-source AI4Finance community.

The methodology centers on a five-layer architecture: data source, data engineering, LLMs, tasks, and applications. The data engineering layer implements a real-time pipeline for cleaning, tokenization, and embedding financial text from news, social media, and filings. For model adaptation, FinGPT employs Low-Rank Adaptation (LoRA) to fine-tune base models like Llama-3.1-8B with minimal trainable parameters, significantly reducing costs. It further introduces Reinforcement Learning on Stock Prices (RLSP), using short-term stock price movements as objective feedback signals to align model outputs with actual market reactions, replacing traditional human feedback with market-driven rewards.

Experiments on financial sentiment analysis demonstrate that FinGPT outperforms baselines such as FinBERT, ChatGPT, and zero-shot Llama-3. The model achieves an accuracy of 82.1% and a Macro-F1 of 80.9%, significantly higher than FinBERT's 71.2% accuracy. Ablation studies confirm that LoRA provides substantial gains over base models, while RLSP further enhances market alignment. The paper showcases applications including robo-advising, quantitative trading signals, and risk management, while noting limitations in real-time deployment latency and the need for continuous data pipeline maintenance to handle market dynamism.

## PIXIU: A Large Language Model, Instruction Data and Evaluation Benchmark for Finance

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, financial question answering, stock prediction, equities, fine-tuning, instruction tuning, news, financial statements, accuracy, backtest, benchmark, dataset, model, open source, hallucination, instruction tuning dataset, domain adaptation, quantitative reasoning, stock movement prediction
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "financial statements"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "financial question answering", "stock prediction"]}
- One-line summary: PIXIU introduces FinMA, an open-source financial LLM fine-tuned on the FIT dataset, and FLARE, a benchmark evaluating financial NLP and stock prediction, showing FinMA outperforms general LLMs on NLP tasks but struggles with quantitative reasoning.

### Detailed Summary

The paper addresses the lack of open-source, instruction-tuned large language models for finance, noting that existing models like BloombergGPT are proprietary or lack instruction-following capabilities. The authors aim to democratize financial AI by creating a comprehensive framework that includes a domain-specific LLM, a large-scale instruction tuning dataset, and a holistic evaluation benchmark covering both natural language understanding and financial prediction tasks. This positioning fills a critical gap in the open-source ecosystem, enabling reproducible research and development in financial AI without relying on closed proprietary models.

The core contribution is the PIXIU framework, which comprises three main components: the FIT dataset, the FinMA model, and the FLARE benchmark. FIT is a multi-task, multi-modal instruction tuning dataset containing 136,609 samples across five tasks: financial sentiment analysis, news headline classification, named entity recognition, financial question answering, and stock movement prediction. The authors fine-tuned LLaMA-7B and LLaMA-30B to create FinMA. FLARE serves as the evaluation benchmark, integrating six NLP datasets and three stock movement prediction datasets. Experiments compared FinMA against proprietary models like GPT-4, ChatGPT, and BloombergGPT, using metrics such as F1, accuracy, and Matthews correlation coefficient across zero-shot and few-shot settings.

Results indicate that FinMA significantly outperforms general LLMs and BloombergGPT on most financial NLP tasks, such as sentiment analysis and headline classification, demonstrating the value of domain-specific instruction tuning. However, FinMA underperforms on financial question answering tasks requiring complex numerical reasoning, a limitation attributed to the LLaMA backbone's lack of mathematical pre-training. Additionally, all models, including FinMA, showed limited performance on stock movement prediction, highlighting the difficulty of this task. The study concludes that while domain adaptation improves NLP performance, challenges remain in quantitative reasoning and prediction, suggesting future work should focus on enhancing these capabilities through specialized training data and model architectures.

## FinBen: A Holistic Financial Benchmark for Large Language Models

- Year: 2024
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: stock prediction, forecasting, sentiment analysis, risk extraction, financial question answering, spreadsheet reasoning, equities, us equities, agent debate, backtesting, sec filings, news, tables, sharpe ratio, accuracy, backtest, benchmark, dataset, open source, overfitting
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "tables"], "deliverable": ["benchmark", "dataset", "open source"], "evaluation": ["sharpe ratio", "accuracy", "backtest"], "market_context": ["us equities"], "method": ["agent debate", "backtesting"], "risk_issue": ["overfitting", "bias"], "task": ["stock prediction", "forecasting", "sentiment analysis", "risk extraction", "financial question answering", "spreadsheet reasoning"]}
- One-line summary: FinBen is a comprehensive open-source benchmark evaluating 15 LLMs across 24 financial tasks, revealing that while models excel at information extraction, they struggle with complex reasoning, forecasting, and trading, with GPT-4 leading in IE and trading while Gemini leads in generation.

### Detailed Summary

The paper addresses the lack of comprehensive evaluation benchmarks for Large Language Models (LLMs) in the financial domain, where existing tools are limited to narrow NLP tasks. The authors introduce FinBen, a holistic benchmark comprising 36 datasets across 24 tasks, categorized into seven aspects: information extraction, textual analysis, question answering, text generation, risk management, forecasting, and decision-making. This framework aims to provide a robust assessment of LLM capabilities in diverse and complex financial scenarios, including the first evaluation of stock trading and agent-based RAG strategies.

The methodology involves evaluating 15 representative general and financial LLMs, such as GPT-4, Gemini, and LLaMA variants, using zero-shot and few-shot settings. The benchmark includes novel datasets like FinTrade for stock trading, EDTSum for news summarization, and Regulations for legal QA. Experiments were conducted on NVIDIA A100 GPUs, with results measured using standard metrics like F1, Accuracy, ROUGE, and financial performance indicators such as Sharpe Ratio and Cumulative Return. The study also hosted a shared task at IJCAI-2024 to test community-developed solutions.

Key findings indicate that LLMs perform well in information extraction and textual analysis but fail in advanced reasoning tasks like forecasting and complex text generation. GPT-4 excels in IE and stock trading, achieving a Sharpe Ratio over 1, while Gemini outperforms others in text generation and forecasting. Instruction-tuned financial LLMs show improvements in specific tasks but lack generalization. The paper highlights limitations in dataset size, model scale, and generalizability to non-US markets, noting that LLMs still lag behind traditional methods in forecasting and face challenges with imbalanced risk management data.

## FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models

- Year: 2023
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, financial question answering, chain of thought, prompt engineering, accuracy, benchmark, dataset, leaderboard, hallucination, chinese financial domain, financial security, financial agent, human baseline, expert evaluation
- Tag facets: {"asset_class": [], "data_source": [], "deliverable": ["benchmark", "dataset", "leaderboard"], "evaluation": ["accuracy"], "market_context": [], "method": ["chain of thought", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["benchmarking", "financial question answering"]}
- One-line summary: FinEval is a comprehensive Chinese financial benchmark evaluating 19 LLMs across academic knowledge, industry tasks, security, and agent capabilities, revealing that while top models surpass ordinary humans, they still lag behind experts, with general models often outperforming domain-specific ones.

### Detailed Summary

The paper addresses the lack of comprehensive evaluation for Large Language Models in the Chinese financial domain, specifically highlighting gaps in security and complex agent tasks. It introduces FinEval, a benchmark comprising 8,351 questions across four categories: Financial Academic Knowledge (4,661 questions across 34 subjects), Financial Industry Knowledge (1,434 questions on practical scenarios like investment research), Financial Security Knowledge (1,640 questions on application and network security), and Financial Agent (616 questions on tool usage and reasoning). The dataset is curated by finance and security experts to ensure high quality and relevance to real-world Chinese financial contexts.

The authors evaluate 19 LLMs, including closed-source models like Claude 3.5-Sonnet and GPT-4o, open-source models like Qwen2.5-72B, and financial-specific models like XuanYuan3-70B. Experiments utilize zero-shot, five-shot, and Chain-of-Thought prompting. Evaluation metrics include accuracy for multiple-choice questions, Rouge-L for industry knowledge, and GPT-4o as a judge for open-ended agent tasks. The study also includes a human baseline comparison with ordinary individuals and financial experts to contextualize model performance.

Results show Claude 3.5-Sonnet achieves the highest weighted average score of 72.9, followed by GPT-4o at 71.9. Notably, general open-source models like Qwen2.5-72B often outperform specialized financial models, suggesting superior generalization. While LLMs significantly outperform ordinary individuals (average score 30.1), they still trail financial experts (average score 85.9). Error analysis reveals that open-source models struggle more with logical reasoning and context, while closed-source models are prone to ambiguity handling issues. The benchmark highlights that despite progress, LLMs require further improvement in complex financial reasoning and security robustness.

## Golden Touchstone: A Comprehensive Bilingual Benchmark for Evaluating Financial Large Language Models

- Year: 2024
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, financial question answering, benchmarking, equities, us equities, china market, instruction tuning, fine-tuning, retrieval, news, sec filings, accuracy, backtest, benchmark, dataset, model, open source, look-ahead bias, bilingual
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "sec filings"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy", "backtest"], "market_context": ["us equities", "china market"], "method": ["instruction tuning", "fine-tuning", "retrieval"], "risk_issue": ["look-ahead bias"], "task": ["sentiment analysis", "stock prediction", "financial question answering", "benchmarking"]}
- One-line summary: Golden Touchstone introduces a comprehensive bilingual benchmark for financial LLMs across eight NLP tasks, revealing that while models excel at sentiment analysis, they struggle with complex reasoning and stock prediction, and proposes Touchstone-GPT as a competitive baseline.

### Detailed Summary

The paper addresses the lack of standardized, high-quality evaluation tools for financial large language models, noting that existing benchmarks suffer from limited language coverage, inconsistent data quality, and inadequate task diversity. To resolve this, the authors introduce Golden Touchstone, a bilingual benchmark encompassing eight core financial NLP tasks in both English and Chinese. These tasks span Natural Language Understanding (sentiment analysis, classification, entity/relation extraction, multiple-choice knowledge) and Natural Language Generation (summarization, question answering, stock movement prediction). The benchmark integrates 22 curated datasets, ensuring consistent evaluation metrics and handling of unknown labels to prevent bias, thereby providing a robust framework for assessing model capabilities in real-world financial contexts.

The experimental evaluation compares state-of-the-art proprietary models (GPT-4o) and open-source general models (Llama-3, Qwen-3) against specialized financial LLMs (FinGPT, FinMA, CFGPT, DISC-FinLLM). Additionally, the authors train and release Touchstone-GPT, a model based on Qwen-2.5, utilizing two-stage training: continual pre-training on 100 billion tokens of financial text and instruction tuning on 300,000 high-quality instruction-response pairs. The evaluation employs greedy decoding for reproducibility and assesses performance using task-specific metrics such as F1, accuracy, ROUGE, and BLEU across both English and Chinese datasets, highlighting the impact of inference templates on model performance.

Results indicate that while sentiment analysis and simple classification are well-handled by most models, complex tasks like relation extraction, summarization, and question answering show significant performance gaps, particularly in Chinese. Stock movement prediction remains practically unusable for all models, as news sentiment alone is insufficient for accurate forecasting without quantitative data. Touchstone-GPT demonstrates strong competitive performance, often outperforming specialized models like FinGPT and FinMA, but still lags behind GPT-4o in complex reasoning. The study concludes that future financial LLMs require better multimodal integration and retrieval-augmented generation to handle numerical and temporal data effectively.

## FLaME: A Holistic Benchmark for Financial Language Models

- Year: 2025
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, spreadsheet reasoning, sec filings, news, tables, accuracy, backtest, benchmark, dataset, leaderboard, hallucination, data leakage, reasoning evaluation, numeric reasoning, causal analysis, cost-performance trade-off, open-weight models
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "news", "tables"], "deliverable": ["benchmark", "dataset", "leaderboard"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": [], "risk_issue": ["hallucination", "data leakage"], "task": ["sentiment analysis", "financial question answering", "spreadsheet reasoning"]}
- One-line summary: FLaME introduces a holistic benchmarking suite for financial NLP, evaluating 23 foundation and reasoning-reinforced LMs across 20 datasets to reveal that no single model dominates all tasks, with significant performance gaps in numeric reasoning and causal analysis, while highlighting cost-performance trade-offs for open-weight models.

### Detailed Summary

This paper addresses the lack of rigorous, standardized evaluation for Large Language Models (LLMs) in specialized financial domains. Existing benchmarks are fragmented, lacking holistic criteria, which has led to an underestimation of LM capabilities in Finance NLP (FinNLP). The authors argue that without comprehensive evaluation, deploying LMs in financial systems risks severe errors due to hallucinations or flawed reasoning. FLaME (Financial Language Model Evaluation) is proposed as the first holistic benchmarking suite designed to provide standardized, multi-metric, and reproducible assessments of LM performance on core FinNLP tasks, explicitly acknowledging the incompleteness of current evaluation methods.

The methodology involves a unified inference hub supporting proprietary and open-weight models, evaluated across 20 curated datasets covering six core NLP tasks: text classification, information retrieval, sentiment analysis, question answering, text summarization, and causal analysis. The study assesses 23 models, including foundation LMs (e.g., Llama 3, Qwen) and reasoning-reinforced models (e.g., DeepSeek R1, o1-mini). Evaluation metrics include accuracy, F1, and BERTScore, with a focus on deterministic decoding for consistency. The authors employ a scenario-based taxonomy categorizing data by task, domain, and language to map the landscape of available FinNLP resources and identify gaps in data coverage, particularly for non-English languages and complex causal tasks.

Results indicate that no single model outperforms all others across every task; DeepSeek R1 leads in multi-step QA, while Claude 3.5 Sonnet excels in sentiment and retrieval. Numeric reasoning and causal detection remain significant bottlenecks, with low F1 scores indicating struggles with precise numeric mapping and cross-sentence references. Summarization tasks show higher tractability. The study highlights a strong cost-performance trade-off, where mid-scale open-weight models like DeepSeek-V3 and Llama 3.1 70B offer efficient alternatives to expensive proprietary models. Limitations include the exclusion of multi-modal models and a current focus on English, with calls for future work on domain-adaptive training and expanded multilingual coverage.

## BBT-Fin: Comprehensive Construction of Chinese Financial Domain Pre-trained Language Model, Corpus and Benchmark

- Year: 2023
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, financial question answering, china market, knowledge graph, fine-tuning, instruction tuning, news, social media, accuracy, benchmark, dataset, model, open source, bias, chinese nlp, pre-training, t5 architecture, knowledge extraction
- Tag facets: {"asset_class": [], "data_source": ["news", "social media"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["knowledge graph", "fine-tuning", "instruction tuning"], "risk_issue": ["bias"], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: The paper introduces BBT-FinT5, a large-scale Chinese financial pre-trained language model enhanced with knowledge extraction, supported by a 300GB corpus and a comprehensive benchmark, demonstrating superior performance over existing domain-specific models on financial NLP tasks.

### Detailed Summary

This paper addresses the lack of high-quality resources for Chinese financial natural language processing by introducing BBT-FinT5, a domain-specific pre-trained language model based on the T5 architecture. The authors argue that existing Chinese financial models are limited by smaller parameter sizes and lack of knowledge enhancement, particularly for entity understanding. To solve this, they propose a knowledge-enhanced pre-training method called Triple Masking (KETM), which integrates knowledge graph triples with text spans to improve entity memorization. The work positions itself as a comprehensive infrastructure contribution, aiming to standardize evaluation and improve baseline performance for downstream financial NLP applications in the Chinese market.

The methodology involves constructing BBT-FinCorpus, a 300GB dataset comprising corporate announcements, research reports, financial news, and social media posts from major Chinese platforms. The BBT-FinT5 model, available in base (220M) and large (1B) parameter versions, is pre-trained using DeepSpeed optimization and BFLOAT16 precision. Evaluation is conducted on BBT-CFLEB, a new benchmark with six tasks including news classification, relation extraction, sentiment analysis, and question answering. Experiments compare BBT-FinT5 against general models (T5, GPT-2) and existing financial models (FinBERT, Mengzi-BERT), using metrics like F1-score and ROUGE across understanding and generation leaderboards.

Results show that BBT-FinT5 significantly outperforms baselines, with the large version achieving the highest average scores on the CFLEB benchmark. The KETM method specifically boosts performance on relation extraction and summarization tasks, confirming the value of explicit knowledge integration. The released corpus and benchmark provide essential tools for the Chinese financial NLP community. However, the study is limited to Chinese text and does not address multimodal or multilingual aspects, nor does it evaluate real-time trading performance or market impact, focusing instead on static text understanding and generation capabilities.

## Large Language Model Evaluation on Financial Benchmarks

- Year: 2024
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: benchmarking, equity research, equities, china market, prompt engineering, sec filings, accuracy, benchmark, dataset, regulatory compliance, financial question answering, document generation
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["prompt engineering"], "risk_issue": ["regulatory compliance"], "task": ["benchmarking", "equity research"]}
- One-line summary: The paper introduces FLAME, a comprehensive Chinese financial LLM evaluation system comprising certification and scenario benchmarks, demonstrating that Baichuan4-Finance outperforms other models in professional knowledge and practical application tasks.

### Detailed Summary

The paper addresses the lack of comprehensive, professional evaluation standards for Large Language Models in the financial domain, particularly within the Chinese context. Existing benchmarks often rely on NLP metrics like text similarity rather than assessing practical financial capabilities. To fill this gap, the authors propose FLAME, a dual-benchmark system designed to rigorously test both theoretical knowledge and real-world application skills of financial LLMs. The system is developed by the School of Finance at Renmin University of China to ensure academic and professional authority, covering everything from basic terminology to complex regulatory compliance and risk control scenarios.

FLAME consists of two core components: FLAME-Cer and FLAME-Sce. FLAME-Cer contains approximately 16,000 manually reviewed multiple-choice questions covering 14 authoritative financial certifications, including CPA, CFA, and FRM, with accuracy as the primary metric. FLAME-Sce features nearly 100 tertiary tasks across 10 primary business scenarios, such as intelligent customer service, document generation, and risk control, evaluated using a multi-dimensional manual scoring system that weighs accuracy, compliance, and practicality. The authors evaluate six representative LLMs, including GPT-4o, Qwen2.5, and Baichuan4-Finance, using zero-shot settings to compare their performance across these diverse and rigorous benchmarks.

The results indicate that Baichuan4-Finance leads in most tasks, achieving an average accuracy of 93.62% on FLAME-Cer and a usability rate of 84.15% on FLAME-Sce. While models generally perform well in financial knowledge theory and data computation, they struggle with complex tasks like financial analysis and document generation. The study highlights that specialized financial models often outperform general-purpose LLMs in domain-specific contexts, though challenges remain in handling nuanced regulatory compliance and deep analytical reasoning. The paper concludes that FLAME provides a vital tool for advancing the development and deployment of reliable financial LLMs in China.

## FLAME: Financial Large Language Model Evaluation System in Chinese

- Year: 2025
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: benchmarking, financial question answering, spreadsheet reasoning, china market, sec filings, tables, accuracy, benchmark, dataset, regulatory compliance, multilingual, manual evaluation, professional certification, chinese financial context
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": [], "risk_issue": ["regulatory compliance"], "task": ["benchmarking", "financial question answering", "spreadsheet reasoning"]}
- One-line summary: FLAME introduces a comprehensive Chinese financial LLM evaluation system comprising certification and scenario benchmarks, revealing that Baichuan4-Finance outperforms other models in professional knowledge and practical application tasks.

### Detailed Summary

The paper addresses the lack of professional, Chinese-language benchmarks for evaluating financial Large Language Models (LLMs), arguing that existing NLP-centric benchmarks fail to capture domain-specific expertise and practical applicability. The authors propose FLAME, a holistic evaluation system designed to assess both theoretical knowledge and real-world business capabilities within the Chinese financial context, ensuring alignment with regulatory standards and industry needs. This system aims to provide a reliable standard for developing and selecting financial LLMs that are both academically rigorous and commercially viable.

FLAME consists of two core benchmarks: FLAME-Cer and FLAME-Sce. FLAME-Cer contains approximately 16,000 manually reviewed multiple-choice questions covering 14 authoritative financial certifications, including CPA, CFA, and FRM, graded by professional depth. FLAME-Sce features nearly 100 tertiary tasks across 10 primary business scenarios, such as risk control, document generation, and customer service, evaluated via a weighted multi-dimensional manual scoring system covering accuracy, compliance, and practicality. The authors evaluate six representative LLMs, including GPT-4o, Qwen2.5, and Baichuan4-Finance, using zero-shot settings to compare their performance across these diverse and complex financial tasks.

Results indicate that Baichuan4-Finance leads with an average accuracy of 93.62% on certifications and 84.15% usability on scenarios, significantly outperforming generalist models like GPT-4o and other open-source models. While models excel in data processing and knowledge retrieval, they struggle with complex financial analysis and document generation, highlighting current limitations in deep reasoning. The study underscores the importance of domain-specific fine-tuning for Chinese financial applications and provides a valuable benchmark for future model development, though it notes that manual evaluation remains resource-intensive and potentially subjective.

## FinQA: A Dataset of Numerical Reasoning over Financial Data

- Year: 2021
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, earnings analysis, equities, us equities, earnings season, retrieval, semantic parsing, earnings calls, tables, accuracy, benchmark, dataset, hallucination, numerical reasoning, domain specific language, executable programs
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities", "earnings season"], "method": ["retrieval", "semantic parsing"], "risk_issue": ["hallucination"], "task": ["financial question answering", "earnings analysis"]}
- One-line summary: The paper introduces FinQA, a large-scale dataset of 8,281 expert-annotated financial question-answer pairs with executable reasoning programs over S&P 500 earnings reports, demonstrating that current LLMs significantly lag behind human experts in complex multi-step numerical reasoning.

### Detailed Summary

Financial analysis requires automating the interpretation of heterogeneous data sources, yet existing NLP benchmarks lack the complexity of real-world financial reasoning. The authors address this gap by introducing FinQA, a dataset designed to test deep numerical reasoning over financial documents. Unlike general-domain QA tasks that involve simple calculations, FinQA questions require integrating information from both unstructured text and structured tables within S&P 500 earnings reports. The dataset is constructed by financial experts to ensure domain relevance, focusing on questions that demand multi-step arithmetic operations and table aggregations to derive answers, thereby establishing a rigorous benchmark for explainable financial AI.

The dataset comprises 8,281 examples derived from 2,789 pages of earnings reports, each annotated with gold reasoning programs defined by a Domain Specific Language (DSL) containing mathematical and table operations. To evaluate performance, the authors propose FinQANet, a retriever-generator framework that first retrieves supporting facts using BERT and then generates executable programs using pre-trained models like RoBERTa and FinBERT. Experiments compare these baselines against human experts and non-expert crowd workers, measuring both execution accuracy and program accuracy to assess the correctness of the reasoning path, not just the final answer.

Results show that the best model, FinQANet with RoBERTa-large, achieves 61.24% execution accuracy, significantly outperforming non-expert crowds (50.68%) but falling far short of human experts (91.16%). The model struggles most with questions requiring both text and table integration, multi-step reasoning, and unit conversions involving constants. Error analysis reveals that failures often stem from a lack of financial domain knowledge and difficulties in aligning numerical values across heterogeneous formats. These findings highlight the substantial gap between current LLM capabilities and the robust, explainable reasoning required for professional financial analysis.

## TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance

- Year: 2021
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: financial question answering, benchmarking, symbolic regression, retrieval, fine-tuning, sec filings, tables, accuracy, benchmark, dataset, model, hallucination, numerical reasoning, hybrid data, table understanding
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables"], "deliverable": ["benchmark", "dataset", "model"], "evaluation": ["accuracy"], "market_context": [], "method": ["symbolic regression", "retrieval", "fine-tuning"], "risk_issue": ["hallucination"], "task": ["financial question answering", "benchmarking"]}
- One-line summary: The paper introduces TAT-QA, a benchmark for financial question answering over hybrid tabular and textual data, and proposes the TAGOP model which uses sequence tagging and symbolic aggregation operators to achieve 58.0% F1, significantly outperforming baselines but lagging behind human experts.

### Detailed Summary

The paper addresses the challenge of Question Answering (QA) over hybrid data, specifically the combination of tabular and textual content found in real-world financial reports. Existing QA systems typically focus on unstructured text or structured knowledge bases, neglecting the complex interdependencies and numerical reasoning required when tables and accompanying paragraphs are semantically linked. The authors argue that this hybrid form is pervasive in finance and requires models to extract information from both modalities and perform arithmetic operations to derive answers.

To tackle this, the authors construct TAT-QA, a large-scale dataset containing 16,552 questions derived from 2,757 hybrid contexts extracted from 182 real financial reports. The dataset includes questions requiring various numerical reasoning types such as addition, subtraction, division, and counting, with annotated derivations and scales. They propose TAGOP, a model that uses a RoBERTa-based encoder for sequence tagging to extract evidence cells and spans, followed by an operator classifier to select from ten symbolic aggregation operators. The model also includes a scale prediction component to handle units like millions or billions. Experiments compare TAGOP against textual, tabular, and hybrid baselines like BERT-RC, TaPas, and HyBrider.

TAGOP achieves 58.0% F1 on the test set, an 11.1% absolute improvement over the best baseline, demonstrating the effectiveness of symbolic reasoning over hybrid data. However, this performance still lags significantly behind human experts, who achieve 90.8% F1. Error analysis reveals that 84% of errors stem from incorrect evidence extraction, highlighting the difficulty of aligning table and text. The paper concludes that TAT-QA is a challenging benchmark that exposes current limitations in numerical reasoning and hybrid data understanding, serving as a foundation for future research in financial QA.

## ConvFinQA: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering

- Year: 2022
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, spreadsheet reasoning, chain of thought, retrieval, prompt engineering, sec filings, tables, accuracy, benchmark, dataset, hallucination, numerical reasoning, conversational qa, multi-turn reasoning, neural symbolic
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["chain of thought", "retrieval", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["financial question answering", "benchmarking", "spreadsheet reasoning"]}
- One-line summary: ConvFinQA introduces a large-scale dataset for conversational financial question answering that requires complex, multi-turn numerical reasoning chains, revealing that both neural symbolic and prompting-based LLMs significantly lag behind human experts in handling long-range dependencies and domain-specific calculations.

### Detailed Summary

The paper addresses the challenge of complex numerical reasoning in financial natural language processing, specifically focusing on conversational question answering over financial reports. The authors propose ConvFinQA, a new dataset comprising 3,892 conversations and 14,115 questions derived from decomposing and concatenating multi-hop questions from the FinQA dataset. This construction simulates realistic investor-analyst dialogues where later questions depend on previous answers, creating long-range reasoning chains that test a model's ability to maintain context and perform sequential calculations across text and tables. The dataset includes both simple conversations from single question decomposition and hybrid conversations integrating two distinct aspects of a report, requiring models to navigate cross-dependencies and varying levels of numerical complexity.

Experiments evaluate two primary approaches: neural symbolic models and prompting-based large language models. The neural symbolic approach utilizes FinQANet, a pipeline combining a retriever for supporting facts with a generator for reasoning programs, tested with BERT and RoBERTa encoders. The prompting-based approach employs GPT-3 (text-davinci-002) using few-shot learning with various prompt formats, including answer-only, program generation in original and normal DSLs, and Chain-of-Thought reasoning. The evaluation metrics are execution accuracy and program accuracy. Results show that the best neural symbolic model (FinQANet with RoBERTa-large) achieves 68.90% execution accuracy, while the best prompting method (Program-normal) reaches only 48.85%. Both methods struggle significantly with later conversation turns and hybrid conversations, where dependency distances are longer and context management is more complex.

The findings highlight a substantial gap between current AI systems and human expert performance, which stands at 89.44% execution accuracy. Neural symbolic models excel at number selection but fail at complex program generation due to lack of domain knowledge and difficulty with long reasoning chains. GPT-3 performs poorly on the conversational paradigm, often mimicking exemplars rather than understanding the task, and struggles with references to previous context. The paper concludes that while LMs are powerful, they currently lack the robust reasoning capabilities required for real-world financial analysis tasks involving multi-turn, complex numerical dependencies. Limitations include the dataset's construction method, which may not cover all real-world conversational patterns, and the exclusive focus on GPT-3 for prompting experiments, leaving open questions about other models' performance in this specific domain.

## MultiHiertt: Numerical Reasoning over Multi Hierarchical Tabular and Textual Data

- Year: 2022
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, earnings analysis, equities, us equities, retrieval, annual reports, sec filings, tables, accuracy, benchmark, dataset, model, hallucination, table understanding, numerical reasoning, hierarchical data
- Tag facets: {"asset_class": ["equities"], "data_source": ["annual reports", "sec filings", "tables"], "deliverable": ["benchmark", "dataset", "model"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["financial question answering", "earnings analysis"]}
- One-line summary: The paper introduces MultiHiertt, a benchmark for numerical reasoning over multi-hierarchical tabular and textual financial data, and proposes MT2Net, a retrieval-reasoning model that significantly outperforms baselines but still lags far behind human experts.

### Detailed Summary

This paper addresses the limitation of existing financial question-answering benchmarks, which typically rely on single flat tables, by introducing MultiHiertt. This new dataset is constructed from S&P 500 annual reports and features documents containing multiple hierarchical tables and long unstructured texts. The primary research problem is enabling systems to perform complex, multi-step numerical reasoning that requires integrating information across these hierarchical structures and textual paragraphs, a task that mirrors the analytical work of financial professionals. The dataset includes 10,440 expert-annotated question-answer pairs with fine-grained reasoning programs and supporting facts, ensuring high quality and diversity in reasoning complexity.

To tackle this challenge, the authors propose MT2Net, a novel QA model consisting of a fact-retrieving module and a reasoning module. The retrieving module uses a BERT-based classifier to extract relevant supporting facts from both hierarchical tables and text, preserving the table's structural hierarchy by flattening cells with their row and column headers. The reasoning module then employs either a program generator or a span selector to compute the final answer. Experiments are conducted on MultiHiertt using various baselines, including FinQANet, TAGOP, and Longformer, with evaluation metrics including Exact Match and F1 scores. The study also includes a human performance baseline to assess the difficulty of the task.

The results demonstrate that MT2Net outperforms all existing baselines, achieving an F1 score of 38.43% on the test set, which is a significant improvement over previous models. However, this performance still lags far behind human experts, who achieved an F1 score of 87.03%. The analysis reveals that models struggle particularly with questions requiring reasoning across multiple tables, multi-step reasoning, and complex hierarchical structures. The paper highlights that current models fail to integrate supporting facts correctly and lack external financial knowledge. These findings indicate that MultiHiertt presents a strong challenge for current NLP models and underscores the need for more advanced table-encoding methods and multi-table reasoning mechanisms in financial AI systems.

## DocFinQA: A Long-Context Financial Reasoning Dataset

- Year: 2024
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: case study
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, retrieval, fine-tuning, 10-k filings, sec filings, accuracy, hit ratio, benchmark, dataset, data leakage, long-context, numerical reasoning, code generation
- Tag facets: {"asset_class": [], "data_source": ["10-k filings", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "hit ratio"], "market_context": [], "method": ["retrieval", "fine-tuning"], "risk_issue": ["data leakage"], "task": ["financial question answering", "benchmarking"]}
- One-line summary: DocFinQA extends the FinQA dataset by grounding 7,437 financial numerical reasoning questions in full-length SEC filings (averaging 123k words), revealing that even state-of-the-art LLMs and retrieval systems struggle significantly with long-context financial document analysis.

### Detailed Summary

The paper addresses the critical gap in financial LLM evaluation where existing datasets rely on short, pre-selected document excerpts, failing to reflect the reality of analysts sifting through hundreds of pages of SEC filings. The authors introduce DocFinQA, a long-document financial question-answering dataset that augments the original FinQA questions with full 10-K filing contexts, increasing average context length from under 700 words to 123k words. This setup tests the model's ability to perform quantitative reasoning and locate specific numerical data within massive, noisy documents, a task essential for realistic financial workflows. The dataset includes 801 unique SEC filings, with questions annotated with Python programs for interpretable, executable answers, ensuring that models must ground their reasoning in the provided text rather than relying on parametric knowledge alone.

The experimental evaluation compares retrieval-based QA pipelines against retrieval-free long-context LLMs. For retrieval, the study employs dense embedding models like ColBERT (including a finetuned variant), Sentence-BERT, and OpenAI Ada, alongside sparse BM25, to retrieve top-k chunks from chunked documents. These chunks are then fed into various LLMs, including Falcon, MPT, Llama 2, CodeLlama, Mistral, and GPT-3.5, using few-shot in-context learning. The results demonstrate that retrieval-based approaches generally outperform retrieval-free methods, with finetuned ColBERT showing the highest hit rates. However, even the best configurations yield low accuracy; GPT-3.5 achieved only 42.6% accuracy with retrieval, while non-expert humans scored 41%. The study also highlights that code-finetuned models and those with supervised fine-tuning perform better, and that larger context windows do not necessarily improve performance if the relevant information is lost in the middle of the document.

A case study on documents exceeding 100k tokens reveals that over 40% of questions remain unanswerable even by models with 128k context windows, indicating severe limitations in long-range dependency handling. The paper notes that non-expert human performance is significantly lower than expert performance in short-context settings, underscoring the difficulty of the task. Limitations include the lack of full validation for training and development sets and potential biases in the automatically generated Python code. The dataset is publicly available and serves as a benchmark for improving long-context financial reasoning, with implications for applications requiring specificity and long-range context understanding in legal and financial domains.

## FinanceBench: A New Benchmark for Financial Question Answering

- Year: 2023
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, due diligence, equities, us equities, retrieval, sec filings, 10-k filings, accuracy, hit ratio, benchmark, dataset, hallucination, ecological validity, long-context, prompt ordering, numerical reasoning
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "10-k filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "hit ratio"], "market_context": ["us equities"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["financial question answering", "due diligence"]}
- One-line summary: FinanceBench is a benchmark of 10,231 financial QA questions from public filings that reveals state-of-the-art LLMs like GPT-4-Turbo and Claude-2 still fail or hallucinate in over 20% of cases even with retrieval or long-context augmentation.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models (LLMs) for financial question answering (QA), noting that existing benchmarks lack ecological validity for real-world analyst tasks. FinanceBench is introduced as a comprehensive test suite comprising 10,231 questions derived from 361 public filings (10-Ks, 10-Qs, 8-Ks) of 40 publicly traded US companies. The dataset is designed to serve as a minimum performance standard, covering information extraction, numerical reasoning, and logical deduction, with a focus on open-book scenarios that require retrieval from external documents rather than relying solely on pre-trained knowledge.

The authors evaluate 16 configurations of four leading models (GPT-4, GPT-4-Turbo, Llama-2, Claude-2) across five setups: closed-book, oracle, single vector store, shared vector store, and long-context windows. A human-evaluated sample of 150 cases was manually reviewed to assess correctness, hallucinations, and refusals. The experimental design tests the impact of retrieval mechanisms and prompt ordering (context-first vs. context-last) on model performance, aiming to simulate realistic enterprise constraints where latency and document size are limiting factors.

Results indicate that while long-context models (Claude-2, GPT-4-Turbo) achieve ~76-79% accuracy, they still produce incorrect answers or refusals in over 20% of cases. Vector store retrieval significantly improves performance over closed-book settings but introduces high latency and complexity; notably, GPT-4-Turbo with a shared vector store failed or answered incorrectly 81% of the time. The study highlights that models often hallucinate plausible but wrong answers, particularly in numerical reasoning tasks, and that prompt ordering significantly affects long-context performance. The findings suggest current LLMs are not yet reliable for high-stakes financial QA without significant human oversight.


## SEC-QA: A Systematic Benchmark for Evaluating Long-Context Question Answering on SEC Filings

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, due diligence, equities, institutional investing, retrieval, chain of thought, sec filings, 10-k filings, accuracy, hit ratio, benchmark, dataset, data leakage, program-of-thought, multi-document reasoning, quantitative extraction
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "10-k filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "hit ratio"], "market_context": ["institutional investing"], "method": ["retrieval", "chain of thought"], "risk_issue": ["data leakage"], "task": ["financial question answering", "due diligence"]}
- One-line summary: SEC-QA introduces a dynamic benchmark for multi-document financial QA using SEC filings, demonstrating that standard RAG fails on complex quantitative tasks while a program-of-thought approach with document selection significantly improves accuracy.

### Detailed Summary

The paper addresses the critical gap in evaluating LLMs on complex, real-world financial tasks involving long-context, multi-document reasoning. Existing benchmarks suffer from data leakage and lack the structural complexity of professional financial analysis, such as navigating 10-Ks and 10-Qs. The authors propose SEC-QA, a framework that semi-automatically generates quantitative question-answer pairs from a database of S&P 500 metrics linked to their source SEC filings. This design ensures the benchmark is refreshable with new data, preventing training contamination, and covers parallel, multi-hop, and structural reference questions that mimic actual analyst workflows.

Experiments evaluate four systems: Vanilla RAG, Multi-Query RAG, CodeGen+PageR, and CodeGen+DocS+PageR, using GPT-4 and Ada embeddings. The CodeGen systems utilize program-of-thought to decompose questions into code that calls helper functions for document selection, page retrieval, and value extraction. Results show that Vanilla RAG performs poorly (30% accuracy on multi-doc tasks) due to retrieval bottlenecks, often retrieving wrong fiscal years. In contrast, CodeGen+DocS+PageR achieves 80% accuracy by leveraging metadata to filter documents before retrieval. The study highlights that document-level recall is the primary driver of QA performance, and that compound metric extraction remains a significant challenge even for advanced models.

The findings underscore the necessity of structured retrieval and code-based reasoning for financial QA, as neural retrieval alone is insufficient for navigating the repetitive and dense structure of SEC filings. The proposed system offers a viable path for automating complex financial data extraction, such as calculating revenue growth or comparing metrics across competitors. However, the approach incurs higher computational costs and latency due to multiple LLM calls. Limitations include the reliance on private databases for ground truth and the difficulty of applying this framework to public sector reports with inconsistent reporting standards, suggesting that the method is currently best suited for regulated, standardized financial disclosures.

## SECQUE: A Benchmark for Evaluating Question-Answering on SEC Filings

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, equities, us equities, prompt engineering, chain of thought, sec filings, 10-k filings, accuracy, benchmark, dataset, bias, llm evaluation, automated judging
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "10-k filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["prompt engineering", "chain of thought"], "risk_issue": ["bias"], "task": ["financial question answering", "benchmarking"]}
- One-line summary: SECQUE is a benchmark of 565 expert-written questions on SEC filings that evaluates LLMs on financial reasoning, with results showing GPT-4o leads but significant gaps remain in complex insight generation.

### Detailed Summary

The paper addresses the lack of domain-specific evaluation for LLMs in real-world financial analysis, noting that existing benchmarks often fail to capture the complexity of tasks financial analysts perform daily. SECQUE is introduced to fill this gap by providing a comprehensive dataset focused on SEC filings, specifically 10-K and 10-Q reports, which are central to corporate financial disclosure. The benchmark is designed to test models on their ability to comprehend, reason over, and synthesize information from lengthy, multi-format documents, moving beyond simple text processing to assess nuanced financial reasoning capabilities.

The dataset comprises 565 questions curated by subject matter experts, covering four categories: comparison and trend analysis, ratio calculation, risk assessment, and financial insight generation. It includes 45 unique SEC filings from 29 companies, with contexts provided in both HTML and Markdown formats to test robustness. The authors developed SECQUE-Judge, an automated evaluation mechanism using a panel of LLM judges (primarily GPT-4o) that aggregates multiple scoring instances to align with human expert evaluations. This judge was validated against human scores, demonstrating high precision in identifying correct answers. The benchmark was used to evaluate seven diverse LLMs, including GPT-4o, Llama-3.3-70B, and smaller models like Phi-4 and Mistral-Nemo.

Results indicate that while leading models perform reasonably well on risk factors and basic ratios, significant challenges persist in complex reasoning and insight generation. GPT-4o achieved the highest strict accuracy (0.69) and normalized accuracy (0.79), outperforming open-source models like Llama-3.3-70B. The study found that text representation (HTML vs. Markdown) had a minor impact, whereas prompt engineering significantly affected performance, with baseline prompts often outperforming more specific financial prompts. Limitations include potential biases in LLM-based judging and the need for broader coverage of document types. The benchmark is publicly available to facilitate further research in financial AI.


## FinanceReasoning: A Financial Benchmark for Large Reasoning Models

- Year: 2025
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, stock prediction, equities, us equities, chain of thought, prompt engineering, retrieval, time-series modeling, tables, accuracy, benchmark, dataset, hallucination, program of thought, numerical precision, function library
- Tag facets: {"asset_class": ["equities"], "data_source": ["tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["chain of thought", "prompt engineering", "retrieval", "time-series modeling"], "risk_issue": ["hallucination"], "task": ["benchmarking", "stock prediction"]}
- One-line summary: FinanceReasoning is a rigorous benchmark for evaluating large reasoning models in financial numerical tasks, demonstrating that combining reasoner and programmer models with structured knowledge retrieval significantly improves accuracy on complex financial calculations.

### Detailed Summary

The paper addresses the lack of credible, comprehensive, and challenging benchmarks for evaluating the numerical reasoning capabilities of Large Reasoning Models (LRMs) in the financial domain. Existing datasets suffer from annotation errors, ambiguous questions, and insufficient coverage of complex financial concepts, leading to inflated performance metrics that do not reflect real-world reasoning abilities. The authors introduce FinanceReasoning to provide a reliable evaluation suite that captures the nuances of financial calculations, such as fee structures, valuation formulas, and statistical tests, ensuring that model performance is assessed with high precision and domain-specific rigor.

The benchmark comprises 2,238 problems derived from re-annotating four public datasets and generating 908 new high-quality problems via Human-AI collaboration. A key contribution is the open-sourced financial function library containing 3,133 Python-formatted functions extracted from Investopedia, which serve as structured knowledge for retrieval-augmented generation. The authors evaluate six LRMs and seven standard LLMs using Chain-of-Thought (CoT) and Program-of-Thought (PoT) prompting. Experiments include knowledge augmentation via function retrieval and a collaborative setup where a reasoner model generates the logic and a programmer model executes the code.

Results show that OpenAI o1 with PoT achieves the highest accuracy (89.1% on Hard problems), but LRMs still struggle with formula application and numerical precision. Knowledge augmentation using the function library improves GPT-4o's accuracy to 91.6%. The combination of DeepSeek-R1 as a reasoner and Claude 3.5 Sonnet as a programmer yields 87.8% accuracy, correcting most calculation errors. The study highlights that PoT is more token-efficient and accurate than CoT for complex tasks, and identifies formula misapplication and rounding errors as primary failure modes for current models.


## BizBench: A Quantitative Reasoning Benchmark for Business and Finance

- Year: 2024
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, retrieval, fine-tuning, sec filings, tables, accuracy, benchmark, dataset, leaderboard, data leakage, quantitative reasoning, program synthesis, auditable reasoning, domain knowledge, code generation, error analysis
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables"], "deliverable": ["benchmark", "dataset", "leaderboard"], "evaluation": ["accuracy"], "market_context": [], "method": ["retrieval", "fine-tuning"], "risk_issue": ["data leakage"], "task": ["financial question answering", "benchmarking"]}
- One-line summary: BizBench introduces a comprehensive benchmark for evaluating LLMs' quantitative reasoning in finance through program synthesis, quantity extraction, and domain knowledge tasks, revealing that current models are bottlenecked by limited financial background knowledge rather than just code generation capabilities.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models' ability to perform precise, multi-step quantitative reasoning required in business and finance workflows. Unlike existing benchmarks focusing on sentiment or classification, BizBench emphasizes transparent reasoning via program synthesis, where models generate executable Python code to answer financial questions. This approach ensures that the rationale for answers is auditable, addressing the opacity of chain-of-thought methods. The benchmark isolates three core capabilities: extracting numerical values from text and tables, understanding financial domain knowledge and formulas, and synthesizing code to compute complex solutions, thereby providing a rigorous test of financial literacy and computational precision.

The methodology comprises eight tasks across three categories: program synthesis (FinCode, CodeFinQA, CodeTAT-QA), quantity extraction (SEC-Num, ConvFinQA Extract, TAT-QA Extract), and domain knowledge (FinKnow, FormulaEval). Data sources include newly collected SEC filings for SEC-Num, professional CFA/CPA exams for FinCode and FinKnow, and augmented versions of existing datasets like FinQA and TAT-QA. The authors evaluate a wide range of open-source (Llama-2, CodeLlama, Mistral) and commercial (GPT-4, GPT-3.5) models using zero-shot, few-shot, and supervised fine-tuning setups. Experiments measure accuracy against ground-truth numeric answers or executable code correctness, with strict matching criteria to ensure precision in financial calculations.

Results indicate that while larger models and those with code-specific pretraining perform better, significant performance gaps remain. GPT-4 leads but still fails over 36% of the most difficult FinCode questions, primarily due to errors in financial knowledge rather than code syntax. Error analysis reveals that models struggle with scaling (millions vs. billions), sign conventions for losses, and complex formula application. Fine-tuning smaller models like Llama-2-7B on BizBench data allows them to outperform larger unfine-tuned models, suggesting that targeted training in financial reasoning is highly effective. The paper highlights that current LLMs lack the robust financial background knowledge necessary for high-stakes, real-world financial applications, limiting their direct deployment in professional workflows without significant domain-specific adaptation.


## FinDABench: Benchmarking Financial Data Analysis Ability of Large Language Models

- Year: 2024
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: fraud detection, sentiment analysis, benchmarking, equities, china market, fine-tuning, prompt engineering, sec filings, news, accuracy, benchmark, dataset, bias, financial data analysis, llm evaluation, zero-shot learning, few-shot learning, domain adaptation, chart analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["fine-tuning", "prompt engineering"], "risk_issue": ["bias"], "task": ["fraud detection", "sentiment analysis", "benchmarking"]}
- One-line summary: FinDABench is a comprehensive benchmark evaluating LLMs on financial data analysis across foundational, reasoning, and technical skills, revealing that even GPT-4 achieves only 32.37% accuracy in zero-shot settings, highlighting significant gaps in domain-specific analytical capabilities.

### Detailed Summary

The paper addresses the lack of rigorous evaluation for Large Language Models in specialized financial data analysis, distinguishing it from general financial knowledge benchmarks. It introduces FinDABench, a benchmark designed to assess data-driven thinking through three dimensions: Foundational Ability (numerical calculation and sentiment risk assessment), Reasoning Ability (comprehending textual information and analyzing abnormal financial reports), and Technical Skill (generating analysis and visualizations). This framework mirrors the multifaceted workflow of financial analysts, moving beyond simple question-answering to test complex data synthesis and interpretation skills required in real-world scenarios.

The benchmark comprises 2,400 instances across six sub-tasks: Numerical Calculations QA, Early Warning Analysis, Fin-report Fraud Detection, Fin-report2Markdown, ChartData2Insight, and NL2ViSQL. Data sources include translated financial reports, scraped news articles, regulatory penalty announcements, and stock exchange filings. The authors evaluate 41 popular LLMs, including English, Chinese, and financial-specific models, in both zero-shot and few-shot settings. Evaluation metrics vary by task type, utilizing Accuracy, F1, Exact Match, and ROUGE scores to measure performance on classification, extraction, and generation tasks, providing a granular view of model strengths and weaknesses across different analytical competencies.

Results indicate that while Supervised Fine-Tuning and financial domain knowledge improve performance, significant challenges remain. GPT-4 achieves the highest score of 32.37% in zero-shot settings, with all other models scoring below 30%, demonstrating that current LLMs lack robust financial reasoning and technical skills. The study finds that financial-specific fine-tuning yields substantial gains but does not fully bridge the gap for complex tasks like SQL generation and chart insight extraction. Limitations include the benchmark's focus on Chinese financial contexts for some tasks and the potential for annotation bias in fraud detection, suggesting that further advancements in domain-specific training and reasoning capabilities are necessary for reliable deployment in financial data analysis.

## Fin-RATE: Financial Report Analytics and Tracking Evaluation for Large Language Models

- Year: 2026
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, equity research, equities, us equities, retrieval, sec filings, 10-k filings, accuracy, benchmark, dataset, hallucination, data leakage, multi-document reasoning, longitudinal tracking, cross-entity comparison, error taxonomy, llm-as-judge
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "10-k filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["retrieval"], "risk_issue": ["hallucination", "data leakage"], "task": ["benchmarking", "equity research"]}
- One-line summary: Fin-RATE introduces a benchmark for evaluating LLMs on SEC filings through detail, cross-entity, and longitudinal tasks, revealing that performance degrades significantly in multi-document reasoning due to hallucinations and entity mismatches.

### Detailed Summary

The paper addresses the limitation of existing financial LLM benchmarks that focus on isolated fact extraction rather than the complex, multi-document reasoning required by professional analysts. It introduces Fin-RATE, a benchmark built on U.S. SEC filings that mirrors analyst workflows through three pathways: detail-oriented reasoning within single disclosures, cross-entity comparison under shared topics, and longitudinal tracking of firms across reporting periods. The dataset includes 7,500 high-quality QA pairs derived from 2,472 filings across 43 companies, ensuring coverage of diverse industries and filing types beyond standard 10-Ks.

The authors evaluate 17 leading LLMs, including closed-source, open-source, and finance-specialized models, under both ground-truth context and retrieval-augmented generation (RAG) settings. They employ a fine-grained error taxonomy with 13 types across four categories to diagnose failures, using an LLM-as-Judge framework for evaluation. Experiments reveal substantial performance drops as task complexity increases, with accuracy falling by 18.60% and 14.35% when shifting from single-document to longitudinal and cross-entity analysis. The study also analyzes retrieval effectiveness, showing that hybrid retrieval with reranking improves evidence coverage but does not fully mitigate downstream reasoning errors.

Key findings indicate that closed-source models maintain robustness but suffer from reasoning inconsistencies, while finance-tuned models collapse on cross-entity tasks due to hallucinations and entity confusion. Longitudinal tracking is hindered by temporal mismatches and trend hallucinations, as models treat yearly data as independent units rather than continuous sequences. The paper highlights that current benchmarks fail to capture these specific failure modes, such as comparative stance hallucination and intent misunderstanding. These limitations suggest that while LLMs are improving at single-document parsing, they lack the structural and temporal abstraction necessary for reliable multi-document financial analysis, posing risks for deployment in high-stakes investment research.

## FinTagging: A Full-Scope Table-Aware XBRL Tagging Benchmark with LLMs

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: xbrl tagging, retrieval, sec filings, tables, xbrl, 10-k filings, accuracy, benchmark, dataset, framework, regulatory compliance
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables", "xbrl", "10-k filings"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["retrieval", "rag"], "risk_issue": ["regulatory compliance"], "task": ["xbrl tagging"]}
- One-line summary: FinTagging introduces a two-stage benchmark for XBRL tagging that decomposes the task into Financial Numeric Identification and Financial Concept Linking, revealing that while LLMs excel at extraction, they struggle significantly with fine-grained alignment to the full US-GAAP taxonomy.

### Detailed Summary

The paper addresses the critical need for accurate, machine-readable interpretation of financial reports by introducing FinTagging, the first comprehensive benchmark for structure-aware XBRL tagging. It argues that existing benchmarks oversimplify the task as flat classification over small concept subsets, ignoring the hierarchical semantics of the 17,000+ US-GAAP concepts and the structured nature of financial documents. FinTagging reframes tagging as an extract-and-align process, enabling evaluation under realistic reporting conditions where models must handle mixed text and table evidence. This approach provides a more rigorous assessment of LLMs' capabilities in numerical reasoning and taxonomy alignment, bridging the gap between academic benchmarks and regulatory compliance requirements.

The methodology decomposes the tagging process into two subtasks: Financial Numeric Identification (FinNI), which extracts numerical entities and their types from heterogeneous contexts, and Financial Concept Linking (FinCL), which maps these entities to the full US-GAAP taxonomy. The dataset comprises 142 SEC 10-K filings from 2023-2024, yielding over 260,000 numerical entities linked to 3,953 unique concepts. Evaluation involves 13 state-of-the-art LLMs and PLMs in zero-shot settings, using a retrieval-reranking framework for FinCL to mitigate extreme classification challenges. The study employs expert-verified audit sets and ablation studies to isolate error propagation and assess the impact of structure-aware context construction versus fixed-window approaches.

Results indicate that while large LLMs like DeepSeek-V3 and GPT-4o generalize well to long-tail concepts in extraction, they exhibit a significant knowledge-alignment gap in concept linking, with top accuracies below 0.19. The paper highlights that modeling tagging as single-step extreme classification leads to performance collapse, whereas the two-stage pipeline yields meaningful differentiation among models. Key limitations include the difficulty of disambiguating highly similar US-GAAP concepts, especially for table-origin entities, and the reliance on retrieval quality which caps downstream reranking performance. These findings underscore the need for improved structure-aware reasoning in financial LLMs for reliable automated reporting.

## Quantifying Material Risks from Textual Disclosures in Financial Statements using Large Language Model Agents

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: case study
- Summary coverage: full_extracted_text
- Tags: risk extraction, due diligence, equities, institutional investing, agentic workflow, sec filings, financial statements, framework, model risk, climate risk, materiality assessment, physical risk, context-aware analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "financial statements"], "deliverable": ["framework"], "evaluation": [], "market_context": ["institutional investing"], "method": ["agentic workflow"], "risk_issue": ["model risk"], "task": ["risk extraction", "due diligence"]}
- One-line summary: This paper demonstrates that LLM agents, by integrating textual disclosures with company-specific financial and operational context, can more accurately assess the materiality of physical climate risks in SEC filings than traditional keyword or embedding methods.

### Detailed Summary

The paper addresses the challenge of extracting and evaluating qualitative physical risk disclosures (e.g., natural disasters) from financial statements, where traditional keyword-based NLP fails to capture indirect or context-dependent language. It positions LLM agents as a superior tool for context-aware materiality assessment, moving beyond simple sentiment analysis to evaluate the financial significance of risks relative to a specific firm's profile. The research highlights the need for supervisors and investors to distinguish between material and non-material risks to improve decision-making and financial stability monitoring.

The methodology employs a three-stage pipeline: first, using semantic embeddings (OpenAI text-embedding-3-small) to extract relevant sentences from SEC 10-K and 8-K filings; second, applying sentiment analysis (ProntoNLP) to classify risk tone; and third, deploying an LLM agent to assess materiality. The agent is prompted with the disclosure text alongside granular company data, including financials (assets, revenue, EBITDA), business description, industry, and location. The study uses case studies from Box 3 and Table 1 to illustrate how the agent weighs factors like financial health and operational vulnerability to determine if a risk is material.

Findings show that the LLM agent effectively differentiates materiality based on context, such as identifying an $8.7 million write-off as material for a weak firm but a $69.2 million loss as non-material for a larger entity. It also recognizes long-term trends (e.g., increasing wildfires) as material for vulnerable sectors like winemaking. The paper concludes that LLMs augment human expertise by providing tailored initial evaluations, though final judgment remains with experts. Limitations include the subjective nature of materiality and the reliance on accurate external data integration.

## Financial Statement Analysis with Large Language Models

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: earnings analysis, alpha mining, stock prediction, equities, us equities, portfolio management, chain of thought, prompt engineering, backtesting, financial statements, sec filings, sharpe ratio, accuracy, portfolio returns, benchmark, dataset, framework, look-ahead bias, overfitting, fundamental analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "sec filings"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["sharpe ratio", "accuracy", "portfolio returns"], "market_context": ["us equities", "portfolio management"], "method": ["chain of thought", "prompt engineering", "backtesting"], "risk_issue": ["look-ahead bias", "overfitting"], "task": ["earnings analysis", "alpha mining", "stock prediction"]}
- One-line summary: This paper demonstrates that GPT-4, when prompted with standardized financial statements and chain-of-thought reasoning, outperforms human analysts and matches specialized machine learning models in predicting earnings direction, generating actionable alpha in trading strategies.

### Detailed Summary

The paper investigates whether large language models can perform financial statement analysis comparable to professional human analysts, addressing the gap in understanding LLM capabilities in quantitative, judgment-heavy tasks. The authors position this research to challenge the notion that LLMs are merely text-processing tools, exploring their potential to emulate human deductive reasoning in fundamental analysis without relying on narrative context or industry-specific soft information. This setup tests the lower bound of LLM performance, as the model is disadvantaged by the absence of management discussion and macroeconomic context typically used by humans.

The methodology involves feeding anonymized and standardized balance sheets and income statements from the Compustat universe (1968-2021) to GPT-4. The model is instructed via a Chain-of-Thought prompt to mimic analyst workflows, computing ratios and synthesizing insights to predict the directional change in future earnings. The study benchmarks GPT-4 against consensus analyst forecasts, stepwise logistic regression, and an artificial neural network trained on the same financial variables. To ensure results are not driven by memory leakage, the authors anonymize data, test for look-ahead bias using out-of-sample 2023 predictions, and verify that the model cannot identify firms from numerical data alone. They also analyze the informational content of the generated narratives using BERT embeddings.

Results show that GPT-4 achieves 60.31% accuracy and an F1-score of 63.45%, significantly outperforming human analysts (53-57%) and matching the state-of-the-art ANN (60.45% accuracy). The LLM exhibits a relative advantage in predicting earnings for loss-making and small firms where human analysts struggle. The generated narratives contain significant predictive power, with an ANN trained on GPT’s text embeddings achieving high accuracy. Trading strategies based on GPT’s predictions yield a Sharpe ratio of 3.36 and annual alphas exceeding 12% in the Fama-French three-factor model. However, the study notes limitations, including the model's reliance on specific prompt engineering and the potential for performance degradation in earlier LLM versions like GPT-3.5, suggesting that while LLMs are powerful, their deployment requires careful validation and may not yet fully replace specialized quantitative models in all contexts.

## Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, sentiment analysis, alpha mining, equities, options, derivatives, us equities, retail investing, prompt engineering, backtesting, time-series modeling, news, market prices, hit ratio, sharpe ratio, transaction costs, portfolio returns, dataset, framework, look-ahead bias
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["news", "market prices"], "deliverable": ["dataset", "framework"], "evaluation": ["hit ratio", "sharpe ratio", "transaction costs", "portfolio returns"], "market_context": ["us equities", "retail investing"], "method": ["prompt engineering", "backtesting", "time-series modeling"], "risk_issue": ["look-ahead bias", "overfitting"], "task": ["stock prediction", "sentiment analysis", "alpha mining"]}
- One-line summary: GPT-4 accurately predicts stock market reactions to news headlines with ~90% hit rates and significant drift predictability, particularly for small caps and negative news, though strategy returns decline as LLM adoption increases.

### Detailed Summary

This paper investigates whether off-the-shelf large language models (LLMs) like ChatGPT can predict stock market reactions to news headlines without explicit financial training. The authors position LLMs as novel instruments for studying market information processing, comparing LLM assessments of news economic implications with actual market responses to quantify underreaction and information processing frictions. They develop a theoretical model incorporating LLM technology, information-processing constraints, and limits to arbitrage to explain why sophisticated models can exploit these inefficiencies.

The empirical analysis uses 159,137 firm-headline-date observations for 4,123 U.S. stocks from October 2021 to May 2024, ensuring an out-of-sample evaluation post-Knowledge cutoff. The authors prompt GPT-4 to categorize headlines as positive, negative, or neutral, then measure initial market reactions and subsequent price drift. They compare GPT-4 against smaller models (GPT-3.5, Llama2) and embedding-based supervised learning methods. Experiments include long-short daily-rebalanced strategies, transaction cost sensitivity analyses with partial rebalancing, and topic modeling to decompose performance across news themes like earnings, insider transactions, and clinical trials.

GPT-4 achieves ~90% hit rates for initial reactions and generates a long-short strategy with an annualized Sharpe ratio of 2.97 (zero costs), significantly outperforming smaller models. Predictability is concentrated in small-cap stocks and negative news, consistent with limits to arbitrage. The study finds that as LLM adoption rises, strategy returns decline, suggesting improved market efficiency. However, high turnover and transaction costs limit practical tradability for large investors. The paper concludes that financial reasoning is an emerging capacity of complex LLMs, offering a new lens on market inefficiencies and the impact of AI on price discovery.

## AI in Investment Analysis: Large Language Models for Equity Stock Ratings

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, equity research, earnings analysis, equities, us equities, chain of thought, prompt engineering, 10-k filings, news, market prices, earnings calls, accuracy, backtest, framework, dataset, bias, data leakage, sentiment analysis, ordinal regression
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "news", "market prices", "earnings calls"], "deliverable": ["framework", "dataset"], "evaluation": ["accuracy", "backtest"], "market_context": ["us equities"], "method": ["chain of thought", "prompt engineering"], "risk_issue": ["bias", "data leakage"], "task": ["stock prediction", "equity research", "earnings analysis"]}
- One-line summary: This study demonstrates that GPT-4-32k, prompted with financial fundamentals and sentiment scores, outperforms traditional Wall Street analysts in predicting S&P 500 stock ratings based on forward returns, while revealing that raw news text introduces bias compared to structured sentiment inputs.

### Detailed Summary

The paper addresses the challenge of automating equity stock ratings, a core task in investment analysis traditionally performed by human analysts who face data overload and cognitive biases. The authors position Large Language Models (LLMs) as a cost-effective, consistent alternative capable of processing multimodal financial data. The research problem centers on evaluating whether instruction-based LLMs can match or exceed the predictive accuracy of professional analysts when provided with structured financial inputs, specifically focusing on the impact of different data modalities such as fundamentals, news summaries, and sentiment scores on rating accuracy.

The methodology employs GPT-4-32k (v0613) with a September 2021 training cutoff to prevent data leakage, applied to S&P 500 constituents from January 2022 to June 2024. The experimental design compares five methods: a Vanilla baseline using technical indicators, News (summaries), Sentiment (pre-computed scores), Fundamentals (quarterly 10-K/10-Q metrics), and Fundamentals + Sentiment. The model uses Chain-of-Thought prompting to generate ordinal ratings (Strong Sell to Strong Buy) and price targets. Evaluation is conducted using Mean Absolute Error (MAE) against forward returns (1, 3, 6, 12, 18 months), quantifying accuracy by comparing predicted ratings to the actual return quintiles of the market.

Results indicate that the Fundamentals + Sentiment method achieves the lowest MAE (1.417), outperforming both the Vanilla baseline (1.447) and traditional analysts (1.570). While news summaries improve short-term (1-month) prediction, they introduce positive bias and do not enhance long-term accuracy compared to sentiment scores, which reduce token usage without performance loss. The study highlights that LLMs are more accurate in short-term horizons, whereas analysts perform relatively better over longer periods. Limitations include the exclusion of qualitative factors like earnings call transcripts and the sensitivity of forward-return evaluation to market volatility, suggesting that while LLMs offer a robust framework, they currently lack the nuanced qualitative judgment of human experts.

## FinMem: A Performance-Enhanced Large Language Model Trading Agent with Layered Memory and Character Design

- Year: 2023
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, strategy generation, equities, portfolio management, agentic workflow, backtesting, retrieval, 10-k filings, news, backtest, portfolio returns, sharpe ratio, framework, open source, trading agent, overfitting, memory systems, interpretability, deep reinforcement learning comparison
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "news"], "deliverable": ["framework", "open source", "trading agent"], "evaluation": ["backtest", "portfolio returns", "sharpe ratio"], "market_context": ["portfolio management"], "method": ["agentic workflow", "backtesting", "retrieval"], "risk_issue": ["overfitting"], "task": ["algorithmic trading", "strategy generation"]}
- One-line summary: FinMem introduces an LLM-based trading agent with a layered memory system and dynamic character design that significantly outperforms deep reinforcement learning baselines in stock trading by effectively prioritizing time-sensitive financial data.

### Detailed Summary

The paper addresses the limitations of existing LLM-based financial agents, which often lack robust memory mechanisms to handle the varying timeliness of financial data, and Deep Reinforcement Learning (DRL) agents, which suffer from poor interpretability and difficulty integrating textual information. FinMem is proposed as a transparent, autonomous trading agent that mimics human cognitive structures to process multi-source financial data. It aims to bridge the gap between general-purpose LLMs and specialized trading needs by providing a framework that can self-evolve its knowledge base and adapt to market volatility through adjustable risk profiles.

FinMem comprises three modules: Profiling, Memory, and Decision-making. The Profiling module sets a dynamic character with specific professional backgrounds and adjustable risk inclinations (risk-seeking, risk-averse, or self-adaptive). The Memory module features a layered long-term memory (shallow, intermediate, deep) that stores insights from daily news, 10-Q reports, and 10-K reports with different decay rates, alongside a working memory for summarization and reflection. The Decision-making module uses these memories to generate buy/sell/hold actions. Experiments were conducted on real-world stock data (e.g., TSLA) comparing FinMem against DRL agents like PPO and DQN, using metrics such as Cumulative Return and Sharpe Ratio.

FinMem demonstrates superior trading performance compared to DRL baselines, achieving higher Cumulative Returns and Sharpe Ratios. The study highlights that tuning the working memory capacity (Top-K) significantly impacts performance, with K=5 showing optimal results for TSLA. The self-adaptive risk profile allows the agent to mitigate losses during downturns. Limitations include reliance on general-purpose LLMs and limited dataset scope, though the authors note potential for improvement with financial-specific LLMs and larger datasets. The framework is also suggested for multi-agent portfolio optimization.

## TradingAgents: Multi-Agents Large Language Models for Financial Trading

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, strategy generation, portfolio optimization, equities, us equities, multi-agent systems, agentic workflow, backtesting, prompt engineering, ohlc data, news, social media, financial statements, backtest, sharpe ratio, drawdown, portfolio returns, framework, open source, trading agent
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "news", "social media", "financial statements"], "deliverable": ["framework", "open source", "trading agent"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["us equities"], "method": ["multi-agent systems", "agentic workflow", "backtesting", "prompt engineering"], "risk_issue": ["look-ahead bias", "hallucination"], "task": ["algorithmic trading", "strategy generation", "portfolio optimization"]}
- One-line summary: TradingAgents introduces a multi-agent LLM framework that simulates professional trading firm dynamics through specialized analyst, researcher, trader, and risk management roles, achieving superior risk-adjusted returns compared to rule-based baselines on major tech stocks.

### Detailed Summary

The paper addresses the limitation of existing LLM trading systems that lack realistic organizational modeling and suffer from inefficient natural language communication interfaces. It proposes TradingAgents, a framework inspired by professional trading firms, featuring specialized agents including fundamental, sentiment, news, and technical analysts, alongside bullish and bearish researchers, traders with varied risk profiles, and a risk management team. The system employs a hybrid communication protocol combining structured reports for clarity and natural language debates for reasoning, utilizing both quick-thinking and deep-thinking LLMs to balance efficiency and analytical depth.

Experiments were conducted via backtesting on major technology stocks (Apple, Nvidia, Microsoft, Meta, Google) from January to March 2024, using a multi-modal dataset comprising historical prices, news, social media sentiment, insider transactions, financial statements, and 60 technical indicators. The framework was benchmarked against Buy-and-Hold, MACD, KDJ+RSI, ZMR, and SMA strategies. Evaluation metrics included cumulative return, annualized return, Sharpe ratio, and maximum drawdown, with agents making decisions based solely on available data to prevent look-ahead bias.

TradingAgents significantly outperformed all baselines, achieving cumulative returns of 26.62% for Apple, 24.36% for Google, and 23.21% for Amazon, surpassing the best rule-based baselines by margins of 6-24%. It demonstrated superior risk-adjusted performance with higher Sharpe ratios and controlled maximum drawdowns, despite rule-based methods sometimes showing lower drawdowns. The debate mechanism and structured communication effectively mitigated context loss and hallucination, providing explainable trading decisions. However, the study is limited to a short backtesting period on large-cap tech stocks, and the reliance on API-based LLMs incurs computational costs, while real-world deployment faces challenges like transaction fees and market impact not fully captured in the simulation.

## InvestorBench: A Benchmark for Large Language Model Agents in Financial Decision-Making

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, stock prediction, portfolio optimization, equities, crypto, etfs, portfolio management, agentic workflow, backtesting, time-series modeling, ohlc data, sec filings, news, backtest, sharpe ratio, drawdown, portfolio returns, benchmark, dataset, framework
- Tag facets: {"asset_class": ["equities", "crypto", "etfs"], "data_source": ["ohlc data", "sec filings", "news"], "deliverable": ["benchmark", "dataset", "framework", "open source"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["portfolio management"], "method": ["agentic workflow", "backtesting", "time-series modeling"], "risk_issue": ["bias", "overfitting"], "task": ["benchmarking", "stock prediction", "portfolio optimization"]}
- One-line summary: InvestorBench introduces a comprehensive benchmark and agent framework for evaluating LLM-based financial decision-making across stocks, cryptocurrencies, and ETFs, revealing that proprietary models significantly outperform open-source alternatives in complex, volatile markets.

### Detailed Summary

The paper addresses the lack of standardized benchmarks for LLM-based agents in financial decision-making by introducing InvestorBench, a unified framework that extends the FINMEM architecture to handle diverse asset classes. The agent employs a layered memory system with varying decay rates to process multi-modal data, including OHLCV prices, SEC filings, and news sentiment, enabling sequential Buy/Sell/Hold decisions within a Partially Observable Markov Decision Process (POMDP) formulation. This approach aims to mimic human cognitive processes by integrating immediate observations with long-term historical insights to adapt to market volatility.

The benchmark evaluates thirteen LLMs, ranging from small open-source models to large proprietary ones, across three distinct environments: single-stock trading (MSFT, TSLA, etc.), cryptocurrency trading (BTC, ETH), and ETF investing. Data sources include Yahoo Finance, SEC EDGAR, and specialized crypto/ETF news datasets. Experiments measure performance using Cumulative Return (CR), Sharpe Ratio (SR), Annualized Volatility, and Maximum Drawdown, comparing agent outputs against passive Buy & Hold baselines. The setup includes a warm-up phase for memory calibration and a test phase for evaluation, ensuring a rigorous assessment of reasoning and risk management capabilities.

Results indicate that proprietary models like GPT-4 and GPT-o1-preview consistently achieve superior CR and SR compared to open-source and domain-specific fine-tuned models, particularly in volatile or complex market conditions. While large open-source models (e.g., Llama-3.1-70B) perform competitively in stable stock markets, they struggle in cryptocurrency and ETF tasks where deep reasoning and broad pre-training knowledge are critical. The study highlights that domain-specific fine-tuning alone does not guarantee trading superiority, suggesting that general reasoning capabilities and model scale are more decisive factors for agentic financial decision-making than specialized financial pre-training.

## StockBench: Can Large Language Models Beat the Stock Market?

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, portfolio optimization, equities, us equities, backtesting, agentic workflow, market prices, financial statements, news, backtest, drawdown, portfolio returns, benchmark, open source, data leakage, look-ahead bias, agent debate, multi-agent systems
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "financial statements", "news"], "deliverable": ["benchmark", "open source"], "evaluation": ["backtest", "drawdown", "portfolio returns"], "market_context": ["us equities"], "method": ["backtesting", "agentic workflow"], "risk_issue": ["data leakage", "look-ahead bias"], "task": ["stock prediction", "portfolio optimization"]}
- One-line summary: STOCKBENCH evaluates LLM agents in a contamination-free, multi-month stock trading environment, revealing that while top models like Kimi-K2 can outperform buy-and-hold baselines, most struggle with profitability and risk management compared to simple passive strategies.

### Detailed Summary

This paper introduces STOCKBENCH, a benchmark designed to evaluate Large Language Model (LLM) agents in realistic, dynamic stock trading environments, addressing the gap left by static financial question-answering benchmarks. The benchmark focuses on sequential decision-making over a multi-month horizon, requiring agents to process daily market signals including prices, fundamentals, and news to make buy, sell, or hold decisions. The primary goal is to assess both profitability and risk management capabilities in a contamination-free setting using recent market data from March to June 2025, ensuring no overlap with model training corpora.

The experimental setup involves a back-trading environment with 20 high-weight Dow Jones Industrial Average (DJIA) stocks. Agents operate through a four-step workflow: portfolio overview, in-depth stock analysis, decision generation, and execution validation. The study evaluates a diverse set of proprietary and open-source LLMs, including GPT-5, Claude-4, Qwen3, and Kimi-K2, against a passive equal-weight buy-and-hold baseline. Performance is measured using cumulative return, maximum drawdown, and the Sortino ratio, with a composite ranking derived from z-scores of these metrics to balance profit and risk.

Results indicate that while most LLM agents achieve lower maximum drawdowns than the passive baseline, indicating effective downside risk management, many fail to significantly outperform the simple buy-and-hold strategy in terms of cumulative return. Kimi-K2 emerges as the top performer, achieving positive returns and robust risk profiles, whereas reasoning-tuned models do not consistently outperform instruction-tuned counterparts. The study highlights that strong performance on static financial QA does not guarantee effective trading behavior, and notes limitations such as the exclusion of trading costs, slippage, and high-frequency trading dynamics.

## Can LLM-Based Financial Investing Strategies Outperform?

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, stock prediction, equities, us equities, backtesting, reinforcement learning, market prices, news, sec filings, backtest, drawdown, sharpe ratio, benchmark, framework, look-ahead bias, overfitting, survivorship bias, data-snooping bias, regime-aware risk control, api cost analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "news", "sec filings"], "deliverable": ["benchmark", "framework"], "evaluation": ["backtest", "drawdown", "sharpe ratio"], "market_context": ["us equities"], "method": ["backtesting", "reinforcement learning"], "risk_issue": ["look-ahead bias", "overfitting"], "task": ["portfolio optimization", "stock prediction"]}
- One-line summary: The FINSABER framework reveals that LLM-based investing strategies fail to outperform simple benchmarks like Buy-and-Hold over long horizons and broad universes due to survivorship bias in prior evaluations and poor regime-aware risk control.

### Detailed Summary

This paper addresses the lack of robust evaluation for LLM-based financial investing strategies, which often suffer from survivorship, look-ahead, and data-snooping biases due to narrow timeframes and selective stock choices. The authors propose FINSABER, a comprehensive backtesting framework designed to mitigate these biases by utilizing a 20-year history of S&P 500 constituents (including delisted stocks) and integrating multi-source unstructured data. The study critically assesses the generalizability of LLM agents by comparing them against traditional rule-based, machine learning, and reinforcement learning baselines under rigorous, bias-aware conditions.

The experimental design employs a two-step pipeline: a selection-based module to generate unbiased stock universes and a timing-based module to execute daily trading signals. The authors evaluate prominent LLM agents, specifically FinMem and FinAgent, alongside benchmarks such as Buy-and-Hold, Moving Average Crossover, and RL agents (PPO, SAC). Experiments cover two decades (2004–2024) across multiple market regimes, using metrics like Sharpe Ratio, Maximum Drawdown, and Alpha/Beta decomposition. The study also includes statistical validation via paired t-tests and behavioral diagnostics through underwater plots to analyze drawdown profiles.

Results indicate that previously reported LLM advantages vanish under broader, longer evaluations, with simple strategies like Buy-and-Hold often outperforming LLMs in risk-adjusted returns. LLM strategies exhibit regime-specific flaws: they are overly conservative in bull markets, missing gains, and overly aggressive in bear markets, incurring severe drawdowns. The agents fail to generate statistically significant alpha, suggesting their performance is driven by market beta rather than skill. The paper concludes that future LLM strategies must prioritize trend detection and adaptive risk management over architectural complexity, noting that high API costs further diminish their practical viability.

## FinTradeBench: A Comprehensive Benchmark for Fundamental and Technical Analysis in Financial Trading

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, stock prediction, equities, us equities, retrieval, sec filings, ohlc data, accuracy, backtest, benchmark, dataset, hallucination, nasdaq-100, time-series modeling
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "ohlc data"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "backtest"], "market_context": ["us equities"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["benchmarking", "stock prediction"]}
- One-line summary: FinTradeBench is a benchmark evaluating LLM financial reasoning over company fundamentals and trading signals, revealing that while retrieval-augmented generation (RAG) significantly improves fundamental analysis, it degrades performance on trading signal reasoning due to LLMs' inability to parse raw numerical time-series data.

### Detailed Summary

The paper addresses the limitation of existing financial benchmarks that focus primarily on textual accounting data, ignoring the critical integration of market dynamics. It introduces FinTradeBench, a benchmark comprising 1,400 questions grounded in NASDAQ-100 companies from 2015 to 2025. The benchmark is structured into three categories: fundamentals-focused, trading-signal-focused, and hybrid questions requiring cross-signal reasoning. The authors employ a calibration-then-scaling framework, using expert seed questions, multi-model response generation, numerical auditing, and human-LLM judge alignment to ensure high-quality annotations. This approach allows for a rigorous evaluation of how well LLMs can synthesize heterogeneous financial signals.

The experimental setup involves evaluating 14 LLMs, ranging from small open-source models to large proprietary ones, under both zero-shot and retrieval-augmented generation (RAG) settings. The RAG architecture features a dual-track retrieval engine: one track indexes SEC filings using hierarchical chunking and dense embeddings, while the other indexes historical price data (OHLCV) for trading signals. The study measures performance using absolute accuracy, relative retrieval delta, and golden indicator F1 scores. The authors also conduct ablation studies and qualitative case studies to analyze the impact of context quality and model architecture on reasoning depth and factual precision.

Key findings indicate a clear performance gap between fundamental and trading reasoning. RAG substantially improves accuracy on fundamentals-focused questions (up to +37%) by grounding models in textual disclosures. However, RAG degrades performance on trading-signal questions (up to -19.7%) because LLMs struggle to compute technical indicators from raw numerical tables, leading to distraction and hallucination. Hybrid questions show the highest gains for reasoning-capable models (e.g., DeepSeek-R1), highlighting the need for latent chain-of-thought capabilities. The study concludes that current LLMs lack the representational framework for quantitative market data and that pre-computed signals are necessary for effective reasoning, suggesting future work should focus on code execution or specialized numerical processing rather than pure text retrieval.

## StockGPT: A GenAI Model for Stock Prediction and Trading

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: stock prediction, alpha mining, portfolio optimization, equities, us equities, portfolio management, time-series modeling, fine-tuning, backtesting, market prices, ohlc data, sharpe ratio, portfolio returns, transaction costs, backtest, model, benchmark, overfitting, look-ahead bias, generative ai
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "ohlc data"], "deliverable": ["model", "benchmark"], "evaluation": ["sharpe ratio", "portfolio returns", "transaction costs", "backtest"], "market_context": ["us equities", "portfolio management"], "method": ["time-series modeling", "fine-tuning", "backtesting"], "risk_issue": ["overfitting", "look-ahead bias"], "task": ["stock prediction", "alpha mining", "portfolio optimization"]}
- One-line summary: StockGPT is a lightweight decoder-only transformer trained on 70 million daily US stock returns that automatically learns predictive patterns, yielding long-short portfolios with significant alphas against standard asset pricing factors.

### Detailed Summary

This paper addresses the challenge of automating stock return prediction by applying generative AI logic to numeric time series data. The author argues that while language models have been used for sentiment-based trading, they rely on noisy text proxies. StockGPT treats discrete return intervals as tokens, allowing a transformer to learn hidden price patterns directly from historical data without manual feature engineering or news dependency. The model aims to surpass human-designed strategies by capturing complex dependencies in price movements through its attention mechanism.

The methodology involves training a ~1 million parameter decoder-only transformer on 50 million daily US stock returns from 1926-2000. Returns are discretized into 402 bins. The model predicts the next day's return distribution given a 256-day input sequence. Experiments include Fama-MacBeth regressions to assess forecast accuracy and the construction of daily and monthly rebalanced long-short decile portfolios. Performance is evaluated against transaction costs and benchmarked against Fama-French five-factor and Hou q-factor models using spanning tests to determine if the AI strategy subsumes traditional factors.

Results show that the daily equal-weighted portfolio yields an annualized return of 119% with a Sharpe ratio of 6.5, while the value-weighted version yields 27% with a Sharpe ratio of 1. The monthly model achieves 13% annual return with a Sharpe ratio of 1. Crucially, spanning tests reveal that StockGPT portfolios earn highly significant alphas against all standard factors, suggesting a novel AI pricing effect. The model also spans momentum and reversal strategies, indicating it automatically learns these patterns. Limitations include the need for frequent retraining, the model's current focus on small-cap predictability, and the lack of high-frequency data integration.

## Decision-Informed Neural Networks with Large Language Model Integration for Portfolio Optimization

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Portfolio, ETF, and Asset Allocation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, equities, us equities, fine-tuning, time-series modeling, tool use, ohlc data, financial statements, sharpe ratio, portfolio returns, risk-adjusted returns, framework, model, overfitting, decision-focused learning, differentiable optimization, llm embeddings, cross-attention
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "financial statements"], "deliverable": ["framework", "model"], "evaluation": ["sharpe ratio", "portfolio returns", "risk-adjusted returns"], "market_context": ["us equities"], "method": ["fine-tuning", "time-series modeling", "tool use"], "risk_issue": ["overfitting"], "task": ["portfolio optimization"]}
- One-line summary: The paper proposes a Decision-Informed Neural Network (DINN) that integrates Large Language Model embeddings with differentiable portfolio optimization to align return predictions directly with investment decision quality, outperforming traditional prediction-focused models on S&P100 and DOW30 datasets.

### Detailed Summary

The paper addresses the critical disconnect between prediction accuracy and decision quality in portfolio optimization, arguing that minimizing mean squared error alone leads to suboptimal portfolio weights due to estimation sensitivity. It positions its approach as a bridge between advanced representation learning and decision-focused learning, leveraging the representational power of Large Language Models (LLMs) to capture complex market dynamics that traditional statistical methods miss. The core problem is that conventional two-stage processes fail to account for how prediction errors propagate into portfolio construction, often resulting in poor out-of-sample performance despite high in-sample predictive accuracy.

The proposed Decision-Informed Neural Network (DINN) architecture integrates LLM-based semantic embeddings with time-series data through a cross-attention mechanism. Input embeddings are generated by converting pairwise asset relationships, sector-level yields, and irregularly sampled macroeconomic variables into textual prompts, which are then embedded using a pretrained LLM. These embeddings are fused with normalized and decomposed return series (separating long-term trends from short-term dynamics) via cross-attention layers. The model outputs predicted returns and covariance factors, which are fed into a differentiable convex optimization layer. This layer computes optimal portfolio weights end-to-end, allowing gradients from the portfolio performance loss to backpropagate through the optimization layer to the forecasting network, thereby aligning prediction objectives with decision objectives.

Extensive experiments on S&P100 and DOW30 datasets demonstrate that DINN consistently outperforms state-of-the-art deep learning baselines in terms of Sharpe ratio, Sortino ratio, and terminal wealth. Gradient-based analyses reveal that the model prioritizes forecasting accuracy for assets with high sensitivity to portfolio weights, effectively mitigating the impact of estimation errors on decision quality. The findings underscore the value of integrating decision objectives into the learning process, showing that context-aware, decision-focused models are more robust to market regime shifts and non-stationary relationships than purely predictive models. Limitations include the computational overhead of LLM embedding generation and the reliance on specific risk-aversion parameters for the optimization layer.

## Leveraging Large Language Models for Top-Down Sector Allocation

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Portfolio, ETF, and Asset Allocation
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: portfolio optimization, sentiment analysis, forecasting, equities, etfs, us equities, portfolio management, agentic workflow, multi-agent systems, prompt engineering, backtesting, news, financial statements, market prices, sharpe ratio, backtest, portfolio returns, transaction costs, framework, dataset
- Tag facets: {"asset_class": ["equities", "etfs"], "data_source": ["news", "financial statements", "market prices"], "deliverable": ["framework", "dataset", "open source"], "evaluation": ["sharpe ratio", "backtest", "portfolio returns", "transaction costs"], "market_context": ["us equities", "portfolio management"], "method": ["agentic workflow", "multi-agent systems", "prompt engineering", "backtesting"], "risk_issue": ["look-ahead bias"], "task": ["portfolio optimization", "sentiment analysis", "forecasting"]}
- One-line summary: The paper introduces an LLM-based agentic framework for top-down sector allocation that integrates macroeconomic indicators and aspect-based sentiment analysis, achieving a Sharpe ratio of 2.51 and 8.79% return in backtests compared to a baseline cross-momentum strategy.

### Detailed Summary

This paper addresses the gap in LLM applications for top-down investment strategies, specifically sector allocation, by proposing a multi-agent architecture that synthesizes macroeconomic data and market sentiment. While existing research focuses on bottom-up security selection, this work leverages LLMs to interpret complex macro-financial relationships and adjust sector weights dynamically based on economic cycles and sentiment shifts. The framework aims to automate the extraction of systematic macro signals and their integration into portfolio construction, offering a more responsive approach to sector-level risk and opportunity identification than traditional static models.

The methodology employs a dual-stream agentic pipeline using DeepSeek-7B for sentiment analysis and Llama-3.3-70B for ranking. The Sentiment Agent performs Named Entity Recognition and Aspect-Based Sentiment Analysis (ABSA) on news articles, storing results in a memory module. The Macro Agent processes economic indicators (CPI, PPI, PCE, NFP, PMI) and FOMC minutes, calculating trends and summarizing policy stances. A Ranking Agent integrates these memories with current portfolio positions to generate stock rankings across 11 GICS sectors. The system was backtested on S&P 500 constituents from January to June 2019, using Alpha Vantage data and NewsAPI, with a $100M initial capital and realistic transaction costs.

Empirical results show the proposed sector-allocation strategy significantly outperformed a cross-momentum baseline, yielding an 8.79% return and a Sharpe ratio of 2.51 versus -1.39% and -0.61, respectively. The study highlights the viability of LLMs for systematic macro analysis but notes limitations including a short backtesting period constrained by computational costs and the potential for improved performance with larger models or additional fundamental data. The authors suggest future work could incorporate reinforcement learning for ranking or counterfactual explanations for regulatory compliance.

## Your AI, Not Your View: The Bias of Large Language Models in Investment Analysis

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, portfolio optimization, equities, us equities, backtesting, sec filings, backtest, portfolio returns, risk-adjusted returns, benchmark, dataset, bias, look-ahead bias, confirmation bias, s p 500, synthetic data, model auditing
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["backtest", "portfolio returns", "risk-adjusted returns"], "market_context": ["us equities"], "method": ["backtesting"], "risk_issue": ["bias", "look-ahead bias"], "task": ["equity research", "portfolio optimization"]}
- One-line summary: This paper introduces a three-stage experimental framework to quantify latent investment biases in LLMs, revealing that models exhibit strong, persistent confirmation biases toward technology stocks, large-cap firms, and contrarian strategies, which cause them to ignore significant counter-evidence.

### Detailed Summary

The paper addresses the critical problem of knowledge conflict in financial LLMs, where pre-trained parametric biases clash with real-time market data, leading to unreliable investment recommendations. The authors argue that existing evaluations fail to capture how LLMs handle conflicting signals, a common scenario in active portfolio management and research. They position their work as a necessary diagnostic tool for trustworthiness, aiming to quantify how internal priors override objective evidence in decision-making processes.

The methodology employs a three-stage framework using 427 S&P 500 stocks. First, balanced buy/sell evidence with uniform 5% intensity is generated by a neutral model to create knowledge conflicts. Second, bias is elicited by measuring decision preferences in balanced contexts, revealing sector, size, and momentum biases. Third, bias persistence is verified by introducing imbalanced counter-evidence in volume and intensity. The study evaluates six major LLMs, including GPT-4.1 and Llama4-Scout, using metrics like bias scores and decision flip rates, supported by statistical tests and entropy analysis of model uncertainty.

Results show consistent biases toward technology sectors, large-cap stocks, and contrarian strategies. Models exhibit strong confirmation bias, with flip rates dropping sharply when even a small amount of supporting evidence is present, despite a majority of counter-evidence. For instance, models with high initial bias struggled to reverse decisions even with 10% intensity increments in counter-evidence. The study highlights that these biases can lead to systematic overvaluation of popular assets and underperformance in momentum strategies. Limitations include the use of synthetic evidence and a focus on hypothetical scenarios rather than live trading, though the findings provide a crucial baseline for auditing financial AI systems.

## Leveraging Large Language Models for Institutional Investment Management

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: portfolio optimization, stock prediction, spreadsheet reasoning, equities, bonds, institutional investing, portfolio management, prompt engineering, chain of thought, backtesting, market prices, financial statements, tables, sharpe ratio, drawdown, backtest, framework, open source, model risk, persona-based ensemble
- Tag facets: {"asset_class": ["equities", "bonds"], "data_source": ["market prices", "financial statements", "tables"], "deliverable": ["framework", "open source"], "evaluation": ["sharpe ratio", "drawdown", "backtest"], "market_context": ["institutional investing", "portfolio management"], "method": ["prompt engineering", "chain of thought", "backtesting"], "risk_issue": ["model risk"], "task": ["portfolio optimization", "stock prediction", "spreadsheet reasoning"]}
- One-line summary: This study demonstrates that LLM-based portfolio management strategies, utilizing persona-based ensembles and economic indicators, outperform buy-and-hold in Sharpe ratio during rising CPI periods but lag during market downturns.

### Detailed Summary

The paper addresses the gap in applying Large Language Models to complex institutional portfolio management by investigating their ability to predict price movements in a 40/60 stock-bond portfolio using macroeconomic indicators. The authors position this work within the context of institutional decision-making, where diverse investor attitudes and long-term perspectives are critical, contrasting with prior research focused on individual stock selection or individual investor behaviors. The core problem is determining whether LLMs can effectively translate economic data into actionable portfolio adjustments and how different 'personas' influence these predictions.

The methodology employs GPT-4 to predict three-class portfolio movements (hold, rise, fall) based on ten days of seven economic indicators, including interest rates, VIX, and currency indices. The experimental design tests three personas (short, medium, and long-term investors) and two ensemble methods (mode and sensitive) across 593 weekdays from October 2021 to January 2024. The investment strategy adjusts position sizes based on predictions, comparing against baselines like buy-and-hold, continuous movement, and regression models. Performance is evaluated using Sharpe ratio, return, volatility, and maximum drawdown, with further analysis stratified by CPI trends to identify specific market conditions where LLMs excel.

Results indicate that the mode ensemble across personas significantly improves prediction accuracy and F1-scores for detecting market declines, achieving a recall of 0.674 for downward movements. In terms of investment performance, LLM-based strategies outperform buy-and-hold in Sharpe ratio during periods of rising CPI, leveraging the model's knowledge to recognize broader trends beyond short-term noise. However, traditional strategies prove more effective during declining CPI trends or sharp market downturns, where LLMs sometimes respond too slowly. The study concludes that while LLMs enhance portfolio management, they require complementary strategies to optimize performance across varying market regimes, highlighting the value of persona-based ensembles in capturing diverse investment rationales.

## FinRobot: AI Agent for Equity Research and Valuation with Large Language Models

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, earnings analysis, equities, us equities, multi-agent systems, chain of thought, sec filings, earnings calls, tables, accuracy, open source, framework, trading agent, hallucination, valuation modeling, dcf, expert evaluation
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "earnings calls", "tables"], "deliverable": ["open source", "framework", "trading agent"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["multi-agent systems", "chain of thought"], "risk_issue": ["hallucination"], "task": ["equity research", "earnings analysis"]}
- One-line summary: FinRobot is an open-source multi-agent LLM framework that automates equity research by integrating quantitative data processing, conceptual reasoning, and narrative synthesis to generate professional-grade investment reports.

### Detailed Summary

The paper addresses the limitations of existing automated financial tools, which often lack the discretionary judgment and real-time adaptability of human sell-side analysts. It introduces FinRobot, the first AI agent framework specifically designed for comprehensive equity research. The system aims to bridge the gap between narrow technical analysis and the nuanced, qualitative reasoning required for robust investment decisions, offering a solution that can dynamically update with new financial information and provide realistic risk assessments comparable to major brokerage firms.

FinRobot employs a multi-agent Chain of Thought (CoT) architecture comprising three specialized agents: the Data-CoT Agent, which aggregates and structures diverse data sources including SEC filings, earnings transcripts, and alternative data; the Concept-CoT Agent, which mimics analyst reasoning to derive actionable insights and financial metrics like EBITDA and ROIC; and the Thesis-CoT Agent, which synthesizes these findings into a coherent investment thesis and report. The methodology integrates quantitative calculations with qualitative storytelling, utilizing a dynamic data pipeline to ensure timeliness. Experiments were conducted on Waste Management, Inc., generating a full equity research report evaluated by a panel of investment banking analysts.

The system was evaluated on accuracy, logicality, and storytelling, receiving high scores from expert reviewers who noted the precision of financial data and the professional structure of the output. Key findings include the ability to generate detailed competitor analyses, valuation models (DCF), and risk assessments. However, limitations include occasional unnatural phrasing, a tendency to read like a list of statistics rather than a compelling narrative, and the need for human oversight in complex qualitative judgments. The open-source release democratizes access to advanced AI-driven research tools.

## FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: infrastructure
- Summary coverage: first_50k_chars
- Tags: equity research, sentiment analysis, financial question answering, equities, us equities, agentic workflow, chain of thought, tool use, multi-agent systems, sec filings, news, social media, tables, framework, open source, trading agent, hallucination, privacy, infrastructure, llm integration
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "social media", "tables"], "deliverable": ["framework", "open source", "trading agent"], "evaluation": [], "market_context": ["us equities"], "method": ["agentic workflow", "chain of thought", "tool use", "multi-agent systems"], "risk_issue": ["hallucination", "privacy"], "task": ["equity research", "sentiment analysis", "financial question answering"]}
- One-line summary: FinRobot is an open-source AI agent platform that integrates multi-source LLMs, financial Chain-of-Thought prompting, and a Smart Scheduler to automate complex financial analysis tasks such as equity research and market forecasting.

### Detailed Summary

The paper addresses the barrier between proprietary financial data and AI capabilities by introducing FinRobot, an open-source platform designed to democratize access to advanced financial AI tools. It aims to solve challenges in transparency, global market adaptation, model diversity, and real-time data processing by providing a comprehensive framework for financial AI agents. The platform is positioned to enhance financial decision-making by combining specialized LLMs with structured reasoning techniques, making sophisticated analysis accessible to both professionals and laypersons.

FinRobot’s architecture consists of four layers: Financial AI Agents, Financial LLM Algorithms, LLMOps/DataOps, and Multi-source LLM Foundation Models. Key methods include Financial Chain-of-Thought (CoT) prompting to break down complex problems, a Smart Scheduler for dynamic model selection among diverse LLMs (e.g., Llama, GPT, FinGPT), and Retrieval-Augmented Generation (RAG) for data integration. The system employs multi-agent workflows with roles like Director, Assistant, and Analysts, utilizing tools for API interaction (Text2Params) and code generation (Text2Code). Experiments demonstrate the platform's ability to generate detailed equity research reports for companies like NVIDIA and Kweichow Moutai, integrating financial statements, news, and market data.

The platform enables end-to-end financial analysis, from data perception to report generation, supporting tasks like sentiment analysis, valuation, and risk assessment. It highlights the utility of multi-agent collaboration and CoT in improving interpretability and accuracy. Limitations include the reliance on open-source models which may lack the depth of proprietary systems, and the need for careful validation of generated insights. The paper emphasizes that while it supports trading-related analysis, its primary contribution is the infrastructure for financial AI agents rather than direct alpha generation strategies.

## The Structure of Financial Equity Research Reports

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: equity research, sentiment analysis, equities, institutional investing, retrieval, 10-k filings, annual reports, sec filings, accuracy, benchmark, dataset, framework, bias, automation potential, ensemble learning, text extraction, analyst workflow
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "annual reports", "sec filings"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["retrieval"], "risk_issue": ["bias"], "task": ["equity research", "sentiment analysis"]}
- One-line summary: This study quantifies the automation potential of equity research reports by mapping 4,964 sentences into 169 question archetypes, finding that 75% are automatable via text extraction or database queries, with LLMs successfully automating approximately 80% of statements when used in an ensemble.

### Detailed Summary

The paper addresses the lack of empirical analysis on the content structure of financial equity research reports (ERRs) and the specific questions analysts answer. It aims to quantify the portion of ERR writing that can be automated by large language models versus human judgment. The authors argue that understanding the frequency and extractability of information is crucial for designing automated systems that can assist or replace parts of the analyst workflow, particularly given the known biases and inefficiencies in traditional human-driven reporting.

The methodology involves a manual, sentence-by-sentence analysis of 72 ERRs from 23 providers, deriving 169 unique question archetypes without pre-defined categories. These questions are classified by extractability (text-extractable, database-extractable, or non-extractable) using public corporate reports and financial databases. To validate automation potential, the authors test Llama-3-70B and GPT-4-turbo on 200 example questions, measuring their ability to extract answers from annual reports. They also conduct expert interviews to verify the relevance of the question list and assess the role of human judgment in areas like management quality assessment.

Results show that 75.15% of questions in ERRs are automatable, with 51.91% being text-extractable and 24.24% database-extractable. Only 24.85% require human judgment, primarily in the 'Analysis' category (recommendations, target prices). Empirical tests reveal that Llama-3-70B and GPT-4 complement each other well, with an ensemble achieving an 84% success rate on extractable questions. The study concludes that significant automation is feasible, especially for factual reporting, but highlights limitations such as the inability of current models to handle complex, multi-source synthesis and the potential for out-of-distribution questions not captured in the sample.

## FinRpt: Financial Report Understanding and Generation Benchmark

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, stock prediction, equities, china market, multi-agent systems, fine-tuning, reinforcement learning, financial statements, news, market prices, accuracy, ablation study, benchmark, dataset, framework, open source, hallucination, equity research report generation, chinese equities, llm judging
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "news", "market prices"], "deliverable": ["benchmark", "dataset", "framework", "open source"], "evaluation": ["accuracy", "ablation study"], "market_context": ["china market"], "method": ["multi-agent systems", "fine-tuning", "reinforcement learning"], "risk_issue": ["hallucination"], "task": ["equity research", "stock prediction"]}
- One-line summary: This paper introduces FinRpt, a benchmark and multi-agent framework for Equity Research Report generation, demonstrating that fine-tuned agents outperform single LLMs in producing professional, accurate financial reports.

### Detailed Summary

The paper addresses the lack of automated Equity Research Report (ERR) generation by formally defining the task and creating the FinRpt benchmark. It tackles data scarcity and evaluation gaps by constructing a dataset of 6,825 high-quality ERRs from 800 Chinese stocks, integrating seven data types including financial statements, news, and market indices. The authors propose a comprehensive evaluation system with 11 metrics, covering basic text similarity and specialized financial professionalism aspects like numeric accuracy and risk analysis, filling a critical void in existing financial NLP benchmarks.

Methodologically, the authors develop FinRpt-Gen, a multi-agent framework decomposing report generation into nine specialized agents for information extraction, analysis, and prediction. The pipeline involves Supervised Fine-Tuning (SFT) using LoRA on four core agents and Reinforcement Learning (RL) via the DAPO algorithm to optimize the prediction agent’s alignment with investment objectives. Experiments compare this framework against standalone LLMs and other baselines, utilizing both automated metrics and LLM-based pairwise evaluations to assess semantic quality and financial logic across the generated reports.

Results show that FinRpt-Gen with SFT and RL significantly outperforms single LLMs, achieving a 55% accuracy in recommendation ratings and superior scores in financial numeric and news analysis metrics compared to GPT-4o. The dataset quality is validated through human evaluation, showing high consistency with expert-written reports. However, the study is limited to the Chinese market (CSI800) and a short time window, raising questions about generalizability to other markets or longer horizons. The work provides a foundational tool for automating analyst workflows but requires further validation on cross-market applicability and real-time trading integration.

## Task-Adaptive Large Language Models to Generate Human-Persuasive Investment Reports

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: earnings analysis, sentiment analysis, investment advisory, equities, earnings season, prompt engineering, earnings calls, backtest, framework, look-ahead bias, human evaluation, conviction scoring, position sizing, investor psychology
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls"], "deliverable": ["framework"], "evaluation": ["backtest"], "market_context": ["earnings season"], "method": ["prompt engineering"], "risk_issue": ["look-ahead bias"], "task": ["earnings analysis", "sentiment analysis", "investment advisory"]}
- One-line summary: This paper presents a two-stage task-adaptive LLM framework that combines granular sentiment extraction with a six-dimensional cognitive reasoning model to generate persuasive investment reports from earnings call transcripts, achieving top rankings in the FinNLP 2025 Earnings2Insights shared task.

### Detailed Summary

The paper addresses the challenge of generating investment reports from earnings call transcripts that are not only factually accurate but also persuasive enough to guide human investment decisions across different time horizons. It positions this task within the FinNLP 2025 Earnings2Insights shared task, highlighting the limitation of traditional metrics that prioritize content similarity over decision-making effectiveness. The research aims to bridge the gap between automated text generation and real-world financial analysis by incorporating investor psychology and multi-perspective reasoning into the LLM pipeline.

The proposed method is a two-stage framework using GPT-4o. Stage one acts as a 'Data Extractor,' employing an 8-category sentiment classification system to analyze Q&A pairs for tone, confidence, and evasion, outputting structured signals. Stage two acts as a 'Cognitive Reasoner,' utilizing a six-dimensional analysis framework (financial performance, business fundamentals, risk, outlook, personal factors, and conviction scoring) to synthesize the extracted data. The system explicitly models investor personalities to tailor recommendations for growth, risk-aware, and other profiles, providing conviction scores and position sizing advice for 1-day, 1-week, and 1-month horizons.

Experiments were conducted on 64 earnings call transcripts from the shared task dataset. The system ranked 1st out of 12 teams in human-evaluation average Likert scores and 2nd in automated Likert scores. It achieved a win rate of 0.881 against professional analyst reports. The results demonstrate that integrating sentiment nuance and investor personality modeling significantly enhances the persuasiveness and utility of AI-generated reports. Limitations include reliance on GPT-4o's capabilities and the subjective nature of human evaluation, though the framework offers a robust template for decision-oriented financial NLP.

## FinSphere: A Conversational Stock Analysis Agent based on Large Language Models

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, equity research, equities, portfolio management, instruction tuning, chain of thought, tool use, agentic workflow, financial statements, market prices, accuracy, dataset, framework, model, open source, model risk, stock analysis, expert evaluation, real-time data, quantitative tools
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "market prices"], "deliverable": ["dataset", "framework", "model", "open source"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["instruction tuning", "chain of thought", "tool use", "agentic workflow"], "risk_issue": ["model risk"], "task": ["stock prediction", "equity research"]}
- One-line summary: FinSphere is a real-time stock analysis agent that integrates proprietary quantitative tools with an instruction-tuned LLM, achieving superior expert-rated analytical quality compared to general and domain-specific baselines.

### Detailed Summary

The paper addresses the critical gap in financial LLMs regarding the lack of objective evaluation metrics for stock analysis reports and the insufficient depth of insights generated by existing models. The authors argue that current systems struggle to synthesize complex, real-time financial data into professional-grade reports, often relying on static historical knowledge or shallow reasoning. To solve this, they introduce a comprehensive framework designed to enhance both the evaluation and generation of stock analysis, positioning their solution as a bridge between automated data processing and expert-level financial reasoning.

The core contribution is FinSphere, an agent that decomposes user queries into subtasks using chain-of-thought reasoning and executes them via specialized quantitative tools connected to a real-time financial database. These tools provide structured background information on technical indicators, capital flows, and fundamentals. The agent's LLM backbone, Qwen2-72B, is fully instruction-tuned on Stocksis, a novel dataset of 5,000 expert-curated training pairs consisting of tool outputs and refined expert analyses. Evaluation is conducted using AnalyScore, a multi-dimensional framework assessing conclusion, content, expression, and data usage, with human experts scoring 100 model responses across various baselines.

Experiments demonstrate that FinSphere achieves the highest AnalyScore (70.88/100) among all tested models, outperforming GPT-4o, FinMem, and FinRobot. The ablation study reveals a strong positive correlation between the volume of Stocksis training data and performance, highlighting the importance of high-quality, expert-refined supervision. The system effectively combines real-time data access with structured analytical reasoning, producing coherent and actionable reports. However, the reliance on proprietary tools and the high cost of expert curation present deployment challenges, and the evaluation remains subjective despite high inter-annotator agreement.


## Finance Agent Benchmark: Evaluating Language Model Agents as Financial Assistants

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, financial question answering, equities, institutional investing, agentic workflow, tool use, retrieval, sec filings, accuracy, benchmark, dataset, hallucination, llm-as-judge, cost-accuracy trade-off, tool usage analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["agentic workflow", "tool use", "retrieval"], "risk_issue": ["hallucination"], "task": ["equity research", "financial question answering"]}
- One-line summary: The Finance Agent Benchmark evaluates 20 LLMs on 537 expert-authored financial research tasks requiring tool use, revealing that even the best model (o3) achieves only 46.8% accuracy, highlighting significant gaps in autonomous financial analysis capabilities.

### Detailed Summary

This paper addresses the critical need for robust, domain-specific benchmarks to evaluate Large Language Model (LLM) agents in real-world financial analysis. It argues that previous benchmarks fail to capture the interactive, multi-step reasoning and tool-use requirements of industry tasks, leaving performance in high-stakes financial settings uncertain. The authors introduce the Finance Agent Benchmark, constructed in consultation with experts from banks, hedge funds, and private equity firms, to provide a standardized testbed for measuring the progress of LLM-driven finance agents.

The benchmark comprises 537 expert-authored questions across nine task categories, ranging from simple quantitative retrieval to complex financial modeling and market analysis. Questions are grounded in recent SEC filings (post-2024) to prevent data contamination. The authors developed an agentic evaluation harness equipped with tools including Google Search, EDGAR database access, HTML parsing, and information retrieval. Evaluation employs a refined LLM-as-judge methodology with rubric-based assessment and contradiction detection to ensure accurate grading of multi-step reasoning trajectories.

Experiments on 20 models reveal that current AI capabilities are significantly limited for autonomous financial tasks. The best-performing model, OpenAI o3, achieved only 46.8% class-balanced accuracy, with no model surpassing 50%. A clear logarithmic relationship exists between cost and accuracy, with diminishing returns beyond $1 per query. While models are significantly faster and cheaper than human experts (avg $3.79 vs $25.66), the low accuracy underscores the need for further advancements before reliable deployment in high-stakes finance. The study also analyzes tool usage patterns, finding that more exploratory models tend to perform better, while high tool usage without precision leads to failure.

## A Preliminary Look at the State of the Art of Large Language Models on Chartered Financial Analyst Exams

- Year: 2024
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, equity research, equities, portfolio management, chain of thought, financial statements, accuracy, benchmark, hallucination, cfa exam, professional certification, essay evaluation, instruction following
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements"], "deliverable": ["benchmark"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["chain of thought"], "risk_issue": ["hallucination"], "task": ["benchmarking", "equity research"]}
- One-line summary: This paper benchmarks 14 LLMs on CFA exams, finding that proprietary models pass Levels I and II but fail Level III essays, while open-source models like LLaMA 3 70B can pass Levels I and II with RAG assistance.

### Detailed Summary

The paper addresses the evaluation of large language models' financial analysis capabilities by benchmarking them against the Chartered Financial Analyst (CFA) program, a rigorous professional certification. It positions LLMs as potential tools for automating investment research and analysis, aiming to determine if current models meet the standards of human professionals. The study covers the full spectrum of CFA exams, from basic concept memorization in Level I to complex case analysis and essay writing in Level III, providing a comprehensive view of LLM strengths and weaknesses in high-stakes financial environments.

The authors evaluate five proprietary and nine open-source models using mock CFA exams from AnalystPrep, ensuring low contamination risk. Experiments employ one-shot chain-of-thought prompting for multiple-choice questions and a model-assisted human evaluation strategy for Level III essays. The study also investigates Retrieval-Augmented Generation (RAG) using CFA textbooks to assess if external knowledge can bridge performance gaps. Metrics include accuracy for MCQs and a weighted score combining MCQ and essay marks for Level III, with ablation studies on shot count and temperature.

Proprietary models like GPT-4o and Claude 3 Opus consistently outperform open-source counterparts, passing Levels I and II but failing Level III due to poor essay performance. Open-source models, particularly LLaMA 3 70B, show strong potential; with RAG, LLaMA 3 70B can pass Levels I and II under lower passing score bounds. However, RAG benefits diminish at higher levels, and open-source models struggle with instruction following and nuance. The paper highlights that while LLMs are proficient in knowledge retrieval and calculation, they lack the professional judgment and structured reasoning required for advanced portfolio management decisions.

## Advanced Financial Reasoning at Scale: Large Language Models on Chartered Financial Analyst Level III

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, equity research, portfolio optimization, equities, derivatives, options, institutional investing, portfolio management, chain of thought, prompt engineering, financial statements, accuracy, benchmark, dataset, bias, cfa exam, llm-as-a-judge, cost-latency trade-off, reasoning models
- Tag facets: {"asset_class": ["equities", "derivatives", "options"], "data_source": ["financial statements"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing", "portfolio management"], "method": ["chain of thought", "prompt engineering"], "risk_issue": ["bias"], "task": ["benchmarking", "equity research", "portfolio optimization"]}
- One-line summary: This paper benchmarks 23 LLMs on CFA Level III exams, showing that frontier reasoning models like o4-mini pass the mock exam with 79.1% accuracy, though significant cost-latency trade-offs and human-LLM grading discrepancies persist.

### Detailed Summary

The paper addresses the critical need for rigorous, domain-specific evaluation of Large Language Models in high-stakes financial settings. It positions the Chartered Financial Analyst (CFA) Level III exam as a gold-standard benchmark for advanced financial reasoning, moving beyond general knowledge to test synthesis, strategic thinking, and professional judgment. The study aims to determine if current state-of-the-art models can meet the cognitive demands of professional investment management and wealth planning, filling a gap left by previous evaluations that focused on easier Levels I and II.

The methodology involves constructing a dataset of mock CFA Level III exams, including 60 multiple-choice questions (MCQs) and 43 essay questions derived from AnalystPrep materials. The authors evaluate 23 diverse LLMs, spanning frontier proprietary models, open-source variants, and specialized financial models. They employ three prompting strategies: zero-shot, Chain-of-Thought with Self-Consistency (CoT-SC), and Self-Discover. Evaluation includes automated LLM-as-a-judge grading and human-expert grading by certified CFA graders to assess alignment. Metrics cover accuracy, latency, cost, and semantic similarity.

Key findings indicate that frontier reasoning models, particularly o4-mini (79.1%) and Gemini 2.5 Flash (77.3%), exceed the 65% passing threshold. While MCQ performance converges across top models, essay scores show greater variance, highlighting the difficulty of complex synthesis. Chain-of-Thought prompting significantly improves performance but increases costs by up to 11x. The study also reveals a systematic bias where human graders are more lenient than LLM judges, awarding an average of 5.6 points higher. These results suggest a tiered deployment strategy is optimal, using smaller models for routine tasks and frontier models for complex analysis, while cautioning against over-reliance on automated grading for subjective financial reasoning.

## Can Large Language Models Tackle the Chartered Financial Analyst Exam?

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, equity research, equities, etfs, mutual funds, portfolio management, retrieval, financial statements, accuracy, benchmark, dataset, hallucination, cfa exam, professional certification, tiered deployment
- Tag facets: {"asset_class": ["equities", "etfs", "mutual funds"], "data_source": ["financial statements"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["benchmarking", "equity research"]}
- One-line summary: This study benchmarks GPT-4o, GPT-o1, and o3-mini on 1,560 CFA mock exam questions, demonstrating that reasoning-specialized models like GPT-o1 excel in financial analysis and that a novel domain-specific RAG pipeline significantly improves accuracy, particularly for complex, knowledge-intensive tasks.

### Detailed Summary

The paper addresses the need for rigorous evaluation of Large Language Models (LLMs) in specialized financial contexts, moving beyond general NLP tasks to professional certification standards. It positions the Chartered Financial Analyst (CFA) exam as a proxy for real-world financial analysis complexity, requiring integrated reasoning, quantitative precision, and domain knowledge. The study aims to assess intrinsic model capabilities and the efficacy of Retrieval-Augmented Generation (RAG) in bridging knowledge gaps, providing actionable insights for model selection and deployment in high-stakes financial environments.

The methodology involves evaluating three distinct model types—GPT-4o (multimodal/generalist), GPT-o1 (reasoning-specialized), and o3-mini (lightweight/efficient)—on 1,560 multiple-choice questions from CFA Levels I-III. The authors implement a zero-shot baseline and a novel domain reasoning RAG pipeline that uses hierarchical knowledge organization and structured query generation to retrieve relevant content from official CFA curriculum materials. The RAG system employs a two-stage process: generating targeted summaries and keywords for precise retrieval, followed by context-augmented reasoning. Performance is measured against estimated passing criteria, with detailed error analysis categorizing failures into knowledge gaps, reasoning errors, calculation inaccuracies, and inconsistencies.

Results show that GPT-o1 consistently outperforms other models in zero-shot settings, achieving high accuracy across all levels, while o3-mini offers a cost-effective alternative with strong performance on foundational topics. The RAG pipeline provides substantial improvements, particularly for Level III questions and complex scenarios, with gains up to 8.64% for GPT-o1. Error analysis reveals that knowledge gaps are the primary failure mode, accounting for over 60% of errors, while calculation errors remain a persistent challenge, especially for GPT-4o. The study concludes that retrieval augmentation is indispensable for fact-heavy conceptual judgment, but deterministic verification layers are needed for quantitative tasks, suggesting a tiered deployment strategy based on task complexity and cost-performance trade-offs.

## FinBERT: Financial Sentiment Analysis with Pre-trained Language Models

- Year: 2019
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, fine-tuning, domain adaptation, news, social media, accuracy, model, finbert, bert, transfer learning, nlp, financial phrasebank, fiqa
- Tag facets: {"asset_class": [], "data_source": ["news", "social media"], "deliverable": ["model"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "domain adaptation"], "risk_issue": [], "task": ["sentiment analysis"]}
- One-line summary: FinBERT, a BERT-based language model further pre-trained on financial text, achieves state-of-the-art performance in financial sentiment analysis on the Financial PhraseBank and FiQA datasets, significantly outperforming traditional machine learning and other transfer learning baselines like ULMFit and ELMo.

### Detailed Summary

Financial sentiment analysis faces challenges due to specialized domain language and scarce labeled data, rendering general-purpose models ineffective. This paper introduces FinBERT, a BERT-based model designed to address these issues by leveraging transfer learning. The core hypothesis is that pre-training on large corpora reduces the need for extensive labeled data and allows for effective fine-tuning on domain-specific texts. The research positions FinBERT as a solution to the limitations of lexicon-based methods and standard deep learning models that struggle with semantic nuance in financial contexts.

The methodology involves further pre-training BERT on a financial corpus (TRC2-financial) and fine-tuning it for classification and regression tasks. Experiments utilize the Financial PhraseBank for three-class sentiment classification and the FiQA dataset for continuous sentiment scoring. The study compares FinBERT against LSTM classifiers with GloVe/ELMo embeddings and ULMFit. Key experimental designs include investigating the impact of further pre-training, training strategies to prevent catastrophic forgetting (slanted triangular learning rates, discriminative fine-tuning, gradual unfreezing), and analyzing which encoder layers contribute most to performance. Metrics include accuracy, F1 score, MSE, and R2.

FinBERT achieves state-of-the-art results, improving accuracy by 15% on Financial PhraseBank and lowering MSE on FiQA compared to prior works. The model demonstrates robustness even with small training sets (250 examples). However, further pre-training on the domain corpus showed marginal gains over vanilla BERT, likely due to high baseline performance. The model struggles with distinguishing neutral statements from positive/negative ones, particularly when implicit sentiment or numerical comparisons are involved. These findings suggest FinBERT is highly effective for explicit sentiment extraction but may require additional context for implicit financial signals.

## A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, stock prediction, crypto, equities, portfolio management, agentic workflow, multimodal modeling, retrieval, tool use, market prices, news, portfolio returns, sharpe ratio, framework, trading agent, overfitting, technical indicators, reflection mechanism, memory retrieval
- Tag facets: {"asset_class": ["crypto", "equities"], "data_source": ["market prices", "news"], "deliverable": ["framework", "trading agent"], "evaluation": ["portfolio returns", "sharpe ratio"], "market_context": ["portfolio management"], "method": ["agentic workflow", "multimodal modeling", "retrieval", "tool use"], "risk_issue": ["overfitting"], "task": ["algorithmic trading", "stock prediction"]}
- One-line summary: FinAgent is a multimodal LLM-based trading agent that integrates news, prices, and charts via a dual-level reflection mechanism and tool-augmented decision-making, significantly outperforming baselines in profit across stock and crypto markets.

### Detailed Summary

Financial trading requires processing diverse, multimodal data and adapting to rapid market dynamics, yet existing AI agents often struggle with generalizability and the integration of visual and textual information. The authors address these gaps by proposing FinAgent, a multimodal foundation agent designed to handle numerical, textual, and visual market intelligence. The system aims to bridge the gap between simple question-answering LLMs and complex sequential decision-making in trading by incorporating reasoning, memory, and tool use to enhance trust and adaptability in volatile environments.

FinAgent employs a five-module architecture: a market intelligence module for summarizing news and prices, a diversified memory retrieval system to store and fetch relevant historical insights, and a dual-level reflection module. The low-level reflection analyzes price movements against market intelligence, while the high-level reflection evaluates past trading decisions to learn from successes and mistakes. The decision-making module integrates these insights with expert guidance and technical indicators (e.g., MACD, KDJ) to generate buy, sell, or hold actions. Experiments were conducted on six financial datasets, including stocks and cryptocurrencies, comparing FinAgent against 12 state-of-the-art baselines such as FinGPT, FinMem, and reinforcement learning methods like SAC and DQN.

FinAgent achieved an average profit improvement of over 36% across six financial metrics and secured a 92.27% return on one dataset, significantly outperforming all baselines. The agent demonstrated superior ability to capitalize on market trends and avoid losses compared to models that failed to adapt to volatility or misinterpreted news. However, limitations include the reliance on specific prompt engineering for reasoning, potential sensitivity to the quality of retrieved historical data, and the computational overhead of multimodal processing. The study highlights the value of structured reflection and tool augmentation in enhancing LLM-based trading agents.

## XuanYuan 2.0: A Large Chinese Financial Chat Model with Hundreds of Billions Parameters

- Year: 2023
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, fine-tuning, instruction tuning, multimodal modeling, news, social media, model, open source, bias, chinese language, chatbot, catastrophic forgetting, self-instruct, infrastructure
- Tag facets: {"asset_class": [], "data_source": ["news", "social media"], "deliverable": ["model", "open source"], "evaluation": [], "market_context": [], "method": ["fine-tuning", "instruction tuning", "multimodal modeling"], "risk_issue": ["bias"], "task": ["financial question answering"]}
- One-line summary: XuanYuan 2.0 is a 176-billion parameter Chinese financial chat model built on BLOOM-176B that utilizes a novel hybrid-tuning method to integrate general and financial knowledge while mitigating catastrophic forgetting.

### Detailed Summary

The paper addresses the scarcity of open-source, large-scale language models specifically designed for the Chinese financial domain. While general-purpose models like GPT-4 and BLOOM exist, and smaller domain-specific models like FinBERT are available, there is a gap in high-parameter chat models capable of handling complex Chinese financial queries. The authors position XuanYuan 2.0 as the largest Chinese chat model to date, aiming to provide accurate, contextually appropriate responses in financial scenarios by leveraging both general linguistic capabilities and specialized financial knowledge.

The core contribution is the model architecture and the proposed hybrid-tuning training framework. Built on the BLOOM-176B decoder-only architecture, the model is trained using a novel hybrid-tuning method that interleaves general pre-training, financial pre-training, and instruction tuning in a single stage. This approach uses crawled internet data for general pre-training, and a mix of unstructured (news, reports) and structured financial data for domain-specific instruction generation via Self-Instruct and Self-QA. The training leverages DeepSpeed and pipeline parallelism on NVIDIA A100 GPUs to manage the 176B parameters. Experiments compare XuanYuan 2.0 against other open-source Chinese conversational models, evaluating performance on manually assessed datasets covering general and financial dimensions.

The findings indicate that XuanYuan 2.0 possesses a robust knowledge base and strong conversational capabilities in the Chinese financial domain, outperforming smaller predecessors. The hybrid-tuning method effectively mitigates catastrophic forgetting, allowing the model to retain general language skills while acquiring financial expertise. However, the paper notes that detailed quantitative evaluation rankings and further insights will be presented in a future version. Limitations include the reliance on manual assessment for current results and the need for continuous data gathering to optimize the model further. The model is primarily a foundational resource for Chinese financial NLP rather than a direct trading tool.

## Advancing Financial Engineering with Foundation Models: Progress, Applications, and Challenges

- Year: 2025
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, equities, institutional investing, reinforcement learning, fine-tuning, instruction tuning, domain adaptation, sec filings, news, accuracy, taxonomy, dataset, literature review, regulatory compliance, privacy, multimodal modeling, time-series modeling, foundation models
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news"], "deliverable": ["taxonomy", "dataset", "literature review"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["reinforcement learning", "fine-tuning", "instruction tuning", "domain adaptation"], "risk_issue": ["regulatory compliance", "privacy"], "task": ["sentiment analysis", "stock prediction"]}
- One-line summary: This survey systematically categorizes financial foundation models into language, time-series, and visual-language types, reviewing their architectures, training strategies, datasets, and applications while identifying key challenges in data, algorithms, and infrastructure.

### Detailed Summary

The paper addresses the gap in general-purpose foundation models regarding the unique domain requirements of financial engineering, such as multimodal reasoning, regulatory compliance, and data privacy. It introduces a comprehensive taxonomy of Financial Foundation Models (FFMs), distinguishing between Financial Language Foundation Models (FinLFMs), Financial Time-Series Foundation Models (FinTSFMs), and Financial Visual-Language Foundation Models (FinVLFMs). The authors aim to provide a unified view of the FFM landscape, covering progress from 2018 to 2025, and serve as a reference for researchers and practitioners navigating this rapidly evolving field.

The methodology involves a systematic literature review and categorization of 21 representative FinLFMs, along with an overview of emerging FinTSFMs and FinVLFMs. The authors analyze training pipelines including pre-training, supervised fine-tuning, and alignment techniques like reinforcement learning for reasoning. They survey a wide range of datasets, from early task-specific English corpora to recent multi-task, cross-lingual benchmarks like AlphaFin and FinBen. The review also examines real-world applications, including sentiment analysis, stock prediction, and regulatory compliance checking, while highlighting the shift from BERT-style encoders to GPT-style generative models and reasoning-enhanced agents.

Key findings indicate that FinLFMs have matured significantly through instruction tuning and alignment, with models like BloombergGPT and FinGPT demonstrating strong domain adaptation. However, FinTSFMs remain in early stages due to the non-stationary nature of financial time series. The paper identifies critical challenges in data availability, algorithmic scalability, and infrastructure constraints. It emphasizes the need for robust evaluation benchmarks and regulatory-compliant alignment. The survey concludes by offering a roadmap for future research, stressing the importance of multimodal integration and autonomous financial agents, while noting that current models still struggle with complex temporal dynamics and strict privacy requirements.

## InvestLM: A Large Language Model for Investment using Financial Domain Instruction Tuning

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: investment advisory, sentiment analysis, financial question answering, institutional investing, fine-tuning, instruction tuning, sec filings, financial statements, accuracy, model, dataset, open source, hallucination, domain adaptation, expert evaluation
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "financial statements"], "deliverable": ["model", "dataset", "open source"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["hallucination"], "task": ["investment advisory", "sentiment analysis", "financial question answering"]}
- One-line summary: InvestLM is a 65B parameter financial LLM instruction-tuned on a curated dataset of ~1,300 high-quality examples, demonstrating expert-rated performance comparable to GPT-3.5/4 and strong generalization across financial NLP benchmarks.

### Detailed Summary

This paper addresses the lack of accessible, high-performance open-source financial LLMs by introducing InvestLM, a model instruction-tuned on LLaMA-65B. The authors challenge the assumption that massive instruction datasets are necessary for domain alignment, instead leveraging the Superficial Alignment Hypothesis to curate a small, diverse, and manually verified dataset. The research problem centers on creating a model that not only understands financial text but also provides actionable, logical investment advice without the hallucinations common in base foundation models or the vagueness of commercial safety-aligned models.

The methodology involves constructing a 1,335-example instruction dataset sourced from CFA exams, StackExchange QuantFinance, academic journals, textbooks, SEC filings, and financial NLP tasks. The model is fine-tuned using LoRA with linear rope scaling to handle long contexts. Evaluation includes expert reviews by hedge fund managers and analysts comparing InvestLM against GPT-3.5, GPT-4, and Claude-2 on investment scenarios, as well as zero-shot testing on nine financial NLP benchmarks including sentiment analysis, numerical reasoning (FinQA), and summarization. The study also ablates the impact of adding generic Alpaca instructions to the domain-specific dataset.

Findings indicate that InvestLM’s responses are rated comparable to or better than GPT-3.5 and GPT-4 by financial experts, particularly in providing concise, decisive advice. On benchmarks, InvestLM outperforms LLaMA-65B in 8 of 9 tasks and achieves state-of-the-art results on FinSent and FiQA. Crucially, the study finds that adding generic instructions (Alpaca) degrades performance on domain tasks, supporting the 'less-is-more' hypothesis for domain alignment. The model significantly reduces hallucinations compared to the base LLaMA model, though it remains a research tool rather than a direct trading system.

## FinBERT: A Pretrained Language Model for Financial Communications

- Year: 2020
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, earnings analysis, equities, us equities, fine-tuning, domain adaptation, 10-k filings, earnings calls, sec filings, accuracy, model, open source, pretraining
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "earnings calls", "sec filings"], "deliverable": ["model", "open source"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["fine-tuning", "domain adaptation"], "risk_issue": [], "task": ["sentiment analysis", "earnings analysis"]}
- One-line summary: FinBERT is a domain-specific BERT model pretrained on 4.9 billion tokens of financial text that significantly outperforms generic BERT on financial sentiment classification tasks.

### Detailed Summary

This paper addresses the lack of pretrained language models tailored for the financial domain, where generic models like BERT often underperform due to the specialized nature of financial language. The authors argue that sentiment analysis is highly domain-dependent and that leveraging large-scale financial communication corpora can yield superior representations for downstream tasks such as market sentiment monitoring and trading signal generation. By pretraining on financial-specific data, the model aims to capture nuances in corporate reports, earnings calls, and analyst opinions that general models miss.

The core method involves pretraining FinBERT, a BERT-Base architecture, on a novel corpus of 4.9 billion tokens comprising SEC 10-K/10-Q filings, earnings call transcripts, and analyst reports. The authors introduce a custom financial vocabulary (FinVocab) and train both cased and uncased variants. Experiments evaluate the model on three financial sentiment classification benchmarks: Financial PhraseBank, AnalystTone, and FiQA. The fine-tuning strategy uses a standard linear classification layer with cross-entropy loss, comparing FinBERT against the original generic BERT-Base model to isolate the impact of domain-specific pretraining.

Results demonstrate that FinBERT consistently outperforms generic BERT across all three sentiment tasks, with accuracy improvements ranging from 4.4% to 29.2% depending on the dataset and model variant. The uncased FinBERT with FinVocab generally achieves the best performance. The study finds that while a custom vocabulary helps, the primary driver of performance gain is the domain-specific pretraining data itself. The authors conclude that FinBERT provides a robust foundation for various financial NLP applications beyond sentiment, including stock return prediction and fraud detection, and release the code and models for public use.

## Towards Competent AI for Fundamental Analysis in Finance: A Benchmark Dataset and Evaluation

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, earnings analysis, xbrl tagging, equities, china market, backtesting, retrieval, annual reports, xbrl, sec filings, accuracy, benchmark, dataset, hallucination, financial statement analysis, fundamental analysis, table extraction, logical reasoning, indicator computation
- Tag facets: {"asset_class": ["equities"], "data_source": ["annual reports", "xbrl", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["backtesting", "retrieval"], "risk_issue": ["hallucination"], "task": ["benchmarking", "earnings analysis", "xbrl tagging"]}
- One-line summary: The paper introduces FinAR-Bench, a benchmark evaluating LLMs on financial statement analysis through information extraction, indicator computation, and logical reasoning, revealing that while large models excel at extraction, they struggle with precise numerical calculation despite improved reasoning capabilities.

### Detailed Summary

This paper addresses the gap in evaluating LLMs for real-world fundamental analysis tasks, specifically focusing on financial statement analysis, which is critical for investment decisions and credit risk assessment. The authors argue that existing benchmarks primarily test question-answering or general financial knowledge, failing to capture the multi-step, structured nature of generating accurate financial reports. To address this, they propose FinAR-Bench, a dataset designed to decompose financial statement analysis into three verifiable subtasks: extracting key financial items, calculating specific financial indicators, and applying logical reasoning to interpret trends. This structured approach allows for objective assessment of each component, providing a more granular view of LLM capabilities in a high-stakes financial context.

The dataset comprises financial statement data from 100 companies listed on the Shanghai Stock Exchange for fiscal years 2022 and 2023, sourced from both structured XBRL formats and unstructured PDF annual reports. The authors evaluate 14 diverse LLMs, ranging from small open-source models to large proprietary ones like GPT-4o and GPT-o1. The evaluation protocol includes a novel RMS metric for assessing table extraction accuracy and a tournament-style LLM-as-a-judge framework for comparing the quality of logical reasoning outputs. Experiments analyze performance across different input formats (text vs. PDF), task sizes, and numeric tolerance thresholds, alongside ablation studies on knowledge augmentation via explicit formula prompts.

Results indicate that large LLMs achieve near-perfect scores in information extraction but perform poorly in indicator computation, with recall rates often below 50% even for top models. However, performance in logical reasoning tasks is significantly higher, suggesting that LLMs can generate plausible financial narratives even when underlying numbers are inaccurate. The study finds that providing explicit calculation formulas improves performance for larger models but can confuse smaller ones. Case studies reveal that while models like GPT-o1 and DeepSeek-r1 lead in reasoning quality, they still exhibit logical contradictions and superficial insights. The paper concludes that while LLMs are competent at data retrieval, they lack the precision required for exact financial computation, highlighting the need for hybrid systems or further domain-specific fine-tuning for reliable automated fundamental analysis.

## CFGPT: Chinese Financial Assistant with Large Language Model

- Year: 2023
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, financial question answering, equities, china market, fine-tuning, instruction tuning, chain of thought, news, sec filings, social media, accuracy, dataset, model, open source, bias, hallucination, multimodal modeling, event detection
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "sec filings", "social media"], "deliverable": ["dataset", "model", "open source"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["fine-tuning", "instruction tuning", "chain of thought"], "risk_issue": ["bias", "hallucination"], "task": ["sentiment analysis", "stock prediction", "financial question answering"]}
- One-line summary: CFGPT introduces a Chinese financial LLM framework comprising a large-scale pre-training dataset (CFData), a 7B-parameter model (CFLLM) fine-tuned via continued pre-training and supervised instruction tuning, and a deployment system (CFAPP) supporting multimodal inputs and complex financial reasoning tasks.

### Detailed Summary

The paper addresses the lack of robust, open-source large language models specifically tailored for the Chinese financial domain, where existing general-purpose LLMs often struggle with domain-specific jargon, regulatory nuances, and complex analytical tasks. The authors position CFGPT as a comprehensive solution that bridges the gap between general NLP capabilities and specialized financial requirements, aiming to provide a deployable assistant for real-world financial applications rather than just a research benchmark. This work contributes to the broader field of multilingual and multimodal finance by demonstrating how domain-specific data curation and two-stage training can significantly enhance model performance in Chinese financial contexts.

The core methodology involves constructing CFData, a massive corpus containing 584 million documents and 141 billion tokens for pre-training, sourced from corporate prospectuses, announcements, research reports, news, and social media, alongside a supervised fine-tuning dataset of 1.5 million instruction pairs covering six tasks: sentiment analysis, event detection, report summarization, topic decomposition, question answering, and stock movement prediction. The base model, InternLM-7B, undergoes continued pre-training on CFData followed by supervised fine-tuning. The deployment framework, CFAPP, integrates vector databases, chain-of-thought reasoning modules, and multimodal parsers (text, audio, PDF) to facilitate interactive financial analysis, including causal reasoning for open-domain questions and risk management tools.

Experimental results indicate that CFLLM outperforms baseline models in zero-shot and few-shot financial tasks, particularly in sentiment analysis and event detection, validating the efficacy of the curated dataset and training strategy. The CFAPP framework demonstrates practical utility in handling diverse input formats and generating structured outputs like mind maps and templated reports. However, limitations include the reliance on GPT-4 for generating some synthetic training data, potential biases in social media sources, and the computational cost of deploying a 7B-parameter model. The paper highlights the importance of high-quality, domain-specific data in enhancing LLMs for finance, offering a valuable resource for researchers and practitioners working with Chinese financial text.

## DISC-FinLLM: A Chinese Financial Large Language Model based on Multiple Experts Fine-tuning

- Year: 2023
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, sentiment analysis, china market, fine-tuning, instruction tuning, chain of thought, retrieval, news, sec filings, accuracy, dataset, model, open source, bias, multilingual, chinese financial market, modular fine-tuning, lora, baichuan
- Tag facets: {"asset_class": [], "data_source": ["news", "sec filings"], "deliverable": ["dataset", "model", "open source"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["fine-tuning", "instruction tuning", "chain of thought", "retrieval"], "risk_issue": ["bias"], "task": ["financial question answering", "sentiment analysis"]}
- One-line summary: DISC-FinLLM is a Chinese financial large language model built on Baichuan-13B using a Multiple Experts Fine-tuning Framework with four specialized LoRA modules, demonstrating superior performance over baselines in financial NLP, computation, and retrieval tasks.

### Detailed Summary

This paper addresses the lack of open-source, domain-specific large language models for the Chinese financial market, where general LLMs often lack specialized knowledge, numerical reasoning capabilities, and real-time information processing skills. The authors propose DISC-FinLLM, a system designed to support financial professionals, developers, and students by integrating multi-turn dialogue, complex text processing, mathematical computation, and retrieval-augmented generation. The core innovation is the Multiple Experts Fine-tuning Framework (MEFF), which avoids catastrophic forgetting by training four distinct Low-rank adaptation (LoRA) modules on specialized instruction subsets, allowing for modular activation of capabilities without retraining the entire base model.

The methodology centers on constructing DISC-FIN-SFT, a comprehensive instruction-tuning dataset of approximately 250,000 samples. This dataset is divided into four categories: financial consulting (translated and augmented FiQA, forum data), financial NLP tasks (derived from ten public datasets like FPB and CCKS, plus reading comprehension from East Money news), financial computing (seed tasks augmented via self-instruction and Chain-of-Thought prompting to train tool-use for calculators and solvers), and retrieval-enhanced generation (using Chain-of-Retrieval prompting on a knowledge base of 87k news and report abstracts). The model is built on the Baichuan-13B backbone, with each LoRA module fine-tuned on its respective data subset to handle specific tasks such as sentiment analysis, entity extraction, formula construction, and document-based Q&A.

Experimental evaluations across multiple benchmarks demonstrate that DISC-FinLLM significantly outperforms baseline models like ChatGLM2 and FinGPT-v3. On the FinCUGE benchmark, the task-specific LoRA improved average F1/ROUGE scores by 2-9 points over the untrained base. In human-generated financial tests (FinEval), the consulting and task modules achieved higher accuracy than GPT-3.5 and matched GPT-4 in specific sub-domains. The computing module surpassed ChatGPT-3.5 in formula construction and result accuracy, while the retrieval module showed superior accuracy, usefulness, and reflectiveness in current affairs analysis. However, the study notes limitations in evaluating zero-shot generalization due to the scarcity of high-quality Chinese financial NLP datasets, and the reliance on ChatGPT for data generation introduces potential biases or quality inconsistencies in the instruction tuning corpus.

## LiveTradeBench: Seeking Real-World Alpha with Large Language Models

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, alpha mining, equities, etfs, prediction markets, us equities, portfolio management, backtesting, tool use, agentic workflow, market prices, news, sharpe ratio, drawdown, portfolio returns, hit ratio, benchmark, simulator, trading agent, data leakage
- Tag facets: {"asset_class": ["equities", "etfs", "prediction markets"], "data_source": ["market prices", "news"], "deliverable": ["benchmark", "simulator", "trading agent"], "evaluation": ["sharpe ratio", "drawdown", "portfolio returns", "hit ratio"], "market_context": ["us equities", "portfolio management"], "method": ["backtesting", "tool use", "agentic workflow"], "risk_issue": ["data leakage", "look-ahead bias"], "task": ["portfolio optimization", "alpha mining"]}
- One-line summary: LiveTradeBench introduces a live trading environment for evaluating LLM agents in U.S. stocks and Polymarket, revealing that high general reasoning scores do not guarantee trading competence and that models exhibit distinct, market-specific portfolio styles.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models (LLMs) for financial decision-making, noting that static benchmarks fail to capture real-world dynamics, uncertainty, and sequential adaptation. It introduces LiveTradeBench, a live trading environment that streams real-time market prices and news to eliminate information leakage inherent in offline backtesting. The framework employs a portfolio management abstraction, requiring agents to output continuous allocation vectors across multiple assets rather than discrete buy/sell actions, thereby integrating risk management and cross-asset reasoning into a single decision loop.

The experimental setup involves a 50-day live evaluation of 21 mainstream LLMs across six families (including GPT-5, Claude, and Llama) in two distinct markets: U.S. equities (15 stocks/ETFs) and Polymarket prediction markets (10 binary contracts). Agents operate within a ReAct-style framework equipped with tool use for data filtering and a memory module storing recent observations. Performance is measured using cumulative return, Sharpe ratio, maximum drawdown, win rate, and volatility. The study compares these live results against static benchmark scores to assess the transferability of general intelligence to financial execution.

Key findings indicate a disconnect between general LLM capabilities and trading performance; top models on LMArena do not necessarily achieve superior trading outcomes. Models display distinct portfolio styles reflecting varying risk appetites, with some effectively leveraging live news signals to adapt allocations. The study highlights that success in one market (e.g., stocks) does not generalize to another (e.g., prediction markets), suggesting that LLMs require market-specific reasoning strategies. The work provides a valuable benchmark for assessing the robustness of LLM agents under live uncertainty, though it notes limitations regarding the long-term sustainability of strategies and the impact of transaction costs not fully modeled in the allocation abstraction.

## Learning to Trade Like an Expert: Cognitive Fine-Tuning for Stable Financial Reasoning in Language Models

- Year: 2026
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, portfolio optimization, equities, us equities, chain of thought, fine-tuning, instruction tuning, sec filings, tables, backtest, portfolio returns, risk-adjusted returns, dataset, model, open source, overfitting, cognitive reasoning, agent debate, regime adaptability
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "tables"], "deliverable": ["dataset", "model", "open source"], "evaluation": ["backtest", "portfolio returns", "risk-adjusted returns"], "market_context": ["us equities"], "method": ["chain of thought", "fine-tuning", "instruction tuning"], "risk_issue": ["overfitting"], "task": ["financial question answering", "portfolio optimization"]}
- One-line summary: The paper introduces a cognitive fine-tuning framework using a curated MCQ dataset, structured chain-of-thought reasoning, and robustness augmentation to train open-source LLMs for stable financial decision-making, demonstrating that smaller models can approach frontier performance in bullish and mixed market regimes when evaluated via a two-stage static and sequential trading simulation.

### Detailed Summary

This paper addresses the challenge of training autonomous financial agents that generalize beyond specific market patterns, aiming to replace complex multi-agent systems with a single, locally deployable model capable of risk-aware reasoning. The authors argue that current open-source models lack the structured decision logic required for stable trading in noisy environments, motivating a focus on cognitive fine-tuning rather than simple prediction or sentiment analysis. The core contribution is a framework that combines high-quality data curation with a novel reasoning template to teach models how to form decisions under uncertainty, rather than just memorizing answers.

The methodology centers on the Cognitive Financial Reasoning Dataset, constructed from classic textbooks and 15 years of S&P 500 historical data, verified by an AI committee of three frontier models to ensure label quality. The training pipeline employs CORA, a four-stage chain-of-thought template (Contextualize, Organize, Reason, Act), and DARA, a dual-axis augmentation strategy that shuffles answer positions and varies technical indicator parameters to prevent shortcut learning. The model, Llama-3.1-8B, is fine-tuned using Q-LoRA on this enriched data. Evaluation uses a two-stage protocol: Stage I measures static MCQ accuracy on a held-out test set, while Stage II assesses sequential trading performance through a chronological simulation of 150 episodes across bullish, bearish, and mixed regimes, tracking returns, exposure, and downside risk.

Results show that the full model achieves 82.38% accuracy in Stage I, outperforming open-source baselines and approaching frontier models, while ablation studies confirm that CORA and DARA are critical for preventing degenerate behavior. In Stage II, the model delivers a 7.64% average return, significantly outperforming baselines and maintaining controlled downside risk in bullish and mixed regimes. However, the model exhibits a long-biased policy that underperforms in bearish markets, highlighting a limitation in regime adaptability. The study concludes that structured cognitive training enables smaller models to exhibit competitive, risk-aware trading behavior, though further work is needed to improve robustness across all market conditions.

## Standard Benchmarks Fail -- Auditing LLM Agents in Finance Must Prioritize Risk

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: fraud detection, risk extraction, crypto, options, derivatives, institutional investing, agentic workflow, tables, ablation study, accuracy, framework, open source, hallucination, model risk, overfitting, regulatory compliance, safety auditing, adversarial robustness, operational risk, stress testing
- Tag facets: {"asset_class": ["crypto", "options", "derivatives"], "data_source": ["tables"], "deliverable": ["framework", "open source"], "evaluation": ["ablation study", "accuracy"], "market_context": ["institutional investing"], "method": ["agentic workflow"], "risk_issue": ["hallucination", "model risk", "overfitting", "regulatory compliance"], "task": ["fraud detection", "risk extraction"]}
- One-line summary: The paper argues that standard accuracy benchmarks for financial LLM agents are insufficient and proposes a risk-centric auditing framework, SAEA, which reveals that high-performing agents still harbor critical safety vulnerabilities like hallucination and adversarial susceptibility.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Model (LLM) agents in finance, arguing that traditional benchmarks focusing on accuracy, F1 scores, or return-based metrics provide an illusion of reliability. It posits that these metrics fail to capture essential safety risks such as hallucinated facts, temporal staleness, and adversarial prompt manipulation, which can lead to significant financial losses in high-stakes environments. The authors contend that the primary evaluation criterion should shift from "how well" an agent performs to "how safely" it can fail, emphasizing the need for risk-aware auditing in safety-critical financial applications.

To operationalize this shift, the authors introduce the Safety-Aware Evaluation Agent (SAEA), a modular auditing recipe grounded in risk-engineering principles and Basel’s operational-risk taxonomy. SAEA conducts a three-level audit: model-level (intrinsic vulnerabilities like hallucination and over-confidence), workflow-level (error propagation and prompt sensitivity in multi-step chains), and system-level (resilience to API failures and external shocks). The authors evaluate six state-of-the-art LLM agents (including GPT-4o, Claude-3.5-Sonnet, and various open-weight models) across three high-impact tasks: finance management (cryptocurrency), webshop automation, and transactional services. They categorize agent trajectories as "safe" or "unsafe" and measure risk severity across nine dimensions, including hallucination, temporal accuracy, and adversarial robustness.

The results demonstrate that SAEA effectively distinguishes between safe and unsafe trajectories, uncovering hidden weaknesses that conventional benchmarks miss. For instance, agents often exhibit high confidence in erroneous actions or fail to detect adversarial inputs despite high accuracy on standard tasks. The paper concludes with actionable recommendations for researchers and regulators, urging the adoption of risk-aware metrics, the publication of stress scenarios, and the treatment of a "safety budget" as a primary success criterion. It highlights that while engineering guardrails are useful, they are insufficient without rigorous, scenario-based stress testing to ensure long-term reliability and compliance in financial systems.

## Mixing It Up: The Cocktail Effect of Multi-Task Fine-Tuning on LLM Performance - A Case Study in Finance

- Year: 2024
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: case study
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, fine-tuning, news, tables, accuracy, open source, overfitting, domain adaptation, numerical reasoning, small language models
- Tag facets: {"asset_class": [], "data_source": ["news", "tables"], "deliverable": ["open source"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning"], "risk_issue": ["overfitting"], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: The paper demonstrates that multi-task fine-tuning on a cocktail of financial and general datasets significantly enhances LLM performance on specific downstream tasks, enabling small models like Phi-3-Mini to surpass larger models like GPT-4-o, though this does not necessarily improve broader domain knowledge.

### Detailed Summary

This study investigates the efficacy of multi-task fine-tuning for adapting large language models to the financial domain, challenging the conventional wisdom that single-task fine-tuning is optimal. The authors conduct a large-scale ablation study with over 200 experiments across four models (Phi-3-Small, Mistral-7B, Llama-3.1-8B, and Phi-3-Mini) to analyze how combining various financial downstream tasks affects performance. They introduce the concept of a "cocktail effect," where training on a mix of related tasks yields synergistic improvements in accuracy compared to training on the target task alone. The research also explores the role of non-financial data, specifically general instruction-following data (Open-Orca) and mathematical reasoning data (Orca-Math), to assess their impact on domain-specific performance and numerical reasoning capabilities.

The experimental design involves fine-tuning models on seven core financial datasets covering sentiment analysis, named entity recognition, headline classification, and numerical reasoning (FinQA, ConvFinQA). The authors evaluate performance using standard metrics like accuracy and exact match, as well as LLM-as-a-Judge for open-ended questions. A key finding is that multi-task fine-tuning allows the 3.8B parameter Phi-3-Mini model to outperform the significantly larger GPT-4-o model on most financial benchmarks, including challenging conversational financial QA tasks. The study further analyzes the contribution of general datasets, hypothesizing that Open-Orca acts as a regularizer, preventing performance degradation by keeping the model aligned with its pre-trained distribution, while Orca-Math enhances numerical reasoning that transfers to financial tasks.

Despite significant gains in specific task performance, the paper highlights a critical limitation: multi-task fine-tuning does not necessarily translate to improved general domain knowledge or complex reasoning abilities. Evaluations on broader benchmarks like MMLU-Pro and FinanceBench show mixed results, with some models even experiencing regression in general business and economics knowledge. This suggests that while multi-task fine-tuning is highly effective for optimizing performance on targeted downstream tasks, it may not be sufficient for achieving comprehensive domain adaptation. The authors conclude that future work should explore hybrid approaches combining multi-task learning with other domain adaptation strategies to bridge the gap between task-specific proficiency and broader domain understanding.

## Will LLMs be Professional at Fund Investment? DeepFund: A Live Arena Perspective

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: infrastructure
- Summary coverage: full_extracted_text
- Tags: portfolio optimization, strategy generation, spreadsheet reasoning, mutual funds, etfs, portfolio management, multi-agent systems, agentic workflow, news, market prices, tables, live benchmark, portfolio returns, framework, open source, simulator, data leakage, overfitting, fund investment, live arena
- Tag facets: {"asset_class": ["mutual funds", "etfs"], "data_source": ["news", "market prices", "tables"], "deliverable": ["framework", "open source", "simulator"], "evaluation": ["live benchmark", "portfolio returns"], "market_context": ["portfolio management"], "method": ["multi-agent systems", "agentic workflow"], "risk_issue": ["data leakage", "overfitting"], "task": ["portfolio optimization", "strategy generation", "spreadsheet reasoning"]}
- One-line summary: DeepFund introduces a live, multi-agent arena platform to evaluate LLM-based fund investment strategies in real-time, addressing critical flaws in existing benchmarks such as data leakage, theoretical disconnect, and excessive human intervention.

### Detailed Summary

The paper addresses the inadequacy of current LLM financial benchmarks, which primarily test document understanding rather than dynamic trading capabilities. The authors identify four systemic failures in existing evaluation methods: data leakage due to pre-training contamination on historical data, navel-gazing where models excel at theory but fail in practice, over-intervention via heavy prompt engineering, and maintenance difficulties due to the need for continuous data updates. This creates an unfair and misleading assessment landscape where models may appear proficient by recalling memorized narratives rather than demonstrating genuine predictive reasoning or adaptive decision-making in live market conditions.

To resolve these issues, the authors propose DeepFund, a comprehensive live arena platform featuring a three-phase workflow. The system employs a multi-agent framework comprising an Agent Planner, specialized Analysts (Technical, Fundamental, Insider, and Media), and an Agent Manager that synthesizes insights into buy, hold, or sell decisions. The platform operates in a time-controlled live environment, providing day-by-day market data, news, and financial information to ensure models only access information available at the decision point, thereby eliminating data leakage. It includes a modular model integration interface for various LLMs and a web-based visualization tool for monitoring performance metrics across diverse market regimes and investment horizons.

DeepFund aims to provide a realistic, fair, and standardized assessment of LLM capabilities in fund investment by mimicking real-world investment processes without human interference. The platform supports diverse portfolio management across multiple asset classes and evaluates performance through traditional financial metrics alongside LLM-specific criteria. By enabling forward testing and continuous updates, DeepFund bridges the gap between theoretical financial knowledge and practical application. The code is publicly available, encouraging community extension with new signal analyses and data sources, ultimately contributing to the development of more reliable AI-based financial decision-making tools.

## FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, financial question answering, equities, forex, china market, us equities, retrieval, tool use, sec filings, news, accuracy, benchmark, dataset, leaderboard, hallucination, expert annotation, open source, llm-as-a-judge, web search
- Tag facets: {"asset_class": ["equities", "forex"], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "dataset", "leaderboard"], "evaluation": ["accuracy"], "market_context": ["china market", "us equities"], "method": ["retrieval", "tool use"], "risk_issue": ["hallucination"], "task": ["benchmarking", "financial question answering"]}
- One-line summary: FinSearchComp is an open-source benchmark of 635 expert-annotated questions evaluating LLM agents' ability to perform realistic financial search and reasoning across time-sensitive, historical, and complex investigative tasks.

### Detailed Summary

The paper addresses the lack of realistic, open-domain benchmarks for evaluating LLM agents' financial search capabilities, noting that existing datasets either bypass search or lack the complexity of real analyst workflows. FinSearchComp is introduced as the first fully open-source agent benchmark for this purpose, designed to stress-test information gathering, coordination, and grounded reasoning in high-stakes financial contexts. It comprises three task families: Time-Sensitive Data Fetching (e.g., real-time prices), Simple Historical Lookup (e.g., point-in-time financials), and Complex Historical Investigation (e.g., multi-period synthesis), covering global and Greater China markets.

The benchmark includes 635 questions curated by 70 professional financial experts from institutions like Citadel and J.P. Morgan, ensuring high difficulty and reliability through a rigorous multi-stage quality-assurance pipeline. Data sources include official filings, regulatory websites, and professional databases, with answers validated via cross-referencing and expert arbitration. The evaluation protocol uses an LLM-as-a-Judge approach with rubric-guided judging and tolerance bands for numerical answers, validated against human labels with 95% agreement. The dataset spans 10 distinct topics, including stocks, indices, currencies, and macroeconomics, with separate subsets for Global and Greater China markets to assess cross-lingual and cross-regional generalization.

Experiments evaluate 21 models, revealing that web-enabled agents with financial plugins significantly outperform those without. Grok 4 (web) leads the global subset with 68.9% accuracy, approaching human expert levels (75.0%), while DouBao (web) leads the Greater China subset. However, all models remain substantially below human performance, with common failure modes including shallow search depth, retrieval of stale information, misalignment with reporting calendars, and errors in unit/currency normalization. The study highlights that while LLMs are making progress, they still struggle with freshness awareness, multi-source reconciliation, and temporal reasoning required for reliable decision support.

## No Language is an Island: Unifying Chinese and English in Financial Large Language Models, Instruction Data, and Benchmarks

- Year: 2024
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, earnings analysis, equities, china market, us equities, fine-tuning, instruction tuning, news, social media, financial statements, accuracy, ablation study, benchmark, dataset, model, open source, bias, multilingual, cross-lingual
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media", "financial statements"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy", "ablation study"], "market_context": ["china market", "us equities"], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["bias"], "task": ["sentiment analysis", "stock prediction", "earnings analysis"]}
- One-line summary: The paper introduces ICE-PIXIU, an open-source framework comprising the ICE-FIND bilingual instruction dataset, the ICE-INTENT fine-tuned LLM, and the ICE-FLARE benchmark, demonstrating that bilingual fine-tuning significantly enhances Chinese financial NLP performance, often surpassing GPT-4.

### Detailed Summary

The paper addresses the critical gap in bilingual Chinese-English financial Large Language Models (LLMs), noting that existing models are predominantly monolingual and lack comprehensive evaluation resources for cross-lingual capabilities. The authors argue that the growing interaction between Chinese and US financial markets necessitates tools that can handle both languages effectively, yet current research largely ignores the potential of bilingual capacity. To bridge this chasm, the study positions itself as the first to provide a unified open-source framework for bilingual financial NLP, aiming to improve linguistic flexibility and analytical acuity in cross-border financial contexts.

The core contribution is the ICE-PIXIU framework, which includes the ICE-FIND dataset, the ICE-INTENT model, and the ICE-FLARE benchmark. ICE-FIND comprises 604k instruction samples across 40 datasets, covering 18 specific tasks such as sentiment analysis, extraction, and prediction in both languages, including original English data and translated Chinese data. The ICE-INTENT model is developed by fine-tuning the InternLM-7B backbone using QLoRA on this diverse dataset. The ICE-FLARE benchmark evaluates 40 datasets across 10 NLP tasks and 20 bilingual-specific tasks, uniquely including data-out-of-training (DOT) sets to test generalization. Experiments compare ICE-INTENT against SOTA models like GPT-4 and ChatGPT on these benchmarks.

Results show that ICE-INTENT significantly outperforms existing models, particularly in Chinese financial tasks, often exceeding GPT-4's performance. The study finds that incorporating translated data enhances cross-lingual generalization and boosts English task performance, highlighting the benefits of bilingual training. However, the paper notes that current LLMs exhibit notable performance disparities between languages. Limitations include the reliance on machine translation for some Chinese datasets, which may introduce noise, and the focus on specific NLP tasks rather than end-to-end trading systems. The work provides a foundational resource for bilingual financial AI but does not directly address algorithmic trading or portfolio optimization.

## Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, portfolio optimization, strategy generation, risk extraction, spreadsheet reasoning, earnings analysis, options, derivatives, multi-agent systems, agentic workflow, prompt engineering, sec filings, earnings calls, ohlc data, tables, benchmark, framework, literature review, regulatory compliance, privacy
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["sec filings", "earnings calls", "ohlc data", "tables"], "deliverable": ["benchmark", "framework", "literature review"], "evaluation": [], "market_context": [], "method": ["multi-agent systems", "agentic workflow", "prompt engineering"], "risk_issue": ["regulatory compliance", "privacy", "overfitting"], "task": ["sentiment analysis", "portfolio optimization", "strategy generation", "risk extraction", "spreadsheet reasoning", "earnings analysis"]}
- One-line summary: This survey bridges financial practice and LLM research by proposing a dual-perspective framework that maps five core financial domains to specific agent tasks, catalogs over 30 benchmarks and 20 models, and identifies critical gaps in numerical reasoning, real-time adaptability, and regulatory compliance.

### Detailed Summary

The paper addresses the disconnect between cutting-edge LLM capabilities and the stringent, interdependent workflows of real-world financial institutions. It argues that while LLMs show promise in automating tasks like parsing filings and gauging sentiment, they struggle with systemic obstacles such as static benchmarks, poor numerical reasoning, and lack of real-time adaptability. The authors propose a dual-perspective framework: a practitioner-centric taxonomy mapping five financial departments (Data Analysis, Investment Research, Trading, Investment Management, Risk Management) to specific agent roles, and a research-focused analysis of modeling challenges, including prompt sensitivity and multi-agent fragility. This holistic view contextualizes technical progress within institutional constraints like privacy and regulatory auditing.

The methodology involves a systematic review of over 30 financial benchmarks and 20 representative LLM models, categorized by modality, task, and deployment limitations. The authors analyze datasets ranging from SEC filings and earnings calls to time-series price data, evaluating models like BloombergGPT, FinMA, and FinGPT. They detail the pipeline for each agent type, from data extraction and sentiment analysis to strategy execution and portfolio optimization. The study highlights specific limitations in current benchmarks, such as the lack of multi-asset coverage, real-time data integration, and consideration of transaction costs or liquidity constraints. It also examines multi-agent collaboration frameworks that mimic institutional workflows, such as investment committees and risk review processes.

Key findings indicate that while LLMs excel in text summarization and entity recognition, they face significant hurdles in numerical precision, long-horizon logic, and dynamic market adaptation. The survey identifies open challenges including the need for continual adaptation, coordination-aware multi-agent systems, and privacy-compliant deployment. It emphasizes that current models often rely on centralized data and lack built-in regulatory auditing mechanisms. The paper concludes by advocating for deeper researcher-practitioner collaboration and transparent model architectures to enable safer, scalable AI adoption in finance, noting that most existing solutions are conceptual or limited to single-asset scenarios without real-world execution constraints.

## FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: financial question answering, equities, us equities, retrieval, 10-k filings, sec filings, accuracy, backtest, benchmark, dataset, hallucination, query disambiguation, llm-as-a-judge, context recall, factual accuracy
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "backtest"], "market_context": ["us equities"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: The paper introduces FinDER, a benchmark dataset of 5,703 expert-annotated query-evidence-answer triplets derived from S&P 500 10-K filings to evaluate Retrieval-Augmented Generation (RAG) systems on ambiguous, real-world financial queries, demonstrating that neural retrievers and LLM-based reranking significantly outperform traditional methods but that factual correctness remains challenging without high-quality context.

### Detailed Summary

The paper addresses the critical need for accurate, up-to-date information retrieval in financial Question-Answering (QA), where standard LLMs struggle with factual accuracy and hallucination. Existing benchmarks often rely on clear, predefined contexts, failing to capture the ambiguity, brevity, and domain-specific jargon characteristic of real-world professional searches. FinDER is introduced as a rigorous testbed that challenges models to retrieve relevant evidence from large corpora of 10-K filings, simulating the complex information needs of investment professionals. The research positions FinDER as a necessary evolution in financial AI benchmarks, emphasizing the retrieval step as central to reliable financial analysis.

The dataset comprises 5,703 query-evidence-answer triplets derived from real-world financial inquiries regarding S&P 500 companies, with evidence manually annotated by investment bank analysts and CPAs. The experimental setup evaluates a RAG pipeline using the RAGAS framework, testing four retrieval models (BM25, GTE, mE5, E5-Mistral) and four generation models (GPT-o1, Claude-3.7-Sonnet, Qwen-QWQ-32B, Deepseek-R1-Distill). The methodology includes assessing retrieval recall, LLM-based reranking of top-10 passages to top-5, and generation correctness and faithfulness across qualitative and quantitative reasoning tasks. The evaluation highlights the impact of query ambiguity by comparing performance on real-world queries versus well-formed, expert-refined versions.

Results indicate that dense neural retrievers, particularly E5-Mistral, significantly outperform sparse methods like BM25 in context recall, though performance drops sharply on ambiguous queries. LLM-based reranking effectively improves precision by filtering noisy retrieval results, with models like Claude-3.7-Sonnet and GPT-o1 showing strong reasoning capabilities. However, generation correctness remains low (around 30%) even with retrieved context, highlighting that while retrieval is improved, factual accuracy in complex financial reasoning is still a major hurdle. The paper concludes that robust financial QA requires not just better generation models but superior retrieval strategies and query disambiguation, providing a valuable benchmark for future RAG development in finance.

## Unlocking Data Value in Finance: A Study on Distillation and Difficulty-Aware Training

- Year: 2026
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, equities, us equities, chain of thought, fine-tuning, reinforcement learning, retrieval, financial statements, news, accuracy, ablation study, benchmark, dataset, model, hallucination, overfitting, data distillation, difficulty-aware sampling, numerical reasoning
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "news"], "deliverable": ["benchmark", "dataset", "model"], "evaluation": ["accuracy", "ablation study"], "market_context": ["us equities"], "method": ["chain of thought", "fine-tuning", "reinforcement learning", "retrieval"], "risk_issue": ["hallucination", "overfitting"], "task": ["sentiment analysis", "stock prediction"]}
- One-line summary: The paper demonstrates that data-centric post-training strategies, specifically high-quality Chain-of-Thought distillation for SFT and difficulty-aware sampling for RL, enable an 8B-parameter financial LLM to outperform larger and specialized open-source competitors across general, sentiment, and numerical reasoning benchmarks.

### Detailed Summary

The paper addresses the challenge of deploying LLMs in finance, where domain-specific terminology, numerical reasoning, and factual accuracy are critical. It argues that in specialized verticals, performance is driven more by the quality and verifiability profile of post-training data than by architectural scaling. The authors propose a data-centric approach, introducing a two-stage hierarchy: using high-quality, verified Chain-of-Thought (CoT) data for Supervised Fine-Tuning (SFT) to establish a robust reasoning foundation, and employing difficulty- and verifiability-aware sampling for Reinforcement Learning (RL) to push generalization on hard tasks without introducing noise from unverified long-form outputs.

To implement this, the authors construct ODA-Fin-SFT-318k by aggregating 697k raw samples from 25+ open-source repositories, applying semantic deduplication, synthesizing CoT traces using a large reasoning model, and filtering via length-adaptive verification. For RL, they curate ODA-Fin-RL-12k by selecting samples with high failure rates (>50%) on the SFT model but retaining only those with concise ground truths (<16 tokens) to ensure reliable online verification using a lightweight reward model. Training is conducted on Qwen3-8B using standard SFT and Group Relative Policy Optimization (GRPO) pipelines, with a hybrid reward function combining format adherence and semantic correctness.

Evaluated on nine benchmarks spanning general financial understanding, sentiment analysis, and numerical reasoning, ODA-Fin-RL-8B achieves a 74.6% average score, surpassing all open-source financial LLMs of comparable size and matching the larger Qwen3-32B. Ablation studies reveal that training exclusively on distilled CoT data outperforms mixing raw data or adding general math/reasoning samples, which cause negative transfer. The RL stage provides consistent gains, particularly in numerical reasoning (FinQA, TaTQA) and agent-level tasks (Finova), validating that hard-but-verifiable data selection effectively refines instruction-following and complex reasoning capabilities beyond what SFT alone can achieve.

## FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models

- Year: 2024
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, credit scoring, risk extraction, equities, institutional investing, multimodal modeling, tool use, fine-tuning, instruction tuning, sec filings, news, social media, tables, accuracy, backtest, benchmark, dataset, model, open source
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "social media", "tables"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy", "backtest"], "market_context": ["institutional investing"], "method": ["multimodal modeling", "tool use", "fine-tuning", "instruction tuning"], "risk_issue": ["hallucination", "bias", "data leakage"], "task": ["sentiment analysis", "stock prediction", "credit scoring", "risk extraction"]}
- One-line summary: FinTral is a multimodal financial LLM based on Mistral-7B that achieves GPT-4-level performance on nine financial tasks by integrating domain-specific pretraining, RLAIF alignment, and tool-augmented retrieval, while introducing FinSet, a comprehensive benchmark for evaluating financial hallucinations.

### Detailed Summary

The paper addresses the challenge of applying large language models to complex financial domains, where dense numerical data, domain-specific jargon, and visual elements like charts require robust multimodal understanding. Standard LLMs often struggle with financial reasoning and are prone to hallucinations, limiting their reliability for decision-making. The authors propose FinTral, a family of models built on Mistral-7B, designed to integrate textual, numerical, tabular, and image data. The core innovation lies in a comprehensive training pipeline that includes domain-specific pretraining on a curated 20-billion-token dataset, instruction fine-tuning, and alignment via Direct Preference Optimization (DPO) using AI feedback. Additionally, the model is enhanced with vision capabilities via a CLIP encoder and equipped with external tools and Retrieval-Augmented Generation (RAG) to handle quantitative tasks and out-of-domain queries effectively.

The experimental framework centers on FinSet, a novel benchmark comprising nine tasks across 25 datasets, including sentiment analysis, named entity recognition, number understanding, stock movement prediction, credit scoring, and a unique financial hallucination analysis. The training data includes a 20-billion-token pretraining corpus derived from SEC filings, news, and social media, alongside instruction tuning data and AI-generated preference pairs. The evaluation compares FinTral variants against baselines like ChatGPT-3.5 and GPT-4. Key results show that FinTral-DPO-T&R, which combines DPO alignment with tools and retrieval, outperforms ChatGPT-3.5 in all tasks and surpasses GPT-4 in five out of nine text-based tasks. The model also demonstrates strong performance in chart understanding and significantly reduces hallucinations, achieving a 97% hallucination index compared to GPT-4's 98%.

The findings highlight that integrating retrieval and tool-use mechanisms is critical for financial LLMs to achieve high accuracy in numerical and factual tasks. FinTral shows potential for real-time financial analysis, document summarization, and risk assessment. However, the paper acknowledges limitations, including the model's domain-specific nature, which may limit generalizability outside finance. The reliance on static pretraining data means the model may not capture real-time market dynamics without continuous updates. Furthermore, the computational cost of training and the potential for bias in public data sources are noted. The work provides a valuable resource for the community through the open-source release of the FinTral models and the FinSet benchmark, facilitating further research into multimodal financial AI and hallucination mitigation.

## Empowering Many, Biasing a Few: Generalist Credit Scoring through Large Language Models

- Year: 2023
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: credit scoring, fraud detection, fine-tuning, instruction tuning, financial statements, accuracy, benchmark, dataset, model, open source, bias
- Tag facets: {"asset_class": [], "data_source": ["financial statements"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["bias"], "task": ["credit scoring", "fraud detection"]}
- One-line summary: The paper introduces CALM, a fine-tuned LLM for credit scoring, demonstrating that LLMs can generalize across diverse financial risk tasks but exhibit significant demographic biases requiring ethical oversight.

### Detailed Summary

This paper addresses the limitation of traditional credit scoring models, which are often task-specific and lack generalization. The authors propose a generalist approach using Large Language Models (LLMs) to handle multiple credit and risk assessment tasks, including credit scoring, fraud detection, financial distress identification, and claim analysis. The core research questions investigate whether LLMs can overcome narrow expertise, generalize across tasks via instruction tuning, and whether their deployment introduces fairness biases in sensitive financial decisions. The work positions LLMs as a potential paradigm shift from isolated expert systems to unified, adaptable risk assessment frameworks.

The methodology involves curating a comprehensive benchmark of 9 datasets with 14,000 samples covering the four task types. The authors construct instruction-tuning data from 6 datasets, totaling 45,000 samples, using both table-based and description-based prompts to handle tabular financial data. They fine-tune Llama2-Chat using LoRA to create CALM, a 7-billion parameter model. Experiments compare CALM against open-source LLMs (Vicuna, Bloomz) and closed-source models (GPT-4, ChatGPT) as well as state-of-the-art expert systems. Evaluation metrics include accuracy, F1, Matthews Correlation Coefficient (MCC) for imbalanced data, and bias metrics (Disparate Impact, Equal Opportunity Difference) focusing on gender, age, and foreign status.

Results show that GPT-4 matches or exceeds expert systems in several tasks, while CALM outperforms other open-source LLMs, demonstrating effective knowledge transfer. However, the study reveals significant biases in LLM predictions, particularly against unprivileged groups defined by age, gender, and nationality. The authors highlight that while LLMs offer inclusivity and comprehensive risk assessment, they risk perpetuating societal biases. The paper contributes open-source datasets, the CALM model, and a benchmark, emphasizing the need for ethical oversight in deploying LLMs for credit decisions to ensure fairness and transparency in financial services.

## Open-FinLLMs: Open Multimodal Large Language Models for Financial Applications

- Year: 2024
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, credit scoring, fraud detection, portfolio optimization, spreadsheet reasoning, equities, portfolio management, multimodal modeling, fine-tuning, instruction tuning, sec filings, news, tables, ohlc data, sharpe ratio, drawdown, accuracy, model, dataset, benchmark
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "tables", "ohlc data"], "deliverable": ["model", "dataset", "benchmark", "open source"], "evaluation": ["sharpe ratio", "drawdown", "accuracy"], "market_context": ["portfolio management"], "method": ["multimodal modeling", "fine-tuning", "instruction tuning"], "risk_issue": ["model risk"], "task": ["sentiment analysis", "credit scoring", "fraud detection", "portfolio optimization", "spreadsheet reasoning"]}
- One-line summary: Open-FinLLMs introduces a suite of open-source multimodal financial LLMs, including FinLLaMA and FinLLaVA, which outperform general and specialized baselines like GPT-4 and BloombergGPT across text, tabular, time-series, and chart data tasks.

### Detailed Summary

The paper addresses the limitations of existing financial LLMs, which suffer from scarce corpora, weak multimodal capabilities, and narrow evaluations. The authors introduce Open-FinLLMs, a suite of models designed to handle diverse financial data types including text, tabular, time-series, and chart data. The suite comprises FinLLaMA, a foundational model pre-trained on a 52-billion-token corpus; FinLLaMA-Instruct, fine-tuned with 573K financial instructions; and FinLLaVA, enhanced with 1.43M multimodal tuning pairs for cross-modal reasoning. This approach aims to bridge the gap between textual and structured financial data, enabling more comprehensive financial knowledge capture.

The methodology involves a structured training pipeline. FinLLaMA is built on LLaMA3-8B and pre-trained on a mix of financial papers, conference calls, reports, indicators, news, historical data, and SEC filings, mixed with general domain data to prevent catastrophic forgetting. FinLLaMA-Instruct uses parameter-efficient fine-tuning with LoRA on a curated instruction dataset. FinLLaVA employs a two-stage multimodal alignment and supervised fine-tuning process using CLIP and LLaVA-1.5 frameworks, incorporating chart and tabular image-text pairs. Evaluations cover 14 financial tasks across 30 datasets and 4 multimodal tasks in zero-shot, few-shot, and fine-tuning settings.

Results demonstrate that Open-FinLLMs outperform advanced financial and general LLMs, including GPT-4, across financial NLP, decision-making, and multimodal tasks. FinLLaMA excels in zero-shot and few-shot settings, while FinLLaMA-Instruct surpasses GPT-4 on three key financial analysis tasks. FinLLaVA achieves state-of-the-art performance on tabular and chart benchmarks, outperforming commercial models like GPT-4o and Gemini-1.5-pro. The models show strong potential for real-world applications such as portfolio optimization, trend analysis, and financial reporting, though the paper notes that trading performance was evaluated using a specific agent framework (FinMem) rather than direct market execution.

## TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance

- Year: 2023
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: algorithmic trading, strategy generation, equities, mutual funds, portfolio management, multi-agent systems, agentic workflow, retrieval, prompt engineering, market prices, news, sharpe ratio, portfolio returns, framework, trading agent, overfitting, layered memory, agent debate, multi-modal data, character design
- Tag facets: {"asset_class": ["equities", "mutual funds"], "data_source": ["market prices", "news"], "deliverable": ["framework", "trading agent"], "evaluation": ["sharpe ratio", "portfolio returns"], "market_context": ["portfolio management"], "method": ["multi-agent systems", "agentic workflow", "retrieval", "prompt engineering"], "risk_issue": ["overfitting"], "task": ["algorithmic trading", "strategy generation"]}
- One-line summary: TradingGPT introduces a multi-agent LLM framework with layered memory and distinct character profiles to enhance automated stock and fund trading performance through collaborative debate and hierarchical information processing.

### Detailed Summary

The paper addresses the limitation of standard LLMs in financial trading, where processing all historical inputs as a single block fails to emulate human hierarchical memory, leading to inefficient prioritization of critical market events. The authors propose TradingGPT, a multi-agent system designed to extract relevant insights from hierarchical financial data by organizing agent memories into short, middle, and long-term layers, each governed by custom decay mechanisms that align with human cognitive processes. This structure allows agents to better navigate financial changes and formulate strategies by integrating multi-source historical actions and real-time market insights.

The methodology employs a multi-modal dataset sourced from Databento, Alpaca News, and ARK fund holdings, processed via FAISS for semantic retrieval. Agents are assigned distinct trading characters (risk-seeking, neutral, or averse) and sector specializations to ensure decision diversity. The system utilizes a dual workflow: single-agent immediate and extended reflections for daily trading decisions, and a multi-agent debate mechanism where agents exchange top-ranked memories and recommendations to optimize trades on shared stocks. The evaluation uses financial metrics like Sharpe Ratio and cumulative returns, comparing performance against baseline strategies using GPT-3.5 Turbo.

Findings indicate that the layered memory and debate mechanisms significantly improve trading accuracy and adaptability to market signals compared to single-agent baselines. The distinct character design enhances robustness by preventing herd behavior and uncovering latent opportunities. However, the study is currently in the prompt design and ablation phase, with full comparative results against reinforcement learning baselines pending. Limitations include reliance on specific LLM backbones and the need for further validation on high-frequency trading scenarios beyond the daily granularity tested.

## Time Travel is Cheating: Going Live with DeepFund for Real-Time Fund Investment Benchmarking

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, benchmarking, equities, us equities, institutional investing, multi-agent systems, backtesting, market prices, financial statements, sec filings, live benchmark, sharpe ratio, drawdown, portfolio returns, benchmark, framework, dataset, open source, data leakage, look-ahead bias
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "financial statements", "sec filings"], "deliverable": ["benchmark", "framework", "dataset", "open source"], "evaluation": ["live benchmark", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["us equities", "institutional investing"], "method": ["multi-agent systems", "backtesting"], "risk_issue": ["data leakage", "look-ahead bias"], "task": ["portfolio optimization", "benchmarking"]}
- One-line summary: DeepFund introduces a live, multi-agent benchmarking framework for LLM-driven fund investment that eliminates historical data leakage, revealing that most state-of-the-art models incur net losses in real-time trading, with only Grok 3 achieving profitability through prudent risk management.

### Detailed Summary

The paper addresses the critical limitation of existing financial LLM benchmarks that rely on historical back-testing, which allows models to "time travel" by leveraging future information embedded in their training corpora, leading to inflated performance estimates. To solve this, the authors introduce DeepFund, a live fund investment benchmarking tool that evaluates LLMs in real-time market conditions, ensuring no information leakage from post-cutoff data. The framework positions LLMs as active fund managers rather than static analysts, requiring them to make dynamic trading decisions under uncertainty.

DeepFund employs a multi-agent architecture where a single LLM backend assumes three roles: a Financial Planner that orchestrates tasks, an Analyst Team comprising specialized agents (Technical, Fundamental, Insider, Company News, Macro Economic, Policy) that generate directional signals, and a Portfolio Manager that synthesizes these signals to execute Buy/Sell/Hold decisions. The system connects to live market data via APIs (Yahoo Finance, Alpha Vantage) and evaluates nine flagship LLMs (e.g., GPT-4.1, DeepSeek-V3, Grok 3) over a 24-day period in March-April 2025, focusing on Berkshire Hathaway’s top five holdings. Performance is measured using standard financial metrics including Cumulative Return, Sharpe Ratio, and Maximum Drawdown.

Empirical results reveal that most LLMs struggle in live trading, with only Grok 3 mini Beta achieving a positive cumulative return (+1.1%), while models like DeepSeek-V3 and Claude 3.7 Sonnet incurred significant losses. The study highlights distinct trading "personalities": Grok adopted a prudent, low-frequency strategy with high cash reserves and diversification, whereas DeepSeek exhibited high-frequency, momentum-driven behavior with low cash reserves, leading to vulnerability during market downturns. The findings underscore the current limitations of LLMs in active fund management and demonstrate the necessity of live benchmarking to assess true predictive power and risk control capabilities.

## Responsible Innovation: A Strategic Framework for Financial LLM Integration

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: conceptual
- Summary coverage: first_50k_chars
- Tags: regulatory reporting, fraud detection, credit scoring, investment advisory, options, derivatives, fine-tuning, framework, regulatory compliance, bias, hallucination, privacy, responsible ai, ai governance, ethical oversight, data governance, hybrid architecture
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": [], "deliverable": ["framework"], "evaluation": [], "market_context": [], "method": ["fine-tuning"], "risk_issue": ["regulatory compliance", "bias", "hallucination", "privacy"], "task": ["regulatory reporting", "fraud detection", "credit scoring", "investment advisory"]}
- One-line summary: This paper proposes a structured six-decision framework to guide financial institutions in the responsible integration of Large Language Models, balancing innovation with regulatory compliance, data governance, and ethical oversight.

### Detailed Summary

The paper addresses the critical gap in strategic governance for Large Language Model (LLM) adoption in finance, where technical capabilities often outpace regulatory and ethical frameworks. It argues that financial institutions must move beyond simple model selection to adopt a holistic lifecycle approach that integrates feasibility, data security, risk management, and ethical considerations. The authors position this framework as a necessary roadmap for balancing the high-stakes demands of financial services—such as credit assessment and compliance—with the opacity and variability inherent in generative AI systems.

The core contribution is a six-decision framework designed to guide institutions from initial feasibility to final deployment. The decisions include: (1) evaluating whether an LLM is necessary versus simpler NLP methods; (2) establishing robust data governance and privacy safeguards; (3) implementing targeted risk management and continuous monitoring; (4) integrating ethical oversight and bias mitigation; (5) justifying Return on Investment (ROI) and strategic value; and (6) selecting the optimal implementation pathway (open-source vs. proprietary, in-house vs. vendor). The paper synthesizes existing literature on parameter-efficient fine-tuning, retrieval-augmented generation, and federated learning to inform these decisions, providing a conceptual rather than empirical methodology.

Findings emphasize that responsible LLM integration requires hybrid architectures, such as combining deterministic rules for compliance-critical tasks with LLMs for unstructured text analysis. The framework highlights the importance of pilot testing, audit trails, and human-in-the-loop oversight to mitigate hallucinations and bias. Limitations include the framework's conceptual nature, lacking quantitative validation or specific case studies, and its reliance on evolving regulatory landscapes which may require frequent updates to the decision criteria.

## Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English

- Year: 2024
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, financial question answering, equities, fine-tuning, instruction tuning, sec filings, news, accuracy, backtest, benchmark, dataset, model, open source, bias, multilingual, spanish, cross-lingual transfer
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["bias"], "task": ["sentiment analysis", "stock prediction", "financial question answering"]}
- One-line summary: The paper introduces Toisón de Oro, a bilingual Spanish-English financial LLM framework including the FinMA-ES model, FIT-ES instruction dataset, and FLARE-ES benchmark, demonstrating that FinMA-ES outperforms GPT-4 in Spanish financial tasks through cross-linguistic transfer.

### Detailed Summary

The paper addresses the significant disparity in financial Natural Language Processing (NLP) resources between English and Spanish, noting that existing large language models (LLMs) are predominantly English-centric despite Spanish's global economic importance. The authors identify a critical gap in bilingual financial tools and propose Toisón de Oro, a comprehensive framework designed to bridge this divide by providing open-source datasets, models, and evaluation benchmarks for Spanish-English financial NLP. This positioning highlights the need for multilingual capabilities in FinTech to serve diverse demographics and global markets effectively.

Methodologically, the authors construct FIT-ES, a bilingual instruction tuning dataset comprising over 144,000 samples from 15 sources covering seven tasks, including sentiment analysis, classification, question answering, and summarization. They fine-tune the LLaMA2-7B model to create FinMA-ES, utilizing both Spanish and English data to leverage cross-linguistic transfer. Evaluation is performed using FLARE-ES, a novel benchmark with 21 datasets across nine tasks, including unseen data to test generalization. The experimental design compares FinMA-ES against state-of-the-art models like GPT-4, ChatGPT, and other open-source LLMs using metrics such as F1, Accuracy, and ROUGE scores.

Results indicate that FinMA-ES significantly outperforms GPT-4 in four out of six Spanish financial tasks, particularly in classification and question answering, validating the efficacy of strategic instruction tuning and cross-lingual data integration. The study reveals a pronounced performance gap in existing LLMs for Spanish financial contexts. However, limitations include the model's 7B parameter size, which may restrict depth, and poor performance on complex summarization tasks. The authors also note ethical concerns regarding the dissemination of financial information and recommend using the model primarily for research purposes.

## Financial Report Chunking for Effective Retrieval Augmented Generation

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, retrieval, sec filings, 10-k filings, accuracy, framework, document understanding, chunking strategy, vector database, information retrieval
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "10-k filings"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["retrieval"], "risk_issue": [], "task": ["financial question answering"]}
- One-line summary: The paper demonstrates that structurally aware chunking of SEC financial reports using the Chipper document understanding model significantly improves Retrieval Augmented Generation (RAG) question-answering accuracy and retrieval consistency compared to fixed-size token chunking.

### Detailed Summary

This research addresses the critical preprocessing bottleneck in Retrieval Augmented Generation (RAG) systems applied to complex financial documents. While standard RAG pipelines typically rely on naive paragraph or fixed-token chunking, this approach often ignores the semantic structure of documents, leading to fragmented context and reduced factual accuracy. The authors argue that financial reports, such as 10-Ks and 10-Qs, contain distinct structural elements like tables, titles, and narrative sections that should guide how text is segmented for indexing. The study positions element-based chunking as a superior alternative to size-based strategies, aiming to preserve contextual integrity and improve the precision of information retrieval for downstream LLM generation tasks.

The methodology involves a systematic comparison of chunking strategies using the FinanceBench dataset, which contains 141 questions derived from 80 SEC filings. The authors employ the Unstructured library's Chipper model, a vision-encoder-decoder, to identify and extract structural elements (titles, narrative text, tables) from the documents. These elements are then merged into chunks respecting structural boundaries, enriched with metadata like keywords and summaries, and indexed in a Weaviate vector database using sentence transformers. The retrieval performance is evaluated using page-level accuracy and paragraph-level ROUGE/BLEU scores, while the final Q&A accuracy is assessed via manual evaluation and automated GPT-4 comparison against ground-truth answers. Baselines include fixed token sizes (128, 256, 512) and aggregated retrieval results.

Results indicate that element-based chunking yields more consistent retrieval performance and higher Q&A accuracy than fixed-size methods. Specifically, the element-based approach achieved a manual Q&A accuracy of 53.19%, outperforming the best fixed-size baseline (48.23% for 512 tokens). The study also found that aggregating results from multiple chunking strategies further improved retrieval metrics, though it risked exceeding LLM context limits. A key finding is that structural chunking eliminates the need for hyperparameter tuning of chunk sizes, offering a more generalizable solution. However, the authors note limitations in automated evaluation consistency and the computational overhead of document understanding models, suggesting future work on broader domain applicability and optimized element relations.

## AlphaFin: Benchmarking Financial Analysis with Retrieval-Augmented Stock-Chain Framework

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, financial question answering, equities, china market, fine-tuning, chain of thought, retrieval, sec filings, news, tables, backtest, accuracy, sharpe ratio, drawdown, portfolio returns, benchmark, dataset, model, open source, overfitting
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "tables"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["backtest", "accuracy", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["china market"], "method": ["fine-tuning", "chain of thought", "retrieval"], "risk_issue": ["overfitting", "hallucination"], "task": ["stock prediction", "financial question answering"]}
- One-line summary: AlphaFin introduces a comprehensive dataset and the Stock-Chain framework, which combines LoRA-finetuned LLMs with Retrieval-Augmented Generation to achieve state-of-the-art stock trend prediction accuracy and a 30.8% annualized return while providing interpretable financial analysis.

### Detailed Summary

The paper addresses the limitations of traditional machine learning models, which lack interpretability and textual integration, and general Large Language Models, which suffer from hallucinations and outdated knowledge in financial contexts. The authors formalize financial analysis into stock trend prediction and financial question answering, aiming to bridge the gap between quantitative forecasting and qualitative reasoning. They introduce AlphaFin, a dataset combining traditional research data, real-time market data, and handwritten chain-of-thought reports, to train models that can provide reasoned, up-to-date investment insights.

The proposed Stock-Chain framework operates in two stages. Stage one fine-tunes a StockGPT model using Low-Rank Adaptation on AlphaFin’s financial reports and chain-of-thought data to predict monthly stock trends (up/down) based on retrieved documents. Stage two enhances this base model with Retrieval-Augmented Generation, utilizing a vector database of financial news and reports to answer user queries with real-time context. The system employs coarse-grained summarization and fine-grained entity-level dialogue generation for knowledge extraction, ensuring the model accesses relevant, current information during inference.

Experiments on Chinese capital market data show Stock-Chain achieves a 30.8% annualized rate of return and 55.7% prediction accuracy, significantly outperforming baselines like FinGPT, ChatGPT, and LSTM models. The framework also demonstrates superior performance in financial question answering, as validated by human and GPT-4 preference evaluations. However, the study is limited by its focus on the Chinese market, the potential for overfitting to specific report structures, and the inherent risks of automated trading strategies, noting that while returns are high, real-world deployment requires careful risk management and continuous data updates.

## A Comprehensive Review of Generative AI in Finance

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, fraud detection, market simulation, investment advisory, retrieval, news, literature review, dataset, regulatory compliance, privacy, hallucination, generative ai, synthetic data, gan, bertopic, taxonomy
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["literature review", "dataset"], "evaluation": [], "market_context": [], "method": ["retrieval"], "risk_issue": ["regulatory compliance", "privacy", "hallucination"], "task": ["sentiment analysis", "fraud detection", "market simulation", "investment advisory"]}
- One-line summary: This 2024 review systematically analyzes 90 papers on generative AI in finance using BERTopic, identifying three main themes: LLM applications for financial tasks, risks and regulatory challenges, and synthetic data generation via GANs.

### Detailed Summary

This paper addresses the need for a structured overview of the rapidly evolving intersection between generative AI (GAI) and the financial sector. Unlike prior surveys that focus narrowly on large language models (LLMs) or rely on manual topic classification, this study employs BERTopic, an advanced unsupervised topic modeling technique, to systematically categorize and analyze 90 key papers published between 2018 and 2024. The research aims to uncover predominant themes, emerging areas of interest, and the broader implications of GAI technologies, including variational autoencoders (VAEs), generative adversarial networks (GANs), and diffusion models, beyond just LLMs. By leveraging BERTopic's ability to capture semantic relationships and context, the authors provide an objective, data-driven taxonomy of the current landscape, addressing gaps in existing literature regarding the comprehensive integration of various GAI models in finance.

The methodology involves retrieving 90 papers from Google Scholar using keywords "generative AI and finance" and "large language models and finance." The dataset includes interdisciplinary research from finance, computer science, economics, and business, sourced from major publishers and preprint servers. The authors apply a three-step BERTopic pipeline: generating document embeddings using Sentence-BERT, reducing dimensionality with UMAP, and clustering with HDBSCAN to identify coherent topics. The resulting clusters are analyzed using class-based TF-IDF to extract representative keywords. The study compares BERTopic's performance against traditional methods like LDA, highlighting its superior ability to handle semantic nuances. The experimental design focuses on thematic clustering rather than empirical performance testing of specific models, aiming to map the intellectual structure of the field.

The analysis reveals three primary clusters: "LLMs for Financial Tasks" (47 papers), "The Risk and Challenge of Generative AI" (20 papers), and "Synthetic Financial Data Generation" (12 papers). The findings indicate that LLMs dominate current research, with applications ranging from sentiment analysis and robo-advisory to complex reasoning and multimodal chart interpretation. Finance-specific models like FinGPT and BloombergGPT are highlighted for their superior performance over general-purpose models in domain-specific tasks. However, the review also emphasizes significant challenges, including hallucinations, ethical concerns, regulatory compliance, and data privacy. Synthetic data generation via GANs is identified as a critical area for overcoming data scarcity and privacy issues in risk modeling and market simulation. The paper concludes that while GAI offers transformative potential, robust regulatory frameworks and ethical guidelines are urgently needed to govern its deployment in finance.

## FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, benchmarking, instruction tuning, fine-tuning, news, tables, accuracy, benchmark, dataset, open source, hallucination, open source models, task interference, zero-shot generalization
- Tag facets: {"asset_class": [], "data_source": ["news", "tables"], "deliverable": ["benchmark", "dataset", "open source"], "evaluation": ["accuracy"], "market_context": [], "method": ["instruction tuning", "fine-tuning"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "benchmarking"]}
- One-line summary: FinGPT introduces a cost-effective instruction tuning benchmark for open-source LLMs, demonstrating that task-specific and multi-task tuning significantly improves financial NLP performance, while zero-shot generalization remains challenging for most models except ChatGLM2.

### Detailed Summary

This paper addresses the challenge of adapting open-source large language models to financial domains by proposing a structured instruction tuning paradigm. The authors argue that while closed-source models like BloombergGPT exist, open-source alternatives offer transparency and cost-efficiency. The research positions itself as a comprehensive benchmarking scheme that evaluates not just final performance, but the entire pipeline of integrating LLMs with financial datasets. It emphasizes reproducibility and the ability to handle diverse financial tasks, ranging from basic entity recognition to complex relation extraction, thereby filling a gap in understanding how different base models behave under domain-specific fine-tuning.

The methodology involves instruction tuning six 7B-parameter open-source models (Llama2, Falcon, BLOOM, MPT, ChatGLM2, Qwen) using Low-Rank Adaptation (LoRA) on a cost-effective budget of approximately $300. The experimental design follows a three-phase progression: task-specific tuning on Sentiment Analysis, Headline Classification, Named Entity Recognition, and Relation Extraction; multi-task tuning combining these datasets; and zero-shot evaluation on unseen sentiment tasks. Data sources include FPB, FiQA-SA, TFNS, NWGI, NER, Headline, and FinRED. The study employs F1-scores as the primary metric, analyzing performance gains and degradations across phases to understand task interference and generalization capabilities.

Key findings reveal that Llama2 and MPT achieved the best overall performance in task-specific and multi-task settings, with MPT showing significant improvements in information extraction tasks after multi-task training. However, zero-shot generalization was poor for most models, with ChatGLM2 and Falcon performing best, likely due to their chat-centric pre-training. A major limitation identified is the trade-off between specialization and generalization, where multi-task tuning sometimes degraded classification performance. The paper highlights that hallucination and task interference remain critical hurdles, suggesting that while instruction tuning is effective for specific financial NLP tasks, robust zero-shot financial reasoning requires further architectural or data-centric innovations.

## FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning

- Year: 2025
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, chain of thought, symbolic regression, tables, accuracy, benchmark, dataset, hallucination, verifiable reasoning, synthetic data, step-level evaluation
- Tag facets: {"asset_class": [], "data_source": ["tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["chain of thought", "symbolic regression"], "risk_issue": ["hallucination"], "task": ["financial question answering", "benchmarking"]}
- One-line summary: FinChain introduces a symbolic benchmark for verifiable multi-step financial reasoning, revealing that even frontier LLMs struggle with complex chain-of-thought verification despite strong final-answer accuracy.

### Detailed Summary

The paper addresses the critical gap in financial NLP benchmarks, which typically prioritize final numerical answers over transparent, verifiable intermediate reasoning. Existing datasets like FinQA lack systematic step-level supervision, making it difficult to distinguish genuine multi-step inference from pattern matching. The authors introduce FinChain, the first benchmark designed specifically for verifiable Chain-of-Thought evaluation in finance, aiming to expose weaknesses in symbolic financial reasoning that previous metrics overlooked. This positioning highlights the need for benchmarks that enforce transparency and auditability in financial AI systems.

FinChain is constructed using parameterized symbolic templates across 58 topics in 12 financial domains, generating contamination-free data with executable Python code for automatic verification. The authors propose CHAINEVAL, a dynamic alignment metric using Dynamic Time Warping to jointly assess step-level semantic and numerical consistency alongside final-answer correctness. They evaluate 26 leading LLMs, including frontier proprietary models and fine-tuned open-weight systems, under zero-shot conditions. The experimental design isolates reasoning ability from document parsing, focusing on structured symbolic operations ranging from basic compound interest to advanced investment analysis.

Results show that while frontier models like GPT-5 lead in overall performance, they still exhibit significant limitations in advanced multi-step symbolic reasoning, with performance degrading sharply on complex tasks. Domain-adapted and math-enhanced models narrow the gap but do not close it, suggesting that scale alone is insufficient without structured supervision. Error analysis reveals heterogeneous failure modes, including computational, conceptual, and hallucination errors. A key limitation is the synthetic nature of the data, which lacks the linguistic diversity of real-world financial texts, though it provides a controlled testbed for developing trustworthy, interpretable financial AI.

## Evaluating Financial Intelligence in Large Language Models: Benchmarking SuperInvesting AI with LLM Engines

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, benchmarking, spreadsheet reasoning, equities, institutional investing, sec filings, annual reports, tables, accuracy, benchmark, dataset, hallucination, indian equities, factual accuracy, analytical completeness
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "annual reports", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": [], "risk_issue": ["hallucination"], "task": ["equity research", "benchmarking", "spreadsheet reasoning"]}
- One-line summary: The paper introduces the AI Financial Intelligence Benchmark (AFIB) to evaluate five AI systems across five dimensions, finding that SuperInvesting achieves the highest aggregate performance in factual accuracy and analytical completeness for Indian equity research.

### Detailed Summary

The paper addresses the lack of systematic evaluation for financial reasoning in large language models, noting that general benchmarks fail to capture the domain-specific requirements of high-stakes investment research. It introduces the AI Financial Intelligence Benchmark (AFIB), a multi-dimensional framework assessing factual accuracy, analytical completeness, data recency, model consistency, and failure patterns. The study positions this evaluation as critical for understanding the reliability of AI systems in professional financial workflows, where numerical precision and coherent synthesis are paramount.

The methodology involves evaluating five AI systems—GPT, Gemini, Perplexity, Claude, and SuperInvesting—on a dataset of 71 structured financial analysis queries derived from real-world equity research tasks focused on the Indian capital markets. The dataset includes companies from diverse sectors such as banking, IT, and conglomerates. Ground truth data is sourced from SEBI-regulated filings and annual reports. The evaluation uses a structured scoring rubric for each dimension, including a consistency test where queries are repeated across sessions to measure response stability. Additionally, the study incorporates a deployment dataset of 432 negatively rated responses to analyze real-world failure modes.

Results indicate that SuperInvesting achieves the highest aggregate performance, with an average factual accuracy of 8.96/10 and the highest completeness score of 56.65/70, while maintaining the lowest hallucination rate. Retrieval-oriented systems like Perplexity excel in data recency but show weaker analytical synthesis. A key finding is the trade-off between recency and analytical depth, with hybrid architectures appearing most effective. The study highlights that financial intelligence is multi-dimensional, and systems combining structured data access with reasoning capabilities provide the most reliable performance for complex investment research.

## TAT-LLM: A Specialized Language Model for Discrete Reasoning over Financial Tabular and Textual Data

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: financial question answering, fine-tuning, instruction tuning, sec filings, tables, accuracy, model, open source, hallucination, tabular reasoning, arithmetic calculation, external executor, low-rank adaptation
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables"], "deliverable": ["model", "open source"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: TAT-LLM is a specialized 7B-70B LLM fine-tuned on a Step-wise Pipeline (Extractor, Reasoner, Executor) that outperforms GPT-4 and prior SOTA models on financial tabular-textual QA benchmarks like FinQA and TAT-QA.

### Detailed Summary

The paper addresses the challenge of discrete reasoning over hybrid tabular and textual financial data, such as SEC filings, where models must perform arithmetic, comparison, and counting tasks. The authors argue that while large online LLMs like GPT-4 are capable, they pose cost, latency, and data security risks, motivating the specialization of smaller, open-source models for practical deployment in finance. The core problem is enabling these smaller models to execute multi-step inference reliably without the hallucination errors common in end-to-end generation.

To solve this, the authors propose a Step-wise Pipeline consisting of three distinct stages: an Extractor to identify relevant evidence from tables and text, a Reasoner to generate the logical equation or rule, and an Executor to compute the final answer. They fine-tune LLaMA 2 (7B, 13B, 70B) using Low-Rank Adaptation (LoRA) on training data automatically generated from FinQA, TAT-QA, and TAT-DQA datasets. A key innovation is the External Executor, a post-processing module that evaluates the Reasoner's output to ensure mathematical correctness, addressing the model's weakness in calculation. The model outputs are structured as markdown tables to facilitate this pipeline.

Experimental results demonstrate that TAT-LLM (7B) outperforms GPT-4 and all previous fine-tuned baselines on FinQA, TAT-QA, and TAT-DQA benchmarks. The 70B variant shows even greater gains, significantly closing the gap to human expert performance. The study highlights that the Step-wise Pipeline combined with the External Executor is critical for accuracy, particularly for arithmetic and counting tasks. However, the model is limited by input sequence length, making it unsuitable for very long documents (>100 pages), and it struggles with evidence extraction when financial terminology is complex or ambiguous.

## FinBloom: Knowledge Grounding Large Language Model with Real-time Financial Data

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: financial question answering, risk extraction, equities, institutional investing, retail investing, fine-tuning, retrieval, tool use, news, sec filings, accuracy, benchmark, dataset, model, open source, hallucination, knowledge grounding, structured data retrieval, schema-aligned query prediction, low-latency inference
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "sec filings"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy"], "market_context": ["institutional investing", "retail investing"], "method": ["fine-tuning", "retrieval", "tool use"], "risk_issue": ["hallucination"], "task": ["financial question answering", "risk extraction"]}
- One-line summary: FinBloom introduces a knowledge-grounding framework using a fine-tuned 7B parameter LLM as a Financial Agent to retrieve real-time structured and textual data, enabling accurate, low-latency responses to dynamic financial queries without relying on traditional dense-vector RAG.

### Detailed Summary

The paper addresses the critical limitation of static Large Language Models (LLMs) in finance, where reliance on pre-trained weights leads to hallucinations and outdated information when handling high-velocity, real-time data. The authors argue that traditional Retrieval-Augmented Generation (RAG) systems, which embed unstructured text into vector spaces, are ill-suited for financial data due to its structured, tabular nature and the precision required for metric-specific queries. To solve this, they propose a knowledge-grounding architecture that keeps the generator LLM frozen while using a specialized agent to handle data retrieval and context construction.

The methodology centers on three key components: a custom 50,000-sample Financial Context Dataset, the FinBloom 7B model, and a Financial Agent pipeline. FinBloom 7B is fine-tuned on Bloom 7B using 14 million news articles from Reuters and DPA, plus a 25% sample of 12 million SEC filings. The Financial Agent, derived from FinBloom 7B, interprets user queries to generate structured data requests (SQL-like) against a Data Module containing real-time tabular and textual repositories. This approach avoids embedding tables into vectors, instead using schema-aligned query prediction to fetch exact values, which are then linearized and appended to the query for a larger LLM (e.g., ChatGPT) to synthesize the final answer.

Experiments demonstrate that this agent-based grounding significantly outperforms standard LLMs with web access, which often provide approximate or incorrect figures for specific financial metrics. The system reduces latency by eliminating manual data provision and enhances accuracy by ensuring the generator LLM receives precise, up-to-date context. The authors release the Financial Context Dataset, the FinBloom 7B model, and the Financial Agent weights. Limitations include the inability to release raw news data due to contractual restrictions and the reliance on a separate large LLM for final synthesis, which may introduce its own latency or cost overheads compared to a fully self-contained model.

## Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? A Study on Several Typical Tasks

- Year: 2023
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, financial question answering, benchmarking, options, derivatives, chain of thought, prompt engineering, retrieval, news, social media, accuracy, ablation study, benchmark, hallucination, named entity recognition, relation extraction, numerical reasoning, zero-shot, few-shot
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["news", "social media"], "deliverable": ["benchmark"], "evaluation": ["accuracy", "ablation study"], "market_context": [], "method": ["chain of thought", "prompt engineering", "retrieval"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "financial question answering", "benchmarking"]}
- One-line summary: This empirical study benchmarks ChatGPT and GPT-4 against domain-specific models and fine-tuned baselines across eight financial NLP datasets, revealing that generalist LLMs excel in sentiment analysis and numerical reasoning but lag in structured prediction tasks like named entity recognition and relation extraction.

### Detailed Summary

The paper addresses the critical question of whether general-purpose large language models like ChatGPT and GPT-4 can serve as effective solvers for financial text analytics without domain-specific fine-tuning. It positions these models against state-of-the-art domain-specific pretrained models (e.g., BloombergGPT) and task-specific fine-tuned approaches to evaluate their transferability and robustness in the financial sector. The study aims to provide empirical evidence on the strengths and limitations of current LLMs to guide their adoption in downstream financial analytical tasks.

The methodology involves an extensive empirical evaluation across five categories of financial NLP tasks: sentiment analysis, text classification, named entity recognition (NER), relation extraction (RE), and question answering (QA). The authors utilize eight benchmark datasets, including Financial PhraseBank, FiQA, TweetFinSent, Headlines, NER FIN3, REFinD, FinQA, and ConvFinQA. Experiments compare zero-shot, few-shot, and Chain-of-Thought (CoT) prompting strategies for ChatGPT (gpt-3.5-turbo) and GPT-4 against baselines like FinBert, RoBERTa-large, Luke-base, and BloombergGPT. Metrics include accuracy, macro-F1, and weighted F1 scores, with additional ablation studies on prompt sensitivity and reasoning complexity.

Findings indicate that GPT-4 significantly outperforms ChatGPT and prior LLMs on nearly all tasks, often surpassing domain-specific models like BloombergGPT in sentiment analysis and numerical QA, particularly when using CoT prompting. However, generalist LLMs struggle with structured prediction tasks like NER and RE, where fine-tuned models (e.g., CRF, Luke-base) remain superior. The study highlights that while LLMs show strong reasoning capabilities, they still make critical numerical errors in complex multi-step calculations and lack the precision required for high-stakes financial information extraction, suggesting a hybrid approach or continued fine-tuning is necessary for complex applications.

## Enhancing Financial Sentiment Analysis via Retrieval Augmented Large Language Models

- Year: 2023
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, equities, institutional investing, instruction tuning, retrieval, news, social media, accuracy, model, open source, data leakage, context enrichment, textual similarity
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media"], "deliverable": ["model", "open source"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["instruction tuning", "retrieval"], "risk_issue": ["data leakage"], "task": ["sentiment analysis"]}
- One-line summary: The paper introduces a retrieval-augmented instruction-tuned LLM framework for financial sentiment analysis that significantly outperforms traditional models and general-purpose LLMs by combining targeted fine-tuning with external context retrieval.

### Detailed Summary

Financial sentiment analysis is critical for investment decision-making, yet traditional NLP models lack generalization, and direct application of Large Language Models (LLMs) suffers from misaligned pre-training objectives and insufficient context in brief financial news. The authors address these challenges by proposing a framework that integrates instruction tuning with retrieval-augmented generation (RAG). This approach aligns LLMs to predict specific sentiment labels while enriching short input queries with relevant background information from external sources, thereby improving prediction reliability and accuracy in complex financial scenarios.

The method involves two main components: an instruction-tuned LLM module and a RAG module. The instruction tuning uses a small dataset of 10,501 samples from Twitter Financial News and FiQA, formatted with human-written instructions to fine-tune open-source models like Llama-7B. The RAG module retrieves context from verified sources such as Bloomberg, Reuters, and Seeking Alpha using a two-step process: multi-source querying followed by similarity-based filtering using the Szymkiewicz-Simpson coefficient. Experiments evaluate the model on the Financial PhraseBank and Twitter validation sets, comparing it against baselines including FinBERT, ChatGPT, and LLaMA, using accuracy and F1 score as metrics.

Results show that the proposed method achieves a 15% to 48% performance gain in accuracy and F1 score over baselines, with the instruction-tuned Llama-7B outperforming ChatGPT 4.0 and FinBERT. The RAG module further enhances performance by resolving ambiguities in short news snippets, as demonstrated in case studies where retrieved context clarified sentiment. However, the approach relies exclusively on textual similarity for retrieval, potentially overlooking macroeconomic timing and microeconomic operational data, which limits its holistic view of financial sentiment and suggests future work should incorporate structured economic indicators.

## FinLlama: Financial Sentiment Classification for Algorithmic Trading Applications

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, alpha mining, equities, us equities, portfolio management, fine-tuning, prompt engineering, news, sharpe ratio, portfolio returns, backtest, model, dataset, overfitting, long-short portfolio, parameter-efficient fine-tuning, lora
- Tag facets: {"asset_class": ["equities"], "data_source": ["news"], "deliverable": ["model", "dataset"], "evaluation": ["sharpe ratio", "portfolio returns", "backtest"], "market_context": ["us equities", "portfolio management"], "method": ["fine-tuning", "prompt engineering"], "risk_issue": ["overfitting"], "task": ["sentiment analysis", "alpha mining"]}
- One-line summary: FinLlama fine-tunes Llama 2 7B using LoRA for financial sentiment analysis, achieving superior cumulative returns and Sharpe ratios in long-short portfolio construction compared to FinBERT and lexicon-based methods.

### Detailed Summary

The paper addresses the limitations of standard lexicon-based sentiment analysis and general-purpose LLMs in finance, where context sensitivity and computational costs are significant barriers. The authors propose FinLlama, a finance-specific framework built on the Llama 2 7B foundation model. By adding a SoftMax classification layer and employing Low-Rank Adaptation (LoRA), the model is fine-tuned to classify sentiment valence (positive, negative, neutral) and quantify its strength. This approach significantly reduces trainable parameters to 4.2 million, enabling efficient training on standard hardware without sacrificing accuracy, thereby bridging the gap between academic benchmarks and practical, resource-constrained deployment in algorithmic trading.

The methodology involves fine-tuning the model on a curated dataset of 34,180 labeled financial news samples. For evaluation, the authors construct a long-short portfolio using daily sentiment signals derived from 204,017 news articles covering 417 S&P 500 companies from 2015 to 2021. The portfolio allocates 35% of capital to long positions (highest positive sentiment) and 35% to short positions (highest negative sentiment), with equal weighting. Performance is assessed against four baselines: LMD, HIV-4, VADER, and FinBERT, using real-world financial metrics including cumulative returns, annualized return, volatility, and the Sharpe ratio, rather than just classification accuracy.

Results demonstrate that FinLlama outperforms all baselines, achieving 308.2% cumulative returns compared to FinBERT's 213.0% and the S&P 500's 83.1%. It also yields the highest Sharpe ratio (2.4) and lowest annualized volatility (18.6%), indicating enhanced risk-adjusted performance and resilience during volatile periods. The study highlights the value of domain-specific fine-tuning for actionable trading signals. However, limitations include the reliance on a relatively small fine-tuning dataset and the potential for overfitting, as well as the exclusion of transaction costs and slippage in the simulation, which may affect real-world applicability.

## When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain

- Year: 2022
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, earnings analysis, fine-tuning, instruction tuning, sec filings, earnings calls, news, accuracy, ablation study, benchmark, dataset, model, bias, domain adaptation, pre-training
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "earnings calls", "news"], "deliverable": ["benchmark", "dataset", "model"], "evaluation": ["accuracy", "ablation study"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["bias"], "task": ["sentiment analysis", "financial question answering", "earnings analysis"]}
- One-line summary: The paper introduces FLANG, a financial language model using preferential masking of financial terms and phrases, and FLUE, a comprehensive benchmark suite, demonstrating that domain-specific pre-training significantly outperforms general and prior financial models on sentiment analysis, news classification, and question answering tasks.

### Detailed Summary

The paper addresses the limitation of existing financial language models that fail to fully leverage the richness of financial data through generic pre-training schemes. The authors argue that financial terminology, often consisting of multi-token phrases, requires specialized handling to capture domain-specific semantics effectively. They propose a novel pre-training methodology that incorporates preferential masking of financial keywords and phrases, alongside a span boundary objective to learn robust multi-word representations. This approach aims to bridge the gap between general English language models and the specialized linguistic patterns found in financial texts, such as earnings calls and regulatory filings, which often contain nuanced sentiment and complex entity relationships not present in standard corpora.

To evaluate these models, the authors introduce FLUE (Financial Language Understanding Evaluation), a comprehensive benchmark suite comprising five distinct NLP tasks: financial sentiment classification and regression, news headline classification, named entity recognition, structure boundary detection, and financial question answering. The models, FLANG-BERT and FLANG-ELECTRA, are pre-trained on a diverse mix of general English data (Wikipedia, BooksCorpus) and financial datasets including SEC 10-K/10-Q filings, earnings call transcripts, analyst reports, and financial news from Reuters and Bloomberg. Experiments show that FLANG-ELECTRA achieves state-of-the-art results across most benchmarks, significantly outperforming baselines like FinBERT and standard BERT, particularly in tasks requiring deep financial understanding such as sentiment analysis and question answering.

The findings highlight that domain-specific pre-training yields substantial performance gains, with FLANG-ELECTRA showing marked improvements in sentiment regression (lower MSE) and classification accuracy compared to prior works. However, the paper notes that improvements are muted on domain-agnostic tasks like Named Entity Recognition, suggesting that domain-specific knowledge is most critical for tasks involving semantic interpretation of financial language. The authors release all models, code, and the FLUE benchmark suite to the community, emphasizing the generalizability of their masking strategy to other domains. A key caveat is that while the method improves performance, it relies on publicly available data, and the benefits may vary depending on the specific downstream task's reliance on financial jargon versus general linguistic structure.

## FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, stock prediction, earnings analysis, equities, portfolio management, agentic workflow, multi-agent systems, reinforcement learning, 10-k filings, earnings calls, news, ohlc data, backtest, portfolio returns, sharpe ratio, drawdown, framework, open source, trading agent, hallucination
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "earnings calls", "news", "ohlc data"], "deliverable": ["framework", "open source", "trading agent"], "evaluation": ["backtest", "portfolio returns", "sharpe ratio", "drawdown"], "market_context": ["portfolio management"], "method": ["agentic workflow", "multi-agent systems", "reinforcement learning"], "risk_issue": ["hallucination"], "task": ["portfolio optimization", "stock prediction", "earnings analysis"]}
- One-line summary: FinCon is an LLM-based multi-agent system with a hierarchical manager-analyst structure and conceptual verbal reinforcement that outperforms DRL and other LLM agents in single-stock trading and portfolio management by synthesizing multi-modal data and dynamically updating investment beliefs.

### Detailed Summary

The paper addresses the challenge of sequential financial decision-making, where LLMs struggle with volatile environments, multi-source information synthesis, and long-term risk management. Existing agent systems often lack hierarchical coordination or effective experience refinement, leading to suboptimal returns and high communication costs. FinCon positions itself as a synthesized framework inspired by real-world investment firms, aiming to enhance decision quality through structured collaboration and continuous learning.

FinCon employs a manager-analyst hierarchy where specialized analyst agents process distinct data modalities (news, filings, audio, tabular data) to distill insights, which the manager agent consolidates for trading decisions. The system utilizes a dual-level risk-control mechanism: within-episode risk control uses Conditional Value at Risk (CVaR) for immediate risk alerts, while over-episode control employs Conceptual Verbal Reinforcement (CVRF). CVRF updates investment beliefs via textual gradient descent based on episodic performance, selectively propagating insights to relevant agents. Experiments cover single-stock trading across eight stocks and portfolio management for two portfolios, comparing FinCon against DRL agents (A2C, PPO, DQN) and LLM agents (FinGPT, FinMem, FinAgent) using metrics like Cumulative Return, Sharpe Ratio, and Max Drawdown.

FinCon significantly outperforms baselines in both tasks, achieving higher returns and better risk-adjusted performance, particularly in volatile markets. Ablation studies confirm the efficacy of both risk-control components. The system demonstrates strong generalization and robustness, though it faces challenges with hallucination in complex multi-asset contexts. Limitations include reliance on specific data availability and the computational cost of multi-agent interactions, though the hierarchical design mitigates this compared to flat structures. The work highlights the potential of structured LLM agents with verbal reinforcement for financial applications.

## FinGPT: Democratizing Internet-scale Data for Financial Large Language Models

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, equities, us equities, fine-tuning, reinforcement learning, news, social media, sec filings, backtest, portfolio returns, framework, open source, dataset, bias, data leakage, retrieval, low-code development
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media", "sec filings"], "deliverable": ["framework", "open source", "dataset"], "evaluation": ["backtest", "portfolio returns"], "market_context": ["us equities"], "method": ["fine-tuning", "reinforcement learning"], "risk_issue": ["bias", "data leakage"], "task": ["sentiment analysis"]}
- One-line summary: FinGPT introduces an open-source framework for democratizing financial LLMs by automating the collection of real-time data from 34+ sources and enabling lightweight fine-tuning via LoRA and a novel Reinforcement Learning with Stock Prices (RLSP) method.

### Detailed Summary

The paper addresses the critical gap in accessible, high-quality financial data for training Large Language Models (LLMs), noting that existing models like BloombergGPT are closed-source and prohibitively expensive to train from scratch. The authors argue that general-purpose LLMs underperform in finance due to domain-specific disparities and the time-sensitive nature of market data, necessitating a data-centric approach that democratizes access to internet-scale financial information. This positioning highlights the need for an open, reproducible infrastructure that supports continuous model adaptation to evolving market conditions.

To solve this, the authors propose FinGPT, a four-layer framework comprising data sourcing, curation, LLM adaptation, and application. The data layer aggregates real-time information from 34 diverse sources, including news, social media, SEC filings, and academic datasets, via unified APIs. The curation pipeline automates cleaning, filtering, and deduplication to handle low signal-to-noise ratios. For model adaptation, the framework employs Low-rank Adaptation (LoRA/QLoRA) for cost-efficient fine-tuning and introduces Reinforcement Learning with Stock Prices (RLSP), which uses automated market feedback (stock price changes) as labels instead of costly human annotations. Experiments demonstrate the framework's utility in robo-advisory, sentiment analysis for quantitative trading, and low-code development.

Empirical results show that FinGPT significantly outperforms base models like LLaMA in financial sentiment classification, particularly when excluding neutral labels, with an 198% improvement in accuracy for positive/negative classification. In simulated quantitative trading, FinGPT achieved a 9.5% average cumulative return compared to -0.1% for the baseline, validating the effectiveness of RLSP and high-quality curated data. The paper emphasizes privacy and openness, allowing users to train local LoRA weights without data leakage. Limitations include the current focus on US and CN markets, the simplicity of the 2% threshold for RLSP labeling, and the need for future work on longer context windows, RAG integration, and bias mitigation.

## Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning of General-Purpose Large Language Models

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, spreadsheet reasoning, financial question answering, instruction tuning, fine-tuning, news, social media, tables, market prices, accuracy, model, benchmark
- Tag facets: {"asset_class": [], "data_source": ["news", "social media", "tables", "market prices"], "deliverable": ["model", "benchmark"], "evaluation": ["accuracy"], "market_context": [], "method": ["instruction tuning", "fine-tuning", "rag"], "risk_issue": [], "task": ["sentiment analysis", "spreadsheet reasoning", "financial question answering"]}
- One-line summary: Instruct-FinGPT improves financial sentiment analysis by instruction-tuning LLaMA-7B, significantly outperforming FinBERT and ChatGPT in numerical sensitivity and contextual understanding.

### Detailed Summary

Financial sentiment analysis is critical for market insight but remains challenging due to the need for precise numerical interpretation and deep contextual comprehension, which general-purpose LLMs often lack. This paper addresses these gaps by proposing Instruct-FinGPT, a method that transforms standard classification datasets into instruction-tuning formats. By fine-tuning the general-purpose LLaMA-7B model on a small subset of financial data, the approach leverages the model's inherent reasoning capabilities to better handle financial jargon, numeric values, and ambiguous contexts, aiming to bridge the performance gap between general LLMs and domain-specific models.

The methodology involves formatting financial sentiment data into instruction-response pairs and supervised fine-tuning LLaMA-7B using sequence-to-sequence loss. The training data combines the Twitter Financial News dataset and the FiQA dataset, totaling over 10,000 samples. The model is evaluated on multiple benchmarks, including a custom numerical sensitivity dataset and a contextual understanding dataset, alongside the Financial PhraseBank. Baselines include FinBERT, ChatGPT (GPT-3.5 and GPT-4.0), and the base LLaMA-7B model. Evaluation metrics focus on accuracy and F1-score, with specific analysis on how models handle numeric fluctuations and implicit sentiment cues.

Results demonstrate that Instruct-FinGPT-7B consistently outperforms FinBERT and ChatGPT across all datasets, achieving an accuracy of 0.880 on the Twitter validation set compared to FinBERT's 0.725. The model shows particular strength in numerical sensitivity, correctly interpreting sentiment from EPS and credit data where FinBERT fails. It also excels in contextual understanding, identifying nuanced sentiments in ambiguous news. However, the model still struggles with certain complex contextual examples, such as distinguishing between IPO price and market price movements. The study highlights that instruction tuning is a cost-effective alternative to training large domain-specific models, offering superior zero-shot generalization to unseen financial texts.

## FinArena: A Human-Agent Collaboration Framework for Financial Market Analysis and Forecasting

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, sentiment analysis, equities, a-share market, us equities, retail investing, agentic workflow, time-series modeling, financial statements, limit order book, news, ohlc data, accuracy, backtest, dataset, framework, data leakage, hallucination, human-agent collaboration, multimodal modeling
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "limit order book", "news", "ohlc data"], "deliverable": ["dataset", "framework"], "evaluation": ["accuracy", "backtest"], "market_context": ["a-share market", "us equities", "retail investing"], "method": ["agentic workflow", "time-series modeling"], "risk_issue": ["data leakage", "hallucination"], "task": ["stock prediction", "sentiment analysis"]}
- One-line summary: FinArena is a human-agent collaboration framework that integrates specialized LLM agents for time series, news, and financial statements with adaptive RAG and investor risk preferences to improve stock trend prediction and personalized investment decisions.

### Detailed Summary

This paper addresses the limitations of traditional financial forecasting models and standalone LLMs, which often struggle with multimodal data integration, hallucinations in unstructured news, and the lack of personalized risk consideration. The authors propose FinArena, a Human-Agent collaboration framework inspired by the Mixture of Experts (MoE) approach. The system comprises three specialized agents: a Time Series Agent for historical price trends, a News Agent utilizing adaptive Retrieval-Augmented Generation (RAG) to mitigate hallucinations by dynamically deciding when to search external sources, and a Statement Agent that performs iterative reasoning on financial reports. A universal expert agent synthesizes these inputs alongside user-defined risk preferences to generate personalized investment recommendations, bridging the gap between automated analysis and human intuition.

The experimental evaluation utilizes a bespoke, small-scale multimodal dataset comprising stock prices, news articles, and financial statements for five U.S. companies (Amazon, Google, Microsoft, Nvidia, Tesla) and five Chinese A-share companies (BYD, CATL, etc.) from January 2023 to March 2024. This dataset was constructed to reflect information accessible to retail investors, avoiding the data leakage issues common in large-scale public datasets. The study compares FinArena against traditional statistical models (ARIMA, GARCH) and machine learning baselines (LSTM, XGBoost) using stock trend prediction accuracy and trading simulation metrics. The adaptive RAG mechanism is specifically tested for its ability to reduce irrelevant responses and improve news analysis efficiency by filtering out low-uncertainty queries.

Results indicate that FinArena surpasses both traditional and state-of-the-art benchmarks in stock trend prediction across both U.S. and Chinese markets. The framework demonstrates promising performance in trading simulations, effectively aligning strategic insights with individual investor risk profiles, ranging from conservative to aggressive. The study highlights the practical utility of the system for retail investors by providing a low-cost, interpretable decision-support tool. However, limitations include the small sample size of selected stocks, potential biases in web-crawled news data, and the reliance on specific LLM capabilities that may vary with model updates. The paper concludes that human-agent collaboration enhances investment outcomes by incorporating nuanced human risk preferences that purely algorithmic systems often overlook.

## Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, fine-tuning, reinforcement learning, chain of thought, instruction tuning, tables, accuracy, model, dataset, bias, robo-advisory, compliance checking, reasoning, bilingual
- Tag facets: {"asset_class": [], "data_source": ["tables"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "reinforcement learning", "chain of thought", "instruction tuning"], "risk_issue": ["bias"], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: Fin-R1 is a 7B-parameter financial reasoning LLM trained via supervised fine-tuning and Group Relative Policy Optimization on a distilled 60k-sample chain-of-thought dataset, achieving competitive benchmark performance and practical utility in compliance and robo-advisory tasks.

### Detailed Summary

The paper addresses the challenge of applying general-purpose large language models to finance, where fragmented data, opaque reasoning, and weak transferability hinder deployment. The authors propose Fin-R1, a compact 7-billion parameter model designed to enhance financial reasoning through a structured two-stage post-training pipeline. This approach aims to produce outputs that are not only accurate but also interpretable and compliant with regulatory standards, addressing the 'black box' nature of existing models. By focusing on reasoning capabilities rather than just text generation, the model seeks to integrate economic, legal, and quantitative logic effectively.

The methodology begins with the construction of Fin-R1-Data, a bilingual dataset of 60,091 high-quality chain-of-thought samples. This data is distilled from authoritative benchmarks using DeepSeek-R1-671B and filtered using Qwen2.5-72B-Instruct as an LLM-as-a-Judge to ensure logical consistency and domain alignment. The model training involves supervised fine-tuning on this dataset to instill reasoning patterns, followed by Group Relative Policy Optimization (GRPO). GRPO utilizes format and accuracy reward functions to optimize the policy without requiring a separate value network, thereby improving computational efficiency and reasoning robustness across diverse financial tasks.

Empirical results demonstrate that Fin-R1 achieves an average score of 75.2 on financial reasoning benchmarks, ranking second overall and outperforming other 7B-scale models by over 17 points. The model shows strong performance in numerical reasoning, sentiment analysis, and code generation for quantitative strategies. Practical applications include compliance checking and robo-advisory, where the explicit reasoning traces provide necessary transparency. However, the study notes limitations in handling highly evolving market environments and potential biases in the distilled data, suggesting that while effective for static reasoning tasks, further work is needed for dynamic real-time financial decision-making.

## Exploring Large Language Models for Financial Applications: Techniques, Performance, and Challenges with FinMA

- Year: 2025
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, benchmarking, spreadsheet reasoning, equities, fine-tuning, instruction tuning, chain of thought, prompt engineering, news, financial statements, tables, accuracy, backtest, benchmark, model, hallucination, bias, open source, numerical reasoning
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "financial statements", "tables"], "deliverable": ["benchmark", "model"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": ["fine-tuning", "instruction tuning", "chain of thought", "prompt engineering"], "risk_issue": ["hallucination", "bias"], "task": ["sentiment analysis", "stock prediction", "benchmarking", "spreadsheet reasoning"]}
- One-line summary: This study evaluates the open-source financial LLM FinMA-7B-full on the FLARE benchmark, demonstrating strong performance in sentiment analysis and classification but significant weaknesses in numerical reasoning, entity recognition, and summarization compared to general-purpose baselines.

### Detailed Summary

This paper addresses the critical need for robust evaluation of domain-adapted Large Language Models (FinLLMs) in financial natural language processing. While general-purpose LLMs like GPT-4 offer broad reasoning capabilities, they often lack the specialized accuracy required for finance. The research positions FinMA, an open-source model from the PIXIU framework, as a key subject for understanding the trade-offs between domain-specific instruction tuning and general pre-training. The study aims to identify specific architectural and training distinctions that enable effective financial NLP, focusing on accuracy, reliability, and interpretability in high-stakes decision-making contexts.

The methodology involves a comprehensive empirical evaluation of the FinMA-7B-full model using the Financial Instruction Tuning (FIT) dataset and the FLARE benchmark. The authors conduct experiments across six primary financial NLP tasks: sentiment analysis, text classification, named entity recognition, question answering, stock movement prediction, and text summarization. The experimental design includes re-evaluating baselines such as GPT-4 and BloombergGPT under consistent conditions, utilizing Hugging Face datasets and metrics like F1, accuracy, and ROUGE. The study also explores the impact of prompt engineering techniques, such as Chain-of-Thought, and assesses the model's performance in zero-shot and few-shot settings to gauge robustness and generalization capabilities.

Findings indicate that FinMA-7B-full excels in sentiment analysis (93.9% F1) and text classification (97.5% Avg F1), outperforming GPT-4 in zero-shot settings for these specific tasks. However, it struggles significantly with numerical reasoning (7.4% Exact Match on FinQA), named entity recognition (64.1% F1), and summarization (2.8% ROUGE). The authors attribute these limitations to the LLaMA backbone's general-purpose nature and insufficient training data for complex reasoning and multimodal tasks. The study highlights challenges such as hallucination risks, bias in training data, and the need for specialized datasets. It suggests future directions including Retrieval-Augmented Generation (RAG), Low-Rank Adaptation (LoRA), and hybrid models integrating time-series data to enhance performance in stock prediction and numerical tasks.

## When AI Meets Finance (StockAgent): Large Language Model-based Stock Trading in Simulated Real-world Environments

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: strategy generation, stock prediction, equities, options, derivatives, us equities, portfolio management, market microstructure, multi-agent systems, backtesting, prompt engineering, chain of thought, news, financial statements, sec filings, limit order book, backtest, portfolio returns, risk-adjusted returns, framework
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["news", "financial statements", "sec filings", "limit order book"], "deliverable": ["framework", "open source", "simulator"], "evaluation": ["backtest", "portfolio returns", "risk-adjusted returns"], "market_context": ["us equities", "portfolio management", "market microstructure"], "method": ["multi-agent systems", "backtesting", "prompt engineering", "chain of thought"], "risk_issue": ["look-ahead bias"], "task": ["strategy generation", "stock prediction"]}
- One-line summary: StockAgent is an LLM-driven multi-agent system that simulates stock trading to analyze how external factors like macroeconomic events and social sentiment influence agent behavior and profitability while mitigating test set leakage.

### Detailed Summary

This paper addresses the limitation of static backtesting in finance by introducing StockAgent, a multi-agent framework that simulates dynamic stock market environments using Large Language Models. The research aims to understand how external factors—such as macroeconomic policies, company fundamentals, and social sentiment—affect trading decisions and market dynamics. It specifically investigates the reliability of LLM-based agents in simulating realistic investor behaviors, including personality traits and risk preferences, while ensuring that agents do not rely on prior knowledge of test data to prevent information leakage.

The methodology employs a multi-agent system where LLMs (GPT-3.5 and Gemini) drive individual investor agents with distinct personalities (Conservative, Aggressive, etc.). The simulation incorporates a transaction module with a random clock page replacement algorithm to manage order books and prevent deadlocks, and a Bulletin Board System (BBS) for agents to share trading tips. Experiments involve simulating one year of trading for two anonymized stocks, incorporating real-world events like interest rate hikes and financial report releases. The study evaluates performance across different external condition ablations (e.g., removing BBS or loan options) and compares the trading outcomes and profitability of different LLM backbones.

Results indicate that external factors significantly impact agent trading behavior and profitability, with the BBS module notably influencing market volatility and agent decisions. The simulation reveals inherent tendencies in LLMs, such as risk aversion or aggression, which affect strategy generation. The framework successfully avoids test set leakage by restricting agents to real-time information. However, limitations include the simplified market mechanics, the use of only two LLMs, and the synthetic nature of the stock data, which may limit direct applicability to live trading without further validation against real market microstructure.

## BizFinBench: A Business-Driven Real-World Financial Benchmark for Evaluating LLMs

- Year: 2025
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, china market, chain of thought, retrieval, news, accuracy, benchmark, dataset, bias, llm evaluation, chinese language, adversarial robustness, iterative calibration
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["chain of thought", "retrieval"], "risk_issue": ["bias"], "task": ["financial question answering", "benchmarking"]}
- One-line summary: BizFinBench introduces a business-driven Chinese financial benchmark with 6,781 real-world queries and the IteraJudge evaluation framework, revealing that while proprietary models lead in reasoning and extraction, no single model dominates all financial tasks, highlighting significant gaps in complex cross-concept reasoning.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models (LLMs) for real-world financial applications, where existing benchmarks often lack the contextual complexity, adversarial noise, and business-grounded reasoning required in practice. BizFinBench is introduced as the first benchmark specifically designed to assess LLMs across five dimensions: numerical calculation, reasoning, information extraction, prediction recognition, and knowledge-based question answering. It comprises 6,781 well-annotated queries in Chinese, derived from real user interactions on the iwencai APP, covering nine fine-grained categories such as anomalous event attribution and financial tool usage. The dataset emphasizes business practicality by including noisy, time-sensitive, and adversarial contexts to test model robustness beyond simple fact retrieval.

To ensure rigorous evaluation, the authors propose IteraJudge, an iterative calibration-based framework that reduces bias when LLMs serve as evaluators. This method employs dimension-decoupled assessment, sequential correction generation, and reference-aligned scoring to provide more reliable metrics than standard LLM-as-a-Judge approaches. The benchmark was used to evaluate 25 state-of-the-art models, including proprietary systems like GPT-4o, Claude-3.5-Sonnet, and Gemini-2.0-Flash, as well as open-source models like DeepSeek-R1 and Qwen series. Experiments were conducted with strict JSON output constraints and chain-of-thought reasoning, measuring performance across objective and subjective metrics to capture both accuracy and nuanced financial understanding.

Results indicate distinct capability patterns: proprietary models dominate in reasoning and information extraction, with ChatGPT-o3 and Gemini-2.0-Flash leading in complex tasks, while open-source models like DeepSeek-R1 show strong competitiveness in numerical calculation and entity recognition. However, no model dominates across all tasks, and performance varies significantly by category; for instance, prediction recognition shows minimal variance among top models, whereas information extraction has the largest spread. The study reveals that current LLMs handle routine queries competently but struggle with complex scenarios requiring cross-concept reasoning and temporal analysis. Limitations include the focus on Chinese-language data, which may limit generalizability to other markets, and the potential for evaluation bias despite IteraJudge's improvements, suggesting a need for further human-in-the-loop validation in high-stakes financial deployments.

## Exploring the Synergy of Quantitative Factors and Newsflow Representations from Large Language Models for Stock Return Prediction

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: stock prediction, alpha mining, portfolio optimization, factor modeling, equities, us equities, cross-sectional equities, multimodal modeling, backtesting, fine-tuning, reinforcement learning, news, financial statements, sharpe ratio, portfolio returns, backtest, framework, model, overfitting, decoupled training
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "financial statements"], "deliverable": ["framework", "model"], "evaluation": ["sharpe ratio", "portfolio returns", "backtest"], "market_context": ["us equities", "cross-sectional equities"], "method": ["multimodal modeling", "backtesting", "fine-tuning", "reinforcement learning"], "risk_issue": ["overfitting"], "task": ["stock prediction", "alpha mining", "portfolio optimization", "factor modeling"]}
- One-line summary: The paper introduces a decoupled training mixture model that adaptively combines quantitative factor predictions with LLM-generated newsflow representations, achieving superior stock return prediction and portfolio performance compared to standard fusion learning, particularly in long-short strategies.

### Detailed Summary

This research addresses the challenge of effectively integrating structured quantitative factors with unstructured financial newsflow for stock return prediction. The authors propose a multimodal fusion learning framework comparing representation combination, summation, and attentive methods, alongside a novel mixture model that adaptively weights single-modality and fused predictions. To overcome training instability in mixture models caused by entangled gradient variance, they introduce a decoupled training approach that independently trains prediction components and aligns mixture probabilities with their relative performance via KL divergence minimization. This method theoretically ensures that the mixture can outperform individual components by leveraging their complementary strengths.

Experiments are conducted on three investment universes: North American, Emerging Markets, and European stocks, using commercial news data and standard quantitative factors. The study evaluates long-only and long-short portfolios rebalanced monthly, comparing performance against baselines like factors-only, news-only, and other fusion methods. Results show that while simple fusion (concatenation) works well in efficient markets like North America, it can dilute factor signals in less efficient markets like Emerging Markets. The decoupled mixture model demonstrates robustness across all universes, achieving the highest annualized returns and Sharpe ratios in long-short portfolios, particularly in the North American and Emerging Markets datasets. The paper also investigates the impact of fine-tuning the LLM (DeBERTa) via LoRA, finding that it does not consistently improve performance, suggesting that pre-trained representations may suffice for this task.

Key findings indicate that the predictive relevance of news varies significantly across markets and time, often overlapping with factor information. The mixture model’s ability to adaptively downweight noisy or redundant news when factors are strong makes it superior for alpha mining in volatile or less efficient environments. Limitations include the dependency on the quality of news data and the potential for overfitting if the mixture weights are not properly regularized. The work provides practical insights for quantitative investors on when to use fusion versus mixture approaches, highlighting that simple concatenation is effective in stable regimes, while adaptive mixing is crucial for robustness across diverse market conditions.

## FinVis-GPT: A Multimodal Large Language Model for Financial Chart Analysis

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: financial question answering, stock prediction, sentiment analysis, equities, a-share market, fine-tuning, instruction tuning, multimodal modeling, ohlc data, accuracy, dataset, model, hallucination, chart analysis, visual-textual alignment, technical patterns
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data"], "deliverable": ["dataset", "model"], "evaluation": ["accuracy"], "market_context": ["a-share market"], "method": ["fine-tuning", "instruction tuning", "multimodal modeling"], "risk_issue": ["hallucination"], "task": ["financial question answering", "stock prediction", "sentiment analysis"]}
- One-line summary: FinVis-GPT is a multimodal large language model fine-tuned on a proprietary dataset of Chinese A-share stock charts that outperforms general-purpose vision-language models in generating descriptions, answering financial questions, and predicting market trends.

### Detailed Summary

The paper addresses the gap in multimodal large language models (LMMs) for financial chart analysis, noting that general-purpose models lack domain-specific visual-textual alignment. The authors propose FinVis-GPT, an LMM built upon the LLaVA architecture, designed to interpret financial visualizations such as candlestick and line charts. The core challenge lies in teaching the model to recognize technical patterns and correlate them with financial terminology, a task where off-the-shelf models often hallucinate or misinterpret visual elements like trend lines and volume bars.

To train the model, the authors constructed a two-stage dataset using historical daily stock price data from Chinese A-shares (2006-2023). The pre-training alignment dataset consists of chart images paired with textual descriptions generated by ChatGPT, while the instruction tuning dataset contains 200,000 entries with diverse Q&A pairs focused on trend analysis and prediction. The model was fine-tuned using standard LLaVA training protocols on NVIDIA A100 GPUs. Evaluation involved case studies comparing FinVis-GPT against baselines like LLaVA, MiniGPT-4, and mPLUG-Owl across three tasks: description generation, question answering, and trend prediction.

Results indicate that FinVis-GPT significantly outperforms baseline models in accuracy and relevance. While baselines frequently hallucinated unrelated content or misidentified chart components, FinVis-GPT provided concise, financially accurate interpretations. The model successfully identified trends and generated plausible future predictions based on visual inputs. However, the evaluation is limited to qualitative case studies rather than quantitative benchmarks, and the dataset is restricted to Chinese A-share markets, potentially limiting generalizability to other asset classes or global markets. The work highlights the necessity of domain-specific data curation for financial LMMs.

## PIXIU: A Comprehensive Benchmark, Instruction Dataset and Large Language Model for Finance

- Year: 2023
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, stock prediction, financial question answering, equities, fine-tuning, instruction tuning, news, tables, ohlc data, accuracy, backtest, benchmark, dataset, model, open source, overfitting, instruction dataset, multi-task learning
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "tables", "ohlc data"], "deliverable": ["benchmark", "dataset", "model", "open source"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["overfitting"], "task": ["sentiment analysis", "stock prediction", "financial question answering"]}
- One-line summary: PIXIU introduces FinMA, an open-source financial LLM fine-tuned on the FIT dataset, and FLARE, a benchmark covering financial NLP and stock prediction tasks, demonstrating that domain-specific instruction tuning significantly improves performance on most financial NLP tasks compared to general and proprietary models.

### Detailed Summary

The paper addresses the lack of open-source, instruction-following large language models tailored for the financial domain, where existing models like BloombergGPT are proprietary or lack instruction-tuning capabilities. The authors aim to democratize financial AI by creating a comprehensive framework that includes a domain-specific model, a large-scale instruction dataset, and a holistic evaluation benchmark. This positioning fills a critical gap in open-source research, enabling reproducible and transparent development of financial AI tools that can handle diverse tasks beyond simple text classification.

The core contribution is the PIXIU framework, which comprises three main components: FinMA, an LLaMA-based LLM fine-tuned with multi-task instruction data; FIT, a 136K-sample instruction dataset covering five tasks (sentiment analysis, headline classification, NER, question answering, and stock movement prediction) across various data modalities including text, tables, and time-series; and FLARE, an evaluation benchmark integrating these tasks. The authors conduct extensive experiments comparing FinMA against proprietary models like GPT-4 and BloombergGPT, as well as other open-source LLMs, using zero-shot and few-shot evaluation protocols on the FLARE benchmark datasets.

Results show that FinMA significantly outperforms competitors on most financial NLP tasks, such as sentiment analysis and headline classification, proving the value of domain-specific instruction tuning. However, FinMA struggles with complex quantitative reasoning in financial question answering and stock movement prediction, largely due to the backbone LLaMA's limitations in mathematics and the inherent difficulty of the prediction tasks. The study highlights that while instruction tuning improves general financial language understanding, it does not fully resolve challenges in numerical reasoning or market prediction, suggesting future work should focus on enhancing these specific capabilities.

## Large Language Model in Financial Regulatory Interpretation

- Year: 2024
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Not Trading Focused
- Evidence type: case study
- Summary coverage: full_extracted_text
- Tags: regulatory reporting, bonds, commodities, equities, forex, institutional investing, prompt engineering, multimodal modeling, sec filings, accuracy, framework, regulatory compliance, basel iii, capital adequacy, document parsing
- Tag facets: {"asset_class": ["bonds", "commodities", "equities", "forex"], "data_source": ["sec filings"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["prompt engineering", "multimodal modeling"], "risk_issue": ["regulatory compliance"], "task": ["regulatory reporting"]}
- One-line summary: This study demonstrates that GPT-4, when paired with image-based document loading and structured prompt engineering, can accurately interpret Basel III regulations and calculate minimum capital requirements, significantly outperforming other LLMs in both information extraction and complex mathematical computation.

### Detailed Summary

This paper addresses the challenge of interpreting complex financial regulations, specifically the Basel III capital adequacy framework, using Large Language Models. The research problem centers on the difficulty of translating verbose legal texts and mathematical formulas into actionable code for risk management systems. The authors propose a systematic framework involving specific document loading techniques and prompt engineering strategies to guide LLMs in distilling regulatory requirements into concise mathematical representations. The study positions itself at the intersection of NLP and financial compliance, aiming to streamline regulatory implementation for global banking institutions, particularly those with limited resources.

The methodology involves a comparative analysis of four LLMs: GPT-4, GPT-3.5, Claude-3-Opus, and Gemini-1.5-Pro. The experiments utilize a manually simulated dataset of over 40 asset holdings, including fixed income, equities, currency pairs, and commodities. Key experimental designs include comparing PDF versus image-based document loading methods and evaluating naive versus detailed prompt structures. The models are tested on their ability to identify risk buckets, risk weights, and correlations, as well as their accuracy in performing complex mathematical calculations for Minimum Capital Requirements (MCR). The evaluation metrics focus on accuracy percentages for information extraction and calculation correctness.

The findings reveal that GPT-4 and Claude-3-Opus significantly outperform GPT-3.5 and Gemini-1.5-Pro in identifying regulatory elements, with GPT-4 achieving 95% accuracy in complex MCR calculations. The study highlights that converting PDFs to images markedly improves LLM performance in parsing mathematical formulas and tables. Detailed prompt engineering, incorporating role definition, input, goal, method, and significance, is shown to be critical for accuracy, especially in identifying correlations and risk buckets. Limitations include the reliance on manually simulated data rather than real-world proprietary datasets and the potential for errors in mathematical reasoning, which remains a challenge for most LLMs. The paper also discusses ethical considerations such as data privacy and transparency in deploying LLMs for regulatory compliance.

## Automate Strategy Finding with LLM in Quant investment

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: alpha mining, portfolio optimization, factor modeling, equities, china market, us equities, agentic workflow, multi-agent systems, backtesting, fine-tuning, ohlc data, financial statements, backtest, sharpe ratio, portfolio returns, framework, open source, overfitting, model risk, sse50
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "financial statements"], "deliverable": ["framework", "open source"], "evaluation": ["backtest", "sharpe ratio", "portfolio returns"], "market_context": ["china market", "us equities"], "method": ["agentic workflow", "multi-agent systems", "backtesting", "fine-tuning"], "risk_issue": ["overfitting", "model risk"], "task": ["alpha mining", "portfolio optimization", "factor modeling"]}
- One-line summary: The paper proposes a three-stage LLM-driven multi-agent framework for automated alpha factor generation and dynamic weight optimization, achieving 53.17% cumulative return on the SSE50 index by adapting to market regimes.

### Detailed Summary

The paper addresses the rigidity and brittleness of traditional deep learning models in quantitative finance by proposing an automated strategy finding framework. It leverages Large Language Models (LLMs) within a risk-aware multi-agent system to generate executable alpha factor candidates from diverse financial data, aiming to overcome the limitations of static factor models in dynamic market environments. The core innovation lies in combining LLM-based exploratory alpha mining with multi-agent evaluation and dynamic weight optimization to create a scalable architecture for financial signal extraction and portfolio construction.

The methodology consists of three stages: First, an LLM-based Seed Alpha Factory (SAF) generates and categorizes 100 seed alphas across nine domains (e.g., Momentum, Fundamental) from multimodal financial research documents. Second, a multi-agent system comprising a Confidence Score Agent (CSA) and a Risk Preference Agent (RPA) evaluates these alphas using historical backtesting metrics like Information Coefficient (IC) and Sharpe Ratio, selecting factors based on market status and category balance. Third, a 3-layer Multi-Layer Perceptron (MLP) optimizes the weights of selected alphas to predict future yields. Experiments were conducted on SSE50, CSI300, and SP500 indices using OHLCV data, financial reports, and macroeconomic indicators from 2019 to 2024.

The framework significantly outperformed benchmarks, achieving a 53.17% cumulative return on SSE50 (Jan 2023-Jan 2024) compared to the index's -13.22% loss, with superior risk-adjusted metrics (Sharpe: 0.287, Calmar: 1.052). It demonstrated robustness across Chinese and US markets, maintaining positive returns during downturns where benchmarks declined. However, limitations include reliance on input document quality, potential lack of financial intuition in LLM-generated alphas, and the assumption of persistent historical relationships between market conditions and alpha performance, which may fail during regime shifts. The system is primarily equity-focused, with cross-asset applicability requiring further investigation.

## Deficiency of Large Language Models in Finance: An Empirical Examination of Hallucination

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, financial question answering, equities, us equities, tool use, prompt engineering, sec filings, market prices, accuracy, backtest, benchmark, dataset, hallucination, factuality, reliability, api integration
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "market prices"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "backtest"], "market_context": ["us equities"], "method": ["tool use", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["stock prediction", "financial question answering"]}
- One-line summary: This paper empirically demonstrates that off-the-shelf LLMs suffer from severe hallucinations in financial tasks, but accuracy can be significantly restored using Retrieval Augmented Generation (RAG) and prompt-based tool learning for external API calls.

### Detailed Summary

The paper addresses the critical issue of hallucination in Large Language Models (LLMs) when applied to the finance domain, where factual accuracy is paramount. It positions the study as an empirical examination of FinLLM reliability, highlighting that while LLMs show promise, their tendency to generate plausible but incorrect information poses significant risks for monetary loss and trust erosion. The authors argue that existing research lacks sufficient empirical investigation into the specific nature and extent of these hallucinations in financial contexts, necessitating a rigorous benchmark to assess model capabilities and failure modes.

The methodology involves evaluating several models, including Llama2, GPT-3.5, GPT-4, and the domain-specific FinMA, across three distinct financial tasks: financial abbreviation recognition, financial term explanation, and historical stock price querying. The authors employ metrics such as accuracy, FactScore for factual consistency, and Mean Absolute Error (MAE) for price predictions. To mitigate hallucinations, they test four strategies: few-shot learning, Decoding by Contrasting Layers (DoLa), Retrieval Augmented Generation (RAG) using Wikipedia, and prompt-based tool learning to generate Python function calls for the Alpha Vantage API.

The findings reveal that general-purpose LLMs exhibit serious hallucination behaviors, with domain-specific fine-tuning (FinMA) sometimes degrading general instruction-following abilities. However, RAG significantly improves factuality in knowledge-intensive tasks, and prompt-based tool learning achieves near-perfect accuracy in stock price queries by delegating data retrieval to external APIs. The study concludes that while LLMs alone are unreliable for precise financial data, integrating external tools and retrieval mechanisms is essential for deploying them safely in finance. Limitations include the narrow scope of tasks and the task-specific nature of the mitigation strategies tested.

## A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification

- Year: 2025
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, equity research, equities, us equities, instruction tuning, fine-tuning, domain adaptation, sec filings, news, accuracy, benchmark, model, overfitting, financial text classification, model merging, catastrophic forgetting, open source models
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "model"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["instruction tuning", "fine-tuning", "domain adaptation"], "risk_issue": ["overfitting"], "task": ["sentiment analysis", "equity research"]}
- One-line summary: The paper demonstrates that instruction fine-tuning smaller open-source LLMs like Mistral-7B and Llama3-8B significantly improves financial text classification, with model merging via MergeKit effectively mitigating catastrophic forgetting on unseen tasks.

### Detailed Summary

This study addresses the challenge of adapting general-domain Large Language Models to specialized financial text classification tasks, where technical terminology and complex reasoning often cause performance degradation. The authors investigate the efficacy of instruction fine-tuning smaller-scale models, specifically Mistral-7B, Llama3-8B, and Phi-3-mini, comparing both base and instruction-tuned variants. The research aims to determine if efficient, resource-light fine-tuning can match or exceed proprietary models like GPT-4 while maintaining generalization capabilities on unseen financial tasks, thereby offering a scalable alternative to training from scratch or using massive proprietary models.

The experimental design involves fine-tuning models on four core financial classification tasks: sentiment analysis (using Financial PhraseBank and FiQA-SA), news headline classification (Headline-Dir), relation extraction (FinRED), and hawkish-dovish policy classification (FOMC). The authors employ Low-Rank Adaptation (LoRA) for efficient training and evaluate performance using accuracy and weighted F1 scores. To assess generalization, they test zero-shot performance on three unseen tasks: argument unit classification (FinArg), deal completeness in M&A news (M&A dataset), and causal classification in SEC filings (FinCausual). Additionally, they implement model merging using the MergeKit framework, combining single-task fine-tuned models with vanilla instruction models to preserve zero-shot capabilities.

Results indicate that instruction fine-tuning yields substantial improvements over zero-shot baselines, with fine-tuned models often outperforming GPT-4 on specific tasks like relation extraction and hawkish-dovish classification. However, base model fine-tuning suffered from significant catastrophic forgetting on unseen tasks, whereas instruction-tuned models remained more robust. Model merging successfully mitigated this degradation, with the merged Mistral-7B model exceeding its original zero-shot accuracy on several unseen datasets. The study concludes that instruction fine-tuning combined with model merging is a highly effective, resource-efficient strategy for deploying domain-specific LLMs in finance, though performance on long-tail relation extraction tasks remains a challenge.

## Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance

- Year: 2025
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, sentiment analysis, fine-tuning, domain adaptation, annual reports, news, accuracy, benchmark, dataset, model, low-resource language, multilingual, named entity recognition, summarization
- Tag facets: {"asset_class": [], "data_source": ["annual reports", "news"], "deliverable": ["benchmark", "dataset", "model"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "domain adaptation"], "risk_issue": [], "task": ["financial question answering", "sentiment analysis"]}
- One-line summary: The paper introduces Plutus-ben, the first Greek financial NLP benchmark, and Plutus-8B, a fine-tuned Greek financial LLM, demonstrating that domain-specific training significantly outperforms general multilingual models in low-resource financial contexts.

### Detailed Summary

This paper addresses the critical gap in low-resource financial NLP by introducing Plutus-ben, the first comprehensive evaluation benchmark for Greek financial language processing. The authors argue that existing multilingual models fail to capture the linguistic complexity and domain-specific reasoning required for Greek financial texts, which are central to international trade and maritime finance. To solve this, they construct a rigorous benchmark covering five core tasks: numeric and textual named entity recognition, question answering, abstractive summarization, and topic classification. The work positions itself as a foundational resource for multilingual inclusivity in finance, providing the necessary infrastructure to assess and improve LLM capabilities in under-resourced languages.

The methodology involves curating four new high-quality datasets (GRFinNUM, GRFinNER, GRFinQA, and GRFinSUM) annotated by expert native Greek speakers with financial expertise, supplemented by two existing resources. The authors fine-tune Llama-Krikri-8B using Low-Rank Adaptation on an instruction dataset derived from these sources to create Plutus-8B. They conduct a comprehensive evaluation of 22 diverse LLMs, including proprietary models like GPT-4 and open-source variants, measuring performance via Entity F1, Accuracy, and Rouge-1. The experimental design isolates the impact of domain adaptation by comparing Greek-general models against English-financial models and the newly proposed Greek-financial model.

Results reveal that even top-tier models like GPT-4o struggle with Greek financial reasoning, with smaller models failing entirely on NER tasks. Plutus-8B achieves state-of-the-art performance, surpassing GPT-4 by 15.38% and GPT-4o by 46.34%, proving that domain-specific fine-tuning is essential for low-resource financial NLP. However, the study highlights significant limitations, particularly in abstractive summarization where all models struggle with long-form documents. The findings underscore the limitations of cross-lingual transfer and the necessity for financial expertise in Greek-trained models, offering a valuable case study for deploying LLMs in specialized, low-resource linguistic markets.

## Large Language Models in equity markets: applications, techniques, and insights

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, portfolio optimization, algorithmic trading, equities, us equities, multi-agent systems, reinforcement learning, fine-tuning, prompt engineering, news, earnings calls, social media, financial statements, backtest, literature review, bias, multi-modal data, hybrid modeling, scalability
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "earnings calls", "social media", "financial statements"], "deliverable": ["literature review"], "evaluation": ["backtest"], "market_context": ["us equities"], "method": ["multi-agent systems", "reinforcement learning", "fine-tuning", "prompt engineering"], "risk_issue": ["bias"], "task": ["sentiment analysis", "stock prediction", "portfolio optimization", "algorithmic trading"]}
- One-line summary: This 2025 review synthesizes 84 studies on LLM applications in equity markets, categorizing them by financial use cases and technical methods to identify trends in forecasting, sentiment analysis, and multi-agent trading while highlighting gaps in real-world validation and interpretability.

### Detailed Summary

This paper addresses the fragmentation in research regarding Large Language Models (LLMs) in equity investing by providing a comprehensive review of 84 studies published between 2022 and early 2025. The authors aim to map the intersection of LLMs and equity markets, addressing key questions about application trends, technical innovations, and existing limitations. The review positions LLMs as transformative tools that shift investment from manual, structured analysis to automated, real-time insights derived from multimodal data, including news, earnings transcripts, and social media. It emphasizes the potential for LLMs to enhance market responsiveness, risk management, and alpha generation through dynamic, self-learning systems powered by reinforcement learning and multi-agent frameworks.

The methodology involves a dual-layered categorization of the selected literature. First, studies are grouped by financial applications, such as stock price forecasting, sentiment analysis, portfolio management, and algorithmic trading. Second, they are classified by technical methodologies, including prompting, fine-tuning, multi-agent frameworks, reinforcement learning, and custom architectures. The authors consolidate findings on datasets used, ranging from financial statements to multimodal data, and systematically compare general-purpose versus finance-specialized LLMs. The review evaluates empirical contributions and methodological innovations, analyzing how LLMs integrate qualitative textual data with structured financial indicators to improve predictive accuracy and generate actionable market signals.

Key findings indicate that LLMs significantly improve sentiment extraction and can generate alpha when combined with reinforcement learning to factor market feedback. However, the review identifies critical gaps in scalability, interpretability, and real-world validation. Many studies rely on simulated environments or historical data, lacking robust evaluation frameworks for live trading. The authors highlight the importance of hybrid modeling approaches and architectures that leverage large context windows for complex reasoning. Limitations include data reliability, potential biases, and the challenge of adapting LLMs to diverse investment strategies and asset classes. The paper concludes by proposing future research directions, emphasizing the need for robust evaluation frameworks and transparent, efficient AI-driven financial strategies.

## FinNLI: Novel Dataset for Multi-Genre Financial Natural Language Inference Benchmarking

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, risk extraction, earnings analysis, chain of thought, instruction tuning, prompt engineering, 10-k filings, annual reports, earnings calls, sec filings, accuracy, benchmark, dataset, hallucination, overfitting, natural language inference, domain adaptation, spurious correlations
- Tag facets: {"asset_class": [], "data_source": ["10-k filings", "annual reports", "earnings calls", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["chain of thought", "instruction tuning", "prompt engineering"], "risk_issue": ["hallucination", "overfitting"], "task": ["benchmarking", "risk extraction", "earnings analysis"]}
- One-line summary: FinNLI is a novel benchmark dataset for Financial Natural Language Inference comprising 21,304 premise-hypothesis pairs from SEC filings, annual reports, and earnings calls, revealing that current LLMs struggle with financial reasoning and that instruction-tuned financial models often underperform general-domain baselines.

### Detailed Summary

The paper addresses the lack of dedicated benchmarks for Financial Natural Language Inference (FinNLI), a critical task for risk assessment and automated reporting. While general-domain NLI datasets exist, they fail to capture the nuances of financial texts, such as complex terminology and implicit causal relationships. The authors introduce FinNLI to evaluate how well language models can infer logical relationships (entailment, neutral, contradiction) within diverse financial genres, filling a gap in evaluating domain-specific reasoning capabilities beyond simple sentiment or extraction tasks.

The dataset construction involves sampling premises from SEC filings, annual reports, and earnings call transcripts. Hypotheses are synthetically generated using GPT-4 and Llama 3.1 70B with varied roles and writing styles, followed by Z-filtering to remove spurious correlations. A high-quality test set of 3,304 instances is annotated by finance experts. The authors evaluate a range of models, including zero-shot general-domain NLI models, fine-tuned Pre-trained Language Models (PLMs) like RoBERTa and FiLM, and various LLMs (Llama, Phi, FinMA) using different prompting strategies like Chain-of-Thought and few-shot learning.

Results show that domain shift significantly degrades general-domain NLI performance, with the best Macro F1 score being 78.62% for Llama 3.1 70B. Surprisingly, instruction-tuned financial LLMs (FinMA) performed poorly, suggesting limited generalizability of domain-specific tuning. The study highlights that smaller models like Phi-3.5 can compete with larger ones, and that Chain-of-Thought prompting benefits smaller LLMs but not the largest ones. The dataset exposes significant weaknesses in current LLMs for financial reasoning, indicating substantial room for improvement in handling complex financial logic and avoiding spurious correlations.

## MarS: a Financial Market Simulation Engine Powered by Generative Foundation Model

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Simulation and Execution Infrastructure
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: market simulation, forecasting, execution analysis, equities, china market, market microstructure, high-frequency trading, reinforcement learning, symbolic regression, limit order book, backtest, market impact, accuracy, simulator, benchmark, dataset, model, overfitting, large market model, mars
- Tag facets: {"asset_class": ["equities"], "data_source": ["limit order book"], "deliverable": ["simulator", "benchmark", "dataset", "model"], "evaluation": ["backtest", "market impact", "accuracy"], "market_context": ["china market", "market microstructure", "high-frequency trading"], "method": ["reinforcement learning", "symbolic regression"], "risk_issue": ["overfitting"], "task": ["market simulation", "forecasting", "execution analysis"]}
- One-line summary: The paper introduces MarS, a financial market simulation engine powered by the Large Market Model (LMM), which generates realistic, interactive, and controllable order-level market trajectories to enable forecasting, risk detection, market impact analysis, and reinforcement learning agent training.

### Detailed Summary

This paper addresses the lack of high-fidelity, interactive simulators for financial markets by proposing the Large Market Model (LMM), a generative foundation model for order-level simulation. Unlike traditional statistical or agent-based models, LMM treats market dynamics as a conditional generation task, leveraging the finest structured data available: individual trading orders and Limit Order Book (LOB) states. The architecture combines an Order Model, which uses causal transformers to tokenize and predict individual orders based on LOB features, with an Order-Batch Model that employs VQ-VAE to represent aggregated trading behaviors as image-like structures. These components are integrated into an ensemble framework that balances fine-grained control with macro-level market trends, enabling the simulation of complex market effects and participant behaviors in a risk-free virtual environment.

The authors evaluate MarS using high-frequency order-level data from Chinese stock markets, validating its realism against eleven stylized facts including aggregational Gaussianity, volatility clustering, and heavy tails. Experiments demonstrate that LMM scales effectively with data size and model complexity, following established scaling laws. The system supports interactive simulations where user-injected orders are matched in a simulated clearing house, allowing for the assessment of market impact. Results show that synthetic market impact adheres to the Square-Root-Law and that MarS can replicate historical events with high correlation when provided with control signals. The model outperforms baselines like DeepLOB in trend prediction by aggregating multiple simulated trajectories, highlighting the advantage of simulation-based forecasting over direct sequence extrapolation.

MarS is showcased in four key applications: forecasting market trends, detecting market manipulation via distribution similarity drops, analyzing market impact through symbolic regression on synthetic data, and training reinforcement learning agents for order execution. The paper identifies new factors influencing market impact, such as resiliency and LOB pressure, beyond traditional volume-based metrics. However, limitations include the current reliance on specific market microstructures and the need for comprehensive evaluation of detection systems. The work represents a paradigm shift by providing a unified, data-driven pipeline for diverse financial tasks, offering infinite synthetic data for strategy testing and risk management without the costs and risks of live trading.

## FinBERT: A Pre-trained Financial Language Representation Model for Financial Text Mining

- Year: 2020
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, financial question answering, fine-tuning, domain adaptation, news, social media, accuracy, ablation study, model, dataset, benchmark, text mining, pre-training, nlp, bert, self-supervised learning
- Tag facets: {"asset_class": [], "data_source": ["news", "social media"], "deliverable": ["model", "dataset", "benchmark"], "evaluation": ["accuracy", "ablation study"], "market_context": [], "method": ["fine-tuning", "domain adaptation"], "risk_issue": [], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: FinBERT is a domain-specific BERT model pre-trained on large-scale financial corpora using six multi-task self-supervised objectives, achieving state-of-the-art performance on financial sentence boundary detection, sentiment analysis, and question answering benchmarks.

### Detailed Summary

The paper addresses the challenge of applying deep learning to financial text mining, where labeled data is scarce and general-domain language models fail to capture financial semantics. The authors propose FinBERT, a pre-trained language model that combines general and financial corpora. Unlike standard BERT, FinBERT employs six multi-task self-supervised pre-training objectives: Span Replace Prediction, Capitalization Prediction, Token-Passage Prediction, Sentence Deshuffling, Sentence Distance, and Dialogue Relation. This design aims to better capture financial vocabulary, named entities, and semantic structures. The model is trained using mixed precision on a distributed Horovod framework to handle the large corpus size efficiently.

The pre-training data includes over 61 GB of text from five sources: English Wikipedia, BooksCorpus, FinancialWeb (news), YahooFinance, and RedditFinanceQA. The model is evaluated on three downstream tasks: Financial Sentence Boundary Detection (FinSBD), Financial Sentiment Analysis (Financial PhraseBank and FiQA), and Financial Question Answering (FiQA Task 2). Experiments compare FinBERT against rule-based, BiLSTM-CRF, and standard BERT baselines. The study also includes ablation studies to assess the impact of pre-training and performance on small training data scenarios, simulating low-resource financial environments.

FinBERT significantly outperforms all state-of-the-art models across all three tasks. On Sentence Boundary Detection, FinBERT Large achieved a mean F1 score of 0.970, surpassing BERT-S by 0.085. For Sentiment Analysis, it reached 0.94 accuracy on PhraseBank and superior R-squared scores on FiQA. In Question Answering, it achieved an nDCG of 0.76 and MRR of 0.68, vastly improving upon previous methods. The model demonstrates robustness even with small training corpora. However, the paper notes that collecting labeled data remains expensive, and the model's effectiveness relies heavily on the quality and diversity of the pre-training financial corpora. The source code and models are publicly available.

## Can Large Language Models beat wall street? Evaluating GPT-4’s impact on financial decision-making with MarketSenseAI

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, alpha mining, equity research, equities, us equities, portfolio management, chain of thought, agentic workflow, news, financial statements, backtest, portfolio returns, sharpe ratio, transaction costs, framework, trading agent, overfitting, explainable ai, signal evaluation
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "financial statements"], "deliverable": ["framework", "trading agent"], "evaluation": ["backtest", "portfolio returns", "sharpe ratio", "transaction costs"], "market_context": ["us equities", "portfolio management"], "method": ["chain of thought", "agentic workflow"], "risk_issue": ["overfitting"], "task": ["stock prediction", "alpha mining", "equity research"]}
- One-line summary: MarketSenseAI leverages GPT-4 with Chain of Thought and In-Context Learning to analyze multi-source financial data for stock selection, achieving up to 72% cumulative returns and 10-30% excess alpha on S&P 100 stocks over 15 months.

### Detailed Summary

This paper addresses the challenge of effective stock selection in complex markets by introducing MarketSenseAI, a framework that emulates expert investment decision-making using GPT-4. The system integrates Chain of Thought and In-Context Learning to process diverse data sources, including market trends, news, fundamentals, and macroeconomic factors. By generating actionable and interpretable investment signals, the framework aims to mitigate human cognitive biases and enhance the quality of financial analysis for both retail and professional investors. The approach bridges domain knowledge with advanced AI reasoning to provide holistic stock insights.

The methodology employs a modular architecture with five core components: a Progressive News Summarizer, a Fundamentals Summarizer, a Stock Price Dynamics Summarizer, a Macroeconomic Summarizer, and a final recommendation engine. Data is sourced from EODHD APIs for news and fundamentals, while peer stocks are identified using MPNet embeddings. The system was empirically tested on S&P 100 stocks over a 15-month period. GPT-4 was used not only for prediction but also as a signal evaluator to rank the quality of explanations. Performance was measured against benchmarks like the S&P 500 and various naive strategies, accounting for transaction costs.

Results demonstrate exceptional performance, with the top strategy achieving a cumulative return of 72.87% (71.64% after costs) and an excess alpha of 10-30%, while maintaining a risk profile comparable to the broader market. The study highlights the value of AI-generated explanations in improving signal reliability and acceptance. However, limitations include the short evaluation period, potential overfitting to specific market conditions, and the commercial affiliation of the authors. The findings suggest significant potential for LLMs in financial analytics but call for extended research across diverse market environments.

## Large Language Models for Financial and Investment Management: Applications and Benchmarks

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, forecasting, portfolio optimization, spreadsheet reasoning, equities, portfolio management, knowledge graph, time-series modeling, agentic workflow, news, social media, tables, benchmark, dataset, literature review, model risk, multimodal modeling, financial question answering
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media", "tables"], "deliverable": ["benchmark", "dataset", "literature review"], "evaluation": [], "market_context": ["portfolio management"], "method": ["knowledge graph", "time-series modeling", "agentic workflow"], "risk_issue": ["model risk"], "task": ["sentiment analysis", "forecasting", "portfolio optimization", "spreadsheet reasoning"]}
- One-line summary: This survey systematically categorizes and reviews the applications of large language models in finance, covering linguistic tasks, sentiment analysis, time series forecasting, reasoning, and agent-based modeling, while providing a comprehensive collection of associated datasets, benchmarks, and code to facilitate research and adoption.

### Detailed Summary

The paper addresses the urgent need for a systematic examination of large language models in finance, bridging the gap between cutting-edge AI technology and practical implementation in investment management. It aims to synthesize recent developments to help researchers and practitioners understand the diverse applications, methodologies, and impacts of LLMs, which are transforming traditional financial practices through contextual understanding and content generation. The authors position this work as a holistic, application-driven review that fills gaps left by existing surveys, which often lack deep dives into practical challenges or broader implications for financial decision-making.

The methodology involves a comprehensive categorization of existing literature into five key application areas: linguistic tasks, sentiment analysis, financial time series, financial reasoning, and agent-based modeling. For each area, the authors analyze specific methodologies such as textual analysis, knowledge-based analysis, forecasting, data augmentation, planning, decision support, and simulations. The paper also compiles a collection of datasets, benchmarks, and code associated with mainstream applications, offering valuable resources for the community. It reviews the evolution from pre-LLM methods to transformer-based architectures, highlighting advancements in handling long documents, multimodal data, and domain-specific adaptations.

Key findings indicate that LLMs excel in summarizing complex financial narratives, extracting entities, and quantifying market sentiment, which can enhance investment performance. They are also shown to support financial planning, generate investment recommendations, and simulate market behaviors through agent-based modeling. However, the paper notes that consensus has not yet formed on which applications will most impact current practices, and many efforts are at an early stage. Limitations include challenges with multimodal document structures, high computational costs, and the need for robust evaluation benchmarks. The work serves as a foundational resource for understanding the current state and future potential of LLMs in finance.

## Assessing Look-Ahead Bias in Stock Return Predictions Generated by GPT Sentiment Analysis

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, equities, us equities, prompt engineering, backtesting, news, sec filings, backtest, portfolio returns, market impact, dataset, benchmark, look-ahead bias, data leakage, distraction effect, entity anonymization, llm bias mitigation
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "sec filings"], "deliverable": ["dataset", "benchmark"], "evaluation": ["backtest", "portfolio returns", "market impact"], "market_context": ["us equities"], "method": ["prompt engineering", "backtesting"], "risk_issue": ["look-ahead bias", "data leakage"], "task": ["sentiment analysis", "stock prediction"]}
- One-line summary: The paper demonstrates that anonymizing company names in news headlines mitigates the 'distraction effect' in GPT-3.5 sentiment analysis, leading to superior in-sample trading performance compared to original headlines where look-ahead bias is outweighed by negative interference from the model's pre-existing knowledge.

### Detailed Summary

The paper addresses the critical challenge of evaluating Large Language Models (LLMs) for financial sentiment analysis, specifically focusing on biases introduced when backtesting strategies using data within the model's training window. The authors identify two distinct sources of bias: look-ahead bias, where the LLM memorizes specific future stock returns associated with a news event, and the distraction effect, where the LLM's general pre-existing knowledge about a company interferes with its objective assessment of the news text's sentiment. The research aims to quantify these biases and propose a mitigation strategy to ensure that backtesting results reflect genuine predictive power rather than data leakage or overconfidence.

The methodology employs GPT-3.5 to analyze sentiment in two datasets of financial news headlines: a scraped dataset from RavenPack/Dow Jones and a Thomson Reuters dataset covering S&P 500 companies. The core experimental design involves an anonymization procedure that replaces company names and related product identifiers with random strings (e.g., "Blahblahblah") using fuzzy string matching and Google Knowledge Graph queries. The authors implement long-short, long-only, and short-only trading strategies based on GPT's sentiment scores derived from both original and anonymized headlines. Performance is evaluated over an in-sample period (Jan 2015–Sep 2021) and an out-of-sample period (Oct 2021–Dec 2022), comparing average daily returns, classification accuracy, and market betas.

The findings reveal that anonymized headlines significantly outperform original headlines in-sample, indicating that the negative distraction effect dominates the positive look-ahead bias. This effect is more pronounced for larger companies, where the LLM has greater general knowledge. The original strategy suffers from overconfidence, making large losses when it misjudges sentiment due to pre-existing knowledge, whereas the anonymized strategy often defaults to neutral, avoiding these trades. Out-of-sample, the difference is less statistically significant but still favors anonymization for larger firms, suggesting the distraction effect persists even outside the training window. The study concludes that entity anonymization is a viable tool for debiased backtesting and potentially improving out-of-sample sentiment analysis.


## Temporal Data Meets LLM - Explainable Financial Time Series Forecasting

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, forecasting, equities, us equities, chain of thought, fine-tuning, prompt engineering, time-series modeling, news, ohlc data, accuracy, dataset, model, overfitting, explainable ai, multi-modal, nasdaq-100
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "ohlc data"], "deliverable": ["dataset", "model"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["chain of thought", "fine-tuning", "prompt engineering", "time-series modeling"], "risk_issue": ["overfitting"], "task": ["stock prediction", "forecasting"]}
- One-line summary: This paper demonstrates that LLMs, particularly GPT-4 with Chain-of-Thought prompting, can outperform traditional statistical and machine learning baselines in forecasting NASDAQ-100 stock returns while providing human-readable explanations derived from multi-modal financial data.

### Detailed Summary

The paper addresses the challenge of explainable financial time series forecasting, aiming to overcome the limitations of black-box models and the difficulty of integrating multi-modal signals like news and price history. It positions Large Language Models as a unified solution capable of cross-sequence reasoning and generating interpretable outputs, focusing specifically on NASDAQ-100 stocks. The research problem centers on whether LLMs can effectively leverage textual and numerical data to predict future price movements with greater accuracy and transparency than conventional methods.

The methodology involves forecasting weekly and monthly stock returns for NASDAQ-100 constituents using historical price data, company metadata, and aggregated financial news. The authors employ GPT-4 for zero-shot and few-shot inference, incorporating Chain-of-Thought (COT) prompting to enhance reasoning. Additionally, they fine-tune the open-source Open LLaMA 13B model on a dataset of 37,000 examples derived from five years of historical data. Baselines include a most-frequent heuristic, ARMA-GARCH, and a LightGBM gradient-boosting tree model with approximately 300 features. Evaluation metrics include binary precision, bin precision, Mean Squared Error (MSE) of bin ordinals, and ROUGE scores for explanation quality.

Results indicate that GPT-4 with few-shot learning and COT achieves the highest performance, significantly outperforming the LightGBM baseline in both prediction accuracy and explanation quality. The fine-tuned Open LLaMA model also shows competitive performance, particularly in binary classification, though it tends to produce more extreme predictions. The study highlights that COT improves performance by enabling the model to identify crucial factors like earnings reports. Limitations include the reliance on GPT-4 for data preprocessing and the tendency of smaller models to overfit to extreme bins, suggesting that while LLMs offer explainability and strong performance, they require careful prompt engineering and potentially fine-tuning for cost-effective deployment.

## FinBERT-FOMC: Fine-Tuned FinBERT Model with Sentiment Focus Method for Enhancing Sentiment Analysis of FOMC Minutes

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, fine-tuning, prompt engineering, sec filings, accuracy, model, dataset, bias, central bank communications, text simplification
- Tag facets: {"asset_class": [], "data_source": ["sec filings"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "prompt engineering"], "risk_issue": ["bias"], "task": ["sentiment analysis"]}
- One-line summary: The paper introduces FinBERT-FOMC, a fine-tuned FinBERT model enhanced with a Sentiment Focus preprocessing method, which significantly improves sentiment classification accuracy on complex FOMC Minutes sentences containing contrasting conjunctions.

### Detailed Summary

This research addresses the challenge of accurately analyzing sentiment in complex financial texts, specifically Federal Open Market Committee (FOMC) Minutes, where standard models struggle with nuanced, contradictory sentences. The authors identify that FinBERT, while effective for simple financial statements, misclassifies sentences containing disjunctive conjunctions like 'but', 'while', and 'though' because it fails to isolate the primary sentiment-bearing clause. The study aims to enhance predictive performance by combining a novel text simplification strategy with domain-specific fine-tuning, targeting the specific linguistic complexities inherent in central bank communications.

The methodology involves curating a dataset of 32,330 sentences from FOMC Minutes (2006-2023) and manually labeling a test set of 1,375 entries. The core innovation is the Sentiment Focus (SF) method, a preprocessing step that removes clauses preceding contrasting conjunctions to simplify sentence structure before classification. The authors fine-tuned FinBERT on a subset of 3,535 complex sentences processed with SF. Experiments compared the original FinBERT, FinBERT with SF preprocessing, and the fine-tuned FinBERT-FOMC model using accuracy as the primary metric on the manually labeled test set.

Results show that the fine-tuned FinBERT-FOMC model achieved an overall accuracy of 88.29%, a 5% improvement over the original FinBERT's 84.07%. The improvement was most pronounced for complex sentences, where the fine-tuned model outperformed the original by 17.4% (87.1% vs. 74.2% accuracy). Specifically, accuracy on sentences with 'but' rose from 67.3% to 86.1%, and on 'though' from 73.1% to 90.4%. The study concludes that simplifying complex syntax via SF and fine-tuning on domain-specific complex examples significantly enhances sentiment analysis robustness, though limitations include the small manual test set and lack of generalization testing on other financial document types.

## A Survey on Large Language Models for Critical Societal Domains: Finance, Healthcare, and Law

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, fraud detection, financial question answering, instruction tuning, domain adaptation, sec filings, news, accuracy, literature review, taxonomy, hallucination, bias, privacy, regulatory compliance, multimodal modeling, information extraction
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "news"], "deliverable": ["literature review", "taxonomy"], "evaluation": ["accuracy"], "market_context": [], "method": ["instruction tuning", "domain adaptation"], "risk_issue": ["hallucination", "bias", "privacy", "regulatory compliance"], "task": ["sentiment analysis", "stock prediction", "fraud detection", "financial question answering"]}
- One-line summary: This survey provides a comprehensive review of large language models in finance, healthcare, and law, categorizing tasks, models, and ethical challenges to guide future interdisciplinary research in high-stakes domains.

### Detailed Summary

The paper addresses the critical need to understand how large language models are transforming high-stakes societal domains: finance, healthcare, and law. It positions LLMs as transformative tools that require specialized handling due to the domains' reliance on professional expertise, confidential data, multimodal documents, strict regulatory compliance, and the necessity for explainability and fairness. The survey aims to unify the fragmented literature by offering a structured overview of methodologies, applications, and ethical considerations across these three sectors, highlighting their shared challenges and unique requirements.

The methodology involves a systematic categorization of existing literature into tasks, datasets, model architectures, and evaluation metrics. In finance, it details tasks such as sentiment analysis, information extraction, question answering, and stock movement prediction, reviewing models like FinBERT, BloombergGPT, and FinMA. The paper analyzes training paradigms, including pre-training on financial corpora and instruction fine-tuning. It also covers healthcare tasks like diagnostic support and legal tasks like contract review, emphasizing the shift from general NLP to domain-specific LLMs. Experiments cited include performance comparisons on benchmarks like FinQA and TAT-QA, and evaluations of proprietary models like BloombergGPT against open-source baselines.

Key findings indicate that while LLMs show promise in enhancing financial analytics and legal interpretation, they face significant hurdles in numerical reasoning, hallucination, and regulatory compliance. The survey identifies under-explored areas such as financial fraud detection and risk assessment. It concludes that future research must prioritize interdisciplinary cooperation, robust ethical frameworks, and methodological advancements to ensure transparent, fair, and robust AI systems. The paper provides a curated reading list and emphasizes the importance of addressing data privacy and bias to mitigate risks in precision-dependent sectors.

## Benchmarking Large Language Models on CFLUE - A Chinese Financial Language Understanding Evaluation Dataset

- Year: 2024
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, financial question answering, fine-tuning, prompt engineering, sec filings, accuracy, benchmark, dataset, chinese financial nlp, llm evaluation, multilingual finance
- Tag facets: {"asset_class": [], "data_source": ["sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "prompt engineering"], "risk_issue": [], "task": ["benchmarking", "financial question answering"]}
- One-line summary: The paper introduces CFLUE, a comprehensive Chinese financial LLM benchmark with 38K+ knowledge questions and 16K+ application tasks, revealing that while GPT-4 leads in knowledge, lightweight models often match or exceed it in application tasks, and specialized financial LLMs underperform general ones.

### Detailed Summary

The paper addresses the lack of comprehensive evaluation benchmarks for Large Language Models (LLMs) in the Chinese financial domain. Existing datasets are limited in size, diversity, or task scope, focusing primarily on multiple-choice questions or event extraction. The authors propose CFLUE (Chinese Financial Language Understanding Evaluation) to provide a robust, multi-dimensional assessment tool that covers both financial knowledge retention and practical NLP application capabilities, filling a critical gap for evaluating Chinese-language financial AI systems.

CFLUE comprises two main components: a knowledge assessment with 38,636 multiple-choice questions from 15 types of professional qualification exams, including answer prediction and reasoning explanations; and an application assessment with 16,522 instances across five NLP tasks: text classification, machine translation, relation extraction, reading comprehension, and text generation. The dataset was carefully curated to mitigate contamination by using recent data and rephrasing questions. The authors evaluated 15 LLMs, including OpenAI models, lightweight general-domain models (e.g., Qwen, LLaMA), and specialized financial LLMs (e.g., FinGPT, Tongyi-Finance), using metrics like accuracy, F1, BLEU, and ROUGE.

Results show that GPT-4 and GPT-4-turbo are the top performers in knowledge assessment, achieving over 60% accuracy, indicating significant room for improvement in current LLMs. However, in application assessment, the advantage of GPT-4 over lightweight models diminishes, with models like Qwen-72B and ChatGLM3-6B performing competitively. Notably, specialized financial LLMs underperformed general-domain models, suggesting that domain-specific fine-tuning on limited corpora may not capture broad financial knowledge effectively. Fine-tuning general models on CFLUE data significantly boosted their performance, allowing smaller models to surpass larger proprietary models in certain tasks.

## Self-explanatory and Retrieval-augmented LLMs for Financial Sentiment Analysis

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, financial question answering, retrieval, fine-tuning, news, accuracy, framework, open source, benchmark, hallucination
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["framework", "open source", "benchmark"], "evaluation": ["accuracy"], "market_context": [], "method": ["retrieval", "rag", "fine-tuning"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: The paper introduces FLEX, a retrieval-augmented framework that enriches financial sentences with explicit knowledge using LLMs, significantly improving financial sentiment analysis accuracy across zero-shot, few-shot, and fine-tuning settings.

### Detailed Summary

Financial sentiment analysis (FSA) faces challenges due to the brevity of financial texts and the implicit nature of sentiment, which often leads to inconsistent predictions by Large Language Models (LLMs). The paper addresses this by proposing FLEX (Financial Language Enhancement with Guided LLM Execution), a system that retrieves qualitative knowledge from an LLM to enrich input sentences. This enrichment makes sentences more knowledge-dense and explicit, preserving original meaning while clarifying financial concepts. The core problem is bridging the gap between general LLM capabilities and the specific, context-heavy requirements of financial text interpretation.

The FLEX framework operates in two phases: MAKEUP and MAKEUP SELECTION. In the MAKEUP phase, an LLM generates multiple candidate sentences enriched with relevant financial context. The MAKEUP SELECTION phase then filters these candidates using a novel logic combining semantic similarity (via cosine similarity of embeddings) and perplexity (measuring naturalness and clarity). This selection process mitigates hallucinations and ensures the enriched sentence is both semantically faithful and more interpretable. The method is evaluated on three benchmark datasets: Financial PhraseBank (FPB), FiQA, and SEntFiN, using Mistral 7B for generation and prediction, and DistilBERT for fine-tuning baselines.

Experimental results demonstrate that FLEX consistently improves FSA accuracy compared to baselines without enrichment. For decoder-only models like Mistral, FLEX boosts zero-shot accuracy from 75.7% to 83.6% and few-shot accuracy from 78.5% to 86.0%. For encoder-only models like DistilBERT, fine-tuning on FLEX-enriched data increases average accuracy from 83.4% to 91.0%. The ablation study confirms that both semantic similarity and perplexity checks are crucial for optimal performance. The approach is particularly effective for short, information-scarce texts like news headlines, making it a valuable tool for downstream financial applications where interpretability and accuracy are paramount.

## Hybrid LSTM and GRU for Cryptocurrency Price Forecasting Based on Social Network Sentiment Analysis Using FinBERT

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: forecasting, sentiment analysis, crypto, high-frequency trading, fine-tuning, time-series modeling, ohlc data, social media, accuracy, model, data leakage, ethereum, solana, finbert, lstm, gru, twitter
- Tag facets: {"asset_class": ["crypto"], "data_source": ["ohlc data", "social media"], "deliverable": ["model"], "evaluation": ["accuracy"], "market_context": ["high-frequency trading"], "method": ["fine-tuning", "time-series modeling"], "risk_issue": ["data leakage"], "task": ["forecasting", "sentiment analysis"]}
- One-line summary: The paper proposes a hybrid LSTM-GRU model integrated with FinBERT-derived social media sentiment to predict Ethereum and Solana prices, demonstrating superior accuracy over baseline models.

### Detailed Summary

This study addresses the challenge of predicting highly volatile cryptocurrency prices by integrating historical market data with social media sentiment. The authors argue that traditional models relying solely on price history miss critical information contained in public opinion, which significantly influences short-term price movements in the crypto market. The research focuses on Ethereum and Solana, targeting the need for more robust forecasting tools for traders and investors dealing with high-frequency, sentiment-driven assets.

The methodology combines daily OHLC (Open, High, Low, Close) price data from Binance with daily sentiment scores extracted from Twitter. Sentiment analysis is performed using FinBERT, a financial-domain pre-trained BERT model, which processes cleaned tweets to generate a daily average sentiment score. This sentiment feature is concatenated with the normalized market data and fed into a hybrid LSTM-GRU neural network. The hybrid architecture leverages LSTM's long-term memory and GRU's computational efficiency to mitigate vanishing gradient issues. The model is evaluated against standalone LSTM and GRU models, both with and without sentiment inputs, using MSE, RMSE, MAE, and MAPE metrics over a one-year period.

Results indicate that the hybrid LSTM-GRU model outperforms all benchmarks, achieving the lowest error rates. The inclusion of FinBERT-derived sentiment consistently improves prediction accuracy across all models, reducing MAPE by approximately 0.5% to 1%. For instance, the hybrid model with sentiment achieved a MAPE of 4.11% for Ethereum and 4.13% for Solana, compared to higher errors for models without sentiment. The study concludes that combining deep learning sequence models with financial NLP sentiment analysis provides a significant edge in cryptocurrency forecasting, though it notes limitations regarding data source diversity and computational cost.

## GPT-InvestAR: Enhancing Stock Investment Strategies through Annual Report Analysis with Large Language Models

- Year: 2023
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: stock prediction, equity research, equities, us equities, time-series modeling, 10-k filings, sec filings, backtest, portfolio returns, transaction costs, framework, open source, overfitting, annual rebalancing, non-negative regression, long-horizon prediction
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "sec filings"], "deliverable": ["framework", "open source"], "evaluation": ["backtest", "portfolio returns", "transaction costs"], "market_context": ["us equities"], "method": ["time-series modeling"], "risk_issue": ["overfitting"], "task": ["stock prediction", "equity research"]}
- One-line summary: GPT-InvestAR demonstrates that LLM-generated insights from 10-K filings, when used as features in a non-negative linear regression model, can outperform the S&P 500 in annual stock selection with minimal transaction costs.

### Detailed Summary

This paper addresses the challenge of efficiently extracting actionable investment signals from lengthy, unstructured annual reports (10-K filings). While financial experts spend years mastering this analysis, the process is cumbersome for large universes of firms. The research positions Large Language Models (LLMs) as a scalable alternative to manual expert analysis, aiming to simplify the assessment of corporate financial health and strategic positioning by converting qualitative textual data into quantitative features for investment strategies.

The methodology involves fetching 10-K filings for the top 1500 US companies by market cap from 2002 to 2023. The authors use the all-mpnet-base-v2 embedding model to chunk documents and retrieve relevant context for 27 curated questions posed to GPT-3.5-Turbo. The LLM outputs confidence scores (0-100) for each question, which serve as features. These are combined with historical price data to create target variables based on 12-month returns and maximum returns. A non-negative least squares linear regression model is trained on data from 2002-2017 and tested on 2018-2023, selecting the top k predicted stocks annually.

Results indicate that the LLM-enhanced model outperforms the S&P 500 benchmark, particularly when selecting a small number of top-ranked stocks (k=5). The strategy utilizing maximum return targets showed significant outperformance, quadrupling a $1 investment over five years compared to the S&P 500's doubling. The paper highlights that annual rebalancing minimizes transaction costs, making long-horizon LLM signals viable. Limitations include the high computational cost and time required for LLM inference, the reliance on a specific model version (GPT-3.5), and the potential for overfitting given the small sampled dataset used for training and testing.

## Enhancing Investment Analysis: Optimizing AI-Agent Collaboration in Financial Research

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: equity research, sentiment analysis, risk extraction, spreadsheet reasoning, equities, us equities, multi-agent systems, tool use, sec filings, news, social media, tables, accuracy, hit ratio, framework, open source, bias, ensemble architecture, agent collaboration, financial report analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "social media", "tables"], "deliverable": ["framework", "open source"], "evaluation": ["accuracy", "hit ratio"], "market_context": ["us equities"], "method": ["multi-agent systems", "tool use"], "risk_issue": ["bias"], "task": ["equity research", "sentiment analysis", "risk extraction", "spreadsheet reasoning"]}
- One-line summary: The paper proposes a multi-agent collaboration framework for financial investment research, demonstrating that an ensemble structure combining single agents for simple tasks and vertical multi-agents for complex risk analysis outperforms uniform architectures in accuracy and efficiency.

### Detailed Summary

This research addresses the limitation of single-agent systems in financial analysis by proposing a configurable multi-agent collaboration framework. The study investigates how varying agent group sizes (single, dual, triple) and collaboration structures (horizontal, vertical, hybrid) impact performance across three sub-tasks: fundamental analysis, market sentiment analysis, and risk analysis. The core problem is determining the optimal architectural configuration for AI agents to maximize the quality of investment research reports and decision-making accuracy when processing complex financial documents like SEC 10-K forms.

The methodology involves implementing these agent structures on the FinRobot platform using GPT-4-1106-vision-preview. Agents are equipped with Retrieval-Augmented Generation (RAG) and tool functions to access financial data, news, and social media. The experiments analyze the 2023 SEC 10-K forms of 30 Dow Jones Index companies. Evaluation metrics include sub-task quality scores (fundamentals, sentiment, risk) assessed by GPT-4, as well as AIGC quality metrics like readability and coherence. The final investment decision is evaluated by predicting one-week target stock prices and binary buy/not-buy recommendations, comparing the performance of different agent configurations against actual market outcomes.

Findings reveal that single agents outperform multi-agent groups in simpler tasks like fundamental and sentiment analysis, where excessive communication introduces noise. Conversely, triple-agent groups excel in complex risk analysis, with vertical structures (leader-subordinate) providing the best results by ensuring focused synthesis and reducing opinion convergence bias. The proposed ensemble structure, which selects the optimal agent configuration for each sub-task, achieves the highest performance with a 2.35% average difference in target price prediction and 66.7% accuracy in buy/not-buy decisions, surpassing all uniform multi-agent architectures. This highlights the importance of task-specific agent design in financial AI systems.

## Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? An Examination on Several Typical Tasks

- Year: 2023
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, stock prediction, equities, us equities, chain of thought, prompt engineering, sec filings, news, social media, accuracy, benchmark, hallucination, numerical reasoning, named entity recognition, relation extraction
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news", "social media"], "deliverable": ["benchmark"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["chain of thought", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "stock prediction"]}
- One-line summary: This study benchmarks ChatGPT and GPT-4 against domain-specific models and fine-tuned baselines across eight financial NLP datasets, revealing that generalist LLMs excel in sentiment analysis and numerical reasoning but lag in structured prediction tasks like named entity recognition and relation extraction.

### Detailed Summary

The paper addresses the critical question of whether general-purpose large language models like ChatGPT and GPT-4 can serve as effective solvers for financial text analytics without domain-specific fine-tuning. It positions these models against specialized alternatives such as BloombergGPT and task-specific fine-tuned architectures, aiming to delineate the boundaries of generalist capabilities in high-stakes financial applications. The research highlights the need to understand if the massive scale and reinforcement learning from human feedback (RLHF) of generalist models translate to superior performance in complex financial domains compared to smaller, domain-adapted models.

The experimental setup evaluates models on eight benchmark datasets spanning five task categories: sentiment analysis (Financial PhraseBank, FiQA, TweetFinSent), headline classification, named entity recognition (NER FIN3), relation extraction (REFinD), and numerical question answering (FinQA, ConvFinQA). The methodology employs zero-shot, few-shot, and Chain-of-Thought (CoT) prompting strategies to assess performance across varying levels of complexity and financial knowledge requirements. Results indicate that GPT-4 significantly outperforms ChatGPT and prior LLMs, often surpassing BloombergGPT in sentiment and QA tasks. However, fine-tuned models like FinBert and RoBERTa variants remain competitive or superior in simpler classification tasks, while structured prediction tasks like NER and relation extraction show poor performance for LLMs compared to CRF or fine-tuned baselines.

Key findings demonstrate that CoT prompting yields substantial accuracy gains, particularly for numerical reasoning in FinQA, where GPT-4 exceeds 78% accuracy, approaching but not matching human expert levels (~90%). Despite these advances, the study identifies significant limitations: LLMs struggle with coreference resolution in conversational QA and exhibit arithmetic errors in multi-step calculations, which poses risks for financial analysis. The paper concludes that while generalist LLMs are powerful tools for sentiment and reasoning tasks, they are not yet reliable for structured information extraction, suggesting a hybrid approach where fine-tuning remains necessary for specific, complex financial NLP applications.

## Integrating Large Language Models in Financial Investments and Market Analysis: A Survey

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: stock prediction, portfolio optimization, sentiment analysis, equities, us equities, chain of thought, fine-tuning, multi-agent systems, sec filings, news, sharpe ratio, portfolio returns, taxonomy, literature review, hallucination, benchmarking
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news"], "deliverable": ["taxonomy", "literature review"], "evaluation": ["sharpe ratio", "portfolio returns"], "market_context": ["us equities"], "method": ["chain of thought", "fine-tuning", "multi-agent systems"], "risk_issue": ["hallucination"], "task": ["stock prediction", "portfolio optimization", "sentiment analysis"]}
- One-line summary: This survey categorizes LLM integration in finance into four frameworks, highlighting that hybrid and agent-based methods significantly outperform baselines in stock prediction and portfolio optimization, though challenges in hallucination and real-time adaptability remain.

### Detailed Summary

This survey addresses the integration of Large Language Models into financial decision-making, categorizing existing research into four primary frameworks: LLM-based pipelines, hybrid integration methods, fine-tuning approaches, and agent-based architectures. It positions LLMs as tools that enhance traditional quantitative models by processing unstructured data like news and filings, thereby improving real-time analytical capabilities and interpretability in complex financial environments. The paper systematically reviews techniques such as Retrieval-Augmented Generation (RAG), Chain-of-Thought reasoning, and Parameter-Efficient Fine-Tuning (PEFT) to contextualize how these methods mitigate knowledge cutoffs and improve domain-specific reasoning.

The authors analyze numerous empirical studies, including MarketSenseAI, Ploutos, and LLMoE, which utilize datasets ranging from S&P 500 indices to proprietary financial news and SEC filings. Experimental designs often involve comparing LLM-generated signals against traditional baselines using metrics like cumulative returns, Sharpe ratios, and prediction accuracy. For instance, MarketSenseAI achieved up to 72% cumulative returns on S&P 100 stocks, while LLMoE demonstrated over 25% improvement in return metrics for Microsoft and Apple. The survey also examines fine-tuning efforts using LoRA on models like Llama-2 and GPT-3.5, and agent systems like FinCon that employ multi-agent collaboration for stock analysis and trading simulations.

Key findings indicate that hybrid models and multi-agent systems generally yield superior performance in stock selection, risk assessment, and portfolio optimization compared to single-model approaches. However, the survey highlights significant limitations, including the susceptibility of LLMs to hallucinations, the high computational cost of fine-tuning, and the lack of standardized benchmarks for financial LLMs. It concludes that future research must focus on adaptive fine-tuning, specialized financial architectures, and robust human-AI collaboration frameworks to ensure reliability and regulatory compliance in live trading environments.

## A Review of Large Language Models for Stock Price Forecasting from a Hedge-Fund Perspective

- Year: 2026
- Category: Surveys and Reviews
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: survey
- Summary coverage: full_extracted_text
- Tags: stock prediction, sentiment analysis, due diligence, earnings analysis, equities, portfolio management, market microstructure, prompt engineering, agentic workflow, time-series modeling, 10-k filings, earnings calls, news, social media, limit order book, sharpe ratio, drawdown, transaction costs, literature review, taxonomy
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "earnings calls", "news", "social media", "limit order book"], "deliverable": ["literature review", "taxonomy"], "evaluation": ["sharpe ratio", "drawdown", "transaction costs"], "market_context": ["portfolio management", "market microstructure"], "method": ["prompt engineering", "agentic workflow", "time-series modeling"], "risk_issue": ["data leakage", "overfitting", "model risk"], "task": ["stock prediction", "sentiment analysis", "due diligence", "earnings analysis"]}
- One-line summary: This review synthesizes LLM applications in stock forecasting from a hedge-fund perspective, critiquing academic practices for ignoring market frictions like data leakage, illiquidity, and regime shifts while proposing rigorous evaluation standards for production deployment.

### Detailed Summary

This paper addresses the gap between academic LLM research and practical hedge-fund deployment for stock price forecasting. It positions LLMs as versatile tools for sentiment extraction, financial report analysis, time-series tokenization, and multi-agent trading systems. Unlike prior surveys, it emphasizes the 'hedge-fund lens,' focusing on the robustness, frictions, and regulatory constraints that determine real-world viability rather than just algorithmic novelty. The authors argue that current literature often overstates LLM capabilities by ignoring market microstructure and evaluation biases.

The review categorizes LLM usage into five areas: sentiment analysis from news/social media, factual extraction from 10-K filings and earnings calls, relationship mapping via graph construction, tokenization of price series for next-token prediction, and multi-agent decision systems (e.g., FinArena, AlphaAgents). It details methods such as prompt engineering, RAG, and agentic frameworks like LangChain. Experiments cited include StockGPT’s 119% annual return and various sentiment-based baselines. The authors critically assess these results, noting that many studies use short horizons, inadequate baselines, and metrics like MSE that do not reflect trading profitability.

Key findings highlight significant pitfalls in current literature. Sentiment signals are fragile due to regime dependence and reflexivity. Dataset designs often suffer from data leakage (e.g., cross-day event drift) and short evaluation windows that miss full market cycles. The paper stresses that ignoring illiquidity premiums and transaction costs can turn profitable backtests into losing strategies, especially for small-cap stocks. It concludes with practical guidelines: use long-horizon datasets, align metrics with risk-adjusted returns (Sharpe, drawdown), control leakage rigorously, and benchmark against non-LLM technical analysis strategies to ensure genuine alpha generation.

## P1GPT: a multi-agent LLM workflow module for multi-modal financial information analysis

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: strategy generation, alpha mining, equities, us equities, multi-agent systems, agentic workflow, backtesting, news, social media, financial statements, backtest, sharpe ratio, drawdown, portfolio returns, framework, trading agent, look-ahead bias, hallucination, multi-modal analysis, structured reasoning
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media", "financial statements"], "deliverable": ["framework", "trading agent"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["us equities"], "method": ["multi-agent systems", "agentic workflow", "backtesting"], "risk_issue": ["look-ahead bias", "hallucination"], "task": ["strategy generation", "alpha mining"]}
- One-line summary: P1GPT introduces a layered multi-agent LLM workflow that fuses technical, fundamental, and news data through structured reasoning to generate interpretable trading signals, demonstrating superior risk-adjusted returns compared to baselines on major U.S. equities.

### Detailed Summary

P1GPT addresses the lack of coherent, multi-modal reasoning in financial LLMs by proposing a layered multi-agent architecture that replaces role-playing with a structured pipeline. The system comprises an Input Layer for data parsing, a Planning Layer for task decomposition, an Analysis Layer with domain-specific Intelligent Specialized Agents (ISAs) for fundamentals, technicals, news, and sectoral insights, and an Integration Layer that fuses these outputs via standardized reports and conflict resolution. This design aims to provide transparent, auditable decision-making suitable for regulated environments, contrasting with single-agent predictors or loosely connected ensembles that lack unified reasoning workflows.

The framework is evaluated through backtesting on three major U.S. equities—Apple, Google, and Tesla—spanning February to September 2025, a period marked by post-election uncertainty and tariff volatility. Data sources include real-time news, social media sentiment, technical indicators (MACD, RSI), and fundamental metrics from EDGAR and Yahoo Finance. The system is compared against Buy & Hold, MACD, KDJ+RSI, Zero-Mean Reversion, and SMA baselines. The experimental design ensures no lookahead bias, with agents accessing only information available prior to the decision timestamp, and outputs are generated as Buy/Sell/Hold signals accompanied by natural language rationales.

Results indicate that P1GPT achieves superior cumulative and risk-adjusted returns with lower maximum drawdowns than all baselines, demonstrating the efficacy of structured multi-modal fusion. The system exhibits stable behavioral patterns, such as disciplined exits during regime shifts and re-entry after drawdowns, driven by aligned multi-modal signals. However, the study abstracts away transaction costs, leverage, and portfolio interactions, limiting external validity. Future work must address realistic execution frictions, multi-asset allocation, and formal causal tracing to assess scalability and robustness in live trading environments.

## Comparative Investigation of GPT and FinBERT’s Sentiment Analysis Performance in News Across Different Sectors

- Year: 2025
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, prompt engineering, fine-tuning, news, accuracy, model
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["model"], "evaluation": ["accuracy"], "market_context": [], "method": ["prompt engineering", "fine-tuning"], "risk_issue": [], "task": ["sentiment analysis"]}
- One-line summary: This study demonstrates that GPT-4o, when optimized through systematic prompt engineering, outperforms the domain-specific FinBERT model in financial sentiment analysis across business, health, and technology sectors by up to 10%.

### Detailed Summary

The paper addresses the comparative efficacy of general-purpose large language models versus domain-specific models in financial sentiment analysis. While FinBERT has been the standard for financial text processing, the rapid advancement of GPT models raises questions about their utility in specialized domains. The authors position this research to evaluate whether a generalist model like GPT-4o can surpass a specialist like FinBERT when properly guided, thereby challenging the necessity of domain-specific fine-tuning for certain NLP tasks in finance. The study focuses on news-based sentiment classification, a critical input for market sentiment indicators and investment decision support systems.

The methodology involves a rigorous experimental design comparing GPT-4o and FinBERT on news data from The New York Times across three sectors: business, health, and technology. For GPT-4o, the authors employ a systematic prompt engineering process, testing eight initial prompts and refining them based on performance on a labeled Kaggle dataset. FinBERT is fine-tuned on a separate financial news dataset. Both models are evaluated using accuracy, precision, recall, and F1-score. The study generates time-series sentiment scores to visualize trends and compares the models' outputs to identify sector-specific performance variations and interpretability differences.

Results indicate that GPT-4o, with optimized prompts, achieves higher accuracy than FinBERT, with performance gains of up to 10% depending on the sector. The study highlights that prompt design is a critical factor in unlocking GPT-4o's potential, often outweighing the benefits of domain-specific pre-training. However, the authors note that performance varies by sector, suggesting that news content characteristics influence model behavior. The findings suggest that GPT-4o can serve as a robust alternative to FinBERT for sentiment analysis, offering actionable insights for predicting financial product outlooks, though the study is limited by its reliance on news headlines and descriptions rather than full articles or real-time market data integration.

## Sentiment trading with large language models

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, stock prediction, equities, us equities, fine-tuning, backtesting, news, sharpe ratio, portfolio returns, transaction costs, model, overfitting, long-short strategy, financial news, refinitiv, crsp
- Tag facets: {"asset_class": ["equities"], "data_source": ["news"], "deliverable": ["model"], "evaluation": ["sharpe ratio", "portfolio returns", "transaction costs"], "market_context": ["us equities"], "method": ["fine-tuning", "backtesting"], "risk_issue": ["overfitting"], "task": ["sentiment analysis", "stock prediction"]}
- One-line summary: The study demonstrates that the OPT large language model significantly outperforms BERT, FinBERT, and the Loughran-McDonald dictionary in analyzing U.S. financial news sentiment, achieving a Sharpe ratio of 3.05 for a long-short trading strategy based on its predictions.

### Detailed Summary

This paper addresses the limitation of traditional dictionary-based sentiment analysis in finance by evaluating the predictive power of large language models (LLMs) on stock returns. The authors position LLMs as superior tools for extracting nuanced sentiment from unstructured text, aiming to bridge the gap between advanced NLP capabilities and practical financial forecasting. They specifically investigate whether models like OPT, BERT, and FinBERT can generate more accurate sentiment signals than the established Loughran-McDonald dictionary, which has long dominated the literature despite its simplistic approach to text representation.

The methodology involves fine-tuning BERT and OPT on a dataset of 965,375 U.S. financial news articles from Refinitiv (2010-2023), using aggregated 3-day excess returns to label sentiment. The authors conduct regression analyses with firm and date fixed effects to test the correlation between model scores and next-day stock returns. They also construct daily-rebalanced, market-value-weighted long-short portfolios for each model, incorporating 10 basis points transaction costs and aligning trades with news release timings to simulate realistic trading conditions. This experimental design allows for a direct comparison of predictive accuracy and portfolio performance across different modeling approaches.

Results show OPT achieving 74.4% sentiment prediction accuracy, significantly higher than BERT (72.5%), FinBERT (72.2%), and the Loughran-McDonald dictionary (50.1%). Regression coefficients confirm OPT's strong positive impact on next-day returns, while the dictionary model shows no significant relationship. The OPT-based long-short strategy yields a Sharpe ratio of 3.05 and a 355% cumulative return from 2021-2023, vastly outperforming BERT, FinBERT, and the dictionary-based strategy. Limitations include the use of open-source OPT as a proxy for GPT-4, potential overfitting in specialized models like FinBERT, and the lack of data availability for replication, though the findings strongly support the integration of advanced LLMs in quantitative finance.

## MASS: Multi-Agent Simulation Scaling for Portfolio Construction

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Portfolio, ETF, and Asset Allocation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, strategy generation, equities, china market, a-share market, portfolio management, multi-agent systems, backtesting, reinforcement learning, financial statements, news, ohlc data, backtest, drawdown, portfolio returns, risk-adjusted returns, framework, dataset, open source, data leakage
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "news", "ohlc data"], "deliverable": ["framework", "dataset", "open source"], "evaluation": ["backtest", "drawdown", "portfolio returns", "risk-adjusted returns"], "market_context": ["china market", "a-share market", "portfolio management"], "method": ["multi-agent systems", "backtesting", "reinforcement learning"], "risk_issue": ["data leakage"], "task": ["portfolio optimization", "strategy generation"]}
- One-line summary: MASS introduces a multi-agent simulation framework with backward optimization for end-to-end portfolio construction, demonstrating a scaling effect where increasing agent count up to 512 improves excess returns on the Chinese A-share market.

### Detailed Summary

The paper addresses the limitations of existing LLM-based financial agents that rely on static workflows or intermediate stock prediction steps, which hinder adaptability in dynamic markets. It proposes Multi-Agent Scaling Simulation (MASS), a framework that shifts focus to direct, end-to-end portfolio construction by simulating a market of heterogeneous investor agents. The core innovation is a backward optimization process that dynamically learns the optimal distribution of agent types to maximize portfolio returns, allowing the system to adapt to evolving market regimes without predefined procedural constraints.

The method employs a daily cycle of forward propagation and backward optimization. In forward propagation, heterogeneous agents with distinct styles and partial market views generate investment signals based on macroeconomic data and stock features. These signals are aggregated using the market disagreement hypothesis, which rewards consensus and penalizes disagreement. Backward optimization uses simulated annealing to adjust the agent type distribution based on historical performance over a look-back window. Experiments were conducted on a self-collected dataset from the 2023 Chinese A-share market, covering SSE 50, CSI 300, and ChiNext 100 indices, using Qwen-2.5-72B-Instruct as the underlying LLM.

Results show MASS significantly outperforms seven state-of-the-art baselines across all metrics, including RIC and ICIR, with backtesting confirming higher cumulative returns and lower drawdowns. A key finding is the scaling effect: increasing the number of agents exponentially up to 512 yields progressively higher excess returns. The framework also demonstrates robustness to data leakage concerns when tested on 2025 data and adapts swiftly to market regime shifts. Limitations include the computational cost of API calls and the reliance on a specific market context, though the authors note potential for broader application.

## Learning to Generate Explainable Stock Predictions using Self-Reflective Large Language Models

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, portfolio optimization, equities, us equities, fine-tuning, reinforcement learning, agentic workflow, prompt engineering, social media, accuracy, sharpe ratio, portfolio returns, framework, dataset, model, hallucination, explainable ai, self-reflection, ppo, vicuna
- Tag facets: {"asset_class": ["equities"], "data_source": ["social media"], "deliverable": ["framework", "dataset", "model"], "evaluation": ["accuracy", "sharpe ratio", "portfolio returns"], "market_context": ["us equities"], "method": ["fine-tuning", "reinforcement learning", "agentic workflow", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["stock prediction", "portfolio optimization"]}
- One-line summary: The paper proposes the SEP framework, which uses a self-reflective agent and PPO to fine-tune LLMs for explainable stock prediction and portfolio construction without human annotations.

### Detailed Summary

The paper addresses the challenge of generating human-readable explanations for stock predictions, a task where traditional deep learning models are black boxes and pre-trained LLMs struggle to weigh chaotic social text impacts. The authors propose the Summarize-Explain-Predict (SEP) framework, which autonomously teaches an LLM to make explainable predictions. The method eliminates the need for expensive expert-annotated data by using a self-reflective agent that iteratively reasons through past mistakes to generate correct and incorrect response pairs. These pairs train a reward model, which then guides a PPO trainer to fine-tune a specialized LLM policy.

The experimental setup involves collecting tweet data for the top 5 stocks in 11 industries from 2020-2022, clustered using BERTopic. The SEP framework is evaluated on binary stock classification against deep learning baselines (VAE+Attention, GRU+Attention, Transformer) and LLM baselines (GPT-3.5, Vicuna, FinGPT). The model is fine-tuned using Vicuna-7b with LoRA. Additionally, the framework is tested on a portfolio construction task, generating explainable weights for multi-stock portfolios. Metrics include prediction accuracy, Matthews Correlation Coefficient (MCC), and portfolio profitability/Sharpe Ratio.

Results show the SEP model outperforms all baselines in accuracy and MCC, particularly when filtering for informative texts. The self-reflective process improves the quality of explanations, enabling decisive weighing of mixed sentiments. In portfolio construction, the model demonstrates generalization by generating weights that yield positive Sharpe ratios. Limitations include potential hallucinations in base models and the reliance on tweet data, which may not capture all market-moving information. The framework is most relevant for explainable AI in finance and agentic workflows.

## AI Agents in Finance and Fintech: A Scientific Review of Agent-Based Systems, Applications, and Future Horizons

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: fraud detection, credit scoring, investment advisory, regulatory reporting, options, derivatives, multi-agent systems, reinforcement learning, graph reasoning, financial statements, accuracy, taxonomy, literature review, hallucination, bias, model risk, systematic literature review, regtech, explainability, neuro-symbolic
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["financial statements"], "deliverable": ["taxonomy", "literature review"], "evaluation": ["accuracy"], "market_context": [], "method": ["multi-agent systems", "reinforcement learning", "graph reasoning"], "risk_issue": ["hallucination", "bias", "model risk"], "task": ["fraud detection", "credit scoring", "investment advisory", "regulatory reporting"]}
- One-line summary: This 2025 scientific review synthesizes the application of autonomous AI agents across finance, contrasting traditional rule-based and reinforcement learning systems with emerging LLM-driven architectures to evaluate their efficacy, ethical implications, and future research directions.

### Detailed Summary

The paper addresses the rapid integration of autonomous AI agents into financial systems, positioning them as a distinct paradigm beyond traditional statistical models. It aims to consolidate knowledge on agent-based methodologies, specifically focusing on reinforcement learning, multi-agent systems, and LLM-driven frameworks. The review highlights the shift towards agents capable of reasoning, learning, and autonomous action in high-stakes environments, while identifying critical gaps in standardized evaluation, scalability, and systemic risk management. It serves as a comprehensive survey for researchers and practitioners navigating the technical and ethical complexities of agentic finance.

The methodology involves a systematic literature review of peer-reviewed publications and industry reports, categorizing applications into algorithmic trading, credit risk, fraud detection, robo-advisory, and RegTech. The authors analyze architectural frameworks, contrasting rule-based, utility-based, and BDI agents with modern deep reinforcement learning and LLM-based systems. Key experiments and findings cited include the use of LLMs to simulate investor behavior (StockAgent), the superiority of multi-agent vertical structures for complex risk analysis, and the performance of CatBoost in credit scoring. The review also examines the use of Graph Neural Networks for fraud detection and the limitations of LLMs in high-frequency trading due to latency and reliability issues.

Findings indicate that while AI agents improve efficiency and accuracy in areas like fraud detection (40% false positive reduction) and credit risk, they introduce significant challenges. LLM-based agents face issues with hallucinations, bias, and prompt sensitivity, making them less suitable for deterministic, low-latency trading compared to specialized RL agents. Ethical and regulatory concerns, including algorithmic bias, lack of explainability, and potential for AI-driven collusion, are prominent. The paper concludes that responsible AI deployment requires human-in-the-loop oversight, robust stress testing, and the development of explainable, neuro-symbolic architectures to ensure trust and compliance in financial ecosystems.

## Can GPT models be Financial Analysts? An Evaluation of ChatGPT and GPT-4 on mock CFA Exams

- Year: 2023
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: equity research, benchmarking, equities, derivatives, institutional investing, chain of thought, prompt engineering, tables, accuracy, benchmark, dataset, hallucination, overfitting, cfa exam, numerical reasoning, professional certification
- Tag facets: {"asset_class": ["equities", "derivatives"], "data_source": ["tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["chain of thought", "prompt engineering"], "risk_issue": ["hallucination", "overfitting"], "task": ["equity research", "benchmarking"]}
- One-line summary: This study evaluates ChatGPT and GPT-4 on mock CFA Level I and II exams, finding that GPT-4 with few-shot prompting can likely pass Level I and potentially Level II, while revealing significant limitations in calculation and complex reasoning.

### Detailed Summary

The paper addresses the gap in rigorous evaluation of Large Language Models' financial reasoning capabilities by benchmarking ChatGPT and GPT-4 against mock Chartered Financial Analyst (CFA) Program exams. It positions LLMs as potential substitutes or assistants for professional financial analysis, testing their ability to handle domain-specific terminology, multi-step calculations, and table-based evidence found in real-world investment scenarios. The study aims to determine if current out-of-the-box models possess sufficient knowledge to pass professional certification exams, thereby assessing their readiness for advisory and analytical roles in finance.

The methodology involves evaluating models on five Level I and two Level II mock exams using Zero-Shot, Chain-of-Thought (CoT), and Few-Shot (FS) prompting strategies. The authors analyze performance across ten finance topics, categorizing errors into knowledge, reasoning, calculation, and inconsistency types. They also estimate the Minimum Passing Score (MPS) for CFA exams based on community data to determine pass/fail likelihoods. Experiments control for memorization and use temperature zero to ensure reproducibility, providing a comprehensive breakdown of where models succeed or fail in financial contexts.

Key findings indicate GPT-4 significantly outperforms ChatGPT, with FS prompting yielding the best results for both models. GPT-4 with FS can likely pass Level I and has a chance at Level II, whereas ChatGPT fails both. CoT prompting often hurts performance on Level I due to hallucinated calculations but helps on Level II by filtering relevant case details. Major limitations include poor numerical reasoning, susceptibility to knowledge gaps when forced to reason step-by-step, and struggles with long-context table interpretation. The paper suggests future improvements via retrieval-augmented generation and external calculation tools.

## Fine-Tuning Large Language Models for Stock Return Prediction Using Newsflow

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, portfolio optimization, equities, us equities, fine-tuning, backtesting, news, backtest, sharpe ratio, portfolio returns, model, alpha mining, long-short strategy, low-rank adaptation, return forecasting
- Tag facets: {"asset_class": ["equities"], "data_source": ["news"], "deliverable": ["model"], "evaluation": ["backtest", "sharpe ratio", "portfolio returns"], "market_context": ["us equities"], "method": ["fine-tuning", "backtesting"], "risk_issue": [], "task": ["stock prediction", "portfolio optimization"]}
- One-line summary: This paper demonstrates that fine-tuning encoder-only and decoder-only LLMs on financial news to directly predict stock returns yields superior portfolio performance compared to conventional sentiment-based methods, with decoder models like Mistral showing robustness across diverse investment universes.

### Detailed Summary

The paper addresses the challenge of extracting predictive signals from financial news for quantitative stock picking by proposing a direct news-to-return forecasting framework. Unlike traditional workflows that rely on intermediate feature extraction such as sentiment scoring, this approach fine-tunes Large Language Models (LLMs) to map text sequences directly to forward stock returns. The authors investigate the impact of model architecture by comparing encoder-only (DeBERTa) and decoder-only (Mistral, Llama3) LLMs, and evaluate two representation integration strategies: bottleneck representations using an end-of-sequence token and aggregated representations via token averaging. This design aims to determine which text encoding methods best capture semantic information relevant to future price movements.

Experiments were conducted on real-world financial news data from 2003 to 2019 across North American, European, and Emerging Market investment universes. The models were fine-tuned using Low-Rank Adaptation (LoRA) to minimize mean squared error between predicted and actual monthly forward returns. The evaluation included decile-wise metrics such as RMSE, precision, and return, alongside backtesting of long-only and long-short portfolios constructed from the top and bottom deciles of predictions. The study compared these LLM-based portfolios against benchmarks using FinBERT and FinVader sentiment scores, ensuring a rigorous assessment of predictive power and economic value in out-of-sample testing periods.

Results indicate that aggregated representations generally enhance portfolio performance, with decoder-based models like Mistral leading in larger universes. The LLM-derived return predictions significantly outperformed conventional sentiment-based portfolios in both annualized returns and Sharpe ratios, particularly in long-short strategies where the short side mitigated volatility. However, the study notes limitations, including inconsistent performance of encoder-only models in large universes and varying results for Llama across different markets. These findings suggest that while LLMs offer strong alpha signals, the choice of architecture and representation method must be tailored to the specific investment universe and strategy, highlighting the need for further exploration of model scaling and robustness.

## A Scoping Review of ChatGPT Research in Accounting and Finance

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, equity research, options, derivatives, prompt engineering, fine-tuning, sec filings, taxonomy, literature review, hallucination, privacy, scoping review, accounting, audit, financial reporting, labor market impact, technology adoption
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["sec filings"], "deliverable": ["taxonomy", "literature review"], "evaluation": [], "market_context": [], "method": ["prompt engineering", "fine-tuning"], "risk_issue": ["hallucination", "privacy"], "task": ["sentiment analysis", "equity research"]}
- One-line summary: This scoping review synthesizes 264 recent papers on ChatGPT and LLMs in accounting and finance, identifying three core themes: domain applications, LLMs as research tools, and professional implications, while providing a framework for future inquiry.

### Detailed Summary

This paper addresses the rapid proliferation of Large Language Model (LLM) research in accounting and finance by conducting a scoping review of 264 publications and working papers from January 2022 to March 2024. The authors aim to map the current state of the art, identify knowledge gaps, and provide technical guidance for researchers. Unlike systematic reviews that assess efficacy, this study focuses on the breadth of emerging literature to inform future research agendas, utilizing an input-process-output framework inspired by technology adoption theories. The review categorizes studies based on their motivation for adoption, the specific LLM capabilities leveraged, and the maturity of adoption implications, ranging from conceptual discussions to value realization.

The methodology involves a structured search across SSRN and published journals, filtering for relevance to accounting and finance. The authors organize the literature into three primary themes: applications of LLMs in specific fields (audit, reporting, asset pricing), the use of LLMs as research tools for classification and summarization, and the implications of LLM adoption for professionals and organizations. The analysis draws on the Gartner Hype Cycle to contextualize the adoption stage, noting a shift from early conceptual papers to potential applications. The review also includes a technical appendix detailing how to use LLM APIs, handle embeddings, and mitigate risks like hallucinations, offering practical guidance for empirical research design.

Key findings indicate that research is heavily concentrated in audit, financial reporting, asset pricing, and corporate finance. LLMs are primarily used for text generation, sentiment analysis, and classification, often outperforming traditional methods in efficiency. The paper highlights that ChatGPT-4 can pass professional exams like the CPA, suggesting significant shifts in labor markets and education. However, the review notes limitations in current studies, including a lack of large-scale empirical evidence on financial payoffs and concerns about data privacy and hallucination. The authors propose future research avenues, such as investigating the long-term impact on labor productivity and developing domain-specific fine-tuning strategies, emphasizing the need for rigorous evaluation of LLM outputs in high-stakes financial contexts.

## Bloated Disclosures: Can ChatGPT Help Investors Process Information?

- Year: 2023
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, earnings analysis, equities, us equities, prompt engineering, sec filings, earnings calls, market impact, dataset, bias, information asymmetry, price efficiency, disclosure quality, obfuscation
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "earnings calls"], "deliverable": ["dataset"], "evaluation": ["market impact"], "market_context": ["us equities"], "method": ["prompt engineering"], "risk_issue": ["bias"], "task": ["sentiment analysis", "earnings analysis"]}
- One-line summary: This paper demonstrates that GPT-3.5 summaries of corporate disclosures amplify sentiment and better explain stock market reactions than original texts, enabling a novel 'bloat' metric that predicts lower price efficiency and higher information asymmetry.

### Detailed Summary

The paper addresses the challenge of information overload in complex corporate disclosures, such as Management Discussion and Analysis (MD&A) sections and earnings conference call transcripts. It investigates whether generative AI tools, specifically GPT-3.5 Turbo, can effectively distill relevant information for investors with limited attention. The authors position this within the context of disclosure quality, obfuscation, and the economic value of AI in financial analysis, aiming to determine if AI summaries retain or enhance the informational content of the original documents compared to human processing constraints.

The methodology involves generating unconstrained and targeted (financial or ESG) summaries for a large sample of MD&As and conference calls from 2009 to 2020. The authors compare the sentiment and informativeness of these summaries against the original texts by regressing short-window abnormal stock returns on sentiment scores derived from both. They also introduce a 'Bloat' measure, defined as the relative reduction in document length after summarization, and analyze its determinants and capital market consequences using proxies for price efficiency and information asymmetry. The study includes robustness checks with out-of-sample data and variance decompositions to isolate firm-specific effects.

Key findings indicate that GPT-3.5 summaries are significantly shorter (25-30% of original length) yet exhibit amplified sentiment and superior explanatory power for stock market reactions. The 'Bloat' metric reveals that firms with higher bloat experience adverse market outcomes, including lower price efficiency and higher information asymmetry. Targeted summaries for ESG topics show increasing market relevance over time. Limitations include the use of GPT-3.5, which may differ from newer models, and the reliance on sentiment-based metrics which might not capture all nuances of complex financial data. The study suggests AI can mitigate information processing costs but highlights risks associated with opaque or bloated disclosures.

## CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, strategy generation, crypto, portfolio management, agentic workflow, multi-agent systems, prompt engineering, news, ohlc data, portfolio returns, sharpe ratio, benchmark, dataset, framework, open source, trading agent, overfitting, zero-shot, on-chain data, reflection mechanism
- Tag facets: {"asset_class": ["crypto"], "data_source": ["news", "ohlc data"], "deliverable": ["benchmark", "dataset", "framework", "open source", "trading agent"], "evaluation": ["portfolio returns", "sharpe ratio"], "market_context": ["portfolio management"], "method": ["agentic workflow", "multi-agent systems", "prompt engineering"], "risk_issue": ["overfitting"], "task": ["alpha mining", "strategy generation"]}
- One-line summary: CryptoTrade is a zero-shot LLM-based multi-agent system that integrates on-chain transaction statistics and off-chain news to guide daily cryptocurrency trading, outperforming time-series baselines but matching traditional technical indicators.

### Detailed Summary

The paper addresses the underutilization of Large Language Models in cryptocurrency trading by introducing CryptoTrade, a framework that synthesizes transparent on-chain data with timely off-chain news. Unlike stock-focused LLM agents, this system leverages the unique transparency of blockchain transactions and the sentiment influence of financial news to navigate the high-volatility crypto market. The core innovation lies in a multi-agent architecture featuring specialized market and news analysts, a trading agent for decision-making, and a reflection agent that refines strategies based on past performance, enabling zero-shot daily trading without fine-tuning.

The methodology employs GPT-3.5-turbo, GPT-4, and GPT-4o to process daily data from CoinMarketCap and Dune Analytics, including metrics like transaction counts, active wallets, and gas prices, alongside news summaries from sources like Bloomberg. The system is evaluated on Bitcoin, Ethereum, and Solana across bull, sideways, and bear markets from 2023, using a $1 million initial portfolio. Experiments compare CryptoTrade against traditional technical indicators (SMA, MACD, Buy and Hold) and deep learning time-series baselines (LSTM, Informer, PatchTST), measuring total return and Sharpe ratio to assess risk-adjusted performance.

Results show CryptoTrade significantly outperforms time-series baselines in most metrics, demonstrating the efficacy of LLMs in capturing complex market dynamics. However, it does not surpass traditional signals like Buy and Hold or SLMA, particularly in strong bull markets. Ablation studies confirm that on-chain transaction statistics and the reflection mechanism are critical for performance. The paper highlights a case study where the agent successfully executed a "buy the rumor, sell the news" strategy around the Bitcoin ETF approval. Limitations include reliance on daily frequency, lack of fine-tuning, and a limited dataset scope, suggesting future work on higher-frequency trading and model adaptation.

## Advancing innovation in financial stability: A comprehensive review of ai agent frameworks, challenges and applications

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: full_extracted_text
- Tags: fraud detection, risk extraction, alpha mining, factor modeling, spreadsheet reasoning, agentic workflow, multi-agent systems, tables, literature review, regulatory compliance, ai agent frameworks, explainability, risk alignment, operational efficiency
- Tag facets: {"asset_class": [], "data_source": ["tables"], "deliverable": ["literature review"], "evaluation": [], "market_context": [], "method": ["agentic workflow", "multi-agent systems"], "risk_issue": ["regulatory compliance"], "task": ["fraud detection", "risk extraction", "alpha mining", "factor modeling", "spreadsheet reasoning"]}
- One-line summary: This 2025 review synthesizes the landscape of AI agent frameworks like LangGraph, CrewAI, and AutoGen, evaluating their architectures, financial applications in risk and trading, and critical challenges regarding regulatory compliance, explainability, and risk alignment.

### Detailed Summary

This paper addresses the growing integration of autonomous AI agents into financial services, positioning agentic systems as transformative tools for automating complex workflows, enhancing decision-making, and improving operational efficiency. It identifies a gap in comprehensive comparative analyses of agent frameworks specifically tailored to the unique constraints of the financial sector, such as strict regulatory compliance, the need for high interpretability, and the critical importance of risk alignment. The review aims to provide a structured overview of how multi-agent collaboration and LLM-based reasoning can be leveraged for tasks ranging from investment analysis to fraud detection, while highlighting the technical and ethical hurdles that currently limit widespread deployment.

The methodology involves a systematic literature review and comparative analysis of leading AI agent frameworks, including LangGraph, CrewAI, AutoGen, FinRobot, and FinCon. The authors evaluate these frameworks based on their architectural features, scalability, multi-agent collaboration capabilities, and suitability for financial use cases. The paper synthesizes insights from academic research, industry reports from McKinsey and Moody’s, and technical documentation from providers like IBM and AWS. It examines specific applications such as algorithmic trading, risk assessment, and customer service, drawing on quantitative findings from cited studies that report performance improvements, such as a 30% increase in decision-making accuracy for FinRobot and a 25% reduction in operational costs for enterprise platforms like IBM Watsonx.ai.

Key findings indicate that while AI agents offer significant potential for alpha mining, risk management, and automation, their deployment is hindered by challenges in data quality, explainability, and regulatory adherence. The paper highlights that frameworks like AutoGen and CrewAI excel in multi-agent orchestration but face scalability and real-time processing limitations. It emphasizes the need for enhanced transparency and security in agentic systems to mitigate risks associated with autonomous decision-making. The review concludes by outlining future directions, including the development of standardized enterprise integration protocols, robust synthetic data validation methods, and hybrid models that combine rule-based systems with learning-based approaches to ensure reliability and compliance in high-stakes financial environments.

## Integrating Stock Features and Global Information via Large Language Models for Enhanced Stock Return Prediction

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: stock prediction, portfolio optimization, equities, a-share market, china market, reinforcement learning, fine-tuning, retrieval, news, ohlc data, backtest, sharpe ratio, drawdown, transaction costs, framework, model, overfitting, alpha mining, feature alignment, llm embeddings
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "ohlc data"], "deliverable": ["framework", "model"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "transaction costs"], "market_context": ["a-share market", "china market"], "method": ["reinforcement learning", "fine-tuning", "retrieval"], "risk_issue": ["overfitting"], "task": ["stock prediction", "portfolio optimization"]}
- One-line summary: The paper proposes SCRL-LG, a framework using Self-Correlated Reinforcement Learning to align LLM-generated news embeddings with quantitative stock features, significantly improving stock return prediction accuracy and portfolio performance in the China A-share market.

### Detailed Summary

The paper addresses the challenge of integrating unstructured financial news with structured quantitative features for stock return prediction. It identifies two main issues: insufficient utilization of LLM semantic information and the misalignment between LLM embeddings and pre-existing stock features. The authors propose a novel framework called Self-Correlated Reinforcement Learning with Local-Global model (SCRL-LG). The Local-Global (LG) model decomposes returns into idiosyncratic alpha (local stock features) and beta (global market/news information). To bridge the semantic gap, the SCRL component uses Proximal Policy Optimization (PPO) to align LLM-generated news embeddings with stock feature spaces, treating the LLM as a feature selector and the quantitative model as a critic to ensure stable policy updates.

Experiments are conducted on the China A-share market using 3,506 stocks and 342 daily price-volume features from 2019 to 2022. The LLM used is Llama 7B, fine-tuned on Chinese news corpora. The study compares SCRL-LG against baselines including a local-only model, a global model using only stock features, and a global model using only LLM embeddings. Evaluation metrics include Rank Information Coefficient (Rank IC), annual returns, Sharpe ratio, and maximum drawdown. The backtesting strategy involves daily sorting into deciles, trading the top 10% with a 0.3% transaction cost.

Results show that SCRL-LG outperforms all baselines, achieving a Rank IC of 0.152 and a Sharpe ratio of 1.24, compared to 0.132 and 0.56 for the local-only model. The integration of global information significantly enhances predictive accuracy, particularly for longer-term horizons (10-20 days), where noise is averaged out. The method demonstrates robustness and improved risk-adjusted returns. However, limitations include the potential for overfitting due to high-dimensional alignment and the reliance on specific Chinese market data, which may limit generalizability to other markets or asset classes without further adaptation.

## Harnessing Earnings Reports for Stock Predictions: A QLoRA-Enhanced LLM Approach

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, earnings analysis, equities, options, derivatives, us equities, earnings season, fine-tuning, instruction tuning, time-series modeling, earnings calls, financial statements, market prices, accuracy, backtest, dataset, model, overfitting, post-earnings drift, parameter-efficient fine-tuning
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["earnings calls", "financial statements", "market prices"], "deliverable": ["dataset", "model"], "evaluation": ["accuracy", "backtest"], "market_context": ["us equities", "earnings season"], "method": ["fine-tuning", "instruction tuning", "time-series modeling"], "risk_issue": ["overfitting"], "task": ["stock prediction", "earnings analysis"]}
- One-line summary: The paper demonstrates that instruction-fine-tuning Llama-3-8B with 4-bit QLoRA on a dataset combining earnings transcripts, financial metrics, and external market factors significantly outperforms GPT-4 in predicting next-day stock direction following earnings announcements.

### Detailed Summary

This paper addresses the challenge of accurately predicting stock market movements following earnings announcements, a task where traditional machine learning models often fail to process extensive unstructured textual data and nuanced financial narratives. The authors argue that while historical price data is insufficient, the integration of qualitative insights from earnings reports with quantitative metrics offers a superior predictive signal. The study positions Large Language Models (LLMs) as a solution to interpret complex financial disclosures and external market conditions, aiming to provide investors with reliable, real-time forecasting tools that adapt to new information during volatile earnings seasons.

The methodology involves constructing a supervised dataset of 8,556 instances from 501 S&P 500 companies, integrating 'base factors' (financial metric growth, earnings transcripts) and 'external factors' (market index performance, analyst grades, earnings surprises). Numerical and categorical data were textualized into natural language prompts. The team fine-tuned several open-source LLMs, including Llama-3-8B, Mistral-7B, and Gemma-7B, using instruction tuning and 4-bit Quantized Low-Rank Adaptation (QLoRA) for efficiency. Models were evaluated on accuracy, weighted F1, and Matthews Correlation Coefficient (MCC) against a GPT-4 baseline, using both a 'Base' dataset (internal factors only) and a 'Full' dataset (internal plus external factors).

Results indicate that the fine-tuned Llama-3-8B-Instruct-4bit model achieved superior performance on the 'Full' dataset, with 16% higher accuracy and 10% better weighted F1 score compared to GPT-4. The inclusion of external factors significantly enhanced predictive power over internal factors alone. The study highlights the efficacy of QLoRA in maintaining high accuracy while reducing computational costs, making it suitable for resource-constrained deployment. Limitations include the binary 'Long/Short' output format, which ignores 'Hold' positions, and the short-term prediction horizon of only the next day, suggesting future work should expand output options and timeframes to better align with diverse investment strategies.

## Ploutos: Towards interpretable stock movement prediction with financial large language model

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, sentiment analysis, alpha mining, factor modeling, equities, us equities, fine-tuning, multimodal modeling, instruction tuning, chain of thought, news, social media, ohlc data, accuracy, ablation study, model, framework, bias, overfitting, interpretable ai
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "social media", "ohlc data"], "deliverable": ["model", "framework"], "evaluation": ["accuracy", "ablation study"], "market_context": ["us equities"], "method": ["fine-tuning", "multimodal modeling", "instruction tuning", "chain of thought"], "risk_issue": ["bias", "overfitting"], "task": ["stock prediction", "sentiment analysis", "alpha mining", "factor modeling"]}
- One-line summary: Ploutos is a financial LLM framework that combines multimodal expert analysis with a novel training strategy to achieve state-of-the-art stock movement prediction accuracy and high-quality interpretable rationales.

### Detailed Summary

The paper addresses the challenge of fusing textual and numerical data for stock movement prediction while maintaining interpretability, a gap in traditional deep learning and existing LLM methods. The authors propose Ploutos, a framework comprising PloutosGen and PloutosGPT. PloutosGen utilizes a pool of specialized experts—Sentiment, Technical, and Human—to analyze diverse data modalities. The Sentiment Expert aggregates news and tweets using supervised and unsupervised fine-tuning on LLaMA-2. The Technical Expert employs a Number-to-Text Alignment (N2I-Align) technique to convert alpha formulas and time-series data into text for next-token prediction. PloutosGPT integrates these insights to generate final predictions and natural language rationales.

The training of PloutosGPT introduces two key mechanisms: rearview-mirror prompting and dynamic token weighting. Rearview-mirror prompting leverages GPT-4 to generate faithful bullish and bearish rationales based on historical data and expert inputs, creating high-quality instruction data for supervised fine-tuning. Dynamic token weighting adjusts the loss function during training by emphasizing key tokens in the rationale generation process, calculated via cosine similarity between token hidden states and verbalizer type embeddings. Experiments are conducted on the ACL18 and CIKM18 datasets, which contain S&P 500 stocks with historical prices and social media text. The model is evaluated against traditional deep learning baselines (ARIMA, Adv-LSTM, StockNet) and LLM baselines (GPT-4, LLaMA-2, FinMA) using accuracy, F1, and Matthews Correlation Coefficient (MCC).

Results show Ploutos-7B outperforms all baselines, achieving 61.21% accuracy and 0.205 MCC on ACL18, significantly higher than FinMA-7B (56.28% Acc) and GPT-4 (53.08% Acc). The framework also demonstrates superior interpretability, scoring 81.24% in faithfulness and 96.52% in informativeness on rationale quality, surpassing FinGPT and GPT-3. Ablation studies confirm the necessity of each expert and training component. Limitations include high computational costs, potential biases in expert selection, and the current exclusion of visual data modalities. The paper highlights the synergy between predictive accuracy and interpretability, suggesting that LLMs can serve as effective decision-support tools in quantitative finance when properly trained with multimodal and explainable constraints.

## Transforming Sentiment Analysis in the Financial Domain with ChatGPT

- Year: 2023
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, forex, prompt engineering, news, accuracy, hit ratio, dataset, benchmark, zero-shot prompting, finbert, market return correlation
- Tag facets: {"asset_class": ["forex"], "data_source": ["news"], "deliverable": ["dataset", "benchmark"], "evaluation": ["accuracy", "hit ratio"], "market_context": [], "method": ["prompt engineering"], "risk_issue": [], "task": ["sentiment analysis"]}
- One-line summary: This study demonstrates that zero-shot prompting of ChatGPT 3.5 significantly outperforms FinBERT in classifying sentiment from forex news headlines and correlates more strongly with market returns, highlighting the value of prompt engineering in financial NLP.

### Detailed Summary

The paper addresses the challenge of financial sentiment analysis, specifically the difficulty of capturing nuanced, context-dependent sentiments in forex news where standard models often fail to distinguish between positive signals for one currency and negative signals for its pair. It positions ChatGPT 3.5 as a superior alternative to domain-specific models like FinBERT by leveraging its broad pre-training and zero-shot capabilities, thereby eliminating the need for costly fine-tuning on limited financial datasets. The research aims to validate whether large language models can effectively interpret complex financial narratives and align with market dynamics through strategic prompt design.

The methodology involves a curated dataset of 2,291 manually annotated forex news headlines covering five major currency pairs, collected from Forex Live and FXstreet. The authors employ a zero-shot prompting approach, testing six distinct prompt templates that frame the task from various perspectives, such as a financial analyst or a sentiment analysis model. They evaluate performance using precision, recall, F1-score, and Sentiment Mean Absolute Error (S-MAE), while also measuring the correlation between predicted sentiment scores and actual market returns. The baseline comparison is established using FinBERT, implemented via the Hugging Face Transformers library, to ensure a rigorous benchmark against the current state-of-the-art in financial NLP.

Results indicate that ChatGPT 3.5 achieves approximately 35% higher performance in sentiment classification and a 36% stronger correlation with market returns compared to FinBERT. The study finds that prompt engineering is critical, with prompts framing the model as a forex trader or analyst yielding the best results. However, the authors note limitations, including that sentiment alone does not fully predict price movements due to other market factors, and that API latency and costs vary with load. The paper concludes that while LLMs offer substantial improvements in accuracy and contextual understanding, they should be integrated into holistic trading systems rather than used as standalone predictive tools, and it releases the dataset to facilitate further research.

## ChatGPT Informed Graph Neural Network for Stock Movement Prediction

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: stock prediction, equities, us equities, graph reasoning, prompt engineering, time-series modeling, news, ohlc data, backtest, portfolio returns, sharpe ratio, drawdown, framework, open source, data leakage, graph neural network, lstm, dow 30, sentiment analysis, zero-shot learning
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "ohlc data"], "deliverable": ["framework", "open source"], "evaluation": ["backtest", "portfolio returns", "sharpe ratio", "drawdown"], "market_context": ["us equities"], "method": ["graph reasoning", "prompt engineering", "time-series modeling"], "risk_issue": ["data leakage"], "task": ["stock prediction"]}
- One-line summary: The paper proposes a framework using ChatGPT to infer dynamic stock networks from financial news, which are then processed by a Graph Neural Network and LSTM to predict stock movements, outperforming baselines in both classification accuracy and portfolio performance.

### Detailed Summary

The paper addresses the challenge of capturing latent inter-dependencies among equities for stock movement prediction, arguing that existing methods often fail to model dynamic relationships and the lead-lag effects caused by news propagation. It positions Large Language Models (LLMs) as superior tools for extracting these relationships from unstructured text compared to static knowledge graphs or handcrafted features. The research aims to leverage ChatGPT's zero-shot inference capabilities to build evolving network structures from daily financial news, thereby enhancing the predictive power of downstream deep learning models.

The proposed method integrates three components: network structure inference, graph embedding, and sequential prediction. First, ChatGPT is prompted to identify target companies affected by daily news headlines and their sentiment, constructing a dynamic graph where edges connect companies mentioned together. Second, a Graph Neural Network (GNN) generates node embeddings by aggregating information from these inferred neighbors. Third, these embeddings are concatenated with historical stock market data and processed by Long Short-Term Memory (LSTM) networks to classify next-day stock movements as up, down, or neutral. The model is evaluated on the DOW 30 companies using data from September 2020 to December 2022, with a test period starting October 2021 to avoid data leakage from ChatGPT's training cutoff.

Experimental results show the model consistently outperforms baselines (LSTM, News-Embed, ChatGPT sentiment-only) in weighted, Micro, and Macro F1 scores, with a minimum improvement of 1.8%. Portfolio backtesting reveals that strategies based on the model's predictions yield higher annualized cumulative returns, lower volatility, and reduced maximum drawdown compared to benchmarks. The study highlights that while ChatGPT sentiment alone struggles with downtrend prediction, the graph-informed approach improves detection of both upward and downward movements. Limitations include the small sample size (DOW 30), potential oversmoothing in GNNs, and reliance on basic network structures without sentiment edge attributes.

## Designing Heterogeneous LLM Agents for Financial Sentiment Analysis

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, spreadsheet reasoning, equities, crypto, retail investing, multi-agent systems, prompt engineering, news, social media, tables, accuracy, framework, data leakage, zero-shot, financial phrasebank, fiqa, sentiment classification
- Tag facets: {"asset_class": ["equities", "crypto"], "data_source": ["news", "social media", "tables"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": ["retail investing"], "method": ["multi-agent systems", "prompt engineering"], "risk_issue": ["data leakage"], "task": ["sentiment analysis", "spreadsheet reasoning"]}
- One-line summary: The paper proposes Heterogeneous Agent Discussion (HAD), a zero-shot framework using five specialized LLM agents guided by financial sentiment error types, which improves classification accuracy by 25-35% of the fine-tuning gap compared to naive prompting.

### Detailed Summary

This study addresses the challenge of applying generative Large Language Models (LLMs) to Financial Sentiment Analysis (FSA) without fine-tuning. While LLMs excel at generative tasks, FSA is discriminative and requires handling domain-specific linguistic nuances like sarcasm, irrealis mood, and external references. The paper positions its contribution within design science, leveraging Minsky’s theory of mind to create a framework where LLMs act as specialized 'resources' or agents, rather than relying on homogeneous multi-agent debates or simple chain-of-thought prompting. The goal is to elicit the full potential of pre-trained models through strategic elicitation and structured collaboration.

The proposed method, Heterogeneous Agent Discussion (HAD), instantiates five specialized LLM agents, each prompted to focus on a specific type of common FSA error: irrealis mood, rhetoric (sarcasm), dependent opinion, aspect mismatch, and external references. These agents process the input text independently, and their outputs are aggregated by a summative agent to determine the final sentiment polarity. The framework is evaluated on five FSA datasets (Financial PhraseBank, StockSen, CMC, FiQA, SEntFiN) using GPT-3.5 and BLOOMZ models. Experiments compare HAD against naive prompting and fine-tuned baselines like FinBERT, utilizing accuracy and macro F-1 scores as metrics. Ablation studies are conducted to assess the individual contribution of each agent type.

Results indicate that HAD consistently improves performance over naive prompting, particularly with GPT-3.5, fixing approximately 25-35% of the performance gap between zero-shot prompting and fine-tuning. The mood, rhetoric, and aspect agents were found to be the most critical contributors, while the dependency agent showed negligible or negative impact when removed. The framework is most effective when agents generate substantial discussion content. Limitations include higher computational costs and latency compared to single-model approaches, potential data leakage in older benchmarks, and the non-linear, complex interactions between agents that require careful prompt engineering. The study provides a theoretical foundation for designing heterogeneous LLM agents in finance.

## DianJin-R1: Evaluating and Enhancing Financial Reasoning in Large Language Models

- Year: 2025
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, regulatory reporting, reinforcement learning, fine-tuning, multi-agent systems, chain of thought, sec filings, accuracy, model, dataset, regulatory compliance, chinese financial benchmarks, grpo, sft, inference cost reduction
- Tag facets: {"asset_class": [], "data_source": ["sec filings"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["reinforcement learning", "fine-tuning", "multi-agent systems", "chain of thought"], "risk_issue": ["regulatory compliance"], "task": ["financial question answering", "regulatory reporting"]}
- One-line summary: DianJin-R1 enhances financial reasoning in LLMs through a structured SFT and GRPO reinforcement learning pipeline on a curated dataset, achieving state-of-the-art accuracy on Chinese financial benchmarks while significantly reducing inference costs compared to multi-agent systems.

### Detailed Summary

The paper addresses the challenge of effective reasoning in large language models for the financial domain, where tasks require domain-specific knowledge, precise numerical calculations, and strict adherence to compliance rules. The authors propose DianJin-R1, a framework that combines reasoning-augmented supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO) reinforcement learning. The core contribution is the construction of DianJin-R1-Data, a high-quality dataset synthesized from CFLUE, FinQA, and a proprietary Chinese Compliance Check (CCC) corpus. The data construction process involves filtering for difficulty and ambiguity, converting multiple-choice questions to open-ended formats, and using multi-agent systems to generate complex reasoning paths for compliance scenarios, verified by GPT-4o. This ensures the training data contains verified, structured reasoning steps alongside final answers.

The training methodology consists of two stages. First, models (DianJin-R1-7B and 32B, based on Qwen2.5) undergo SFT to learn generating structured outputs with <think> and <answer> tags. Second, GRPO is applied using hard cases from the dataset, employing dual reward signals: a format reward for strict structural adherence and an accuracy reward for correct final answers. The models are evaluated on five benchmarks: three financial (CFLUE, FinQA, CCC) and two general reasoning (MATH-500, GPQA-Diamond). The experimental design compares DianJin-R1 against non-reasoning baselines (e.g., Qwen2.5, GPT-4o) and other reasoning models (e.g., DeepSeek-R1, QwQ-32B), measuring accuracy and computational efficiency.

Results show that DianJin-R1 models consistently outperform their non-reasoning counterparts, particularly on complex financial tasks. DianJin-R1-32B achieved 86.74% on CFLUE, 80.82% on FinQA, and 96.00% on CCC, surpassing even larger general reasoning models like DeepSeek-R1 on financial benchmarks. Notably, on the CCC compliance task, the single-call DianJin-R1 models matched or exceeded the performance of multi-agent systems that required an average of 8.15 API calls per instance, demonstrating superior cost-efficiency. The paper highlights that while financial reasoning training improves general reasoning, it does not fully close the gap with models trained on general reasoning data. Limitations include the exclusion of the proprietary CCC data from public release and the observation that RL improvements were less pronounced on English datasets (FinQA) due to the Chinese-centric RL training data.


## Forecasting the S&P 500 Index Using Mathematical-Based Sentiment Analysis and Deep Learning Models: A FinBERT Transformer Model and LSTM

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: forecasting, sentiment analysis, equities, us equities, fine-tuning, time-series modeling, news, ohlc data, accuracy, dataset, model, bias, finbert, lstm, s p 500, new york times
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "ohlc data"], "deliverable": ["dataset", "model"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["fine-tuning", "time-series modeling"], "risk_issue": ["bias"], "task": ["forecasting", "sentiment analysis"]}
- One-line summary: This study demonstrates that incorporating FinBERT-derived sentiment scores from New York Times news summaries significantly improves the accuracy of LSTM-based S&P 500 index forecasts compared to models using only historical price data.

### Detailed Summary

The research addresses the challenge of enhancing stock market forecasting by integrating unstructured textual data with quantitative time-series models. Specifically, it investigates whether the sentiment expressed in financial news provides predictive signal for broad market indices, positioning the work within the intersection of natural language processing and financial mathematics. The authors aim to validate the efficacy of domain-specific transformer models in extracting actionable sentiment metrics that can be mathematically mapped to market movements, thereby bridging the gap between qualitative news analysis and quantitative prediction frameworks.

The methodology employs a two-stage pipeline using data from January 2018 to December 2022. First, the FinBERT transformer model is applied to daily news summaries extracted from The New York Times to classify sentiment as positive, neutral, or negative, generating a daily aggregate sentiment score. Second, a Long Short-Term Memory (LSTM) neural network is trained to predict the S&P 500 index closing price. The experimental design compares two LSTM configurations: a baseline model using only historical market variables (Open, High, Low, Close, Adj Close, Volume) and an enhanced model that includes the FinBERT sentiment score as an additional feature. Model hyperparameters are optimized via random search, and performance is evaluated using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE).

Empirical results indicate that the inclusion of FinBERT sentiment scores consistently reduces prediction errors across all three metrics, confirming that news sentiment adds significant value to S&P 500 forecasting. The study highlights that using concise news summaries rather than full articles is a computationally efficient strategy that yields comparable predictive power. However, limitations include the reliance on a single news source (NYT), which may introduce source-specific bias, and the lack of backtesting for actual trading profitability. The findings suggest that while sentiment enhances accuracy, the model's generalizability to other markets or asset classes remains unverified, and the static nature of the pre-trained FinBERT model may not capture real-time shifts in financial language usage.

## Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations

- Year: 2023
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: conceptual
- Summary coverage: first_50k_chars
- Tags: investment advisory, prompt engineering, financial statements, framework, model, hallucination, budgeting, household finance, personal finance, optimization, coevolutionary theory
- Tag facets: {"asset_class": [], "data_source": ["financial statements"], "deliverable": ["framework", "model"], "evaluation": [], "market_context": [], "method": ["prompt engineering"], "risk_issue": ["hallucination"], "task": ["investment advisory"]}
- One-line summary: This paper proposes an optimization framework for individual and household budgeting that integrates LLM-generated recommendations as initial feasible solutions, validated through a prospective verification mechanism and extended coevolutionary theory to enhance personalization and financial resilience.

### Detailed Summary

The paper addresses the challenge of democratizing financial planning by bridging traditional econometric optimization with AI-driven personalization. It introduces two mathematical models: an individual budgeting framework maximizing savings subject to income and expense constraints, and a cooperative household model that incorporates member-specific preference weights and shared expense constraints. The core innovation lies in using Large Language Models (LLMs) to provide initial, context-aware budget allocations, which serve as guiding beacons for users unfamiliar with financial nuances, thereby reducing the complexity of decision-making for non-experts.

Methodologically, the authors employ GPT-4 to analyze user-provided income and expense data, generating tailored recommendations. These LLM outputs are integrated into the optimization pipeline not as rigid directives but as adjustable constraints within a feasible solution space. The paper details a prospective validation framework involving expert review, contextual analysis against economic indicators, and risk assessment. It also proposes a Retrieval-Augmented Generation (RAG) approach to mitigate hallucinations by grounding recommendations in verifiable financial data and regulatory guidelines, ensuring the advice aligns with established financial principles and real-world conditions.

Preliminary results indicate that LLM-recommended solutions produce budget plans that are economically sound and aligned with user goals, outperforming traditional one-size-fits-all methods in personalization and adaptability. The system demonstrates high scalability and the ability to handle complex cooperative dynamics in households. However, the study acknowledges limitations such as potential LLM hallucinations, the need for human-in-the-loop oversight, and the reliance on simulated or preliminary validation rather than extensive longitudinal empirical testing. The work positions AI agents as influential actors in shaping human economic behavior, suggesting future integration with real-time data and expanded utility functions for long-term planning.

## An Evaluation of Reasoning Capabilities of Large Language Models in Financial Sentiment Analysis

- Year: 2024
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, prompt engineering, news, social media, accuracy, framework, hallucination, reasoning evaluation, zero-shot, prompt templates
- Tag facets: {"asset_class": [], "data_source": ["news", "social media"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["prompt engineering"], "risk_issue": ["hallucination"], "task": ["sentiment analysis"]}
- One-line summary: The paper evaluates LLM reasoning in financial sentiment analysis by introducing a Financial Attribute Prompting framework, revealing that models like GPT-3.5 and PaLM-2 lack inherent capabilities in numerical and comparative reasoning despite improvements from explicit prompts.

### Detailed Summary

This study addresses the gap in understanding how Large Language Models reason about specific financial attributes during sentiment analysis, a task distinct from general sentiment analysis due to its reliance on quantitative data, temporal context, and comparative benchmarks. The authors identify six key financial attributes—semantic, numerical, temporal, comparative, causal, and risk factors—and propose a Financial Attribute Prompting (FAP) framework to explicitly guide LLMs in considering these dimensions. The research aims to determine whether LLMs possess intrinsic reasoning capabilities for these attributes or require structured prompting to achieve competent performance in financial contexts.

The experimental design employs the FAP framework on two benchmark datasets: PhraseBank (financial news) and Twitter Financial News. The study evaluates zero-shot performance of GPT-3.5, PaLM-2, and GPT-4 against lexicon-based and supervised baselines like FinBERT. An ablation study isolates the impact of each financial attribute prompt to measure reasoning deficiencies. Results show that while FAP significantly boosts accuracy for PaLM-2 and GPT-3.5, allowing them to surpass unsupervised baselines, it reveals critical weaknesses. Specifically, removing numerical and comparative prompts causes sharp performance drops, indicating these models struggle to interpret quantitative metrics and relative performance comparisons without explicit instruction.

The findings highlight that LLMs do not inherently reason about financial nuances; they require structured guidance to process numerical and comparative data effectively. While causal reasoning shows some intrinsic capability in GPT-3.5, other attributes like temporal and risk factors yield inconsistent results across datasets, suggesting sensitivity to annotation criteria. The paper concludes that current LLMs lack the structural thinking framework of human analysts for FSA. This has implications for deploying LLMs in finance, as reliance on zero-shot capabilities may lead to errors in interpreting complex financial texts, necessitating robust prompting strategies or fine-tuning for reliable sentiment analysis.

## Agentic AI Systems Applied to tasks in Financial Services: Modeling and model risk management crews

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: fraud detection, portfolio optimization, bonds, institutional investing, multi-agent systems, agentic workflow, tool use, financial statements, accuracy, backtest, framework, model, model risk, hallucination, bias, model risk management, credit scoring, human-in-the-loop
- Tag facets: {"asset_class": ["bonds"], "data_source": ["financial statements"], "deliverable": ["framework", "model"], "evaluation": ["accuracy", "backtest"], "market_context": ["institutional investing"], "method": ["multi-agent systems", "agentic workflow", "tool use"], "risk_issue": ["model risk", "hallucination", "bias"], "task": ["fraud detection", "portfolio optimization"]}
- One-line summary: This paper implements and evaluates agentic crews using the CrewAI framework to automate financial modeling and model risk management (MRM) workflows, demonstrating robust performance in credit card fraud detection, approval, and portfolio risk tasks with human-in-the-loop oversight.

### Detailed Summary

The paper addresses the challenge of automating complex, regulated financial modeling and model risk management (MRM) processes by leveraging multi-agent systems. It positions agentic AI as a solution to streamline workflows that traditionally require significant human effort, focusing on the intersection of large language models (LLMs) and rigorous financial compliance standards. The authors argue that while LLMs offer autonomy, their 'black box' nature and potential for hallucination necessitate structured collaboration and human oversight in high-stakes financial environments.

The methodology involves building two distinct agentic crews using the CrewAI framework: a Modeling Crew and an MRM Crew. The Modeling Crew includes agents for data extraction, exploratory data analysis (EDA), feature engineering, hyperparameter tuning, training, evaluation, and documentation. The MRM Crew features agents for documentation compliance, model replication, conceptual soundness, and outcome analysis. A human-in-the-loop (HITL) module acts as an orchestrator, providing feedback and correcting errors. The system is tested on three datasets: credit card fraud detection, credit card approval, and portfolio credit risk modeling, utilizing LLMs such as Llama 3, Deepseek-R1, and GPT-3.5 Turbo.

Results indicate that the agentic crews effectively perform end-to-end modeling and validation tasks. The MRM agents successfully replicated models, verified conceptual soundness through feature importance analysis, and conducted stress testing with shifted inputs. The system demonstrated high accuracy in compliance checks and model replication, with metrics like AUC and F1-score closely matching original models. However, the paper notes a 1-10% error rate in code execution, highlighting the necessity of the HITL component. The study concludes that agentic systems can significantly enhance efficiency in financial modeling and MRM, provided that human oversight is integrated to manage safety, bias, and operational risks.

## RiskLabs: Predicting Financial Risk Using Large Language Model Based on Multi-Sources Data

- Year: 2024
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: forecasting, equities, portfolio management, multimodal modeling, retrieval, time-series modeling, earnings calls, news, ohlc data, backtest, drawdown, framework, model, model risk, value at risk, volatility prediction, multimodal fusion, earnings conference calls
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls", "news", "ohlc data"], "deliverable": ["framework", "model"], "evaluation": ["backtest", "drawdown"], "market_context": ["portfolio management"], "method": ["multimodal modeling", "retrieval", "time-series modeling"], "risk_issue": ["model risk"], "task": ["forecasting"]}
- One-line summary: RiskLabs is a multimodal framework that leverages LLMs to extract features from earnings calls, news, and time series data to significantly improve financial risk prediction compared to traditional baselines.

### Detailed Summary

The paper addresses the underexplored application of Large Language Models (LLMs) in financial risk prediction, specifically targeting volatility and Value at Risk (VaR). While LLMs have succeeded in text-based finance tasks, their direct use for numerical regression remains challenging. The authors position RiskLabs as a solution that integrates multimodal data—audio and text from Earnings Conference Calls (ECCs), daily news, and market time series—to provide a holistic view of market dynamics, moving beyond simple text summarization or sentiment analysis.

The RiskLabs framework employs specialized encoders for each data modality. ECC audio is processed via Wav2vec2 and self-attention, while transcripts are encoded using SimCSE and an LLM-based hierarchical summarization module that extracts key insights via a question bank. News is summarized by an LLM, and time series (VIX) is encoded using a BiLSTM. These features are fused additively and fed into a multi-task learning head to predict volatility across multiple horizons (3, 7, 15, 30 days) and 1-day VaR. Experiments compare RiskLabs against classical methods (GARCH), neural networks (LSTM, HAN, MRDM), and direct LLM prompting (GPT-3.5).

Results show RiskLabs outperforms all baselines in MSE for short-to-medium term volatility and achieves the most accurate VaR prediction (0.049 vs. target 0.05), significantly better than the historical method (0.016) and neural networks. Ablation studies confirm that adding LLM-derived analysis and time series data incrementally improves performance. A key finding is that direct LLM prompting for risk prediction is ineffective and potentially hazardous, establishing LLMs as powerful feature extractors rather than standalone predictors. Limitations include challenges with news quality and the need for dynamic windowing for long-term forecasts.

## BondBERT: What we learn when assigning sentiment in the bond market

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, forecasting, bonds, fine-tuning, domain adaptation, news, market prices, accuracy, information ratio, backtest, model, dataset, look-ahead bias, uk sovereign bonds, inverse sentiment-price relationship, synthetic labeling
- Tag facets: {"asset_class": ["bonds"], "data_source": ["news", "market prices"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy", "information ratio", "backtest"], "market_context": [], "method": ["fine-tuning", "domain adaptation"], "risk_issue": ["look-ahead bias"], "task": ["sentiment analysis", "forecasting"]}
- One-line summary: BondBERT, a transformer fine-tuned on bond-specific news, outperforms general financial sentiment models by correctly capturing the inverse relationship between economic optimism and bond prices, yielding higher directional accuracy and lower forecasting error for UK sovereign bonds.

### Detailed Summary

The paper addresses the critical gap in financial NLP where general sentiment models, trained on equity-centric data, fail to capture the inverse relationship between macroeconomic news and bond prices. While equity markets often rise on economic optimism, bond prices typically fall due to rising yield expectations. The authors introduce BondBERT, a domain-adaptive transformer designed to act as a perception module for financial decision-support agents, specifically targeting fixed-income dynamics where sentiment signals are noisy and effect sizes are small. The research positions BondBERT as a solution to the 'wrong-sign' bias inherent in models like FinBERT when applied to fixed income.

Methodologically, the authors compiled and cleaned 30,000 UK bond market articles from 2018–2025, using GPT-4.1-nano with specialized prompts to generate continuous sentiment labels in the [-1, 1] range. BondBERT was created by fine-tuning the FinBERT architecture on this bond-specific dataset, while baselines included ProsusAI/FinBERT, FinGPT (LLaMA-2-7B with LoRA), and Instruct-FinGPT (LLaMA-2-13B). Experiments evaluated sentiment alignment via event-based correlation on sentiment shock days, directional accuracy of next-day returns, and predictive power using an LSTM forecasting model across ten liquid UK sovereign bonds. Metrics included Pearson correlation, normalised RMSE, Information Coefficient (IC), and Diebold-Mariano tests.

Results demonstrate that BondBERT consistently produces positive correlations with bond returns, reversing the negative bias seen in FinBERT. It achieved the highest directional accuracy, significantly outperforming the random baseline, while FinGPT and Instruct-FinGPT performed poorly. In LSTM forecasting, BondBERT yielded the lowest normalised RMSE (0.0079 vs 0.0086 for FinBERT) and highest IC (0.80 vs 0.745). Diebold-Mariano tests confirmed statistical significance for several bonds. Limitations include reliance on synthetic GPT-generated labels which may introduce noise or look-ahead bias, and the restriction to liquid UK sovereign bonds, excluding corporate bonds due to illiquidity. The work highlights the necessity of domain-specific adaptation for LLMs in fixed-income markets.

## Reasoning or Overthinking: Evaluating Large Language Models on Financial Sentiment Analysis

- Year: 2025
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, chain of thought, prompt engineering, news, accuracy, benchmark, hallucination, zero-shot, overthinking, human alignment
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["benchmark"], "evaluation": ["accuracy"], "market_context": [], "method": ["chain of thought", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["sentiment analysis"]}
- One-line summary: The paper demonstrates that zero-shot financial sentiment classification aligns better with human judgment when using intuitive, direct prompting (System 1) rather than deliberative chain-of-thought reasoning (System 2), which often leads to overthinking and reduced accuracy.

### Detailed Summary

This study investigates whether explicit reasoning improves large language model (LLM) performance on financial sentiment analysis, a task grounded in human perception and intuition. The authors challenge the prevailing assumption that more reasoning universally enhances LLM decisions, positing that for subjective financial tasks, fast, intuitive judgment may better match human annotators than slow, deliberative processes. They evaluate three proprietary models (GPT-4o, GPT-4.1, o3-mini) and two finetuned baselines (FinBERT-Prosus, FinBERT-Tone) on the Financial PhraseBank dataset using zero-shot settings. The experimental design compares four prompting paradigms: No-CoT (direct classification), CoT-Short, CoT-Long, and LIRA (label first, then explanation), mapping these to cognitive System 1 and System 2 theories to assess alignment with human sentiment labels.

The evaluation focuses on macro F1 scores across varying levels of inter-annotator agreement and linguistic complexity. Results indicate that No-CoT prompting consistently yields the highest performance, with GPT-4o achieving the best overall alignment. Introducing explicit reasoning via CoT strategies degrades performance, particularly in low-ambiguity cases. The reasoning-optimized model o3-mini performs the worst, generating verbose outputs that correlate negatively with accuracy. LIRA prompting outperforms forward-chained CoT, suggesting that post-hoc rationalization aligns better with human interpretation than pre-commitment reasoning. Finetuned models like FinBERT-Prosus perform well in-domain but generalize poorly to complex or ambiguous out-of-domain text compared to zero-shot general-purpose LLMs.

The findings suggest that reasoning can introduce 'overthinking,' causing models to misalign with human heuristic judgments. Longer completion tokens are negatively correlated with performance, indicating that verbose reasoning dilutes predictive accuracy. The study highlights that while reasoning might help in highly ambiguous scenarios, it generally harms performance on clear-cut financial sentiment tasks. Limitations include the focus on zero-shot settings and the use of human-annotated sentiment rather than market-impact data, meaning the results reflect alignment with human perception rather than predictive power for stock movements. The work advises matching prompting strategies to task nature, favoring intuitive approaches for sentiment classification.

## Interpretable LLMs for Credit Risk: A Systematic Review and Taxonomy

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: credit scoring, fraud detection, sentiment analysis, spreadsheet reasoning, chain of thought, domain adaptation, fine-tuning, instruction tuning, financial statements, news, sec filings, tables, accuracy, literature review, taxonomy, bias, hallucination, regulatory compliance, explainable ai, xai
- Tag facets: {"asset_class": [], "data_source": ["financial statements", "news", "sec filings", "tables"], "deliverable": ["literature review", "taxonomy"], "evaluation": ["accuracy"], "market_context": [], "method": ["chain of thought", "domain adaptation", "fine-tuning", "instruction tuning"], "risk_issue": ["bias", "hallucination", "regulatory compliance"], "task": ["credit scoring", "fraud detection", "sentiment analysis", "spreadsheet reasoning"]}
- One-line summary: This paper presents the first systematic review and taxonomy of LLM-based credit risk assessment, categorizing 60 studies by model architecture, data modality, interpretability mechanisms, and application domains to highlight trends and research gaps.

### Detailed Summary

The paper addresses the lack of systematic classification in the rapidly growing field of Large Language Models (LLMs) applied to credit risk assessment. While traditional credit scoring relies on structured financial ratios, LLMs offer the potential to extract risk signals from unstructured texts like analyst reports, disclosures, and news. The authors identify a critical gap in existing literature: most surveys either focus broadly on generative AI in banking or narrowly on specific ML techniques, failing to provide a comprehensive taxonomy that integrates model architectures with the crucial requirement of interpretability (XAI) for high-stakes financial decisions. This work aims to serve as a reference framework for researchers and practitioners navigating the intersection of NLP, finance, and explainable AI.

The methodology follows the PRISMA guidelines to select 60 relevant papers published between 2020 and 2025 from major academic databases. The authors construct a four-pillar taxonomy: model architectures (encoder-only, decoder-only, hybrid, and domain-specific FinLLMs), data modalities (structured, unstructured text, time-series, multimodal, and synthetic data), interpretability mechanisms (post-hoc XAI like SHAP/LIME, chain-of-thought prompting, and intrinsically transparent designs), and application areas (retail/SME scoring, fraud detection, sentiment analysis, and investment). Experiments and findings are synthesized from the selected studies, covering benchmarks like FinLLM Leaderboard and FinLMEval, and evaluating metrics such as F1 scores, fairness indices (ISIP/ISA), and hallucination rates. The review highlights the shift from black-box predictions to transparent, regulation-compliant systems.

Key findings indicate that encoder-only models (e.g., FinBERT) excel in fine-tuning for classification, while decoder models (e.g., GPT-4) are preferred for generative tasks and few-shot scenarios. Hybrid pipelines combining LLMs with traditional ML (e.g., GPT-LGBM) and Retrieval-Augmented Generation (RAG) show promise in mitigating data scarcity and hallucination. Interpretability is achieved through post-hoc methods, instruction tuning, and novel architectures like Logit Leaf. Use cases span P2P lending, SME credit scoring, AML, and bond yield prediction. Limitations include the predominance of preprints, lack of standardized benchmarks for credit-specific XAI, and challenges in ensuring fairness and reproducibility across diverse datasets. The paper concludes by outlining future directions for robust, interpretable, and fair LLM deployment in credit risk.

## MarketSenseAI 2.0: Enhancing Stock Analysis Through LLM Agents

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, equity research, portfolio optimization, earnings analysis, equities, us equities, agentic workflow, chain of thought, retrieval, 10-k filings, earnings calls, financial statements, market prices, news, backtest, portfolio returns, risk-adjusted returns, framework, model, hallucination
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "earnings calls", "financial statements", "market prices", "news"], "deliverable": ["framework", "model"], "evaluation": ["backtest", "portfolio returns", "risk-adjusted returns"], "market_context": ["us equities"], "method": ["agentic workflow", "chain of thought", "retrieval"], "risk_issue": ["hallucination"], "task": ["alpha mining", "equity research", "portfolio optimization", "earnings analysis"]}
- One-line summary: MarketSenseAI 2.0 leverages a multi-agent LLM architecture with RAG to integrate SEC filings, earnings calls, and macroeconomic reports, achieving 125.9% cumulative returns on S&P 100 stocks (2023-2024) and a 33.8% higher Sortino ratio on S&P 500 stocks (2024) compared to benchmarks.

### Detailed Summary

MarketSenseAI 2.0 addresses the fragmentation in stock analysis by integrating heterogeneous data sources—financial news, historical prices, company fundamentals, and macroeconomic environments—into a unified decision-making framework. The system aims to overcome limitations of traditional quantitative models that often ignore textual context and qualitative insights, providing transparent, explainable investment signals through a Chain-of-Agents (CoA) architecture. By combining Retrieval-Augmented Generation (RAG) with specialized LLM agents, the framework processes complex documents like 10-K filings and earnings call transcripts, enriching macroeconomic analysis with institutional reports to support holistic stock selection.

The methodology employs five distinct LLM agents: News, Fundamentals, Dynamics, Macroeconomic, and Signal. The Fundamentals Agent uses a three-layer approach to summarize SEC filings and earnings calls, integrating qualitative managerial tone with quantitative financial ratios. The Macroeconomic Agent utilizes semantic chunking and Hypothetical Dense Embeddings (HyDE) for retrieval from a vector datastore containing central bank and investment bank reports. Empirical evaluations were conducted on S&P 100 stocks over 2023-2024 and S&P 500 stocks in 2024, using VectorBTPro for backtesting and Ragas for RAG evaluation. The system generates monthly long-only portfolios based on buy signals, comparing performance against benchmark indices and factor models.

Results indicate significant outperformance, with MarketSenseAI achieving 125.9% cumulative returns on the S&P 100 versus 73.5% for the index, and a 33.8% higher Sortino ratio on the S&P 500. Factor analysis reveals unexplained alpha of 8.0%, suggesting the model captures idiosyncratic opportunities beyond traditional value and momentum factors. The inclusion of textual data from filings and calls moderates sentiment scores, revealing hidden risks and shifting approximately 5% of investment signals. Limitations include reliance on GPT-4o, potential context window constraints, and the need for robust prompt engineering to ensure reproducibility and mitigate hallucinations in financial reasoning.

## PyFi: Toward Pyramid-like Financial Image Understanding for VLMs via Adversarial Agents

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, financial question answering, multi-agent systems, mcts, chain of thought, fine-tuning, tables, accuracy, dataset, framework, model, data leakage, hallucination, vision-language models, synthetic data, visual reasoning, process supervision
- Tag facets: {"asset_class": [], "data_source": ["tables"], "deliverable": ["dataset", "framework", "model"], "evaluation": ["accuracy"], "market_context": [], "method": ["multi-agent systems", "mcts", "chain of thought", "fine-tuning"], "risk_issue": ["data leakage", "hallucination"], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: PyFi introduces a pyramid-structured dataset and adversarial multi-agent synthesis framework to enable vision-language models to perform hierarchical financial image understanding, significantly improving accuracy on complex decision-support tasks through chain-of-thought fine-tuning.

### Detailed Summary

The paper addresses the scarcity of high-quality, expert-level visual reasoning data for financial vision-language models (VLMs), noting that existing benchmarks rely on costly human annotation or hallucinated synthetic data. It proposes PyFi, a framework that structures financial image understanding into a six-level pyramid ranging from basic perception to complex decision support, enabling progressive reasoning through interconnected question chains. This hierarchical approach aims to provide interpretable, step-wise guidance for VLMs to solve intricate financial problems that require deep domain expertise and visual analysis.

The core contribution is PyFi-600K, a dataset of 600,000 samples synthesized automatically using PyFi-adv, a multi-agent adversarial mechanism based on Monte Carlo Tree Search. A challenger agent generates increasingly difficult questions while a solver agent attempts to answer them, creating hierarchical question chains with reward scores for process supervision. The authors evaluate 15 pre-trained VLMs, revealing a sharp accuracy drop from 71.80% at the perception level to 32.95% at the decision level. They then fine-tune Qwen2.5-VL-3B and 7B models on these chains, demonstrating that supervised fine-tuning with chain-of-thought annotations significantly enhances the models' ability to decompose and solve complex financial visual tasks.

Results show that fine-tuning yields average accuracy improvements of 19.52% for the 3B model and 8.06% for the 7B model, with the smaller model benefiting disproportionately from the chain-of-thought training. The study highlights that errors in calculation analysis and data extraction are primary causes of failure in higher-level decision support. While the framework effectively improves interpretability and performance on financial charts and infographics, the reliance on synthetic data generation introduces potential biases, and the current scope is limited to visual reasoning rather than broader market prediction or trading execution.

## When Agents Trade: Live Multi-Market Trading Benchmark for LLM Agents

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, portfolio optimization, equities, crypto, agentic workflow, backtesting, news, market prices, sharpe ratio, drawdown, portfolio returns, benchmark, dataset, trading agent, model risk, multi-agent systems, agent architecture, live trading, behavioral analysis
- Tag facets: {"asset_class": ["equities", "crypto"], "data_source": ["news", "market prices"], "deliverable": ["benchmark", "dataset", "trading agent"], "evaluation": ["sharpe ratio", "drawdown", "portfolio returns"], "market_context": [], "method": ["agentic workflow", "backtesting"], "risk_issue": ["model risk"], "task": ["algorithmic trading", "portfolio optimization"]}
- One-line summary: The paper introduces Agent Market Arena (AMA), a live multi-market benchmark demonstrating that agent architecture, rather than LLM backbone, primarily determines trading performance and behavioral patterns in real-time financial markets.

### Detailed Summary

The paper addresses the critical gap in evaluating LLM-based trading agents by introducing Agent Market Arena (AMA), the first lifelong, real-time benchmark for assessing financial reasoning and adaptability. Existing benchmarks often test static models or rely on unverified, noisy data over limited periods. AMA provides a unified framework with verified, expert-checked news and price data across equities and cryptocurrencies, enabling continuous, fair comparison of diverse agent architectures under live market conditions. This setup allows for rigorous evaluation of how agents perceive, plan, and act in dynamic, high-stakes environments, moving beyond simple prediction tasks to sequential decision-making.

The experimental design deploys four distinct agent frameworks—InvestorAgent, TradeAgent, HedgeFundAgent, and DeepFundAgent—across five leading LLM backbones (GPT-4o, GPT-4.1, Claude-3.5-haiku, Claude-sonnet-4, Gemini-2.0-flash). These agents operate in a live environment trading Tesla (TSLA), BioMarin (BMRN), Bitcoin (BTC), and Ethereum (ETH) for two months. The Market Intelligence Stream aggregates and verifies multi-source data, while the Agent Execution Protocol standardizes inputs and outputs. Performance is tracked via cumulative return, Sharpe ratio, volatility, and maximum drawdown, with a transparent leaderboard providing real-time analytics.

Results indicate that LLM-based agents can outperform buy-and-hold strategies, but agent architecture is the dominant factor shaping performance, outweighing the choice of LLM backbone. InvestorAgent achieved high Sharpe ratios (e.g., 6.47 on TSLA with GPT-4.1), while DeepFundAgent showed balanced adaptability. TradeAgent and HedgeFundAgent exhibited aggressive risk-taking with higher volatility. The study highlights that specific agent-model pairings yield optimal results, suggesting complementarity. Limitations include the short evaluation period and the specific asset selection, though the framework is designed for continuous evolution. The work establishes a reproducible foundation for studying financial intelligence in autonomous agents.

## Multimodal Financial Foundation Models (MFFMs): Progress, Prospects, and Challenges

- Year: 2025
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, risk extraction, regulatory reporting, factor modeling, xbrl tagging, earnings analysis, equities, portfolio management, agentic workflow, multimodal modeling, fine-tuning, earnings calls, sec filings, tables, xbrl, accuracy, taxonomy, framework, hallucination, privacy
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls", "sec filings", "tables", "xbrl"], "deliverable": ["taxonomy", "framework"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["agentic workflow", "multimodal modeling", "fine-tuning"], "risk_issue": ["hallucination", "privacy", "regulatory compliance"], "task": ["alpha mining", "risk extraction", "regulatory reporting", "factor modeling", "xbrl tagging", "earnings analysis"]}
- One-line summary: This position paper surveys Multimodal Financial Foundation Models (MFFMs), detailing their data-centric approach, agentic applications, and critical challenges in transparency, reasoning, and governance.

### Detailed Summary

The paper addresses the evolution from unimodal Financial LLMs to Multimodal Financial Foundation Models (MFFMs) capable of processing interleaved data types including text, audio, video, charts, and tabular financial records. It positions MFFMs as essential for handling the complexity of real-world financial data, such as earnings calls and regulatory filings, which contain rich multimodal signals beyond simple text. The authors argue that current language-centric models are insufficient for tasks requiring deep integration of diverse data sources, such as interpreting visual charts in reports or analyzing audio sentiment in conference calls.

The authors provide a comprehensive taxonomy of multimodal financial data, covering Earnings Conference Calls (ECCs), Monetary Policy Conferences (MPCs), SEC filings (10-K, 10-Q), financial news, market time-series, and climate data. They discuss specific datasets like MDRM and MONOPOLY, highlighting challenges in data curation, alignment, and storage. The paper also introduces an agentic FinAI ecosystem, detailing tool agents (search, tutor, XBRL) and service agents (robo-advisors, compliance auditors) powered by frameworks like FinGPT and protocols like MCP and A2A. Experiments and case studies include the development of a 'Warren Buffett' agent via FinLoRA and the use of FinRL for trading strategies.

Key findings emphasize the potential of MFFMs to democratize financial services and enhance decision-making through agentic workflows. However, significant challenges remain, including 'model cannibalism,' 'openwashing,' hallucination, and the high cost of training and inference. The paper calls for robust guardrail frameworks, better benchmarks like CFA exam evaluations, and adherence to openness standards. It concludes that while MFFMs offer promising prospects for alpha mining, risk modeling, and automated reporting, achieving 'FinAI readiness' requires solving critical issues in transparency, privacy, and regulatory compliance.

## A Comprehensive Review of Gen AI Agents: Applications and Frameworks in Finance, Investments and Risk Domains

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: fraud detection, portfolio optimization, algorithmic trading, market microstructure, institutional investing, multi-agent systems, agentic workflow, risk-adjusted returns, accuracy, framework, literature review, regulatory compliance, model risk, generative ai agents, multi-agent architecture, productivity gains, deployment challenges
- Tag facets: {"asset_class": [], "data_source": [], "deliverable": ["framework", "literature review"], "evaluation": ["risk-adjusted returns", "accuracy"], "market_context": ["market microstructure", "institutional investing"], "method": ["multi-agent systems", "agentic workflow"], "risk_issue": ["regulatory compliance", "model risk"], "task": ["fraud detection", "portfolio optimization", "algorithmic trading"]}
- One-line summary: This 2025 survey synthesizes the landscape of generative AI agent frameworks and their applications in finance, highlighting productivity gains, multi-agent architectures, and deployment challenges.

### Detailed Summary

This paper provides a comprehensive review of generative AI agent frameworks and their specific applications within the financial services sector, including trading, investment analysis, and risk management. It positions agentic AI as the next evolutionary step beyond standard LLMs, emphasizing the shift toward autonomous, self-reasoning systems capable of complex, multi-step financial tasks. The authors synthesize insights from academic research, industry reports, and technical documentation to map the current state of the art, focusing on the transition from single-agent tools to collaborative multi-agent systems that can handle sophisticated financial workflows and decision support scenarios.

The methodology involves a comparative analysis of prominent open-source and enterprise frameworks, including LangGraph, CrewAI, AutoGen, and LlamaIndex, alongside cloud platforms like IBM watsonx and NVIDIA NIM. The paper outlines a proposed three-layer multi-agent architecture comprising data, agent, and orchestration layers, supported by theoretical foundations such as verbal reinforcement learning and market microfoundations. It evaluates these systems through proposed scenarios like portfolio optimization, fraud detection, and algorithmic trading, using metrics such as accuracy, efficiency, and risk-adjusted returns, while benchmarking against traditional rule-based and single-agent baselines.

Key findings indicate that specialized agent frameworks can achieve 50-80% productivity gains in financial data tasks, with multi-agent systems showing particular promise in complex domains like fraud detection and algorithmic trading. The paper highlights real-world examples, such as an 80% reduction in data task time and significant workforce efficiency improvements. However, it cautions that successful deployment requires addressing critical challenges in regulatory compliance, risk alignment, and workforce upskilling. The study concludes that while agentic AI offers transformative potential, financial institutions must adopt standardized architectures, robust testing protocols, and hybrid human-AI workflows to mitigate risks and ensure reliable performance in production environments.

## Large Language Model Adaptation for Financial Sentiment Analysis

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, fine-tuning, instruction tuning, domain adaptation, sec filings, news, accuracy, model, dataset, small language models, synthetic data generation
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "news"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "instruction tuning", "domain adaptation"], "risk_issue": [], "task": ["sentiment analysis"]}
- One-line summary: The paper demonstrates that small LLMs (under 1.5B parameters) can outperform larger generalist and specialized financial models in financial sentiment analysis and related tasks through a two-stage adaptation process involving further pre-training on financial documents and instruction fine-tuning with synthetic data augmentation.

### Detailed Summary

This paper addresses the challenge of adapting Large Language Models (LLMs) to the financial domain, specifically focusing on financial sentiment analysis. It argues that generalist LLMs often underperform on complex financial texts due to specific terminology and complexity, necessitating domain adaptation. The study aims to show that smaller, more efficient models can achieve competitive performance compared to larger, resource-intensive models like BloombergGPT or GPT-4, thereby lowering the barrier to entry for financial institutions. The research positions itself within the context of existing financial LLMs like FinBERT and FinMA, highlighting the need for efficient, accessible models that maintain high accuracy on financial NLP tasks.

The methodology involves adapting two foundation models, Pythia-1.4B and OPT-1.3B, using a two-stage fine-tuning strategy. First, the models undergo further pre-training on a curated dataset of financial documents (EDGAR, Reuters, in-house) mixed with general data (The Pile) to shift their language understanding towards finance. Second, they are fine-tuned on an instruction dataset derived from the FLARE benchmark, which includes tasks like sentiment analysis, named entity recognition (NER), and news headline classification. A key innovation is the use of a larger LLM (LLaMA-2-13B) to generate synthetic instructions and inputs to augment the training data, particularly for tasks with limited samples. The models are evaluated on the FLARE benchmark, comparing their performance against classical ML algorithms, generalist LLMs (GPT-4), and other financial LLMs (BloombergGPT, FinMA).

The results indicate that the two-stage adaptation strategy significantly improves model performance. The fine-tuned small models outperform GPT-4 and BloombergGPT on classification tasks such as financial sentiment analysis and headline classification, achieving F1 scores of 0.84-0.86 on the Financial Phrase Bank. They also show competitive performance on NER, though GPT-4 remains superior in generative tasks. The study finds that instruction fine-tuning yields greater improvements than document pre-training alone, and data augmentation enhances performance on sentiment tasks but can slightly degrade performance on others due to distribution shifts. The paper concludes that small, adapted LLMs offer a highly efficient alternative to large-scale models for specific financial tasks, though they lag in generative capabilities and may require further testing on unseen tasks and larger model scales.

## Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: alpha mining, factor modeling, equities, us equities, china market, agentic workflow, backtesting, retrieval, ohlc data, sec filings, backtest, information ratio, portfolio returns, sharpe ratio, framework, model, trading agent, overfitting, human-ai interaction, symbolic alpha expressions
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "sec filings"], "deliverable": ["framework", "model", "trading agent"], "evaluation": ["backtest", "information ratio", "portfolio returns", "sharpe ratio"], "market_context": ["us equities", "china market"], "method": ["agentic workflow", "backtesting", "retrieval"], "risk_issue": ["overfitting"], "task": ["alpha mining", "factor modeling"]}
- One-line summary: Alpha-GPT introduces a human-AI interactive framework for quantitative alpha mining, leveraging LLMs to translate trading ideas into formulaic factors and achieving top-10 global rankings in the WorldQuant International Quant Championship 2024.

### Detailed Summary

The paper addresses the inefficiency and labor-intensity of traditional alpha mining, which relies on manual factor synthesis or compute-heavy algorithmic search. It proposes a third paradigm centered on human-AI interaction, where Large Language Models (LLMs) act as mediators to interpret quant researchers' natural language intuitions and translate them into executable symbolic alpha expressions. This approach aims to bridge the gap between abstract trading concepts and precise mathematical formulations, reducing the cognitive load on researchers and accelerating the discovery of effective trading signals.

The proposed system, Alpha-GPT, employs an agentic workflow comprising ideation, implementation, and review stages. In the ideation phase, a 'Trading Idea Polisher' agent uses Retrieval-Augmented Generation (RAG) over financial literature and data field databases to formalize user inputs. The 'Quant Developer' agent then generates seed alpha expressions, which are refined using genetic programming in the implementation stage. The 'Analyst' agent evaluates these alphas via backtesting engines, providing natural language feedback to guide iterative refinement. The system supports both interactive mode, where humans guide the process, and autonomous mode, which uses hierarchical RAG to explore large-scale quantitative databases without overwhelming the LLM's context window.

Empirical evaluations demonstrate Alpha-GPT's effectiveness in improving research efficiency and alpha quality. In consistency tests, Alpha-GPT-generated factors outperformed those from junior human researchers, achieving an 86.6% win rate in pairwise comparisons. Search enhancement experiments showed significant improvements in Information Coefficient (IC) over 20 iterations, with out-of-sample IC stabilizing to indicate good generalization. Notably, in the WorldQuant International Quant Championship 2024, Alpha-GPT ranked among the top 10 worldwide out of 41,000 teams, generating 81 qualified alphas with competitive in-sample and out-of-sample scores. The system also successfully captured complex technical patterns like Bollinger band breakouts and moving average divergences, validating its ability to translate abstract ideas into concrete, profitable signals.

## MME-Finance: A Multimodal Finance Benchmark for Expert-level Understanding and Reasoning

- Year: 2025
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, equity research, spreadsheet reasoning, equities, us equities, china market, multimodal modeling, ohlc data, tables, accuracy, benchmark, dataset, hallucination, multimodal llm, chart interpretation, visual perception, bilingual evaluation, llm-as-a-judge
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities", "china market"], "method": ["multimodal modeling"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "equity research", "spreadsheet reasoning"]}
- One-line summary: MME-Finance is a bilingual multimodal benchmark evaluating 19 MLLMs on financial charts, revealing that while top models like GPT-4o and Qwen2VL-72B show competence, they struggle significantly with fine-grained visual perception, spatial awareness, and domain-specific chart interpretation.

### Detailed Summary

The paper addresses the lack of rigorous benchmarks for Multimodal Large Language Models (MLLMs) in the financial domain, where unique challenges include specialized jargon, complex chart types like candlesticks, and high data density. Existing general benchmarks fail to capture these nuances, necessitating a domain-specific evaluation tool to guide the development of large financial models. The authors introduce MME-Finance, the first comprehensive bilingual (English and Chinese) multimodal benchmark designed to assess expert-level understanding and reasoning in finance.

The benchmark comprises 4,751 curated samples, including open-ended, binary-choice, and multi-turn questions, covering six image types: candlestick charts, technical indicator charts, statistical charts, tables, documents, and mixed charts. Data collection simulates real-world usage via computer screenshots and mobile photographs. Annotation involves experts with 10+ years of experience. The evaluation pipeline uses an LLM-based evaluator (GPT-4o) that incorporates visual context to score open-ended responses, achieving high consistency with human judges. The study evaluates 19 mainstream MLLMs, including open-source models like Qwen2VL-72B and proprietary ones like GPT-4o, across perception, reasoning, and cognition tasks.

Results indicate that state-of-the-art MLLMs exhibit significant deficiencies in fine-grained visual perception and domain-specific image understanding. GPT-4o achieved the highest accuracy on open-ended questions (79.28% in the abstract, though text reports 63.18% overall score normalized), while Qwen2VL-72B led open-source models. Models performed poorly on candlestick and technical indicator charts, as well as on mobile photographs due to resolution and angle issues. Spatial awareness and estimated numerical calculations were particularly challenging. The paper highlights that models excelling in general benchmarks do not necessarily perform well in finance, underscoring the need for specialized training and evaluation.

## From fiction to fact: the growing role of generative AI in business and finance

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: case study
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, equities, us equities, prompt engineering, time-series modeling, annual reports, sec filings, risk-adjusted returns, sharpe ratio, framework, bias, hallucination, environmental policy, cap-and-trade, prompt sensitivity
- Tag facets: {"asset_class": ["equities"], "data_source": ["annual reports", "sec filings"], "deliverable": ["framework"], "evaluation": ["risk-adjusted returns", "sharpe ratio"], "market_context": ["us equities"], "method": ["prompt engineering", "time-series modeling"], "risk_issue": ["bias", "hallucination"], "task": ["sentiment analysis", "stock prediction"]}
- One-line summary: This study demonstrates that ChatGPT-generated sentiment scores from corporate annual reports regarding environmental policy effectively predict firms' risk management adjustments and subsequent stock return performance.

### Detailed Summary

This paper addresses the emerging role of generative AI in financial decision-making, specifically focusing on its ability to extract actionable insights from unstructured corporate text. It positions generative AI not just as a tool for content creation but as a valid instrument for sentiment analysis and risk assessment, bridging the gap between natural language processing and quantitative finance. The authors aim to validate whether AI-derived sentiment can serve as a reliable predictor for firm behavior and market outcomes, contributing to the literature on AI applications in investment research.

The methodology involves a case study using ChatGPT 3.5 and ChatGPT 4 to analyze sentiment towards California’s cap-and-trade program in the annual reports of 321 affected firms. The authors extract text mentioning the policy, input it into the models with a strict prompt template to generate negative sentiment scores on a 0-1 scale, and correlate these scores with financial data from Compustat. They employ regression models with firm fixed effects to test the relationship between AI-generated sentiment, R&D spending, leverage, and stock volatility, comparing the predictive power of ChatGPT 4 against ChatGPT 3.5 and traditional keyword mentions.

The findings reveal that higher negative sentiment scores generated by ChatGPT 4 are significantly associated with increased R&D investment in cleaner technology and reduced leverage, indicating proactive risk management. Furthermore, these sentiment scores predict lower stock return volatility following the policy implementation, suggesting that investors reward firms that manage environmental regulatory risks effectively. The study highlights that ChatGPT 4 outperforms earlier versions and Bard in reasoning and consistency. However, it notes limitations such as prompt sensitivity and the need for regulatory frameworks to address ethical concerns and potential biases in AI-driven financial analysis.

## LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, factor modeling, equities, us equities, china market, prompt engineering, time-series modeling, news, ohlc data, accuracy, ablation study, framework, benchmark, bias, explainability, factor extraction
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "ohlc data"], "deliverable": ["framework", "benchmark"], "evaluation": ["accuracy", "ablation study"], "market_context": ["us equities", "china market"], "method": ["prompt engineering", "time-series modeling"], "risk_issue": ["bias"], "task": ["stock prediction", "factor modeling"]}
- One-line summary: LLMFactor introduces Sequential Knowledge-Guided Prompting to extract explainable factors from news and historical prices, achieving superior stock movement prediction accuracy over keyphrase, sentiment, and time-series baselines across US and Chinese markets.

### Detailed Summary

The paper addresses the challenge of explainable stock movement prediction by proposing LLMFactor, a framework that extracts specific market factors from textual news rather than relying on generic sentiment or keyphrases. The authors argue that factors provide better human readability and direct correlation to price dynamics, addressing the black-box nature of traditional deep learning models and the limited interpretability of sentiment analysis. The research positions this approach as a novel task in financial NLP, aiming to bridge the gap between unstructured text analysis and structured time-series forecasting.

The core method, Sequential Knowledge-Guided Prompting (SKGP), operates in three steps: first, it uses a fill-in-the-blank strategy to identify relationships between the target stock and related companies in the news; second, it extracts the top-k factors influencing the stock price; and third, it combines these factors with historical price movements converted into text to predict future direction. The study evaluates this framework using GPT-3.5-turbo, GPT-4, and GPT-4-turbo on four benchmark datasets (StockNet, CMIN-US, CMIN-CN, and EDT), comparing performance against keyphrase-based, sentiment-based, and time-series baselines using Accuracy and Matthews Correlation Coefficient (MCC).

Results show LLMFactor outperforms state-of-the-art methods, with GPT-4 achieving the highest MCC scores across US datasets. Ablation studies reveal that the extracted factors contribute significantly to performance gains, particularly in MCC, while historical price data remains the strongest predictor. The framework demonstrates strong explainability through case studies on Apple and Tesla. However, limitations include reliance on LLM API variability, reduced performance on Chinese datasets due to language proficiency gaps in GPT models, and the challenge of converting time-series data into text without losing nuance.

## FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation

- Year: 2025
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, benchmarking, equities, derivatives, commodities, forex, options, portfolio management, multimodal modeling, retrieval, annual reports, tables, accuracy, benchmark, dataset, hallucination, chart reasoning, financial charts, mllm evaluation, multimodal finance
- Tag facets: {"asset_class": ["equities", "derivatives", "commodities", "forex", "options"], "data_source": ["annual reports", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["multimodal modeling", "retrieval"], "risk_issue": ["hallucination"], "task": ["equity research", "benchmarking"]}
- One-line summary: The paper introduces FinMME, a large-scale multimodal benchmark with over 11,000 high-quality financial samples across 18 domains, demonstrating that state-of-the-art MLLMs struggle with financial chart reasoning and introducing FinScore to penalize hallucinations.

### Detailed Summary

The paper addresses the critical lack of specialized evaluation frameworks for Multimodal Large Language Models (MLLMs) in the finance domain, where high knowledge density and complex visual data require rigorous assessment. Existing general benchmarks fail to capture the nuances of financial analysis, such as interpreting diverse chart types and performing domain-specific reasoning. The authors position FinMME as a comprehensive solution to bridge this gap, providing a structured, high-quality dataset designed to test and improve MLLM capabilities in real-world financial scenarios, including equity research, macroeconomic analysis, and asset allocation.

FinMME comprises 11,099 samples spanning 18 core financial domains and 6 asset classes, featuring 10 major chart types and 21 subtypes. Data was curated from professional research reports and web sources, with a rigorous annotation pipeline involving 20 human annotators and LLM-based consistency checks to maintain error rates below 1%. The evaluation framework, FinScore, incorporates domain-normalized scoring and hallucination penalties to ensure unbiased assessment. Experiments evaluated 17 proprietary and open-source models, including GPT-4o, Claude 3.5 Sonnet, and Qwen2.5-VL, using multiple-choice and calculation questions across comprehensive perception, fine-grained perception, and cognitive reasoning dimensions.

Results indicate that even leading models like GPT-4o achieve only around 46% average accuracy, with calculation tasks being the most challenging. Proprietary models generally outperform open-source alternatives, though Qwen2.5-VL-72B shows competitive performance in specific domains. The benchmark demonstrates high robustness, with prediction variations under different prompts remaining below 1%. However, the study acknowledges limitations, including a reliance on multiple-choice formats that may not fully capture complex financial analysis, potential biases in expert annotations, and a lack of audio/video content. The dataset is released to facilitate future research in financial multimodal reasoning.

## OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, retrieval, fine-tuning, multi-agent systems, sec filings, news, accuracy, benchmark, dataset, open source, hallucination, evaluation framework, retriever evaluation, generator evaluation, multi-hop reasoning
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "dataset", "open source"], "evaluation": ["accuracy"], "market_context": [], "method": ["retrieval", "fine-tuning", "multi-agent systems"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: OmniEval introduces an omnidirectional, automatic RAG benchmark for finance using a matrix-based topic-task evaluation framework, multi-agent data generation, and fine-tuned LLM evaluators to reveal significant performance gaps in vertical domain RAG systems.

### Detailed Summary

The paper addresses the lack of comprehensive, automatic evaluation benchmarks for Retrieval-Augmented Generation (RAG) systems in specialized vertical domains, specifically finance. Existing benchmarks often focus solely on final response quality or lack domain-specific granularity. OmniEval aims to provide an omnidirectional assessment that captures the nuances of financial queries by structuring the evaluation space into a matrix of 16 financial topics and 5 task classes, including extractive QA, multi-hop reasoning, and conversational QA. This positioning allows for a structured, multi-dimensional profile of RAG capabilities rather than a single aggregate score.

The methodology involves constructing a diverse knowledge corpus from sources like BSCF, FinGLM, and official web pages, processed via LlamaIndex. Data generation utilizes a multi-agent pipeline powered by GPT-4 to create question-answer pairs aligned with the topic-task matrix, followed by automatic and manual quality inspections, achieving an 87.47% human acceptance rate. The evaluation system combines rule-based metrics (Rouge-L, MAP, MRR) with five fine-tuned LLM-based metrics (Accuracy, Completeness, Hallucination, Utilization, Numerical Accuracy) trained on Qwen2.5-7B. Experiments evaluate various retrievers (BGE-M3, GTE-Qwen2) and generators (Llama3.1, Qwen2.5) on both auto-generated and human-annotated test sets.

Results indicate that RAG systems generally outperform close-book LLMs but still exhibit significant room for improvement in financial domains. Performance varies substantially across different topics and tasks, with multi-hop reasoning and conversational QA posing particular challenges. The study highlights that retrievers fine-tuned from LLMs (like GTE-Qwen2) perform better than those trained from scratch. The benchmark reveals imbalances in RAG capabilities across topics, suggesting that pre-training corpus popularity influences retrieval effectiveness. The paper provides open-source code and datasets, serving as a critical resource for advancing RAG reliability in finance.


## Open FinLLM Leaderboard: Towards Financial AI Readiness

- Year: 2025
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, financial question answering, forecasting, risk extraction, xbrl tagging, retrieval, xbrl, tables, sec filings, accuracy, backtest, benchmark, leaderboard, dataset, hallucination, multimodal modeling, zero-shot evaluation, privacy-preserving verification, community-driven ecosystem
- Tag facets: {"asset_class": [], "data_source": ["xbrl", "tables", "sec filings"], "deliverable": ["benchmark", "leaderboard", "dataset"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["benchmarking", "financial question answering", "forecasting", "risk extraction", "xbrl tagging"]}
- One-line summary: The paper introduces an open, continuously updated FinLLM leaderboard developed with the Linux Foundation and Hugging Face to standardize the evaluation of financial language models and agents across multimodal tasks, addressing the static nature of existing benchmarks.

### Detailed Summary

The paper addresses the critical need for robust, dynamic evaluation frameworks for Financial Large Language Models (FinLLMs) and FinAgents, noting that existing benchmarks like FinBen and FinanceBench are static and insufficient for tracking rapid model advancements. The authors propose an open FinLLM leaderboard, a collaborative platform designed to democratize access to financial AI readiness by providing a standardized, transparent, and continuously updated ecosystem for assessing model performance. This initiative aims to bridge the gap between academic research and industry deployment by fostering a community-driven approach to benchmarking, ensuring that models are evaluated on their real-world utility and reliability in complex financial contexts.

The methodology involves a comprehensive testing pipeline that evaluates popular models, including GPT-4, LLaMA 3.1, Gemini, and Qwen2, using zero-shot settings on expert-validated datasets. The leaderboard covers seven task categories: Information Extraction, Textual Analysis, Question Answering, Text Generation, Risk Management, Forecasting, and Decision-Making, utilizing 42 financial datasets that include multimodal data such as text, tables, and XBRL filings. The evaluation process employs specific metrics like Accuracy, F1, ROUGE, and BERTScore, with scores normalized to a 0-100 scale for fair comparison. Additionally, the platform integrates Zero-Knowledge Proofs (ZKP) to ensure privacy-preserving verification and prevent leaderboard gaming, while offering interactive demos like the FinGPT Search Agent for side-by-side model comparisons.

Key findings highlight the leaderboard's role in identifying model strengths and weaknesses across diverse financial tasks, revealing issues such as hallucinations in financial reasoning and difficulties with complex XBRL parsing. The paper demonstrates that while models perform well on standard text tasks, they struggle with precise numerical reasoning and context identification in structured financial documents. Use cases include enhancing legal consultations, simplifying financial document analysis for the general public, and supporting regulatory compliance. Limitations include the current static nature of some underlying datasets and the challenge of evaluating multimodal capabilities fully. The work serves as a foundational resource for surveying the state of FinLLM evaluation, emphasizing the shift from static benchmarks to dynamic, community-driven assessment ecosystems.

## INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, stock prediction, sentiment analysis, crypto, equities, etfs, portfolio management, agentic workflow, backtesting, retrieval, 10-k filings, news, ohlc data, backtest, drawdown, portfolio returns, sharpe ratio, benchmark, dataset, framework
- Tag facets: {"asset_class": ["crypto", "equities", "etfs"], "data_source": ["10-k filings", "news", "ohlc data"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["backtest", "drawdown", "portfolio returns", "sharpe ratio"], "market_context": ["portfolio management"], "method": ["agentic workflow", "backtesting", "retrieval"], "risk_issue": ["overfitting"], "task": ["portfolio optimization", "stock prediction", "sentiment analysis"]}
- One-line summary: InvestorBench introduces a comprehensive benchmark and agent framework for evaluating LLM-based financial decision-making across stocks, cryptocurrencies, and ETFs, demonstrating that proprietary and large open-source models significantly outperform smaller or domain-specific models in sequential trading tasks.

### Detailed Summary

The paper addresses the lack of standardized benchmarks for evaluating LLM-based agents in diverse financial decision-making contexts. It introduces InvestorBench, a framework that extends the FINMEM architecture to support multi-asset trading (stocks, crypto, ETFs) using a layered memory system with varying decay rates to manage information sensitivity. The research positions this as a solution to the fragmentation of existing financial agent frameworks, which often focus on single asset classes or rely on proprietary data, thereby limiting comparative analysis.

The methodology involves constructing three distinct market environments using open-source data sources like Yahoo Finance, SEC EDGAR, and CoinMarketCap, supplemented by news sentiment data. The authors evaluate 13 different LLMs, ranging from small open-source models to large proprietary ones, as backbones for the agent. Experiments are conducted across single-asset trading tasks and a multi-asset portfolio management task, using metrics such as Cumulative Return, Sharpe Ratio, Annualized Volatility, and Maximum Drawdown. The experimental design includes a warm-up phase for memory initialization and a test phase for performance evaluation.

Key findings indicate that proprietary models (e.g., GPT-4, GPT-o1-preview) generally achieve superior risk-adjusted returns compared to open-source and domain-specific models, particularly in complex or volatile markets. Larger open-source models (e.g., Llama-3.1-70B, Qwen2.5-72B) outperform smaller counterparts, confirming that reasoning capability scales with parameter size. The study highlights that domain-specific fine-tuning does not guarantee better trading performance if the model lacks robust general reasoning. Limitations include the reliance on historical data which may not reflect future market dynamics and the potential for overfitting to specific market regimes, as evidenced by performance variations in bullish versus bearish conditions.

## Innovative Sentiment Analysis and Prediction of Stock Price Using FinBERT, GPT-4 and Logistic Regression: A Data-Driven Approach

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: stock prediction, sentiment analysis, equities, portfolio management, fine-tuning, prompt engineering, time-series modeling, news, accuracy, dataset, model, data leakage, emerging markets, nigerian stock exchange, computational efficiency, baseline comparison
- Tag facets: {"asset_class": ["equities"], "data_source": ["news"], "deliverable": ["dataset", "model"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["fine-tuning", "prompt engineering", "time-series modeling"], "risk_issue": ["data leakage"], "task": ["stock prediction", "sentiment analysis"]}
- One-line summary: This study compares FinBERT, GPT-4, and Logistic Regression for predicting the NGX All-Share Index using financial news, finding that optimized Logistic Regression outperforms both advanced LLMs in accuracy and efficiency.

### Detailed Summary

This paper addresses the challenge of leveraging financial news sentiment to predict stock market movements, specifically focusing on the Nigerian NGX All-Share Index. The authors position their work within the broader context of AI-driven financial forecasting, aiming to determine whether state-of-the-art large language models like FinBERT and GPT-4 offer superior predictive power compared to traditional, computationally efficient machine learning baselines. The research problem centers on the trade-off between model complexity, computational cost, and prediction accuracy in real-world trading scenarios, questioning the practical utility of resource-intensive transformers for simple binary classification tasks in emerging markets.

The methodology involves scraping 24,923 news headlines from Nigerian financial news sources (Nairametric and Proshare) spanning 2010 to 2024, aggregated into 3,573 temporal observations. The target variable is binary: Class 1 for daily share price gains and Class 0 for unchanged or fallen prices. The authors employ time-series cross-validation to prevent data leakage. FinBERT-base is fine-tuned using Optuna for hyperparameter optimization and mixed-precision training. GPT-4 is used via API with a predefined sentiment classification prompt. Logistic Regression utilizes TF-IDF vectorization, also optimized with Optuna. All models are evaluated on accuracy, precision, recall, F1 score, and ROC AUC.

Results indicate that Logistic Regression significantly outperforms both LLMs, achieving 81.83% accuracy and 89.76% ROC AUC. FinBERT achieved moderate performance (63.33% accuracy, 65.59% ROC AUC) despite its domain-specific training, while GPT-4 performed poorly (54.19% accuracy) using its predefined approach. The study concludes that for this specific task and dataset, the simplicity and interpretability of Logistic Regression, combined with effective feature engineering, provide a more robust and efficient solution than complex deep learning models. The authors suggest future work should explore hybrid models that combine the nuanced sentiment extraction of FinBERT with the predictive strength of traditional classifiers, noting that GPT-4 may require fine-tuning rather than zero-shot prompting for financial tasks.

## PreBit - A multimodal model with Twitter FinBERT embeddings for extreme price movement prediction of Bitcoin

- Year: 2022
- Category: Multimodal and Multilingual Finance
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, crypto, retail investing, multimodal modeling, backtesting, social media, ohlc data, backtest, accuracy, risk-adjusted returns, dataset, model, model risk, extreme price movement, finbert, sentiment analysis
- Tag facets: {"asset_class": ["crypto"], "data_source": ["social media", "ohlc data"], "deliverable": ["dataset", "model"], "evaluation": ["backtest", "accuracy", "risk-adjusted returns"], "market_context": ["retail investing"], "method": ["multimodal modeling", "backtesting"], "risk_issue": ["model risk"], "task": ["stock prediction"]}
- One-line summary: The paper proposes PreBit, a multimodal model combining FinBERT-embedded Twitter text with technical analysis data to predict extreme Bitcoin price movements, demonstrating that social media content improves prediction accuracy and enables a lower-risk trading strategy.

### Detailed Summary

This paper addresses the challenge of predicting extreme price fluctuations in Bitcoin, a highly volatile asset influenced by speculative retail trading and social media sentiment. The authors argue that existing models relying solely on sentiment scores or traditional technical indicators fail to capture the full informational content of social media discussions. The research aims to determine if embedding raw Twitter text using financial-domain language models provides superior predictive power for significant market movements compared to baseline methods.

The methodology introduces the PreBit dataset, comprising 9.4 million tweets from 2015 to 2021 alongside daily OHLCV data, correlated asset prices (Ethereum, Gold), and 13 technical indicators. The core model is a hybrid architecture: a Support Vector Machine processes the technical data, while a Convolutional Neural Network processes sentence-level FinBERT embeddings of concatenated daily tweets. These modalities are fused to classify next-day extreme price movements (defined as up/down 2% or 5%). The study includes an ablation analysis to isolate the contribution of social media data and backtests a trading strategy based on model predictions with varying confidence thresholds.

Results indicate that adding FinBERT-embedded Twitter data significantly improves prediction accuracy over models using only technical indicators. The ablation study confirms that social media content adds unique predictive value. Backtesting reveals that a trading strategy based on the multimodal model’s predictions achieves higher returns with reduced risk exposure compared to simple buy-and-hold or moving average strategies. The authors highlight that adjusting the prediction threshold allows traders to balance profitability against risk, offering a practical tool for managing downside risk in cryptocurrency markets.

## Can Large Language Models Trade? Testing Financial Theories with LLM Agents in Market Simulations

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Simulation and Execution Infrastructure
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: market simulation, strategy generation, equities, options, derivatives, market microstructure, portfolio management, agentic workflow, prompt engineering, tool use, limit order book, market impact, open source, simulator, model risk, experimental finance, systemic risk, emergent behavior, continuous double-auction
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["limit order book"], "deliverable": ["open source", "simulator"], "evaluation": ["market impact"], "market_context": ["market microstructure", "portfolio management"], "method": ["agentic workflow", "prompt engineering", "tool use"], "risk_issue": ["model risk"], "task": ["market simulation", "strategy generation"]}
- One-line summary: This paper introduces an open-source simulation framework where heterogeneous LLM agents act as trading participants in a realistic market with a persistent order book, demonstrating that LLMs can execute specific strategies, generate emergent market dynamics like bubbles, and serve as a tool for experimental finance.

### Detailed Summary

The paper addresses the gap in understanding how Large Language Models function as autonomous trading agents within complex financial environments. It positions LLMs not merely as forecasting tools but as active market participants whose behavior is driven by natural language instructions rather than explicit profit-maximization objectives. The research aims to test whether LLMs can adhere to trading strategies, how their interactions affect market stability, and whether they can replicate phenomena observed in human-subject experimental finance, such as bubbles and underreaction. This addresses a critical need for regulatory and academic insight into the potential systemic risks of widespread LLM adoption in trading.

The methodology involves an open-source framework implementing a continuous double-auction market with a persistent order book, supporting limit and market orders, partial fills, dividends, and equilibrium clearing. Heterogeneous LLM agents are defined via system prompts (e.g., value investor, market maker, momentum trader) and user prompts containing real-time market data, position info, and order book depth. Agents output structured JSON decisions using function calling, validated via Pydantic. The study compares LLM agents against deterministic rule-based benchmarks. Experiments vary agent compositions and market conditions to observe emergent behaviors, utilizing analysis techniques akin to partial dependence plots to interpret agent responses to market variables.

Key findings indicate that LLMs consistently adhere to their instructed strategies, such as mean reversion or liquidity provision, even when it leads to financial losses, highlighting a divergence from human profit-maximization. The simulation generates realistic market dynamics, including price discovery, speculative bubbles, and underreaction to information, depending on the agent mix. The framework enables the study of market stability and the impact of correlated LLM behaviors. Limitations include the abstraction of real-world latency and the reliance on prompt engineering for strategy definition, which may not fully capture the complexity of institutional trading systems. The work serves as a foundational tool for experimental finance and systemic risk analysis.

## QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, strategy generation, crypto, equities, commodities, high-frequency trading, multi-agent systems, tool use, multimodal modeling, ohlc data, backtest, risk-adjusted returns, hit ratio, framework, benchmark, dataset, technical analysis, interpretability, zero-shot
- Tag facets: {"asset_class": ["crypto", "equities", "commodities"], "data_source": ["ohlc data"], "deliverable": ["framework", "benchmark", "dataset"], "evaluation": ["backtest", "risk-adjusted returns", "hit ratio"], "market_context": ["high-frequency trading"], "method": ["multi-agent systems", "tool use", "multimodal modeling"], "risk_issue": [], "task": ["algorithmic trading", "strategy generation"]}
- One-line summary: QuantAgent introduces a multi-agent LLM framework for high-frequency trading that decomposes OHLC data analysis into specialized indicator, pattern, trend, and risk agents, achieving superior directional accuracy and risk-adjusted returns across diverse asset classes compared to traditional baselines.

### Detailed Summary

Existing LLM-based financial agents primarily rely on textual inputs like news or sentiment, which lag price discovery and are ill-suited for the low-latency, precision-critical demands of high-frequency trading (HFT). QuantAgent addresses this gap by operating exclusively on structured, short-horizon price signals derived from OHLC bars. The framework decomposes the trading process into four specialized agents: IndicatorAgent, which computes technical metrics like RSI and MACD; PatternAgent, which uses multimodal reasoning to identify chart formations; TrendAgent, which fits support and resistance channels to determine directional bias; and RiskAgent, which integrates these signals to define stop-loss and take-profit boundaries. This modular design allows for traceable, language-native rationales for each trade decision, bridging the interpretability of LLMs with the speed and structure required for algorithmic trading.

The system is evaluated on a multi-asset benchmark comprising nine financial instruments, including cryptocurrencies (Bitcoin), equity indices (S&P 500, Nasdaq), commodities (Crude Oil), and volatility indices (VIX). Experiments utilize 1-hour and 4-hour OHLC data, with 5,000 historical bars per asset, testing the model against random selection, linear regression, and XGBoost baselines. The evaluation focuses on directional accuracy over the next three candlesticks and risk-constrained rate-of-return metrics (Rcc, Rmax, Rmin) that simulate realistic execution with fixed stop-loss thresholds. The agents operate in a zero-shot setting without supervised fine-tuning, relying on structured prompts and tool-use capabilities to process market data and generate executable trade orders.

QuantAgent consistently outperforms all baselines across most assets, achieving up to 80% directional accuracy in rolling-window validations and significant improvements in risk-adjusted returns. Notably, it shows pronounced gains in equity markets like SPX and NQ, demonstrating robust generalization across different market regimes. However, the system faces limitations in ultra-short timeframes (1-15 minutes), where noise degrades prediction quality, and inference latency remains a barrier to true real-time deployment. The findings suggest that coupling structured price signals with multi-agent LLM reasoning offers a viable path for interpretable, high-frequency decision systems, though further optimization is needed for micro-second execution environments.

## AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, stock prediction, equities, us equities, agentic workflow, reinforcement learning, tool use, market prices, news, social media, financial statements, backtest, sharpe ratio, drawdown, portfolio returns, framework, open source, model, hallucination, overfitting
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "news", "social media", "financial statements"], "deliverable": ["framework", "open source", "model"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["us equities"], "method": ["agentic workflow", "reinforcement learning", "tool use"], "risk_issue": ["hallucination", "overfitting"], "task": ["algorithmic trading", "stock prediction"]}
- One-line summary: AlphaQuanter introduces a single-agent reinforcement learning framework that optimizes tool-augmented decision-making for stock trading, achieving state-of-the-art performance and higher faithfulness than multi-agent or prompt-only baselines.

### Detailed Summary

The paper addresses the limitations of existing LLM-based trading agents, which often suffer from inefficiency, inconsistent signals in multi-agent debate pipelines, and a lack of end-to-end optimization for coherent strategy learning. AlphaQuanter proposes a single-agent framework that uses reinforcement learning to learn a dynamic policy over a transparent, tool-augmented decision workflow. This allows the agent to autonomously orchestrate tools and proactively acquire information on demand, establishing a verifiable and traceable reasoning process that overcomes the black-box nature of traditional deep RL and the prompt-sensitivity of current LLM methods.

The method models the trading task as a tool-augmented Markov Decision Process where the agent selects between query actions (to gather market, fundamental, sentiment, and macro data) and decision actions (BUY, SELL, HOLD). Training employs a composite reward function combining outcome scores based on smoothed future returns and process scores that penalize inefficient tool use and format violations. Experiments are conducted on five large-cap U.S. stocks (GOOGL, MSFT, META, NVDA, TSLA) using a backtesting protocol over a six-month test period. The framework is evaluated against seven categories of baselines, including passive strategies, rule-based systems, deep RL, and various multi/single-agent LLM setups, using metrics like Annualized Rate of Return (ARR), Sharpe Ratio, and Maximum Drawdown.

Results show that AlphaQuanter, particularly the 7B variant, achieves state-of-the-art performance, significantly outperforming multi-agent frameworks and prompt-only single agents in ARR and risk-adjusted returns. The RL training enables the agent to learn sophisticated, expert-like heuristics, such as prioritizing technical indicators over low-frequency fundamentals, while maintaining high faithfulness in its decision traces. However, the framework is limited to single-asset decisions, relies on a predefined toolset without novel analysis generation, and faces context-length challenges due to accumulating tool outputs, highlighting the need for better memory mechanisms.


## When Agents Trade: Live Multi-Market Trading Arena for LLM Agents

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, stock prediction, equities, market microstructure, portfolio management, agentic workflow, backtesting, multimodal modeling, reinforcement learning, ohlc data, tables, backtest, sharpe ratio, portfolio returns, framework, simulator, trading agent, overfitting, multi-agent systems, visual reasoning
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "tables"], "deliverable": ["framework", "simulator", "trading agent"], "evaluation": ["backtest", "sharpe ratio", "portfolio returns"], "market_context": ["market microstructure", "portfolio management"], "method": ["agentic workflow", "backtesting", "multimodal modeling", "reinforcement learning"], "risk_issue": ["overfitting"], "task": ["algorithmic trading", "stock prediction"]}
- One-line summary: The paper introduces the Agent Trading Arena, a closed-loop multi-agent simulation where LLMs trade in a zero-sum environment, demonstrating that visual inputs and reflection modules significantly improve numerical reasoning and trading performance over textual data and static baselines.

### Detailed Summary

The paper addresses the limitation of static backtesting in financial LLM research by introducing the Agent Trading Arena, a virtual zero-sum stock market where LLM-based agents engage in competitive trading. Unlike traditional methods where agents cannot influence prices, this platform simulates real-time bid-ask interactions, allowing agents to directly impact price dynamics and experience market friction, liquidity constraints, and slippage. This closed-loop design bridges the gap between training and evaluation by forcing agents to adapt to shifting market conditions and opponent behaviors rather than relying on historical patterns.

The proposed method, ArenaTrader, integrates textual and visual modalities, using line charts and bar graphs alongside price data to enhance numerical reasoning. A reflection module is incorporated to enable iterative strategy refinement by evaluating past trades and contrasting successful with unsuccessful tactics. Experiments were conducted on NASDAQ and CSI datasets, comparing ArenaTrader against baselines like Buy & Hold, SMA, MACD, and deep learning models such as StockFormer and TimesNet. The evaluation focused on total return, Sharpe ratio, and win rate under varying volatility regimes.

Results indicate that LLMs struggle with numerical reasoning on plain-text data, often overfitting to local patterns, whereas visual inputs substantially improve performance. The ArenaTrader with GPT-4o achieved a Sharpe ratio of 0.348 on NASDAQ, outperforming the benchmark and all baselines. The reflection module further boosted returns, particularly with visual inputs. The study highlights that while LLMs show promise in dynamic environments, they remain sensitive to input modality and require mechanisms like reflection to handle complex, interactive financial scenarios effectively.

## ECC Analyzer: Extracting Trading Signal from Earnings Conference Calls using Large Language Model for Stock Volatility Prediction

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: stock prediction, forecasting, earnings analysis, equities, us equities, earnings season, multimodal modeling, time-series modeling, retrieval, earnings calls, ohlc data, backtest, ablation study, framework, dataset, overfitting, volatility prediction, multimodal fusion, hierarchical extraction
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls", "ohlc data"], "deliverable": ["framework", "dataset"], "evaluation": ["backtest", "ablation study"], "market_context": ["us equities", "earnings season"], "method": ["multimodal modeling", "time-series modeling", "retrieval"], "risk_issue": ["overfitting"], "task": ["stock prediction", "forecasting", "earnings analysis"]}
- One-line summary: The ECC Analyzer framework leverages LLMs to extract fine-grained textual and audio features from earnings conference calls, achieving a 27.7% reduction in MSE for short-term stock volatility prediction compared to state-of-the-art baselines.

### Detailed Summary

The paper addresses the challenge of forecasting stock volatility by extracting rich, predictive signals from unstructured earnings conference call (ECC) data. While prior multimodal approaches often treat text and audio as flat inputs, missing nuanced context, this work positions LLMs as essential tools for hierarchical information extraction. The core problem is to move beyond general sentiment analysis to capture specific, high-impact financial details that drive market reactions, thereby improving the accuracy of volatility forecasts for S&P 500 stocks.

The proposed ECC Analyzer framework employs a multi-stage pipeline. It extracts audio embeddings using Wav2Vec2 and text embeddings using SimCSE, processed through Multi-Head Self-Attention. Crucially, it implements a hierarchical extraction strategy: LLMs summarize ECC transcripts at paragraph and chunk levels, while a Retrieval-Augmented Generation (RAG) system uses a financial expert-designed 'Question Bank' to retrieve fine-grained focus sentences. These diverse features—raw audio, raw text, summaries, and RAG-extracted sentences—are fused via additive interactions and fed into a regression model. Experiments use the S&P 500 ECC dataset, comparing against GARCH, LSTM, and multimodal baselines like HTML and MRDM, evaluating performance using Mean Squared Error (MSE) across 3, 7, 15, and 30-day horizons.

Results show ECC Analyzer outperforms all baselines, particularly in short-term (3-day and 7-day) volatility prediction, reducing average MSE by 27.7% compared to the best existing model. Ablation studies confirm that fine-grained RAG-extracted sentences contribute most significantly to performance gains, whereas raw LLM direct prediction is ineffective. The study highlights that LLMs serve best as feature extractors rather than direct predictors. Limitations include reliance on specific financial questions for RAG and potential overfitting to short-term signals, with medium-term performance comparable but not superior to specialized baselines like AMA-LSTM.

## ATLAS: Adaptive Trading with LLM AgentS Through Dynamic Prompt Optimization and Multi-Agent Coordination

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, strategy generation, equities, portfolio management, market microstructure, agentic workflow, multi-agent systems, prompt engineering, backtesting, market prices, news, limit order book, sharpe ratio, drawdown, hit ratio, portfolio returns, framework, simulator, trading agent, overfitting
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "news", "limit order book"], "deliverable": ["framework", "simulator", "trading agent"], "evaluation": ["sharpe ratio", "drawdown", "hit ratio", "portfolio returns"], "market_context": ["portfolio management", "market microstructure"], "method": ["agentic workflow", "multi-agent systems", "prompt engineering", "backtesting"], "risk_issue": ["overfitting", "model risk"], "task": ["algorithmic trading", "strategy generation"]}
- One-line summary: ATLAS introduces a multi-agent trading framework with Adaptive-OPRO, a dynamic prompt optimization method that consistently outperforms static prompts and reflection-based feedback across diverse market regimes and LLM families.

### Detailed Summary

The paper addresses the challenge of deploying LLMs as autonomous trading agents in sequential, noisy environments where rewards are delayed and information is heterogeneous. It proposes ATLAS, a unified multi-agent framework that integrates market data, news, and fundamentals through specialized analyst agents, feeding a Central Trading Agent that emits executable orders. The core innovation is Adaptive-OPRO, a prompt optimization technique that dynamically updates the agent's static instructions using real-time, stochastic feedback over rolling windows, while keeping the execution interface stable to ensure edit locality and prevent overfitting to transient noise.

Experiments evaluate ATLAS across three market regimes (bearish-volatile, sideways, bullish) using seven LLM families (GPT, Claude, Llama, Qwen) and a custom StockSim environment. The study compares Adaptive-OPRO against fixed expert-engineered baselines and reflection-based feedback mechanisms. Metrics include ROI, Sharpe Ratio, Maximum Drawdown, Win Rate, and trade frequency. The design isolates the adaptation mechanism by running each configuration three times to account for LLM stochasticity, ensuring that performance gains are systematic rather than random. The evaluation covers both the decision policy and the prompt optimizer, testing cross-family transfer and model capacity effects.

Results show that Adaptive-OPRO consistently improves performance over static prompts, particularly in volatile regimes, with GPT-o3 and GPT-o4-mini achieving significant positive returns where baselines failed. In contrast, reflection-based feedback often deteriorates performance, suggesting it amplifies stochasticity in high-noise environments. The study finds that increased information availability does not uniformly improve performance, highlighting the importance of careful modality integration. Limitations include the abstraction of market microstructure (no slippage or latency) and the potential for over-optimization if the evaluation window is too short. The work demonstrates that systematic prompt evolution can yield interpretable, actionable trading constraints.

## From Earnings Calls to Investment Reports: Evaluating Role-based Multi-Agent LLM Systems

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: earnings analysis, investment advisory, equities, earnings season, multi-agent systems, tool use, agentic workflow, earnings calls, financial statements, accuracy, hit ratio, framework, dataset, hallucination, report generation, human evaluation, fact-checking
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls", "financial statements"], "deliverable": ["framework", "dataset"], "evaluation": ["accuracy", "hit ratio"], "market_context": ["earnings season"], "method": ["multi-agent systems", "tool use", "agentic workflow"], "risk_issue": ["hallucination"], "task": ["earnings analysis", "investment advisory"]}
- One-line summary: This paper introduces a role-based multi-agent LLM framework that generates investment reports from earnings call transcripts, achieving 58.1% decision accuracy and outperforming professional analyst reports in human evaluations by prioritizing logical structure and practical utility over surface-level quality.

### Detailed Summary

The paper addresses the challenge of automating complex financial analysis and investment report generation from unstructured earnings call transcripts, a task where single-agent LLMs often struggle with hallucinations and incomplete coverage. The authors propose a collaborative multi-agent system powered by GPT-4.1, orchestrated via Microsoft AutoGen, which mimics professional analyst teams through specialized roles: an Analyst for data extraction and fact-checking, a Writer for drafting, and an Editor for quality control. This role-based specialization aims to improve factual accuracy and interpretability by enforcing structured workflows and iterative feedback loops, addressing the limitations of monolithic generative models in high-stakes financial contexts.

The experimental setup utilizes the Earnings2Insights dataset, comprising 64 earnings call transcripts from the ECTSum and Professional subsets. The system integrates external tools, including Alpha Vantage for historical financial data and a sentiment analysis API for recent news, to ground its outputs in verifiable facts. Evaluation involved both automatic LLM-based judging and a large-scale human study with 176 participants on the Prolific platform, assessing metrics such as decision accuracy (Buy/Neutral/Sell predictions), persuasiveness, logic, and usefulness. The multi-agent system was compared against twelve other systems, including baseline single-agent approaches and professional analyst reports, to validate its competitive edge in generating actionable investment guidance.

Results indicate that the multi-agent system achieved the highest financial decision accuracy among automated approaches at 58.1%, with human evaluators rating it highly for logic (5.89/7) and persuasiveness (5.95/7). The system outperformed professional analyst reports in pairwise comparisons most of the time, demonstrating that structured collaboration yields more useful and reliable insights. However, the authors note limitations, including a performance ceiling around 60% accuracy and the system's inability to incorporate non-textual market signals or industry intuition. The findings suggest that while AI can augment human analysts by providing robust foundational analysis, it currently serves best as a tool for refinement rather than a replacement for human judgment in investment decision-making.

## To Trade or Not to Trade: An Agentic Approach to Estimating Market Risk Improves Trading Decisions

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: alpha mining, portfolio optimization, equities, portfolio management, agentic workflow, backtesting, reinforcement learning, time-series modeling, market prices, news, backtest, portfolio returns, risk-adjusted returns, sharpe ratio, framework, trading agent, model risk, overfitting, tail risk, stochastic differential equations
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "news"], "deliverable": ["framework", "trading agent"], "evaluation": ["backtest", "portfolio returns", "risk-adjusted returns", "sharpe ratio"], "market_context": ["portfolio management"], "method": ["agentic workflow", "backtesting", "reinforcement learning", "time-series modeling"], "risk_issue": ["model risk", "overfitting", "tail risk"], "task": ["alpha mining", "portfolio optimization"]}
- One-line summary: The paper develops an agentic framework where LLMs iteratively discover stochastic differential equations to estimate market risk, demonstrating that model-informed trading decisions significantly outperform standard sentiment-based LLM agents in both historical backtests and synthetic market simulations.

### Detailed Summary

The research addresses the gap in agentic finance frameworks that typically rely on sentiment or trend analysis by introducing a principled model-building step. The authors propose an agentic system where Large Language Models (LLMs) act as 'risk analysts' to iteratively discover Stochastic Differential Equations (SDEs) that best fit historical financial time series. This process uses a builder-critic loop, where builder agents implement and calibrate SDEs using gradient descent, and critic agents evaluate them based on statistical moments, tail metrics, and symbolic similarity. The discovered SDEs generate risk metrics such as Value-at-Risk (VaR), Conditional VaR (CVaR), and Maximum Drawdown (MDD), which are then passed to a 'trader agent' alongside news sentiment to make daily buy, sell, or hold decisions. This approach aims to enhance market risk estimation by combining LLM reasoning with rigorous mathematical modeling, moving beyond simple pattern recognition to explicit stochastic process discovery.

The experimental evaluation covers multiple equities, using historical price data to train and calibrate the SDE models. The system employs a monthly model discovery cycle, recalibrating the best-performing SDE daily using the most recent 100 trading days of data. Risk metrics are calculated via Monte Carlo simulations from the calibrated SDEs, supplemented by Extreme Value Theory (EVT) for tail risk estimation. The trading strategy is tested using traditional backtesting on historical data and an intelligent backtesting environment called Simudyne Horizon, which generates causally plausible synthetic price paths and news events to test robustness against out-of-distribution scenarios. The study compares the performance of the model-informed agent against baseline LLM agents that rely solely on news sentiment and technical indicators like the Relative Strength Index (RSI). The evaluation metrics include Sharpe ratios, trading returns, and the accuracy of risk metric estimation.

Results indicate that the model-informed trading strategies significantly outperform standard LLM-based agents, achieving higher Sharpe ratios across multiple equities. The integration of SDE-derived risk metrics provides a more robust foundation for trading decisions, particularly in identifying tail risks that sentiment analysis might miss. The use of synthetic data from Simudyne Horizon confirms that the improvements are not merely artifacts of training data bias but reflect genuine improvements in risk-aware decision-making. However, the study notes limitations, including the computational cost of the agentic loop and the potential for LLMs to struggle with out-of-distribution events that contradict their training data. The authors suggest that while the framework is promising, it currently requires human supervision for model validation and may benefit from more advanced memory structures to handle long-term dependencies in market dynamics.

## TradeTrap: Are LLM-based Trading Agents Truly Reliable and Faithful?

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: strategy generation, portfolio optimization, equities, us equities, backtesting, agentic workflow, ohlc data, news, backtest, drawdown, sharpe ratio, portfolio returns, framework, benchmark, open source, hallucination, model risk, data leakage, adversarial robustness, agent security
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "news"], "deliverable": ["framework", "benchmark", "open source"], "evaluation": ["backtest", "drawdown", "sharpe ratio", "portfolio returns"], "market_context": ["us equities"], "method": ["backtesting", "agentic workflow"], "risk_issue": ["hallucination", "model risk", "data leakage"], "task": ["strategy generation", "portfolio optimization"]}
- One-line summary: TradeTrap demonstrates that LLM-based trading agents are highly vulnerable to system-level perturbations, where small attacks on market intelligence, strategy, or state management can cause catastrophic portfolio drawdowns and unreliable behavior.

### Detailed Summary

This paper addresses the critical reliability gap in LLM-based autonomous trading agents, which are increasingly deployed in high-stakes financial environments but lack systematic robustness evaluation. The authors argue that while agent capability is well-studied, their faithfulness under adversarial or faulty conditions remains unexamined, posing significant risks in irreversible financial markets. The work positions itself as a stress-testing framework rather than a new agent architecture, focusing on the security and stability of existing adaptive and procedural agent designs.

The proposed TradeTrap framework decomposes trading agents into four core components: market intelligence, strategy formulation, portfolio/ledger handling, and trade execution. It introduces six targeted attack modules, including data fabrication, MCP tool hijacking, prompt injection, memory poisoning, and state tampering. Experiments are conducted in a closed-loop historical backtesting setting on US equity data (NASDAQ-100) with identical initial conditions. The study evaluates both Adaptive agents (e.g., AI-Trader) and Procedural agents (e.g., NoFX, ValueCell) using nine quantitative metrics such as Total Return, Maximum Drawdown, and Position Concentration to measure the propagation of localized perturbations through the decision loop.

Results show that small perturbations can induce extreme concentration, runaway exposure, and large drawdowns. Adaptive agents are highly sensitive to informational attacks (fake news, tool hijacking), leading to aggressive misallocation, while Procedural agents are more robust to noise but catastrophically fail when internal state is corrupted (memory poisoning, state tampering). For instance, state tampering caused a Procedural agent to suffer a -61% total return and -100% annualized return. The findings highlight a trade-off: adaptive agents capture more upside but are attackable via information channels, whereas procedural agents are structurally constrained but vulnerable to state corruption. The paper concludes that current agents lack system-level security and consistency checking.

## Design and Empirical Study of a Large Language Model-Based Multi-Agent Investment System for Chinese Public REITs

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: portfolio optimization, stock prediction, public reits, china market, agentic workflow, fine-tuning, reinforcement learning, backtesting, market prices, news, sec filings, backtest, sharpe ratio, drawdown, portfolio returns, open source, model, dataset, hallucination, model risk
- Tag facets: {"asset_class": ["public reits"], "data_source": ["market prices", "news", "sec filings"], "deliverable": ["open source", "model", "dataset"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["china market"], "method": ["agentic workflow", "fine-tuning", "reinforcement learning", "backtesting"], "risk_issue": ["hallucination", "model risk"], "task": ["portfolio optimization", "stock prediction"]}
- One-line summary: This paper proposes a multi-agent LLM framework for Chinese Public REITs that decomposes analysis into four specialized agents and compares a general-purpose LLM (DeepSeek-R1) against a fine-tuned small model (Qwen3-8B), finding both significantly outperform buy-and-hold with superior risk-adjusted returns.

### Detailed Summary

The study addresses the challenge of automating investment decisions in the low-volatility Chinese Public Real Estate Investment Trusts (REITs) market, where traditional single-model approaches often struggle with multi-source information integration and risk control. The authors propose a closed-loop multi-agent system that decomposes the trading process into analysis, prediction, decision, and execution layers. The system employs four distinct analytical agents—announcement, event, price momentum, and market macro—to generate structured insights from diverse data sources. These insights are fused by a prediction agent to output directional probability distributions across multiple time horizons (T+1, T+5, T+20), which are then translated into discrete position adjustment signals by a decision agent constrained by risk limits. This architecture aims to enhance reasoning quality, reduce hallucination risks, and provide auditable, executable decision logic amidst market noise.

The experimental design involves a 12-month backtest from October 2024 to October 2025 on 28 Chinese Public REITs listed for over one year. The core comparison evaluates two pathways for the prediction agent: using the general-purpose reasoning model DeepSeek-R1 versus a specialized small model, Qwen3-8B, fine-tuned via supervised fine-tuning (SFT) and Group Sequence Policy Optimization (GSPO) reinforcement learning. The fine-tuning process utilizes teacher-model distillation to create structured reasoning data and aligns the model with real price movements using a dynamic volatility threshold to define 'up', 'down', and 'sideways' labels. The system incorporates technical indicators, historical announcement impacts, event-driven news, and a four-quadrant macro allocation framework based on interest rates and equity market states. Performance is evaluated against a buy-and-hold benchmark using cumulative return, Sharpe ratio, and maximum drawdown metrics.

Results indicate that both agent-based strategies significantly outperform the buy-and-hold benchmark in cumulative return, Sharpe ratio, and maximum drawdown control. The DeepSeek-R1 pathway achieved a mean cumulative return of 15.50% with a Sharpe ratio of 1.71, while the fine-tuned Qwen3-8B pathway achieved 13.75% return with a slightly higher Sharpe ratio of 1.77. Both strategies maintained maximum drawdowns under -5%, compared to over -11% for the benchmark. The fine-tuned small model demonstrated competitive performance, suggesting that domain-specific alignment can match or exceed general-purpose models in stability. However, the system showed limitations in capturing rapid trend accelerations and experienced synchronous drawdowns during market corrections, indicating room for improvement in high-volatility adaptability and decision agent proactiveness.

## Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, strategy generation, equity research, equities, portfolio management, multi-agent systems, fine-tuning, backtesting, ohlc data, financial statements, sharpe ratio, risk-adjusted returns, backtest, framework, open source, trading agent, look-ahead bias, japan market, toxic index, interpretability
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "financial statements"], "deliverable": ["framework", "open source", "trading agent"], "evaluation": ["sharpe ratio", "risk-adjusted returns", "backtest"], "market_context": ["portfolio management"], "method": ["multi-agent systems", "fine-tuning", "backtesting"], "risk_issue": ["look-ahead bias"], "task": ["portfolio optimization", "strategy generation", "equity research"]}
- One-line summary: This paper demonstrates that decomposing investment analysis into fine-grained, expert-defined tasks within a hierarchical multi-agent LLM system significantly improves risk-adjusted returns and interpretability compared to coarse-grained baselines in Japanese equity backtesting.

### Detailed Summary

The paper addresses the performance degradation and lack of interpretability in existing multi-agent LLM trading systems, which often rely on abstract, coarse-grained instructions that fail to mimic real-world analyst workflows. The authors propose a hierarchical framework that explicitly decomposes investment analysis into fine-grained tasks, assigning specific, concrete analytical protocols to specialized agents rather than vague high-level objectives. This approach aims to enhance both the operational performance and the transparency of decision-making processes in automated trading environments.

The methodology employs a seven-agent system evaluated on the TOPIX 100 from September 2023 to November 2025, using a leakage-controlled backtesting setting with GPT-4o. The architecture includes four Level-1 analyst agents (Technical, Quantitative, Qualitative, and News) that generate scores and rationales, a Level-2 Sector Agent for relative valuation, a Macro Agent for economic regime assessment, and a Level-3 Portfolio Manager for final long-short construction. The study compares fine-grained prompts, which provide pre-calculated indicators and structured metrics, against coarse-grained prompts that feed raw data, while also conducting ablation studies to isolate agent contributions.

Results indicate that fine-grained task decomposition significantly improves Sharpe ratios across most portfolio sizes, with the Technical Agent playing a critical role in driving this advantage. Text analysis reveals that fine-grained prompts produce more specific, domain-relevant vocabulary and better semantic alignment between intermediate outputs and final decisions. Furthermore, combining the agent-generated signals with the market index via portfolio optimization yields superior risk-adjusted returns. However, the study notes that removing certain agents can sometimes improve performance, suggesting that fine-grained coordination is essential to prevent noise introduction from redundant or conflicting signals.

## ECC Analyzer: Extract Trading Signal from Earnings Conference Calls using Large Language Model for Stock Performance Prediction

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, forecasting, earnings analysis, equities, us equities, earnings season, multimodal modeling, time-series modeling, earnings calls, backtest, framework, model, overfitting, volatility prediction, feature extraction, audio-text fusion
- Tag facets: {"asset_class": ["equities"], "data_source": ["earnings calls"], "deliverable": ["framework", "model"], "evaluation": ["backtest"], "market_context": ["us equities", "earnings season"], "method": ["multimodal modeling", "time-series modeling"], "risk_issue": ["overfitting"], "task": ["stock prediction", "forecasting", "earnings analysis"]}
- One-line summary: The ECC Analyzer framework leverages LLMs to extract fine-grained textual and audio features from earnings conference calls, achieving a 27.7% reduction in Mean Squared Error for stock volatility prediction compared to state-of-the-art baselines.

### Detailed Summary

Predicting stock volatility using unstructured earnings conference call (ECC) data remains challenging due to the complexity of extracting nuanced signals from multimodal inputs. Existing multimodal models often treat text and audio equally, missing critical contextual details. This paper addresses the problem by proposing ECC Analyzer, a framework that integrates large language models to perform hierarchical information extraction. The goal is to distill richer, more predictive features from ECCs to enhance volatility forecasting accuracy, moving beyond simple feature concatenation to a deeper semantic understanding of executive communications and vocal cues.

The method employs a multimodal pipeline using Wav2vec2 for audio embeddings and SimCSE for text embeddings, processed through Multi-Head Self-Attention. Crucially, it uses LLMs for hierarchical summarization and Retrieval-Augmented Generation (RAG) guided by a financial expert-designed 'Question Bank' to extract fine-grained focus sentences. These features are fused via additive interactions and trained on a temporal split of the S&P 500 ECC dataset (2017) with 572 instances. Experiments compare against GARCH, LSTM, and SOTA multimodal models like HTML and AMA-LSTM, evaluating performance using Mean Squared Error (MSE) across 3, 7, 15, and 30-day volatility horizons.

Results show ECC Analyzer reduces average MSE by 27.7% compared to the best baseline, with significant improvements in short-term (3-day, 7-day) volatility prediction. The model outperforms direct LLM predictions, which proved ineffective, highlighting the necessity of structured feature extraction. Ablation studies confirm that fine-grained RAG-extracted sentences contribute most to performance gains. Limitations include the model's reliance on specific financial questions and potential overfitting to short-term signals, with medium-term performance comparable but not superior to specialized baselines like AMA-LSTM. The study underscores the value of LLMs as feature extractors rather than direct predictors in financial time-series tasks.

## TradingGroup: A Multi-Agent Trading System with Self-Reflection and Data-Synthesis

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, strategy generation, sentiment analysis, stock prediction, equities, portfolio management, multi-agent systems, agentic workflow, fine-tuning, chain of thought, retrieval, news, financial statements, ohlc data, backtest, sharpe ratio, drawdown, portfolio returns, framework, model
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "financial statements", "ohlc data"], "deliverable": ["framework", "model", "open source"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["portfolio management"], "method": ["multi-agent systems", "agentic workflow", "fine-tuning", "chain of thought", "retrieval"], "risk_issue": ["overfitting"], "task": ["algorithmic trading", "strategy generation", "sentiment analysis", "stock prediction"]}
- One-line summary: TradingGroup is a multi-agent quantitative trading system that integrates specialized agents for sentiment, fundamentals, and forecasting with self-reflection mechanisms and a dynamic risk management module, achieving superior backtesting performance over baselines and enabling effective parameter-efficient fine-tuning via an automated data-synthesis pipeline.

### Detailed Summary

The paper addresses the limitations of existing LLM-based trading agents, which often lack inter-agent coordination, structured self-reflection, and access to high-quality, domain-specific post-training data derived from actual trading activities. The authors propose TradingGroup, a multi-agent system designed to enhance decision-making quality and adaptability through a self-reflective architecture and an end-to-end data-synthesis pipeline. The system aims to distill past successes and failures to improve reasoning in analogous future scenarios and to generate instruction data for fine-tuning base LLMs.

TradingGroup consists of five specialized agents: News-Sentiment, Financial-Report, Stock-Forecasting, Style-Preference, and Trading-Decision. The News-Sentiment Agent uses an MCP client and reranking to filter and score news. The Financial-Report Agent employs hybrid retrieval (dense and sparse) to extract key indicators from filings. The Stock-Forecasting Agent integrates technical indicators with agent outputs and uses a hybrid gate to constrain predictions. The Style-Preference Agent dynamically selects trading styles based on self-reflection of past performance. A dynamic risk-management module adjusts stop-loss and take-profit thresholds based on volatility and style. The system also features an automated data-synthesis pipeline that logs agent inputs, outputs, and Chain-of-Thought trajectories, labeling them with reward signals for supervised fine-tuning.

Backtesting experiments on five stocks (AMZN, NFLX, TSLA, MSFT, COIN) from October 2022 to April 2023 demonstrate that TradingGroup outperforms rule-based, machine learning, reinforcement learning, and existing LLM-based baselines like FinMem and FinAgent. Notably, it achieved a 40.46% cumulative return on AMZN with lower drawdown. The paper also shows that fine-tuning Qwen3-8B with the synthesized data (Qwen3-Trader-8B-PEFT) significantly improves performance over the base model, surpassing GPT-4o-mini on some metrics. Limitations include the reliance on specific backtesting frameworks and the potential for overfitting to historical data patterns, though the authors note the importance of flexible risk configuration.

## Navigating Complexity: GPT-4's Performance in Predicting Earnings and Stock Returns in China's A-Share Market

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, earnings analysis, equities, a-share market, china market, prompt engineering, backtesting, financial statements, accuracy, sharpe ratio, portfolio returns, dataset, framework, bias, overfitting, emerging markets, overconfidence, generalization
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements"], "deliverable": ["dataset", "framework"], "evaluation": ["accuracy", "sharpe ratio", "portfolio returns"], "market_context": ["a-share market", "china market"], "method": ["prompt engineering", "backtesting"], "risk_issue": ["bias", "overfitting"], "task": ["stock prediction", "earnings analysis"]}
- One-line summary: This study evaluates GPT-4's ability to predict earnings direction and stock returns in China's A-share market using anonymized financial statements, revealing high confidence but low and inconsistent accuracy with no reliable correlation to actual returns.

### Detailed Summary

The paper addresses the challenge of applying large language models to financial analysis in emerging markets, specifically China's A-share market, which differs significantly from Western markets due to high retail investor participation, frequent policy interventions, and the prevalence of state-owned enterprises. The authors investigate whether GPT-4, trained primarily on English and Western data, can effectively analyze financial statements and predict earnings changes in this unique context, comparing its performance against human analysts and traditional benchmarks to assess generalizability and reliability.

The methodology involves extracting annual financial data from 2000 to 2023 for A-share listed companies from Wind and CSMAR databases, applying strict filtering criteria to ensure data quality. The financial statements are standardized, anonymized, and normalized by industry medians to remove identifiers and scale effects. GPT-4 is prompted to act as a professional analyst, performing trend analysis, ratio calculation, industry comparison, and policy sensitivity analysis to predict the direction of next-year earnings per share (EPS) and provide a confidence score. The study evaluates prediction accuracy, F1 score, confidence calibration, and the economic value of the predictions by constructing portfolios based on GPT-4's signals and calculating stock returns, Sharpe ratios, and alpha.

Results show that GPT-4's prediction accuracy fluctuates significantly between 10.62% and 48.67%, with an average F1 score of only 0.30, indicating poor classification performance. Despite low accuracy, the model maintains high confidence levels (75-90%), suggesting a significant overconfidence bias. Stock returns derived from GPT-4's predictions vary widely (-4.86% to 13.59%) and show no consistent correlation with prediction accuracy, implying that the model's insights do not translate into reliable alpha generation. The study concludes that while GPT-4 can perform structured financial analysis, it is not yet reliable for direct investment decisions in complex emerging markets, highlighting the need for hybrid models, improved calibration, and careful regulatory oversight.


## Signal or Noise in Multi-Agent LLM-based Stock Recommendations?

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, stock prediction, equities, us equities, portfolio management, multi-agent systems, backtesting, retrieval, news, financial statements, backtest, information ratio, portfolio returns, risk-adjusted returns, benchmark, framework, model, look-ahead bias, data leakage, multi-agent llm
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "financial statements"], "deliverable": ["benchmark", "framework", "model"], "evaluation": ["backtest", "information ratio", "portfolio returns", "risk-adjusted returns"], "market_context": ["us equities", "portfolio management"], "method": ["multi-agent systems", "backtesting", "retrieval"], "risk_issue": ["look-ahead bias", "data leakage"], "task": ["alpha mining", "stock prediction"]}
- One-line summary: The deployed MarketSenseAI multi-agent LLM system generates strong-buy recommendations that significantly outperform passive equal-weight benchmarks and random selection on the S&P 500, with performance driven by an adaptive synthesis of specialist agent signals rather than a single dominant factor.

### Detailed Summary

This paper addresses the critical gap in rigorous out-of-sample validation for multi-agent LLM equity systems, specifically testing whether the strong-buy recommendations from the deployed MarketSenseAI platform generate alpha beyond random stock selection. The research focuses on eliminating look-ahead bias by generating all signals live at each observation date, ensuring that the system's outputs are not influenced by future data or knowledge leakage from pre-training corpora. The study aims to quantify the economic value of these signals and decompose the internal reasoning process to understand the source of any observed edge.

The methodology employs a fixed-cohort design on S&P 500 (19 months) and S&P 100 (35 months) universes, using a Monte Carlo null distribution of 10,000 random same-sized portfolios to test selection skill. The system uses four specialist agents (News, Fundamentals, Dynamics, Macro) whose outputs are synthesized into a thesis and ordinal recommendation. To interpret the model, the authors apply Non-Negative Least Squares (NNLS) to decompose thesis embeddings into agent contributions, validating the results with cosine diagnostics and Information Coefficient (IC) analysis restricted to the actionable buy/strong-buy universe. This approach isolates the predictive content of the continuous agent weights from the discrete recommendation label.

Results show the S&P 500 strong-buy portfolio earns a +25.2% compound excess return over the equal-weight benchmark, ranking at the 99.7th percentile of the Monte Carlo null (p=0.003), with a statistically significant cross-sectional ICIR of +0.489. The S&P 100 cohort shows a similar directional excess (+30.5%) but lacks formal significance due to small position counts. NNLS attribution reveals an adaptive-integration mechanism where agent contributions rotate with market regimes: Fundamentals leads in the S&P 500, while Macro dominates in the S&P 100. The system exhibits downside protection, with strong-buy picks showing lower left-tail risk than hold signals. Limitations include the short time horizon, lack of sell-side implementation data, and the need for validation across more diverse market regimes and international universes.

## Document-Level Numerical Reasoning across Single and Multiple Tables in Financial Reports

- Year: 2026
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, earnings analysis, equities, institutional investing, multi-agent systems, retrieval, backtesting, sec filings, annual reports, tables, accuracy, benchmark, dataset, framework, hallucination, data leakage, document-level reasoning, cross-table reasoning, numerical qa, long-context
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "annual reports", "tables"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["multi-agent systems", "retrieval", "backtesting"], "risk_issue": ["hallucination", "data leakage"], "task": ["financial question answering", "earnings analysis"]}
- One-line summary: The paper introduces FinLongDocQA, a benchmark for cross-table numerical reasoning in long financial reports, and proposes FinLongDocAgent, a multi-agent RAG system that significantly improves LLM accuracy by iteratively retrieving evidence and verifying calculations.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models (LLMs) on document-level numerical reasoning within long, structured financial documents. While existing benchmarks focus on single-table or short-context settings, financial analysis often requires integrating scattered evidence across multiple tables and narrative text in annual reports exceeding 100k tokens. The authors identify two primary bottlenecks: context rot, where models fail to locate relevant tables in long inputs, and errors in multi-step numerical reasoning even when evidence is retrieved. This work positions itself as a necessary step toward reliable automated financial statement analysis by providing a rigorous benchmark and a method to mitigate these specific failure modes.

To address these challenges, the authors construct FinLongDocQA, a dataset comprising 7,527 question-answer pairs derived from 1,456 S&P 500 annual reports (2022-2024). The dataset is designed to require cross-table and cross-page reasoning, with evidence often spanning dozens of pages. The construction pipeline involves LLM-generated QA candidates, rule-based filtering to ensure multi-hop requirements and calculation correctness, and manual review for financial relevance. The authors also propose FinLongDocAgent, a multi-agent system built on AutoGen. It employs an Expansion Agent to formulate metric-aware queries, a Solving Agent to perform calculations with page-grounded citations, and an Evaluation Agent to verify completeness and trigger iterative retrieval rounds if operands are missing. Experiments evaluate closed-source and open-source LLMs against baselines like single-round RAG, GraphRAG, and agentic web search.

Experimental results demonstrate that standard long-context prompting and single-round RAG are insufficient for this task, with top models achieving only ~33% Exact Match. FinLongDocAgent significantly outperforms these baselines, raising Exact Match to 41.34% with Gemini-3-Flash. The ablation study highlights the critical role of the Evaluation Agent in reducing missing operand errors. Error analysis reveals that retrieval failures account for 62% of errors, followed by evidence utilization (19%) and calculation errors (8%). The paper concludes that iterative retrieval and verification are essential for reliable financial numerical QA. Limitations include the dataset's focus on S&P 500 firms and the computational overhead of multi-agent interactions. The work is highly relevant for surveys on financial document understanding, RAG architectures, and LLM reasoning capabilities in structured domains.

## MultiFinRAG: An Optimized Multimodal Retrieval-Augmented Generation Framework for Financial Question Answering

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: financial question answering, multimodal modeling, retrieval, 10-k filings, sec filings, tables, accuracy, benchmark, dataset, framework, open source, hallucination
- Tag facets: {"asset_class": [], "data_source": ["10-k filings", "sec filings", "tables"], "deliverable": ["benchmark", "dataset", "framework", "open source"], "evaluation": ["accuracy"], "market_context": [], "method": ["multimodal modeling", "retrieval"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: MultiFinRAG is a multimodal RAG framework that extracts structured data from financial PDFs and uses tiered retrieval to achieve 75.3% accuracy on complex QA tasks, outperforming ChatGPT-4o by 19 percentage points.

### Detailed Summary

The paper addresses the challenge of answering complex questions over long, multimodal financial documents like 10-Ks and 10-Qs, where traditional RAG pipelines fail due to token limits, layout loss, and fragmented cross-modal context. The authors propose MultiFinRAG, a system designed to preserve numerical and visual relationships by converting tables and figures into structured JSON and summaries using quantized open-source multimodal LLMs, while embedding narrative text for semantic search. This approach aims to enable precise retrieval and joint reasoning across text, tables, and images without relying on expensive proprietary models.

The methodology involves a three-stage pipeline: multimodal extraction, semantic chunking, and tiered retrieval. Tables and images are batch-processed by Gemma-3 or LLaMA-3.2-Vision to generate descriptions and JSON, which are embedded alongside text chunks using BAAI/bge-base-en-v1.5. The system employs semantic chunk merging to reduce redundancy and uses modality-aware similarity thresholds in a FAISS index. A tiered fallback strategy retrieves text first, escalating to table and image contexts only if initial retrieval is insufficient, thereby optimizing context size and cost. Evaluation is conducted on 300 manually crafted questions spanning text, image, table, and combined modalities, using manual verification for accuracy.

Results show MultiFinRAG with Gemma-3 achieves 75.3% accuracy on complex multimodal questions, surpassing ChatGPT-4o (free tier) by 19.3 percentage points and significantly outperforming baseline RAG systems. The framework reduces token usage by 40-60% and runs efficiently on commodity hardware. Limitations include reliance on manual evaluation, potential brittleness in OCR/layout parsing, and the current focus on single-document queries rather than cross-document or longitudinal analysis. The system is positioned as a cost-effective, open-source alternative for financial document understanding.

## Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, equities, institutional investing, fine-tuning, chain of thought, prompt engineering, sec filings, 10-k filings, tables, accuracy, ablation study, benchmark, dataset, framework, open source, hallucination, evidence curation, hierarchical retrieval, standardized documents, cost-efficiency
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "10-k filings", "tables"], "deliverable": ["benchmark", "dataset", "framework", "open source"], "evaluation": ["accuracy", "ablation study"], "market_context": ["institutional investing"], "method": ["fine-tuning", "chain of thought", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: The paper proposes HiREC, a hierarchical retrieval and evidence curation framework that improves open-domain financial question answering on standardized SEC filings by reducing near-duplicate confusion and iteratively filling information gaps, evaluated on the new LOFin benchmark.

### Detailed Summary

The paper addresses the challenge of applying Retrieval-Augmented Generation (RAG) to standardized financial documents like SEC filings, where repetitive boilerplate text and similar table structures cause traditional retrieval methods to misidentify near-duplicates, leading to irrelevant or redundant context. The authors propose the Hierarchical Retrieval with Evidence Curation (HiREC) framework to mitigate these issues. HiREC employs a two-stage retrieval process: first, it retrieves relevant documents using cover-page summaries to narrow the search space, and second, it selects specific passages within those documents. This hierarchical approach reduces confusion among similar texts. Additionally, an evidence curation module filters out irrelevant passages and generates complementary queries when initial evidence is insufficient, ensuring complete information for complex comparative questions.

To evaluate the framework, the authors construct LOFin, a large-scale open-domain financial question-answering benchmark comprising 145,897 SEC filings (10-K, 10-Q, 8-K) from S&P 500 companies and 1,595 question-answer pairs. The experimental design compares HiREC against state-of-the-art RAG baselines (e.g., Dense, IRCoT, Self-RAG) and commercial systems (Perplexity, SearchGPT). The method utilizes a fine-tuned DeBERTa-v3 cross-encoder for passage retrieval, an E5 bi-encoder for document retrieval, and GPT-4o for answer generation using Program-of-Thought or Chain-of-Thought prompting. Metrics include page-level recall/precision and answer accuracy across numeric and textual categories.

HiREC outperforms all baselines, achieving at least 13% higher answer accuracy and 10% higher page recall than the second-best model. It demonstrates superior cost-efficiency, using fewer tokens and lower API costs while maintaining high precision. The framework effectively handles multi-document and multi-hop reasoning, though it faces limitations in temporal aggregation across multiple years and complex numerical computations from tables. The approach also shows generalizability to legal document retrieval, indicating robustness beyond the financial domain.

## Evaluating Large Language Models (LLMs) in Financial NLP: A Comparative Study on Financial Report Analysis

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: equity research, benchmarking, equities, us equities, chain of thought, 10-k filings, sec filings, accuracy, benchmark, dataset, bias, model evaluation, human annotation, inter-rater reliability
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["chain of thought"], "risk_issue": ["bias"], "task": ["equity research", "benchmarking"]}
- One-line summary: This study evaluates five major LLMs on 10-K Business sections using human, automated, and behavioral metrics, finding no single model dominates and highlighting significant inter-rater disagreement in qualitative assessments.

### Detailed Summary

This paper addresses the critical need for reliable evaluation frameworks for Large Language Models (LLMs) in high-stakes financial contexts, specifically focusing on the analysis of complex regulatory disclosures. While LLMs are increasingly deployed for interpreting financial reports, their behavioral consistency, transparency, and reliability remain poorly understood. The authors position this work as a controlled comparative pilot study that moves beyond simple accuracy metrics to examine how different models handle nuanced, open-ended questions regarding corporate strategy, risk, and business models found in SEC filings. The study aims to provide a multi-dimensional assessment that captures not just output quality but also the stability and interpretability of model responses under standardized conditions.

The experimental design involves evaluating five transformer-based LLMs—GPT-4, Claude 4 Opus, Gemini Pro, Perplexity, and DeepSeek-V2—on the Item 1 (Business) sections of 10-K filings from the "Magnificent 7" tech companies over three years. The authors constructed a benchmark of 21 documents and 10 open-ended interpretative questions per document, resulting in 1,050 model responses. Evaluation was conducted through three complementary axes: human annotation by five experts assessing relevance, completeness, clarity, conciseness, and factual accuracy; automated metrics including ROUGE, Jaccard, and Sentence-BERT cosine similarity; and behavioral diagnostics measuring response stability and cross-prompt alignment. The study employed deterministic sampling where possible and controlled for context leakage by using fresh sessions for each query.

Results indicate that no single model consistently outperforms others across all evaluation perspectives. GPT-4 generally received higher human ratings for relevance and clarity, while other models showed strengths in specific areas like conciseness or lexical overlap. However, a key finding is the low inter-rater reliability among human annotators, with Krippendorff’s alpha values often near zero, suggesting that qualitative financial judgments are highly subjective. The study concludes that apparent performance differences should be viewed as relative tendencies rather than definitive indicators of general reliability. This highlights the necessity for evaluation frameworks that account for human disagreement and behavioral variability when deploying LLMs in financially consequential applications, cautioning against over-reliance on any single model for strategic analysis.

## A Scalable Data-Driven Framework for Systematic Analysis of SEC 10-K Filings Using Large Language Models

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: case study
- Summary coverage: full_extracted_text
- Tags: due diligence, equity research, equities, institutional investing, prompt engineering, retrieval, 10-k filings, sec filings, framework, dataset, bias, corporate health, longitudinal analysis, qualitative to quantitative, no-code application
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "sec filings"], "deliverable": ["framework", "dataset"], "evaluation": [], "market_context": ["institutional investing"], "method": ["prompt engineering", "retrieval"], "risk_issue": ["bias"], "task": ["due diligence", "equity research"]}
- One-line summary: The paper proposes a scalable framework using Cohere's Command-R+ LLM to extract, clean, and quantitatively rate SEC 10-K filings across confidence, environment, innovation, and people dimensions, enabling longitudinal and comparative corporate analysis.

### Detailed Summary

The paper addresses the challenge of efficiently monitoring and comparing the performance and strategic shifts of numerous publicly listed companies, a task traditionally hindered by the volume and narrative-heavy nature of SEC 10-K filings. It positions Large Language Models (LLMs) as a solution to transform qualitative disclosures into actionable, quantitative metrics, offering a cost-effective alternative to manual analysis for stakeholders like investors and analysts. The system aims to provide a scalable "litmus test" for corporate health, focusing on longitudinal trends and cross-company comparisons to mitigate biases inherent in static, single-year assessments.

The methodology involves an end-to-end pipeline: data collection from SEC EDGAR, automated cleaning using unstructured-io to extract narrative text and segment sections based on SEC structures, and LLM evaluation. The system uses Cohere’s Command-R+ with role-based zero-shot prompting to generate absolute ratings (0-2 scale) for four dimensions: confidence, environment, innovation, and people. It employs two grader versions (standard and strict) to reduce bias. Relative analysis compares excerpts from multiple companies using pairwise selection. The framework is implemented as a no-code web application for visualization and year-on-year comparison.

Results demonstrate the system's ability to generate uncorrelated ratings across dimensions and track strategic shifts over time for companies like Apple, IBM, and Royal Gold. The relative analysis identifies sector leaders in specific filing sections. Limitations include potential gaps in section extraction, inherent LLM biases reflecting training data, and the subjective nature of qualitative ratings. The paper contributes a reproducible pipeline and a user-friendly tool for systematic financial document analysis, though it does not directly link ratings to market performance or trading signals.

## EDINET-Bench: Evaluating LLMs on Complex Financial Tasks using Japanese Financial Statements

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: fraud detection, earnings analysis, benchmarking, equities, china market, retrieval, annual reports, financial statements, tables, accuracy, backtest, benchmark, dataset, open source, bias, data leakage, japan market, accounting fraud, multi-modal reasoning, expert-level tasks
- Tag facets: {"asset_class": ["equities"], "data_source": ["annual reports", "financial statements", "tables"], "deliverable": ["benchmark", "dataset", "open source"], "evaluation": ["accuracy", "backtest"], "market_context": ["china market"], "method": ["retrieval"], "risk_issue": ["bias", "data leakage"], "task": ["fraud detection", "earnings analysis", "benchmarking"]}
- One-line summary: EDINET-Bench evaluates LLMs on complex Japanese financial tasks like fraud detection and earnings forecasting, revealing that state-of-the-art models perform only marginally better than logistic regression, highlighting the need for richer reasoning scaffolding.

### Detailed Summary

This paper addresses the lack of expert-level financial benchmarks by introducing EDINET-Bench, an open-source dataset for evaluating Large Language Models on complex Japanese financial tasks. The benchmark focuses on three challenging classification problems: accounting fraud detection, earnings forecasting, and industry prediction. These tasks require models to process entire annual reports, integrating information across multiple tables and textual sections, demanding reasoning capabilities that are difficult even for human professionals. The study positions this work as a critical step toward benchmarks that reflect the high-stakes, multi-modal nature of real-world financial analysis, moving beyond simple knowledge retrieval or basic numerical QA.

The dataset is constructed from ten years of annual reports filed via Japan’s EDINET platform, comprising approximately 40,000 documents. The authors developed edinet2dataset to parse these reports into structured components including balance sheets, cash flow statements, profit and loss statements, and textual narratives. For fraud detection, they identified fraudulent cases by analyzing amendment reasons using LLMs and manual review, resulting in a balanced binary classification dataset. Earnings forecasting was created by predicting year-over-year profit changes, while industry prediction used a consolidated 16-category classification scheme. Experiments evaluated zero-shot performance of closed-source models (GPT-4o, Claude 3.5/3.7, GPT-5) and open-weight models (Llama 3.3, DeepSeek-V3/R1) against classical baselines like Logistic Regression and Random Forest, using ROC-AUC, MCC, and accuracy metrics.

Results indicate that even state-of-the-art LLMs struggle significantly, performing only marginally better than logistic regression in fraud detection and earnings forecasting. For instance, GPT-5 achieved a ROC-AUC of 0.65 in earnings forecasting, while Random Forest outperformed all LLMs in fraud detection. Incorporating textual information improved fraud detection but not earnings forecasting, suggesting different reliance on narrative signals. The study also assessed contamination risks, finding minimal impact through company name prediction tests. The authors conclude that simply providing reports is insufficient, advocating for benchmark frameworks with richer scaffolding, such as realistic simulations and task-specific reasoning support, to better emulate professional financial environments.

## Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, retrieval, prompt engineering, 10-k filings, sec filings, accuracy, framework, hallucination, financebench, ragchecker, contextual chunks, metadata-driven rag
- Tag facets: {"asset_class": [], "data_source": ["10-k filings", "sec filings"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["retrieval", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: This paper proposes a metadata-driven multi-stage RAG architecture that leverages LLM-generated metadata for pre-retrieval filtering, contextual chunk embedding, and custom reranking, achieving superior financial question-answering performance on FinanceBench compared to baseline and advanced RAG configurations.

### Detailed Summary

The paper addresses the challenge of Retrieval-Augmented Generation (RAG) in long, structured financial filings where relevant evidence is sparse and cross-referenced. Standard dense retrieval often fails to capture the hierarchical structure and implicit relationships within annual reports, leading to poor precision. The authors position their work as a systematic investigation into metadata-driven RAG, aiming to treat documents as hierarchical knowledge structures rather than flat collections of chunks. This approach seeks to improve the reliability and accuracy of financial question-answering systems by integrating multi-level metadata throughout the retrieval pipeline.

The methodology involves an offline indexing pipeline where LLMs generate document-level summaries, key entities, and thematic clusters, along with chunk-level enrichments such as parent references and potential question-answer pairs. The authors benchmark a spectrum of enhancements including pre-retrieval filtering, post-retrieval reranking, and enriched embeddings. They evaluate these techniques on the FinanceBench dataset, which contains 150 manually annotated question-answer-evidence triples from 10-K filings, using the RAGChecker framework for fine-grained evaluation of precision, recall, faithfulness, and hallucination. The experimental design compares naive RAG, hybrid retrieval, and various metadata-integrated architectures.

Results indicate that while powerful rerankers are essential for precision, the most significant performance gains come from embedding chunk metadata directly with text, creating "contextual chunks." The optimal architecture combines LLM-driven pre-retrieval optimizations (file filtering and query rewriting) with these contextual embeddings. The study also presents a custom metadata reranker that offers a cost-effective alternative to commercial solutions. Limitations include the reliance on a relatively small public subset of FinanceBench and the computational overhead of LLM-based metadata generation. The paper provides a blueprint for building robust, metadata-aware RAG systems for financial document analysis, highlighting the trade-off between peak performance and operational efficiency.

## Detecting Semantic Mismatches in XBRL Tag Mapping for SEC 10-K Filings: A Text Comparison and Historical Consistency Analysis

- Year: 2026
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: xbrl tagging, retrieval, sec filings, xbrl, framework, dataset, data leakage, data quality, semantic parsing, text comparison, tf-idf, bm25, historical consistency
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "xbrl"], "deliverable": ["framework", "dataset"], "evaluation": [], "market_context": [], "method": ["retrieval"], "risk_issue": ["data leakage"], "task": ["xbrl tagging"]}
- One-line summary: This study proposes a lightweight, tiered text comparison framework using TF-IDF, BM25, and historical consistency analysis to detect semantic mismatches in XBRL tag mappings for SEC 10-K filings, revealing persistent industry-specific tagging heterogeneity and offering practical validation checkpoints for disclosure workflows.

### Detailed Summary

The paper addresses the critical issue of semantic mismatches in XBRL tag mapping within SEC 10-K filings, which undermines the reliability of automated financial analysis. Despite the mandate for Inline XBRL, tag mapping accuracy remains a persistent challenge, with custom tag usage rates fluctuating between 16% and 23% across filer categories. The research positions itself at the intersection of financial data quality and NLP, aiming to provide a computationally efficient method for detecting errors that standard validation rules often miss, particularly those involving semantic nuances rather than structural violations.

The methodology employs a tiered text comparison approach combining lexical similarity scoring (TF-IDF and BM25) with domain-specific contextual features extracted from the SEC Financial Statement Data Sets (2014–2024). The system analyzes the alignment between reported line-item labels and assigned taxonomy elements, incorporating polarity, hierarchical, and measurement features. Additionally, it utilizes cross-period consistency analysis and SIC-code industry peer benchmarking to identify anomalous tag selection changes. The study leverages the XBRL US Data Quality Committee validation rules and SEC trend reports to establish baselines and detect deviations indicative of data quality degradation.

Findings reveal persistent heterogeneity in custom tag rates, with non-accelerated filers and complex industries like insurance and real estate showing higher error propensity. The analysis identifies three primary mismatch categories: qualifier, granularity, and concept boundary errors. The proposed lightweight verification methods are designed for integration into disclosure management workflows, offering pre-tagging, post-tagging, and pre-submission checkpoints. While effective for reducing computational overhead, the approach relies on taxonomy definition quality and requires sufficient peer data for benchmarking, limiting its utility for highly specialized industries with few filers.

## Optimizing Retrieval Strategies for Financial Question Answering Documents in Retrieval-Augmented Generation Systems

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, fine-tuning, prompt engineering, retrieval, 10-k filings, sec filings, ablation study, accuracy, framework, model, open source, hallucination, dpo training, embedding models, query expansion, markdown restructuring
- Tag facets: {"asset_class": [], "data_source": ["10-k filings", "sec filings"], "deliverable": ["framework", "model", "open source"], "evaluation": ["ablation study", "accuracy"], "market_context": [], "method": ["fine-tuning", "prompt engineering", "retrieval"], "risk_issue": ["hallucination"], "task": ["financial question answering"]}
- One-line summary: The paper introduces a three-phase RAG pipeline for financial question answering that combines query expansion, markdown restructuring, fine-tuned hybrid retrieval, and DPO-optimized generation, achieving significant NDCG@10 improvements across seven financial benchmarks.

### Detailed Summary

This paper addresses the challenge of retrieving accurate information from complex financial documents, such as 10-K reports, within Retrieval-Augmented Generation (RAG) systems. The authors argue that standard RAG pipelines fail to handle domain-specific vocabulary and multi-hierarchical tabular data effectively. They propose an end-to-end pipeline divided into pre-retrieval, retrieval, and post-retrieval phases to enhance the quality of retrieved context for Large Language Models (LLMs). The core problem is mitigating hallucinations and improving factual grounding in high-stakes financial applications where precision is critical.

The methodology involves three key stages. In pre-retrieval, the system employs LLM-based query expansion and corpus markdown restructuring to preserve document structure. For retrieval, the authors fine-tune embedding models (specifically Stella en 1.5B v5) using contrastive learning on financial data and implement a hybrid strategy combining dense embeddings and sparse BM25 retrieval, optimizing a weighting parameter alpha per dataset. Post-retrieval, a reranker refines the top-20 results, and a selection agent filters documents to reduce context noise. Finally, a DPO-trained GPT-4o mini model generates answers. Experiments are conducted on seven datasets (FinDER, FinQABench, FinanceBench, TATQA, FinQA, ConvFinQA, MultiHiertt) using NDCG@10 for retrieval and RAGAS metrics for generation.

Results show that fine-tuned hybrid retrieval significantly outperforms baseline models, with NDCG@10 scores improving from ~0.32 to ~0.51. Query expansion and markdown restructuring were identified as the most effective preprocessing techniques. The DPO-trained generation agent achieved higher answer relevance and context precision than standard GPT-4o. Limitations include the difficulty of handling streaming real-time data and potential security vulnerabilities. The work is highly relevant for finance LLM surveys focusing on RAG optimization, information retrieval, and financial question answering systems.

## HiFi-KPI: A Dataset for Hierarchical KPI Extraction from Earnings Filings

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: xbrl tagging, equities, us equities, fine-tuning, sec filings, xbrl, accuracy, dataset, benchmark, data leakage, structured extraction, encoder-based models, llm evaluation, date normalization, label sparsity
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "xbrl"], "deliverable": ["dataset", "benchmark"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["fine-tuning"], "risk_issue": ["data leakage"], "task": ["xbrl tagging"]}
- One-line summary: HiFi-KPI introduces a large-scale dataset of 1.65M iXBRL-tagged paragraphs with unified taxonomies and contextual metadata, demonstrating that encoder-based models excel at classification while LLMs struggle with structured extraction, particularly regarding date normalization.

### Detailed Summary

This paper addresses the challenge of extracting Key Performance Indicators (KPIs) from SEC filings by leveraging the complex, fine-grained structure of inline eXtensible Business Reporting Language (iXBRL). The authors argue that existing datasets lack the hierarchical context and cross-company transferability provided by iXBRL taxonomies. To solve this, they introduce HiFi-KPI, a corpus of 1.65M paragraphs and 4.5M entities derived from 10-K and 10-Q filings between 2017 and 2024. The dataset preserves critical contextual metadata, including time periods, currencies, and numeric values, alongside two unified taxonomies (Presentation and Calculation) created via a bottom-up aggregation algorithm to reduce label sparsity. A smaller, expert-curated subset, HiFi-KPI-Lite, is also provided for rapid evaluation of structured extraction tasks.

The authors evaluate three tasks: text classification, sequence labeling, and LLM-based structured extraction. For classification and labeling, they fine-tune encoder-based models like BERT and FLANG-BERT, testing performance across varying levels of taxonomy granularity. For structured extraction, they benchmark four large language models (Gemma-3-27B, Qwen3-30B-A3B, Mistral-Small-3.2-24B, and DeepSeek-V3.1) on HiFi-KPI-Lite, requiring the extraction of labels, dates, currencies, and values in JSON format. The experiments use macro-F1 scores for classification and exact match F1 for extraction, with a temporal split to prevent data leakage. The study highlights the difficulty of aligning LLM outputs with strict gold standards, particularly in normalizing numerical values and interpreting temporal phrases.

Results show that encoder-based models achieve high performance (macro-F1 > 0.906) on classification tasks, especially when using coarser taxonomy levels to mitigate sparsity. In contrast, LLMs perform significantly lower on structured extraction, with the best model (Qwen3) reaching only 0.440 F1. Qualitative analysis reveals that LLM errors primarily stem from date misinterpretation (e.g., confusing start and end dates) and value normalization issues. The paper concludes that while LLMs show promise, domain-specific fine-tuning and robust handling of iXBRL context remain critical. Limitations include potential biases toward large US companies and the strictness of the evaluation criteria, which may penalize semantically correct but syntactically different extractions.

## Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and Accounting Tasks

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, benchmarking, earnings analysis, prompt engineering, retrieval, earnings calls, news, financial statements, accuracy, benchmark, hallucination, bias, reproducibility, consistency, aggregation strategies, statistical robustness, g-hacking
- Tag facets: {"asset_class": [], "data_source": ["earnings calls", "news", "financial statements"], "deliverable": ["benchmark"], "evaluation": ["accuracy"], "market_context": [], "method": ["prompt engineering", "retrieval"], "risk_issue": ["hallucination", "bias"], "task": ["sentiment analysis", "stock prediction", "benchmarking", "earnings analysis"]}
- One-line summary: This study provides a comprehensive assessment of LLM consistency across five finance tasks, finding that while simple tasks are highly reproducible, complex tasks vary, yet aggregation strategies and downstream statistical robustness mitigate these inconsistencies.

### Detailed Summary

This paper addresses the critical methodological concern of reproducibility in Large Language Model (LLM) applications within finance and accounting research. As LLMs are increasingly used for text analysis, their inherent stochasticity raises questions about the reliability of research findings. The authors aim to establish baseline expectations for output consistency across common tasks, comparing different model versions and evaluating the impact of output variability on downstream statistical inference. This work fills a gap in the literature by systematically quantifying reproducibility rather than just performance accuracy.

The authors conduct an extensive empirical study using three OpenAI models (GPT-3.5-turbo, GPT-4o-mini, and GPT-4o) across five tasks: binary/multi-class classification, sentiment analysis, summarization, text generation, and prediction. They generate over 3.4 million outputs from 50 independent runs for each task, using diverse financial texts including MD&As, FOMC statements, news, and earnings calls. Consistency is measured using metrics like Fleiss’ Kappa, Cohen’s Kappa, and semantic similarity. The study also compares LLM consistency to human expert annotators, tests aggregation strategies (majority voting/averaging), and performs simulation analyses to assess the impact of output variation on regression results.

Findings reveal task-dependent consistency: binary classification and sentiment analysis achieve near-perfect reproducibility, while complex tasks like multi-class classification and numerical prediction show greater variability. Advanced models do not consistently outperform predecessors in consistency. LLMs significantly outperform human experts in consistency, maintaining high agreement even where humans disagree. Simple aggregation across 3-5 runs dramatically improves consistency and may improve accuracy. Crucially, simulation analysis shows that despite output variability, downstream statistical inferences remain robust, with negligible impact on regression coefficients and significance tests, suggesting low risk of "G-hacking" in typical finance applications.

## FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: xbrl tagging, benchmarking, retrieval, semantic parsing, xbrl, sec filings, hit ratio, accuracy, benchmark, dataset, hallucination, financial auditing, us-gaap, multi-document reasoning, numerical verification
- Tag facets: {"asset_class": [], "data_source": ["xbrl", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["hit ratio", "accuracy"], "market_context": [], "method": ["retrieval", "semantic parsing"], "risk_issue": ["hallucination"], "task": ["xbrl tagging", "benchmarking"]}
- One-line summary: FinAuditing introduces a taxonomy-structured benchmark using real XBRL filings to evaluate LLMs on semantic matching, relationship extraction, and mathematical reasoning, revealing significant gaps in cross-document consistency and numerical accuracy.

### Detailed Summary

Financial auditing requires detecting semantic, structural, and numerical inconsistencies across large-scale, structured disclosures like XBRL filings. Existing benchmarks often fail to capture cross-document dependencies and taxonomy-defined constraints. This paper addresses the need for a realistic evaluation of LLMs in professional-grade auditing by introducing FinAuditing, a benchmark built from real US-GAAP-compliant XBRL filings. It reframes auditing as a structured information reasoning problem, requiring models to align concepts, interpret hierarchical metadata, and maintain logical consistency across interdependent documents. The work highlights the limitations of current models in handling complex, regulation-driven financial information tasks that go beyond simple text processing.

The benchmark contains 1,102 annotated instances averaging over 33k tokens, derived from authoritative Data Quality Committee (DQC) error messages linked to SEC EDGAR filings. It defines three tasks: Financial Semantic Matching (FinSM) for concept alignment, Financial Relationship Extraction (FinRE) for structural consistency, and Financial Mathematical Reasoning (FinMR) for numerical verification. The authors evaluate 13 state-of-the-art LLMs, including GPT-4o, DeepSeek-V3, and financial-specific models like Fin-o1, using zero-shot settings. Evaluations employ metrics such as Hit Rate, Macro-F1, Accuracy, and fine-grained error rates (Structural, Extraction, Calculation) to assess performance on long-context, structure-aware reasoning.

Results reveal substantial gaps in LLM capabilities. FinSM performance is uniformly low, with top models achieving under 13% Hit Rate, indicating reliance on surface-level similarity rather than taxonomy-aware retrieval. FinRE shows GPT-4o leading with ~92% accuracy, but most open-source and financial models struggle, particularly with complex Combination Errors. FinMR is the most challenging, with the best model achieving only 13.86% accuracy; calculation errors dominate failures. The findings suggest that parameter scaling and domain pretraining are insufficient for structured auditing. The benchmark serves as an official contest benchmark, emphasizing the need for models with explicit structural grounding and multi-step reasoning capabilities for trustworthy financial intelligence.

## Decomposing Retrieval Failures in RAG for Long-Document Financial Question Answering

- Year: 2026
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, spreadsheet reasoning, earnings analysis, fine-tuning, retrieval, sec filings, earnings calls, tables, accuracy, model, hallucination, data leakage, retrieval failure analysis, page-level retrieval, financebench
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "earnings calls", "tables"], "deliverable": ["model"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "retrieval"], "risk_issue": ["hallucination", "data leakage"], "task": ["financial question answering", "spreadsheet reasoning", "earnings analysis"]}
- One-line summary: The paper introduces a domain-fine-tuned page scorer for financial RAG that significantly improves page and chunk retrieval accuracy by treating pages as intermediate retrieval units, closing the gap between document discovery and precise context localization.

### Detailed Summary

This paper addresses the critical failure mode in financial Retrieval-Augmented Generation (RAG) where the correct regulatory filing is retrieved, but the specific page or chunk containing the answer is missed. The authors argue that standard document-level metrics obscure within-document retrieval errors, which lead to hallucinations when generators extrapolate from incomplete context. They propose an oracle-based analysis to decompose retrieval performance into document, page, and chunk levels, providing empirical upper bounds on performance. The study focuses on Financial Question Answering (QA) over long SEC filings, highlighting the need for granular retrieval to support verifiable, high-stakes financial analysis.

The authors evaluate diverse retrieval strategies on a 150-question subset of FinanceBench, including dense, sparse, hybrid, hierarchical, and query reformulation methods. They introduce a novel domain-fine-tuned page scorer using a bi-encoder trained with contrastive learning on financial filings. This scorer ranks pages before chunk retrieval, filtering the search space to relevant sections. The experimental setup uses Qwen-2.5-7B-Instruct for generation and measures performance via document recall, page recall, and chunk-level BLEU/ROUGE-L scores. The page scorer is trained on document-level splits to prevent leakage and evaluated using 5-fold cross-validation.

Results show that while baseline methods achieve high document recall, page recall lags significantly, with the best baseline at 0.46 compared to an oracle document bound of 0.60. The proposed page scorer achieves 0.55 page recall, outperforming all baselines and improving chunk retrieval metrics. It particularly excels on metrics-generated questions, exceeding the oracle document bound. However, performance drops on earnings call transcripts due to structural differences. The study concludes that explicit page-level modeling improves within-document retrieval, though generalization to other document types and the need for gold annotations during training remain limitations.

## Fin-Rag A Rag System for Financial Documents

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: financial question answering, spreadsheet reasoning, multimodal modeling, retrieval, financial statements, tables, accuracy, framework, document processing, latency optimization, multimodal retrieval
- Tag facets: {"asset_class": [], "data_source": ["financial statements", "tables"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["multimodal modeling", "retrieval"], "risk_issue": [], "task": ["financial question answering", "spreadsheet reasoning"]}
- One-line summary: Fin-RAG is a multimodal Retrieval-Augmented Generation system for financial documents that combines GPT-4, BERT embeddings, and CoBERT re-ranking to achieve high accuracy in natural language querying of text and image-based financial reports.

### Detailed Summary

The paper addresses the challenge of efficiently retrieving and synthesizing information from complex, multimodal financial documents such as balance sheets, profit and loss statements, and scanned invoices. Traditional search methods are often slow and lack context, whereas Fin-RAG leverages Retrieval-Augmented Generation (RAG) to enable natural language querying. The system aims to improve decision-making efficiency in auditing, corporate finance, and strategic analysis by providing real-time, context-aware insights while maintaining compliance and scalability. It specifically targets the need for domain-specific understanding in financial terminology and the ability to process both textual and visual data formats seamlessly.

The proposed system utilizes a pipeline built on the LlamaIndex framework, integrating GPT-4 as the core language model for response generation and OpenAI’s multimodal capabilities for image analysis. For retrieval, the system employs BERT-base-uncased for embedding financial documents and queries, selecting it for its superior contextual match in financial language compared to other models like BGE or GTE. The retrieval process is enhanced by a re-ranking stage where CoBERT outperformed other models, achieving 100% accuracy in specific evaluation scenarios. The implementation includes enhanced metadata dictionaries to accelerate responses for frequent queries and uses vector databases for semantic search. The experimental design involved comparing multiple embedding and re-ranking models based on relevance scores, processing time, and accuracy.

Results indicate that Fin-RAG achieves a 92% accuracy rate with GPT-4 and an 87% retrieval precision using the BGE-large model combined with re-ranking. The system maintained an average response latency of 2.3 seconds per query, with metadata dictionaries reducing retrieval time by 35% for predefined questions. User feedback was positive, with 80% rating the experience as excellent. The system supports multimodal inputs, allowing for the extraction of data from charts and scanned reports. Limitations include the high computational cost of embedding and inference, potential latency issues in multi-step processes, and the need for domain-specific fine-tuning to further improve precision for niche financial queries. The paper suggests future enhancements involving RLHF and integration with real-time financial APIs.

## Automating Financial Statement Audits with Large Language Models

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: xbrl tagging, equities, institutional investing, retrieval, financial statements, sec filings, tables, accuracy, benchmark, dataset, hallucination, financial auditing, accounting standards, error detection, tabular reasoning
- Tag facets: {"asset_class": ["equities"], "data_source": ["financial statements", "sec filings", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["xbrl tagging"]}
- One-line summary: This paper introduces a benchmark and five-stage evaluation framework to assess LLMs' capabilities in automating financial statement audits, revealing that while models can detect errors, they struggle with accounting standard citations and table revisions.

### Detailed Summary

The paper addresses the inefficiency and error-proneness of manual financial statement auditing by proposing an automated auditing framework using Large Language Models. It identifies a critical gap in current workflows where human auditors may miss granular details, and existing AI tools fail at low-level cross-verification of transaction data against financial disclosures. The research aims to systematically evaluate LLMs' ability to verify financial tables, identify discrepancies, and ensure compliance with accounting standards, thereby laying the foundation for more accurate and efficient automated auditing systems.

The authors introduce the first benchmark for automatic financial statement auditing, combining real-world financial tables from S&P 500 companies with synthesized historical transaction data. The dataset includes 371 financial statements with injected errors such as missing rows, numerical errors, redundant rows, and misclassifications. A rigorous five-stage evaluation framework assesses LLMs on general judgment, error identification, error resolution, standards citation, and financial statement revision. Experiments were conducted using GPT-3.5-Turbo and GPT-4, evaluating their performance on single and multiple error scenarios using metrics like Exact Match, BertScore, and BLEU.

Results show that state-of-the-art LLMs effectively identify errors in financial statements when provided with historical transaction data, achieving perfect scores in general judgment. However, they demonstrate significant limitations in explaining detected errors, citing relevant accounting standards, and executing complete audits with necessary revisions. The models struggle with joint reasoning across tabular and textual data and lack domain-specific accounting knowledge. The paper highlights that current LLMs are insufficient as reliable auditors for complex, real-world scenarios and suggests future research should focus on enhancing domain-specific knowledge and hybrid reasoning capabilities.

## Evaluating Retrieval-Augmented Generation Models for Financial Report Question and Answering

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, equity research, equities, institutional investing, retrieval, sec filings, accuracy, benchmark, dataset, hallucination, banking sector, private investors, qualitative analysis
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["retrieval"], "risk_issue": ["hallucination"], "task": ["financial question answering", "equity research"]}
- One-line summary: This study evaluates Retrieval-Augmented Generation (RAG) systems for answering questions about bank financial reports, finding that high-quality embedding and generation models significantly improve context relevance and answer faithfulness, particularly for qualitative inquiries.

### Detailed Summary

The paper addresses the challenge of enabling private investors to accurately analyze half-yearly and quarterly bank financial reports using Large Language Models (LLMs). It identifies a gap in tailored RAG solutions for this specific use case, where manual analysis is labor-intensive and standard LLMs suffer from hallucinations and outdated knowledge. The research aims to enhance context relevance, answer faithfulness, and answer relevance by developing and evaluating a custom RAG system designed for financial report question-answering.

The authors employ a Design Science Research (DSR) methodology to build and test three distinct RAG model configurations using the Verba RAG application. The dataset consists of quarterly and half-yearly reports from five major European banks (Barclays, HSBC, Credit Suisse, Credit Agricole, and Banco Santander) for 2022 and 2023, along with irrelevant reports to test filtering. The system uses a 100-word chunk size with 50-token overlap, a hybrid WindowRetriever, and various embedding models (OpenAI ADA, MiniLM) and LLMs (GPT-4, Llama 3, Gemini 1.5 Pro). Evaluation is conducted manually on 10 questions per bank, covering both quantitative and qualitative aspects.

Results indicate that Model One (OpenAI ADA embeddings with GPT-4 generation) achieved the highest performance in accuracy and relevance, while Model Three (MiniLM embeddings with GPT-4) scored significantly lower, highlighting the critical importance of high-quality embedding models. The study finds that well-structured reports yield better RAG performance than less coherent ones. Additionally, qualitative questions received higher scores than quantitative ones, suggesting current RAG systems are more proficient in handling descriptive data than precise numerical extraction. Limitations include difficulties with complex PDF layouts and the need for domain-specific terminology repositories.

## Can LLMs be Good Financial Advisors?: An Initial Study in Personal Decision Making for Optimized Outcomes

- Year: 2023
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Wealth, Advisory, and Personal Investing
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: investment advisory, mutual funds, retail investing, prompt engineering, financial statements, accuracy, dataset, bias, hallucination, personal finance, mathematical reasoning, multilingual evaluation, advisory reliability
- Tag facets: {"asset_class": ["mutual funds"], "data_source": ["financial statements"], "deliverable": ["dataset"], "evaluation": ["accuracy"], "market_context": ["retail investing"], "method": ["prompt engineering"], "risk_issue": ["bias", "hallucination"], "task": ["investment advisory"]}
- One-line summary: This study evaluates ChatGPT and Bard on 13 personal finance queries involving credit cards, bank accounts, and certificates of deposit, revealing that while outputs are fluent, both models suffer from significant mathematical errors, perceptual mistakes, and a lack of personalized, accurate financial advice.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models as reliable personal financial advisors, specifically focusing on their ability to handle complex, multi-product decision-making scenarios. The authors argue that while LLMs show potential in revolutionizing public decision-making, their susceptibility to hallucinations and reasoning failures poses risks in domains like banking where accuracy is paramount. The study positions itself as an initial comparative analysis of two leading chatbots, ChatGPT and Bard, to identify specific failure modes in providing optimized financial outcomes for users managing interacting products like credit lines, dues, and interest rates.

The experimental design involves 13 structured queries covering four categories of product interactions: credit card only, credit card with bank account, credit card with certificate of deposit, and all three combined. The queries test constraints such as credit limits, billing cycles, cashback incentives, and APR penalties. The authors also included queries in African American Vernacular English (AAVE) and Telugu to assess dialect and language robustness. The models were evaluated based on accuracy, utilization of user information, personalization, bias, and error types including mathematical, perceptual, and grammatical mistakes, with results quantified by error percentages across the query set.

Findings indicate that while both models generate fluent text, they exhibit critical gaps in reliability. Bard often failed to use all provided information and gave biased recommendations, while ChatGPT struggled with AAVE and produced grammatical errors in Telugu. Both models frequently lacked personalized recommendations and committed mathematical errors, with Bard showing higher rates of perceptual errors and ChatGPT having more mathematical inaccuracies in specific calculations. The study concludes that current LLMs are not yet ready for trusted financial advisory roles due to these limitations, highlighting the need for integration with numeric solvers and better handling of diverse user inputs and complex constraints.


## Enhancing the Efficiency and Accuracy of Underlying Asset Reviews in Structured Finance: The Application of Multi-agent Framework

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: full_extracted_text
- Tags: due diligence, fraud detection, multi-agent systems, prompt engineering, retrieval, financial statements, accuracy, framework, open source, literature review, privacy, regulatory compliance, document extraction, synthetic data, cost analysis, audit automation
- Tag facets: {"asset_class": [], "data_source": ["financial statements"], "deliverable": ["framework", "open source", "literature review"], "evaluation": ["accuracy"], "market_context": [], "method": ["multi-agent systems", "prompt engineering", "retrieval"], "risk_issue": ["privacy", "regulatory compliance"], "task": ["due diligence", "fraud detection"]}
- One-line summary: This paper demonstrates that multi-agent LLM frameworks can effectively automate the cross-verification of underlying assets in structured finance, achieving near-perfect accuracy in matching loan applications to bank statements while offering a cost-effective alternative to manual auditing.

### Detailed Summary

The paper addresses the significant due diligence challenges in structured finance, specifically the manual and error-prone process of reviewing underlying assets for Asset-Backed Securities (ABS). It positions AI-driven automation as a solution to enhance efficiency and accuracy in verifying the completeness and compliance of financial documents, focusing on auto ABS as a primary use case. The research aims to bridge the gap in applying multi-agent LLM systems to audit consulting services by proposing a framework that automates document processing, information extraction, and error detection.

The methodology involves a multi-agent system where one agent generates synthetic bank and loan statement data, another extracts key information from PDFs, and a third evaluates the extraction accuracy against ground truth labels. The study compares the performance of closed-source models (GPT-4) against open-source models (LLAMA2, LLAMA3, DBRX) in a zero-shot setting. Experiments were conducted on 49 pairs of simulated bank and loan statements, measuring extraction accuracy for fields like names, balances, and addresses. The authors also analyzed the operational costs associated with each model to assess economic viability.

Results indicate that GPT-4 achieved 99% accuracy, while LLAMA3 reached 93-99% accuracy depending on the document type. Notably, a dual-agent system that cross-verifies information within the same document achieved 100% accuracy for both model types, albeit at higher computational costs. The paper highlights that while open-source models are significantly cheaper (e.g., $0.003 vs $0.05 per document), they require careful prompt engineering to handle unstructured data like multi-line addresses. The findings suggest that AI agents can streamline due diligence, reduce human error, and offer scalable solutions for financial document analysis, though regulatory and privacy compliance remains a critical consideration for deployment.

## Are Generative AI Agents Effective Personalized Financial Advisors?

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Wealth, Advisory, and Personal Investing
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: investment advisory, stock prediction, equities, retail investing, prompt engineering, sec filings, accuracy, dataset, framework, bias, user study, personality traits, preference elicitation, trust alignment, wealth management, human-in-the-loop
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings"], "deliverable": ["dataset", "framework"], "evaluation": ["accuracy"], "market_context": ["retail investing"], "method": ["prompt engineering"], "risk_issue": ["bias"], "task": ["investment advisory", "stock prediction"]}
- One-line summary: A user study of 64 participants reveals that while LLM-advisors can match human experts in eliciting investment preferences, they often fail to resolve conflicting needs, and users exhibit a dangerous insensitivity to advice quality, preferring extroverted personas that provide worse financial guidance.

### Detailed Summary

This paper investigates the effectiveness of Large Language Model (LLM) agents as personalized financial advisors, addressing three core challenges: eliciting user preferences in complex domains, providing personalized investment guidance, and leveraging advisor personality to build trust. The authors argue that unlike simple recommendation tasks, financial advisory requires handling high-stakes decisions where users may lack domain expertise or clarity about their own needs. The study aims to determine if LLMs can replicate the nuanced, trust-based relationship of human financial advisors.

The methodology involves a lab-based user study with 64 participants interacting with LLM-advisors (Llama-3.1 8B) across two stages. Stage 1 focuses on preference elicitation using a System-Ask-User-Respond paradigm, comparing LLM performance against a human financial expert. Stage 2 involves advisory discussions where participants evaluate stock suitability based on their elicited profiles. The study compares a non-personalized baseline against personalized variants and tests two distinct personality profiles (extroverted vs. conscientious) derived from the Big Five model. Evaluation metrics include elicitation accuracy, ranking correlation (Spearman’s Rho) against expert-curated ground truth, and user perception questionnaires.

Results indicate that LLMs match human experts in preference elicitation accuracy (approx. 0.78-0.89) but struggle with conflicting user statements. Personalization improves decision quality only when preference elicitation is accurate; otherwise, it directs users to unsuitable assets. Crucially, users were insensitive to advice quality, showing no significant difference in perceived usefulness between good and bad advice. More alarmingly, users reported higher trust and satisfaction with extroverted LLMs that provided statistically worse advice than conscientious ones, highlighting a misalignment between user perception and actual financial suitability.


## Can ChatGPT Plan Your Retirement?: Generative AI and Financial Advice

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Wealth, Advisory, and Personal Investing
- Evidence type: case study
- Summary coverage: first_50k_chars
- Tags: investment advisory, options, derivatives, retail investing, framework, regulatory compliance, hallucination, bias, wealth management, fiduciary duty, prompt injection
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": [], "deliverable": ["framework"], "evaluation": [], "market_context": ["retail investing"], "method": [], "risk_issue": ["regulatory compliance", "hallucination", "bias"], "task": ["investment advisory"]}
- One-line summary: This conceptual paper proposes a research agenda for deploying large language models in financial advice, identifying domain expertise, trustworthiness, and regulatory compliance as critical challenges that must be addressed before LLMs can safely replace or augment human financial advisors.

### Detailed Summary

The paper addresses the gap between the rapid advancement of general-purpose large language models and their safe, effective deployment in high-stakes, regulated domains like financial planning. The authors argue that while LLMs offer the potential to democratize access to financial advice, current models lack the necessary domain-specific expertise, ethical alignment, and regulatory adherence required for fiduciary duties. The research problem centers on defining the specific technical and governance hurdles that prevent LLMs from serving as trusted copilots for retirement planning, asset allocation, and tax optimization, rather than offering generic, potentially misleading information.

The methodology is conceptual and framework-based, drawing on the authors' prior work in adaptive markets and financial engineering. The paper analyzes the evolution of LLM technology (algorithms, data, compute) and contrasts it with the coevolution of finance and technology. It uses illustrative examples, such as prompt injection attacks and hallucinated citations, to demonstrate the opacity and unpredictability of current models. The authors propose a roadmap for developing finance-specific LLMs, emphasizing the need for specialized training data, ensemble models, and rigorous auditing mechanisms to ensure reliability and explainability.

Key findings include the identification of three core challenges: tailoring domain expertise to individual user situations, ensuring trustworthiness and ethical standards, and conforming to regulatory oversight. The paper concludes that scaling general models is insufficient; future progress requires specialization, curated financial datasets, and new chip architectures optimized for LLM workloads. Limitations include the current inability of LLMs to handle the heterogeneity of investor circumstances and the risk of hallucinations leading to significant financial losses. The paper serves as a call to action for interdisciplinary collaboration between computer scientists, financial researchers, and policymakers to develop safe and effective generative AI tools for wealth management.

## FinVault: Benchmarking Financial Agent Safety in Execution-Grounded Environments

- Year: 2026
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: fraud detection, regulatory reporting, equities, private markets, institutional investing, market microstructure, tool use, sec filings, limit order book, accuracy, benchmark, dataset, bias, hallucination, regulatory compliance, agent safety, prompt injection, jailbreaking, sandbox evaluation, adversarial robustness
- Tag facets: {"asset_class": ["equities", "private markets"], "data_source": ["sec filings", "limit order book"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing", "market microstructure"], "method": ["tool use"], "risk_issue": ["bias", "hallucination", "regulatory compliance"], "task": ["fraud detection", "regulatory reporting"]}
- One-line summary: FinVault introduces the first execution-grounded security benchmark for financial agents, revealing that state-of-the-art LLMs remain highly vulnerable to semantic and regulatory attacks in sandboxed environments with state-writable databases.

### Detailed Summary

The paper addresses the critical gap in evaluating the security of LLM-powered financial agents, which currently rely on abstract or content-level safety checks that fail to capture execution-grounded risks in real-world operational workflows. The authors argue that existing benchmarks overlook systemic risks arising from multi-step decision-making, tool invocation, and state-changing actions in highly regulated financial environments. To bridge this gap, they propose FinVault, a benchmark designed to evaluate agent robustness under adversarial conditions that approximate real-world execution, featuring isolated sandboxes with state-writable databases and explicit compliance constraints.

FinVault comprises 31 regulatory case-driven scenarios across credit, insurance, securities, and payments, containing 107 predefined vulnerabilities and 963 test cases. The dataset includes 856 attack samples covering prompt injection, jailbreaking, and financially adapted attacks, alongside 107 benign cases for false-positive evaluation. The experimental setup evaluates ten mainstream LLMs and three defense models using metrics like Attack Success Rate (ASR) and False Positive Rate (FPR). The methodology involves a three-stage attack generation pipeline of expert design, model augmentation, and human verification, ensuring real-world plausibility and regulatory relevance.

Results show that existing defenses are largely ineffective, with ASRs reaching 50.0% for vulnerable models and 6.7% for the most robust (Claude-Haiku-4.5). Semantic attacks like role-playing and instruction overriding are significantly more effective than technical attacks. The study highlights a trade-off in defense mechanisms, where higher detection rates come with unacceptable false positive rates that disrupt business continuity. Limitations include the exclusion of emerging attack strategies and the simplification of sandbox environments compared to production systems. The paper concludes that general-purpose safety alignment does not transfer well to financial contexts, necessitating financial-specific defenses.

## Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: spreadsheet reasoning, benchmarking, agentic workflow, tool use, multimodal modeling, tables, sec filings, accuracy, benchmark, dataset, hallucination, enterprise finance, accounting workflows, long-horizon tasks, llm-as-judge
- Tag facets: {"asset_class": [], "data_source": ["tables", "sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["agentic workflow", "tool use", "multimodal modeling"], "risk_issue": ["hallucination"], "task": ["spreadsheet reasoning", "benchmarking"]}
- One-line summary: Finch introduces FinWorkBench, a benchmark of 172 real-world enterprise finance and accounting workflows sourced from Enron and other institutions, revealing that even top AI agents like GPT-5.1 Pro pass only 38.4% of complex, long-horizon spreadsheet tasks.

### Detailed Summary

The paper addresses the gap in evaluating AI agents on realistic, messy enterprise finance and accounting workflows, which involve interleaved tasks like data entry, calculation, and reporting across heterogeneous artifacts. Unlike clean benchmarks, real-world work is long-horizon, knowledge-intensive, and multimodal, requiring agents to navigate complex spreadsheet structures, cross-file references, and implicit business logic. The authors argue that current benchmarks fail to capture the compositional complexity and structural messiness that characterize professional F&A work.

To address this, the authors construct FinWorkBench (Finch) using a novel pipeline that mines workflows from Enron email threads, versioned spreadsheet histories, and public financial reports. The dataset comprises 172 composite workflows with 384 tasks, involving 1,710 spreadsheets with 27 million cells, alongside PDFs and images. Evaluation employs both expert human judgment and an automated LLM-as-judge pipeline that uses structured diffs and screenshots to assess completeness, correctness, and over-edit avoidance. The study evaluates frontier models including GPT-5.1 Pro, Claude Opus/Sonnet 4.5, Gemini 3 Pro, Grok 4, and Qwen 3 Max.

Results show that even the strongest agents pass fewer than 50% of workflows, with GPT-5.1 Pro achieving only 38.4% under human evaluation despite spending an average of 16.8 minutes per workflow. Key failure modes include error accumulation in long-horizon tasks, difficulty with messy spreadsheet layouts, and struggles to reconstruct latent business logic in formulas. The paper highlights that multimodal artifacts and cross-file retrieval further degrade performance. Finch serves as a rigorous testbed for agentic workflows, revealing that current LLMs are not yet ready for autonomous enterprise finance operations without significant human oversight.

## Advancing Anomaly Detection: Non-Semantic Financial Data Encoding With Large Language Models

- Year: 2024
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: fraud detection, fine-tuning, time-series modeling, financial statements, accuracy, framework, bias, general ledger, anomaly detection, sentence-bert, feature encoding
- Tag facets: {"asset_class": [], "data_source": ["financial statements"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "time-series modeling"], "risk_issue": ["bias"], "task": ["fraud detection"]}
- One-line summary: The paper demonstrates that using Sentence-BERT embeddings to encode non-semantic categorical features in general ledger journal entries significantly improves anomaly detection performance compared to traditional one-hot encoding, particularly when paired with Logistic Regression and Neural Networks.

### Detailed Summary

This paper addresses the challenge of detecting anomalies in financial general ledger data, specifically focusing on the difficulties posed by feature heterogeneity and sparsity in non-semantic categorical attributes. Traditional machine learning approaches often struggle with the varying lengths and complexities of journal entries, leading to high-dimensional sparse vectors that are inefficient for classification. The authors propose a novel hybrid approach that leverages pre-trained Sentence-BERT (SBERT) large language models to encode these non-linguistic financial features into dense, fixed-size vector representations. This method aims to standardize feature variability and retain information more compactly than conventional vectorization techniques, thereby enhancing the input quality for downstream anomaly detection models.

The experimental design utilizes a real-world, anonymized general ledger dataset containing 32,100 transaction-level data points with 148 artificially inserted anomalies representing eight error types. The researchers tested three SBERT models (all-mpnet-base-v2, all-distilroberta-v1, and all-MiniLM-L6-v2) to generate embeddings for concatenated categorical transaction features. These embeddings were then fed into five optimized machine learning classifiers: Logistic Regression, Random Forest, XGBoost, Support Vector Machines, and Neural Networks. Performance was evaluated using macro recall average to handle class imbalance, with hyperparameters tuned via Bayesian optimization. The study also employed Principal Component Analysis to assess the dimensionality reduction efficiency and information retention of the LLM embeddings versus traditional one-hot encoding.

Results indicate that SBERT embeddings offer superior dimensionality reduction, requiring significantly fewer components to preserve variance compared to one-hot encoding. In downstream tasks, the LLM-enhanced models outperformed baselines in selected settings, with Logistic Regression and Neural Networks showing the most consistent improvements in anomaly detection accuracy. However, Random Forest and SVM models experienced performance declines when using LLM embeddings, highlighting the importance of model-embedding compatibility. The findings confirm that LLMs can effectively encode non-semantic financial data, tackling feature sparsity and enhancing audit reliability. Limitations include the synthetic nature of the anomalies, which may limit generalizability to real-world unlabeled fraud, and the linear constraints of PCA used for analysis.

## A Review on Large Language Models and Generative AI in Banking

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: credit scoring, fraud detection, investment advisory, regulatory reporting, options, derivatives, multi-agent systems, prompt engineering, taxonomy, literature review, bias, data leakage, hallucination, privacy, banking, systematic literature review, generative ai
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": [], "deliverable": ["taxonomy", "literature review"], "evaluation": [], "market_context": [], "method": ["multi-agent systems", "prompt engineering"], "risk_issue": ["bias", "data leakage", "hallucination", "privacy"], "task": ["credit scoring", "fraud detection", "investment advisory", "regulatory reporting"]}
- One-line summary: This structured literature review analyzes 14 recent studies to map the current state, application scenarios, and significant challenges of integrating Large Language Models and Generative AI into core banking operations, highlighting a gap between experimental potential and productive deployment due to regulatory and reliability constraints.

### Detailed Summary

This paper addresses the critical intersection of Generative AI and the banking sector, a domain characterized by high potential for efficiency gains but also by strict regulatory requirements and high stakes for accuracy. The authors conduct a Systematic Literature Review (SLR) to answer the research question regarding the current state of incorporating GenAI and LLMs in banking. The study aims to identify common study types, specific tasks where LLMs are explored, and the apparent challenges and concerns emerging from the scientific literature. It positions itself as a foundational overview in a rapidly evolving field, noting that while many papers offer general overviews, few provide structured, rigorous reviews of the domain's specific application landscape.

The methodology involves a rigorous SLR protocol across four major scientific databases: Scopus, IEEE Xplore, ACM Digital Library, and AIS Electronic Library. The search query combined terms for GenAI/LLMs with banking-related terms, restricted to titles, and filtered for peer-reviewed journal articles and conference papers in English, explicitly excluding preprints and papers focused on auxiliary activities like stock trading or document analysis. The final corpus comprises 14 papers published in 2023 and 2024. The analysis categorizes these papers by research type (overview vs. specific development), addressed area, tasks mentioned, challenges, models used, and prompting strategies. Key experiments reviewed include prompt engineering for credit risk reports, multi-agent architectures for digital banking assistants, LLM-based data augmentation for bankruptcy prediction, and fairness studies for financial advisement.

The findings reveal that most research is experimental, with no identified papers having deployed LLMs productively in core banking tasks at the time of writing. Common applications include customer service, credit risk analysis, fraud detection, and regulatory compliance. Significant challenges persist, including hallucinations, data privacy, biases, lack of transparency, and insufficient model quality for critical decisions. The review highlights that language-specific models often outperform general ones like ChatGPT in non-English contexts. A major limitation is the lack of standardized reporting in LLM projects, making reproducibility difficult. The paper concludes that while the potential is vast, the technology is in its infancy regarding banking integration, requiring further maturity and robust evaluation frameworks before widespread adoption.

## Evaluating LLMs in Finance Requires Explicit Bias Consideration

- Year: 2026
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, options, derivatives, backtesting, backtest, market impact, framework, open source, look-ahead bias, data leakage, overfitting, survivorship bias, narrative bias, cost bias, epistemic calibration
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": [], "deliverable": ["framework", "open source"], "evaluation": ["backtest", "market impact"], "market_context": [], "method": ["backtesting"], "risk_issue": ["look-ahead bias", "data leakage", "overfitting"], "task": ["benchmarking"]}
- One-line summary: This position paper identifies five critical biases in financial LLM evaluation—look-ahead, survivorship, narrative, objective, and cost—and proposes a Structural Validity Framework with a checklist to enforce rigorous, deployment-ready standards.

### Detailed Summary

The paper addresses the lack of rigorous evaluation standards in financial Large Language Models (LLMs), arguing that current practices often produce misleading results due to specific, compounding biases. The authors review 164 main conference papers from 2023 to 2025 and identify five recurring failure modes: look-ahead bias (using future information via weights or retrieval), survivorship bias (excluding delisted firms), narrative bias (generating coherent but unsupported stories), objective bias (optimizing for confidence over calibrated uncertainty), and cost bias (ignoring inference costs and latency). These biases create an illusion of validity, where strong empirical results conceal fundamental weaknesses in evaluation design, making reported performance useless for deployment claims. The authors highlight a significant gap between academic recognition of these issues and practical mitigation, noting that 74% of surveyed practitioners find evaluation tools scarce.

To address these issues, the authors propose a Structural Validity Framework comprising five components: Temporal Sanitation, Dynamic Universe Construction, Rationale Robustness, Epistemic Calibration, and Realistic Implementation Constraints. Each component targets one of the identified biases with specific, binary pass/fail requirements. For instance, Temporal Sanitation mandates point-in-time data access and strict knowledge cutoff enforcement, while Dynamic Universe Construction requires including delisted entities in backtests. The paper also presents a user study of 112 researchers and practitioners, revealing that 50% view the lack of standardized frameworks as the biggest bottleneck to bias mitigation. The authors provide an interactive dashboard and a detailed checklist template to help researchers audit their evaluations for these structural validity requirements.

The findings emphasize that generic language evaluation metrics are insufficient proxies for financial validity. The paper argues that without explicit attention to these biases, financial LLM systems risk deploying invalid strategies that fail in real-world conditions due to data leakage, survivor-conditioned overestimation, or unaccounted operational costs. The proposed framework aims to establish minimum requirements for interpreting backtests as evidence of deployable alpha. By enforcing structural validity, the field can move towards more credible and reproducible research. The paper concludes that bias mitigation is not just a reporting gap but a fundamental requirement for the safe and effective integration of LLMs into financial workflows, urging the community to adopt these standards before supporting any deployment claim.

## CN-Buzz2Portfolio: A Chinese-Market Dataset and Benchmark for LLM-Based Macro and Sector Asset Allocation from Daily Trending Financial News

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Portfolio, ETF, and Asset Allocation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, alpha mining, etfs, equities, china market, retail investing, agentic workflow, backtesting, retrieval, news, sharpe ratio, drawdown, portfolio returns, ablation study, benchmark, dataset, framework, hallucination, overfitting, narrative analysis
- Tag facets: {"asset_class": ["etfs", "equities"], "data_source": ["news"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["sharpe ratio", "drawdown", "portfolio returns", "ablation study"], "market_context": ["china market", "retail investing"], "method": ["agentic workflow", "backtesting", "retrieval"], "risk_issue": ["hallucination", "overfitting"], "task": ["portfolio optimization", "alpha mining"]}
- One-line summary: CN-Buzz2Portfolio introduces a rolling-horizon benchmark mapping Chinese daily trending news to macro and sector ETF allocation, revealing that LLMs generate significant alpha in sector rotation but struggle in sideways markets due to regime-dependent efficacy and narrative hallucination.

### Detailed Summary

The paper addresses the evaluation gap in financial LLM agents, arguing that existing benchmarks are either irreproducible live trading systems or entity-centric static tests that ignore public attention dynamics. It introduces CN-Buzz2Portfolio, a reproducible benchmark for the Chinese market that maps daily trending news to macro and sector asset allocation, aiming to isolate reasoning logic from stochastic market noise. The authors posit that current paradigms fail to test the 'narrative sifting' process required in real-world trading, where investors must identify relevant sectors from unstructured trending topics rather than pre-filtered entity news.

The methodology employs a Tri-Stage CPA Agent Workflow comprising Compression (filtering noise), Perception (analyzing narrative impact on sectors), and Allocation (generating rebalancing commands). The dataset aggregates daily top-20 trending topics from four major Chinese financial platforms from 2024 to mid-2025, simulating a realistic public attention stream. Experiments evaluate nine LLMs across two tasks: macro allocation using 11 broad indices and sector rotation using 14 sector-specific ETFs. The simulation assumes a retail investor environment with 100,000 RMB initial capital, daily rebalancing at close, and a 0.01% transaction cost, comparing performance against quantitative baselines like Momentum and Mean-Variance Optimization.

Results show that LLMs significantly outperform benchmarks in sector rotation during volatile regimes, generating structural alpha by identifying leading sectors. However, in low-volatility sideways markets, model performance collapses, often underperforming simple momentum strategies due to 'over-reacting to noise' and hallucinating narratives. The study highlights a 'capability trap' where larger models do not always outperform smaller ones in uncertain regimes. Limitations include the exclusion of short-selling, reliance on daily closing prices ignoring microstructure frictions, and the finding that LLMs are currently regime-dependent decision-makers rather than robust generalists.

## Benchmarking large language models for supply chain risk identification: an extended evaluation within the LARD-SC framework

- Year: 2025
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: risk extraction, sentiment analysis, equities, supply chain finance, prompt engineering, retrieval, news, accuracy, benchmark, dataset, framework, hallucination, bias, operational resilience, supply chain risk management
- Tag facets: {"asset_class": ["equities"], "data_source": ["news"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["accuracy"], "market_context": ["supply chain finance"], "method": ["prompt engineering", "retrieval"], "risk_issue": ["hallucination", "bias"], "task": ["risk extraction", "sentiment analysis"]}
- One-line summary: This paper benchmarks five LLM variants within the LARD-SC framework for supply chain risk identification, demonstrating that GPT-4o variants achieve superior accuracy and lower false positive rates compared to earlier models when analyzing news about Apple's Tier 1 suppliers.

### Detailed Summary

The paper addresses the challenge of timely and accurate supply chain risk identification in complex global networks, where traditional expert-based methods struggle with the volume and unstructured nature of daily news. It positions Large Language Models (LLMs) as transformative tools for automating the detection and classification of emerging risks, extending the previously introduced LARD-SC service-oriented architecture. The research aims to provide empirical evidence on which LLMs best support proactive risk management by integrating advanced text analytics into operational resilience strategies.

The methodology involves an extended evaluation of the LARD-SC framework, specifically benchmarking GPT-3.5 Turbo, GPT-4o, GPT-4o Mini, Claude 3.5 Sonnet, and Claude 3.5 Haiku. The study utilizes a curated dataset of 120 real-world news articles concerning Apple’s Tier 1 suppliers. The LARD-SC framework employs a structured pipeline: Data Collection and Visualization for Risk Analysis (DCV-RA) gathers and preprocesses news; Large Language Model-based approach for Risk Identification (LLM-RI) extracts risk events, likelihood, and impact using specialized prompts; and Large Language Model-based approach for Risk Classification (LLM-RC) categorizes risks using the Cambridge Taxonomy of Business Risks. Performance is assessed via expert-reviewed metrics: Risk Validation Rate (RVR), Potential Risk Rate (PRR), and False Identification Rate (FIR), culminating in a Relative Performance Index (RPI).

Findings indicate that advanced GPT-4o variants deliver the most consistent and accurate risk identifications, achieving higher RVR and minimizing false positives compared to GPT-3.5 and Claude models. The study highlights the value of LLMs in capturing novel, emergent risks beyond pre-defined dictionaries and their scalability for automated monitoring. However, limitations include the potential for hallucinations, dependency on prompt engineering quality, and the need for human-in-the-loop validation. The paper concludes that while LLMs significantly enhance SCRM, successful deployment requires balancing technological sophistication with careful oversight and addressing ethical considerations like data privacy and bias.

## Event Identification for Supply Chain Risk Management Through News Analysis by Using Large Language Models

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: risk extraction, sentiment analysis, supply chain finance, retrieval, news, accuracy, framework, bias, event detection, unsupervised learning, supply chain risk
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["framework"], "evaluation": ["accuracy"], "market_context": ["supply chain finance"], "method": ["retrieval"], "risk_issue": ["bias"], "task": ["risk extraction", "sentiment analysis"]}
- One-line summary: The paper introduces LUEI, a lightweight unsupervised framework using LLMs and semantic similarity to identify supply chain risk contributing events in news without training data, achieving significantly higher accuracy than keyword-based or commercial alternatives.

### Detailed Summary

This paper addresses the challenge of proactive supply chain risk management by identifying Contributing Events (CEs) that precede major disruptions. Traditional event extraction methods require extensive annotated training data, which is impractical for rare or novel risks. The authors propose the LUEI framework, part of the broader CERIA system, to autonomously detect CEs in real-time news feeds. The core problem is determining CE occurrences without prior labeled examples, leveraging the semantic understanding of Large Language Models to bridge the gap between event names and diverse news terminology.

The LUEI framework operates in three stages: Seed Collection, News Crawling, and Event Detection. First, it generates 'seed phrases' for a CE by combining WordNet synonyms with semantic pruning using SBERT embeddings to filter irrelevant terms. It then expands this set by analyzing three years of historical news via KeyBERT. Second, it crawls Google News using these seed phrases. Finally, the Event Detector module uses SBERT to compute cosine similarity between news articles and the CE name, labeling articles as relevant if the score exceeds a threshold (0.5). The system was evaluated on four specific CEs leading to delivery delays, such as 'Airport Staff Shortage' and 'Construction Workers Hold Strike'.

Experimental results demonstrate LUEI's superiority over single-keyword searches, WordNet-only expansions, and commercial tools like EventRegistry and Aylien. LUEI achieved an accuracy of 98.31% and an F1 score of 90.90% for 'Increase in COVID Cases', compared to 8.72% and 16.04% for single-keyword search, respectively. The framework effectively filters noise, returning highly relevant articles with minimal false positives. While the paper focuses on supply chain risk, the methodology offers a generalizable approach for unsupervised event detection in financial news, particularly for identifying precursor signals to market-moving events without relying on historical training data.

## FinBERT2: A Specialized Bidirectional Encoder for Bridging the Gap in Finance-Specific Deployment of Large Language Models

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, equity research, spreadsheet reasoning, equities, china market, fine-tuning, retrieval, domain adaptation, news, sec filings, tables, accuracy, model, benchmark, finbert2, chinese financial nlp, discriminative tasks, topic modeling, hybrid architecture
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "sec filings", "tables"], "deliverable": ["model", "benchmark"], "evaluation": ["accuracy"], "market_context": ["china market"], "method": ["fine-tuning", "retrieval", "domain adaptation"], "risk_issue": [], "task": ["sentiment analysis", "equity research", "spreadsheet reasoning"]}
- One-line summary: FinBERT2, a specialized Chinese financial bidirectional encoder pretrained on 32B tokens, outperforms leading LLMs in classification and retrieval tasks while enabling superior topic modeling, demonstrating that fine-tuned encoders remain superior to LLMs for discriminative and feature-extraction tasks in finance.

### Detailed Summary

The paper addresses the practical limitations of deploying large language models (LLMs) in finance, specifically their high computational cost, slower inference speeds, and suboptimal performance on discriminative tasks like sentiment analysis and named entity recognition compared to specialized encoders. It argues that while LLMs excel at generation, they are inefficient for real-time labeling and lack mature use cases for feature-based scenarios like topic modeling. The authors propose FinBERT2, a hybrid architecture strategy where FinBERT2 serves as a domain specialist to complement LLMs, bridging the gap in finance-specific deployment by offering a lightweight, customizable, and cost-effective alternative for specialized NLP tasks.

FinBERT2 is pretrained on a curated 32B-token Chinese financial corpus, the largest of its kind for this parameter size, comprising analyst reports, company announcements, and news. The model employs a finance-customized tokenizer and is fine-tuned into three variants: Fin-Labelers for five classification tasks (industry, sentiment, NER), Fin-Retrievers for dense retrieval using contrastive learning on financial QA pairs, and Fin-TopicModel for unsupervised clustering. Experiments benchmark these against general BERTs, other FinBERTs, and leading LLMs (GPT-4, Claude, Qwen) on classification accuracy and retrieval metrics (Recall@k, nDCG) across custom financial benchmarks and general domains.

Results show Fin-Labelers outperform leading LLMs by 9.7%-12.3% on average across five financial classification tasks, while Fin-Retrievers surpass open-source and proprietary embedders by +6.8% and +4.2% respectively in financial retrieval. The Fin-TopicModel demonstrates superior clustering and topic representation for financial titles. The paper concludes that fine-tuned encoders are more efficient and accurate for discriminative and feature-extraction tasks, suggesting a hybrid deployment where FinBERT2 handles labeling, retrieval, and topic modeling, while LLMs focus on generative tasks, optimizing cost and performance in financial enterprises.


## Fine-Tuning and Explaining FinBERT for Sector-Specific Financial News: A Reproducible Workflow

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Portfolio, ETF, and Asset Allocation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, etfs, equities, us equities, portfolio management, fine-tuning, backtesting, news, sharpe ratio, backtest, transaction costs, dataset, open source, framework, hallucination, explainable ai, faithfulness audit, reactive signal, long-short strategy
- Tag facets: {"asset_class": ["etfs", "equities"], "data_source": ["news"], "deliverable": ["dataset", "open source", "framework"], "evaluation": ["sharpe ratio", "backtest", "transaction costs"], "market_context": ["us equities", "portfolio management"], "method": ["fine-tuning", "backtesting"], "risk_issue": ["hallucination"], "task": ["sentiment analysis"]}
- One-line summary: The paper presents a reproducible workflow for fine-tuning FinBERT on a new 1,500-headline gold-standard dataset, demonstrating that while the resulting sentiment signal is reactive rather than predictive of returns, it supports profitable sector-specific long-short strategies with high Sharpe ratios.

### Detailed Summary

This study addresses the opacity of financial sentiment models by introducing a fully reproducible, open-source workflow for building, explaining, and evaluating sector-specific sentiment classifiers. The authors argue that transparency and trust are critical for high-stakes financial applications, necessitating models that are not only accurate but also auditable. They construct a new manually annotated gold-standard corpus of 1,500 U.S. sector-tagged financial headlines mapped to GICS sectors and investable ETFs, filling a gap in domain-specific, high-quality training data. The workflow integrates model training, faithfulness auditing of explanations, and economic validation to ensure the pipeline is robust and aligned with market practice.

The methodology benchmarks several models, including lexicon-based tools (VADER, Loughran-McDonald), interpretable baselines (Logistic Regression, Explainable Boosting Machines), and transformer-based models (FinBERT). The core experiment involves fine-tuning FinBERT on the gold-standard dataset, achieving a macro F1 of 0.707, a significant improvement over the zero-shot baseline (0.555). The authors perform a rigorous faithfulness audit using Integrated Gradients, LIME, and attention rollout, evaluating them via deletion curves and Area Over the Perturbation Curve (AOPC). They find LIME to be the most faithful explainer. Additionally, they quantify the risks of weak supervision, showing that using VADER-generated labels leads to a 21% accuracy drop and divergent explanations compared to gold-label training.

Econometric tests reveal that the sentiment signal is reactive, not predictive, of next-day returns, as confirmed by Granger causality tests. However, the signal retains practical utility for sector rotation strategies. Backtesting simple long-short strategies on sector ETFs, adjusted for transaction costs, yields profitable results, with the Technology sector achieving a Sharpe ratio of 1.88. The paper concludes that while the signal does not predict future returns, it effectively captures market reactions, supporting its use in reactive trading strategies. The study emphasizes the importance of fine-tuning, faithfulness auditing, and economic validation in deploying LLMs for finance.

## SHIELD: LLM-Driven Schema Induction for Predictive Analytics in EV Battery Supply Chain Disruptions

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: forecasting, risk extraction, commodities, supply chain finance, fine-tuning, graph reasoning, knowledge graph, retrieval, news, accuracy, dataset, framework, hallucination, ev battery, critical minerals, geopolitical risk, graph convolutional networks
- Tag facets: {"asset_class": ["commodities"], "data_source": ["news"], "deliverable": ["dataset", "framework"], "evaluation": ["accuracy"], "market_context": ["supply chain finance"], "method": ["fine-tuning", "graph reasoning", "knowledge graph", "retrieval"], "risk_issue": ["hallucination"], "task": ["forecasting", "risk extraction"]}
- One-line summary: SHIELD integrates LLM-driven schema induction with GCN-based prediction to accurately forecast EV battery supply chain disruptions, outperforming baseline models and direct LLM prompting.

### Detailed Summary

The paper addresses the critical need for predictive analytics in the electric vehicle (EV) battery supply chain, where geographic and economic concentrations of critical minerals like lithium and cobalt create vulnerability to geopolitical and natural disruptions. Traditional rule-based or black-box ML methods often lack the interpretability and adaptability required for proactive risk management. SHIELD proposes a two-stage framework that combines Large Language Models (LLMs) with domain expertise to construct a hierarchical knowledge schema and predict disruptions from news sources. This approach aims to mitigate LLM hallucinations while providing actionable, interpretable insights for supply chain resilience.

The methodology involves two main stages: schema learning and disruption analysis. In schema learning, LLMs (GPT-4o, Llama3) extract hierarchical structures from 239 academic and industry sources, refined by human experts into a unified schema library. For disruption analysis, the system processes 12,070 news paragraphs using fine-tuned RoBERTa for event extraction, multi-dimensional similarity matching to link events to the schema, and Graph Convolutional Networks (GCNs) with logical constraints for prediction. The pipeline includes coreference resolution and logical consistency checks to ensure robustness. Experiments evaluate performance on a dataset spanning 2022-2023, comparing SHIELD against ablation versions and direct LLM prompting (GPT-4o).

SHIELD achieves an F-score of 0.732 in disruption prediction, significantly outperforming GPT-4o (0.624) and GCN-only baselines (0.685). The system successfully predicted real-world events, such as material shortages following the Inflation Reduction Act and lithium supply risks due to Australia-China tensions. Key contributions include an interactive schema curation system, a novel schema-news dataset, and a hybrid architecture that balances predictive accuracy with interpretability. Limitations include challenges in schema integration and the need for continuous expert feedback to maintain relevance as supply chain dynamics evolve.

## FinKario: Event-Enhanced Automated Construction of Financial Knowledge Graph

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: stock prediction, equity research, equities, a-share market, china market, knowledge graph, retrieval, prompt engineering, sec filings, tables, backtest, sharpe ratio, accuracy, dataset, framework, bias, knowledge graph rag, event-driven analysis, institutional strategies comparison
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "tables"], "deliverable": ["dataset", "framework"], "evaluation": ["backtest", "sharpe ratio", "accuracy"], "market_context": ["a-share market", "china market"], "method": ["knowledge graph", "retrieval", "prompt engineering"], "risk_issue": ["bias"], "task": ["stock prediction", "equity research"]}
- One-line summary: FinKario introduces an automated, event-enhanced financial knowledge graph and a two-stage graph-based RAG retrieval strategy that significantly outperforms financial LLMs and institutional strategies in stock trend prediction and backtesting accuracy.

### Detailed Summary

The paper addresses the challenge of integrating rapidly evolving market events and unstructured equity research reports into LLM-based financial analysis, where static knowledge bases and simple chunking fail to provide timely, context-aware insights. The authors propose FinKario, a dual-structured financial knowledge graph comprising an attribute subgraph for stable fundamentals and an event subgraph for time-sensitive drivers, constructed automatically via prompt-driven extraction guided by professional institutional templates like the CFA handbook and FIBO ontology. This approach overcomes the limitations of manual schema engineering and slow update cycles, enabling dynamic, real-time knowledge population from raw markdown reports.

The methodology includes a comprehensive pipeline for corpus acquisition, schema construction, knowledge population, and quality control refinement using Tushare data for attribute completion. To leverage this graph, the authors develop FinKario-RAG, a two-stage retrieval strategy that first identifies coarse-grained entities (stocks, dates) and then expands to fine-grained related entities and relationships to form a semantically coherent subgraph for reasoning. Experiments involve backtesting a long-only trading strategy on Chinese A-share stocks from August 2024 to March 2025, comparing FinKario-RAG against vanilla LLMs, financial domain LLMs, and real-world institutional brokerage strategies using metrics like Sharpe ratio, annualized return, and predictive accuracy.

Results demonstrate that FinKario-RAG achieves superior performance, outperforming financial LLMs by 18.81% and institutional strategies by 17.85% in predictive accuracy, with a Sharpe ratio improvement of 58.14% over the runner-up. Ablation studies confirm the critical role of the event graph and the two-stage retrieval mechanism, showing significant performance drops when either is removed. The system provides actionable, grounded investment guidance with textual rationales, addressing the lack of explainability in black-box models. Limitations include reliance on the quality of source reports and potential biases in institutional templates, while the scope is currently limited to the Chinese market and specific asset classes.

## Sentiment-driven prediction of financial returns: a Bayesian-enhanced FinBERT approach

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Portfolio, ETF, and Asset Allocation
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: stock prediction, alpha mining, etfs, portfolio management, fine-tuning, backtesting, time-series modeling, social media, ohlc data, backtest, accuracy, sharpe ratio, dataset, model, overfitting, sentiment analysis, feature selection, bayesian optimization, support vector machine, stocktwits
- Tag facets: {"asset_class": ["etfs"], "data_source": ["social media", "ohlc data"], "deliverable": ["dataset", "model"], "evaluation": ["backtest", "accuracy", "sharpe ratio"], "market_context": ["portfolio management"], "method": ["fine-tuning", "backtesting", "time-series modeling"], "risk_issue": ["overfitting"], "task": ["stock prediction", "alpha mining"]}
- One-line summary: The paper demonstrates that combining FinBERT-extracted sentiment features with Bayesian-optimized feature selection significantly improves SPY ETF return sign prediction and cumulative trading profits compared to existing benchmarks.

### Detailed Summary

Predicting financial asset returns is challenging due to market uncertainty and the need to effectively integrate textual sentiment data. This study addresses the problem of selecting optimal features from social media text to enhance return sign prediction models, specifically focusing on the SPY ETF. The authors argue that while sentiment is valuable, the sheer volume of data requires rigorous feature selection to avoid noise and overfitting, positioning their work as an improvement over previous literature that used larger, less curated feature sets.

The methodology employs FinBERT to classify 3.2 million StockTwits tweets into positive, negative, or neutral sentiments, computing a daily sentiment index. To select features, the authors implement Bayesian-optimized Recursive Feature Elimination (BO-RFE) using a Random Forest kernel, which iteratively identifies the most informative subset of features based on F1-score. They further enrich this set using correlation analysis, identifying that negative sentiment and its lagged values (7 days) capture slow, weekly seasonal dynamics. The final prediction model is a Support Vector Machine (SVM) with SMOTE and bagging, trained on a moving window of SPY price and volume data alongside the selected sentiment features.

Results show that the proposed BO-RFE-5 architecture (5 features) achieves an F1-score above 70% and 64.1% accuracy, outperforming the literature benchmark (F1 0.622). The optimal feature set is dominated by sentiment indicators (4 out of 5 features), highlighting their predictive power. Backtesting reveals that the BO-RFE-5 strategy generates significantly higher cumulative profits during volatile periods compared to the benchmark. A key advantage is the reduced training window requirement (210 days vs. 240 days), allowing for faster model adaptation. Limitations include the focus on a single ETF and the exclusion of transaction costs in the simulation.

## FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, portfolio optimization, stock prediction, equities, us equities, agentic workflow, fine-tuning, knowledge graph, reinforcement learning, news, backtest, portfolio returns, sharpe ratio, drawdown, benchmark, dataset, framework, model, hallucination, event ripple effect
- Tag facets: {"asset_class": ["equities"], "data_source": ["news"], "deliverable": ["benchmark", "dataset", "framework", "model"], "evaluation": ["backtest", "portfolio returns", "sharpe ratio", "drawdown"], "market_context": ["us equities"], "method": ["agentic workflow", "fine-tuning", "knowledge graph", "reinforcement learning"], "risk_issue": ["hallucination"], "task": ["alpha mining", "portfolio optimization", "stock prediction"]}
- One-line summary: FinRipple aligns LLMs with financial markets via time-varying knowledge graphs and CAPM-guided reinforcement learning to predict event ripple effects, significantly outperforming baselines in asset pricing and portfolio management.

### Detailed Summary

The paper addresses the limitation of existing event studies that fail to capture complex, cross-entity ripple effects in financial markets. It introduces FinRipple, a framework that integrates time-varying knowledge graphs (KGs) with large language models (LLMs) to model dynamic corporate relationships. The authors formalize ripple effect prediction as a standardized task, aiming to enhance LLM reasoning by grounding it in market structure and classical asset pricing theory. This approach overcomes the structural unawareness and hallucination issues common in direct LLM applications for finance.

The methodology involves three stages: constructing time-varying KGs from unstructured data (news, patents, supply chains), injecting this knowledge into LLM adapters via instruction tuning, and aligning predictions with market reality using Proximal Policy Optimization (PPO). The reward function is derived from CAPM residuals, ensuring predicted shocks explain unexplained return variance. Experiments utilize 110,000 news articles and S&P 500 data, comparing FinRipple against RAG, zero-shot, and in-context learning baselines across multiple LLM architectures. Evaluation metrics include explanatory power (R2) on CAPM residuals, ANOVA significance, and refusal-to-answer rates.

Results show FinRipple significantly improves explanatory power, with R2 values up to 0.59 on Fama-French 5-factor residuals, outperforming all baselines. The model demonstrates superior instruction following and lower refusal rates. In portfolio management, a strategy based on FinRipple predictions achieves a Sharpe ratio of 1.153 and lower maximum drawdown compared to equal-weight and Markowitz benchmarks. Limitations include the computational cost of training and the dependency on the quality of KG construction. The paper provides an open-source benchmark for ripple effect prediction.

## FinDKG: Dynamic Knowledge Graphs with Large Language Models for Detecting Global Trends in Financial Markets

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: alpha mining, equity research, portfolio optimization, equities, etfs, portfolio management, us equities, fine-tuning, graph reasoning, knowledge graph, retrieval, news, sec filings, backtest, portfolio returns, sharpe ratio, dataset, model, open source, bias
- Tag facets: {"asset_class": ["equities", "etfs"], "data_source": ["news", "sec filings"], "deliverable": ["dataset", "model", "open source"], "evaluation": ["backtest", "portfolio returns", "sharpe ratio"], "market_context": ["portfolio management", "us equities"], "method": ["fine-tuning", "graph reasoning", "knowledge graph", "retrieval"], "risk_issue": ["bias", "data leakage"], "task": ["alpha mining", "equity research", "portfolio optimization"]}
- One-line summary: The paper introduces ICKG, a fine-tuned LLM for generating dynamic knowledge graphs from financial news, and KGTransformer, an attention-based GNN that leverages meta-entities to outperform baselines in link prediction and thematic AI investing.

### Detailed Summary

This paper addresses the challenge of extracting structured, temporal financial insights from unstructured news text by proposing a pipeline that combines Large Language Models with Graph Neural Networks. The authors argue that static knowledge graphs fail to capture the dynamic nature of financial markets and that existing LLM applications often lack the structural reasoning capabilities required for complex trend detection. By integrating meta-entity information into dynamic knowledge graph learning, the work aims to improve the accuracy of link prediction and enable more robust thematic investing strategies based on evolving corporate and macroeconomic relationships.

The methodology centers on two main contributions: the Integrated Contextual Knowledge Graph Generator (ICKG) and the KGTransformer architecture. ICKG is a Mistral-7B model fine-tuned via supervised learning on GPT-4-generated quadruples from 400,000 Wall Street Journal articles to extract entities, relations, and timestamps. The resulting FinDKG dataset is analyzed using KGTransformer, a graph attention network that incorporates meta-entities (e.g., Company, Person, Sector) to enhance embedding quality. The model uses recurrent neural networks to handle temporal dynamics and is evaluated on link prediction tasks across benchmark datasets and FinDKG. For application, the authors construct a monthly-rebalanced AI-themed portfolio using predicted link probabilities from the model.

Experimental results demonstrate that KGTransformer significantly outperforms static and temporal baselines, particularly on FinDKG where meta-entities provide a ~10% improvement in MRR. In thematic investing, the FinDKG-AI portfolio achieved a 39.6% annualized return and a Sharpe ratio of 1.81, surpassing major AI ETFs like ARKK and the S&P 500 benchmark during the 2022-2023 period. The paper highlights the utility of graph centrality measures for tracking global trends, such as the COVID-19 pandemic. Limitations include the reliance on news text which may introduce noise, the computational cost of LLM-based extraction, and the specific focus on AI themes which may not generalize to all market conditions without further validation.

## NatureKG: an ontology and knowledge graph for nature finance with a Text2Cypher application

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: risk extraction, public reits, institutional investing, fine-tuning, knowledge graph, semantic parsing, tables, accuracy, dataset, model, hallucination, nature finance, text2cypher, sustainable finance, esg, environmental risk
- Tag facets: {"asset_class": ["public reits"], "data_source": ["tables"], "deliverable": ["dataset", "model"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["fine-tuning", "knowledge graph", "semantic parsing"], "risk_issue": ["hallucination"], "task": ["risk extraction"]}
- One-line summary: The paper introduces NatureKG, a domain-specific knowledge graph for nature finance, and demonstrates the feasibility of using fine-tuned small LLMs like Phi-3 to translate natural language into Cypher queries for structured environmental risk assessment.

### Detailed Summary

This paper addresses the lack of structured tools for mapping dependencies between natural capital and financial assets, a critical gap in nature finance where institutions struggle to systematically assess environmental risks and impacts. The authors propose NatureKG, the first ontology and instantiated knowledge graph tailored to this domain, grounded in frameworks like ENCORE and SBTN. The research positions this work as a foundational step toward integrating domain-specific ontologies with AI systems to enhance transparency and scalability in sustainable finance decision support, particularly for the built environment sector.

The methodology involves designing an ontology defining entities such as Actions, Drivers of Nature Loss, and Value Chains, which was instantiated into a Neo4j database containing 320 nodes and 540 relationships curated by experts. To enable natural language interaction, the authors constructed a Text2Cypher dataset and fine-tuned three open-source LLMs (Phi-3, LLaMA-3.1-8B, and Mistral-7B) using LoRA. The experimental design included three dataset split strategies (paraphrase, cypher-level, and generalization) to evaluate linguistic and structural generalization, using metrics like execution accuracy, BLEU, and clause-level F1 scores.

Results indicate that Phi-3 achieved the highest execution accuracy (0.21) and Macro F1 (0.56), demonstrating that smaller, fine-tuned models can generalize effectively in low-resource, domain-specific settings, outperforming larger models like Mistral-7B. However, the study acknowledges limitations including modest initial accuracy, potential memorization from paraphrasing, and a narrow focus on the built environment. The findings validate the feasibility of LLM-assisted querying for nature finance but highlight the need for larger, domain-aligned data catalogues and refined reasoning capabilities for practical deployment in financial risk assessment.

## FinCARE: Financial Causal Analysis with Reasoning and Evidence

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, risk extraction, equities, portfolio management, knowledge graph, chain of thought, agentic workflow, 10-k filings, ablation study, framework, model risk, causal discovery, counterfactual analysis, synthetic data
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings"], "deliverable": ["framework"], "evaluation": ["ablation study"], "market_context": ["portfolio management"], "method": ["knowledge graph", "chain of thought", "agentic workflow"], "risk_issue": ["model risk"], "task": ["portfolio optimization", "risk extraction"]}
- One-line summary: FinCARE integrates SEC 10-K derived knowledge graphs and LLM reasoning into causal discovery algorithms (PC, GES, NOTEARS), achieving significant F1 score improvements and reliable counterfactual scenario analysis for portfolio management.

### Detailed Summary

Portfolio managers often rely on correlation-based heuristics that fail to capture true causal drivers of performance. FinCARE addresses this by proposing a hybrid framework that augments statistical causal discovery with domain knowledge from SEC 10-K filings and LLM reasoning. The system extracts causal triplets from filings to build a knowledge graph, which provides algorithmic constraints for causal discovery algorithms. Simultaneously, an LLM module generates hypotheses for missing edges based on financial theory. This approach aims to ground statistical discoveries in financial expertise while maintaining empirical validation, enabling proactive risk management and strategic decision-making in dynamic markets.

The methodology enhances three causal discovery paradigms: constraint-based (PC), score-based (GES), and continuous optimization (NOTEARS). Knowledge graph constraints are encoded as edge weights, with required edges bypassing independence tests in PC and adding bonuses to the BIC score in GES. In NOTEARS, constraints are applied via regularization and post-processing. The LLM component uses a 'MissingEdgeDiscoverer' to propose edges, which are integrated similarly to KG constraints. Experiments utilize a synthetic dataset of 500 firms across 18 variables with a known ground truth DAG. The study evaluates graph recovery metrics (F1, precision, recall) and counterfactual prediction accuracy using structural causal models.

Results show consistent improvements across all algorithms when enhanced with KG and LLM knowledge. NOTEARS achieved the highest F1 score of 0.759, a 366% improvement over the baseline. The framework demonstrated perfect directional accuracy for intervention effects and a mean absolute error of 0.003610 in counterfactual predictions. Ablation studies revealed that a single focused LLM agent outperformed multi-agent setups and that algorithmic KG encoding was more effective than prompt injection. Limitations include reliance on synthetic data for evaluation and the need for temporal extensions to capture dynamic market relationships.

## FinReflectKG: Agentic Construction and Evaluation of Financial Knowledge Graphs

- Year: 2025
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: due diligence, risk extraction, equities, options, derivatives, institutional investing, agentic workflow, knowledge graph, prompt engineering, retrieval, 10-k filings, sec filings, accuracy, dataset, framework, open source, hallucination, model risk, entity extraction, schema compliance
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["10-k filings", "sec filings"], "deliverable": ["dataset", "framework", "open source"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["agentic workflow", "knowledge graph", "prompt engineering", "retrieval"], "risk_issue": ["hallucination", "model risk"], "task": ["due diligence", "risk extraction"]}
- One-line summary: FinReflectKG introduces an agentic, reflection-driven framework for constructing large-scale financial knowledge graphs from S&P 100 SEC 10-K filings, achieving superior extraction quality and schema compliance compared to single-pass and multi-pass baselines.

### Detailed Summary

The paper addresses the critical gap in large-scale, high-quality open-source financial knowledge graphs by proposing a robust construction pipeline for SEC 10-K filings. Recognizing that existing datasets often rely on noisy news feeds or lack rigorous evaluation, the authors introduce a schema-guided, closed-information extraction approach. This method integrates intelligent document parsing, table-aware semantic chunking, and iterative prompt engineering to extract structured triples from the complex, regulatory-heavy text of annual reports. The system is designed to support downstream applications such as entity search, multi-hop question answering, and signal generation, providing a foundational resource for financial AI research that emphasizes transparency and reproducibility.

The core methodology features three extraction modes: single-pass, multi-pass, and a novel reflection-agent-based workflow. Using Qwen2.5-72B-Instruct, the reflection agent employs a critic-corrector loop to iteratively refine extracted triples, checking for schema compliance, entity normalization, and business relevance. The dataset comprises triples from all S&P 100 companies' 2024 10-K filings, utilizing a comprehensive ontology of entity types (e.g., ORG, RISK_FACTOR) and relationships (e.g., Has_Stake_In, Impacted_By). Evaluation combines rule-based checks (CheckRules), coverage ratios, entropy metrics, and LLM-as-a-Judge assessments for precision, faithfulness, and comprehensiveness, offering a holistic view of extraction quality without requiring ground-truth annotations.

Empirical results demonstrate that the reflection-agent mode achieves the best balance of accuracy and coverage, attaining a 64.8% compliance score across all rule-based policies and outperforming baselines in LLM-as-a-Judge evaluations for precision and comprehensiveness. While it generates denser, more navigable graphs, it exhibits lower semantic entropy, indicating a deliberate reduction in diversity for higher reliability. Key limitations include the lack of cross-document co-reference resolution and the reliance on LLM-voting for evaluation, which may propagate judge biases. The authors note that while the reflection mode is computationally heavier, it is essential for high-stakes financial applications requiring auditability and trust.

## Modal-adaptive Knowledge-enhanced Graph-based Financial Prediction from Monetary Policy Conference Calls with LLM

- Year: 2024
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: stock prediction, forecasting, equities, bonds, commodities, forex, institutional investing, multimodal modeling, knowledge graph, retrieval, fine-tuning, earnings calls, ablation study, accuracy, model, open source, data leakage, monetary policy, graph convolutional networks, volatility prediction
- Tag facets: {"asset_class": ["equities", "bonds", "commodities", "forex"], "data_source": ["earnings calls"], "deliverable": ["model", "open source"], "evaluation": ["ablation study", "accuracy"], "market_context": ["institutional investing"], "method": ["multimodal modeling", "knowledge graph", "retrieval", "fine-tuning"], "risk_issue": ["data leakage"], "task": ["stock prediction", "forecasting"]}
- One-line summary: The paper proposes MANAGER, a multimodal LLM framework that integrates external financial knowledge and adaptive graph-based fusion of text, video, and audio from Monetary Policy Conference calls to outperform baselines in predicting asset price movements and volatility.

### Detailed Summary

The paper addresses the challenge of financial prediction using Monetary Policy Conference (MPC) calls by identifying three key limitations in prior multimodal approaches: the neglect of external financial knowledge, the equal weighting of disparate modalities despite varying informational value, and the independent treatment of correlated financial assets. The authors aim to create a more robust prediction system that leverages the semantic richness of text, the non-verbal cues in video and audio, and the contextual depth of domain-specific knowledge graphs to improve forecasting accuracy for asset price movements and volatility.

The proposed method, MANAGER, utilizes ChatGLM2 as its backbone, enhanced by a knowledge-enhanced cross-modal graph. It extracts text features via ChatGLM2, video features via BEiT-3, and audio features via HuBERT. External knowledge is retrieved from the dynamic FinDKG to enrich the textual context. These modalities are fused using Graph Convolutional Networks (GCNs) that model intra-modal and inter-modal semantic relations, allowing the model to adaptively weigh the contribution of each modality. The system is evaluated on the Monopoly dataset, which contains multimodal data from MPC calls and labels for six financial assets, predicting price movement (F1 score) and volatility (MSE) over 1, 3, 7, and 15-day horizons.

Experimental results demonstrate that MANAGER consistently outperforms state-of-the-art baselines, including text-only models and other multimodal architectures, across all metrics and asset classes. Ablation studies confirm the significant contribution of external knowledge and the graph-based fusion mechanism, while also revealing that text remains the dominant modality, with video and audio providing marginal but positive gains. The study highlights the importance of incorporating domain knowledge and adaptive fusion in financial LLM applications, though it notes that improper handling of non-verbal cues can sometimes degrade performance compared to text-only methods.

## Interpreting Fedspeak with Confidence: A LLM-Based Uncertainty-Aware Framework Guided by Monetary Policy Transmission Paths

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, forecasting, equities, us equities, fine-tuning, prompt engineering, domain adaptation, sec filings, accuracy, framework, model, hallucination, fedspeak, monetary policy, uncertainty quantification, fomc
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings"], "deliverable": ["framework", "model"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["fine-tuning", "prompt engineering", "domain adaptation"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "forecasting"]}
- One-line summary: The paper proposes an LLM-based framework that integrates monetary policy transmission path reasoning and a dynamic uncertainty decoding module to achieve state-of-the-art accuracy and reliability in classifying Federal Reserve policy stances.

### Detailed Summary

The paper addresses the challenge of interpreting "Fedspeak," the nuanced language used by the U.S. Federal Open Market Committee (FOMC) to signal monetary policy stances. Traditional sentiment analysis models struggle with the contextual ambiguity of central bank communications, while existing LLM approaches often lack interpretability and reliability metrics. The authors position their work to bridge this gap by combining domain-specific economic reasoning with uncertainty-aware decoding, aiming to enhance both classification accuracy and the trustworthiness of model predictions for financial forecasting and algorithmic trading.

The proposed method augments Fedspeak texts by extracting financial entity relations and reasoning over monetary policy transmission paths using structured templates, emulating expert economic analysis. This augmented data is used to fine-tune LLMs, specifically Qwen-3-14B. A key innovation is the dynamic uncertainty decoding module, which quantifies Perceptual Uncertainty (PU) by decomposing it into Cognitive Risk (CR) and Environmental Ambiguity (EA) based on token logits. The model adaptively selects aggressive or conservative decoding strategies based on PU thresholds. Experiments are conducted on the Trillion Dollar Words FOMC dataset, covering meeting minutes, press conferences, and speeches from 1996 to 2022, evaluating performance using Macro-F1 and Weighted-F1 metrics against various zero-shot and fine-tuned baselines.

Results show the framework achieves state-of-the-art performance, outperforming the best baseline by 6.6% in Macro-F1. The ablation study confirms that transmission path reasoning provides the largest performance gain, while uncertainty quantification significantly improves reliability. Statistical analysis reveals a strong positive correlation between PU and error rates, with low-PU predictions achieving high accuracy (0.7822 Weighted-F1) compared to high-PU predictions (0.4372). Limitations include reliance on hand-crafted templates, limited generalizability to non-US central banks, and difficulties with implicit statements and contextual confusion. The work offers a robust tool for policy stance analysis with built-in confidence calibration.

## PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: forecasting, alpha mining, prediction markets, market microstructure, backtesting, prompt engineering, multimodal modeling, limit order book, news, backtest, sharpe ratio, market impact, transaction costs, benchmark, dataset, overfitting, data leakage, polymarket, clob, confidence-weighted return
- Tag facets: {"asset_class": ["prediction markets"], "data_source": ["limit order book", "news"], "deliverable": ["benchmark", "dataset"], "evaluation": ["backtest", "sharpe ratio", "market impact", "transaction costs"], "market_context": ["market microstructure"], "method": ["backtesting", "prompt engineering", "multimodal modeling"], "risk_issue": ["overfitting", "data leakage"], "task": ["forecasting", "alpha mining"]}
- One-line summary: PolyBench evaluates seven LLMs on live Polymarket data, revealing that only MiMo-V2-Flash and Gemini-3-Flash achieve positive financial returns, highlighting the gap between language fluency and profitable probabilistic reasoning under market uncertainty.

### Detailed Summary

The paper addresses the critical challenge of evaluating Large Language Models (LLMs) as autonomous forecasting agents in live, financially incentivized environments. Existing benchmarks often suffer from data contamination or lack real-time market grounding, failing to capture the multimodal complexity of fusing qualitative news with quantitative order-book dynamics. PolyBench introduces a contamination-proof benchmark derived from Polymarket, comprising 38,666 binary prediction markets across 4,997 events, synchronized with Central Limit Order Book (CLOB) states and real-time news streams to ensure strict temporal discipline and zero-shot evaluation.

The methodology involves a four-stage pipeline: collecting market data via the Polymarket Gamma API, fetching multimodal context (news and CLOB snapshots), batch processing predictions through seven state-of-the-art LLMs, and matching outcomes against ground truth. The evaluation framework assesses directional accuracy, Confidence-Weighted Return (CWR), Annualized Percentage Yield (APY), and Sharpe ratio via realistic order-book execution simulation. Models are constrained to issue BUY decisions only when confidence exceeds 0.6, with capital allocation scaled by stated confidence to penalize miscalibration. The study analyzes performance across varying lot sizes to account for slippage and liquidity constraints.

Results indicate a pronounced divergence: only MiMo-V2-Flash (17.6% CWR) and Gemini-3-Flash (6.2% CWR) achieve positive returns, while five models incur losses despite high stated confidence. Key findings include LLMs' implicit meta-cognition (higher confidence correlates with accuracy), severe miscalibration in volatile domains like Crypto, and the erosion of alpha due to order-book slippage at larger position sizes. The paper concludes that instruction adherence is necessary but insufficient for profitability, establishing PolyBench as a financially grounded standard for future LLM research.

## Dynamic Hedging Strategies in Derivatives Markets with LLM-Driven Sentiment and News Analytics

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Derivatives, Options, and Structured Products
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: derivatives hedging, sentiment analysis, derivatives, options, portfolio management, fine-tuning, backtesting, news, social media, sharpe ratio, drawdown, hit ratio, framework, model risk, dynamic hedging, real-time adjustment, sentiment index
- Tag facets: {"asset_class": ["derivatives", "options"], "data_source": ["news", "social media"], "deliverable": ["framework"], "evaluation": ["sharpe ratio", "drawdown", "hit ratio"], "market_context": ["portfolio management"], "method": ["fine-tuning", "backtesting"], "risk_issue": ["model risk"], "task": ["derivatives hedging", "sentiment analysis"]}
- One-line summary: The paper proposes a dynamic hedging framework for derivatives that integrates LLM-driven sentiment analysis from news and social media to adjust positions in real-time, achieving superior risk-adjusted returns compared to static hedging baselines.

### Detailed Summary

This paper addresses the challenge of managing risk in derivatives markets by integrating large language models (LLMs) into dynamic hedging strategies. The authors argue that traditional static hedging methods fail to account for rapid shifts in market sentiment driven by news and social media. The proposed framework leverages LLMs to extract sentiment indicators from diverse textual sources, allowing for real-time adjustments to hedging positions based on these signals. The research positions this approach as a significant advancement in decision-making processes within derivatives trading, aiming to enhance portfolio management and mitigate risks associated with volatility.

The methodology involves collecting textual data from news articles, social media, and financial reports, then using LLMs like GPT-4 and Llama-3-13b to generate sentiment scores. These scores are aggregated into a sentiment index, which drives the dynamic adjustment of hedging positions through a sensitivity parameter. The experimental setup includes backtesting on historical derivatives data from 2018 to 2022, comparing the proposed dynamic and LLM-optimized strategies against static hedging baselines. Metrics such as Sharpe Ratio, maximum drawdown, win rate, and average profit are used to evaluate performance. The study also conducts ablation studies to assess the impact of different model enhancements and sentiment source weights.

Results indicate that dynamic hedging strategies significantly outperform static methods, with GPT-4 achieving a Sharpe Ratio of 1.85 and a maximum drawdown of 9.8% under LLM optimization, compared to 1.25 and 15.6% for static hedging. The LLM fine-tuning approach further improved performance, yielding the highest Sharpe Ratio of 1.90. The paper highlights that real-time sentiment adjustments lead to higher win rates and average profits, particularly during market volatility spikes. However, the study notes limitations such as the computational cost of LLM inference and the potential for misleading content from LLMs. The findings suggest that sentiment-informed dynamic hedging can effectively enhance risk management in derivatives markets.

## FinSheet-Bench: From Simple Lookups to Complex Reasoning, Where LLMs Break on Financial Spreadsheets

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: due diligence, spreadsheet reasoning, private markets, venture capital, institutional investing, prompt engineering, tables, accuracy, benchmark, dataset, hallucination, synthetic data, tabular reasoning
- Tag facets: {"asset_class": ["private markets", "venture capital"], "data_source": ["tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["prompt engineering"], "risk_issue": ["hallucination"], "task": ["due diligence", "spreadsheet reasoning"]}
- One-line summary: FinSheet-Bench evaluates LLMs on synthetic private equity spreadsheet QA, revealing that even top models like Gemini 3.1 Pro achieve only 82.4% accuracy, with performance collapsing on complex aggregations, indicating a need for hybrid architectures separating parsing from computation.

### Detailed Summary

The paper addresses the critical gap in evaluating Large Language Models (LLMs) for extracting and reasoning over structured tabular data in private equity due diligence, where real-world data is confidential. Existing benchmarks fail to capture the complexity of non-standardized, multi-sheet financial spreadsheets used in alternative investment analysis. The authors introduce FinSheet-Bench, a benchmark of synthetic portfolio data modeled on real fund structures, designed to test text-serialized spreadsheet question answering and numeric reasoning tasks. This work positions itself at the intersection of financial NLP and tabular reasoning, highlighting the specific challenges of private markets data.

The methodology involves generating 24 synthetic Excel files from 8 real structural templates, applying rigorous anonymization and perturbation to cell values while preserving layout complexity. The authors evaluate ten model configurations from OpenAI, Google, and Anthropic using a zero-shot prompt and a cascading verification system (exact, fuzzy, and LLM-adjudicated matching). The experiments cover seven question categories ranging from simple lookups to complex aggregations, testing performance across varying spreadsheet sizes and structural modifications like merged cells and hidden rows.

Results show no standalone model achieves error rates low enough for unsupervised professional use, with the best model (Gemini 3.1 Pro) reaching 82.4% accuracy. Performance degrades significantly on larger, more complex spreadsheets, dropping to 48.6% for the largest file. Simple lookups achieve ~89% accuracy, but complex aggregations fall to ~20%. The findings suggest that LLMs struggle with multi-step numerical reasoning and spatial understanding in serialized text. The paper concludes that reliable extraction requires architectural approaches separating document understanding from deterministic computation, rather than relying solely on model scaling.

## FinanceQA: A Benchmark for Evaluating Financial Analysis Capabilities of Large Language Models

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: benchmarking, earnings analysis, spreadsheet reasoning, equities, institutional investing, fine-tuning, instruction tuning, 10-k filings, tables, accuracy, benchmark, dataset, hallucination, accounting conventions
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["hallucination"], "task": ["benchmarking", "earnings analysis", "spreadsheet reasoning"]}
- One-line summary: FinanceQA is a benchmark evaluating LLMs on realistic financial analysis tasks, revealing that state-of-the-art models fail approximately 60% of professional-grade questions due to poor handling of accounting conventions and incomplete information, though fine-tuning significantly improves performance.

### Detailed Summary

The paper addresses the critical gap between LLM capabilities and the rigorous demands of professional financial analysis, where high precision and adherence to accounting standards are non-negotiable. It argues that existing benchmarks like FinQA are misaligned with real-world workflows, focusing on simple extraction rather than complex reasoning, hand-spreading of metrics, and handling incomplete data. The authors introduce FinanceQA, a benchmark designed to test LLMs on tactical questions derived from primary documents like 10-K filings and conceptual questions requiring financial logic, aiming to replicate the daily tasks of hedge fund and private equity analysts.

The dataset was annotated by professionals with experience in investment firms, ensuring questions reflect actual on-the-job challenges. The evaluation covers four top models: GPT-4o, o1, Claude-3.5-Sonnet, and Llama-3.3-70B. Tasks are categorized into basic tactical, assumption-based (requiring inference from missing data), and conceptual questions. The study also experiments with fine-tuning GPT-4o on a synthetic dataset generated from human-annotated examples to assess if high-quality training data can bridge the performance gap. Evaluation uses exact match metrics to enforce strict accuracy standards.

Results show that even the best model, o1, achieves only 48.7% accuracy, with assumption-based tasks performing worst at under 5%. Fine-tuning GPT-4o yielded significant gains, improving total accuracy from 39.2% to 56.8%, with assumption-based performance jumping over 600%. The paper highlights that LLMs struggle with non-GAAP adjustments, lease accounting conventions, and generating assumptions for missing variables. Limitations include the dataset's focus on a single company (Costco) and the exclusion of Excel-based modeling tasks, suggesting that while fine-tuning helps, current LLMs remain insufficient for fully autonomous professional financial analysis.

## Biased echoes: Large language models reinforce investment biases and increase portfolio risks of private investors

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Wealth, Advisory, and Personal Investing
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: investment advisory, portfolio optimization, equities, etfs, retail investing, portfolio management, prompt engineering, backtesting, market prices, portfolio returns, risk-adjusted returns, drawdown, dataset, framework, bias, model risk, wealth management, cognitive bias, expense ratio, diversification risk
- Tag facets: {"asset_class": ["equities", "etfs"], "data_source": ["market prices"], "deliverable": ["dataset", "framework"], "evaluation": ["portfolio returns", "risk-adjusted returns", "drawdown"], "market_context": ["retail investing", "portfolio management"], "method": ["prompt engineering", "backtesting"], "risk_issue": ["bias", "model risk"], "task": ["investment advisory", "portfolio optimization"]}
- One-line summary: This study demonstrates that LLMs (ChatGPT, Gemini, Copilot) systematically increase portfolio risks for private investors across five dimensions—geographical, sector, trend chasing, active allocation, and expense risks—due to training data biases, with debiasing interventions only partially mitigating these effects.

### Detailed Summary

The paper addresses the critical gap in understanding how Large Language Models (LLMs) used for financial advice impact the investment risks of private investors. While LLMs are increasingly adopted for personalized advisory, there is limited empirical evidence on whether they perpetuate human cognitive biases or introduce new systemic risks. The authors position this work within the broader context of AI reliability in high-stakes domains, arguing that if LLMs reinforce biases inherent in their training data, they could expose millions of individuals to disproportionate financial harm and potentially amplify market volatility through herd-like behavior.

The methodology involves a large-scale experimental design querying three major LLMs (ChatGPT 3.5, Gemini, Copilot) with 270 prompts varying by investor age (15, 30, 50) and risk tolerance (low, medium, high). Recommendations were parsed and augmented with financial data from Yahoo Finance and Refinitiv Eikon to calculate five risk metrics: geographical cluster risk (US overexposure), sector cluster risk, trend chasing risk (momentum bias), active investment allocation risk, and total expense risk. Results were analyzed using MANOVA and mixed linear models, comparing LLM portfolios against a diversified global benchmark (Vanguard VT ETF).

Findings reveal that LLMs consistently recommend portfolios with significantly higher risks across all five dimensions compared to the benchmark, including over 93% US equity exposure and heavy trend chasing. The models exhibit 'cognitive' biases similar to humans, such as availability and recency biases. While debiasing interventions (e.g., prompt engineering) reduced some risks, they only partially mitigated the effects. The study highlights that LLMs often recommend higher-cost, actively managed assets, leading to lower risk-adjusted returns. Limitations include the use of ChatGPT 3.5 and the focus on retail investor profiles, suggesting a need for further testing on newer models and professional advisory contexts.

## The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Private Markets, VC, and Due Diligence
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: startup prediction, due diligence, venture capital, private markets, institutional investing, graph reasoning, multi-agent systems, retrieval, sec filings, accuracy, framework, model, data leakage, pitchbook dataset, interpretable ai, information gain, series a funding
- Tag facets: {"asset_class": ["venture capital", "private markets"], "data_source": ["sec filings"], "deliverable": ["framework", "model"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["graph reasoning", "multi-agent systems", "retrieval"], "risk_issue": ["data leakage"], "task": ["startup prediction", "due diligence"]}
- One-line summary: MIRAGE-VC introduces an information-gain-driven graph path retriever and multi-agent RAG framework to predict venture capital startup success, achieving state-of-the-art performance by distilling complex investment networks into interpretable reasoning chains.

### Detailed Summary

The paper addresses the challenge of predicting early-stage startup success in venture capital, a task requiring synthesis of complex relational evidence that traditional machine learning and graph neural networks cannot interpretably reason over. While LLMs offer reasoning capabilities, they face a modality mismatch with graph structures, and existing graph-LLM methods focus on in-graph tasks rather than off-graph prediction where the target outcome lies outside the network. The core problem is selecting high-value graph paths that maximize predictor performance on an external objective while enabling step-by-step, interpretable reasoning for investment theses.

The proposed MIRAGE-VC framework employs an information-gain-driven path retriever that iteratively selects neighbors to maximize LLM predictor accuracy, distilling investment networks into compact chains to avoid context overflow. It integrates three evidence streams—company disclosures, lead investor profiles, and graph-based paths—using a multi-agent architecture where specialist agents analyze each stream. A learnable gating network dynamically weights these heterogeneous evidence sources based on company attributes, and a manager agent synthesizes the weighted signals into a calibrated prediction with an interpretable rationale. Experiments use the PitchBook dataset with strict anti-leakage controls, evaluating on startups that secured Series A funding within one year of their seed round.

MIRAGE-VC achieves state-of-the-art results, improving F1 by 5.0% and Precision@5 by 16.6% over strong baselines like GNN-RAG and SSFF. The model demonstrates that correctly classified startups are associated with longer, richer retrieved paths, highlighting the value of structural context. The approach provides actionable investment signals and interpretable rationales, addressing the lack of transparency in black-box GNNs. Limitations include reliance on the proprietary PitchBook dataset, which restricts public reproducibility, and a myopic supervision objective that optimizes local one-hop gains rather than globally optimal subgraphs, potentially overlooking long-term dependencies in the network.

## StockSim: A Dual-Mode Order-Level Simulator for Evaluating Multi-Agent LLMs in Financial Markets

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Simulation and Execution Infrastructure
- Evidence type: infrastructure
- Summary coverage: full_extracted_text
- Tags: market simulation, execution analysis, equities, market microstructure, high-frequency trading, multi-agent systems, backtesting, limit order book, news, sharpe ratio, drawdown, market impact, open source, simulator, data leakage, look-ahead bias, agent coordination, latency modeling, slippage, reproducibility
- Tag facets: {"asset_class": ["equities"], "data_source": ["limit order book", "news"], "deliverable": ["open source", "simulator"], "evaluation": ["sharpe ratio", "drawdown", "market impact"], "market_context": ["market microstructure", "high-frequency trading"], "method": ["multi-agent systems", "backtesting"], "risk_issue": ["data leakage", "look-ahead bias"], "task": ["market simulation", "execution analysis"]}
- One-line summary: StockSim is an open-source, dual-mode simulation platform that evaluates LLM trading agents using realistic order-book microstructure and candlestick data, revealing distinct strategic behaviors between models like GPT-o3 and GPT-o4-mini.

### Detailed Summary

The paper addresses the critical gap in standardized, realistic evaluation infrastructure for Large Language Models (LLMs) in financial decision-making. Existing benchmarks often suffer from data leakage or abstract away crucial market microstructure details like latency and slippage. StockSim introduces a unified, open-source platform that supports two complementary simulation modes: an order-level execution mode that emulates real-time limit-order book dynamics, queueing, and market impact, and a candlestick-level mode for scalable, high-throughput testing. The system features an asynchronous architecture with role-based multi-agent coordination, allowing heterogeneous LLMs to act as specialist analysts (technical, fundamental, news) coordinated by a trader agent, thereby enabling rigorous assessment of reasoning under uncertainty and sequential decision-making in dynamic financial environments.

The methodology leverages a modular exchange simulation engine that integrates real-time market data from providers like Polygon.io and Alpha Vantage, alongside external news and fundamental streams. The engine processes agent actions via RabbitMQ, supporting limit, market, and stop orders with realistic latency and slippage modeling. Experiments were conducted on NVIDIA stock data from April to June 2025, comparing GPT-o3 and GPT-o4-mini agents using identical prompts. The evaluation framework computes comprehensive performance metrics including ROI, Sharpe ratio, Sortino ratio, win rate, and profit factor. The system was also stress-tested for scalability with deterministic agents, demonstrating linear scaling up to 150 concurrent agents on consumer hardware, ensuring reproducibility and consistent simulation outputs across runs.

Results indicate distinct trading strategies between the evaluated models: GPT-o3 adopted a selective, high-conviction approach with fewer trades, higher profit per trade, and superior risk-adjusted returns (Sharpe 5.97 vs 2.62), while GPT-o4-mini exhibited a more active, lower-efficiency trading style. The platform successfully captures these behavioral differences, highlighting its utility for NLP research on agent coordination and reasoning. Limitations include the platform's computational demands for large-scale multi-agent simulations and the inherent simplification of market complexities such as liquidity constraints and full market impact. Despite these caveats, StockSim provides a vital, production-grade testbed for bridging NLP research with real-world deployment requirements in financial markets.

## A Multi-Agent Orchestration Framework for Venture Capital Due Diligence

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Private Markets, VC, and Due Diligence
- Evidence type: case study
- Summary coverage: full_extracted_text
- Tags: due diligence, startup prediction, venture capital, private markets, institutional investing, agentic workflow, multi-agent systems, retrieval, tool use, sec filings, tables, framework, open source, hallucination, n8n, greek business registry, low-code, ocr, web scraping
- Tag facets: {"asset_class": ["venture capital", "private markets"], "data_source": ["sec filings", "tables"], "deliverable": ["framework", "open source"], "evaluation": [], "market_context": ["institutional investing"], "method": ["agentic workflow", "multi-agent systems", "retrieval", "tool use"], "risk_issue": ["hallucination"], "task": ["due diligence", "startup prediction"]}
- One-line summary: This paper presents an automated multi-agent framework for venture capital due diligence that integrates real-time web retrieval, reverse-engineered access to the Greek Business Registry for official financial filings, and a structural fallback mechanism to prevent hallucination by explicitly flagging data gaps.

### Detailed Summary

The paper addresses the inefficiencies and hallucination risks inherent in manual venture capital due diligence by proposing a fully automated, event-driven multi-agent orchestration framework. The system decomposes the research process into specialized sub-tasks handled by distinct AI agents, combining large language models with real-time web retrieval to synthesize unstructured data into structured investment intelligence. This approach aims to reduce human error, cognitive bias, and delays while ensuring that financial figures are grounded in auditable, official sources rather than generated estimates.

The methodology employs a Directed Acyclic Graph (DAG) architecture implemented on the n8n low-code platform. The pipeline begins with data intake, followed by market and competitive intelligence modules that query the Perplexity Sonar Deep Research API for real-time sector sizing and competitor analysis. A core technical contribution is a programmatic extraction pipeline that reverse-engineers the frontend-to-backend communication of the Greek Business Registry (Γ.E.MH.) to retrieve official financial PDFs, which are then parsed using a layout-aware OCR extractor. The system includes a structural fallback mechanism that queries third-party databases like Crunchbase or Dealroom if registry data is unavailable, or explicitly flags data absence to prevent hallucination.

The framework produces structured HTML reports containing company overviews, market intelligence, competitive landscapes, and financial summaries with preserved source citations. Key findings highlight the system's ability to automate end-to-end corporate research, delivering actionable insights such as attractiveness scores and 30-to-180-day recommendations. However, the system is limited by its reliance on the Greek registry for high-quality financial data, dependency on external commercial APIs, and non-deterministic LLM outputs. The authors note that generalizability across geographies and sectors requires further empirical evaluation, and suggest future work includes integrating international registries and self-hosted alternatives to reduce operational costs.

## LLM-Guided Evolutionary Strategy Generation for Quantitative Trading

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: strategy generation, alpha mining, equities, china market, market microstructure, fine-tuning, backtesting, news, limit order book, backtest, portfolio returns, drawdown, risk-adjusted returns, framework, model, model risk, interpretability, genetic algorithm, llm-guided evolution
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "limit order book"], "deliverable": ["framework", "model"], "evaluation": ["backtest", "portfolio returns", "drawdown", "risk-adjusted returns"], "market_context": ["china market", "market microstructure"], "method": ["fine-tuning", "backtesting"], "risk_issue": ["model risk"], "task": ["strategy generation", "alpha mining"]}
- One-line summary: The provided paper text describes KD-MSLRT, a lightweight sign language recognition model using knowledge distillation, which is unrelated to the cataloged paper 'LLM-Guided Evolutionary Strategy Generation for Quantitative Trading' (LLM-GA) that uses LLMs and genetic algorithms for quantitative trading strategy generation.

### Detailed Summary

The provided paper text details KD-MSLRT, a lightweight sign language recognition model, which is entirely unrelated to the cataloged paper 'LLM-Guided Evolutionary Strategy Generation for Quantitative Trading' (LLM-GA). The cataloged abstract describes LLM-GA, a framework integrating large language models with genetic algorithms for automated trading strategy generation. LLM-GA comprises three modules: a signal generator for technical, fundamental, and sentiment indicators; an LLM-enhanced genetic algorithm core that uses LLMs for semantically-aware crossover and mutation to maintain logical consistency; and an execution module. Experiments on Chinese stock market data (2020-2024) show LLM-GA achieves an Annualized Excess Return of 12.3% and a Maximum Drawdown of 35.2%, outperforming vanilla GA, PSO, and ensemble learning. Ablation studies indicate LLM-guided initialization improves starting strategy quality by 215%, and semantic crossover reduces invalid strategies by 83.5%. While LLM-GA's AER is 2-3% lower than reinforcement learning methods, it offers superior interpretability and diversity, addressing black-box limitations. The work establishes a paradigm for human-AI collaborative quantitative strategy development.

The provided text, however, focuses on sign language recognition. It introduces KD-MSLRT, which uses MediaPipe to extract skeletal landmarks from videos, reducing input from 3D video to 1D landmark data. This approach significantly reduces computational burden compared to video-based models. The model employs 3D to 1D knowledge distillation, transferring knowledge from a complex teacher network (CorrNet) to a lightweight student network (MSLR). It also includes a novel text correction network trained via self-supervised learning to correct output errors. The authors release a new large-scale Chinese sign language dataset of 8,976 samples. Experiments on PHOENIX14 and PHOENIX14T datasets show KD-MSLRT achieves a Word Error Rate decrease of at least 1.4% compared to state-of-the-art models, with a model size of 12.93 MB, enabling efficient deployment on resource-constrained devices like Intel CPUs.

There is a complete mismatch between the cataloged metadata and the provided paper text. The cataloged paper is about quantitative trading using LLMs and genetic algorithms, while the provided text is about sign language recognition using knowledge distillation and pose estimation. Therefore, no summary of the trading paper can be derived from the provided text. The trading paper's relevance to finance is high, as it directly addresses automated trading strategy generation. The sign language paper has no relevance to finance or LLMs in a financial context. The summary below reflects the cataloged paper's content as described in the abstract, since the text is irrelevant.

## MM-DREX: Multimodal-Driven Dynamic Routing of LLM Experts for Financial Trading

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, portfolio optimization, equities, crypto, derivatives, etfs, us equities, a-share market, market microstructure, multimodal modeling, reinforcement learning, fine-tuning, agentic workflow, tables, limit order book, sharpe ratio, drawdown, portfolio returns, ablation study, framework
- Tag facets: {"asset_class": ["equities", "crypto", "derivatives", "etfs"], "data_source": ["tables", "limit order book"], "deliverable": ["framework", "dataset", "benchmark"], "evaluation": ["sharpe ratio", "drawdown", "portfolio returns", "ablation study"], "market_context": ["us equities", "a-share market", "market microstructure"], "method": ["multimodal modeling", "reinforcement learning", "fine-tuning", "agentic workflow"], "risk_issue": ["model risk"], "task": ["algorithmic trading", "portfolio optimization"]}
- One-line summary: MM-DREX is a multimodal LLM framework that uses a vision-language router to dynamically allocate weights among four specialized trading experts, achieving superior risk-adjusted returns across stocks, futures, and crypto compared to static baselines.

### Detailed Summary

The paper addresses the challenge of non-stationary financial markets where traditional quantitative models and static LLM agents fail to adapt to regime shifts. MM-DREX proposes a decoupled architecture that separates market state perception from strategy execution. It employs a Vision-Language Model (VLM) to jointly analyze candlestick chart patterns and temporal price features, enabling the system to detect complex visual signals like head-and-shoulders formations alongside numerical trends. This multimodal input allows for a more robust understanding of market conditions than unimodal approaches, addressing the limitation of existing LLM trading systems that lack fine-grained, adaptive decision mechanisms.

The core method involves a dynamic router trained via a hybrid Supervised Fine-Tuning and Reinforcement Learning (SFT-RL) paradigm. The router allocates weights to four heterogeneous experts: Trend, Reversal, Breakout, and Positioning. Each expert implements specific technical strategies (e.g., MACross, RSI reversal, Turtle breakout). The system is evaluated on a novel multimodal dataset spanning US equities, Chinese A-shares, ETFs, futures, and cryptocurrencies, covering bull, bear, and crisis periods. Experiments compare MM-DREX against 15 baselines, including deep reinforcement learning models (PPO, SAC) and other LLM agents (FinAgent, FinMem), using metrics like total return, Sharpe ratio, and maximum drawdown.

Results show MM-DREX significantly outperforms baselines, achieving a 47.5% return in US equities and a Sharpe ratio of 1.83, surpassing the best RL and LLM competitors. Ablation studies confirm that visual modalities provide critical incremental value, with performance degrading substantially when candlestick data is removed. The model demonstrates robustness during black-swan events like the 2020 COVID crash and 2022 rate hikes, maintaining lower drawdowns than the S&P 500. Limitations include the computational cost of the 72B VLM backbone and the need for future work on real-time latency, transaction costs, and meta-learning for expert evolution to handle extreme long-horizon dependencies.

## AlphaForgeBench: Benchmarking End-to-End Trading Strategy Design with Large Language Models

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, strategy generation, factor modeling, crypto, equities, us equities, backtesting, prompt engineering, tool use, ohlc data, tables, backtest, sharpe ratio, drawdown, ablation study, benchmark, dataset, framework, model risk, overfitting
- Tag facets: {"asset_class": ["crypto", "equities"], "data_source": ["ohlc data", "tables"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "ablation study"], "market_context": ["us equities"], "method": ["backtesting", "prompt engineering", "tool use"], "risk_issue": ["model risk", "overfitting"], "task": ["alpha mining", "strategy generation", "factor modeling"]}
- One-line summary: AlphaForgeBench introduces a deterministic benchmark for LLMs that evaluates their ability to generate executable alpha factors and strategy code rather than direct trading actions, revealing that this approach eliminates the severe behavioral instability and non-reproducibility inherent in direct-trading agent evaluations.

### Detailed Summary

The paper addresses the critical failure mode of behavioral instability in LLM-based trading agents, where direct action emission leads to extreme run-to-run variance, inconsistent decision sequences even under deterministic decoding, and irrational action flipping due to stateless architectures and sensitivity to continuous-to-discrete mappings. To resolve this, the authors propose AlphaForgeBench, a framework that repositions LLMs as quantitative researchers generating executable alpha factors and strategy code, thereby decoupling reasoning from execution to ensure deterministic and reproducible evaluation aligned with real-world quantitative workflows.

The benchmark utilizes a two-stage dataset construction process: Stage 1 curates 633 real-world single-asset queries from brokerage reports and open-source repositories, while Stage 2 generates 270 structured queries across a 3x3 difficulty taxonomy (Logic Translation, Logic Completion, Goal-Oriented Generation) to enable fine-grained diagnostic evaluation. Experiments evaluate six frontier LLMs (including Gemini, Claude, GPT, DeepSeek, and Grok) by generating Python strategy functions and executing them in a unified backtest engine across seven assets (BTC, ETH, AAPL, GOOGL, MSFT, NVDA, TSLA) over a five-year period, measuring performance via Sharpe Ratio, Annual Return, Maximum Drawdown, and other risk-adjusted metrics.

Results demonstrate that the code-generation paradigm eliminates execution-induced instability, with intra-query variance an order of magnitude smaller than inter-query variance, and temperature-invariant model rankings. The study reveals distinct "risk personalities" among models (e.g., Gemini favors aggressive returns, DeepSeek favors conservative risk control) and identifies a clear performance hierarchy where Gemini-3-Pro leads in return-oriented metrics. The benchmark effectively exposes complementary cognitive capabilities, showing that code-translation skill and strategic reasoning are dissociable, with Level 3 tasks providing the highest discriminative power for assessing true financial reasoning and alpha discovery.

## Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, stock prediction, equities, market microstructure, portfolio management, agentic workflow, backtesting, multimodal modeling, retrieval, tables, limit order book, backtest, sharpe ratio, portfolio returns, benchmark, framework, open source, trading agent, overfitting, visual chart inputs
- Tag facets: {"asset_class": ["equities"], "data_source": ["tables", "limit order book"], "deliverable": ["benchmark", "framework", "open source", "trading agent"], "evaluation": ["backtest", "sharpe ratio", "portfolio returns"], "market_context": ["market microstructure", "portfolio management"], "method": ["agentic workflow", "backtesting", "multimodal modeling", "retrieval"], "risk_issue": ["overfitting"], "task": ["algorithmic trading", "stock prediction"]}
- One-line summary: The paper introduces the Agent Trading Arena, a zero-sum multi-agent simulation framework that demonstrates LLM-based agents significantly outperform traditional baselines when using visual chart inputs and a reflection module to handle dynamic market microstructure.

### Detailed Summary

The paper addresses the limitation of static backtesting in financial LLM research by introducing the Agent Trading Arena, a closed-loop, zero-sum virtual stock market. This environment forces LLM-based agents to interact via bid-ask mechanisms, directly influencing price dynamics and simulating realistic market friction, liquidity constraints, and slippage. The study positions this framework as a necessary step to bridge the gap between training and evaluation in dynamic financial environments, moving beyond passive historical analysis to active, adaptive decision-making where agents must compete against each other and adapt to shifting market conditions in real-time.

The proposed method, ArenaTrader, employs a three-stage pipeline: market analysis, trade execution, and strategic reflection. Agents process multi-modal inputs, including plain-text time-series data and visualizations like line charts and bar graphs, while also accessing a shared 'Chat Pool' for noisy or informative rumors. A key component is the reflection module, which allows agents to evaluate past strategies, contrast top and bottom performers, and refine future actions. Experiments were conducted on NASDAQ and CSI datasets using various LLMs (GPT-4o, Gemini-1.5, Qwen-VL) and compared against baselines such as Buy & Hold, SMA, MACD, and specialized models like StockFormer and TimesNet. Metrics included Total Return, Sharpe Ratio, and Win Rate.

Results indicate that LLMs struggle with numerical reasoning on plain-text data, often overfitting to local patterns, whereas visual inputs substantially improve performance. The combination of visual data and the reflection module yielded the best results, with GPT-4o achieving a Sharpe Ratio of 0.348 on NASDAQ, significantly outperforming the benchmark and traditional quantitative models. The agent demonstrated robustness, particularly in high-volatility regimes, without task-specific retraining. Limitations include the synthetic nature of the zero-sum environment, which may not fully capture external macroeconomic shocks, and the reliance on vision-capable LLMs, which may not be universally accessible or cost-effective for high-frequency trading applications.

## From Natural Language to Executable Option Strategies via Large Language Models

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Derivatives, Options, and Structured Products
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, derivatives hedging, options, derivatives, portfolio management, semantic parsing, backtesting, limit order book, market prices, backtest, hit ratio, risk-adjusted returns, benchmark, dataset, framework, hallucination, model risk, neuro-symbolic pipeline, option chain data, strategy generation
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["limit order book", "market prices"], "deliverable": ["benchmark", "dataset", "framework"], "evaluation": ["backtest", "hit ratio", "risk-adjusted returns"], "market_context": ["portfolio management"], "method": ["semantic parsing", "backtesting"], "risk_issue": ["hallucination", "model risk"], "task": ["alpha mining", "derivatives hedging"]}
- One-line summary: The paper introduces Option Query Language (OQL), a neuro-symbolic pipeline that translates natural language trading intents into executable option strategies by using LLMs as semantic parsers for a domain-specific intermediate representation, significantly improving execution accuracy and risk management over direct code generation baselines.

### Detailed Summary

The paper addresses the challenge of translating natural language trading intents into correct, executable option strategies, a task hindered by the high dimensionality of option chain data and the propensity of LLMs to hallucinate invalid constraints. It positions this work as a bridge between general LLM capabilities and the rigorous logic required for derivatives trading, proposing a neuro-symbolic approach that decouples semantic parsing from deterministic execution. The core innovation is the Option Query Language (OQL), a domain-specific intermediate representation that abstracts option markets into high-level primitives, allowing LLMs to function as reliable semantic parsers rather than free-form programmers.

The methodology involves a two-stage pipeline: first, an LLM converts natural language intent into structured OQL queries, which are then validated and executed by a deterministic engine against real-time option chain data. The system uses role-based abstraction, scoped filtering, and soft-matching operators to handle linguistic ambiguity and financial constraints. The authors introduce a new benchmark dataset of 200 diverse option trading instructions across five underlying assets (SPY, NVDA, AAPL, GOOG, TSLA) in 2025, evaluating models on query validity, strategy match, and semantic accuracy. Experiments compare OQL against free-form leg generation, partial-chain grounding, and text-to-SQL baselines using various commercial and open-weight LLMs.

Results demonstrate that OQL significantly improves execution accuracy and logical consistency, with specialized coding models like DeepSeek-Coder-6.7B outperforming larger general models in profitability and win rate. The neuro-symbolic pipeline reduces dangerous hallucinations and risk exposure, achieving a 60.9% win rate for DeepSeek-Chat compared to 52.8% for SQL. The study highlights that semantic accuracy is more predictive of downstream strategy performance than generation success alone. Limitations include the current reliance on predefined strategy templates and the need for future work to support free-form leg design and existing portfolio conditioning.

## PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, forecasting, market simulation, prediction markets, market microstructure, agentic workflow, multi-agent systems, backtesting, prompt engineering, market prices, limit order book, backtest, accuracy, framework, open source, trading agent, hallucination, regulatory compliance, latency arbitrage, bayesian aggregation
- Tag facets: {"asset_class": ["prediction markets"], "data_source": ["market prices", "limit order book"], "deliverable": ["framework", "open source", "trading agent"], "evaluation": ["backtest", "accuracy"], "market_context": ["market microstructure"], "method": ["agentic workflow", "multi-agent systems", "backtesting", "prompt engineering"], "risk_issue": ["hallucination", "regulatory compliance"], "task": ["alpha mining", "forecasting", "market simulation"]}
- One-line summary: PolySwarm is a multi-agent LLM framework that deploys 50 diverse personas to trade prediction markets via Bayesian aggregation and KL-divergence-based arbitrage, outperforming single-model baselines in calibration.

### Detailed Summary

This paper addresses the limitations of single-model LLMs in financial forecasting, specifically hallucination, miscalibration, and prompt sensitivity, by proposing PolySwarm, a multi-agent system for real-time prediction market trading. The authors argue that swarm intelligence can suppress idiosyncratic errors through diversity, positioning the framework as a solution to the epistemic uncertainty inherent in transformer-based inference for high-stakes financial decisions. The system targets decentralized platforms like Polymarket, leveraging their liquidity and binary outcome structures to test automated forecasting and arbitrage strategies.

The methodology involves deploying a swarm of 50 heterogeneous LLM personas with distinct analytical priors (e.g., macro, technical, contrarian) that operate independently to avoid anchoring. Individual probability estimates are aggregated using confidence-weighted Bayesian model averaging, combined with market-implied probabilities via a 70/30 linear mixture. The system employs an information-theoretic engine using Kullback-Leibler and Jensen-Shannon divergences to detect cross-market inefficiencies and negation pair mispricings. A latency arbitrage module exploits stale prices by deriving CEX-implied probabilities from a log-normal model. Experiments evaluate the system on Polymarket using Brier scores, log-loss, and calibration analysis, benchmarking against human superforecasters and single-model baselines.

Results demonstrate that swarm aggregation consistently outperforms single-model baselines in probability calibration, validating the wisdom-of-crowds effect in LLM ensembles. The system executes trades using quarter-Kelly position sizing for risk control. Key limitations include the risk of agent hallucination, high computational costs at scale, regulatory exposure in decentralized finance, and feedback-loop risks. The paper concludes that while multi-agent systems improve calibration, they require careful design to mitigate correlated errors and ensure robustness in live trading environments, suggesting future work on adaptive calibration and human-AI collaboration.

## Application of Startup Success Prediction Models and Business Document Extraction Using Large Language Models to Enhance Due Diligence Efficiency

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Private Markets, VC, and Due Diligence
- Evidence type: case study
- Summary coverage: full_extracted_text
- Tags: due diligence, startup prediction, spreadsheet reasoning, venture capital, private markets, institutional investing, prompt engineering, fine-tuning, sec filings, tables, accuracy, framework, model, privacy, venture capital prediction, business document extraction, user acceptance testing
- Tag facets: {"asset_class": ["venture capital", "private markets"], "data_source": ["sec filings", "tables"], "deliverable": ["framework", "model"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": ["prompt engineering", "fine-tuning"], "risk_issue": ["privacy"], "task": ["due diligence", "startup prediction", "spreadsheet reasoning"]}
- One-line summary: This paper presents a due diligence dashboard for venture capital that integrates GPT-4 for document analysis and XGBoost for startup success prediction, achieving a 4.50/5.00 user satisfaction score in a case study.

### Detailed Summary

The paper addresses the inefficiency and high failure rates in venture capital due diligence, which traditionally takes 4-6 weeks and relies on manual, error-prone processes. The authors aim to enhance decision-making accuracy and speed by developing an AI-assisted system that automates data extraction and risk assessment for early-stage startups. The research is grounded in a case study of an Indonesian corporate venture capital firm, highlighting the need for tools that can handle incomplete information and provide comprehensive business analysis.

The proposed solution follows the Team Data Science Process (TDSP) and integrates multiple technologies. It uses GPT-4 via the OpenAI API to extract and analyze unstructured data from pitch decks and financial reports, supplemented by the Google Search API for competitor and market trend analysis. For predictive modeling, the system employs an XGBoost classifier trained on a Kaggle dataset of 923 startups to predict success or failure based on funding and demographic features. The system is deployed as a web dashboard using React, Express.js, and Flask, allowing users to upload documents and receive structured analysis and predictions.

Experimental results show that the XGBoost model outperformed other tree-based models, achieving 84% accuracy and an F1 score of 88.23% through K-fold cross-validation. User acceptance testing with eight experienced investors yielded a high satisfaction score of 4.50/5.00, indicating strong approval of the system's usability and relevance. However, the authors note limitations, including GPT-4's struggles with complex mathematical reasoning and multi-page financial documents, as well as data security risks associated with third-party LLM APIs. The system is positioned as a supplementary tool rather than a replacement for expert judgment.

## ChatGPT as a Financial Advisor: A Re-Examination

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Wealth, Advisory, and Personal Investing
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: investment advisory, financial question answering, retail investing, prompt engineering, accuracy, benchmark, hallucination, regulatory compliance, personal finance, wealth management, tax implications, legal nuances, empathy assessment
- Tag facets: {"asset_class": [], "data_source": [], "deliverable": ["benchmark"], "evaluation": ["accuracy"], "market_context": ["retail investing"], "method": ["prompt engineering"], "risk_issue": ["hallucination", "regulatory compliance"], "task": ["investment advisory", "financial question answering"]}
- One-line summary: This qualitative study re-evaluates ChatGPT-4o and ChatGPT-5 against 21 personal finance scenarios, finding that while prompt engineering and model upgrades improve tone and numerical accuracy, the models still struggle with legal nuances, tax implications, and genuine empathy, positioning them as supportive rather than replacement tools for human advisors.

### Detailed Summary

This study addresses the evolving capability of large language models to provide personal financial advice, specifically examining whether ChatGPT-4o and ChatGPT-5 have improved upon the limitations observed in ChatGPT-3.5. The research problem centers on the qualitative assessment of AI-generated guidance, focusing on content accuracy, tone, legal caution, and emotional resonance in nuanced personal finance scenarios. The authors aim to determine if prompt engineering can mitigate previous shortcomings and if newer models offer meaningful advancements in delivering tailored, safe, and comprehensive financial planning suggestions to consumers and professionals.

The methodology employs a qualitative expert assessment of 21 personal finance cases originally developed by Schlosky et al. (2024). The authors evaluate ChatGPT-4o outputs under both regular and enhanced prompts, where the enhanced prompt defines a specific persona of a competent, empathetic, and tax-aware financial advisor. The analysis compares the content, prioritization, and tone of these outputs. Additionally, the study extends to a preliminary evaluation of ChatGPT-5 on a subset of cases to assess further improvements in numerical accuracy and general advice quality. Expert judgment is used to critique the advice for logical consistency, legal validity, and emotional appropriateness.

Findings indicate that ChatGPT-4o produces more thorough and creative suggestions than its predecessor, with prompt engineering significantly improving tone and attention to detail, such as tax implications. However, persistent limitations include overly broad generalizations, misleading legal references, and a lack of genuine empathy, often resulting in "false compassion." ChatGPT-5 shows better numerical accuracy but offers similar qualitative advice to ChatGPT-4o. The study concludes that while ChatGPT is maturing into a useful supporting tool for financial literacy and initial guidance, it cannot replace human advisors due to its inability to handle complex legal, ethical, and highly personalized financial planning needs effectively.

## QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: algorithmic trading, strategy generation, market microstructure, agentic workflow, backtesting, news, limit order book, backtest, benchmark, dataset, open source, bias, code generation, semantic alignment, execution analysis
- Tag facets: {"asset_class": [], "data_source": ["news", "limit order book"], "deliverable": ["benchmark", "dataset", "open source"], "evaluation": ["backtest"], "market_context": ["market microstructure"], "method": ["agentic workflow", "backtesting"], "risk_issue": ["bias"], "task": ["algorithmic trading", "strategy generation"]}
- One-line summary: QuantCode-Bench evaluates LLMs on generating executable Backtrader trading strategies, revealing that while syntax is mastered, semantic alignment and logic operationalization remain significant challenges even for frontier models.

### Detailed Summary

This paper addresses the gap in evaluating Large Language Models' ability to generate executable algorithmic trading strategies, a task requiring domain-specific financial logic, API knowledge, and semantic alignment beyond standard code generation. The authors introduce QuantCode-Bench, a benchmark of 400 tasks derived from Reddit, TradingView, StackExchange, GitHub, and synthetic sources, designed to test strategy generation for the Backtrader framework. The evaluation pipeline enforces four nested criteria: syntactic correctness, successful backtest execution, presence of trades, and semantic validation via an LLM judge, distinguishing technical executability from functional trading behavior.

Experiments compare state-of-the-art models in single-turn and agentic multi-turn settings. Results show that while compilation rates are near-perfect for frontier models, performance drops significantly at the trade and judge stages in single-turn mode, with top models achieving only 70-76% Judge Pass. In the agentic setting, iterative feedback allows models to repair local errors, boosting success rates to 95-98%. Error analysis reveals that failures are rarely syntactic; instead, they stem from incorrect operationalization of trading logic, improper API usage (e.g., Line object handling), and failure to match the task's semantic intent, particularly when conditions do not activate on data.

The study concludes that trading strategy generation is a distinct class of domain-specific code generation where success requires aligning natural language descriptions with financial logic and observable data behavior. Limitations include reliance on a single framework (Backtrader), the use of an LLM judge which may have biases, and the lack of evaluation on profitability or risk robustness. The benchmark highlights that general-purpose models often outperform code-specialized models in semantic interpretation, suggesting that instruction-following capabilities are critical for financial code generation.

## DeepFinLLM: an intelligent financial advisor unleashing strategic insights with large language models

- Year: 2025
- Category: Professional, Regulatory, and Advisory Applications
- Trading subtheme: Wealth, Advisory, and Personal Investing
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: investment advisory, financial question answering, equities, retail investing, tool use, prompt engineering, market prices, accuracy, hit ratio, framework, model, overfitting, hallucination, wealth management, latency optimization, factual consistency
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices"], "deliverable": ["framework", "model"], "evaluation": ["accuracy", "hit ratio"], "market_context": ["retail investing"], "method": ["tool use", "prompt engineering"], "risk_issue": ["overfitting", "hallucination"], "task": ["investment advisory", "financial question answering"]}
- One-line summary: DeepFinLLM is an intelligent financial advisor that integrates the DeepSeek Chat V3 model with real-time data from the Financial Modeling Prep API to provide accurate, low-latency financial insights, achieving 94.2% accuracy and outperforming baselines like FinGPT and BloombergGPT on standard financial benchmarks.

### Detailed Summary

The paper addresses the limitations of traditional rule-based financial tools and static AI models, which often suffer from low accuracy, high latency, and an inability to handle complex, unstructured natural language queries in real-time. DeepFinLLM is positioned as a hybrid system that combines sparse rule-based analysis with dense LLM-driven retrieval to deliver precise, contextually rich financial insights. The system aims to bridge the gap between semantic understanding and dynamic market data, ensuring that users receive timely and relevant advice for investment decisions, risk assessment, and market trend analysis.

The methodology employs a multi-layered architecture featuring a presentation layer, state management for conversational continuity, a data processing core, and an API integration layer that fetches live data via the Financial Modeling Prep (FMP) API. The system utilizes the DeepSeek Chat V3 model for semantic processing and intent classification, augmented by NLP techniques like tokenization and named entity recognition. Evaluation was conducted using five benchmark datasets (FinQA, FiQA, NumerSense, FinSim, ConvFinQA) against baselines including FinGPT, BloombergGPT, LLaMA-7B, and RoBERTa-Fin. Metrics included general language model performance (Perplexity, BLEU, ROUGE-L) and finance-specific accuracy, exact match, and inference latency.

Results indicate that DeepFinLLM achieves a 94.2% accuracy rate with an inference latency of 0.8 seconds, significantly outperforming baselines in both language generation quality and financial precision. It demonstrated superior performance in factual consistency (96.5%) and ranking quality (nDCG 0.95). The system is particularly useful for wealth advisory and personal investing, offering an intuitive interface for both novices and experts. However, limitations include potential overfitting to benchmark datasets, lack of statistical significance testing against baselines, and unproven generalizability to emerging markets or non-English queries. The authors note that real-world ecological validity and temporal stability require further validation.

## Can large language models effectively process and execute financial trading instructions?

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: execution analysis, equities, market microstructure, agent debate, prompt engineering, tables, limit order book, accuracy, dataset, framework, hallucination, trade order recognition, natural language to json, agent collaboration, information-exposure risk
- Tag facets: {"asset_class": ["equities"], "data_source": ["tables", "limit order book"], "deliverable": ["dataset", "framework"], "evaluation": ["accuracy"], "market_context": ["market microstructure"], "method": ["agent debate", "prompt engineering"], "risk_issue": ["hallucination"], "task": ["execution analysis"]}
- One-line summary: The paper proposes an intelligent trade order recognition pipeline using five LLMs to convert natural language trading instructions into standard JSON formats, revealing high syntactic validity but low end-to-end accuracy and excessive unnecessary clarifications.

### Detailed Summary

This research addresses the challenge of integrating Large Language Models (LLMs) into financial trading systems by developing an intelligent trade order recognition pipeline. The primary goal is to enable the conversion of unstructured trade orders into a standard format, specifically JSON, to facilitate automated trade execution. The study aims to improve human-trader interaction with platforms while mitigating misinformation risks during the execution phase. By focusing on the initial step of order recognition, the authors seek to bridge the gap between natural language intent and structured system commands.

The methodology involves creating a custom dataset of 500 trade order pieces to simulate real-world scenarios. Five state-of-the-art LLMs were evaluated using this dataset to assess their generative power and reliability in finance. The experimental design includes specific metrics for dataset reliability and model performance, focusing on syntactic validity, information completeness, and the frequency of clarifying questions. The system architecture features an agent collaboration model with user and trading agents, supported by carefully designed prompts for core tasks, instruction generation, and financial reasoning.

Results indicate that while most models generate syntactically valid JSON at high rates (80%-99%) and initiate clarifying questions in nearly all incomplete cases (90%-100%), end-to-end accuracy remains low (6%-14%). A significant limitation is the tendency for models to over-interrogate, with 70%-80% of follow-ups being unnecessary, which raises interaction costs and information-exposure risks. Despite these accuracy issues, the research demonstrates the feasibility of integrating the pipeline with real-world trading systems, paving the way for practical deployment of LLM-based trade automation solutions.

## DeltaHedge: A Multi-Agent Framework for Portfolio Options Optimization

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Derivatives, Options, and Structured Products
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, derivatives hedging, sentiment analysis, forecasting, equities, options, derivatives, portfolio management, multi-agent systems, reinforcement learning, backtesting, ohlc data, news, market prices, sharpe ratio, drawdown, risk-adjusted returns, framework, trading agent, tail risk
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["ohlc data", "news", "market prices"], "deliverable": ["framework", "trading agent"], "evaluation": ["sharpe ratio", "drawdown", "risk-adjusted returns"], "market_context": ["portfolio management"], "method": ["multi-agent systems", "reinforcement learning", "backtesting"], "risk_issue": ["tail risk"], "task": ["portfolio optimization", "derivatives hedging", "sentiment analysis", "forecasting"]}
- One-line summary: DeltaHedge is a multi-agent framework integrating transformer-based forecasting, sentiment analysis, and an ensemble of reinforcement learning agents to dynamically hedge equity portfolios with protective puts, significantly outperforming traditional and standalone RL baselines in risk-adjusted returns.

### Detailed Summary

The paper addresses the limitation of existing AI-driven portfolio management systems that largely ignore options trading for dynamic risk hedging. It proposes DeltaHedge, a hierarchical multi-agent system that coordinates specialized modules for forecasting, sentiment analysis, trading, and hedging. The framework aims to balance risk and return by integrating options into the decision-making loop, addressing the gap where traditional equity-focused methods fail to mitigate tail risks effectively in volatile markets. The system leverages the unique properties of options to provide downside protection while maintaining upside potential through coordinated agent interactions.

The methodology employs a Forecasting Agent using the Informer transformer for price predictions and a Sentiment Analysis Agent using DistilRoBERTa for news sentiment. The core decision-making involves a Trading Agent using Proximal Policy Optimization (PPO) for equity allocation and a Hedging Agent that dynamically adjusts protective put positions to maintain a delta-neutral stance. An ensemble strategy concurrently trains PPO, A2C, and DDPG agents, selecting the best performer quarterly based on Sharpe ratio validation. Experiments are conducted on S&P 500, Apple, and Tesla data from 2010-2024, comparing against Buy-and-Hold, technical strategies, standalone RL, and LLM-based frameworks like FinAgent, using metrics like Sharpe, Sortino, and Maximum Drawdown.

Results show DeltaHedge achieves a Sharpe ratio of 1.33 and Sortino ratio of 1.81 on the S&P 500, nearly doubling the next-best method, while capping maximum drawdowns at 10%. The ensemble hedging strategy proves robust across rising, falling, and volatile market regimes, outperforming single-agent hedgers and classical delta-hedge benchmarks. The system effectively times protection, lightening hedges when insurance is overpriced and switching to full protection during volatility spikes. Limitations include the focus on long-only positions, single-asset scope, and the assumption of sufficient liquidity for option execution, with future work targeting multi-asset portfolios and complex option structures.

## AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, factor modeling, equities, china market, us equities, multi-agent systems, chain of thought, backtesting, symbolic regression, ohlc data, backtest, hit ratio, information ratio, transaction costs, framework, open source, overfitting, alpha decay, quantitative investment, csi 500
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data"], "deliverable": ["framework", "open source"], "evaluation": ["backtest", "hit ratio", "information ratio", "transaction costs"], "market_context": ["china market", "us equities"], "method": ["multi-agent systems", "chain of thought", "backtesting", "symbolic regression"], "risk_issue": ["overfitting"], "task": ["alpha mining", "factor modeling"]}
- One-line summary: AlphaAgent is an autonomous multi-agent framework that uses LLMs to mine decay-resistant alpha factors by enforcing originality via AST similarity, hypothesis alignment, and complexity control, achieving superior risk-adjusted returns in CSI 500 and S&P 500 markets.

### Detailed Summary

Alpha mining faces significant challenges from alpha decay, where predictive signals lose efficacy due to overfitting and factor crowding. Traditional genetic programming and reinforcement learning methods often generate complex, spurious factors that fail in live markets, while existing LLM-based approaches lack regularization, leading to homogenized signals that replicate known inefficiencies. This paper addresses the critical need for decay-resistant factor discovery by introducing a structured approach that balances novelty, financial rationale, and parsimony, aiming to sustain predictive power across evolving market regimes in both Chinese and U.S. equity markets.

The proposed AlphaAgent framework employs a closed-loop multi-agent system comprising an idea agent, factor agent, and eval agent. The idea agent generates market hypotheses using chain-of-thought reasoning, while the factor agent constructs symbolic expressions using an operator library and abstract syntax trees (ASTs). Regularization mechanisms include AST-based similarity checks against existing alphas like Alpha101 to enforce originality, LLM-evaluated semantic consistency to ensure hypothesis alignment, and structural constraints to limit complexity. The system is evaluated on CSI 500 and S&P 500 data from 2021 to 2024, using LightGBM for return prediction and backtesting with transaction costs to assess performance.

Experiments demonstrate that AlphaAgent outperforms traditional and LLM-based baselines, achieving an 81% higher hit ratio and significant annualized excess returns of 11.0% (IR=1.5) for CSI 500 and 8.74% (IR=1.05) for S&P 500. The framework shows remarkable resistance to alpha decay, maintaining stable predictive power across bull and bear markets. However, the study relies on historical data and specific LLM capabilities, and the effectiveness may vary with different base models or market conditions. The approach offers a robust pipeline for quantitative investment, highlighting the potential of regularized LLM agents in discovering sustainable alpha sources.

## Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, factor modeling, equities, china market, a-share market, mcts, time-series modeling, backtesting, market prices, ohlc data, information ratio, backtest, ablation study, framework, open source, overfitting, data leakage, symbolic regression, interpretability, search diversity
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "ohlc data"], "deliverable": ["framework", "open source"], "evaluation": ["information ratio", "backtest", "ablation study"], "market_context": ["china market", "a-share market"], "method": ["mcts", "time-series modeling", "backtesting"], "risk_issue": ["overfitting", "data leakage"], "task": ["alpha mining", "factor modeling"]}
- One-line summary: The paper proposes an LLM-powered Monte Carlo Tree Search framework for formulaic alpha mining that integrates multi-dimensional backtesting feedback and frequent subtree avoidance to discover interpretable, high-performing alpha factors.

### Detailed Summary

The paper addresses the challenge of automated formulaic alpha mining, where traditional genetic programming and reinforcement learning methods often produce opaque, hard-to-interpret factors or suffer from inefficient search spaces. The authors propose a novel framework that models alpha discovery as a tree search problem, leveraging Large Language Models (LLMs) to iteratively generate and refine symbolic alpha formulas. This approach aims to balance predictive power with human interpretability, addressing the 'black box' nature of neural network-based alphas and the structural homogeneity of genetic programming outputs. By framing the task as a reasoning problem guided by financial feedback, the method seeks to navigate the vast space of possible mathematical expressions more effectively than previous automated techniques.

The core methodology integrates an LLM with Monte Carlo Tree Search (MCTS). The LLM acts as a generative prior, proposing refinements to candidate alpha formulas based on multi-dimensional evaluation scores derived from financial backtesting, including effectiveness, stability, turnover, diversity, and overfitting risk. A key innovation is the Frequent Subtree Avoidance (FSA) mechanism, which identifies common structural motifs in successful alphas and explicitly instructs the LLM to avoid them, thereby enhancing search diversity. The system uses a relative ranking approach to evaluate new alphas against an evolving repository of effective factors. Experiments are conducted on Chinese A-share markets (CSI 300 and CSI 1000 indices) using 10-day and 30-day return prediction targets, comparing the method against baselines like Genetic Programming, Deep Symbolic Optimization, AlphaGen, and other LLM-based approaches such as Chain-of-Thought and Tree-of-Thought.

Experimental results demonstrate that the proposed framework outperforms all baselines in predictive accuracy (IC, RankIC) and trading performance (Annualized Excess Return, Information Ratio). The ablation studies confirm the individual contributions of MCTS, multi-dimensional feedback, and FSA to the overall performance. Notably, the method achieves superior out-of-sample generalization, indicating reduced overfitting compared to competitors. The mined alphas also exhibit high interpretability, ranking second only to Chain-of-Thought in human-logic assessments, while significantly outperforming non-LLM baselines in this regard. The framework offers flexibility in LLM choice, allowing for a trade-off between performance and computational cost, with lightweight models achieving competitive results at a fraction of the cost of larger models like GPT-4.1.

## JAX-LOB: A GPU-Accelerated limit order book simulator to unlock large scale reinforcement learning for trading

- Year: 2023
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Simulation and Execution Infrastructure
- Evidence type: infrastructure
- Summary coverage: full_extracted_text
- Tags: execution analysis, market simulation, equities, high-frequency trading, market microstructure, reinforcement learning, tool use, limit order book, backtest, portfolio returns, framework, open source, simulator, overfitting, gpu acceleration, jax, ppo, trade execution
- Tag facets: {"asset_class": ["equities"], "data_source": ["limit order book"], "deliverable": ["framework", "open source", "simulator"], "evaluation": ["backtest", "portfolio returns"], "market_context": ["high-frequency trading", "market microstructure"], "method": ["reinforcement learning", "tool use"], "risk_issue": ["overfitting"], "task": ["execution analysis", "market simulation"]}
- One-line summary: JAX-LOB is the first GPU-accelerated limit order book simulator that enables large-scale parallel reinforcement learning for optimal trade execution, achieving at least a 7x speedup over CPU-based implementations.

### Detailed Summary

The paper addresses the computational bottleneck in training reinforcement learning agents for high-frequency trading tasks, specifically optimal trade execution, by introducing JAX-LOB, a GPU-enabled limit order book simulator. Traditional CPU-based simulators struggle with the low signal-to-noise ratio and the need for massive parallelization required to overcome overfitting and capture realistic market dynamics. The authors position this tool as a critical infrastructure component for agent-based models and RL environments, aiming to unlock scalable research into market microstructure and execution strategies without compromising the realism of LOB mechanisms.

The core method involves implementing the LOB mechanics using JAX, leveraging its just-in-time compilation and automatic vectorization to process thousands of order books in parallel via the vmap operator. The architecture uses fixed-size arrays to represent bid and ask sides, avoiding the overhead of dynamic sorting during message processing. The simulator is integrated with the Gymnax RL framework and PureJaxRL, wrapping the environment to allow both experience rollout and network updates to occur entirely on the GPU. Experiments compare JAX-LOB against CPU-based implementations (including RL4MM and a custom linked-list simulator) using LOBSTER data for stocks like TSLA and AMZN, measuring processing times per message and training steps per second.

Results demonstrate a significant performance advantage, with JAX-LOB achieving up to 75x faster per-message processing and a 7x speedup in RL training steps compared to CPU baselines. The paper provides a preliminary example of training a Recurrent PPO agent for optimal execution, showing it can outperform a TWAP benchmark in-sample, though out-of-sample validation is noted as future work. Limitations include the current lack of strategic agent interaction in the replay data (only direct market impact is captured) and the need for rigorous hyperparameter tuning and broader testing to establish robustness. The deliverable is an open-source framework designed to facilitate large-scale RL research in trading.

## Can Large Language Models Mine Interpretable Financial Factors More Effectively? A Neural-Symbolic Factor Mining Agent Model

- Year: 2024
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: alpha mining, factor modeling, stock prediction, equities, us equities, portfolio management, agentic workflow, chain of thought, prompt engineering, backtesting, ohlc data, sharpe ratio, portfolio returns, ablation study, model, framework, hallucination, neuro-symbolic, interpretability, in-context learning
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data"], "deliverable": ["model", "framework"], "evaluation": ["sharpe ratio", "portfolio returns", "ablation study"], "market_context": ["us equities", "portfolio management"], "method": ["agentic workflow", "chain of thought", "prompt engineering", "backtesting"], "risk_issue": ["hallucination"], "task": ["alpha mining", "factor modeling", "stock prediction"]}
- One-line summary: The paper proposes FAMA, a neural-symbolic agent that uses LLMs with Cross-Sample Selection and Chain-of-Experience to mine interpretable alpha factors, achieving superior predictive performance and portfolio returns on S&P 500 data compared to symbolic and neural baselines.

### Detailed Summary

The paper addresses the challenge of mining financially interpretable factors for stock return prediction, a critical task in empirical asset pricing. Existing methods are divided into symbolic models, which offer interpretability but suffer from inefficient search spaces, and neural models, which are efficient but lack transparency. The authors propose FAMA (FActor Mining Agent), an agent-based framework that leverages Large Language Models (LLMs) to bridge this gap. FAMA treats the LLM as a neuro-symbolic bridge, using in-context learning to generate symbolic factor expressions that retain financial interpretability while benefiting from the generative power of neural networks. The core problem is mitigating the homogeneity and inefficiency of direct LLM factor generation by structuring the prompt with diverse examples and past successful mining paths.

The FAMA model consists of two key components: Cross-Sample Selection (CSS) and Chain-of-Experience (CoE). CSS employs K-Means clustering on factor exposures to select low-correlation factors as in-context examples, ensuring diversity in the generated factors and reducing homogeneity. CoE maintains a dynamic chain of successful factor mining paths, allowing the LLM to learn from past experiences. The system iteratively mines factors using text-davinci-002 on S&P 500 stock data from 2015 to 2022. Experiments compare FAMA against symbolic baselines like Alpha101 and Genetic Programming, and neural baselines like FactorVAE and DTransformer. Evaluation metrics include RankIC and RankICIR for predictive accuracy, and annualized return and Sharpe ratio for investment simulation.

Results demonstrate that FAMA outperforms state-of-the-art models, achieving a RankIC improvement of 0.006 and RankICIR of 0.105 over the best neural baseline. In investment simulations, FAMA achieved an annualized return of 38.4% and a Sharpe ratio of 667.2%, significantly surpassing the S&P 500 benchmark and other models. The ablation studies confirm that both CSS and CoE contribute to performance, with CoE iterations enhancing results up to a point. However, the paper notes limitations regarding LLM hallucinations in the financial domain, which can introduce noise into the factor mining process. The study highlights the potential of agentic workflows for alpha mining but cautions about the need for robust error handling in production environments.

## ABIDES: Towards High-Fidelity Multi-Agent Market Simulation

- Year: 2020
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Simulation and Execution Infrastructure
- Evidence type: infrastructure
- Summary coverage: first_50k_chars
- Tags: market simulation, execution analysis, equities, market microstructure, high-frequency trading, agent debate, agentic workflow, multi-agent systems, limit order book, market impact, backtest, simulator, open source, look-ahead bias, discrete event simulation, nasdaq protocols, co-location, reproducibility
- Tag facets: {"asset_class": ["equities"], "data_source": ["limit order book"], "deliverable": ["simulator", "open source"], "evaluation": ["market impact", "backtest"], "market_context": ["market microstructure", "high-frequency trading"], "method": ["agent debate", "agentic workflow", "multi-agent systems"], "risk_issue": ["look-ahead bias"], "task": ["market simulation", "execution analysis"]}
- One-line summary: ABIDES is an open-source, high-fidelity agent-based discrete event simulation environment for equity markets that enables controlled experiments on market impact, co-location, and learning agents by replicating NASDAQ protocols with nanosecond precision.

### Detailed Summary

The paper addresses the lack of accessible, high-fidelity market simulation environments for academic research, noting that proprietary tools are unavailable and existing open-source platforms often lack the realism required for studying complex agent interactions. The authors introduce ABIDES, an open-source Agent-Based Interactive Discrete Event Simulation environment designed to support agent-based research in market applications. The core problem is enabling researchers to conduct controlled "what if" studies, such as analyzing market impact or co-location benefits, which are impossible with historical data alone due to the inability to isolate variables and observe individual agent intent. ABIDES aims to fill this gap by providing a platform where strategies can be endogenously chosen by learning agents interacting in a realistically structured market.

The method involves a Python-based discrete event simulation kernel that models the NASDAQ ITCH and OUCH message-based protocols. Key features include nanosecond time resolution, configurable pairwise network latency with cubic jitter, and computation delays that affect message timing. The architecture consists of a simulation kernel, an exchange agent, and a hierarchy of agent classes (basic, exchange, trading). Experiments validate the environment using background agents (Zero Intelligence and Heuristic Belief Learning) to reproduce historical price movements and an "impact agent" to study market impact. The system supports deterministic execution via global virtual time and per-agent random number generators, ensuring reproducibility while allowing for A/B testing of specific agent changes.

Findings demonstrate that ABIDES can accurately reproduce historical intra-day transaction histories using background agents and effectively model the mechanical and strategic market impact of large orders. The market impact case study shows that profit per share declines as trade size increases, with a correlation of r = -0.31 across trials. The platform also supports non-finance applications, such as simulating secure multiparty federated learning. Limitations include the current single-threaded nature of the kernel, which may limit scalability for extremely large populations, and the reliance on historical data for background agents, which may not capture all emergent behaviors. The tool is positioned as a foundational infrastructure for developing and evaluating ML trading algorithms and studying market microstructure.

## A Fused Large Language Model for Predicting Startup Success

- Year: 2024
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Private Markets, VC, and Due Diligence
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: startup prediction, due diligence, venture capital, private markets, institutional investing, fine-tuning, time-series modeling, private company data, accuracy, backtest, model, bias, crunchbase, bert embeddings, fused model, roi estimation
- Tag facets: {"asset_class": ["venture capital", "private markets"], "data_source": ["private company data"], "deliverable": ["model"], "evaluation": ["accuracy", "backtest"], "market_context": ["institutional investing"], "method": ["fine-tuning", "time-series modeling"], "risk_issue": ["bias"], "task": ["startup prediction", "due diligence"]}
- One-line summary: The paper develops a fused large language model combining BERT-generated embeddings of textual self-descriptions with fundamental variables from Crunchbase profiles to predict startup success, achieving a statistically significant improvement in balanced accuracy and a substantial increase in estimated investment ROI compared to baselines using only structured data or traditional text representations.

### Detailed Summary

The paper addresses the challenge of predicting startup success to support venture capital investment decisions, a task complicated by high failure rates and the reliance on subjective investor judgment. It positions the use of online venture capital platform data, specifically Crunchbase, as a scalable alternative to proprietary databases or manual scorecards. The core problem is leveraging both structured fundamental variables (e.g., founder education, funding history) and unstructured textual self-descriptions of business models and innovations to improve prediction accuracy beyond what is possible with structured data alone.

The methodology employs a tailored fused large language model architecture. Textual self-descriptions are processed using a pre-trained BERT model to generate 768-dimensional document embeddings, which are then concatenated with normalized fundamental variables. This fused vector is fed into various machine learning classifiers, including logistic regression, elastic net, random forest, and neural networks. The study utilizes a dataset of 20,172 startup profiles from Crunchbase, defining success via events like IPOs, acquisitions, or subsequent funding rounds. Performance is evaluated using balanced accuracy, AUROC, and a calculated Return on Investment (ROI) metric derived from estimated valuations and investment costs, with rigorous out-of-sample testing and sensitivity analyses across sectors and startup ages.

Results indicate that the fused model significantly outperforms baselines using only fundamental variables (balanced accuracy 74.33% vs. 72.00%) and traditional text representations like bag-of-words or GloVe. The inclusion of textual self-descriptions adds statistically significant predictive power, translating to a 40.61 percentage point increase in estimated ROI for the investment portfolio. The paper demonstrates that while fundamental variables provide a strong baseline, the semantic information in self-descriptions captures latent factors like business model clarity and tone that enhance decision-making. Limitations include the reliance on self-reported data which may be biased, the approximation of financial metrics due to lack of public valuation data, and the focus on US-based startups, potentially limiting generalizability to other markets or early-stage pre-profile ventures.

## Beyond Isolated Investor: Predicting Startup Success via Roleplay-Based Collective Agents

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Private Markets, VC, and Due Diligence
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: startup prediction, due diligence, venture capital, private markets, institutional investing, multi-agent systems, graph reasoning, agent debate, private company data, ablation study, framework, open source, data leakage, venture capital syndication, collective decision making, pitchbook data, crunchbase data, vgat architecture, investor network
- Tag facets: {"asset_class": ["venture capital", "private markets"], "data_source": ["private company data"], "deliverable": ["framework", "open source"], "evaluation": ["ablation study"], "market_context": ["institutional investing"], "method": ["multi-agent systems", "graph reasoning", "agent debate"], "risk_issue": ["data leakage"], "task": ["startup prediction", "due diligence"]}
- One-line summary: SimVC-CAS predicts startup financing success by simulating collective venture capital decision-making through LLM-based investor agents interacting over a co-investment network, achieving a 25% relative improvement in AP@10 over baselines.

### Detailed Summary

The paper addresses the limitation of existing startup success prediction models that treat investors as isolated decision-makers, ignoring the collective dynamics and network effects inherent in real-world venture capital syndication. It reframes financing prediction as a group decision-making task, positing that investor interactions and peer influence significantly impact funding outcomes. The proposed SimVC-CAS system simulates this process by constructing heterogeneous investor agents and modeling their interactions within a graph-structured co-investment network.

The method employs a three-module architecture: a startup panoramic portrait integrating firm fundamentals and team data; heterogeneous investor portraits generated from historical investor profiles and past investment behaviors; and a collective interaction module using a Virtual Node Graph Attention Network (VGAT). VGAT models the startup as a virtual node to capture context-specific interaction patterns among investors. Agents perform initial individual evaluations using LLM role-playing, then update decisions based on peer influence derived from the learned interaction topology. The system is trained and evaluated on proprietary PitchBook data and public Crunchbase data, using strict temporal splits to prevent leakage.

SimVC-CAS achieves a 25% relative improvement in average precision@10 compared to the strongest baseline, demonstrating superior capability in ranking high-potential startups. The interaction mechanism is particularly effective for network-central startups, confirming the importance of network structure. Analysis reveals that correct decision revisions are driven more by authority influence and information completion than consensus pressure. The system exhibits high consistency with real investor decisions and interpretability, though it relies on proprietary data and may face generalization challenges to other group decision contexts.

## FinAgent: A multimodal foundation agent for financial trading: Data-retrieval data-mining, policy-generation, and trading

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: strategy generation, portfolio optimization, equities, us equities, multi-agent systems, multimodal modeling, chain of thought, news, ohlc data, sharpe ratio, drawdown, portfolio returns, ablation study, framework, dataset, open source, model risk, technical analysis, position sizing, explainability
- Tag facets: {"asset_class": ["equities"], "data_source": ["news", "ohlc data"], "deliverable": ["framework", "dataset", "open source"], "evaluation": ["sharpe ratio", "drawdown", "portfolio returns", "ablation study"], "market_context": ["us equities"], "method": ["multi-agent systems", "multimodal modeling", "chain of thought"], "risk_issue": ["model risk"], "task": ["strategy generation", "portfolio optimization"]}
- One-line summary: FinVision is a multi-agent LLM framework that integrates news, visual technical analysis, and historical reflection to generate explainable trading decisions with position sizing, outperforming traditional and RL baselines on major tech stocks.

### Detailed Summary

The paper addresses the challenge of integrating diverse, multi-modal financial data into explainable trading systems, moving beyond the limitations of traditional deep learning and reinforcement learning models that often lack interpretability and oversimplify complex market dynamics. The authors propose FinVision, a multi-agent framework designed to synthesize textual news, visual chart patterns, and historical performance data to make granular trading decisions. This approach aims to provide a transparent, step-by-step reasoning process for each trade, allowing for better risk management and strategy refinement compared to black-box models.

The methodology employs four specialized agents built on GPT-4o-mini and o1-mini, orchestrated via LangGraph. The Summarize Agent processes daily news, the Technical Analyst Agent interprets candlestick charts and indicators like MACD and RSI, and the Reflection Agent analyzes past trading signals and performance metrics. These insights are fed into a Prediction Agent that outputs a BUY/SELL/HOLD action, a specific position size as a percentage of the portfolio, and a detailed rationale. The system was evaluated on Apple, Amazon, and Microsoft over a seven-month testing period in 2023, using Annual Rate of Return, Sharpe Ratio, and Maximum Drawdown as key performance indicators, while comparing against Buy-and-Hold, rule-based strategies, and RL models like PPO and DQN.

Results indicate that FinVision achieved competitive returns and superior risk-adjusted performance compared to passive and RL-based baselines, with a Sharpe Ratio of 1.20 for AAPL versus 0.67 for Buy-and-Hold. Ablation studies confirmed that the reflection module significantly boosts performance by enabling adaptive learning from past errors. However, the framework underperformed the FinAgent baseline, which utilized a year-long training period, highlighting the trade-off between API costs and performance. The study demonstrates the viability of multi-modal LLM agents for trading but notes limitations in handling extreme market volatility and the high computational cost of multi-agent inference.

## LOB-Bench: Benchmarking Generative AI for Finance - an Application to Limit Order Book Data

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: market simulation, stock prediction, equities, high-frequency trading, market microstructure, backtesting, time-series modeling, limit order book, market impact, accuracy, benchmark, open source, model, overfitting, generative ai, synthetic data, state-space models, distributional similarity
- Tag facets: {"asset_class": ["equities"], "data_source": ["limit order book"], "deliverable": ["benchmark", "open source", "model"], "evaluation": ["market impact", "accuracy"], "market_context": ["high-frequency trading", "market microstructure"], "method": ["backtesting", "time-series modeling"], "risk_issue": ["overfitting"], "task": ["market simulation", "stock prediction"]}
- One-line summary: LOB-Bench introduces a comprehensive benchmark for evaluating generative models of limit order book data, demonstrating that autoregressive state-space models outperform traditional parametric and GAN-based approaches in reproducing realistic market microstructure dynamics.

### Detailed Summary

The paper addresses the critical lack of standardized, quantitative evaluation metrics for generative models in financial market microstructure, specifically for limit order book (LOB) data. Existing methods rely on qualitative assessments of stylized facts or simple cross-entropy losses that fail to capture error accumulation during autoregressive sampling. The authors propose LOB-Bench, a Python-based framework that evaluates the distributional similarity between real and generated LOB data using both unconditional and conditional statistical metrics. This includes measuring distributional differences in key LOB statistics such as spread, order book volumes, order imbalance, and message inter-arrival times, alongside adversarial discriminator scores and market impact response functions. The framework is designed to be extensible and applicable to other high-dimensional financial time series.

The study benchmarks four modern generative AI models against a traditional parametric baseline: an autoregressive state-space model (LOBS5), a conditional GAN (Coletta), and two RWKV variants. Experiments are conducted on high-frequency LOB data for Alphabet (GOOG) and Intel (INTC) stocks in the LOBSTER format. The evaluation pipeline computes L1 and Wasserstein-1 distances between real and generated distributions, assesses conditional dependencies (e.g., spread conditioned on time of day), and measures the divergence of errors over increasing prediction horizons to identify "model derailment." Additionally, the authors train a discriminator network to distinguish real from generated trajectories and evaluate the downstream utility of synthetic data by training a mid-price prediction classifier.

Results indicate that the autoregressive LOBS5 model significantly outperforms traditional classes, achieving the lowest distributional errors and best reproduction of market impact curves, particularly for the small-tick GOOG stock. The baseline parametric model fails to capture complex dynamics, while RWKV models exhibit rapid error accumulation and distributional drift. The Coletta model performs well on small-tick stocks but fails on larger ticks like INTC. The benchmark reveals that while GenAI models can match many statistical properties, they still struggle with specific conditional distributions and long-horizon stability. The paper provides open-source code and generated data, establishing a new standard for evaluating synthetic financial data generation.

## QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, factor modeling, equities, china market, us equities, multi-agent systems, backtesting, reinforcement learning, ohlc data, backtest, information ratio, drawdown, portfolio returns, framework, trading agent, overfitting, look-ahead bias, evolutionary optimization, symbolic regression, regime shift robustness
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data"], "deliverable": ["framework", "trading agent"], "evaluation": ["backtest", "information ratio", "drawdown", "portfolio returns"], "market_context": ["china market", "us equities"], "method": ["multi-agent systems", "backtesting", "reinforcement learning"], "risk_issue": ["overfitting", "look-ahead bias"], "task": ["alpha mining", "factor modeling"]}
- One-line summary: QuantaAlpha is an evolutionary multi-agent framework for alpha mining that improves factor discovery through trajectory-level mutation and crossover, achieving superior predictive power and cross-market robustness compared to existing LLM-based agents.

### Detailed Summary

Financial alpha mining is hindered by market non-stationarity and noisy backtest feedback, which often cause LLM-based agents to drift into spurious correlations or local optima. QuantaAlpha addresses this by treating each mining run as a trajectory and applying evolutionary operators to refine factors systematically. The framework enforces semantic consistency between hypotheses, symbolic expressions, and code, while constraining complexity to prevent crowding. This approach aims to provide controllable, traceable, and robust factor discovery that adapts to regime shifts.

The method employs a multi-agent system for hypothesis generation, symbolic factor construction, and backtesting. Evolution occurs via mutation, which localizes and rewrites suboptimal trajectory segments, and crossover, which recombines high-reward segments from parent trajectories. Experiments on the CSI 300 dataset (2016-2025) compare QuantaAlpha against traditional ML, deep learning, and other LLM agents like AlphaAgent and RD-Agent. The system uses GPT-5.2 as the backbone and evaluates factors using Information Coefficient (IC) and strategy metrics like Annualized Return (ARR) and Maximum Drawdown (MDD). Cross-market transfer to CSI 500 and S&P 500 is also tested.

QuantaAlpha achieves an IC of 0.0472 and ARR of 4.68% on CSI 300, outperforming baselines. Ablation studies confirm that mutation drives exploration while crossover aids reuse. The framework demonstrates strong robustness during the 2023 market regime shift, maintaining performance where baselines failed due to alpha decay. Factors mined on CSI 300 transfer effectively to CSI 500 and S&P 500, yielding significant cumulative excess returns. Limitations include the need for transaction cost modeling in live deployment and potential diminishing returns after ~15 iterations.

## AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution

- Year: 2026
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: alpha mining, factor modeling, equities, china market, agentic workflow, multi-agent systems, retrieval, backtesting, market prices, ohlc data, sharpe ratio, backtest, drawdown, framework, open source, dag-based evolution, bayesian factor retriever, dag-aware llm generator, csi 300, csi 500
- Tag facets: {"asset_class": ["equities"], "data_source": ["market prices", "ohlc data"], "deliverable": ["framework", "open source"], "evaluation": ["sharpe ratio", "backtest", "drawdown"], "market_context": ["china market"], "method": ["agentic workflow", "multi-agent systems", "retrieval", "backtesting"], "risk_issue": [], "task": ["alpha mining", "factor modeling"]}
- One-line summary: AlphaPROBE introduces a DAG-based framework for alpha mining that uses a Bayesian Factor Retriever and a DAG-aware LLM generator to discover diverse, high-performing factors on Chinese stock markets.

### Detailed Summary

AlphaPROBE addresses the limitations of existing automated alpha mining methods, which typically treat factor discovery as either isolated generation events or local iterative refinements. These approaches lack a global structural view, leading to redundant searches and limited diversity in the factor pool. The paper reframes alpha mining as the strategic navigation of a Directed Acyclic Graph (DAG), where factors are nodes and evolutionary links are edges. This topological perspective allows the system to treat the factor pool as a dynamic, interconnected ecosystem rather than a static collection, enabling more efficient and robust discovery of predictive signals.

The framework consists of two core components: a Bayesian Factor Retriever and a DAG-aware Factor Generator. The Retriever balances exploitation and exploration by calculating a posterior probability for each factor, considering its quality, depth in the graph, and retrieval frequency, while also assessing its potential contribution to the pool's diversity. The Generator uses an LLM-based multi-agent workflow (Analyst, Execution, Validator) that leverages the full ancestral trace of selected parent factors to produce context-aware, non-redundant optimizations. Experiments are conducted on three major Chinese stock market datasets (CSI 300, 500, 1000) using Deepseek V3.1 as the backbone LLM, comparing AlphaPROBE against eight baselines including expert-designed factors, reinforcement learning methods, and other LLM-based agents.

Results demonstrate that AlphaPROBE significantly outperforms baselines in predictive accuracy (IC, RIC) and portfolio construction metrics (Sharpe Ratio, Maximum Drawdown) across all three datasets. The method shows enhanced stability against market regime shifts and faster convergence during training. Ablation studies confirm the necessity of the Bayesian retrieval mechanism and the DAG-aware generation process. The paper highlights that leveraging global evolutionary topology is essential for efficient alpha discovery, reducing redundant mutations and encouraging diverse factor expressions. The implementation is open-sourced, providing a reproducible pipeline for automated factor mining.

## FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: alpha mining, factor modeling, portfolio optimization, equities, china market, a-share market, agentic workflow, multi-agent systems, chain of thought, backtesting, ohlc data, annual reports, sharpe ratio, backtest, transaction costs, drawdown, framework, open source, data leakage, overfitting
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "annual reports"], "deliverable": ["framework", "open source"], "evaluation": ["sharpe ratio", "backtest", "transaction costs", "drawdown"], "market_context": ["china market", "a-share market"], "method": ["agentic workflow", "multi-agent systems", "chain of thought", "backtesting"], "risk_issue": ["data leakage", "overfitting"], "task": ["alpha mining", "factor modeling", "portfolio optimization"]}
- One-line summary: FactorEngine introduces a program-level factor mining framework that combines LLM-guided macro-evolution with Bayesian micro-optimization to discover executable, interpretable alpha factors from OHLCV data and financial reports, achieving state-of-the-art predictive and portfolio performance on Chinese A-share markets.

### Detailed Summary

The paper addresses the limitations of existing alpha mining methods, which suffer from bounded expressiveness in symbolic approaches or poor interpretability and overfitting in neural models. FactorEngine (FE) casts factors as Turing-complete Python programs, enabling complex control flows and higher-order feature interactions. The framework introduces three key separations to improve efficiency: logic revision versus parameter optimization, LLM-guided directional search versus Bayesian hyperparameter search, and LLM usage versus local computation. This allows the system to scale effectively while maintaining the interpretability required for auditable quantitative strategies.

The methodology comprises a bootstrapping module that transforms unstructured financial reports into executable factors via a closed-loop multi-agent pipeline, and an evolution module that performs macro-micro co-evolution. The macro level uses LLM agents to propose structural mutations guided by a chain of experience, while the micro level employs Bayesian optimization for parameter tuning. Experiments are conducted on CSI300 and CSI500 indices using OHLCV data from 2017 to 2024, comparing FE against baselines like Alpha158, GPlearn, AlphaAgent, and RD-Agent. The evaluation includes predictive metrics (IC, ICIR) and portfolio performance (AR, Sharpe, MDD) under realistic trading constraints including transaction costs and liquidity limits.

Results show that FE significantly outperforms baselines, with FE-report achieving a 58% improvement in IC and a 126% increase in annual excess return compared to Alpha158. The framework demonstrates superior predictive stability and portfolio impact, particularly in the CSI500 market. However, the study acknowledges that modern LLMs may have been trained on data extending beyond the test period, a common limitation in agent-based methods. Additionally, the performance gains are contingent on the quality of the initial knowledge infusion and the computational resources required for the multi-agent evolution process.

## TradeFM: A Generative Foundation Model for Trade-flow and Market Microstructure

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Market Microstructure, Execution, and Prediction Markets
- Evidence type: infrastructure
- Summary coverage: first_50k_chars
- Tags: market simulation, execution analysis, equities, market microstructure, high-frequency trading, time-series modeling, reinforcement learning, limit order book, backtest, market impact, model, simulator, model risk, generative foundation model, zero-shot generalization, synthetic data generation, trade event streams
- Tag facets: {"asset_class": ["equities"], "data_source": ["limit order book"], "deliverable": ["model", "simulator"], "evaluation": ["backtest", "market impact"], "market_context": ["market microstructure", "high-frequency trading"], "method": ["time-series modeling", "reinforcement learning"], "risk_issue": ["model risk"], "task": ["market simulation", "execution analysis"]}
- One-line summary: TradeFM is a 524M-parameter generative Transformer that learns universal market microstructure dynamics from billions of trade events across >9K equities, achieving 2-3x lower distributional error than Hawkes baselines and zero-shot generalization to APAC markets.

### Detailed Summary

TradeFM addresses the challenge of modeling heterogeneous, high-frequency market microstructure by introducing a generative foundation model that learns directly from raw, partially observed trade event streams rather than full limit order book snapshots. The research problem centers on whether a single model can capture universal principles of price formation across diverse assets and liquidity regimes without asset-specific calibration, leveraging the hypothesis that scale-invariant representations exist in order flow. The authors propose a decoder-only Transformer architecture trained on over 10 billion tokens from US equities, utilizing a novel universal tokenization scheme and scale-invariant feature engineering to map multi-modal event data into a unified discrete sequence. This approach eliminates the need for privileged full-LOB access, aligning the model with the information available to typical market participants.

The experimental design integrates the pre-trained model with a deterministic market simulator to create a closed-loop evaluation environment. Key experiments assess the model's ability to reproduce stylized facts of financial returns, such as heavy tails, volatility clustering, and lack of return autocorrelation, while also measuring distributional fidelity against baselines like Zero-Intelligence agents and Compound Hawkes processes. The study further evaluates out-of-distribution generalization by testing the model on held-out temporal periods and geographically distinct APAC markets (China and Japan) without fine-tuning. Metrics include Kolmogorov-Smirnov and Wasserstein distances for return distributions and order flow statistics, alongside perplexity measures for cross-market transfer.

Findings indicate that TradeFM significantly outperforms traditional stochastic baselines, achieving 2-3x lower distributional error in reproducing stylized facts and superior fidelity in order volume and interarrival time distributions. The model demonstrates robust zero-shot generalization to APAC markets with only moderate perplexity degradation, confirming the transferability of scale-invariant trade representations. Limitations include the model's inability to perfectly replicate bid-ask spreads compared to Hawkes processes and the reliance on a deterministic simulator that may not capture all real-world execution frictions. Use cases include synthetic data generation for illiquid assets, stress testing via counterfactual scenario injection, and providing a realistic environment for training reinforcement learning agents for optimal execution.

## Strategic Complexity and Behavioral Distortion: Retail Investing Under Large Language Model Augmentation

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: conceptual
- Summary coverage: first_50k_chars
- Tags: risk extraction, sentiment analysis, equities, options, derivatives, retail investing, agent debate, framework, bias, model risk, behavioral finance, cognitive bias, overconfidence, investor protection
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": [], "deliverable": ["framework"], "evaluation": [], "market_context": ["retail investing"], "method": ["agent debate"], "risk_issue": ["bias", "model risk"], "task": ["risk extraction", "sentiment analysis"]}
- One-line summary: This conceptual paper introduces Perceived Cognitive Assistance (PCA) to explain how LLMs alter retail investors' strategy selection and risk posture, proposing a moderated regression model and a Behavioral Shift Index (BSI) for future empirical validation.

### Detailed Summary

The paper addresses the behavioral gap in retail investing where Large Language Models (LLMs) lower cognitive barriers to complex strategies, potentially causing an 'illusion of understanding.' It introduces Perceived Cognitive Assistance (PCA) as a psychological construct where investors feel enhanced capability to execute institutional-grade strategies without adequate comprehension. The authors argue this empowerment-distortion duality can lead to behavioral distortion, overconfidence, and emergent market-level risks like algorithmic coherence and volatility amplification among retail cohorts.

Methodologically, the paper is conceptual and proposes a five-step research agenda rather than reporting empirical results. It extends the Theory of Planned Behavior (TPB) by integrating the Technology Acceptance Model (TAM) and Risk-as-Feelings Theory. The core methodological contributions are two estimators: Equation (1), a moderated regression linking LLM engagement, PCA, and behavioral outcomes, and Equation (2), a composite Behavioral Shift Index (BSI) derived from trading logs to measure shifts in strategy complexity. The paper also outlines a dual-agent simulation framework using a 'Virtual Trader' (bounded cognition) and a 'Digital Persona' (behaviorally plausible logic) for causal benchmarking in future studies.

The findings are theoretical predictions rather than empirical results. The authors posit that PCA moderates the relationship between LLM use and complex strategy adoption, with positive interaction effects expected. Limitations include the lack of current empirical data, the reliance on future preregistered studies, and the challenge of isolating LLM effects from other market factors. The paper serves as a foundational framework for measuring cognitive shifts in AI-augmented retail trading, highlighting the need for investor protection policies and platform design changes to mitigate behavioral risks.

## Cognitive Alpha Mining via LLM-Driven Code-Based Evolution

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: alpha mining, stock prediction, factor modeling, equities, us equities, china market, agentic workflow, multi-agent systems, fine-tuning, ohlc data, information ratio, ablation study, framework, open source, overfitting, cognitive alpha, evolutionary search, interpretable factors, global stock markets
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data"], "deliverable": ["framework", "open source"], "evaluation": ["information ratio", "ablation study"], "market_context": ["us equities", "china market"], "method": ["agentic workflow", "multi-agent systems", "fine-tuning"], "risk_issue": ["overfitting"], "task": ["alpha mining", "stock prediction", "factor modeling"]}
- One-line summary: The CogAlpha framework leverages a seven-level agent hierarchy and LLM-driven evolutionary search to discover interpretable, robust alpha factors that outperform traditional machine learning and existing LLM-based baselines across multiple global stock markets.

### Detailed Summary

The paper addresses the challenge of discovering robust, interpretable alpha factors in high-dimensional financial data, where existing neural and symbolic methods suffer from opacity, fragility, or poor generalization. The authors propose CogAlpha, a framework that treats LLMs as adaptive cognitive agents to perform structured, human-like exploration of the alpha search space, balancing logical consistency with creative innovation. This approach aims to move beyond shallow pattern replication toward deeper reasoning and economically grounded factor discovery.

CogAlpha employs a seven-level agent hierarchy to generate initial alpha candidates from OHLCV data, covering domains from market cycles to geometric fusion. A multi-agent quality checker validates code syntax, logic, and economic meaning, while a fitness evaluation filters candidates using IC, RankIC, and other metrics. The core innovation is the 'Thinking Evolution' module, which uses LLM-driven mutation and crossover operations to iteratively refine qualified alphas. Experiments on five datasets from China, the US, and HK markets demonstrate that CogAlpha consistently discovers alphas with superior predictive accuracy and robustness compared to 21 baselines, including deep learning models and other LLM-based methods.

The framework achieves state-of-the-art performance, with CogAlpha-generated alphas showing significantly higher IC and RankIC values than baselines like LightGBM and Alpha158. The generated factors are accompanied by detailed comments and code, ensuring interpretability and economic grounding. However, the method relies heavily on the reasoning capabilities of large LLMs, which may incur high computational costs. The study also notes that while generalization is strong across markets, the specific performance may vary with different prediction horizons and training methods, suggesting potential sensitivity to market regime shifts.

## AlphaCrafter: A Full-Stack Multi-Agent Framework for Cross-Sectional Quantitative Trading

- Year: 2026
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Alpha Mining and Factor Discovery
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: alpha mining, portfolio optimization, factor modeling, equities, cross-sectional equities, us equities, china market, multi-agent systems, agentic workflow, backtesting, ohlc data, financial statements, news, sharpe ratio, backtest, drawdown, portfolio returns, framework, trading agent, overfitting
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "financial statements", "news"], "deliverable": ["framework", "trading agent"], "evaluation": ["sharpe ratio", "backtest", "drawdown", "portfolio returns"], "market_context": ["cross-sectional equities", "us equities", "china market"], "method": ["multi-agent systems", "agentic workflow", "backtesting"], "risk_issue": ["overfitting", "look-ahead bias"], "task": ["alpha mining", "portfolio optimization", "factor modeling"]}
- One-line summary: AlphaCrafter is a full-stack multi-agent framework that unifies LLM-driven factor discovery, regime-adaptive selection, and risk-constrained execution, demonstrating robust live trading performance on CSI 300 and S&P 500 indices by outperforming static and decoupled baselines.

### Detailed Summary

Financial quantitative trading faces significant challenges due to market non-stationarity and the rapid decay of alpha signals. Traditional approaches often decouple factor discovery from execution or rely on static factor sets that fail to adapt to shifting macroeconomic regimes. AlphaCrafter addresses this fragmentation by introducing a closed-loop, fully automated pipeline that continuously adapts to evolving market dynamics without manual intervention. The framework is designed to maintain predictive power and risk-adjusted returns in non-stationary environments by integrating three specialized agents that operate in a coordinated daily rotation, ensuring that signal generation, selection, and execution are holistically aligned with current market conditions.

The system comprises three distinct agents: a Miner, a Screener, and a Trader. The Miner utilizes LLM-guided search to autonomously generate, validate, and maintain a dynamic factor library, pruning ineffective signals to prevent alpha decay. The Screener assesses prevailing market regimes—such as trend direction, volatility, and liquidity—and constructs a regime-conditioned factor ensemble by selecting and weighting factors based on their suitability for the current environment. The Trader then translates this ensemble into executable quantitative strategies, optimizing portfolio construction and risk constraints through hyperparameter tuning and backtesting. Experiments were conducted on the CSI 300 and S&P 500 indices using daily-frequency data from 2016 to 2026, including price-volume, fundamental, and alternative data sources. The framework was evaluated against traditional technical strategies, machine learning models, deep learning architectures, and other LLM-based trading agents, using metrics such as Annualized Return, Sharpe Ratio, and Maximum Drawdown.

AlphaCrafter consistently outperformed state-of-the-art baselines in both backtesting and live trading phases, achieving the highest risk-adjusted returns and the lowest cross-trial variance. Notably, it was the only method to deliver positive live trading returns on both markets, whereas many baselines suffered from severe overfitting or regime sensitivity. The framework exhibited robust stability across different backbone LLMs and demonstrated superior factor longevity compared to static factor sets. However, the study acknowledges limitations related to the daily trading frequency, which may not capture high-frequency microstructure effects, and the potential for LLM inference latency in real-time deployment. The results confirm that an integrated, adaptive factor-to-execution design yields more reliable and robust trading performance than decoupled or static approaches.

## Taxonomy-Aligned Risk Extraction from 10-K Filings

- Year: 2026
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: case study
- Summary coverage: first_50k_chars
- Tags: risk extraction, xbrl tagging, equities, us equities, retrieval, agentic workflow, 10-k filings, sec filings, accuracy, taxonomy, dataset, hallucination, taxonomy alignment, embedding-based mapping, llm-as-a-judge, autonomous refinement
- Tag facets: {"asset_class": ["equities"], "data_source": ["10-k filings", "sec filings"], "deliverable": ["taxonomy", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["retrieval", "agentic workflow"], "risk_issue": ["hallucination"], "task": ["risk extraction", "xbrl tagging"]}
- One-line summary: This paper presents a three-stage pipeline combining LLM extraction, embedding-based mapping, and LLM-as-a-judge validation to extract structured risk factors from 10-K filings into a hierarchical taxonomy, demonstrating autonomous taxonomy refinement and strong industry clustering validity.

### Detailed Summary

The paper addresses the challenge of extracting structured, taxonomy-aligned risk factors from unstructured 10-K filings, where naive LLM outputs produce inconsistent labels. The authors propose a three-stage pipeline: first, an LLM extracts free-form risk factors with supporting quotes; second, embedding-based semantic similarity maps these quotes to a predefined three-tier hierarchical taxonomy; and third, an LLM-as-a-judge validates mappings, filtering spurious assignments based on quality scores. This hybrid approach balances the nuance of LLMs with the consistency of fixed categories, ensuring high-precision extraction while maintaining computational efficiency through local embedding models.

The methodology is evaluated on 2024 10-K filings for S&P 500 companies, extracting 10,688 validated risk factors. The study introduces an autonomous taxonomy maintenance system where an AI agent analyzes low-quality validation feedback to diagnose failure patterns and propose description refinements, achieving a 104.7% improvement in embedding separation for a pharmaceutical approval category. External validation uses inverse prevalence weighting to compute risk profile similarity, testing whether same-industry companies exhibit higher similarity than cross-industry pairs without using industry codes as input features.

Results show that same-industry companies have 63% higher risk profile similarity than cross-industry pairs, with Cohen’s d=1.06 and AUCs ranging from 0.733 to 0.822 for predicting industry membership at varying SIC granularities. Sector-specific analysis reveals intuitive patterns, such as 83% of banks tagged with interest rate risk versus 22% of all companies. Limitations include API costs and latency for real-time applications, the need for upfront domain expertise in taxonomy design, and the current focus on English-language filings, though the methodology is theoretically language-agnostic.

## The Wall Street Neophyte: A Zero-Shot Analysis of ChatGPT over Multimodal Stock Movement Prediction Challenges

- Year: 2023
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Stock Prediction and Market Forecasting
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: stock prediction, sentiment analysis, equities, us equities, chain of thought, prompt engineering, multimodal modeling, ohlc data, social media, accuracy, ablation study, benchmark, hallucination, zero-shot, explainability, reasoning stability
- Tag facets: {"asset_class": ["equities"], "data_source": ["ohlc data", "social media"], "deliverable": ["benchmark"], "evaluation": ["accuracy", "ablation study"], "market_context": ["us equities"], "method": ["chain of thought", "prompt engineering", "multimodal modeling"], "risk_issue": ["hallucination"], "task": ["stock prediction", "sentiment analysis"]}
- One-line summary: This paper evaluates ChatGPT's zero-shot capability in multimodal stock movement prediction, finding it underperforms traditional baselines and specialized deep learning models despite the utility of tweet data, while highlighting its limitations in reasoning stability and explainability.

### Detailed Summary

This study addresses the gap in understanding how large language models perform in financial forecasting tasks without fine-tuning. Specifically, it investigates whether ChatGPT can effectively predict binary stock price movements (rise or fall) by integrating historical price features with social media sentiment from tweets. The research positions ChatGPT as a 'Wall Street Neophyte,' aiming to determine if its general language understanding translates to accurate market prediction or if it lacks the specialized reasoning required for complex financial time-series analysis. The work challenges the assumption that zero-shot LLMs can immediately replace specialized financial models in high-stakes prediction environments.

The authors conduct a comprehensive zero-shot analysis using three benchmark datasets: BIGDATA22, ACL18, and CIKM18, which contain high-trade-volume US stocks, historical price features, and associated tweets. They compare ChatGPT against strong baselines including Logistic Regression, Random Forest, LSTM, and state-of-the-art multimodal models like SLOT and DTML. The experimental design tests vanilla zero-shot prompting and Chain-of-Thought (CoT) strategies to see if structured reasoning improves accuracy. Metrics include Accuracy and Matthews Correlation Coefficient (MCC). The study also performs ablation studies to isolate the impact of tweet inclusion and analyzes the quality of the model's generated explanations through case studies.

Results show that ChatGPT generally underperforms both traditional statistical methods and advanced deep learning models, often failing to beat simple linear regression baselines. While incorporating tweets provides a positive, albeit modest, boost in performance, the model struggles to effectively fuse multimodal information. CoT prompting offers limited improvement in accuracy but provides some interpretability, though the explanations are often superficial and prone to hallucination or incorrect sentiment alignment. The paper concludes that ChatGPT lacks the stability and precision for direct trading applications without specialized training, highlighting significant limitations in handling long-tail stock distributions and complex market dynamics.


## Revolutionizing Finance with LLMs: An Overview of Applications and Insights

- Year: 2024
- Category: Surveys and Reviews
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, portfolio optimization, alpha mining, forecasting, financial question answering, factor modeling, news, accuracy, taxonomy, literature review, hallucination, robo-advisory, m a forecasting, insolvency prediction, financial engineering
- Tag facets: {"asset_class": [], "data_source": ["news"], "deliverable": ["taxonomy", "literature review"], "evaluation": ["accuracy"], "market_context": [], "method": [], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "portfolio optimization", "alpha mining", "forecasting", "financial question answering", "factor modeling"]}
- One-line summary: This survey reviews the integration of Large Language Models into finance, categorizing applications into engineering, forecasting, risk management, and QA, while empirically evaluating GPT-4's ability to follow instructions across these diverse financial tasks.

### Detailed Summary

This paper addresses the growing intersection of Large Language Models (LLMs) and the financial sector, aiming to synthesize existing literature and evaluate practical utility. It positions LLMs as transformative tools capable of processing unstructured data to enhance decision-making, risk assessment, and operational efficiency. The authors identify key challenges, including the need for domain-specific comprehension, high accuracy in high-stakes decisions, and the integration of specialized financial knowledge with general language capabilities. The work serves as a foundational survey for researchers and practitioners, mapping the current landscape of LLM applications in finance.

The methodology involves a comprehensive literature review categorized into four main areas: financial engineering, financial forecasting, financial risk management, and real-time question answering. The authors also conduct holistic empirical tests on GPT-4 using natural language instructions across these tasks. The paper details technical approaches such as Named Entity Recognition (NER), sentiment analysis, and time series forecasting adaptations for LLMs. It explores specific use cases like quantitative trading, portfolio optimization, robo-advisory services, M&A forecasting, and insolvency prediction, drawing on both traditional statistical methods and emerging deep learning techniques.

Findings indicate that GPT-4 effectively follows prompt instructions across various financial tasks, demonstrating strong potential for automating report generation, sentiment analysis, and complex reasoning. The paper highlights the synergy between quantitative models and qualitative insights from LLMs, particularly in portfolio optimization and alpha mining. However, it notes limitations in current robo-advisory personalization and the challenges of ensuring reliability and interpretability in high-risk financial decisions. The survey concludes by identifying unresolved issues and future research directions, emphasizing the need for robust evaluation benchmarks and domain-specific fine-tuning to fully realize LLMs' potential in finance.

## WWW'18 Open Challenge: Financial Opinion Mining and Question Answering

- Year: 2018
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: sentiment analysis, financial question answering, retrieval, news, social media, accuracy, backtest, benchmark, dataset, aspect-based sentiment, opinion mining, stack exchange, knowledge base
- Tag facets: {"asset_class": [], "data_source": ["news", "social media"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy", "backtest"], "market_context": [], "method": ["retrieval"], "risk_issue": [], "task": ["sentiment analysis", "financial question answering"]}
- One-line summary: The WWW'18 Open Challenge established benchmarks for aspect-based financial sentiment analysis and opinion-based question answering, revealing that while sentiment prediction is feasible, aspect classification and opinion QA remain difficult tasks with limited performance.

### Detailed Summary

This paper introduces the WWW'18 Open Challenge, designed to advance Natural Language Processing techniques for the financial domain by focusing on two specific tasks: aspect-based financial sentiment analysis and opinion-based question answering. The motivation stems from the need for fine-grained models that can capture the semantic complexity of financial language, moving beyond document-level sentiment to target specific aspects and entities within unstructured data like news headlines and microblogs. The challenge aimed to catalyze research by providing standardized datasets and evaluation metrics for these under-explored areas, fostering dialogue between academia and industry regarding the automatic analysis of financial opinions.

The challenge comprised two tasks. Task 1 involved predicting sentiment scores (-1 to 1) for pre-defined aspect categories in financial news headlines and microblogs, using datasets of 529 headlines and 774 posts. Task 2 required building a QA system over a knowledge base of 57,640 Stack Exchange posts to answer natural language questions, including opinionated queries targeting specific entities and sentiments. Evaluation metrics included regression measures (MSE, R2, Cosine) for sentiment, classification metrics (Accuracy, F1) for aspect categories, and ranking metrics (nDCG, MRR) for QA. Participating teams submitted models for these tasks, with results reported in tables showing performance across different systems.

Results indicated significant challenges in the domain. For sentiment prediction, models achieved moderate correlation (Cosine ~0.6) but struggled with aspect classification, with F1-scores often below 0.5. The best QA system achieved an nDCG@10 of 0.3052, highlighting the difficulty of retrieving relevant opinionated answers. The paper concludes that while sentiment score prediction is relatively more tractable, aspect-based classification and opinion QA require more sophisticated semantic understanding. The challenge provided valuable baseline data and highlighted the gap between general NLP capabilities and the specific demands of financial opinion mining, serving as a foundational resource for subsequent research in financial text analysis.

## FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: full_extracted_text
- Tags: algorithmic trading, stock prediction, spreadsheet reasoning, equities, crypto, us equities, fine-tuning, reinforcement learning, prompt engineering, market prices, tables, sharpe ratio, portfolio returns, backtest, framework, model, overfitting, tail risk, parameter-efficient fine-tuning, ppo
- Tag facets: {"asset_class": ["equities", "crypto"], "data_source": ["market prices", "tables"], "deliverable": ["framework", "model"], "evaluation": ["sharpe ratio", "portfolio returns", "backtest"], "market_context": ["us equities"], "method": ["fine-tuning", "reinforcement learning", "prompt engineering"], "risk_issue": ["overfitting", "tail risk"], "task": ["algorithmic trading", "stock prediction", "spreadsheet reasoning"]}
- One-line summary: FLAG-Trader integrates a partially fine-tuned LLM with Proximal Policy Optimization to enable a small 135M-parameter model to outperform larger proprietary models in single-asset stock and crypto trading.

### Detailed Summary

The paper addresses the limitation of LLMs in sequential financial decision-making by proposing FLAG-Trader, a framework that treats a partially fine-tuned LLM as a policy network within a reinforcement learning setup. It converts market states into structured text prompts, allowing the LLM to leverage pre-trained reasoning capabilities while adapting to financial domains through parameter-efficient fine-tuning of only the top layers. This hybrid approach aims to combine the multimodal understanding of LLMs with the reward-driven optimization of RL, overcoming the static nature of standard LLM inference and the feature-engineering burden of traditional RL.

The method employs an actor-critic architecture where the policy and value networks share trainable LLM layers while keeping base layers frozen. Training utilizes Proximal Policy Optimization (PPO) with a reward function based on the Sharpe ratio of cumulative profits. Experiments evaluate the model on five US stocks (MSFT, JNJ, UVV, HON, TSLA) and Bitcoin, comparing it against buy-and-hold, LLM-agentic baselines (InvestorBench), and various large proprietary and open-source models. The 135M-parameter SmolLM2 backbone is fine-tuned using structured prompts containing price history, account status, and recent decision metrics.

Results show FLAG-Trader consistently outperforms baselines in Cumulative Return and Sharpe Ratio, notably enabling the small open-source model to surpass larger proprietary models like GPT-4 and GPT-o1-preview in several assets. The framework demonstrates convergence to stable policies and robustness across different market conditions. However, limitations include high computational costs during fine-tuning, potential biases from structured prompts, and a lack of explicit risk-sensitive constraints beyond Sharpe ratio optimization, which may limit generalization in highly volatile or non-stationary markets.

## RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?

- Year: 2026
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, financial question answering, equities, options, derivatives, institutional investing, sec filings, accuracy, benchmark, dataset, hallucination, epistemic caution, missing premises, bilingual evaluation, cfa, cpa
- Tag facets: {"asset_class": ["equities", "options", "derivatives"], "data_source": ["sec filings"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["institutional investing"], "method": [], "risk_issue": ["hallucination"], "task": ["benchmarking", "financial question answering"]}
- One-line summary: RealFin introduces a bilingual benchmark evaluating LLMs' ability to detect under-specified financial questions, revealing that general models over-commit to guesses while finance-specialized models fail to identify missing premises.

### Detailed Summary

The paper addresses the critical gap in financial LLM evaluation by introducing RealFin, a benchmark designed to test whether models can recognize when a question lacks sufficient information for a justified answer. Unlike traditional benchmarks that assume a closed-world setting with complete premises, RealFin systematically removes essential assumptions from professional exam-style questions in English (CFA) and Chinese (CPA), creating underdetermined problems that appear linguistically plausible but are logically unsolvable without clarification. This approach targets the real-world scenario where users leave implicit assumptions unstated, requiring models to exhibit epistemic caution rather than blind computation.

The dataset comprises 2,020 paired questions, including full-condition and condition-missing variants, covering six reasoning types and multiple financial sub-domains. The authors evaluate 15 LLMs, including general-purpose, finance-specialized, and reasoning-enhanced models, using three formulations: standard answering, recognizing missing information, and a None-of-the-Above (NOTA) setting to force genuine inference. Experiments are conducted in a zero-shot setting with greedy decoding, measuring accuracy and confidence scores to assess both answer correctness and the model's ability to identify logical underdetermination.

Results show that general-purpose models often improve in accuracy on missing-condition questions by implicitly filling in gaps with learned defaults, leading to high confidence but low reasoning accuracy. In contrast, finance-specialized models frequently fail to answer even full-condition questions in Chinese due to rigid rule-matching, while reasoning-enhanced models show mixed results. The NOTA evaluation reveals a significant gap between answer accuracy and reasoning accuracy, indicating that many correct answers are driven by pattern recognition rather than true logical deduction. The study highlights a structural failure in current LLMs to withhold commitment when information is insufficient, a key requirement for reliable financial reasoning.

## HedgeAgents: A Balanced-aware Multi-agent Financial Trading System

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: portfolio optimization, derivatives hedging, strategy generation, spreadsheet reasoning, crypto, equities, forex, portfolio management, high-frequency trading, multi-agent systems, reinforcement learning, tool use, retrieval, market prices, news, tables, sharpe ratio, drawdown, portfolio returns, ablation study
- Tag facets: {"asset_class": ["crypto", "equities", "forex"], "data_source": ["market prices", "news", "tables"], "deliverable": ["framework", "trading agent"], "evaluation": ["sharpe ratio", "drawdown", "portfolio returns", "ablation study"], "market_context": ["portfolio management", "high-frequency trading"], "method": ["multi-agent systems", "reinforcement learning", "tool use", "retrieval"], "risk_issue": ["data leakage", "model risk"], "task": ["portfolio optimization", "derivatives hedging", "strategy generation", "spreadsheet reasoning"]}
- One-line summary: HedgeAgents is a multi-agent system using LLMs to coordinate specialized asset experts and a fund manager through hedging conferences, achieving 400% total return and superior risk management across Bitcoin, stocks, and forex compared to baselines.

### Detailed Summary

The paper addresses the fragility of existing LLM-based trading agents, which suffer significant losses during market volatility, by introducing HedgeAgents, a multi-agent framework designed for robust hedging. The system mimics a hedge fund structure with a central fund manager and specialized experts for Bitcoin, stocks, and forex. These agents utilize LLMs for cognitive processing, employing a reflection-driven decision-making pipeline that integrates memory retrieval, reinforcement learning-based action selection, and self-reflection updates. The core innovation lies in three coordination mechanisms: Budget Allocation Conferences for periodic portfolio rebalancing, Experience Sharing Conferences for knowledge accumulation, and Extreme Market Conferences for emergency risk mitigation during high volatility.

Experiments were conducted on a dataset spanning 2015-2023, comprising daily prices, volumes, and news for Bitcoin, DJIA components, and forex pairs. The testing period (2021-2023) evaluated performance against rule-based, reinforcement learning, and other LLM-based baselines using metrics like Total Return, Sharpe Ratio, and Maximum Drawdown. The system achieved a 70% annualized return and 400% total return over three years, significantly outperforming state-of-the-art models. Ablation studies confirmed the necessity of all three conference types, with the Extreme Market Conference crucial for limiting drawdowns. The framework also demonstrated robustness across different LLM backbones, with GPT-4 yielding the best results, while maintaining low operational costs.

HedgeAgents excels in risk-adjusted returns, achieving the lowest Maximum Drawdown (14.21%) and highest diversification metrics among all tested models. It effectively navigates extreme market conditions, such as the May 2022 downturn, where baselines failed. The system generates interpretable investment experiences stored in memory, comparable to human expert insights. However, limitations include reliance on specific LLM capabilities, potential data leakage risks mitigated by temporal isolation tests, and the assumption that historical correlations hold. The system is primarily a proof-of-concept for multi-agent coordination in finance, with real-world deployment caveats regarding transaction costs and slippage not fully modeled.

## Trade in Minutes! Rationality-Driven Agentic System for Quantitative Financial Trading

- Year: 2025
- Category: Agents and Multi-Agent Systems
- Trading subtheme: Trading Agents and Strategy Generation
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: algorithmic trading, strategy generation, portfolio optimization, crypto, derivatives, high-frequency trading, us equities, multi-agent systems, agentic workflow, backtesting, reinforcement learning, tool use, market prices, ohlc data, backtest, sharpe ratio, drawdown, portfolio returns, framework, dataset
- Tag facets: {"asset_class": ["crypto", "derivatives"], "data_source": ["market prices", "ohlc data"], "deliverable": ["framework", "dataset", "open source", "trading agent"], "evaluation": ["backtest", "sharpe ratio", "drawdown", "portfolio returns"], "market_context": ["high-frequency trading", "us equities"], "method": ["multi-agent systems", "agentic workflow", "backtesting", "reinforcement learning", "tool use"], "risk_issue": ["overfitting", "model risk"], "task": ["algorithmic trading", "strategy generation", "portfolio optimization"]}
- One-line summary: TiMi is a rationality-driven multi-agent system that decouples strategy development from minute-level deployment, achieving superior risk-adjusted returns and low latency across 200+ trading pairs by leveraging specialized LLMs for semantic analysis, code generation, and mathematical optimization.

### Detailed Summary

The paper addresses the limitations of existing LLM-based financial agents, which often suffer from emotional biases, reliance on noisy peripheral data, and high inference latency due to continuous multi-agent reasoning. The authors propose TiMi, a system that harmonizes strategic depth with mechanical rationality by architecturally decoupling the offline policy and optimization stages from the online deployment stage. This design allows for complex, time-consuming reasoning to occur offline, while the live deployment relies on lightweight, pre-compiled trading bots, ensuring minute-level execution efficiency.

TiMi employs a multi-agent architecture comprising a macro analysis agent for pattern recognition, a strategy adaptation agent for pair-specific customization, a bot evolution agent for code generation, and a feedback reflection agent for mathematical optimization. The system utilizes specialized LLMs: DeepSeek-V3 for semantic analysis, Qwen2.5-Coder for programming, and DeepSeek-R1 for mathematical reasoning. Strategies are transformed into layered trading bots (strategy, function, parameter levels) and optimized via closed-loop feedback where risk scenarios are formulated as linear programming problems to solve for optimal parameters. Experiments cover 200+ pairs in U.S. stock index futures and cryptocurrency markets, comparing against quantitative, ML/RL, and other LLM-agent baselines.

Empirical results demonstrate that TiMi achieves competitive Annual Rate of Return (ARR) and superior Sharpe ratios, particularly in volatile altcoin markets, while maintaining low action latency comparable to traditional quantitative methods. The decoupling mechanism significantly reduces computational costs during deployment. Limitations include the reliance on specific LLM capabilities for the offline stages and the potential for overfitting during the optimization phase if risk scenarios are not diverse enough. The system is most relevant for quantitative trading infrastructure rather than discretionary investment advice.

## FAMMA: A Benchmark for Financial Domain Multilingual Multimodal Question Answering

- Year: 2024
- Category: Financial QA, Reasoning, and Table Understanding
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: financial question answering, benchmarking, derivatives, equities, options, portfolio management, multimodal modeling, fine-tuning, prompt engineering, tables, financial statements, accuracy, benchmark, dataset, model, multilingual, reasoning trajectories, distillation, program of thoughts, budget forcing
- Tag facets: {"asset_class": ["derivatives", "equities", "options"], "data_source": ["tables", "financial statements"], "deliverable": ["benchmark", "dataset", "model"], "evaluation": ["accuracy"], "market_context": ["portfolio management"], "method": ["multimodal modeling", "fine-tuning", "prompt engineering"], "risk_issue": [], "task": ["financial question answering", "benchmarking"]}
- One-line summary: FAMMA is a multilingual, multimodal benchmark for advanced financial reasoning that reveals significant gaps in LLMs' domain knowledge and demonstrates that fine-tuning on distilled reasoning trajectories improves performance on unseen financial questions.

### Detailed Summary

This paper introduces FAMMA, an open-source benchmark designed to evaluate large language models on complex financial reasoning tasks that require specialized knowledge, calculation, and multimodal input. Unlike existing benchmarks that focus on rudimentary text-based questions, FAMMA covers eight major finance subfields (e.g., derivatives, portfolio management) and includes questions in English, Chinese, and French, featuring charts, tables, and diagrams. The benchmark consists of FAMMA-Basic (1,945 questions from textbooks/exams) and FAMMA-LivePro (103 novel, contamination-free questions created by domain experts), with difficulty levels aligned to CFA standards. The research addresses the scarcity of high-quality, challenging financial reasoning benchmarks that test both advanced domain knowledge and sophisticated calculation capabilities.

The authors constructed the dataset through a rigorous two-stage cleaning protocol and curated 1,273 reasoning trajectories from DeepSeek-R1 on FAMMA-Basic. They evaluated a suite of proprietary (GPT-o1, Claude, Gemini) and open-source (Qwen, DeepSeek-R1) models using zero-shot prompting, Program-of-Thoughts (PoT) for arithmetic, and Retrieval-Augmented Generation (RAG). Experiments included supervised fine-tuning of Qwen models on the distilled reasoning data and applying budget forcing at inference time. Evaluation metrics focused on Pass@1 accuracy across arithmetic vs. non-arithmetic questions, subfields, and languages, with GPT-4o used as a deterministic evaluator for open-ended responses.

Results show that even frontier models like GPT-o1 struggle significantly, solving only 30% of hard LivePro questions. PoT prompting drastically improves arithmetic performance but fails to address non-arithmetic bottlenecks, where domain knowledge gaps account for 75% of errors. RAG provided no significant gains for strong reasoning models, suggesting they already encode sufficient textbook knowledge. Fine-tuning open-source models on distilled reasoning trajectories yielded systematic improvements, particularly for larger models (32B), and budget forcing offered complementary gains. The study highlights that closing the gap in financial reasoning requires deeper domain expertise rather than just numerical tool use or retrieval.

## FinReasoning: A Hierarchical Benchmark for Reliable Financial Research Reporting

- Year: 2026
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, equity research, equities, a-share market, multi-agent systems, retrieval, sec filings, news, accuracy, benchmark, dataset, hallucination, financial research reporting, multi-agent role suitability, llm-as-a-judge, error injection, semantic consistency, data alignment
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "news"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": ["a-share market"], "method": ["multi-agent systems", "retrieval"], "risk_issue": ["hallucination"], "task": ["benchmarking", "equity research"]}
- One-line summary: FinReasoning introduces a hierarchical benchmark decomposing financial research into semantic consistency, data alignment, and deep insight, revealing that closed-source models outperform open-source and financial-domain models in multi-agent role suitability.

### Detailed Summary

The paper addresses the lack of granular evaluation for LLMs in financial research, where existing benchmarks collapse distinct reasoning stages into single scores, obscuring capability bottlenecks in multi-agent systems. FinReasoning decomposes financial reasoning into three tracks: Semantic Consistency (error detection/correction in long texts), Data Alignment (numerical verification and rule-based reasoning on structured data), and Deep Insight (research-grade analysis using a 12-indicator expert rubric). This hierarchical approach allows for precise diagnosis of model strengths and weaknesses across the analytical workflow, from proofreading to strategic synthesis.

The benchmark utilizes 4,800 samples derived from real-world financial literature, news, and A-share market data (2023-2025), constructed via error injection and expert-validated QA generation. The authors evaluate 19 LLMs, including closed-source, open-source general, and financial-domain models, using a hybrid evaluation framework combining objective metrics with a fused LLM-as-a-Judge protocol. Experiments assess error localization, calculation accuracy, and causal depth, with robustness checks confirming high inter-expert agreement and judge stability. The setup isolates performance across difficulty levels, from simple verification to complex multi-step reasoning.

Results show clear capability stratification: closed-source models like Doubao-Seed-1.8 and GPT-5 lead in overall performance and are best suited for core reasoning agents. Open-source general models (e.g., Qwen3-235B) underperform on Semantic Consistency, while financial-domain models (e.g., Fin-R1) lack foundational auditing skills despite moderate insight generation. A key finding is that reasoning-specialized models often fail on simple data retrieval tasks due to over-reasoning. The benchmark is deployed in pilot banking scenarios, highlighting its utility for system design, though limitations include potential judge bias and the specific focus on Chinese A-share data.

## Financial Numeric Extreme Labelling: A Dataset and Benchmarking for XBRL Tagging

- Year: 2023
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: xbrl tagging, fine-tuning, instruction tuning, 10-k filings, sec filings, xbrl, accuracy, benchmark, dataset, data leakage, extreme classification, sequence labeling, attentionxml, fnxl dataset, us-gaap
- Tag facets: {"asset_class": [], "data_source": ["10-k filings", "sec filings", "xbrl"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": ["fine-tuning", "instruction tuning"], "risk_issue": ["data leakage"], "task": ["xbrl tagging"]}
- One-line summary: The paper introduces the Financial Numeric Extreme Labelling (FNXL) dataset with 2,794 XBRL tags and benchmarks sequence labeling versus extreme classification pipelines, finding that while sequence labeling excels on frequent labels, the extreme classification pipeline better handles the long-tail distribution of rare accounting metrics.

### Detailed Summary

This paper addresses the challenge of automating the assignment of U.S. GAAP XBRL labels to numerals in SEC filings, a task requiring annotation from an extremely large label set of 2,794 tags. The authors formulate this as a financial numeric entity recognition problem, aiming to reduce the manual effort required for regulatory compliance and to enable the tagging of historical documents lacking XBRL metadata. The research positions itself against prior work like FiNER, which focused on only the top 139 frequent labels, arguing that real-world application requires handling the full long-tail distribution of accounting metrics.

The core contribution is the release of the FNXL dataset, derived from 10-K filings of 2,339 companies (2019-2021), containing 79,088 sentences and 142,922 annotated numerals. The authors benchmark two approaches: a sequence labeling method using FiNER (BERT-based) and a two-step pipeline combining a binary numeral extractor with AttentionXML, an extreme classification model. Experiments evaluate Macro and Micro F1 scores, bucketing performance by label frequency, and conducting human-in-the-loop studies with financial subject matter experts to assess practical utility in reducing annotation time.

Results show that FiNER achieves higher Micro-F1 (75.84%) due to superior performance on frequent labels, while the AttentionXML pipeline achieves higher Macro-F1 (47.54%) by better handling rare labels. The pipeline achieves ~90% Hits@5, suggesting it can significantly accelerate human annotators. However, the study notes limitations including the exclusion of tabular data, the inability to handle zero-shot labels, and the high semantic similarity among top-k predictions which may confuse experts. The work provides a critical benchmark for automating financial data structuring but highlights the difficulty of generalizing to unseen or highly specific accounting contexts.

## Exploring the In-Context Learning Capabilities of LLMs for Money Laundering Detection in Financial Graphs

- Year: 2025
- Category: Benchmarks and Evaluation Suites
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: full_extracted_text
- Tags: fraud detection, prompt engineering, knowledge graph, financial statements, accuracy, hit ratio, benchmark, framework, model risk, anti-money laundering, graph reasoning, synthetic data, explainability
- Tag facets: {"asset_class": [], "data_source": ["financial statements"], "deliverable": ["benchmark", "framework"], "evaluation": ["accuracy", "hit ratio"], "market_context": [], "method": ["prompt engineering", "knowledge graph"], "risk_issue": ["model risk"], "task": ["fraud detection"]}
- One-line summary: This paper demonstrates that LLMs can effectively detect money laundering in financial graphs via in-context learning on serialized subgraphs, achieving 63.7% accuracy while providing interpretable rationales, though scalability remains a challenge.

### Detailed Summary

The paper addresses the challenge of detecting complex money laundering schemes in financial knowledge graphs by leveraging Large Language Models (LLMs) as interpretable reasoning engines. It positions LLMs not just as text generators but as in-context learning agents capable of emulating analyst-style investigative logic. The core problem is the need for explainable, graph-structured reasoning in Anti-Money Laundering (AML) without the black-box nature of traditional Graph Neural Networks (GNNs). The study focuses on evaluating whether LLMs can identify suspicious transaction patterns by analyzing localized graph neighborhoods, thereby bridging the gap between structured financial data and natural language reasoning capabilities.

The methodology involves a three-stage pipeline: extracting k-hop subgraphs around target transactions from the IBM AML Synthetic Dataset, serializing these subgraphs into structured text with node and edge metadata, and prompting an LLM (GPT-4o) using few-shot in-context learning. The prompt includes eight canonical laundering typologies (e.g., fan-out, gather-scatter) and non-suspicious examples as demonstrations. The experimental setup uses a balanced dataset of 2,000 transactions (1,000 suspicious, 1,000 clean) to evaluate binary classification and pattern recognition. Performance is assessed using bootstrap resampling to estimate confidence intervals for accuracy, precision, and recall, ensuring robustness despite the fixed test set.

Results show the LLM achieves 63.7% overall accuracy, with higher performance on structured patterns like fan-out (80.3% recall) and lower performance on complex patterns like random or bipartite structures. The model successfully generates human-readable justifications aligned with investigative logic, highlighting its value for explainability. However, the study notes significant limitations, including the computational cost of LLM inference, which hinders scalability for large-scale production. The authors propose a hybrid approach where lightweight classifiers perform initial triage, escalating only borderline cases to the LLM for detailed reasoning. This work serves as a foundational exploration for language-driven financial crime analytics rather than a production-ready system.

## Bridging Language Models and Financial Analysis: A Survey of Datasets, Models, and Applications

- Year: 2025
- Category: Surveys and Reviews
- Trading subtheme: Not Trading Focused
- Evidence type: survey
- Summary coverage: first_50k_chars
- Tags: sentiment analysis, stock prediction, risk extraction, financial question answering, earnings analysis, options, derivatives, chain of thought, multi-agent systems, multimodal modeling, 10-k filings, earnings calls, news, social media, taxonomy, literature review, hallucination, experimental economics, behavioral finance, esg scoring
- Tag facets: {"asset_class": ["options", "derivatives"], "data_source": ["10-k filings", "earnings calls", "news", "social media"], "deliverable": ["taxonomy", "literature review"], "evaluation": [], "market_context": [], "method": ["chain of thought", "multi-agent systems", "multimodal modeling"], "risk_issue": ["hallucination"], "task": ["sentiment analysis", "stock prediction", "risk extraction", "financial question answering", "earnings analysis"]}
- One-line summary: This survey bridges the gap between rapid LLM advancements and cautious financial adoption by comprehensively reviewing datasets, models, and applications across trading, risk, and ESG, while outlining future research directions for reasoning, RAG, and multi-agent systems.

### Detailed Summary

The paper addresses the interdisciplinary gap between computer science’s focus on predictive scalability and finance’s emphasis on causal inference and validation. It aims to synthesize recent LLM developments to guide their practical integration into the financial sector, where cautious adoption and long-term validation are prioritized. The survey highlights that while LLMs offer transformative potential for processing multifaceted financial data, their implementation remains slower than technological innovation due to these domain-specific requirements. By mapping the current landscape, the work seeks to provide a roadmap for researchers and practitioners to leverage emerging techniques effectively in high-stakes financial environments.

The methodology involves a comprehensive review of textual data tasks, including classification, information extraction, summarization, and question answering, alongside an analysis of model architectures from BERT to decoder-based LLMs. The authors categorize applications into trading (sentiment analysis, time-series forecasting, fundamental analysis), risk modeling, ESG scoring, M&A forecasting, and financial agents. They examine specific systems like LLMFactor, StockGPT, and FinRobot, evaluating their use of Chain-of-Thought, Retrieval-Augmented Generation, and multi-agent simulations. The survey also covers experimental economics using LLM agents, noting their ability to replicate human subject experiments with comparable results in behavioral finance contexts.

Key findings indicate that LLMs significantly enhance fundamental analysis by handling large contexts and enabling deductive reasoning, surpassing traditional models in interpreting complex narratives. The survey identifies promising future directions, including advanced prompting techniques, RAG for knowledge-based inference, tool-augmented models, and multimodal capabilities. However, it notes that research on LLMs in ESG and M&A remains in early stages, with challenges in scoring consistency and high-stakes validation. The paper concludes that while LLMs show immense potential, their full impact requires systematic application of these innovations to achieve greater accuracy and adaptability in complex financial modeling and prediction tasks.

## From Scores to Skills: A Cognitive Diagnosis Framework for Evaluating Financial Large Language Models

- Year: 2025
- Category: Foundation and Domain Language Models
- Trading subtheme: Not Trading Focused
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: benchmarking, equity research, spreadsheet reasoning, sec filings, tables, accuracy, benchmark, dataset, bias, cognitive diagnosis, cpa exam, knowledge gap analysis, model evaluation framework
- Tag facets: {"asset_class": [], "data_source": ["sec filings", "tables"], "deliverable": ["benchmark", "dataset"], "evaluation": ["accuracy"], "market_context": [], "method": [], "risk_issue": ["bias"], "task": ["benchmarking", "equity research", "spreadsheet reasoning"]}
- One-line summary: The paper introduces FinCDM, a cognitive diagnosis framework for evaluating financial LLMs at the knowledge-skill level, revealing hidden gaps and specialization patterns that aggregate benchmarks miss.

### Detailed Summary

Existing financial LLM benchmarks suffer from score flattening and narrow concept coverage, obscuring nuanced model capabilities. The authors propose FinCDM, a cognitive diagnosis framework inspired by educational assessment, which evaluates LLMs based on mastery of latent financial skills rather than single aggregate scores. This approach aims to provide interpretable, skill-aware diagnostics that identify precise knowledge gaps and strengths across diverse financial domains, addressing the inadequacy of current evaluation paradigms in high-stakes financial applications.

The core contribution is CPA-KQA, a dataset derived from the Certified Public Accountant examination, covering 70 key financial concepts with rigorous expert annotation and high inter-annotator agreement. The method employs non-negative matrix co-factorization to model the relationship between questions, latent skills, and model proficiency. The authors evaluate 30 proprietary, open-source, and domain-specific LLMs on this dataset, comparing their performance against traditional benchmarks like FinEval-KQA to demonstrate the superior diagnostic power of their framework in capturing fine-grained knowledge states.

Results reveal that models with similar aggregate scores exhibit divergent knowledge specializations; for instance, Gemini excels in general accounting while Doubao dominates financial cost management. The study highlights that prior benchmarks overlook critical areas like tax and regulatory reasoning, which FinCDM exposes as significant weaknesses. Additionally, the analysis uncovers behavioral clusters among models and emphasizes the importance of linguistic resources, showing that models lacking Chinese pretraining perform poorly. These findings support more targeted model development and deployment strategies in finance.

Additional survey-useful detail: Proposes FinCDM, the first cognitive diagnosis framework for financial LLMs that moves beyond aggregate metrics to assess knowledge-skill mastery. CPA-KQA dataset: 210 questions covering 70 financial concepts from CPA exams, annotated by domain experts with high inter-annotator agreement. Dataset is based on Chinese CPA exams, potentially limiting generalizability to other jurisdictions or languages.

## RA-CFGPT: Chinese financial assistant with retrieval-augmented large language model

- Year: 2024
- Category: RAG, Search, and Knowledge Systems
- Trading subtheme: Not Trading Focused
- Evidence type: empirical
- Summary coverage: abstract_or_fragment
- Tags: financial question answering, risk extraction, fine-tuning, sec filings, framework, model, regulatory compliance, chinese finance, document analysis, hybrid knowledge base
- Tag facets: {"asset_class": [], "data_source": ["sec filings"], "deliverable": ["framework", "model"], "evaluation": [], "market_context": [], "method": ["fine-tuning"], "risk_issue": ["regulatory compliance"], "task": ["financial question answering", "risk extraction"]}
- One-line summary: RA-CFGPT introduces a retrieval-augmented Chinese financial assistant that fine-tunes a large language model on a hybrid knowledge base to improve accuracy, compliance, and risk assessment in financial question answering and document analysis.

### Detailed Summary

The paper addresses the challenge of applying large language models to the complex and knowledge-intensive domain of Chinese finance. It argues that existing financial LLMs often neglect the critical role of retrieval-augmented generation (RAG) during training, leading to insufficient handling of intricate financial terminology and compliance requirements. The authors position their work as a solution that integrates retrieval mechanisms directly into the fine-tuning process to ensure outputs are both accurate and compliant with regulatory standards.

The core method involves constructing a specialized hybrid knowledge base tailored for various financial aspects. The authors fine-tune a Chinese LLM using this retrieved document context as background knowledge for multiple financial tasks. The system workflow is designed to not only generate accurate responses but also to explicitly flag associated risks, ensuring that the generated content meets strict compliance mandates. This approach contrasts with standard pre-training or supervised fine-tuning that lacks dynamic knowledge retrieval.

The primary findings highlight the effectiveness of integrating RAG into the fine-tuning pipeline for Chinese financial tasks. The system demonstrates improved performance in question answering, document analysis, and risk assessment by leveraging the hybrid knowledge base. The key contribution is the establishment of a workflow that balances accuracy with regulatory compliance, addressing a significant gap in current financial LLM applications. The paper emphasizes the necessity of domain-specific knowledge bases and retrieval mechanisms for reliable financial AI systems.

Additional survey-useful detail: Construction of a hybrid knowledge base tailored for diverse Chinese financial domain aspects. Construction of a proprietary hybrid knowledge base for Chinese financial data. The paper is truncated, limiting the availability of detailed quantitative results.

## Trading-R1: Financial Trading with LLM Reasoning via Reinforcement Learning

- Year: 2025
- Category: Trading, Investment, and Portfolio Management
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: empirical
- Summary coverage: first_50k_chars
- Tags: alpha mining, portfolio optimization, equity research, spreadsheet reasoning, equities, etfs, portfolio management, reinforcement learning, fine-tuning, chain of thought, backtesting, news, financial statements, market prices, tables, risk-adjusted returns, drawdown, backtest, dataset, model
- Tag facets: {"asset_class": ["equities", "etfs"], "data_source": ["news", "financial statements", "market prices", "tables"], "deliverable": ["dataset", "model", "open source"], "evaluation": ["risk-adjusted returns", "drawdown", "backtest"], "market_context": ["portfolio management"], "method": ["reinforcement learning", "fine-tuning", "chain of thought", "backtesting"], "risk_issue": ["look-ahead bias", "overfitting"], "task": ["alpha mining", "portfolio optimization", "equity research", "spreadsheet reasoning"]}
- One-line summary: Trading-R1 is a financial reasoning LLM trained via supervised fine-tuning and reinforcement learning with a three-stage curriculum to generate structured, evidence-based investment theses and volatility-adjusted trading decisions.

### Detailed Summary

The paper addresses the challenge of aligning large language models with the disciplined, interpretable reasoning required for professional financial trading. It argues that while general reasoning LLMs excel in math and coding, they struggle with the noise, uncertainty, and path-dependency of markets. The authors propose Trading-R1, a model designed to produce structured investment theses and actionable trade recommendations, bridging the gap between natural language analysis and executable trading strategies. The work positions itself against opaque quantitative models and ungrounded general-purpose LLMs, emphasizing the need for explainability and risk-aware decision-making in high-stakes financial environments.

The methodology centers on Tauric-TR1-DB, a 100k-sample corpus spanning 18 months and 14 equities, integrating technical, fundamental, news, sentiment, and macro data. Training employs a three-stage easy-to-hard curriculum: first, supervised fine-tuning (SFT) structures the output format; second, SFT grounds claims in evidence using reverse reasoning distillation from proprietary models; third, reinforcement learning fine-tuning (RFT) aligns decisions with market outcomes. Labels are generated via a volatility-aware, multi-horizon discretization method mapping returns to five trading actions. The backbone is Qwen3-4B, optimized for reasoning tasks.

Evaluated on six major equities and ETFs, Trading-R1 demonstrates improved risk-adjusted returns and lower drawdowns compared to open-source and proprietary instruction-following models. The system generates structured, evidence-based investment theses that support disciplined trading. Key innovations include reverse reasoning distillation to reconstruct hidden CoT traces and volatility-adjusted reward labeling. Limitations include reliance on synthetic reasoning traces and evaluation on a limited set of blue-chip assets, potentially restricting generalizability to smaller caps or different market regimes. The code and terminal will be released publicly.

## Language Models Fine-Tuning for Automatic Format Reconstruction of SEC Financial Filings

- Year: 2024
- Category: Reports, Filings, Accounting, and Risk
- Trading subtheme: Investment Research and Financial Analysis
- Evidence type: benchmark
- Summary coverage: first_50k_chars
- Tags: xbrl tagging, equities, us equities, fine-tuning, semantic parsing, sec filings, 10-k filings, accuracy, model, dataset, data leakage, document structure reconstruction, regulatory compliance, text classification
- Tag facets: {"asset_class": ["equities"], "data_source": ["sec filings", "10-k filings"], "deliverable": ["model", "dataset"], "evaluation": ["accuracy"], "market_context": ["us equities"], "method": ["fine-tuning", "semantic parsing"], "risk_issue": ["data leakage"], "task": ["xbrl tagging"]}
- One-line summary: The paper introduces SEC-former, a bidirectional transformer fine-tuned to reconstruct standardized SEC 10-K item structures from unstructured filings, demonstrating improved document similarity and topic detection for downstream financial analysis.

### Detailed Summary

The research addresses the growing heterogeneity in SEC 10-K filing formats, which complicates automated knowledge extraction and comparative analysis. While the SEC provides a standardized structure, many companies deviate, creating noise for investors and regulators. The authors frame document format reconstruction as a multi-class sentence-level classification task with 18 classes, aiming to map unstructured paragraphs to their correct SEC item sections. This standardization is critical for enabling consistent semantic comparison across firms, supporting tasks like portfolio optimization and risk assessment that rely on aligned textual data. The work positions itself within the broader context of NLP for finance, specifically targeting the data preprocessing bottleneck that hinders effective use of large language models in regulatory compliance and investment research.

The methodology involves fine-tuning pre-trained transformer models, including BERT, RoBERTa, and XLNet, using a bidirectional fine-tuning procedure with Bi-LSTM layers. The dataset comprises approximately 9.54 million paragraphs from 43,608 10-K filings of 6,000 US public companies between 2011 and 2022. Data splitting ensures mutual exclusion of companies across train, validation, and test sets to prevent data leakage from copy-pasted content. The best-performing model, SEC-former, is evaluated on topic detection accuracy, document similarity using TF-IDF and Doc2Vec embeddings, and a real-world case study on a non-compliant filing. Baselines include XGBoost and Bi-LSTM models using TF-IDF features, highlighting the superiority of contextual embeddings for this structural task.

Results show that SEC-former significantly outperforms baselines in classification accuracy and produces document embeddings that better capture semantic similarity compared to traditional bag-of-words approaches. The model successfully reconstructs the structure of a real-world non-compliant filing, validating its practical utility. The improved document similarity metrics suggest that SEC-former can enhance downstream applications like portfolio optimization by providing more accurate semantic representations of annual reports. However, limitations include the heavy class imbalance in the dataset, the exclusion of rarely filled items, and the reliance on regex-based labeling which may introduce noise. The model's effectiveness is also constrained by the static nature of the 18-class schema, which may not capture all nuances of evolving reporting standards.

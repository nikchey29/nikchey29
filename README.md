# Hi, I'm Chaithanya Vemuri 👋

### Data Science • Machine Learning • ML Engineering • Recommender Systems

Currently completing an M.Sc. in Data Science, AI & Digital Business, building end-to-end machine-learning systems around large-scale behavioral data, forecasting, recommendation, ranking, and production-oriented analytics.

My recent work focuses on moving beyond notebook-only ML: reproducible data pipelines, leakage-safe evaluation, experiment tracking, scalable feature engineering, model serving, testing, and deployment-oriented engineering.


## Portfolio Snapshot

- **[REES46 V2](https://github.com/nikchey29/rees46-v2)** — Large-scale recommendation engineering system over **411.7M behavioral events** and **15.6M users**; the final held-out ranker improved **MRR@20 by 45.6%** over popularity. `DuckDB` `TensorFlow` `MLflow` `FastAPI` `PostgreSQL` `Docker`
- **[FulfillAI](https://github.com/nikchey29/fulfillai)** — end-to-end e-commerce data and ML platform with **50K orders**, **10 PostgreSQL tables**, dbt analytics, forecasting, operational-risk models, PySpark streaming, MLflow and FastAPI; demand WAPE improved **88.24% → 69.59% (21.14% relative)**.
- **[OTTO Demand Forecasting](https://github.com/nikchey29/otto-demand-forecasting-dissertation)** — compared **8 forecasting approaches** using chronological rolling-origin evaluation over **672 hourly observations**; selected model achieved **13.93% mean CV WAPE**, with final holdout WAPE of **9.80% for carts** and **11.34% for orders**.


---

## Featured Projects

### 🛒 REES46 V2 — Behavioral Recommendation Platform

[Repository](https://github.com/nikchey29/rees46-v2)

Production-style recommendation engineering platform built on the public REES46 multi-category marketplace behavior dataset.

**Scale**

- Processed **411,709,736 behavioral events**
- Produced **410,325,314 canonical deduplicated events**
- Removed **1,384,422 exact duplicates**
- Modeled behavior across **15,639,803 users**
- **386,299 products**
- **1,325 categories**
- **8,969,359 sessions**

**Recommendation stack**

- Global and contextual popularity
- Session co-visitation
- Collaborative filtering
- Hybrid candidate retrieval
- Purchase-oriented ranking
- TensorFlow sequential recommendation experiment
- Top-K offline evaluation

**Measured held-out performance**

The final purchase-oriented ranker improved over the popularity baseline on the untouched April 2020 test set by:

- **Recall@10: +24.7%**
- **Recall@20: +10.6%**
- **MRR@20: +45.6%**
- **NDCG@20: +23.3%**

**Engineering**

`Python` `DuckDB` `Parquet` `Pandas` `scikit-learn` `TensorFlow` `MLflow` `FastAPI` `PostgreSQL` `Docker` `GitHub Actions` `pytest` `mypy` `Ruff`

The project also documents a real scalability redesign: a global Gold aggregation exhausted temporary storage, so the pipeline was redesigned around restartable month-partitioned Gold datasets and bounded working sets.

---

### 📦 FulfillAI — E-commerce Data & ML Platform

[Repository](https://github.com/nikchey29/fulfillai)

End-to-end e-commerce analytics and machine-learning system covering relational data modeling, demand forecasting, operational risk prediction, feature engineering, and reproducible model evaluation.

**Data platform**

- **50,000 orders**
- **300 products**
- **5 warehouses**
- **10 relational PostgreSQL tables**
- Analytical SQL views and reproducible Parquet ML datasets

**Forecasting**

Built leakage-safe demand features including:

- Lag features
- Rolling statistics
- Seasonality
- Historical demand behavior
- Chronological train / validation / test splits

A hurdle Gradient Boosting forecasting approach reduced demand:

- **WAPE: 88.24% → 69.59%**
- **21.14% relative improvement** over the rolling baseline

**Risk modeling**

Developed models for:

- Late delivery
- Delivery exceptions
- 7-day stockout risk
- Reorder risk

The project emphasizes realistic temporal evaluation and avoiding future-data leakage rather than reporting inflated random-split metrics.

**Stack**

`Python` `PostgreSQL` `SQL` `Pandas` `NumPy` `scikit-learn` `Parquet` `Machine Learning` `Feature Engineering`

---

### 📈 OTTO Demand Forecasting

[Repository](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

Large-scale demand-forecasting research project built around e-commerce behavioral data.

The project explores classical and deep-learning forecasting approaches with a focus on reproducible temporal evaluation and production-oriented experimentation.

**Approaches include**

- Time-series feature engineering
- Multi-horizon forecasting
- Ridge-based baselines
- GRU models
- Transformer-based experimentation
- PyTorch workflows
- Model evaluation and API-oriented delivery

**Stack**

`Python` `PyTorch` `Pandas` `NumPy` `scikit-learn` `Time Series` `Forecasting`

---

## What I Work On

I am particularly interested in problems involving:

- Recommendation systems
- Ranking and retrieval
- Machine learning engineering
- Large-scale behavioral data
- Demand forecasting
- E-commerce analytics
- Feature engineering
- Temporal and leakage-safe evaluation
- Data pipelines
- ML experimentation
- Model serving
- Applied deep learning

---

## Technical Stack

**Languages**

`Python` `SQL`

**Data & Analytics**

`Pandas` `NumPy` `DuckDB` `Parquet` `PostgreSQL`

**Machine Learning**

`scikit-learn` `TensorFlow` `PyTorch`

**ML Systems**

`MLflow` `FastAPI`

**Engineering**

`Docker` `Git` `GitHub Actions` `pytest` `mypy` `Ruff`

**Core areas**

`Recommendation Systems` `Ranking` `Retrieval` `Forecasting` `Feature Engineering` `Experimentation` `Data Pipelines`

---

## Engineering Principles

I try to build projects that demonstrate the full path from raw data to a defensible result:

```text
Raw data
    ↓
validation
    ↓
canonical datasets
    ↓
feature engineering
    ↓
chronological splits
    ↓
baselines
    ↓
modeling
    ↓
offline evaluation
    ↓
experiment tracking
    ↓
model artifacts
    ↓
API / serving
    ↓
testing + CI
```

I prioritize:

- Reproducibility
- Leakage prevention
- Measured baselines
- Chronological evaluation
- Explicit limitations
- Scalable data processing
- Testable code
- Clear experiment boundaries
- Evidence-backed project claims

---

## Current Focus

I am currently targeting opportunities in:

**Data Science • Machine Learning • ML Engineering • Applied AI • Analytics**

Open to both **full-time roles and internships** where I can work on real data, modeling, experimentation, recommendation, forecasting, or production ML systems.

---

## Connect

- [LinkedIn](https://www.linkedin.com/in/chaithanya-vemuri-141897264/)
- [GitHub](https://github.com/nikchey29)

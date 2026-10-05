# Hi, I'm Chaithanya Vemuri

**ML & Data Engineering | Python, SQL, reproducible ML systems | Berlin**

I'm completing an MSc in Data Science, AI & Digital Business at Gisma University of Applied Sciences (expected November 2026), following a BTech in Electronics & Communication Engineering. My independent projects connect data quality and chronological model evaluation to pipelines, APIs and delivery. I'm seeking junior ML Engineering or Data Engineering roles; start date by agreement.

[Portfolio](https://chaithanyavemuri.netlify.app/) · [Focused resumes](https://chaithanyavemuri.netlify.app/resume) · [LinkedIn](https://www.linkedin.com/in/chaithanya-vemuri-141897264/)

## Selected work

### [REES46 V2 — Recommendation & Data Engineering](https://github.com/nikchey29/rees46-v2)

Processed **411.7M public behavioral events** across a corpus containing **15.6M dataset users** into Bronze/Silver/Gold layers. Replaced a failed global DuckDB aggregation (~30.6 GiB temporary spill) with bounded monthly partitions/session buckets and resumable outputs.

The offline hybrid retrieval/ranker benchmark used **~1.50M training interactions and 5,000 held-out April 2020 users**. **MRR@20: 0.02443 → 0.03556 (+45.6% vs popularity)**. Dataset scale, model training and evaluation samples are separate; these are not served-user or customer metrics. MLflow, FastAPI and PostgreSQL connect the frozen model to a serving implementation.

[Benchmark JSON](https://github.com/nikchey29/rees46-v2/blob/main/results/latest/model_benchmark.json) · [Case study](https://chaithanyavemuri.netlify.app/projects/rees46-v2)

### [FulfillAI — Data, ML & CloudOps Platform](https://github.com/nikchey29/fulfillai)

Built a **50K synthetic-order** system with PostgreSQL/dbt, prediction-time feature contracts, forecasting/risk models, MLflow, FastAPI and checkpointed Redpanda/PySpark streaming.

Frozen demand evaluation on **63,501 synthetic test rows (June–July 2026)**: **69.59% WAPE vs 88.24% rolling-28 baseline**, a 21.14% relative reduction. The residual error is high, and **RMSE is worse: 0.934 model vs 0.837 baseline**. This supports a modeling trade-off, not a real-world supply-chain accuracy claim.

The completed **GCP/GKE API platform lab** adds Terraform, repository-restricted OIDC/WIF, scanned images, immutable digest promotion, Helm/Argo CD delivery, Prometheus/Grafana, synthetic Alertmanager-to-Slack verification and recovery drills. **99.9% is a lab SLO target**. V2 remains on its own branch; the cloud proof covers API health/metrics and delivery.

[V2 implementation](https://github.com/nikchey29/fulfillai/tree/platform-engineering-v2) · [Evidence overview](https://github.com/nikchey29/fulfillai/blob/main/docs/cloudops/V2_OVERVIEW.md) · [Frozen results](https://github.com/nikchey29/fulfillai/blob/platform-engineering-v2/docs/results.md) · [Case study](https://chaithanyavemuri.netlify.app/projects/fulfillai)

### [OTTO Demand Forecasting — MSc Dissertation Research](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

Compared **eight approaches on 672 hourly observations**, with three chronological folds, five neural seeds and a separate 96-hour holdout. Selected the **168-hour seasonal baseline** at **13.93% mean CV WAPE**; final holdout WAPE was **9.80% carts / 11.34% orders**. The evaluated Transformer was not the selected winner.

## Core tools in context

| Work | Core tools |
|---|---|
| Data pipelines | Python, SQL, pandas, PostgreSQL, DuckDB, Parquet, dbt; PySpark/Redpanda streaming |
| ML systems | scikit-learn, chronological evaluation, MLflow, FastAPI, Docker, GitHub Actions |
| Supporting platform lab | GCP/GKE, Terraform, Kubernetes, Argo CD, OIDC/WIF, Prometheus/Grafana |

I keep baselines visible, freeze decisions before final evaluation and document failures. The evidence comes from independent engineering, MSc research and controlled labs; it does not establish employer production ownership or on-call experience.

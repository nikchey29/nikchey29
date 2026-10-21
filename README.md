# Hi, I'm Chaithanya 👋

I'm based in Berlin and finishing my MSc in Data Science, AI & Digital Business at Gisma University of Applied Sciences (expected November 2026). I'm looking for **junior Data Engineering or ML Engineering roles**.

I like working on the parts of ML that happen before and after model training: getting messy data into shape, checking whether an experiment is trustworthy, and making the result usable through an API or a repeatable pipeline.

A lot of that learning came from projects that didn't work on the first try. I've kept the failures, decisions and limitations in the repositories below.

[Portfolio & case studies](https://chaithanyavemuri.netlify.app/) · [Role-specific CVs](https://chaithanyavemuri.netlify.app/resume) · [LinkedIn](https://www.linkedin.com/in/chaithanya-vemuri-141897264/)

## Work I'd show in an interview

### [REES46 V2 — behavioral data and recommendations](https://github.com/nikchey29/rees46-v2)

I processed **411.7 million historical marketplace events** using DuckDB and Parquet. My first attempt at a global aggregation failed after spilling roughly 30.6 GiB to disk, so I rebuilt the Gold stage around restartable monthly partitions.

For the *separate, bounded offline recommendation experiment* (1.50M training interactions; 5,000 held-out users), the final ranker improved **MRR@20 from 0.02443 to 0.03556** over popularity. This is an offline ranking result, not a customer or revenue metric.

[Code and methodology](https://github.com/nikchey29/rees46-v2) · [Saved benchmark](https://github.com/nikchey29/rees46-v2/blob/main/results/latest/model_benchmark.json)

### [FulfillAI — from simulated orders to a monitored API](https://github.com/nikchey29/fulfillai)

I created a **synthetic, 50K-order** fulfillment dataset to explore SQL/dbt modeling, time-aware ML evaluation, streaming and API delivery. The forecasting experiment beat its rolling-28 baseline on WAPE, but the absolute error was still high and RMSE got worse. Both results are documented.

I then built a **GCP/GKE platform lab** around the API: Terraform, keyless GitHub Actions, immutable image promotion, Helm/Argo CD, Prometheus/Grafana and a deliberately broken release to practise recovery. The complete V2 implementation is on its [dedicated branch](https://github.com/nikchey29/fulfillai/tree/platform-engineering-v2). These are controlled lab exercises, not claims of running an employer's production service.

[Implementation and verification notes](https://github.com/nikchey29/fulfillai/blob/main/docs/cloudops/V2_OVERVIEW.md)

### [OTTO — my MSc forecasting dissertation](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

I used OTTO event logs to forecast **hourly cart and order activity**, comparing eight methods on **672 hourly observations**. The result surprised me: a simple weekly seasonal baseline did better in development testing than the Transformer. I kept that result rather than changing the project story to make the deep-learning model look like the winner.

The chosen baseline scored **13.93% mean cross-validation WAPE**. On the untouched 96-hour holdout it reached **9.80% WAPE for carts** and **11.34% for orders**.

[Research, code and figures](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

## Tools I use

- **Data:** Python, SQL, DuckDB, Parquet, PostgreSQL, dbt, pandas and PySpark
- **ML systems:** scikit-learn, PyTorch, chronological evaluation, MLflow, FastAPI and Docker
- **Deployment labs:** GitHub Actions, Terraform, GCP/GKE, Kubernetes, Helm, Argo CD and Prometheus/Grafana

Most of this work is independent engineering and MSc research. I haven't presented it as paid production ownership. If something failed or a metric has an important caveat, I try to show that too.

**Based in Berlin · Open to junior Data Engineering / ML Engineering opportunities · Start date by agreement**

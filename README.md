# Chaithanya Vemuri

**Data Engineer · ML Engineer** · Berlin, Germany · open to junior and graduate roles

I build data pipelines in Python and SQL and ship the models that run on them. My projects cover large-scale event processing, offline model evaluation, and deploying and recovering an API on GKE.

MSc Data Science, AI & Digital Business, Gisma University of Applied Sciences (expected 01/2027) · English (working language) · German A1, studying toward B1

[Portfolio and case studies](https://chaithanyavemuri.xyz/) · [Resume](https://chaithanyavemuri.xyz/assets/Chaithanya_Vemuri_Resume.pdf) · [LinkedIn](https://www.linkedin.com/in/chaithanya-vemuri-141897264/)

## Selected work

### [FulfillAI — GKE API delivery and recovery](https://github.com/nikchey29/fulfillai/tree/platform-engineering-v2)

I used Terraform to provision a GKE lab, GitHub Actions with Workload Identity Federation to publish images without a service-account key, and Argo CD to deploy pinned image digests. I injected an invalid image, diagnosed `ImagePullBackOff`, and verified rollback. The GKE checks covered API delivery, health and metrics. The data and model evaluations used 50,000 simulated orders.

[Implementation](https://github.com/nikchey29/fulfillai/blob/platform-engineering-v2/docs/cloudops/V2_OVERVIEW.md) · [Delivery run](https://github.com/nikchey29/fulfillai/actions/runs/37233814366) · [Rollback drill](https://github.com/nikchey29/fulfillai/blob/platform-engineering-v2/incidents/INC-002-bad-release.md)

### [REES46 V2 — restartable event processing](https://github.com/nikchey29/rees46-v2)

I processed **411.7M historical events** with DuckDB and Parquet. A global aggregation exhausted temporary storage after spilling roughly 30.6 GiB. Monthly partitions and 64 deterministic session buckets bounded the work and let the pipeline reuse completed outputs on restart.

In a separate offline benchmark with 1.50M training interactions and 5,000 held-out users, the final ranker beat the popularity baseline by **46% on MRR@20** (0.02443 to 0.03556).

[Partitioning decision](https://github.com/nikchey29/rees46-v2/blob/main/docs/adr/001-partitioned-gold.md) · [Saved benchmark](https://github.com/nikchey29/rees46-v2/blob/main/results/latest/model_benchmark.json)

### [OTTO — MSc forecasting dissertation](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

I streamed **216.7M OTTO events** into **672 hourly observations** and compared eight methods for 24-hour cart and order forecasts. The weekly seasonal baseline scored **13.93% mean CV WAPE** versus **17.67%** for the PyTorch Transformer. The selected model reached **9.80% cart WAPE** and **11.34% order WAPE** on a separate 96-hour holdout.

[Research, code and figures](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

## Tools used in these projects

- **Data engineering** · Python, SQL, DuckDB, Parquet, PostgreSQL, dbt and PySpark
- **ML systems** · PyTorch, scikit-learn, MLflow, FastAPI and Docker
- **Cloud and delivery** · Terraform, GCP/GKE, Kubernetes, Helm, Argo CD, GitHub Actions and Prometheus/Grafana

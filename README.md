# Hi, I'm Chaithanya Vemuri

**Data Science & ML Engineering, with growing hands-on Cloud/DevOps, Platform Engineering and MLOps experience.**

I'm completing an MSc in Data Science, AI & Digital Business at Gisma University of Applied Sciences, with a BTech in Electronics & Communication Engineering. Based in Berlin, I build independent projects that connect data quality and defensible model evaluation to APIs, delivery automation, observability and recovery.

[Portfolio](https://chaithanyavemuri.netlify.app/) · [General resume](https://chaithanyavemuri.netlify.app/assets/Chaithanya_Vemuri_Resume.pdf) · [LinkedIn](https://www.linkedin.com/in/chaithanya-vemuri-141897264/)

## Selected work

### [FulfillAI - Data, ML & CloudOps Platform](https://github.com/nikchey29/fulfillai)

Synthetic e-commerce data/ML platform covering **50K orders**, PostgreSQL/dbt, forecasting and risk models, Redpanda/PySpark streaming, MLflow and FastAPI. Frozen demand WAPE improved **88.24% -> 69.59% (21.14% relative)** against a rolling baseline.

The completed platform lab adds:

- **Infrastructure and identity:** Terraform/GCP/GKE Autopilot, Artifact Registry, VPC/subnet, state reconciliation and repository-restricted OIDC/Workload Identity Federation.
- **Delivery:** GitHub Actions tests/validation, Docker and Trivy, exact digest promotion, Helm and Argo CD automated sync/prune/self-heal. Actions builds/promotes; Argo CD deploys.
- **Operations:** Prometheus/PromQL, versioned Grafana dashboard, multi-window burn alerts for a **99.9% lab SLO target**, and Secret-backed Alertmanager routing with a verified synthetic Slack notification.
- **Recovery and learning:** deliberate ImagePullBackOff diagnosis/rollback, self-healing, incident/runbooks, and separate Linux/systemd/SELinux work. Jenkins, Ansible, ELK and OpenShift were additional hands-on labs.

[V2 implementation](https://github.com/nikchey29/fulfillai/tree/platform-engineering-v2) · [Architecture and evidence](https://github.com/nikchey29/fulfillai/blob/main/docs/cloudops/V2_OVERVIEW.md) · [Successful delivery run](https://github.com/nikchey29/fulfillai/actions/runs/37233814366) · [Case study](https://chaithanyavemuri.netlify.app/projects/fulfillai)

V2 is completed on its branch; it is not merged into `main`. The cloud proof covers API health/metrics and delivery, not every model's inference or the entire data stack in GKE.

### [REES46 V2 - Behavioral Recommendation Platform](https://github.com/nikchey29/rees46-v2)

Processed a public corpus of **411.7M behavioral events containing 15.6M distinct users** through Bronze/Silver/Gold pipelines. Modeling and evaluation use bounded workloads; the final held-out ranker improved **MRR@20 by 45.6%** over popularity. These are dataset and offline-evaluation figures, not served-user or customer metrics.

Reworked a resource-heavy DuckDB aggregation into monthly partitions/session buckets and resumable outputs after temporary-storage failures. Hybrid retrieval/ranking, chronological evaluation, MLflow, FastAPI, PostgreSQL, Docker and CI connect the data path to a serving implementation.

### [OTTO Demand Forecasting - MSc Dissertation Research](https://github.com/nikchey29/otto-demand-forecasting-dissertation)

Compared **eight approaches on 672 hourly observations**, using three chronological folds, five fixed neural seeds and a separate 96-hour holdout. The selected **168-hour weekly seasonal baseline** achieved **13.93% mean CV WAPE**; final holdout WAPE was **9.80% carts / 11.34% orders**. More complex models were evaluated; the Transformer was not the selected winner.

## Technical tools in context

| Area | Tools and practice |
|---|---|
| Data and ML | Python, SQL, pandas, NumPy, scikit-learn, PyTorch, TensorFlow; recommendation, forecasting and chronological evaluation |
| Data/ML systems | PostgreSQL, DuckDB, Parquet, dbt, PySpark, Redpanda, MLflow, FastAPI |
| Cloud and delivery labs | GCP/GKE, Terraform, Artifact Registry, Docker, Kubernetes, Helm, Argo CD, GitOps, GitHub Actions, OIDC/WIF |
| Operations/security labs | Prometheus, PromQL, Grafana, Alertmanager, Trivy, Linux, systemd, SELinux, probes, runbooks and recovery drills |
| Additional hands-on exposure | Jenkins CI; Ansible idempotency; local ELK logging; OpenShift build/Service/TLS Route |

## How I work and what I'm looking for

I keep baselines visible, freeze model decisions before final evaluation, document failures and state the limits of each result. The projects are independent engineering/research and controlled lab implementations; they do not establish enterprise production ownership, an SLA, historical 99.9% availability or 24/7 on-call experience.

I'm seeking early-career **Data Science, ML Engineering, MLOps/ML Platform, Data Engineering and junior Cloud/DevOps/Platform Engineering** opportunities where I can contribute to data-intensive systems and develop my operational judgment.

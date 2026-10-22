"""Render role-focused, selectable-text, one-page CVs from verified facts."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parents[1]
FONTS=ROOT/'source-assets/fonts'
pdfmetrics.registerFont(TTFont('DM',str(FONTS/'dm-sans-400-normal.ttf')))
pdfmetrics.registerFont(TTFont('DM-Medium',str(FONTS/'dm-sans-500-normal.ttf')))
pdfmetrics.registerFontFamily('DM',normal='DM',bold='DM-Medium',italic='DM',boldItalic='DM-Medium')
ink=HexColor('#172a20');gray=HexColor('#425047');accent=HexColor('#5e7559')
styles={
 'name':ParagraphStyle('name',fontName='DM-Medium',fontSize=27,leading=30,textColor=ink,spaceAfter=7),
 'role':ParagraphStyle('role',fontName='DM-Medium',fontSize=11,leading=15,textColor=ink,spaceAfter=9),
 'contact':ParagraphStyle('contact',fontName='DM',fontSize=8.3,leading=12,textColor=gray,spaceAfter=2),
 'section':ParagraphStyle('section',fontName='DM-Medium',fontSize=8.5,leading=12,textColor=accent,spaceBefore=16,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='DM',fontSize=9.3,leading=13.3,textColor=gray,spaceAfter=5),
 'project':ParagraphStyle('project',fontName='DM-Medium',fontSize=10.2,leading=14,textColor=ink,spaceBefore=7,spaceAfter=5),
 'bullet':ParagraphStyle('bullet',fontName='DM',fontSize=9.1,leading=13,textColor=gray,leftIndent=10,firstLineIndent=-9,spaceAfter=4),
 'small':ParagraphStyle('small',fontName='DM',fontSize=8.4,leading=12,textColor=gray,spaceAfter=4)
}
GH='https://github.com/nikchey29'
P='https://chaithanyavemuri.netlify.app'
LI='https://www.linkedin.com/in/chaithanya-vemuri-141897264/'
def paragraph(text,style='body'):return Paragraph(text,styles[style])
def hyperlink(url,text):return f'<link href="{url}" color="#172a20">{text}</link>'
def bullets(texts):return [paragraph('- '+s,'bullet') for s in texts]
def project(name,url,label,items):
 return [KeepTogether([paragraph(hyperlink(url,name)+' <font size="8" color="#64715f"> / '+label+'</font>','project'),*bullets(items)])]
def footer(canvas,doc):
 canvas.saveState();w,h=doc.pagesize
 canvas.setStrokeColor(HexColor('#c6d0c2'));canvas.setLineWidth(.5);canvas.line(43,35,w-43,35)
 canvas.setFont('DM',7);canvas.setFillColor(gray);canvas.drawString(43,23,'Chaithanya Vemuri | Berlin, Germany | Start date by agreement');canvas.drawRightString(w-43,23,str(doc.page));canvas.restoreState()

def make(kind):
 platform=kind=='Cloud_Platform';general=kind=='General'
 role='Junior Cloud / Platform Engineer | Python, GCP/GKE, Terraform & GitOps' if platform else 'Junior Data Engineer / ML Engineer | Python, SQL & Reliable ML Systems'
 intro=('Berlin-based MSc candidate with independent GCP/GKE delivery and recovery labs, supported by Python, SQL and ML engineering projects. I am interested in junior platform roles where repeatable delivery, observability and careful troubleshooting matter.' if platform else 'Berlin-based MSc candidate building data pipelines, recommendation systems and forecasting experiments. My independent work connects data validation and chronological evaluation to API serving and delivery labs. Seeking junior Data Engineering or ML Engineering opportunities.')
 story=[paragraph('Chaithanya Vemuri','name'),paragraph(role,'role'),paragraph('Berlin, Germany | '+hyperlink('mailto:chaithanyavemuri28@gmail.com','chaithanyavemuri28@gmail.com'),'contact'),paragraph(hyperlink(GH,'github.com/nikchey29')+' | '+hyperlink(P,'Portfolio & case studies')+' | '+hyperlink(LI,'LinkedIn'),'contact'),paragraph('PROFILE','section'),paragraph(intro)]
 story.append(paragraph('TECHNICAL SKILLS','section'))
 if platform:
  skills=['<b>Platform labs:</b> GCP, GKE Autopilot, Terraform, Kubernetes, Helm, Argo CD, OIDC / WIF','<b>Delivery / operations:</b> Docker, GitHub Actions, Trivy, Prometheus, Grafana, Alertmanager, Linux, Bash','<b>Data / services:</b> Python, SQL, FastAPI, PostgreSQL, DuckDB, Parquet, dbt, pytest']
 else:
  skills=['<b>Data:</b> Python, SQL, DuckDB, PostgreSQL, Parquet, dbt, pandas; PySpark / Redpanda project work','<b>ML / services:</b> scikit-learn, PyTorch, MLflow, chronological evaluation, FastAPI, Docker, pytest','<b>Delivery labs:</b> GitHub Actions, Terraform, GCP/GKE, Helm, Argo CD, Prometheus / Grafana']
 story += [paragraph(x,'small') for x in skills]
 story.append(paragraph('SELECTED INDEPENDENT ENGINEERING & MSc RESEARCH','section'))
 rees=project('REES46 V2',GH+'/rees46-v2','Data engineering / recommendations',[
  'Processed 411.7M historical events into 410.3M canonical Silver events using DuckDB and Parquet. Reworked a failed ~30.6 GiB global spill into restartable monthly Gold outputs and 64 session hash buckets.',
  'Separate offline benchmark: 1,499,021 training interactions and 5,000 held-out test users. Purchase-ranker MRR@20 improved from 0.02443 to 0.03556 versus popularity; exposed the bundle through a local FastAPI service.'
 ])
 fulfill=project('FulfillAI',GH+'/fulfillai/tree/platform-engineering-v2','Synthetic data / ML / API platform',[
  'Built a workflow using 50,000 synthetic orders with PostgreSQL/dbt, time-aware features, streaming and API serving. Frozen demand WAPE was 69.59% versus 88.24% for rolling-28; RMSE worsened from 0.836723 to 0.933770.',
  'Extended the API into a controlled Terraform / GCP / GKE lab with keyless CI, exact-digest GitOps promotion, Helm / Argo CD, Prometheus / Grafana and documented recovery exercises.'
 ])
 cloud=project('FulfillAI Platform V2',GH+'/fulfillai/tree/platform-engineering-v2','Controlled GCP/GKE API lab',[
  'Provisioned the lab with Terraform. Built keyless GitHub Actions delivery using OIDC / Workload Identity Federation, container scanning and exact-digest promotion into Helm / Argo CD desired state.',
  'Verified the API health / metrics delivery path, Prometheus / Grafana and synthetic Alertmanager-to-Slack routing. Diagnosed a deliberately injected ImagePullBackOff and restored a known-good release.',
  'Recorded controller-ownership and rollout-verification lessons. The 99.9% SLO is a lab target; cloud checks do not establish that the full data and ML stack ran in GKE.'
 ])
 otto=project('OTTO hourly cart / order forecasting',GH+'/otto-demand-forecasting-dissertation','MSc dissertation',[
  'Compared eight methods on 672 hourly observations using three chronological development folds and a separate 96-hour holdout. Weekly seasonal baseline selected at 13.93% mean CV WAPE; final carts / orders WAPE: 9.80% / 11.34%. The Transformer was not selected.'
 ])
 story += (cloud+rees+otto if platform else rees+otto+fulfill)
 story.append(paragraph('EDUCATION & TRAINING','section'))
 story += [paragraph('<b>MSc Data Science, AI & Digital Business</b> | Gisma University of Applied Sciences | In progress','small'),paragraph('<b>BTech Electronics & Communication Engineering</b> | Sri Venkateswara College of Engineering, Tirupati','small'),paragraph('<b>IntrnForte:</b> Python self-directed learning / training.','small')]
 target=ROOT/'assets'/f'Chaithanya_Vemuri_{kind}_CV.pdf'
 doc=SimpleDocTemplate(str(target),pagesize=(595.276,841.89),rightMargin=43,leftMargin=43,topMargin=34,bottomMargin=48,title='Chaithanya Vemuri - '+('Cloud / Platform Engineering' if platform else 'Data / ML Engineering'),author='Chaithanya Vemuri')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
 print(target)

for kind in ['Data_ML','Cloud_Platform','General']:make(kind)

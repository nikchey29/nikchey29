"""Check built routes, assets, metadata, links and evidence contracts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
import csv
import re
import xml.etree.ElementTree as ET
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
errors=[]
class Doc(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.assets=[];self.imgs=[];self.h1=0;self.main=0;self.lang='';self.meta={};self.canonical='';self.buttons=[];self.title='';self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
  if tag=='title':self.in_title=True
  if tag=='meta':self.meta[a.get('name') or a.get('property')]=a.get('content')
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='a':
   self.links.append(a.get('href',''))
   if a.get('target')=='_blank' and 'noopener' not in a.get('rel',''):errors.append('unsafe external target')
  if tag in ('script','img') and a.get('src'):self.assets.append(a['src'])
  if tag=='link' and a.get('rel') in ('stylesheet','icon','preload'):self.assets.append(a.get('href',''))
  if tag=='img':self.imgs.append(a)
  if tag=='button':self.buttons.append(a)
 def handle_endtag(self,tag):
  if tag=='title':self.in_title=False
 def handle_data(self,data):
  if self.in_title:self.title+=data

docs={}
for path in DIST.rglob('*.html'):
 if path.name.startswith('__qa'):continue
 doc=Doc();doc.feed(path.read_text());docs[path]=doc
 if doc.h1!=1 or doc.main!=1:errors.append(f'{path}: one h1 and main required')
 if len(doc.ids)!=len(set(doc.ids)):errors.append(f'{path}: duplicate ids')
 if doc.lang!='en':errors.append(f'{path}: language missing')
 if not doc.title or not doc.meta.get('description') or not doc.canonical:errors.append(f'{path}: SEO metadata missing')
 if doc.meta.get('og:image')!='https://chaithanyavemuri.netlify.app/assets/social-card.png':errors.append(f'{path}: absolute social image missing')
 for image in doc.imgs:
  if not image.get('alt') or not image.get('width') or not image.get('height'):errors.append(f'{path}: image dimensions / alt missing')
 for button in doc.buttons:
  if button.get('type')!='button':errors.append(f'{path}: button type missing')

link_count=asset_count=0
def resolve(base,url):
 parsed=urlsplit(url)
 target=(DIST/parsed.path.lstrip('/')) if parsed.path.startswith('/') else (base.parent/parsed.path) if parsed.path else base
 if parsed.path.endswith('/') or target.is_dir():target=target/'index.html'
 return target,unquote(parsed.fragment)
for path,doc in docs.items():
 for url in doc.links:
  link_count+=1
  if url.startswith(('https://','mailto:')):continue
  target,fragment=resolve(path,url)
  if not target.is_file():errors.append(f'{path}: broken link {url}');continue
  if fragment and target in docs and fragment not in docs[target].ids:errors.append(f'{path}: missing anchor {url}')
 for url in doc.assets:
  asset_count+=1
  if url.startswith(('http:','https:')):errors.append(f'{path}: external render asset {url}');continue
  if not resolve(path,url)[0].is_file():errors.append(f'{path}: missing asset {url}')
for path in (DIST/'assets').glob('*.css'):
 for url in re.findall(r'url\([\'\"]?([^\)\'\"]+)',path.read_text()):
  if not resolve(path,url)[0].is_file():errors.append(f'{path}: missing CSS asset {url}')

foundation=json.loads((ROOT/'evidence/rees46-foundation.json').read_text())
assert foundation['bronze_rows']==411709736
assert foundation['silver_rows']==410325314
assert foundation['bronze_rows']-foundation['silver_rows']==foundation['exact_duplicates_removed']==1384422
benchmark=json.loads((ROOT/'evidence/rees46-benchmark.json').read_text())
assert benchmark['sample']['train_interactions']==1499021
assert benchmark['sample']['test_users']==5000
metrics=json.loads((ROOT/'evidence/fulfillai-metrics.json').read_text())['demand_forecasting']
assert round(metrics['hurdle']['wape_pct'],2)==69.59
assert metrics['hurdle']['rmse']>metrics['rolling_28']['rmse']
manifest=json.loads((ROOT/'evidence/otto-manifest.json').read_text())
assert manifest['final_fold']['test_end']-manifest['final_fold']['test_start']==96
assert len(manifest['cv_folds'])==3
rank=list(csv.DictReader((ROOT/'evidence/otto-ranking.csv').read_text().splitlines()))
assert len(rank)==8 and rank[0]['model']=='Seasonal naive 168h'
assert round(float(rank[0]['mean_cv_wape'])*100,2)==13.93
assert len(ET.parse(DIST/'sitemap.xml').getroot())==10
assert 'Sitemap:' in (DIST/'robots.txt').read_text()
for path in (DIST/'assets').glob('*.pdf'):
 pdf=PdfReader(path)
 if len(pdf.pages)!=1:errors.append(f'{path}: expected one page')
 text=' '.join(p.extract_text() for p in pdf.pages)
 if len(text.split())<250:errors.append(f'{path}: insufficient extracted text')
 if '\x7f' in text or '\ufffd' in text:errors.append(f'{path}: invalid glyph')
 if len(pdf.pages[0].get('/Annots',[]))<6:errors.append(f'{path}: expected clickable contact and source links')

def luminance(c):
 v=[int(c[i:i+2],16)/255 for i in (1,3,5)];return sum(k*(x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for x,k in zip(v,[.2126,.7152,.0722]))
contrast={}
for text,bg in [('#e9e8df','#101312'),('#adb6ac','#101312'),('#849086','#101312'),('#d6a586','#171c19'),('#3d4a37','#c9d2bc')]:
 a,b=sorted([luminance(text),luminance(bg)]);ratio=(b+.05)/(a+.05);contrast[text+' on '+bg]=round(ratio,2)
 if ratio<4.5:errors.append('body text contrast '+text)
report={'status':'failed' if errors else 'passed','html_documents':len(docs),'internal_and_external_link_references':link_count,'asset_references':asset_count,'sitemap_routes':10,'pdfs':3,'contrast_ratios':contrast,'errors':errors}
(ROOT/'static-check-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if errors:raise SystemExit(1)

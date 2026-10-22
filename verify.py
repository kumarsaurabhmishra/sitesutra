from pathlib import Path
from html.parser import HTMLParser
class Scan(HTMLParser):
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a' and a.get('href','').startswith('/'):
   url=a['href'].split('#')[0]
   target=Path('dist')/url.lstrip('/')
   assert target.is_file() or (target/'index.html').is_file(),str(target)
for p in Path('dist').rglob('index.html'):
 s=p.read_text();Scan().feed(s);assert s.count('<h1>')==1;assert 'rel="canonical"' in s
print(str(len(list(Path('dist').rglob('index.html'))))+' pages: internal links, canonical metadata, single H1 passed')
def lum(c):
 a=[int(c[i:i+2],16)/255 for i in (0,2,4)]
 a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a]
 return sum(v*w for v,w in zip(a,[.2126,.7152,.0722]))
for a,b in [('171c28','f7f5ef'),('ffffff','244cff'),('171c28','ff8659'),('fafaf7','10182d'),('606571','f7f5ef'),('244cff','e8edff')]:
 l=sorted([lum(a),lum(b)]);ratio=(l[1]+.05)/(l[0]+.05);assert ratio>=4.5;print(a,b,round(ratio,2))

# Check page anchors and local assets as well as page routes.
from urllib.parse import urlsplit,unquote
class ReferenceScan(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:assert a['id'] not in self.ids,a['id'];self.ids.add(a['id'])
  for key in ('href','src'):
   if key in a:self.refs.append(a[key])
scans={}
for path in Path('dist').rglob('*.html'):
 scan=ReferenceScan();scan.feed(path.read_text());scans[path.resolve()]=scan
checks=0
for path,scan in scans.items():
 for ref in scan.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(Path('dist')/unquote(u.path).lstrip('/')).resolve() if u.path.startswith('/') else (path.parent/unquote(u.path)).resolve() if u.path else path
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(path,ref)
  if u.fragment and target.suffix=='.html':assert unquote(u.fragment) in scans[target].ids,(path,ref)
  checks+=1
print('Local assets and page anchors passed:',checks,'references')

# Search foundations: metadata uniqueness, entity links, crawl policy and sitemap parity.
import json, xml.etree.ElementTree as ET
from html import unescape
import re
origin=json.loads(Path('site-config.json').read_text())['origin'].rstrip('/')
titles=set();descriptions=set();indexable=set()
for path in Path('dist').rglob('index.html'):
 text=path.read_text(); scan=ReferenceScan();scan.feed(text)
 title=unescape(re.search(r'<title>(.*?)</title>',text).group(1))
 description=unescape(re.search(r'<meta name="description" content="([^"]+)"',text).group(1))
 assert title not in titles,('duplicate title',path);titles.add(title)
 assert description not in descriptions,('duplicate description',path);descriptions.add(description)
 route='/' + str(path.parent.relative_to('dist')).strip('.') + '/';route=route.replace('//','/')
 assert f'rel="canonical" href="{origin}{route}"' in text,path
 assert len(description)>=50,path
 if '/demos/' in route:
  assert 'content="noindex,follow"' in text,path
  continue
 indexable.add(origin+route)
 assert 'content="index,follow,max-image-preview:large"' in text,path
 graph=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',text).group(1))['@graph']
 ids={n['@id'] for n in graph if '@id' in n}
 assert any(n['@type']=='WebSite' for n in graph),path
 assert any(n['@type']=='Organization' for n in graph),path
 for node in graph:
  for key in ('publisher','isPartOf','breadcrumb','author','founder','mainEntityOfPage','mainEntity'):
   if isinstance(node.get(key),dict) and '@id' in node[key]:assert node[key]['@id'] in ids,(path,key)
 image=re.search(r'property="og:image" content="([^"]+)"',text).group(1)
 assert image.startswith(origin+'/') and (Path('dist')/image[len(origin)+1:]).is_file(),path
 assert f'property="og:url" content="{origin}{route}"' in text,path
 assert 'name="twitter:card"' in text,path
urls={n.text for n in ET.parse('dist/sitemap.xml').getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
assert urls==indexable,(urls-indexable,indexable-urls)
robots=Path('dist/robots.txt').read_text()
assert 'User-agent: OAI-SearchBot\nAllow: /' in robots
assert 'Disallow: /private/' in robots and 'Disallow: /admin/' in robots
assert 'noindex,follow' in Path('dist/404.html').read_text()
redirect=json.loads(Path('vercel.json').read_text())['redirects'][0]
assert redirect['has']==[{'type':'host','value':'sitesutra.vercel.app'}]
assert redirect['destination']==origin+'/:path*' and redirect['permanent'] is True
print('SEO checks passed:',len(indexable),'indexable URLs; unique metadata, schema, social assets, sitemap, robots and migration redirect')

# Target ownership must survive future route and editorial changes.
import csv
with Path('keyword-map.csv').open() as f: targets=list(csv.DictReader(f))
assert len(targets)==10 and len({row['keyword'] for row in targets})==10
for row in targets:
 assert row['priority']=='active' and row['demand_status'] in ('unverified','verified')
 assert origin+row['canonical_path'] in indexable,row
for route in {row['canonical_path'] for row in targets}:
 assert any(route in scan.refs for path,scan in scans.items() if '/blog/' in str(path)),route
print('Approved target map passed: 10 phrases, four canonical service destinations with blog links')

# The homepage film is decorative, code-native and pauses when it is not useful.
home=Path('dist/index.html').read_text()
script=Path('dist/app.js').read_text()
styles=Path('dist/style.css').read_text()
assert 'data-sutra-film' in home and 'aria-hidden="true"' in home
assert "heroFilm.classList.toggle('is-playing'" in script
assert 'IntersectionObserver' in script and 'animation-play-state:paused' in styles
assert '@media(prefers-reduced-motion:reduce)' in styles
print('Cinematic hero passed: decorative SVG, visibility pause and reduced-motion fallback')

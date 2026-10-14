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

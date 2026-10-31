"""Original editorial articles stored as trusted repository content."""
from pathlib import Path
from html import escape
import json,datetime,shutil

def add_blog(g):
 source_downloads=Path('content/downloads')
 if source_downloads.exists():
  destination=Path('dist/downloads');destination.mkdir(parents=True,exist_ok=True)
  for source in source_downloads.iterdir():
   if source.is_file():shutil.copyfile(source,destination/source.name)
 posts=[]
 for file in Path('content/blog').glob('*.json'):
  post=json.loads(file.read_text());datetime.date.fromisoformat(post['date'])
  assert all(c in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in post['slug']),file
  posts.append(post)
 posts.sort(key=lambda post:(post['date'],post.get('sequence',0),post['slug']),reverse=True)
 g['blog_posts']={}
 cards=[]
 for post in posts:
  route='/blog/'+post['slug']+'/'
  title=escape(post['title']);day=datetime.date.fromisoformat(post['date']).strftime('%d %B %Y')
  g['blog_posts'][route]=post
  body=g['intro']('SITESUTRA JOURNAL / '+escape(post['category']).upper(),title,escape(post['summary']))
  body+='<section class="reading blog-article"><p class="fine">By SiteSutra · <time datetime="'+post['date']+'">'+day+'</time></p><nav class="article-nav" aria-label="Article navigation"><a href="/blog/">← All articles</a><a href="#next-step">Your next step ↓</a></nav>'+post['body']+'</section>'
  body+='<section class="editorialclosing"><h2>Make the next decision with clarity.</h2><p>Discuss your business website or an agency delivery brief with Kumar Saurabh Mishra.</p><a class="btn orange" href="/#booking">Book a discovery call ↗</a></section>'
  g['pages'][route]=(post['title'],body);g['descriptions'][route]=post['description']
  cards.append('<a class="guidecard blog-card" href="'+route+'"><small>'+day+' / '+escape(post['category'])+'</small><h2>'+title+'</h2><p>'+escape(post['summary'])+'</p><span>Read article ↗</span></a>')
 g['pages']['/blog/']=('Website & Digital Marketing Blog',g['intro']('SITESUTRA JOURNAL','Better questions.<br>Clearer business decisions.','Practical notes on websites, digital marketing and agency delivery, with guidance for businesses in Varanasi and beyond.')+'<section class="guidegrid">'+''.join(cards)+'</section><section class="reading"><h2>Planning your next website?</h2><p>Start with our <a href="/guides/">buyer guides</a>, or explore <a href="/services/website-development/">small-business website development</a> and <a href="/agency-partnerships/">white-label agency support</a>.</p></section>')
 g['descriptions']['/blog/']='Original SiteSutra articles on choosing website and digital marketing partners, planning useful scope and improving business enquiries in Varanasi and beyond.'
 g['nav']=g['nav'].replace('<a href="/about/">','<a href="/blog/">Blog</a><a href="/about/">')
 t,b=g['pages']['/'];start=b.rfind('<section class="editorialclosing">')
 feature='<section><div class="sectionhead"><div><span class="eyebrow">FROM THE JOURNAL</span><h2>Read before you brief.</h2></div><p>Useful questions for your next business decision.</p></div><div class="guidegrid">'+''.join(cards[:1])+'</div><p><a class="textlink" href="/blog/">All articles ↗</a></p></section>'
 if start>=0:b=b[:start]+feature+b[start:]
 else:b+=feature
 g['pages']['/']=(t,b)

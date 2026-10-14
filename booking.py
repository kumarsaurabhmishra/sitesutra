from html import escape
import re,json
from pathlib import Path

def update(g):
 p=g['pages'];c=g['config'];url=c.get('bookingUrl','');embed=c.get('bookingEmbedUrl','')
 c.setdefault('bookingDurationMinutes',30)
 duration=c['bookingDurationMinutes']
 cal_link=c.get('calLink','')
 def widget():
  if c.get('bookingProvider')=='cal.com' and cal_link:
   return f'<div class="bookinglive calbooking"><div class="calendar-theme" role="group" aria-label="Calendar appearance" hidden><span>Calendar appearance <small>(switching refreshes slots)</small></span><div><button type="button" data-cal-theme="light" aria-pressed="false">Light</button><button type="button" data-cal-theme="dark" aria-pressed="true">Dark</button></div></div><div id="cal-inline" data-cal-link="{escape(cal_link)}" role="region" aria-label="Cal.com discovery-call booking calendar"><p class="cal-loading" role="status">Loading available times…</p></div><p id="cal-fallback" class="fine">If the calendar does not load, use the booking link below.</p><a class="textlink" href="{escape(url)}" target="_blank" rel="noopener">Open Cal.com booking page ↗</a></div>'
  if embed:
   return f'<div class="bookinglive"><iframe title="Book a 30-minute discovery call with Kumar" src="{escape(embed)}" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe><a class="textlink" href="{escape(url or embed)}" target="_blank" rel="noopener">Open booking calendar in a new tab ↗</a></div>'
  if url:
   return f'<div class="bookingexternal"><h3>Choose your 30-minute slot.</h3><p>Open the live booking page to view availability in your timezone and confirm your appointment.</p><a class="btn" href="{escape(url)}" target="_blank" rel="noopener">View available slots ↗</a></div>'
  return '''<div class="bookingpreview" aria-describedby="booking-state"><div class="calendarcontrols"><button type="button" data-month="previous" aria-label="Previous month">←</button><h3 id="booking-month" aria-live="polite">Calendar preview</h3><button type="button" data-month="next" aria-label="Next month">→</button></div><div class="calendarweek" aria-hidden="true"><span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span><span>S</span></div><div class="calendardates" id="booking-dates" aria-label="Calendar dates — booking not activated"></div><div class="bookingempty"><span class="emptyclock">◷</span><div><b>Live availability isn’t connected yet.</b><p id="booking-state">30-minute calls. Slots will appear here once the booking schedule is activated. No appointment can be booked from this preview.</p></div></div><a class="textlink" href="mailto:contactkumarsmishra@gmail.com">Email Kumar to arrange a call ↗</a><noscript><p>Booking is not activated. Please email Kumar to arrange a call.</p></noscript></div>'''
 def card():return f'<div class="bookingcard" id="booking"><span class="eyebrow">MEET KUMAR / {duration}-MINUTE CALL</span><h2>Let’s talk about<br>your project.</h2><p class="bookingintro">Share your starting point, ask your questions, and discuss the next step. Choose a date and see available times in your timezone.</p>'+widget()+'</div>'
 t,b=p['/'];start=b.index('<div class="herofigure">');end=b.index('</section>',start)
 summary=f'<aside class="callsummary"><span class="eyebrow">A DIRECT CONVERSATION WITH THE FOUNDER</span><span class="calllength">{duration}<span>min</span></span><h2>Your project.<br>A clear starting point.</h2><p>Bring your ideas, your current website, or just a few questions. We can talk through what you need next.</p><ul><li>Website, design, or marketing priorities</li><li>Scope and working arrangements</li><li>Agency partnership opportunities</li></ul><a class="textlink" href="#booking">Choose a time below ↓</a></aside>'
 b=b[:start]+summary+'</section><section class="landingbooking">'+card()+'</section>'+b[end+len('</section>'):]
 b=b.replace('href="/contact/">Discuss your project <span>↗</span>','href="#booking">Book a discovery call <span>↗</span>').replace('<a class="textlink" href="/work/">Explore the work ↗</a>','<a class="btn secondary" href="/work/">See example websites <span>↗</span></a>',1)
 b=b.replace('See the thinking<br>behind the design.','See the kind of website<br>we could create.').replace('Explore original concepts showing how visual identity, content, and website structure come together. Independent demonstrations, not commissioned projects.','These two fictional example websites show my design and development approach. They are demonstrations, not client projects.')
 b=b.replace('View all work ↗','Explore the website examples ↗')
 p['/']=(t,b)
 for route,(t,b) in list(p.items()):
  b=b.replace('Independent concept · Lifestyle retail','EXAMPLE WEBSITE / HOMEWARE SHOP').replace('Independent concept · Architecture','EXAMPLE WEBSITE / ARCHITECTURE STUDIO')
  b=b.replace('A warm, product-led website concept for a fictional homeware brand.','A fictional homeware shop: browse products, inspect materials, and try the demo basket.').replace('A project-led website concept for a fictional architecture practice.','A fictional architecture studio: explore projects and try a consultation brief.')
  b=re.sub(r'<section class="editorialclosing">(.*?)<a class="btn orange" href="/contact/">.*?</a></section>',r'<section class="editorialclosing">\1<a class="btn orange" href="/#booking">Book a discovery call ↗</a><a class="bookingfallback" href="/contact/">Prefer email? Send a project enquiry ↗</a></section>',b,flags=re.S)
  p[route]=(t,b)
 g['nav']=g['nav'].replace('<a href="/contact/">Contact</a>','<a href="/#booking">Book a call</a>')
 # Keep the old contact URL useful as an email fallback; add booking first.
 t,b=p['/contact/'];b=b.replace('<section class="contactsection">','<section class="bookingcontact">'+card()+'</section><section class="contactsection">',1);p['/contact/']=(t,b)
 # Don't leak calendar credentials or event details into the static application.
 public={k:c.get(k,'') for k in ['formEndpoint','bookingUrl','bookingTimezone','email','bookingEmbedUrl','bookingDurationMinutes','bookingProvider','calLink']}
 (g['P']/'site-config.js').write_text('window.SITESUTRA_CONFIG='+json.dumps(public)+';')
 if embed or url:
  t,b=p['/privacy/'];b=b.replace('<h2>Concept interactions</h2>','<h2>Call bookings</h2><p>Cal.com processes the booking details and selected time you enter in its embedded scheduler. The booking page uses Google Meet. Calendar connections, confirmation messages, and appointment records are managed through Cal.com and the connected providers, which may use their own cookies and privacy terms.</p><h2>Concept interactions</h2>');p['/privacy/']=(t,b)

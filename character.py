"""A lightweight cinematic homepage loop built from inline SVG."""


def add_hero_film(g):
    route = '/'
    title, body = g['pages'][route]
    old = '<a class="textlink" href="#booking">Choose a time below ↓</a></aside></section><section class="landingbooking">'
    film = '''<div class="sutra-film" data-sutra-film aria-hidden="true">
<div class="film-head"><span>FROM BRIEF TO USEFUL WEBSITE</span><span class="film-status"><i>DISCOVER</i><i>DESIGN</i><i>BUILD</i><i>CONNECT</i></span></div>
<svg viewBox="0 0 460 240" focusable="false">
<defs><pattern id="film-grid" width="18" height="18" patternUnits="userSpaceOnUse"><path d="M18 0H0v18"/></pattern><linearGradient id="film-glow" x1="0" x2="1"><stop stop-color="#244cff"/><stop offset="1" stop-color="#8ca0ff"/></linearGradient></defs>
<rect class="film-bg" width="460" height="240" rx="12"/><rect class="film-grid" width="460" height="240" rx="12"/>
<g class="film-brief"><rect x="28" y="45" width="142" height="132" rx="9"/><circle cx="47" cy="65" r="5"/><path d="M60 65h77M45 88h90M45 105h69M45 132h48M45 149h78"/><path class="film-tick" d="m135 139 7 7 14-17"/></g>
<path class="film-thread" d="M46 192C78 205 92 171 124 184s42 22 70-2c31-27 60-29 89-5 27 23 48 16 70-9 20-23 41-14 64-5"/>
<g class="film-browser"><rect class="film-browser-shell" x="123" y="31" width="230" height="157" rx="10"/><path class="film-browser-top" d="M123 57h230"/><circle cx="140" cy="45" r="3"/><circle cx="151" cy="45" r="3"/><circle cx="162" cy="45" r="3"/>
<g class="film-wire"><path d="M142 75h78v47h-78zm91 0h98v10h-98zm0 20h77v7h-77zm0 16h89v7h-89zM142 136h55v32h-55zm65 0h55v32h-55zm65 0h59v32h-59z"/></g>
<g class="film-polish"><rect x="142" y="75" width="78" height="93" rx="4"/><rect x="233" y="75" width="98" height="10" rx="3"/><rect x="233" y="95" width="77" height="7" rx="3"/><rect x="233" y="111" width="89" height="7" rx="3"/><rect x="233" y="136" width="98" height="32" rx="5"/><circle cx="160" cy="94" r="10"/><path d="M154 94h12M160 88v12"/></g></g>
<g class="film-phone"><rect x="343" y="69" width="72" height="132" rx="14"/><path d="M365 82h28M355 103h48v45h-48zm0 57h31v7h-31zm0 17h44v7h-44"/><circle cx="379" cy="191" r="3"/></g>
<g class="film-search"><circle cx="371" cy="126" r="27"/><path d="m391 146 21 21"/><path class="film-scan" d="M350 126h42"/></g>
<g class="film-finale"><path class="film-mark" d="M230 68v44m-22-22h44m-37-16 30 31m0-31-30 31"/><circle cx="230" cy="90" r="11"/><text x="230" y="139" text-anchor="middle">sitesutra</text><path d="M186 154h88"/></g>
</svg>
<div class="film-track"><span>Brief</span><span>Structure</span><span>Experience</span><span>Discovery</span></div>
</div>'''
    assert old in body
    replacement = '''<a class="textlink" href="#booking">Choose a time below ↓</a></aside></section>
<section class="hero-film-band"><div class="film-intro"><span class="eyebrow">THE WORK, IN MOTION</span><h2>From first brief<br>to a useful website.</h2><p>A compact look at how structure, experience and discovery connect—without making either hero card carry extra weight.</p></div>''' + film + '</section><section class="landingbooking">'
    g['pages'][route] = (title, body.replace(old, replacement, 1))

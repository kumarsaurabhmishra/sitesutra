"""SiteSutra's lightweight, logo-derived homepage guide."""


def add_character(g):
    route = '/'
    title, body = g['pages'][route]
    old = '<a class="textlink" href="#booking">Choose a time below ↓</a></aside>'
    spark = '''<div class="sutra-spark" data-sutra-spark data-mode="design" aria-hidden="true">
<svg viewBox="0 0 92 68" focusable="false">
<path class="spark-thread" d="M3 57c18 0 17-24 34-24 13 0 14 18 28 18 9 0 13-8 24-8"/>
<g class="spark-mark">
<path class="spark-rays" d="M45 8v32M29 24h32M34 13l22 22M56 13 34 35"/>
<circle class="spark-face" cx="45" cy="24" r="9"/>
<circle class="spark-eye spark-eye-left" cx="42" cy="22" r="1.2"/>
<circle class="spark-eye spark-eye-right" cx="48" cy="22" r="1.2"/>
<path class="spark-smile" d="M41 27c2.5 2 5.5 2 8 0"/>
</g>
<g class="spark-symbol spark-symbol-design"><circle cx="76" cy="16" r="3"/><circle cx="84" cy="19" r="3"/><circle cx="79" cy="25" r="3"/></g>
<g class="spark-symbol spark-symbol-build"><path d="m73 17-5 5 5 5m10-10 5 5-5 5m-3-13-4 16"/></g>
<g class="spark-symbol spark-symbol-grow"><circle cx="77" cy="20" r="7"/><path d="m82 25 6 6"/></g>
</svg>
<span class="spark-copy"><small>MEET SUTRA SPARK</small><strong data-spark-title>Shaping the idea</strong></span>
</div>'''
    assert old in body
    replacement = '<a class="textlink" href="#booking">Choose a time below ↓</a>' + spark + '</aside>'
    g['pages'][route] = (title, body.replace(old, replacement, 1))

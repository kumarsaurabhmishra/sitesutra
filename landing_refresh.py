"""Focused homepage hierarchy and interaction refinements."""


def improve(g):
    pages = g['pages']
    title, body = pages['/']

    # Keep one primary action above the fold. Examples remain prominent in the
    # following section and phone or WhatsApp remain available in the footer.
    body = body.replace(
        '<a class="btn secondary" href="#examples">See example websites <span>↗</span></a>',
        '',
        1,
    )
    hero_contacts = (
        '<div class="local-contact-links">'
        '<a href="tel:+919555037373">Call +91 95550 37373 ↗</a>'
        '<a href="https://wa.me/919555037373" target="_blank" rel="noopener">Ask on WhatsApp ↗</a>'
        '</div>'
    )
    proof = (
        '<div class="hero-proof" aria-label="SiteSutra working arrangement">'
        '<span>Direct founder involvement</span>'
        '<span>Written project scope</span>'
        '<span>Documented handover</span>'
        '</div>'
    )
    body = body.replace(hero_contacts, proof, 1)

    body = body.replace(
        '<a class="textlink" href="#booking">Choose a time below ↓</a></aside>',
        '<p class="call-note">No prepared brief required. No project commitment.</p>'
        '<a class="textlink" href="#booking">Choose a time below ↓</a></aside>',
        1,
    )
    body = body.replace(
        'A compact look at how structure, experience and discovery connect—without making either hero card carry extra weight.',
        'See how a short brief becomes a structured experience with clear content, responsive layouts and useful next steps.',
        1,
    )

    words = [
        'A', 'website', 'should', 'explain', 'your', 'business,',
        'earn', 'the', 'right', 'enquiry,', 'and', 'stay', 'clear',
        'after', 'launch.'
    ]
    spans = ''.join('<span data-reveal-word>'+word+'</span> ' for word in words)
    tagline = (
        '<section class="tagline-reveal" data-tagline-reveal>'
        '<span class="eyebrow">WHAT THE WEBSITE SHOULD DO</span>'
        '<p aria-label="A website should explain your business, earn the right enquiry, and stay clear after launch.">'
        '<span aria-hidden="true">'+spans+'</span>'
        '</p></section>'
    )
    marker = '</section><section class="landingbooking">'
    film_start = body.index('<section class="hero-film-band">')
    marker_at = body.index(marker, film_start)
    body = body[:marker_at] + '</section>' + tagline + '<section class="landingbooking">' + body[marker_at + len(marker):]

    # Turn the existing delivery stages into a progressive visual flow. The
    # JavaScript enhancement adds motion only after the static content exists.
    body = body.replace(
        '<div class="process">',
        '<div class="process process-flow" data-process-flow>',
        1,
    )

    pages['/'] = (title, body)

    # The persistent header button already owns the booking action.
    g['nav'] = g['nav'].replace('<a href="/#booking">Book a call</a>', '')

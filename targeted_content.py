"""Buyer-facing depth for the four agreed search-intent groups."""
from html import escape


def improve(g):
    pages = g['pages']
    website = '/services/website-development/'
    agency = '/agency-partnerships/'
    local = '/digital-marketing-company-varanasi/'
    search = '/services/seo-marketing/'

    def insert(route, content):
        title, body = pages[route]
        # Place useful decision content before the existing delivery details.
        marker = '<section class="reading">'
        assert marker in body, route
        pages[route] = (title, body.replace(marker, marker + content, 1))

    insert(website, '''<h2>Website design and development in Varanasi</h2>
<p>SiteSutra works directly with small businesses in Varanasi and remotely across India. Start with the service you sell, the people you need to reach and the action your website should make easy. Kumar handles the agreed design and development, with a preview to review before launch.</p>
<h3>What should a website development company help you decide?</h3>
<p>Before choosing layouts or technology, agree which customers the website serves, which pages they need, what proof you can publish and how an enquiry will reach you. The proposal should name the pages, content owner, integrations, review stages, acceptance checks and handover. This gives a Varanasi business a concrete basis for comparing website developers without relying on a broad package label.</p>
<h2>Small business website design in India: choose the right starting point</h2>
<div class="tablewrap" tabindex="0" role="region" aria-label="Website scope comparison"><table><caption>Match the project to the business problem</caption><thead><tr><th>Your starting point</th><th>A useful scope</th><th>What we check</th></tr></thead><tbody>
<tr><td>No business website</td><td>A focused set of service, about and enquiry pages using approved business information.</td><td>Can someone understand your offer and take the next step on a phone?</td></tr>
<tr><td>An outdated website</td><td>Keep useful content, improve navigation and layouts, and plan old URL redirects.</td><td>Do important links and booking or enquiry paths still work?</td></tr>
<tr><td>One campaign or offer</td><td>A landing page with one clear audience, offer and next action.</td><td>Does the page answer the promise made by the campaign?</td></tr>
</tbody></table></div>
<h2>Website redesign services: improve what matters, preserve what works</h2>
<p>A redesign starts with your existing site rather than a blank template. We list pages, identify content worth keeping, check account access and agree which URLs stay or redirect. Your launch checklist covers responsive layouts, contact details, links, metadata and the agreed integrations.</p>
<p>Use the <a href="/guides/redesign/">website redesign inventory and redirect-map example</a> to prepare. The <a href="/guides/costs/">website cost guide</a> explains how content, migration and integrations change a quote.</p>
<h3>What do I need to supply?</h3><p>Your business name, services, genuine contact information, logo or brand assets, content owner and permission to use any photographs or project examples. For a redesign, include the current domain, website and account owners. If content is incomplete, we identify the missing decisions in the scope.</p>
<h3>Can the website include WhatsApp or online booking?</h3><p>Yes, where agreed. SiteSutra itself demonstrates a phone link, WhatsApp link and Cal.com booking embed. A contact form needs a configured submission provider and a tested receiving address; displaying a confirmation message alone is not proof that a message arrived.</p>
<h2>Plan the website, search review and handover together</h2>
<p>A useful website scope records the pages and visitor journey before launch, then defines what will be checked afterwards. Prepare with the <a href="/blog/website-development-varanasi-project-brief/">Varanasi website project brief</a>, organise the homepage with the <a href="/blog/small-business-homepage-content-plan/">small-business content planner</a>, and use the <a href="/blog/search-console-first-28-days/">first 28 days Search Console review</a> after release.</p>
''')

    insert(agency, '''<h2>White-label web development in India, built around your agency</h2>
<p>Keep your client relationship and bring SiteSutra an approved design or a defined implementation brief. Kumar works from Varanasi, India, with the communication overlap, repository access and review cadence agreed before delivery. Client meetings happen only under your agreed contact rules.</p>
<h2>What an agency development brief should contain</h2>
<ol><li><strong>Approved inputs:</strong> design files, final copy, image permissions, fonts and required states.</li><li><strong>Build boundaries:</strong> page list, responsive behaviour, integrations and the person who owns each provider account.</li><li><strong>Acceptance:</strong> supported devices, accessibility checks, agency reviewer and the point at which the client approves.</li><li><strong>Handover:</strong> source repository, editing notes, deployment ownership and separately agreed support.</li></ol>
<h3>A small pilot before a larger commitment</h3>
<p>Hypothetical scope: your agency supplies an approved services page and copy. SiteSutra implements the page, mobile navigation and an existing booking destination, shares a preview and hands over the source after the agreed review. Copywriting, a new identity and custom backend features sit outside that pilot unless added to the proposal.</p>
<p>Use the <a href="/blog/website-handover-checklist-for-agencies/">agency website handover checklist</a> to define the evidence your reviewer expects. The <a href="/guides/platforms/">editing and maintenance demonstration</a> shows the static delivery approach used here.</p>
<h3>Will you work inside our existing platform?</h3><p>This site demonstrates HTML, CSS, JavaScript and a Git-based review workflow. Share the stack and repository requirements for a capability check before we quote. Platform-specific delivery is agreed against the actual brief.</p>
''')

    insert(local, '''<h2>Digital marketing services in Varanasi, starting with your enquiry journey</h2>
<p>If you are comparing a digital marketing agency in Varanasi, ask what will actually change in your business: clearer service pages, a working booking route, a technical search review, a content plan or a campaign landing page. SiteSutra starts with that decision and agrees the work with you directly.</p>
<h2>A founder-led digital marketing consultant in Varanasi</h2>
<p>SiteSutra is a small founder-led studio, so you discuss the brief, priorities and review evidence directly with Kumar Saurabh Mishra. This can suit a business that wants one accountable point of contact for its website, search foundations and content plan. If your project needs daily social publishing, large paid-media operations or specialist production, those responsibilities and any additional partners must be agreed before work starts.</p>
<p>The first conversation is used to identify a useful scope, not to prescribe every channel. Bring your current website, the service you want to sell, the enquiries you consider qualified and any search or campaign evidence you already have.</p>
<h3>A practical starting plan for a local service business</h3>
<p>Hypothetical example: a Varanasi home-repair business has a phone number and a dated website. The first scope could clarify its actual services and coverage, make contact actions easy on mobile, and repair any broken enquiry links. The next scope could improve service information and plan answers to real customer questions. Advertising is a separate decision once the offer, landing page and receiving process are ready.</p>
<h3>What should a useful report tell you?</h3>
<p>Which pages were changed, what evidence prompted the change, what was tested and which decisions need your input. Search visibility belongs alongside real enquiry quality: a call or message should be reviewed for service fit, timing and the next step, rather than counted as useful merely because it happened.</p>
<p>Read how to <a href="/blog/website-clicks-vs-qualified-enquiries/">separate website clicks from qualified enquiries</a>. For the website itself, explore <a href="/services/website-development/">website design and development in Varanasi</a>; for crawl and content issues, review <a href="/services/seo-marketing/">technical SEO audit services</a>.</p>
<h2>Guides for planning the work before choosing channels</h2>
<ul><li><a href="/blog/digital-marketing-varanasi-quote-scope/">Compare a Varanasi digital marketing quote and its responsibilities</a>.</li><li><a href="/blog/digital-marketing-varanasi-content-plan/">Build a useful local-business content plan</a>.</li><li><a href="/blog/website-clicks-vs-qualified-enquiries/">Separate website activity from received and qualified enquiries</a>.</li></ul>
''')

    insert(search, '''<h2>A technical SEO audit tied to decisions</h2>
<p>A useful audit connects a technical observation to a specific URL, a proposed fix and a way to verify it. SiteSutra reviews the agreed public website and the search accounts you authorise, then separates confirmed problems from questions that need more evidence.</p>
<h2>Technical SEO audit services in India: what you receive</h2>
<p>The scope can cover crawl access, response status, indexability, canonical signals, sitemap URLs, metadata, headings, internal links, structured data and redirect requirements. The handover groups findings by affected URL, evidence, business impact, recommended owner and retest method. It does not turn a crawler export into a list of unexplained errors.</p>
<h3>One consultant from review through retesting</h3>
<p>Kumar Saurabh Mishra conducts the agreed review and explains the findings directly. Implementation can be included or quoted separately after access and platform constraints are understood. A completed fix is retested against the acceptance evidence; Google indexing, rankings and traffic remain outcomes outside the audit's control.</p>
<h3>What an audit finding looks like</h3>
<div class="tablewrap" tabindex="0" role="region" aria-label="Example audit findings"><table><caption>Hypothetical audit findings — examples of the handover format</caption><thead><tr><th>Observation</th><th>Recommended action</th><th>Acceptance evidence</th></tr></thead><tbody>
<tr><td>An old service URL returns an error after a redesign.</td><td>Check whether an equivalent page exists and agree the appropriate redirect.</td><td>The old URL reaches the agreed destination without a redirect chain.</td></tr>
<tr><td>Two service pages have the same title but answer different buyer questions.</td><td>Write descriptive titles for the distinct page purposes.</td><td>The rendered titles match approved content and remain unique.</td></tr>
<tr><td>A booking-link click is reported as a received enquiry.</td><td>Separate click activity from confirmed bookings and qualified conversations.</td><td>The report names each measure and its actual source.</td></tr>
</tbody></table></div>
<h3>Which access is needed?</h3><p>A public crawl can start without account credentials. Search Console, Bing and analytics evidence require the account owner's approved access. Implementation also needs the relevant repository or platform access. Keep credentials in the provider's access controls, not a shared project brief.</p>
<h3>Audit first, then agree implementation</h3><p>The handover records affected URLs, evidence, business impact, owner and how to retest. Fixes can be scoped separately from content, campaigns or a redesign. For a wider change, use the <a href="/guides/redesign/">redesign migration checklist</a>; local businesses can review the <a href="/digital-marketing-company-varanasi/">Varanasi digital marketing overview</a>.</p>
<h2>Use the audit evidence after launch</h2>
<p>Read the <a href="/blog/technical-seo-audit-deliverables/">technical SEO audit deliverables guide</a> before agreeing the handover. After a launch or approved implementation, use the <a href="/blog/search-console-first-28-days/">28-day Search Console review</a> to check important URLs, page and query signals, and the next evidence-supported action. Keep <a href="/blog/website-clicks-vs-qualified-enquiries/">qualified enquiry measurement</a> separate from impressions and clicks.</p>
''')

    # Remove internal keyword-planning notes from buyer-facing service copy.
    title, body = pages[search]
    start = body.index('<h2>Candidate phrases need validation</h2>')
    end = body.index('<h2>', start + 4)
    pages[search] = (title, body[:start] + body[end:])

    g['descriptions'].update({
        website: 'Website design and development in Varanasi for small businesses: new websites, redesigns, booking integrations and documented handover.',
        agency: 'White-label web development in India for design and marketing agencies. Approved briefs, scoped pilots, review previews and source handover.',
        local: 'Founder-led digital marketing consultant in Varanasi for websites, SEO, useful content and campaign planning. Discuss a clear scope with SiteSutra.',
        search: 'Technical SEO audit services in India with URL-level findings, indexability checks, prioritised fixes and retesting. Request a tailored audit scope.',
    })

    related = {
        'digital-marketing-varanasi-content-plan': [(local, 'Digital marketing services in Varanasi'), (website, 'Small-business website design and development')],
        'search-console-first-28-days': [(search, 'Technical SEO audit services in India'), (website, 'Small-business website design and development')],
        'website-account-ownership-checklist': [(website, 'Small-business website design and development'), (agency, 'White-label web development for agencies')],
        'small-business-homepage-content-plan': [(website, 'Small-business website design and development'), (local, 'Digital marketing services in Varanasi')],
        'white-label-web-development-paid-pilot': [(agency, 'White-label web development for agencies'), (website, 'Website design and development scope')],
        'technical-seo-audit-deliverables': [(search, 'Technical SEO audit services in India'), (website, 'Website redesign and development scope')],
        'digital-marketing-varanasi-quote-scope': [(local, 'Digital marketing services in Varanasi'), (search, 'Technical SEO and search-marketing scope')],
        'website-redesign-or-targeted-fixes': [(website, 'Website redesign and development scope'), (search, 'Technical SEO audit services')],
        'website-development-varanasi-project-brief': [(website, 'Website design and development in Varanasi'), (search, 'Technical SEO audit scope')],
        'choosing-digital-marketing-company-varanasi': [(local, 'Digital marketing services in Varanasi'), (website, 'Small-business website design and development')],
        'website-clicks-vs-qualified-enquiries': [(search, 'Technical SEO audits and measurement planning'), (local, 'Local digital marketing scope')],
        'google-business-profile-or-website-varanasi': [(website, 'Website design and development in Varanasi'), (local, 'Digital marketing services for Varanasi businesses')],
        'website-handover-checklist-for-agencies': [(agency, 'White-label web development for agencies'), (website, 'Website redesign and handover')],
    }
    for route, post in g['blog_posts'].items():
        links = related.get(post['slug'], [(website, 'Small-business website development'), (agency, 'White-label agency development')])
        title, body = pages[route]
        content = '<h2>Put the guidance into your project</h2><ul>' + ''.join(
            '<li><a href="' + url + '">' + escape(label) + '</a></li>' for url, label in links) + '</ul>'
        marker = '<section class="reading blog-article">'
        # Keep service links at the end of the article, before its closing CTA.
        start = body.index(marker)
        end = body.index('</section>', start)
        pages[route] = (title, body[:end] + content + body[end:])

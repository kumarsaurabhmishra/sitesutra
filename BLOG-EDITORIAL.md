# SiteSutra editorial workflow

Daily writing is a draft cadence, not an automatic publishing commitment. The heartbeat runs at 10:00 Asia/Kolkata. Each draft needs a useful buyer task, original example and human review. Today's first article is dated 14 October 2026.

## Add an article

Store one JSON object in content/blog/YYYY-MM-DD-topic.json with slug, title, date (ISO), category, description, summary and body (trusted HTML). blog.py creates /blog/ and /blog/slug/, homepage/nav/footer links. The current article navigation expects a next-step heading with id="next-step". Use only safe, semantic article HTML; no inline scripts, fake data or tracking. Write in SiteSutra’s editorial voice. Public articles use the SiteSutra byline and date, without tool credits, writing-assistance disclosures or internal review notes. Do not fabricate personal experiences, credentials or approval. Human preview approval is still required before publication.

Before a first live publication, datePublished must match the actual release date. The draft date is visible in previews only. If release happens on a later date, update the JSON date before merging; future modifications should use an actual dateModified only when documented.

Use git branches and PRs; never push main directly. Rebuild with python3 build.py, python3 demos.py and python3 verify.py, then check article navigation, relevant service links, mobile layout, canonicals and JSON-LD. Commit generated dist and source. Create or update a preview PR with Summary, Reason and Validation. Do not merge until the human approves that preview. If this feature is still in an open PR, inspect it and safely update the correct branch without losing work.

## Topic direction

Core audience: small businesses, especially businesses in Varanasi, plus agency partners seeking white-label implementation. Candidate phrases: best website agency; best digital marketing company in Varanasi; digital marketing company in Varanasi. Use 'best' to answer comparison intent, never as an unsupported SiteSutra accolade. No search demand has been verified. Closely related phrases belong in one substantial article, not duplicate doorway pages. Platform-specific capability claims require inspectable work.

Potential next distinct buyer tasks: prepare a local service-business website brief; distinguish booking clicks from qualified enquiries; inventory old URLs before a redesign; approve an agency development handover; separate campaign budget from management scope. These are topic candidates, not promises of demand. Do not publish filler simply to meet a daily count. Review existing articles first.

Research changeable claims from primary sources and link them directly. Never invent client work, testimonials, rankings, volumes, office details or outcomes. Label invented business examples hypothetical. Evidence should be inspectable; measurement separates search visibility, dated AI citation samples and real qualified enquiries.

## Local agency reference review

COMPETITOR-REVIEW.md and keyword-map.csv document the 15 October 2026 review of five reference agencies. Use the mapped buyer needs to select distinct useful topics, not to reproduce competitor copy or treat their claims as verified performance. Keep local agency/company variations together and preserve SiteSutra’s core website and white-label offers. Phone/WhatsApp is +91 95550 37373; no genuine client testimonials have been supplied.

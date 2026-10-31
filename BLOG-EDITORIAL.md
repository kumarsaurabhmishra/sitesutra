# SiteSutra editorial workflow

Daily writing is a draft cadence, not an automatic publishing commitment. The heartbeat runs at 10:00 Asia/Kolkata. Each draft needs a useful buyer task, original example and human review. Today's first article is dated 14 October 2026.

## Add an article

Store one JSON object in content/blog/YYYY-MM-DD-topic.json with slug, title, date (ISO), category, description, summary and body (trusted HTML). blog.py creates /blog/ and /blog/slug/, homepage/nav/footer links. For multiple explicitly requested articles on the same date, an optional integer sequence controls same-day ordering (higher appears first; the default is 0). It is editorial ordering, not a publication timestamp. The current article navigation expects a next-step heading with id="next-step". Use only safe, semantic article HTML; no inline scripts, fake data or tracking. Write in SiteSutra’s editorial voice. Public articles use the SiteSutra byline and date, without tool credits, writing-assistance disclosures or internal review notes. Do not fabricate personal experiences, credentials or approval. Human preview approval is still required before publication.

Before a first live publication, datePublished must match the actual release date. The draft date is visible in previews only. If release happens on a later date, update the JSON date before merging; future modifications should use an actual dateModified only when documented.

Use git branches and PRs; never push main directly. Rebuild with python3 build.py, python3 demos.py and python3 verify.py, then check article navigation, relevant service links, mobile layout, canonicals and JSON-LD. Commit generated dist and source. Create or update a preview PR with Summary, Reason and Validation. Do not merge until the human approves that preview. If this feature is still in an open PR, inspect it and safely update the correct branch without losing work.

## Topic direction

Core audience: small businesses, especially businesses in Varanasi, plus agency partners seeking white-label implementation. The only active acquisition keyword set is the 10 approved rows in keyword-map.csv (17 October 2026). Support those four canonical service groups with distinct buyer questions; do not add new acquisition keywords, location doorway pages or platform claims without a new decision. Older comparison articles remain useful but “best” phrases are no longer active targets. No search demand or difficulty has been verified. Closely related phrases belong on the mapped useful service page; supporting articles answer distinct tasks and link back to it.

Potential next distinct buyer tasks: prepare a local service-business website brief; distinguish booking clicks from qualified enquiries; inventory old URLs before a redesign; approve an agency development handover; separate campaign budget from management scope. These are topic candidates, not promises of demand. Do not publish filler simply to meet a daily count. Review existing articles first.

Research changeable claims from primary sources and link them directly. Never invent client work, testimonials, rankings, volumes, office details or outcomes. Label invented business examples hypothetical. Evidence should be inspectable; measurement separates search visibility, dated AI citation samples and real qualified enquiries.

## Query-led, story-led articles

Start each proposed article with a real buyer question, not a broad keyword topic. Use Search Console query language first when available, then current search-result questions and genuine customer language as candidates. Record the exact evidence and date internally. A query or search result is evidence that the wording exists; it is not verified demand, volume or difficulty.

Identify the decision beneath the wording. Someone asking for the “top digital marketing company in Varanasi” may need to compare a consultant, a channel specialist and a full-service company, understand a quote, or decide what should be fixed first. Answer that practical decision early. Keep close variants on the existing canonical service page and use an article only for a distinct task, scenario or question. Review all existing titles and summaries before drafting so a new article does not compete with an older one.

Prefer a clear narrative over a generic list. A useful structure is: introduce a clearly labelled hypothetical Indian small business and its decision; show what the owner notices, asks and compares; explain the trade-offs with an original table, worksheet or decision rule; then return to the story and show the next sensible step. The example must remain fictional unless the owner supplies a permissioned case study. Do not invent a result, testimonial, budget, founder experience or customer quote.

Teach before promoting. The article should still be useful if every SiteSutra reference is removed. Mention SiteSutra only where a relevant service, guide or next step helps the reader act. Use “top” and “best” as buyer language to unpack, never as a claim that SiteSutra holds that position. Avoid generic introductions, repeated service lists, keyword-stuffed headings and articles whose only purpose is to target a phrase.

Before creating a preview, check five editorial gates:

1. The query evidence and intended canonical service page are recorded.
2. The article answers a distinct buyer decision that no existing article already owns.
3. The story or example is concrete, Indian-context appropriate and clearly labelled hypothetical where invented.
4. The reader receives an original decision tool, worksheet, worked example or inspection method.
5. Claims are sourced, limitations are visible, and the final SiteSutra invitation is proportionate to the educational content.

## Local agency reference review

COMPETITOR-REVIEW.md documents the historical 15 October 2026 review of five reference agencies. keyword-map.csv now contains the 10 user-approved active targets. Use the mapped buyer needs to select distinct useful topics, not to reproduce competitor copy or treat their claims as verified performance. Keep local agency/company variations together and preserve SiteSutra’s core website and white-label offers. Phone/WhatsApp is +91 95550 37373; no genuine client testimonials have been supplied.

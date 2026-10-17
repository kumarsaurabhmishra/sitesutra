# SiteSutra search changes

## 17 October 2026 — targeting and measurement preview

- Adopt exactly the 10 user-approved acquisition phrases in keyword-map.csv, grouped onto four existing service destinations. Broader competitor research remains historical context, not the active keyword programme.
- Add useful local website/redesign decision content, agency brief and pilot boundaries, local marketing starting plan and an illustrative audit handover. Strengthen related article-to-service links. Preserve routes, design and truthful concept labels.
- Remove internal keyword-planning notes from buyer-facing service copy. Keep public metadata focused on actual services.
- Defer loading the external Cal.com embed until its booking container approaches the viewport. Keep the direct booking link available. This reduces early third-party work; no Core Web Vitals or ranking improvement is asserted.
- Capture an honest baseline: Google performance processing; 23 sitemap-discovered pages; Bing sitemap processing; no verified ranking, enquiry or citation counts available.
- Correct the previously approved old-host redirect in Vercel domain settings. The vercel.json host rule did not produce a redirect when tested; the domain-level redirect is the active migration control. Test exact final path and query. Retain the source rule as a fallback.

Publication status: preview only for content and JavaScript changes; deployment date will be recorded on approved release. Vercel domain migration correction is a hosting fix for the already-approved domain migration.

No new analytics provider, paid tool, advertising campaign, backlink purchase or external directory listing was created. Genuine client evidence, professional profiles and a verified business presence require real supplied information and permissions.

## Verification evidence

Google URL Inspection on 17 October: /services/website-development/ is Discovered — currently not indexed. Its live test reports URL is available to Google / Page can be indexed and one valid breadcrumb item. Google accepted one indexing request and placed it in the crawl queue; this is not confirmed indexing.

The four target service pages passed browser checks at 320, 390 and 1440 px with a single H1, correct canonical and no horizontal page overflow. The comparison tables are keyboard-focusable scroll regions. At 320 × 600 the booking script stayed unloaded while its container was below the viewport, then loaded and rendered the correctly titled iframe after following the booking CTA. No appointment was submitted. Direct Cal.com fallback remains present. The old production host now returns 308 with the exact service path and query preserved.

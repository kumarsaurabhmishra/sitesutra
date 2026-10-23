# Measuring SiteSutra's agreed target set

The 10 rows in ../keyword-map.csv are the active acquisition targets. Four existing canonical pages own those intents. Related design services and older articles stay accessible; they are not additional keyword campaigns. No search volumes or difficulty scores have been verified.

## Baseline

17 October 2026: Google Search Console performance is processing. The Google sitemap has 23 discovered pages, which does not mean 23 indexed pages. Bing's sitemap is Submitted / Processing. Empty metrics in the baseline CSV and null JSON values mean unavailable, not zero.

21 October 2026: the first Search Console performance rows are available for 16–18 October. See `gsc-observation-2026-10-21.json`. The sample is only 5 impressions and Page indexing is still processing, so use it as an early crawl/query signal rather than a trend or demand estimate.

23 October 2026: Search Console reports 18 impressions and no clicks for 16–21 October. Technical SEO audit variations account for the clearest visible query cluster, and the local marketing page has begun matching `digital marketing consultant in varanasi`. See `gsc-observation-2026-10-23.json` for the exact rows, positions and content decisions. Six days of data cannot establish demand or a ranking trend; website-development targets still have no reported query row.

Keep future exports and private enquiry records outside this public repository. Publish aggregate observations only when approved; do not commit names, messages, bookings, account tokens or raw reports containing private data.

## A repeatable review

1. Record the deployment date and commit in ../SEO-CHANGELOG.md. Compare changes against that date rather than the draft date.
2. When search data is available, export query and page reports for the same completed 28-day windows. Use Web search and record geography/device filters. Review India and the unfiltered market separately; Search Console does not provide city-level query reporting for Varanasi.
3. Review each target phrase with its close variants and owning page. Exact-query rows can be absent because of reporting limits; absence does not prove zero demand. Keep clicks, impressions, CTR and average position together. Average position is a report aggregate, not a promised fixed rank.
4. Check indexability, sitemap processing and Google-selected canonical for the four owning service URLs. Diagnose technical issues before rewriting pages. Do not repeatedly request indexing or resubmit unchanged sitemaps to chase rankings.
5. Count real received enquiries and confirmed bookings separately. Record service fit, customer/agency type and an agreed next step in a private lead sheet. Ask how the visitor found SiteSutra if the source is unknown. Contact-link clicks are not confirmed enquiries; this site has no automatic attribution system.
6. If measuring AI citations, keep a dated prompt, provider/version and cited URL sample separately from search reports. A sampled mention is not market share and is not a qualified lead.

A useful cadence is a weekly health check and a comparison of completed 28-day periods once data exists. This document does not create an automated monitor.

## What the evidence should change

| Observed issue | Next action |
| --- | --- |
| An intended page is excluded from indexing | Check access, status, canonical and the provider's stated reason. |
| Relevant impressions but weak clicks | Review whether title, description and visible offer accurately answer that query; change one coherent page intent. |
| Visits or clicks without qualified enquiries | Test real booking/message receipt, then review scope, proof and fit. Do not treat this as a keyword problem automatically. |
| The wrong SiteSutra page appears for a target group | Review overlapping content, internal links and canonical ownership before adding another page. |
| No usable data yet | Keep values unavailable; improve verifiable technical issues and collect evidence before claiming progress. |

Primary definitions: https://support.google.com/webmasters/answer/7576553 and https://support.google.com/webmasters/answer/17010961

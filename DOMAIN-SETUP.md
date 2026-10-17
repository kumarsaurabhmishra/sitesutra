# SiteSutra custom domain

Preferred origin: https://sitesutra.in. Vercel project: sitesutra in kumarsaurabhmishras-projects.

## GoDaddy DNS

Records requested by Vercel on 17 October 2026:

| Type | Name | Value |
| --- | --- | --- |
| A | @ | 216.198.79.1 |
| CNAME | www | 26ad1112122473f2.vercel-dns-017.com |

Replace conflicting web records only. Preserve MX, mail-related TXT and other unrelated records. Use the provider default TTL. Vercel routes the apex to production and www to the apex with a 308 permanent redirect.

## Release gate

Keep the canonical-origin PR unmerged until Vercel reports valid configuration, HTTPS works for both names and the www redirect preserves paths. Then merge the PR and verify page canonicals, sitemap URLs, robots.txt and representative existing routes on the custom domain. Do not claim domain activation until these checks pass.

Search Console and Bing verification remain pending. Use SEARCH-SETUP.md after DNS activation. This change does not configure domain email.

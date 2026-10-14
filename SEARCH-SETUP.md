# Search verification and measurement

Status: prepared only. No Google or Bing verification, sitemap submission or indexing has been confirmed. Intended account owner: contactkumarsmishra@gmail.com. Current production host: https://sitesutra.vercel.app/.

## Verify after preview approval

1. Sign into Google Search Console using the owner account. Add the URL-prefix property https://sitesutra.vercel.app/ (a Domain property requires control of domain DNS).
2. Choose HTML tag verification and copy only the public content value into googleSiteVerification in site-config.json. It is emitted on the homepage and studio pages only when nonempty. Rebuild, review and merge through a PR. Click Verify in Search Console only after that tag is publicly served; record the confirmation.
3. Sign into Bing Webmaster Tools with the account identity associated with the owner email. Add the same site, then use its HTML meta tag and put the public content value into bingSiteVerification. Alternatively import from an already verified Search Console property using the provider's authorised flow. Do not assume the Gmail address already has a Microsoft account.
4. After real verification, submit https://sitesutra.vercel.app/sitemap.xml in each tool and record the response. Inspect key service URLs. Successful verification/submission does not establish indexing.
5. Public routes allow crawling, including OAI-SearchBot. /private/ and /admin/ remain excluded and contain no published files. Robots exclusions are not authentication; protect any future private content at the host. Preview deployments keep production canonicals and must not be submitted as properties.

Google: https://support.google.com/webmasters/answer/9008080
Bing: https://www.bing.com/webmasters/help/how-to-verify-ownership-of-your-site-afcfefc6

## Keep three measurement streams separate

- Search visibility: dated Search Console/Bing exports of impressions, clicks, queries, page coverage and search tool limitations. Candidate phrases are relevance hypotheses, not verified demand estimates.
- AI citations: manually record date, assistant/version where shown, exact prompt, cited URL and evidence capture. Distinguish citation from mention and referral. Repeat a consistent sample; never call it overall market share.
- Qualified enquiries: only real received email or confirmed booking counts. Record source (ask the visitor if unknown), business/agency fit, service, goal, timing, budget discussion and agreed next step. Avoid copying private enquiry details into this public repo. Booking CTA clicks are not booking confirmations. No analytics integration or automatic measurement has been installed.

Review the three streams separately; none guarantees rankings, citations or sales. Keep baseline and follow-up dates explicit and report missing data as unavailable.

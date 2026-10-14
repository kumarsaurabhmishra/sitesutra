# SiteSutra
Simple static HTML, CSS and JavaScript. `python3 build.py` rebuilds 11 crawlable pages. Edit copy and project data in build.py; styles and interactions are in dist/style.css and dist/app.js. Do not delete those two files when rebuilding.

## Remaining business setup
- Replace demonstration projects with authorised portfolio material.
- Supply city/registered business details, real pricing and privacy retention policy.
- Current enquiry flow prepares a mailto email draft; it requires a configured email app and the visitor must send the draft. No backend submission exists. An agreed form provider can replace it later.
- Current canonical URL is the private Sites address. When configuring a public custom domain, update origin in build.py and regenerate.
- robots.txt allows OAI-SearchBot while excluding /admin/ and /private/. Robots exclusions are not access control. Those paths must be protected by hosting authentication if introduced.
- Before public launch, ensure hosting/CDN firewall permits OAI-SearchBot on public pages; private hosting authentication currently prevents public crawling. Crawler access and schema do not guarantee ChatGPT recommendations.
- No analytics are installed; add appropriate consent and update privacy information before adding tracking.

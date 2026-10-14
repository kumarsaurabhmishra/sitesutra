# SiteSutra preview and launch setup

This revision is local preview only. No save/deploy has been called. Existing Site identity and hosting access are preserved.

## Enquiry delivery — required
No provider account or endpoint has been supplied. The form is therefore visibly unavailable for submission and never shows a successful result. Direct email remains available.

To activate delivery:
1. Create a form service/account you control and verify notification email contactkumarsmishra@gmail.com.
2. Supply its public HTTPS submission endpoint. No secret key belongs in site-config.json or client-side code.
3. The current adapter sends multipart POST with Accept: application/json and expects a JSON response with `ok: true`. A provider with a different response contract needs an adapter update. Configure server-side validation, allowed origins, spam controls, and email notification in the provider.
4. Set `formEndpoint` and `formProvider` in site-config.json, run `python3 build.py`, and update the privacy copy with the provider identity and agreed retention arrangements.
5. Test the preview origin, a valid test brief, an invalid/server-rejected brief, duplicate/retry behaviour, and confirmed receipt in the destination inbox. An accepted HTTP response is not proof of notification receipt. Notification delivery cannot be verified before an endpoint is configured.

The form collects name, email, service, existing website, goal, optional budget, and timeline. It preserves entries on failure and blocks duplicate clicks while a request is in progress. It times out after 15 seconds and reports unconfirmed delivery without claiming failure means no server receipt.

## Domain and domain email
Supply a domain you own or wish to register, registrar/DNS provider, desired canonical hostname, and preferred mailbox provider. No domain was invented or registered and no DNS settings were changed. Public sharing/deployment remains pending approval.

After the host confirms custom-domain support and provides the exact DNS target, configure the apex/www records and TLS. Do not guess a DNS target. Choose one canonical hostname; redirect the other and update `origin` in site-config.json before rebuilding metadata, schema, sitemap and robots.txt.

Supply the desired mailbox address, such as contact@your-owned-domain, and verified sending service. Use the mailbox provider’s exact MX, SPF and DKIM records, then establish DMARC monitoring and check delivery. Do not overwrite existing SPF/MX records without reviewing them. Set email in site-config.json only after the mailbox works; confirm notification delivery again.

## Booking
Supply a real booking URL. Set `bookingUrl` and `bookingTimezone` (currently Asia/Kolkata). The site then links to the provider and tells visitors to choose their timezone there. Enable timezone detection/selection in that provider and test with overseas visitors. Until then, the site invites visitors to email their timezone and suitable times. No fake calendar or slots are shown.

## Founder profile and portfolio
Confirmed by the founder: Kumar Saurabh Mishra, Varanasi, India, 10+ years of experience, skills in websites/design/SEO/marketing. The story uses only those facts and the stated studio direction. No employers, credentials, projects, or dates have been invented. Add a supplied photograph and genuine profile URLs when available. Optional `profileLinks` entries are `{ "label": "LinkedIn", "url": "actual profile URL" }`.

Two original concept demos exist; no third project has been added. Retail prices and architecture locations are explicitly fictional. Demo cart and consultation interactions do not store or transmit visitor data.

## SEO and privacy
17 studio pages have titles, descriptions, canonicals and one H1 each. The two concept demos use noindex,follow and are intentionally omitted from sitemap. Studio metadata retains the existing origin until a verified custom domain is supplied. OAI-SearchBot public access rules and private/admin exclusions remain in robots.txt. Private hosting authentication prevents public crawling; robots.txt is not authorization. Allow crawler access through hosting/CDN only when public launch is approved. No rankings or recommendation guarantees are made.

No analytics installed. No secrets are held in files. Google Fonts and hosting requests are described in privacy copy. Final form-provider disclosure and retention details are required before activating submission.

## Preview
Run `python3 build.py`, then `python3 -m http.server 8000 --directory dist`. Open http://localhost:8000. Source is build.py, refinements.py, demos.py and site-config.json. CSS and JS live in dist and are retained when rebuilding. Custom illustrations live in dist/assets.

## Latest editorial revision
This section supersedes earlier copy-specific notes above. Public copy follows the supplied editorial brief: India only, with no duration, personal history, city, project locations or illustrative product prices. Contact currently prepares an email draft; the visitor must send it from their email app. No website receipt is claimed. Business name, website, budget and timeline are optional. Budget supports “Not sure”. Only a real configured endpoint activates “Send project enquiry” and provider-confirmed success. Photograph, real profile URLs, submission endpoint and booking URL remain unsupplied.

The content layer is editorial.py, applied after refinements.py. Local CSS/JS and demo screenshots are retained on rebuild. Do not publish until the owner approves the current preview.

## Booking activation — 14 October 2026
Google Calendar appointment schedule created for contactkumarsmishra@gmail.com:
- SiteSutra — 30-minute discovery call
- Every day, 10:00–18:00, Asia/Kolkata
- Primary-calendar conflict checking enabled
- Google Meet generated after confirmed booking
- Required first name, surname and email; optional project question
- Google defaults retained: 60-day scheduling window, 4-hour lead time, no buffer, no daily booking cap
- Public booking link: https://calendar.app.google/Qfayhpr6Y3CB4a8o6

The verified inline embed URL is in site-config.json. Google handles live slot availability, timezone selection and booking confirmation. No OAuth secrets or private calendar events are placed in the website. Schedule setup is active in Google; the website revision still remains local pending approval. The primary connector is a chat capability and is not a website backend.

Homepage replaces the three-perspective card with the live booking widget. Both hero buttons have matching height/top alignment. Email enquiries remain optional through the preserved contact URL. Work is labelled homeware-shop and architecture-studio example websites. No appointment has been booked just for testing.

## Cal.com migration
The website now uses the official Cal.com inline embed for https://cal.com/kumar-saurabh-mishra/15min. Its live event is SiteSutra discovery call, 15 minutes, Google Meet; the public calendar shows weekday availability with times beginning at 09:00 India time. This differs from the former 30-minute/daily Google schedule. Website labels match the supplied event. Change availability/duration in Cal.com if different hours are wanted, then update bookingDurationMinutes in site-config.json accordingly.

The Google widget and its link are removed from the website. The separate Google appointment schedule was not deleted. Cal.com's actual calendar connection/conflict settings and final booking notification delivery have not been independently verified. A real booking was not submitted during testing. No API keys are required in this static website.

Verified slot selection opens the real Cal.com confirmation form. Site changes remain local pending publication approval.

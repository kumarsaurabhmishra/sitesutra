# SiteSutra

Founder-led website studio website, built with static HTML, CSS and JavaScript. Includes services, buyer guides, two clearly labelled concept demos, case studies and Cal.com booking.

## Run locally

Requires Python 3; no package installation is needed.

```sh
python3 build.py
python3 demos.py
python3 verify.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. The build produces 19 pages. Keep the existing `dist` directory: its CSS, JavaScript and original assets are source files retained during generation.

## Edit the website

- `build.py`, `refinements.py`, `editorial.py`, `booking.py` and `examples.py`: studio pages and content.
- `demos.py`: retail and architecture demonstrations.
- `dist/style.css`, `dist/app.js`: studio styling and interactions.
- `dist/demo.css`, `dist/demo.js`: demonstration styling and interactions.
- `dist/assets`: original illustrations and preview images.
- `site-config.json`: canonical origin, contact details and public integration configuration. Never put secret API keys here.

Rebuild both generators after editing content or configuration. `verify.py` checks page links, assets, fragments, metadata and core colour contrast. See `TESTING.md` for manual checks.

## Hosting and remaining setup

The preferred production domain is https://sitesutra.in. The existing https://sitesutra.vercel.app deployment remains available while DNS is connected. Vercel serves the committed `dist` directory and deploys merges to `main`. The source repository is public. `.openai/hosting.json` retains the earlier Sites project identity.

Bookings use the configured Cal.com 15-minute event. Availability and calendar connections are managed in Cal.com. The project-brief form currently prepares an email draft; the visitor must send it. A real submission endpoint and notification delivery still need configuration.

Domain email, genuine professional-profile links and founder photograph can be supplied later. Update `origin` in `site-config.json` and rebuild when changing domains. Concept projects are demonstrations, not commissioned client work. See `SETUP.md` for further launch notes.

## Branch and pull request workflow

`main` is the production branch; Vercel deploys it after merges. Develop on `deployment` or a feature branch, then open a PR to `main`. Complete the Summary, Reason and Validation sections and use a specific title. The PR metadata check runs from trusted base-branch workflow code without checking out or executing PR code.

Enable local commit/push guardrails after cloning:

```sh
git config core.hooksPath .githooks
```

Local hooks are convenience guardrails and can be bypassed. GitHub must enforce PR-only merges, administrator enforcement, no force pushes/deletions, conversation resolution and the `PR title and description` status check through branch protection. The public repository has enforced protection on `main`, including for administrators. No review approval is required while the founder is the sole reviewer.

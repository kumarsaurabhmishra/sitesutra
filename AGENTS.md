# Repository workflow

- Keep main as the production and default branch. Never commit or push directly to main.
- Use deployment for integration work, or a codex/ feature branch for isolated changes.
- Submit changes to main through a pull request with a specific title and completed Summary, Reason and Validation sections.
- Run python3 build.py, python3 demos.py and python3 verify.py for website changes. Commit the generated dist output, because Vercel serves it directly.
- Vercel production follows main; changes on deployment are preview candidates until merged.
- Enable the local guardrails with git config core.hooksPath .githooks. Local hooks can be bypassed; server-side branch protection must also be enabled when the GitHub plan supports it.

# Cross-Browser Regression Suite — Playwright + Pytest + GitHub Actions

A CI/CD-integrated automated test suite demonstrating smoke and full-regression
coverage across Chromium, Firefox, and WebKit, with results published as an
HTML report on every run.

**Target app:** [SauceDemo](https://www.saucedemo.com) — a public e-commerce
demo app used for QA practice (login, inventory, cart, checkout flows).

## Why this project

Automated test suites tend to rot in two ways: they run everything on every
commit (slow, expensive), or they're never organized by risk/priority at all.
This suite separates **smoke** (critical path, runs on every push — login,
page loads, inventory renders) from **regression** (full functional coverage —
cart, sorting, checkout — runs on PRs and on demand), and validates both
across all three major browser engines in a CI matrix.

## Project structure

```
.
├── .github/workflows/tests.yml   # CI: browser matrix, marker-based runs, report publishing
├── tests/
│   ├── conftest.py               # Shared fixtures (base URL, logged-in session)
│   ├── test_smoke.py             # Critical-path checks
│   └── test_regression.py        # Full functional coverage
├── pytest.ini                    # Marker registration, default options
└── requirements.txt
```

## Running locally

```bash
pip install -r requirements.txt
playwright install

# Fast critical-path check
pytest -m smoke

# Full regression, specific browser
pytest -m regression --browser firefox

# All browsers (run each separately — Playwright doesn't fan out natively)
for b in chromium firefox webkit; do pytest -m regression --browser $b; done

# Generate an HTML report
pytest -m regression --html=report.html --self-contained-html
```

## CI/CD design

- **Push to `main`** → runs the **smoke** suite across all 3 browsers (fast feedback).
- **Pull request** → runs the **full regression** suite across all 3 browsers.
- **Manual dispatch** → choose either suite on demand.
- Each browser's HTML report is uploaded as a build artifact, and on `main`
  they're combined into a small static site and published to **GitHub Pages**,
  so results are viewable without downloading anything.

## What this demonstrates

- Structuring a test suite by risk tier (smoke vs. regression) rather than
  running everything indiscriminately.
- Cross-browser coverage via a CI matrix, not just "works on Chrome."
- Wiring test results into a durable, shareable artifact (GitHub Pages) instead
  of leaving them buried in CI logs.
- Clean fixture design (`conftest.py`) to keep test bodies readable.

## Live report

Once pushed, the latest report is published at:
`https://<your-username>.github.io/<repo-name>/`

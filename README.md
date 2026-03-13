# CW Script Manager

Script generation and management system for Chatting Wizard. Deployed via GitHub Pages.

## Structure

```
{model}/               → Per-model folder (index.html, objections.html, smart-messages.html, XLSX, profile photo)
scripts/framework/     → Master script framework and strategy docs
assets/                → Logos and favicon
tools/                 → Local-only Python scripts (gitignored — generators, CLIs, model configs)
.cursor/rules/         → Agent rules and context
.github/workflows/     → GitHub Actions deploy pipeline
```

## How it works

1. Model configs live in `tools/models/{name}.py` (local only).
2. Python generators in `tools/` create HTML guides, XLSX exports, and Smart Messages pages.
3. Generated output is committed and deployed to GitHub Pages automatically on push.
4. Chatters access their model's guide via the dashboard at the root `index.html`.

## Key files

- `index.html` — Main dashboard with all creators, search, and filters
- `tools/model_factory.py` — Core generator for guides and XLSX
- `tools/generate_dashboard.py` — Dashboard generator
- `tools/generate_nudge_pages.py` — Smart Messages page generator
- `tools/regenerate_all.py` — Regenerates all output for all models

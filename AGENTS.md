# AGENTS.md — Data Storytelling Workshop

Context for AI agents (Copilot CLI, Claude Code, Cursor, etc.) working in this repo.

## Repo Purpose

Workshop materials for "From Raw Data to Confident Narratives" — a 1-hour UW Foster School of Business classroom session teaching undergrad data analytics students the difference between naive AI prompting and skill-harnessed data storytelling.

The repo contains:
- Synthetic datasets (coffee shops + job market) with intentional quality issues
- Two VS Code workspaces (naive vs. harnessed)
- A Slidev presentation deck with UW branding
- Six custom agent skills for data analysis workflows

## Repo Structure

```
data-storytelling-workshop/
├── slides.md                  Slidev deck (~18 slides)
├── styles/index.css           UW purple/gold design tokens
├── data/                      Synthetic datasets (source of truth)
│   ├── coffee-shops/          Track A: 5 files, 6 months transactions
│   └── job-market/            Track B: 3 files, 400 postings
├── workspace-naive/           Demo workspace — minimal, no skills
├── workspace-harnessed/       Demo workspace — full skills suite
├── skills/                    Source of truth for custom skills
├── milestones/                README + prompts for each workshop milestone
└── scripts/                   Data generation + setup scripts
```

## Conventions

### Files
- **`slides.md`**: Slidev deck. Preserve frontmatter. One idea per slide. Keep in sync with workshop arc.
- **`data/`**: Source of truth for all data files. Do not modify data files unless regenerating via `python scripts/generate_data.py`.
- **`workspace-naive/data/`**: Mirror of `data/coffee-shops/` only. Sync when source data changes.
- **`workspace-harnessed/data/`**: Mirrors of both tracks. Sync when source data changes.
- **`skills/`**: Source of truth for custom skills. Mirror to `workspace-harnessed/.agents/skills/` after changes.
- **`.agents/skills/<name>/SKILL.md`**: Keep body focused. Description must be retrieval-optimized (verb-led, trigger phrases).

### Voice and Content Rules
- No emoji in finished content.
- No em dashes — use commas, periods, or parentheses.
- No sycophantic openers.
- No banned phrases: delve, showcase, robust, seamless, cutting-edge, innovative, game-changer, groundbreaking.
- Lists are tools, not finished prose.

### Commits
- Conventional commits: `feat:`, `fix:`, `docs:`, `chore:`, `data:`
- Always include trailer: `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`
- Verify `git diff --staged` is free of secrets before pushing.

### Build Commands
```bash
npm run dev          # Slidev dev server at http://localhost:3030
npm run build        # Static build to dist/
npm run build:vercel # Vercel deployment build
npm run export       # Export to PPTX/PDF (requires playwright-chromium)
python scripts/generate_data.py  # Regenerate all synthetic data files
```

## When Working On...
- **slides.md**: One idea per slide. Maintain the 4-milestone arc. Presenter notes are the script.
- **data files**: Never hand-edit — regenerate via the Python script to preserve intentional quality issues.
- **skills/**: Keep body ≤ 80 lines for SKILL.md. Move deep content to `reference.md`. After any CRUD, run `/sync-skills-index`.
- **workspace-harnessed/**: The CLAUDE.md here is the agent's operating instructions. Keep it accurate.
- **workspace-naive/**: Must stay minimal. No CLAUDE.md with skills. No `.agents/` directory.

## Skills Index
<!-- pipe-compressed: name | triggers | path -->

### Workshop skills
bootstrap-preflight       | preflight check, environment setup, verify tools, student quickstart, presenter setup | skills/bootstrap-preflight/SKILL.md
data-confidence-scorer    | confidence scores, add confidence, document assumptions, source lineage, audit analysis, defensible report | skills/data-confidence-scorer/SKILL.md
data-refinement-interview | pre-analysis interview, refine scope, ask questions before analyzing, structured intake, grill data | skills/data-refinement-interview/SKILL.md
html-infographic-builder  | create data report, generate infographic, make this visual, HTML dashboard, chart from data | skills/html-infographic-builder/SKILL.md
spotlight-walkthrough     | add tour, guided walkthrough, Shepherd.js, interactive report, self-presenting, tour the report | skills/spotlight-walkthrough/SKILL.md
sync-skills-index         | update skills index, sync AGENTS.md, regenerate skills list, stale index | skills/sync-skills-index/SKILL.md

## Safe Defaults
- Never commit `.env`, API keys, or local dev secrets.
- Never modify data files by hand — use the generation script.
- workspace-naive must never gain a CLAUDE.md with skills references. That's the whole demo contrast.

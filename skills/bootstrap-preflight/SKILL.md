---
name: bootstrap-preflight
description: Verify the workshop environment is ready for a live demo or student session. Two modes: presenter-preflight (checks Node.js, VS Code, Copilot/Claude, Slidev, data files, browser) and student-quickstart (validates data files, suggests platform loading instructions). Use before starting the workshop.
---

# Bootstrap Preflight

Environment verification for the data-storytelling-workshop. Catches setup problems before they become live-demo problems.

## When to Use

- **Presenter mode**: Run before the workshop starts. Validates the full presenter setup (three desktops, all tools, Slidev live).
- **Student mode**: Students run this to verify they can follow along. Validates data files are accessible and AI platform is ready.

## Modes

### Mode 1: Presenter Preflight (`/bootstrap-preflight presenter`)

Checks, in order:
1. **Node.js** — `node --version` >= 18. If missing: `winget install OpenJS.NodeJS` (Windows) or `brew install node` (macOS)
2. **npm** — `npm --version`. If missing: comes with Node.js
3. **Slidev** — `npm run dev` in repo root. Confirm slides load at `http://localhost:3030`
4. **VS Code** — confirm two windows open (workspace-naive, workspace-harnessed)
5. **AI Platform** — confirm Claude.ai or Claude Code CLI responding
6. **Data files** — verify all 8 files present in `data/coffee-shops/` and `data/job-market/`
7. **Workspace naive** — confirm `workspace-naive/data/` has coffee shop files, no CLAUDE.md skills
8. **Workspace harnessed** — confirm `.agents/skills/` has all 4 core skills, CLAUDE.md present
9. **Browser** — Slidev deck accessible at the Vercel URL (confirm public access)
10. **Desktop layout** — D1 (slides), D2 (naive VS Code), D3 (harnessed VS Code) — visual reminder only

### Mode 2: Student Quickstart (`/bootstrap-preflight student`)

Checks:
1. Confirm the repo URL: `github.com/BrettReifs/data-storytelling-workshop`
2. Check that data files can be downloaded (provide direct URLs for each CSV/JSON)
3. Detect AI platform: ask which platform the student is using
4. Provide platform-specific file loading instructions:
   - **Claude.ai**: Attach files via paperclip icon. Max ~5MB per session.
   - **ChatGPT**: Upload via paperclip. Use Code Interpreter / Data Analysis mode.
   - **Gemini**: Attach files via paperclip. Gemini 1.5 Pro recommended for large CSVs.
   - **GitHub Copilot**: Add files to workspace, use `#file:` references in prompt.
5. Suggest starter prompt for Milestone 1

## Failure Recovery

| Problem | Recovery |
|---------|----------|
| Node.js missing | `winget install OpenJS.NodeJS` or `brew install node` |
| Slidev not starting | `npm install` first, then `npm run dev` |
| Skills not loading in Claude Code | Verify `.agents/skills/` directory is inside the VS Code workspace root |
| Data file missing | Re-run `python scripts/generate_data.py` from repo root |
| Vercel URL not loading | Check `vercel.json`, run `npm run build:vercel` and redeploy |

## Output Format

```
PREFLIGHT REPORT — Presenter Mode
Generated: 2026-05-27 14:00 PT

[PASS] Node.js v20.11.0
[PASS] Slidev running at http://localhost:3030
[PASS] 8/8 data files present
[WARN] workspace-harnessed/.agents/skills/bootstrap-preflight not found (nice-to-have)
[PASS] CLAUDE.md present in harnessed workspace
[PASS] Vercel deployment live: https://data-storytelling-workshop.vercel.app

Status: READY (1 warning — non-blocking)
```

## Acceptance Criteria

- [ ] Presenter mode checks all 10 items and produces a pass/warn/fail report
- [ ] Student mode detects platform and provides correct loading instructions
- [ ] Any FAIL item includes a specific recovery command
- [ ] Output is scannable (not a wall of text)

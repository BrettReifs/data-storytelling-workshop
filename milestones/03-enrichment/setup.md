# Milestone 3 — Skill Installation

For participants running outside the workshop environment, or forking the repo for their own use.

## Quick Install (harnessed workspace)

The skills are already installed if you cloned the repo and are using `workspace-harnessed/` as your VS Code workspace root.

Verify by checking:
```
workspace-harnessed/.agents/skills/
├── bootstrap-preflight/SKILL.md
├── data-confidence-scorer/SKILL.md
├── data-refinement-interview/SKILL.md
├── html-infographic-builder/SKILL.md
├── spotlight-walkthrough/SKILL.md
└── sync-skills-index/SKILL.md
```

## Using Skills with Different Platforms

### Claude Code (Claude.ai)
Skills in `.agents/skills/` are automatically available when `workspace-harnessed/` is your workspace root. Invoke with `/skill-name` or reference by name in your prompt.

### GitHub Copilot CLI
Skills are available as installed skills. Reference with `/skill-name` or describe the task — the skill triggers on matching phrases.

### ChatGPT / Gemini / Other Platforms
These platforms don't have native skill discovery. Instead, paste the contents of the relevant `SKILL.md` file into your system prompt or conversation context before running the analysis.

Example:

1. Open `.agents/skills/data-refinement-interview/SKILL.md`
2. Copy the full contents
3. Paste into your conversation: "Use these instructions for this analysis: [paste SKILL.md]"
4. Load your data and proceed

## Updating Skills

Skills are defined in `.agents/skills/` (source of truth). After any changes, run:

```bash
# Copy updated skills to harnessed workspace
cp -r .agents/skills/* workspace-harnessed/.agents/skills/

# Regenerate AGENTS.md index
# (or run /sync-skills-index in Claude Code)
```

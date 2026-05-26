---
name: sync-skills-index
description: Scan the skills directory and regenerate the pipe-compressed skills index section in AGENTS.md. Use when a new skill is added, an existing skill is removed, or the AGENTS.md index is out of date. Trigger phrases: "update skills index," "sync AGENTS.md," "regenerate skills list."
---

# Sync Skills Index

Keeps the pipe-compressed skills index in AGENTS.md synchronized with the actual skill directories on disk.

## When to Use

- After adding a new skill to `.agents/skills/` or `workspace-harnessed/.agents/skills/`
- After removing or renaming a skill directory
- When the AGENTS.md index appears stale or incomplete
- As a routine maintenance step at session end

## Process

1. Scan all subdirectories of `.agents/skills/` for `SKILL.md` files
2. Also scan `workspace-harnessed/.agents/skills/` for any additional skills
3. For each found `SKILL.md`, extract:
   - `name:` from frontmatter
   - `description:` from frontmatter (extract 3-5 trigger phrases as a comma-separated list)
   - Relative path from repo root
4. Locate the `<!-- pipe-compressed: name | triggers | path -->` marker in AGENTS.md
5. Replace everything between that marker and the next `##` section header with the regenerated index
6. Write the updated AGENTS.md

## Pipe-Compressed Format

```
<!-- pipe-compressed: name | triggers | path -->
skill-name | trigger phrase one, trigger phrase two, trigger phrase three | path/to/SKILL.md
```

Rules:
- One line per skill, no blank lines between entries
- Triggers: 4-6 phrases extracted from the `description:` field, comma-separated
- Path: relative from repo root, forward-slash separated
- Sort alphabetically by skill name within each group

## Example Output

```
<!-- pipe-compressed: name | triggers | path -->
bootstrap-preflight | preflight check, environment setup, verify tools, student quickstart | .agents/skills/bootstrap-preflight/SKILL.md
data-confidence-scorer | confidence scores, add confidence, document assumptions, source lineage, audit analysis | .agents/skills/data-confidence-scorer/SKILL.md
data-refinement-interview | pre-analysis interview, refine scope, ask questions before analyzing, structured EDA intake | .agents/skills/data-refinement-interview/SKILL.md
html-infographic-builder | create data report, generate infographic, make this visual, HTML dashboard | .agents/skills/html-infographic-builder/SKILL.md
spotlight-walkthrough | add tour, guided walkthrough, Shepherd.js, interactive report, self-presenting | .agents/skills/spotlight-walkthrough/SKILL.md
sync-skills-index | update skills index, sync AGENTS.md, regenerate skills list | .agents/skills/sync-skills-index/SKILL.md
```

## Acceptance Criteria

- [ ] All SKILL.md files in `.agents/skills/` are represented in the index
- [ ] Each entry has name, triggers (4-6), and correct relative path
- [ ] AGENTS.md is updated in place (not a new file created)
- [ ] Format matches pipe-compressed convention exactly
- [ ] Index is sorted alphabetically within groups

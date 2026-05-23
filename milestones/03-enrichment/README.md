# Milestone 3: The Enrichment

**Duration:** ~10 minutes  
**Workspace:** D3 — `workspace-harnessed/` (full skills suite, structured CLAUDE.md)  
**Goal:** Show what changes when the agent has a systematic framework instead of a blank slate.

## What Happens

Switch to the harnessed workspace. Show the skills directory and CLAUDE.md. Run the same analysis with skills active. The agent will conduct a pre-analysis interview, flag data quality issues systematically, and produce annotated findings.

## Setup

See `setup.md` for skill installation instructions if you're running this outside the workshop VM.

The harnessed workspace should already have:
- `.agents/skills/` with all 6 custom skills
- `CLAUDE.md` with data quality protocol, scoping rules, and output standards
- `data/coffee-shops/` with all 5 coffee shop files

## What to Show

1. Open `workspace-harnessed/` in VS Code
2. Walk through `CLAUDE.md` briefly — show the agent identity, scoping rules, skills table
3. Show `.agents/skills/` directory — open `data-refinement-interview/SKILL.md` as an example
4. Load the data and trigger the interview

## Suggested Prompts

See `prompts.md` for the milestone prompt sequence.

## What to Watch For

- The interview: does the agent ask specific questions about the actual data, or generic questions?
- Does it flag the S3 flat-sales anomaly before you mention it?
- Does the date format issue surface in the quality notes?
- Are the findings annotated differently from Milestone 1?

## The Core Lesson

The skills did not give the agent more data. They gave it a framework for what questions to ask before drawing conclusions. The output is not smarter — it is more disciplined.

## Transition to Milestone 4

The enrichment produces better analysis. Milestone 4 adds the final layer: confidence scoring, source lineage, audience variants, and the spotlight tour.

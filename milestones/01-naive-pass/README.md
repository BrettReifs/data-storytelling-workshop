# Milestone 1: The Naive Pass

**Duration:** ~10 minutes  
**Workspace:** D2 — `workspace-naive/` (no skills, minimal CLAUDE.md)  
**Goal:** See what unstructured AI analysis actually gives you.

## What Happens

Load the coffee shop sales data into any AI platform. Run one prompt. Observe the output without any structure, skills, or quality gates.

This milestone is not a failure demonstration. Raw AI analysis is genuinely useful. The lesson is about what it cannot tell you: where the numbers came from, what was assumed, and what was quietly skipped.

## Setup

1. Open your AI platform of choice (Claude.ai, ChatGPT, Gemini, GitHub Copilot)
2. Upload `shop-sales.csv` from `workspace-naive/data/`
3. No additional setup needed

## Suggested Prompts

See `prompts.md` for the milestone prompt sequence.

## What to Watch For

- Does the agent notice the mixed date formats?
- Does it mention that "HUB Coffee" has multiple name variants in the data?
- Does it flag the suspiciously flat sales at Suzzallo Roasters?
- Are the findings cited with source row ranges, or stated as confident assertions?

Spoiler: most platforms will produce confident-sounding output that glosses over these issues. That's the pedagogical point.

## Transition to Milestone 2

The output you get here is useful as a starting point. Ask yourself: "Would I present this to a VP without checking the numbers?" If the answer is no — that's what the rest of the workshop addresses.

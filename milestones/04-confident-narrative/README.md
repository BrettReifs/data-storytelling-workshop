# Milestone 4: The Confident Narrative

**Duration:** ~10 minutes  
**Workspace:** D3 — `workspace-harnessed/` (full skills suite)  
**Goal:** Produce a final, defensible data narrative. Demonstrate context scoping. Generate audience variants.

## What Happens

Two things happen in this milestone:

**First: Context Bleed Demo.** Load both the coffee shop data and job market data. Ask a question that could draw from either. Watch the agent blend context. Then fix it with scoping.

**Second: Final Report.** Generate the complete final HTML infographic with confidence scores, assumptions log, source lineage, and Shepherd.js spotlight tour. Produce three audience variants.

## Setup

See `setup.md` for any additional setup needed.

The harnessed workspace should have both datasets:
- `data/coffee-shops/` — 5 files
- `data/job-market/` — 3 files

## The Context Bleed Demo

1. Load both datasets into context simultaneously
2. Run the bleed prompt (see `prompts.md`)
3. Show the confused output — the agent may reference both datasets in the same answer
4. Fix: open `CLAUDE.md`, point to the dataset scoping rules
5. Re-run with explicit scoping — show the corrected output

## The Final Report

After the scoping fix:
1. Run the full final report prompt (see `prompts.md`)
2. The agent should invoke `html-infographic-builder` + `data-confidence-scorer` + `spotlight-walkthrough`
3. Open the HTML in browser
4. Run the spotlight tour
5. Compare side-by-side with the Milestone 2 naive infographic

## What to Watch For

- Context bleed: does the agent notice the ambiguity, or answer without flagging it?
- Confidence scores: are they meaningfully different for different claims?
- Spotlight tour: does it walk the story in a logical order?
- Side-by-side comparison: can students articulate the specific improvements?

## The Core Lesson

The data did not change between Milestone 2 and Milestone 4. The harness did. Skills + semantic layer + quality gates + context scoping = an analysis you can stake your name on.

## Transition to Q&A

This is the final milestone. Move to the recap slide, then open for questions.

---
name: data-refinement-interview
description: Conduct a focused pre-analysis interview to surface scope decisions, quality assumptions, and audience framing before generating a data report. Use when the user loads data and asks for analysis, says "analyze this," or when beginning a new data project. Asks 4 targeted questions drawn from a bank of 10, selected based on actual data characteristics. Hard cap: 5 questions.
---

# Data Refinement Interview

A semi-scripted pre-analysis interview that asks targeted questions before drawing conclusions from data. Prevents the most common failure modes: wrong metric definition, unresolved outliers, audience-agnostic framing, and silent assumptions about data quality.

## When to Use

- When data is loaded and the user asks for analysis — trigger this before writing a single finding
- Milestone 3 of the workshop: demonstrates what "structured reasoning" looks like vs. raw prompting
- Any analysis that will be shared with a decision-maker
- When data has visible quality issues (missing values, inconsistencies, anomalies)

## Question Bank (10 candidates — select 4, cap at 5)

**Category: Data Quality**
1. Several rows appear to have [identified inconsistency]. Should I standardize these to a single canonical value, or does the variation carry meaning I should preserve?
2. [X]% of [column] values are missing. Should I exclude those rows, impute with [method], or surface the gap as a finding?

**Category: Outliers**
3. [Shop/entity] shows [outlier pattern] that differs significantly from the others. Is this a data collection error I should exclude, or a real signal worth investigating?
4. There's a spike in [metric] during [time period]. Before I treat it as a trend, do you know of any external event that might explain it?

**Category: Metric Definition**
5. When you say "[metric term]," do you mean [interpretation A] or [interpretation B]? This affects how I calculate the headline number.
6. Should revenue figures be gross or net (after deducting cost-of-goods)? The catalog data supports either, but I need one definition to use consistently.

**Category: Audience Framing**
7. Who is the primary reader of this analysis — a shop manager, a campus VP, or a vendor procurement committee? Each gets a different emphasis.
8. Is this analysis meant to support a specific decision (e.g., renewing a vendor contract, reallocating budget), or is it an open-ended exploration?

**Category: Scope**
9. The dataset covers [date range]. Should I restrict the analysis to [recent period] for relevance, or use the full range to maximize statistical confidence?
10. I have [multiple files loaded]. Should I analyze them separately with cross-references, or combine them into a single unified view?

## Selection Logic

Before asking any questions, analyze the loaded data for:
- Name/format inconsistencies (triggers Q1)
- Missing value rate > 10% in a key column (triggers Q2)
- Statistical outliers (1.5× IQR or 3-sigma) (triggers Q3 or Q4)
- Ambiguous terminology in column names (triggers Q5 or Q6)
- Multiple files in context (triggers Q10)
- No explicit audience mentioned (always triggers Q7 or Q8)

Select the 4 questions that map to the most prominent issues found. If fewer than 4 issues are found, use Q7 (audience) as a default addition.

**Hard cap: never ask more than 5 questions in a single session.**

## Interview Conduct Rules

- Ask all selected questions at once (numbered list), not one at a time
- Phrase each question as it appears in the bank, but fill in the [placeholders] with specific values from the actual data
- Do not start analysis until all questions are answered
- Accept partial answers — do not re-ask unanswered questions
- After receiving answers: summarize your understanding in 3-4 bullet points, then confirm and proceed

## Output After Interview

```
Before I begin the analysis, let me confirm my understanding:

- "Revenue" = gross sales (total column), not net of cost-of-goods
- The Suzzallo flat-sales anomaly will be flagged but not excluded
- Primary audience: shop managers, with a one-page VP summary requested
- Analysis covers full 6-month window (July–December 2024)

Proceeding with EDA now.
```

## Acceptance Criteria

- [ ] Interview triggered before any analysis is written
- [ ] Questions are specific to the actual data loaded (placeholders filled)
- [ ] No more than 5 questions asked
- [ ] Questions asked together in one message, not sequentially
- [ ] Analysis does not begin until questions are answered (or user explicitly skips)
- [ ] Confirmation summary output before starting EDA

---
name: data-confidence-scorer
description: Annotate every claim in a data report with a confidence score (0-1), an assumptions log, data quality annotations, and source lineage. Use when the user asks to "add confidence scores," "document assumptions," "flag data quality issues," "add source citations," "make this defensible," or wants to audit an existing analysis for trustworthiness.
---

# Data Confidence Scorer

Annotates data findings with structured trust metadata: confidence scores, assumptions, quality flags, and source lineage. Transforms a plausible-sounding report into a defensible one.

## When to Use

- After a data analysis is complete — before presenting findings
- User asks to "add confidence," "document assumptions," or "make this auditable"
- User wants a report they can defend in a meeting
- Before generating a final HTML infographic, to ensure each claim is annotated
- Any analysis that will be shared with decision-makers who need to know how much to trust each number

## Inputs

- A list of findings, claims, or a draft data report
- The underlying data files (or a summary of them)
- Optional: the analysis methodology used

## Confidence Score Framework

Score each claim on a 0.0–1.0 scale based on the following factors:

| Factor | Reduces Confidence | No Penalty |
|--------|-------------------|------------|
| Sample size | < 30 rows | >= 100 rows |
| Missing data | > 20% null rate in relevant column | < 5% null rate |
| Outlier presence | Unresolved outlier in the distribution | Outliers investigated and resolved |
| Data inconsistency | Mixed formats, name variants, unit mismatches | Clean, standardized column |
| Temporal coverage | < 30 days of data | >= 90 days |
| Cross-file dependency | Claim requires joining 2+ files with no documented key | Clean join on validated key |

Score buckets:
- **0.85–1.0**: High confidence. Cite as fact with source.
- **0.65–0.84**: Moderate confidence. Present as finding, note caveats.
- **0.40–0.64**: Low confidence. Flag as preliminary. Recommend validation.
- **< 0.40**: Unreliable. Do not include in executive summary. Flag for data remediation.

## Process

For each claim or finding:

1. Identify the data source (file name, column name, row count used)
2. Check for quality issues in the relevant data: nulls, inconsistencies, outliers, format problems
3. Assign a confidence score using the framework above
4. Write a one-sentence assumption statement: what had to be true for this conclusion to hold
5. Add a quality annotation if any issue was present
6. Document source lineage: `file.csv :: column_name :: rows N–M (n=X)`

## Output Format

Annotate each claim in this structure:

```
CLAIM: [the finding in plain language]
CONFIDENCE: 0.82
SCORE RATIONALE: 6-month data window, no missing values in revenue column,
  outlier in week 18 investigated and attributed to viral post (documented)
ASSUMPTION: "Suzzallo Roasters" in shop-sales.csv refers to the same entity
  as "suzzallo-roasters" — treated as canonical after manual review
DATA QUALITY: Shop name inconsistency across files — 3 variants for S1 (HUB Coffee).
  Resolved by grouping. Confidence reduced 0.05 for that shop's figures.
SOURCE LINEAGE: shop-sales.csv :: total :: rows 1–45835 (n=45835, date range 2024-07-01–2024-12-31)
```

For HTML reports, embed annotations as:
- Inline `<span class="confidence-badge">0.82</span>` next to each claim
- A collapsible `<details>` block with the full annotation
- A summary assumptions log in the report footer

## Quality Rules

- Every claim in an executive summary must have a confidence score
- Claims with confidence < 0.50 must not appear in an executive summary without a prominent caveat
- Assumptions log must be included in every report (even if short)
- Source lineage must specify: file name, column(s), row count, date range if temporal

## Acceptance Criteria

- [ ] Every claim has a numeric confidence score
- [ ] Every claim has at least one assumption documented
- [ ] Data quality issues in the source data are reflected in reduced scores
- [ ] Source lineage links each claim to a file + column + row range
- [ ] Claims below 0.50 are explicitly flagged
- [ ] Assumptions log section present in the final output

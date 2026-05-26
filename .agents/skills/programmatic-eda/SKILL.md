---
name: programmatic-eda
description: Run a systematic data quality scan before analysis begins. Checks column types, null rates, outliers (1.5x IQR), format inconsistencies, and cross-file key integrity. Use when starting analysis on a new dataset, after the data-refinement-interview, or when asked to "scan the data," "check data quality," "run EDA," or "surface data issues." Outputs a structured quality report with row-level citations before any findings are generated.
---

# Programmatic EDA

Performs a systematic exploratory data analysis scan that surfaces data quality issues before any findings are generated. This is what separates a defensible analysis from a plausible-sounding one.

## When to Use

- After `data-refinement-interview` completes and interview answers are confirmed
- When a user loads new data and asks to "run EDA," "check the data," or "scan for issues"
- Before generating any analysis, report, or visualization
- Milestone 3: the agent runs this scan autonomously after the refinement interview

## Process

### Pass 1: Structure Check
For each file loaded:
1. Report column names, inferred types, and row count
2. Identify columns with ambiguous or mixed types (e.g., dates stored as strings)
3. Flag columns with abbreviations or acronyms that lack clear meaning

### Pass 2: Completeness Check
For each column:
1. Count null, missing, and empty values; report as a percentage
2. Null rate > 10%: flag as quality issue with file + column name
3. Null rate > 30%: flag as potential structural problem

### Pass 3: Consistency Check
For each column:
1. String columns: detect case variants, whitespace differences, and apparent duplicates (e.g., "HUB Coffee" vs "hub-coffee" vs "The HUB")
2. Date columns: detect mixed format strings (ISO vs MM/DD/YYYY vs DD-MM-YYYY)
3. Numeric columns: detect values that appear to be encoded strings (e.g., "$1,234")
4. Flag each inconsistency with: column name, examples of variants found, estimated row count affected

### Pass 4: Outlier Check
For each numeric column with >= 30 non-null rows:
1. Compute IQR; flag values outside 1.5x IQR as potential outliers
2. For time-series data: flag runs of suspiciously identical or zero values (possible POS sync issues)
3. Report: column, outlier count, example values, whether they appear systematic or random

### Pass 5: Cross-File Check (when multiple files are loaded)
1. Identify potential join keys (shared column names or apparent entity identifiers)
2. Check referential integrity: are all key values in one file present in the other?
3. Flag orphaned records with count and examples

## Output Format

```
## Data Quality Scan — [filename(s)] — [date]

### Structure
- shop-sales.csv: 45,835 rows × 6 columns (date, shop_id, item, quantity, unit_price, total)
  - `date`: mixed types — ISO 8601 and MM/DD/YYYY detected (see Consistency)

### Completeness
- vendor-bids.csv :: quote_amount: 22.3% null (1,087 / 4,875 rows)
  FLAG: expected missing data per procurement rules
- All other key columns: < 2% null — PASS

### Consistency
- shop-sales.csv :: shop_id: 3 variants detected for entity S1
  "HUB Coffee", "hub-coffee", "The HUB" (~12,400 rows affected)
- shop-sales.csv :: date: ~15% of rows use MM/DD/YYYY instead of ISO (~6,875 rows)

### Outliers
- shop-sales.csv :: total (Suzzallo Roasters, S3): 47 consecutive days of identical
  $312.00 daily totals starting 2024-10-01 — FLAG: possible POS sync issue
- social-signals.csv :: engagement: spike of 8,400 on 2024-08-22 for HUB Coffee
  (3.8x IQR above baseline) — FLAG: investigate before averaging

### Cross-File Integrity
- shop-sales.csv × menu-catalog.json: 2 item codes in sales not found in catalog (retired items)

### Summary
Issues found: 5 (2 critical, 3 advisory)
Recommended actions before analysis:
1. Standardize shop name variants — treat "HUB Coffee", "hub-coffee", "The HUB" as S1
2. Normalize date formats to ISO 8601
3. Investigate S3 flat-sales before including in trend analysis
```

## Quality Rules

- Never skip a pass because the dataset "looks clean"
- Always cite: file name, column name, and approximate row count affected
- Distinguish between critical issues (block analysis) and advisory issues (note and proceed)
- Do not draw conclusions during this scan — report only, analyze after

## Acceptance Criteria

- [ ] All 5 passes executed for each file loaded
- [ ] Every flagged issue includes: file name, column, row count estimate, severity (critical/advisory)
- [ ] Cross-file check run when multiple files are loaded
- [ ] No analysis or conclusions drawn during the scan
- [ ] Scan output precedes any EDA findings

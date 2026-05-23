# Job Market Data — Dictionary

Synthetic data representing the Seattle-area data analytics job and internship market, 2024-2025. Introduced in Milestone 4 for the context-scoping demo.

---

## job-postings.csv

400 synthetic job postings for data analytics roles in the Seattle metro area.

| Column | Type | Description |
|--------|------|-------------|
| `posting_id` | string | Unique posting ID (JOB-0001 format) |
| `title` | string | Job title — **inconsistent variants** across postings |
| `company` | string | Employer name |
| `location` | string | City/state or "Remote" |
| `work_type` | string | Remote, Hybrid, or On-site |
| `salary_min` | integer | Minimum salary (empty if not disclosed) |
| `salary_max` | integer | Maximum salary (empty if not disclosed) |
| `required_skills` | string | Semicolon-separated skill list |
| `experience_years` | integer | Years of experience required |
| `posted_date` | string | ISO posting date |
| `uw_partnership` | boolean | Whether company has a UW recruiting partnership |
| `is_duplicate_flag` | boolean | Flagged as a likely duplicate from aggregator |
| `status` | string | Active or Expired |

**Known Quality Issues:**
- `title`: "Data Analyst" appears as "Jr. Data Analyst," "Analyst, Data," "Associate Data Analyst," etc. Standardize before counting or grouping.
- `salary_min` / `salary_max`: empty on ~30% of rows. Missing at random, not systematically.
- `status = Expired`: ~8% of rows are old listings (2023) still in the feed from aggregator sources.
- `is_duplicate_flag = true`: ~5% of rows are near-duplicate postings from the same company.

See [`../QUALITY-ISSUES.md`](../QUALITY-ISSUES.md) for root cause analysis and real-world frequency assessment of all quality issues.

**Row count:** 400

---

## internship-programs.csv

100 synthetic internship listings for data analytics roles, primarily summer 2025.

| Column | Type | Description |
|--------|------|-------------|
| `intern_id` | string | Unique ID (INT-001 format) |
| `company` | string | Employer name |
| `role` | string | Internship role title |
| `duration_weeks` | integer | Program length in weeks |
| `compensation` | string | Weekly rate or "Unpaid / Credit" |
| `location` | string | City/state, Remote, or Hybrid |
| `start_term` | string | Summer 2025, Fall 2025, etc. |
| `uw_partnership` | boolean | Whether company has a UW recruiting partnership |
| `application_deadline` | string | ISO deadline date |
| `openings` | integer | Number of open spots |

**Note:** `compensation` is a string field (e.g., "$1,000/week"), not a numeric. Parse out the dollar amount for salary analysis.

---

## skills-demand.csv

Aggregated skill frequency counts by role category, derived from the job postings.

| Column | Type | Description |
|--------|------|-------------|
| `skill` | string | Skill name |
| `skill_category` | string | Technical, Visualization, Analytical, Soft, or Cloud |
| `role_category` | string | One of 6 role categories |
| `posting_count` | integer | Number of postings mentioning this skill |
| `pct_of_postings` | float | Percentage of total postings |
| `yoy_change_pct` | float | Year-over-year demand change |
| `median_salary_premium` | integer | Estimated median salary premium for this skill |

**Row count:** 180 (30 skills × 6 role categories)

---

## Context Scoping Note

This dataset is intentionally loaded alongside the coffee shop data in Milestone 4 to demonstrate context bleed. Prompts like "what is the average revenue?" or "what are the top metrics?" can draw from both datasets simultaneously without proper scoping.

The fix is in `workspace-harnessed/CLAUDE.md` — explicit dataset scoping rules prevent cross-contamination.

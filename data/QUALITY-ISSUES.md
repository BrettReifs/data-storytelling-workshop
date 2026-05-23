# Data Quality Field Guide

A rationalized breakdown of every intentional quality issue in this workshop's datasets.

For each issue: what caused it, how common this pattern is in the real world, and the standard remediation.

---

## Coffee Shop Data

### 1. Mixed date formats in `shop-sales.csv`

**The issue:** Approximately 15% of rows use `MM/DD/YYYY` (e.g., `07/01/2024`). The remaining 85% use ISO 8601 (`YYYY-MM-DD`). Both formats appear in the same column.

**What caused this:**  
Two POS (Point of Sale) systems were in use simultaneously. The older system — installed before the university's 2021 IT standardization push — exports dates in the US format common to its legacy codebase. When the university rolled out a new cloud-based POS across three shops, the export format changed to ISO 8601. The migration was staggered: some shops switched mid-fiscal-year. The central reporting pipeline ingested CSVs from both systems without a normalization step, because the analyst who built the pipeline assumed all files used the same format.

**How common is this:**  
Extremely common — arguably the most frequently encountered date issue in real-world analytics pipelines. Any organization that has upgraded, merged, or replaced systems over time without enforcing a data standard will have it. Triggers include: ERP migrations, acquisitions, multi-vendor integrations, and manual data entry by staff in different regions (the US is one of the few countries that still defaults to MM/DD). In practice, mixed date formats are the rule rather than the exception in mid-size organizations.

**Standard remediation:**  
Date parsing with explicit format detection before normalization to a canonical format. In Python: `pd.to_datetime(col, infer_datetime_format=True)` handles most cases, but edge cases (e.g., `01/02/2024` — is that January 2nd or February 1st?) require a documented assumption.

---

### 2. Shop name inconsistency across files

**The issue:** "HUB Coffee" (shop S1) appears as `HUB Coffee`, `The HUB`, `hub-coffee`, and `HUB` across the five data files. Similar variation exists for other shops at lower frequency.

**What caused this:**  
Four separate data entry contexts, none of which talk to each other:

| System | Name Used | Why |
|--------|-----------|-----|
| POS export | `hub-coffee` | Internal slug used for database keys |
| Social media dashboard | `The HUB` | Public brand name used by the marketing team |
| Vendor contract system | `HUB Coffee` | Legal entity name on the master vendor agreement |
| Staff scheduling app | `HUB` | Abbreviated name favored by operations staff |

No master data management (MDM) layer exists to enforce a canonical name. Each system was set up independently. When the analyst pulled data for a consolidated report, the names came from whichever field each system populated — and they were never the same.

**How common is this:**  
Ubiquitous in organizations without MDM. This pattern appears with customer names, product SKUs, supplier names, and location identifiers. It is one of the top reasons data analysts spend more time on data preparation than on actual analysis. A 2023 survey by Monte Carlo Data found that entity name inconsistency was the leading cause of data trust failures in BI tools across mid-market companies.

**Standard remediation:**  
Build a reference table mapping every variant to a canonical name. In SQL: a lookup join. In Python: a dictionary replace or fuzzy-match library (`rapidfuzz`, `thefuzz`). Long-term fix: an MDM system that enforces canonical entity names at the point of entry.

---

### 3. Suspiciously flat daily sales at Suzzallo Roasters (S3)

**The issue:** Shop S3 shows 28-32 transactions per day every day for the entire observation period, with almost no variance. Every other shop shows natural variation (weekday/weekend swings, weather effects, event-driven spikes). The numbers are not zero and not obviously wrong — they just look like a quiet shop having an uncannily consistent day, every day.

**What caused this:**  
A software update to Suzzallo's POS system in early October 2024 introduced a configuration error: the system began caching transactions locally rather than syncing to the central reporting database in real time. The cached records were forwarded to the database in batches at the end of each day, but the batch job had a fixed transaction limit — it would send at most 30 records per run. Transactions beyond that limit were queued and never retried. The result was a daily ceiling of approximately 30 records regardless of actual sales volume. IT identified the issue in a November maintenance report, but the historical data was never corrected.

**How common is this:**  
Moderately common in any physical retail or hospitality environment with on-premise hardware. Connectivity failures, sync errors, caching bugs, and configuration drift in POS or IoT systems are recurring operational realities. What makes this pattern particularly dangerous analytically is that the data does not look wrong at a glance — it looks like a quiet but consistent location. Detecting it requires variance analysis or comparison to baseline expectations, not just a null check.

**Standard remediation:**  
Compare variance across peer entities. A coefficient of variation (CV) that is near zero while peer entities show 15-30% CV is a red flag. Cross-reference against staffing records or foot-traffic data if available. Flag for source-system audit before including in any aggregate metric.

---

### 4. Missing values in `vendor-bids.csv`

**The issue:** Approximately 20% of `price_quoted` rows are empty. The missing pattern is not random — it corresponds to vendors who did not submit quotes for all line items.

**What caused this:**  
The university's procurement system sends bid requests to all approved vendors for every line item in the sourcing package. Vendors are not required to respond to every item. A coffee equipment specialist may not bid on cleaning supplies. A bulk commodity supplier may not bid on annual machine maintenance contracts. The system records absence of a bid as an empty field, not as "No bid submitted" or a null-coded flag. Analysts who do not read the data dictionary may interpret the empty as an unknown price, zero, or data error.

**How common is this:**  
Very common in procurement, survey, and CRM data — anywhere that responses are voluntary per item. RFP (Request for Proposal) datasets routinely have 15-30% partial response rates. The same pattern appears in customer satisfaction surveys (not all customers answer all questions), clinical trial data (not all patients complete all assessments), and sales CRM records (reps fill in the fields they care about). The key distinction is that "not applicable" and "unknown" mean different things analytically, and empty fields collapse both into one ambiguous state.

**Standard remediation:**  
Document the business meaning of empty in the data dictionary (which this repo does). Use separate columns or coded flags for "not applicable" vs. "unknown" in future designs. For analysis: exclude empties from price comparisons; count them separately as "vendors without a qualifying bid."

---

### 5. Viral outlier in `social-signals.csv`

**The issue:** Week 18 shows engagement metrics for HUB Coffee (S1) that are 47 times higher for likes and 85 times higher for shares than the shop's baseline. The engagement rate for that week is not comparable to any other week in the dataset.

**What caused this:**  
During homecoming week in October 2024, a UW student posted a 45-second TikTok video filmed at the HUB Coffee location. The video accumulated 2.3 million views over 72 hours, driven partly by a tag from a mid-tier food influencer. The weekly social metrics aggregate — which sums all engagement across all posts — was dominated entirely by this single event. The `engagement_rate` metric (likes + comments divided by follower count) became a meaningless operational benchmark for that week, since the denominator (followers) had not changed but the numerator reflected reach far beyond the shop's organic audience.

**How common is this:**  
Viral events are uncommon in absolute terms but not rare enough to ignore. Any brand-adjacent account — even a small campus coffee shop — can be caught in a viral moment through user-generated content. The measurement problem this creates is well-documented: aggregate metrics that blend organic performance with viral spikes produce misleading trend lines. Most analytics practitioners who work with social data handle this with outlier detection, period exclusion, or separate tracking of organic vs. viral reach. The failure mode is including the spike in a rolling average, which inflates the "normal" baseline and makes every subsequent week look underperforming by comparison.

**Standard remediation:**  
Flag outliers using statistical thresholds (e.g., values beyond 3 standard deviations from the rolling mean). Segment analysis by "organic weeks" vs. "event-affected weeks." For KPI reporting, use median engagement rate rather than mean, which is more robust to extreme values.

---

## Job Market Data

### 6. Inconsistent job titles in `job-postings.csv`

**The issue:** "Data Analyst" appears as `Data Analyst`, `Jr. Data Analyst`, `Analyst, Data`, `Associate Data Analyst`, and `Data Analyst I` — all referring to the same entry-level data role category. Similar variation exists across all eight role groups.

**What caused this:**  
The dataset aggregates postings from six sources: company career pages, LinkedIn, Indeed, Handshake, a university career center portal, and a staffing agency feed. Each source uses its own title taxonomy. The same role posted by the same company appears differently across channels: the company's career page uses their internal job architecture title (`Data Analyst I`), the LinkedIn post was entered manually by a recruiter who shortened it (`Jr. Data Analyst`), and the Indeed syndication transformed it through an automated category mapping (`Analyst, Data`). No normalization was applied at ingestion because the pipeline was built to collect volume, not standardize structure.

**How common is this:**  
Pervasive — arguably the defining data quality challenge of job market analytics. It is why O*NET, LinkedIn's Economic Graph team, Burning Glass (now Lightcast), and others have invested years and significant NLP resources into job title standardization models. Any labor market analysis that groups roles by title without a normalization step will miscount demand, misattribute skills, and produce misleading salary benchmarks. The broader principle applies anywhere human beings enter free-text into fields that should be controlled vocabularies: product categories, medical procedures, company industry codes.

**Standard remediation:**  
Build or adopt a title normalization taxonomy. Options range from a hand-curated lookup table (sufficient for workshop-scale data) to NLP-based classification using a pre-trained model fine-tuned on job titles. For SQL analysis: a `CASE WHEN` statement mapping known variants to canonical groups. Document the mapping decisions as they affect all downstream counts.

---

### 7. Missing salary ranges (~30% of rows)

**The issue:** `salary_min` and `salary_max` are empty on approximately 30% of job postings. The missing pattern correlates weakly with company size — smaller companies and staffing agencies are more likely to omit salary data.

**What caused this:**  
Three converging factors. First, salary disclosure has historically been voluntary in most US jurisdictions, and many companies treat compensation as confidential until the offer stage. Second, Washington's Equal Pay and Opportunities Act requires salary range disclosure for job postings, but enforcement and awareness have been uneven — smaller companies are less likely to comply consistently. Third, some roles — particularly senior positions where total compensation includes equity and negotiable components — are posted without finalized salary bands because the compensation committee has not yet approved the range.

**How common is this:**  
Common and shifting. Before state-level pay transparency laws (Colorado 2021, Washington 2023, California 2023, New York City 2022), missing salary data was the majority of postings on most aggregators. Post-legislation, the missing rate in compliant jurisdictions has dropped to 20-40% and continues to fall. For multi-state aggregators, the effective missing rate reflects a weighted mix of jurisdictions. The practical impact for analysts: any median salary calculation on this dataset is a median of disclosed salaries, not of all salaries — and disclosed salaries skew toward roles where companies felt comfortable being transparent, which may not be representative.

**Standard remediation:**  
Disclose the missing rate and selection bias explicitly in any salary analysis. Consider imputation only if you have a reliable reference dataset (e.g., BLS Occupational Employment Statistics). For group comparisons, use disclosed-only figures but report both the N and the missing rate for each group.

---

### 8. Expired listings mixed with active (`status = Expired`)

**The issue:** Approximately 8% of postings have a `posted_date` from 2023 — prior to the nominal data collection window — and carry `status = Expired`. They are present in the same dataset as 2024 active listings.

**What caused this:**  
Job aggregators cache listings and do not always receive deletion notifications from source systems. When a company fills a role and removes the posting from their career page, the aggregator's copy persists until the cache expires — which varies by vendor from 30 days to indefinitely. Some aggregators deliberately retain expired listings because they improve search engine indexing. The data pipeline that assembled this dataset ingested a full export from the aggregator rather than filtering by status or recency at collection time, because status codes are set by the aggregator (not the original poster) and are not always reliable.

**How common is this:**  
Very common in any dataset sourced from job aggregators. Industry practitioners routinely apply a 90-day recency filter as a standard pre-processing step. The problem is familiar enough that "zombie listings" has become an informal term in HR analytics. The analytical impact: without filtering, demand analysis overstates the number of open roles, inflates apparent skill frequency counts, and may include salary data from a different market period.

**Standard remediation:**  
Filter on `posted_date >= [reference_date - 90 days]` and `status = Active` before any demand or salary analysis. Treat the expired listings as a data provenance issue, not as useful historical data, unless a longitudinal study is the explicit goal.

---

### 9. Duplicate postings (`is_duplicate_flag = true`, ~5% of rows)

**The issue:** Approximately 5% of postings are near-duplicates: same title, same company, overlapping date ranges, appearing as separate records.

**What caused this:**  
Two mechanisms. First, the same job opening was posted by the company on their own career page and then syndicated automatically to LinkedIn, Indeed, and Handshake — each syndication creating a separate record in the aggregated dataset. Second, companies routinely "refresh" postings after 30 days to improve search visibility on aggregator platforms; a refreshed posting gets a new record ID and a new date, making it appear as a new opening. The aggregator does not de-duplicate across sources or across refresh cycles.

**How common is this:**  
Common in any dataset assembled from multiple job aggregators. Industry estimates put the effective duplication rate at 5-20% depending on how many sources are included and how aggressively the aggregator normalizes. The analytical impact is meaningful: at 5% duplication, a raw count of 400 postings in this dataset represents closer to 380 unique roles. At scale, this inflates apparent demand, inflates apparent skill frequency counts, and can bias any metric calculated per-posting rather than per-role.

**Standard remediation:**  
De-duplicate using fuzzy matching on `(title, company, location)` within a rolling date window (e.g., same company, same normalized title, same location, within 45 days = duplicate). The `is_duplicate_flag` column in this dataset pre-labels the known duplicates for workshop use; in a real pipeline you would detect them programmatically.

---

## Frequency Summary

| Issue | How Common | Risk if Unaddressed |
|-------|-----------|---------------------|
| Mixed date formats | Extremely common | Silent parsing errors, wrong date ranges |
| Entity name inconsistency | Ubiquitous without MDM | Undercounting/overcounting by entity |
| Flat-data anomaly (POS sync failure) | Moderately common | Misleading benchmarks for affected entity |
| Missing values (voluntary response) | Very common in procurement/survey | Biased averages, misread as zero |
| Viral outlier | Uncommon but unpredictable | Inflated averages, false baselines |
| Inconsistent job titles | Pervasive in HR data | Miscount of demand, broken skill attribution |
| Missing salary ranges | Common, jurisdiction-dependent | Selection bias in salary benchmarks |
| Expired listings | Very common in aggregated data | Inflated demand counts |
| Duplicate postings | Common in multi-source aggregates | Inflated counts, biased frequency analysis |

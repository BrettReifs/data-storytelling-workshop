# Milestone 4 — Suggested Prompts

---

## Part A: Context Bleed Demo

### Prompt 1: Trigger Context Bleed

Load both `shop-sales.csv` AND `job-postings.csv` into context first, then:

```
What is the average revenue for data analysts in Seattle?
```

This question blends "revenue" (coffee shop data) with "data analysts in Seattle" (job market data).
Watch what the agent produces.

---

### Prompt 2: Explicit Ambiguity Test

```
What is the average salary?
```

One dataset has `salary_min`/`salary_max`. The other has `total` (revenue). The agent should ask which dataset — or may make a silent assumption.

---

### Prompt 3: The Scoping Fix

After demonstrating the bleed, reference the CLAUDE.md rules:

```
Using only the coffee shop dataset (data/coffee-shops/), what is the average daily revenue per shop?
```

Show how explicit dataset references prevent the bleed.

---

## Part B: Final Report Generation

### Prompt 4: Full Confident Narrative

```
Using the coffee shop data only, generate the final data narrative report.
Apply all skills: data-confidence-scorer for every claim, html-infographic-builder
for the visual output, and spotlight-walkthrough for the guided tour.
Produce three audience variants: shop manager, campus VP, and vendor committee.
```

---

### Prompt 5: Audience Variant Emphasis

If the agent needs guidance on audience framing:

```
For the shop manager variant, emphasize daily foot traffic, supply cost per unit sold,
and staff scheduling efficiency.
For the campus VP variant, emphasize aggregate revenue trends and brand consistency scores.
For the vendor committee variant, emphasize comparative vendor pricing, delivery reliability,
and contract ROI projections.
```

---

## Part C: Side-by-Side Comparison

### Prompt 6: Articulate the Difference

After generating the final report:

```
Compare the report you just generated to the naive infographic from Milestone 2.
List the specific improvements — what does this report have that the other did not?
```

Use the agent's own words to close the lesson.

---

## Reflection Questions for Students

1. What would happen to your career if you presented the Milestone 2 report and the numbers were wrong?
2. What would happen if you presented the Milestone 4 report and someone challenged a finding?
3. Which of the six skills would be most useful for your own data projects?
4. What would it take to build a harness like this for your team?

# Milestone 3 — Suggested Prompts

Run these in the harnessed workspace with skills loaded.

---

## Prompt 1: Trigger the Refinement Interview

```
I have the UW campus coffee shop data loaded. Before we begin the analysis,
run the data-refinement-interview skill to identify the right scope and assumptions.
```

Or simply load the data and say:
```
Analyze this data.
```

The `data-refinement-interview` skill should trigger automatically when analysis is requested.

---

## Prompt 2: After the Interview — Structured EDA

After answering the interview questions:

```
Now run a full exploratory data analysis on the coffee shop data.
Apply the data quality protocol, flag all issues, and summarize findings
with confidence annotations.
```

---

## Prompt 3: Compare to Naive Output

```
Summarize the 3 most important findings. For each finding, include:
- The confidence score
- The data quality issues that affected this finding
- What assumption you made to reach this conclusion
```

---

## Reflection Questions for Students

1. What questions did the interview ask that you would not have thought to ask?
2. Which quality issues did the harnessed analysis surface that the naive pass missed?
3. Did the confidence scores change how you think about any of the findings?
4. What would it cost (time, effort) to build a harness like this for your own data project?

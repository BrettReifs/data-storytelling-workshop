# Milestone 2 — Suggested Prompts

---

## Prompt 1: The Infographic Request

```
Create a standalone HTML infographic report from this data.
Include at least 3 charts showing key metrics, use professional styling,
and make it something I could share with a stakeholder.
The file should be completely self-contained — no external dependencies
other than CDN links.
```

---

## Prompt 2: Add a Specific Chart

If the first output is missing something you want to highlight:

```
Add a chart showing the comparison between all 5 shops by total revenue.
Make sure all shop names are consistent in the chart labels.
```

Note whether the agent handles the name inconsistency or silently picks one variant.

---

## Prompt 3: Test the Foundation

After reviewing the output:

```
For the [specific number] you showed in the report —
what rows in the data support that figure?
Is that calculation correct given the date format inconsistency in the file?
```

This often reveals that the agent made silent assumptions about date parsing.

---

## Reflection Questions for Students

1. Compare this output to Milestone 1. What improved?
2. What is still missing that you would need to trust this report?
3. If a chart shows "Average Daily Revenue: $X" — how do you know that's right?
4. What would a data quality disclosure section look like in this report?

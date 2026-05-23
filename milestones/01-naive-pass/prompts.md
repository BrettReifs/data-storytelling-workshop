# Milestone 1 — Suggested Prompts

Platform-agnostic. Use with any AI assistant that supports file uploads.

---

## Prompt 1: The Naive Analysis

```
Analyze this data and tell me what's interesting.
```

Run this with `shop-sales.csv` attached. Let it run without guidance.

---

## Prompt 2: Dig Into a Finding

After the initial response, push on one of the findings:

```
You mentioned [finding the agent produced]. How confident are you in that?
What data supports it exactly?
```

Substitute the actual finding from the response. Watch whether the agent can cite specific rows or date ranges.

---

## Prompt 3: Ask About Quality

```
Are there any data quality issues in this file I should know about before using these findings?
```

This often surfaces some issues — but rarely all of them. Note what it misses.

---

## Reflection Questions for Students

After running these prompts:

1. Which findings felt trustworthy? Which felt like guesses?
2. Did the agent disclose any assumptions it made?
3. Could you reproduce any of these findings manually in Excel?
4. Would you send this output to your manager as-is?

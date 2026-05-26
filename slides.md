---
theme: default
title: "From Raw Data to Confident Narratives"
titleTemplate: "%s — UW Foster"
info: |
  Workshop: From Raw Data to Confident Narratives
  Agent-Driven Data Storytelling
  UW Foster School of Business, May 2026
  Presenter: Brett Reif
drawings:
  persist: false
transition: slide-left
css: unocss
fonts:
  sans: Inter
  mono: JetBrains Mono
---

---
layout: cover
class: hero
---

<div class="hero-grid">
  <div class="hero-left">
    <div class="uw-label mb-4">UW Foster School of Business · Data Analytics</div>
    <h1>From Raw Data to<br>Confident Narratives</h1>
    <div class="uw-rule mt-3 mb-4"></div>
    <p class="hero-tagline"><strong>Agent-Driven Data Storytelling</strong></p>
  </div>
  <div class="hero-right">
    <div class="hero-photo-wrap">
      <img src="/profile-brett.jpg" alt="Headshot of Brett Reifers, Senior Product Manager at Microsoft" class="hero-photo" />
    </div>
    <div class="hero-presenter-name">Brett Reifers</div>
    <div class="hero-presenter-role">Senior Product Manager, Microsoft</div>
  </div>
</div>

<style scoped>
.hero-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 3rem;
  align-items: center;
  width: 100%;
}
.hero-left {
  min-width: 0;
}
.hero-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 0.5rem;
}
.hero-photo-wrap {
  width: 240px;
  height: 240px;
  border-radius: 16px;
  overflow: hidden;
  border: 3px solid var(--uw-gold-bright, #D4A853);
  box-shadow: 0 10px 32px rgba(75, 46, 131, 0.35);
  margin-bottom: 0.75rem;
}
.hero-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 20%;
}
.hero-presenter-name {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #ffffff;
}
.hero-presenter-role {
  font-size: 0.95rem;
  color: #F6F1FA;            /* solid light tint; 4.7:1 on the lightest band of the purple gradient, passes WCAG AA */
  line-height: 1.4;
  max-width: 24ch;
}
</style>

<!--
Welcome. This workshop is one hour, four milestones, two workspaces, and one question that matters: how do you know when to trust what the AI is telling you about your data?

We are not here to debate whether AI can analyze data. It can. We are here to learn how to make it do so in a way that produces findings you can stand behind.
-->

---
layout: center
class: hero
---

<div class="h-full w-full flex flex-col justify-center">
  <div class="uw-label mb-6">The Context</div>
  <div style="font-size: clamp(2rem, 5.2vw, 4.5rem); line-height: 1.08; font-weight: 800; max-width: 16ch;">
    You will prototype a story with data for me in the next 45 minutes.
  </div>
</div>

<!--
Set the room with a single concrete expectation before moving into the challenge slide.
Pause after reading this line so students feel the time constraint.
-->

---
layout: default
class: section
---

<div class="uw-label mb-6">The Problem</div>

# Turning data into a clear narrative is hard

<div class="uw-rule mt-4 mb-6"></div>

<div class="grid grid-cols-[1fr_auto_1fr] gap-4 items-stretch mb-5">
  <div class="p-5 rounded-xl border-2" style="border-color: #93c5fd; background: #eff6ff; color: #0f172a;">
    <div class="font-semibold text-lg">What raw analysis gives you</div>
    <ul class="mt-3 space-y-2" style="padding-left: 1.1rem; margin: 0.75rem 0 0 0;">
      <li>Revenue and volume trends</li>
      <li>Segment-level performance cuts</li>
      <li>Early chart directions</li>
    </ul>
  </div>
  <div class="self-center px-3 py-1 rounded-full" style="background: var(--uw-purple); color: #ffffff; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em;">VS</div>
  <div class="p-5 rounded-xl border-2" style="border-color: #fcd34d; background: #fffbeb; color: #1a0a30;">
    <div class="font-semibold text-lg">What stakeholders still need</div>
    <ul class="mt-3 space-y-2" style="padding-left: 1.1rem; margin: 0.75rem 0 0 0;">
      <li>A clear business story</li>
      <li>Assumptions and caveats</li>
      <li>Risks and tradeoffs</li>
    </ul>
  </div>
</div>

How do you know when a story is "good enough?"

<div class="mt-8 p-4 rounded-lg border-l-4" style="border-color: var(--uw-gold-bright); background: var(--uw-gold-pale); color: #1a0a30;">
<strong>The gap is not capability. It is confidence.</strong><br>
Raw output is a rough draft, not a decision-ready narrative.
</div>
<!--
The problem isn't that AI hallucinates — though it can. The problem is that even when the output is technically correct, there's no trail. No assumptions log. No confidence markers. No way to know what question it thought you asked.

Click through each point, pause on the VP question. Ask the room: raise your hand if you've ever gotten AI output and wondered whether to trust it.
-->

---
layout: two-cols
class: reveal
---

<div class="uw-label mb-4">What We Will Build</div>

# Before vs. After

<div class="uw-rule mt-3 mb-6"></div>

**Milestone 1 output**

- Unstructured observations
- Charts without sourcing
- No quality flags
- Confident tone, shaky foundation

**Milestone 2 output**

- Pretty HTML infographic
- Looks professional
- Still no confidence trail

::right::

<div class="mt-12"></div>

**Milestone 4 output**

- Every claim has a confidence score
- Assumptions logged
- Data quality issues flagged inline
- Source lineage: file, column, row range
- Spotlight tour walks the narrative
- Three audience variants from one analysis

<div class="mt-8 p-4 rounded-lg" style="background: var(--uw-purple-light); color: #1a0a30;">
<strong>Same data. Different harness.</strong><br>
That's the whole lesson.
</div>

<!--
Show the side-by-side visually if you have reference infographics ready. If not, describe the contrast verbally and let the live demo make the case.
-->

---
layout: default
class: section
---

<div class="uw-label mb-6">The Scenario</div>

# The Data: UW Campus Coffee Shops

<div class="uw-rule mt-4 mb-6"></div>

As data specialists entering AI-first teams, this is your reality: more data than time, uneven quality, and instant AI-generated outputs.

**The real challenge is not speed. It is delivering analysis leaders can trust and defend.**

| File | What It Contains |
|------|-----------------|
| `shop-sales.csv` | ~46k daily transactions, 6 months |
| `menu-catalog.json` | 78 menu items, pricing, cost-of-goods |
| `social-signals.csv` | Weekly social metrics, all shops |
| `vendor-bids.csv` | 5 vendors, 8 line items, partial quotes |
| `shop-profiles.md` | Location, equipment, lease costs |
<div class="mt-6 p-4 rounded-lg border-l-4" style="border-color: var(--uw-gold-bright); background: var(--uw-gold-pale); color: #1a0a30;">
The data has issues. Intentional ones. Finding them is part of the workshop.
</div>
<!--
Don't name the issues yet — let students discover them in the demo. This slide just establishes the scenario.

If students ask: "Is this real data?" The answer is: it's synthetic but realistic. The quality issues mirror what you will see in actual enterprise datasets.
-->

---
layout: default
class: section
---

<div class="uw-label mb-3">Milestone 1 of 4</div>

# The Naive Pass

<div class="uw-rule mt-3 mb-6"></div>

**What we do:** Load the coffee shop data into any AI platform. One prompt. No setup.

**The prompt:**
```
Analyze this data and tell me what's interesting.
```

**What we observe:** What does unstructured analysis actually give you?

<div class="mt-8 p-4 rounded-lg" style="background: #f0f9ff; color: #1a0a30; border: 1px solid #bae6fd;">
<strong>Follow along:</strong> Open your AI platform of choice (Claude.ai, ChatGPT, Gemini, Copilot). Upload <code>shop-sales.csv</code> and run the same prompt.
</div>

<!--
Switch to Desktop 2 (naive workspace). Open VS Code, no skills installed, no CLAUDE.md.

Load shop-sales.csv into Claude.ai or whichever platform you're using for the naive demo.

Run the prompt. Let it run. Don't guide it. The point is to see what raw prompting produces without any structure.

Students should be following along on their own platforms simultaneously.
-->

---
layout: center
class: demo
---

<div class="uw-label mb-4">Live Demo · Desktop 2</div>

# Milestone 1 — Naive Pass

<div class="uw-rule mt-4 mb-8"></div>

**Loading:** `data/coffee-shops/shop-sales.csv`

**Prompt:** "Analyze this data and tell me what's interesting."

<div class="mt-8 opacity-80 text-base font-medium">Switch to Desktop 2 for live demo</div>

<!--
LIVE DEMO SLIDE — no content to present.
Keep this slide visible on D1 while you work on D2.
-->

---
layout: two-cols
class: reveal
---

<div class="uw-label mb-4">Milestone 1 Reveal</div>

# What Did We Get?

<div class="uw-rule mt-3 mb-6"></div>

**What was useful:**

- Identified top-selling categories
- Spotted the revenue leaders
- Produced readable prose
- Generated in seconds

::right::

<div class="mt-12"></div>

**What was ungrounded:**

- Which "Suzzallo" is that? (3 name variants in the data)
- "Sales are trending up" — from which date range?
- No mention of the flat-sales anomaly at S3
- Date field mixed two formats — did it notice?
- Missing vendor quote gaps — not flagged

<div class="mt-8 p-4 rounded-lg border-l-4" style="border-color: #f59e0b; background: #fffbeb; color: #1a0a30;">
<strong>The output was confident. The foundation wasn't.</strong>
</div>

<!--
Walk through each "ungrounded" point by referencing what you saw in the actual output.

The goal: students should feel the tension between "this looks right" and "but I can't verify it." That tension is the pedagogical moment for this milestone.
-->

---
layout: default
class: section
---

<div class="uw-label mb-3">Milestone 2 of 4</div>

# The Infographic

<div class="uw-rule mt-3 mb-6"></div>

**What we do:** Same naive workspace, same data. One step further.

**The prompt:**
```
Create a standalone HTML infographic report from this data.
Include charts, key metrics, and professional styling.
```

**What we're testing:** Can the agent produce a deliverable artifact?

<div class="mt-8 p-3 rounded-lg" style="background: #f5f3ff; color: #1a0a30; border: 1px solid #c4b5fd;">
Open the generated HTML in your browser. Look at it as a stakeholder, not a developer.
</div>

<!--
Switch back to D2 naive workspace.
Run the HTML infographic prompt.
Open the output in VS Code integrated browser, or drag to Chrome.
Students on their own platforms: generate the same HTML.
-->

---
layout: center
class: demo
---

<div class="uw-label mb-4">Live Demo · Desktop 2</div>

# Milestone 2 — The Infographic

<div class="uw-rule mt-4 mb-8"></div>

**Prompt:** "Create a standalone HTML infographic report from this data."

<div class="mt-8 opacity-80 text-base font-medium">Switch to Desktop 2 for live demo</div>

<!--
LIVE DEMO SLIDE — no content to present.
Keep this slide visible on D1 while you work on D2.
-->

---
layout: two-cols
class: reveal
---

<div class="uw-label mb-4">Milestone 2 Reveal</div>

# Pretty — But Is It Trustworthy?

<div class="uw-rule mt-3 mb-6"></div>

**What improved:**

- Visual. Shareable. Professional-looking.
- Charts communicating structure
- Summary metrics front and center
- Someone will believe this

::right::

<div class="mt-12"></div>

**What's still missing:**

- No confidence scores on any claim
- No data quality disclosures
- No source citations (which rows? which date range?)
- The S3 flat-sales anomaly is buried or absent
- Audience: who is this for? Shop managers? The VP? Both?
- You can't tell the difference between a 95% reliable finding and a guess

<div class="mt-6 p-4 rounded-lg border-l-4" style="border-color: #ef4444; background: #fff1f2; color: #1a0a30;">
<strong>A polished report can look more confident than it is.</strong><br>That's a liability, not an asset.
</div>

<!--
Ask the room: "Would you send this to your dean?" 
Let a few students answer. 

The point is that the visual layer adds authority the analysis hasn't earned yet.
-->

---
layout: default
class: section
---

<div class="uw-label mb-3">Milestone 3 of 4</div>

# The Enrichment

<div class="uw-rule mt-3 mb-6"></div>

**Switch to Desktop 3 — harnessed workspace.**

What changes:

- **CLAUDE.md**: Agent identity, data context, quality standards
- **Skills installed**: EDA, confidence scoring, infographic builder, refinement interview
- **Semantic model**: shared definitions for "revenue," "engagement rate," "active shop"
**The agent will ask you questions before analyzing.** This is the interview.

Four targeted questions selected from a bank of ten, based on what it found in the data. Hard cap: five questions max.
<!--
Switch to Desktop 3. Show the workspace structure: .agents/skills/, CLAUDE.md.
Don't run anything yet. Walk through what's installed and why each piece matters.

Then trigger the data-refinement-interview skill and let it run. Students watching should see how the agent's behavior changes with structure.
-->

---
layout: none
class: demo
clicks: 4
---

<RecipeDemo
  mode="cinematic"
  eyebrow="Milestone 3 of 4 · Live Demo · Desktop 3"
  title="The Enrichment"
  meta="★ 5/5 · workspace-harnessed · ~6 min walkthrough"
  :ingredients="[
    { label: 'Workspace', value: 'workspace-harnessed/', note: 'CLAUDE.md visible in editor' },
    { label: 'Skills', value: '.agents/skills/', note: '6 skills auto-loaded' },
    { label: 'Data', value: 'data/coffee-shops/', note: 'same CSVs as M1' },
    { label: 'Commands', value: '/data-refinement-interview · /programmatic-eda' },
  ]"
  overview="The harness gives the agent a framework for what to ask before drawing conclusions. The data did not change. The disciplines did."
  :steps="[
    {
      kicker: 'Step 1',
      title: 'Open the workspace',
      heroCaption: 'CLAUDE.md and .agents/skills/ visible in the editor',
      detail: 'Show students the CLAUDE.md operating instructions and the skill files that ship with the workspace.',
      expected: 'Skills are listed in chat; agent acknowledges the operating instructions.',
    },
    {
      kicker: 'Step 2',
      title: 'Trigger the interview',
      heroCaption: 'Run /data-refinement-interview',
      detail: 'The agent will ask 3–5 grounded questions before touching the data.',
      expected: '≤ 5 questions, each tied to a specific column, file, or audience.',
    },
    {
      kicker: 'Step 3',
      title: 'Answer the interview',
      heroCaption: 'Resolve audience, scope, and outlier handling',
      detail: 'Tell it: audience is the VP; investigate S3 flat-sales; treat HUB Coffee variants as one shop.',
      expected: 'Scope, audience, and outlier rules logged at the top of the analysis.',
    },
    {
      kicker: 'Step 4',
      title: 'Run programmatic EDA',
      heroCaption: 'Run /programmatic-eda — watch it flag the same issues we missed in M1',
      detail: 'The agent flags the S3 flat-sales anomaly, date format inconsistency, and shop name variants — all on its own.',
      expected: 'Three data quality issues surfaced, each with file + row range citations.',
    },
  ]"
/>

<!--
LIVE DEMO SLIDE — recipe-card walkthrough on Desktop 1.
The presenter executes the same steps live on Desktop 3 while the audience tracks progress here.

Press → / Space to advance through 4 steps. The card on the right morphs from Ingredients/Overview into Step-by-step/What-changes. After step 4, → moves to the next slide.
-->

---
layout: two-cols
class: reveal
---

<div class="uw-label mb-4">Milestone 3 Reveal</div>

# Structured vs. Unstructured

<div class="uw-rule mt-3 mb-6"></div>

**What the harness added:**

- Agent flagged the S3 flat-sales anomaly
- Date format inconsistency surfaced and documented
- Shop name variants identified (3 for HUB Coffee)
- Missing vendor bids flagged per line item

::right::

<div class="mt-12"></div>

**The interview demonstrated:**

- What "revenue" means in this context
- Which outlier to investigate vs. exclude
- Who reads this analysis (changes framing)
- Whether to normalize sales by operating hours

<div class="mt-8 p-4 rounded-lg" style="background: var(--uw-purple-light); color: #1a0a30;">
<strong>Skills are not prompts. They are systematic thinking encoded as instructions.</strong><br><br>
The agent did not become smarter. It became more disciplined.
</div>

<!--
Key point: the skills didn't give the AI more information. They gave it a framework for what questions to ask before drawing conclusions.

This is the core lesson. Walk it slow.
-->

---
layout: default
class: section
---

<div class="uw-label mb-3">Milestone 4 of 4</div>

# The Confident Narrative

<div class="uw-rule mt-3 mb-6"></div>

**Still on Desktop 3. Now we add the job market data.**

The problem we will demonstrate first:

```
What is the average salary for data analysts in Seattle?
```
Without context scoping, the agent draws from both datasets simultaneously.

"Average salary" appears in job-postings.csv. "Average daily revenue" appears in shop-sales.csv.

The agent may blend the context. Watch what happens.
Then we fix it. Then we generate the final report.
<!--
This is the context bleed demo. Load both datasets into context without scoping, then ask the salary question. Show whatever the agent produces.

Then show how CLAUDE.md scoping and explicit dataset references prevent the bleed.
-->

---
layout: center
class: demo
---

<div class="uw-label mb-4">Live Demo · Desktop 3</div>

# Milestone 4 — The Confident Narrative

<div class="uw-rule mt-4 mb-8"></div>

**1.** Load both datasets — context bleed demo

**2.** Scope fix — CLAUDE.md dataset references

**3.** Generate final HTML report with confidence scores and spotlight tour

<div class="mt-8 opacity-80 text-base font-medium">Switch to Desktop 3 for live demo</div>

<!--
LIVE DEMO SLIDE — no content to present.
Keep this slide visible on D1 while you work on D3.
-->

---
layout: two-cols
class: reveal
---

<div class="uw-label mb-4">Milestone 4 Reveal</div>

# V1 vs. V4

<div class="uw-rule mt-3 mb-6"></div>

**The Milestone 2 report:**

- No data quality disclosures
- No confidence scores
- No source lineage
- No audience framing
- Flat presentation

::right::

<div class="mt-12"></div>

**The Milestone 4 report:**

- Every claim: confidence score (0-1)
- Data quality annotations inline
- Source lineage: file + row range
- Assumptions logged
- Three audience variants (manager / VP / vendor committee)
- Shepherd.js spotlight tour walks the narrative
- Defensible. Presentable. Auditable.

<div class="mt-6 p-4 rounded-lg border-l-4" style="border-color: var(--uw-gold-bright); background: var(--uw-gold-pale); color: #1a0a30;">
<strong>The data did not change. The harness did.</strong>
</div>

<!--
Show the two HTML files side by side in the browser.

Spend 30 seconds on the spotlight tour — click through it live.

Then move to the final recap slide.
-->

---
layout: default
class: section
---

<div class="uw-label mb-4">Recap</div>

# The 4-Layer Progression

<div class="uw-rule mt-3 mb-8"></div>

| Milestone | Method | What Changed |
|-----------|--------|-------------|
| 1. Naive Pass | Raw prompt | Baseline. Fast, ungrounded. |
| 2. Infographic | Raw prompt + HTML | Polished surface, same foundation. |
| 3. Enrichment | Skills + interview | Systematic reasoning, flagged issues. |
| 4. Confident Narrative | Full harness + scoping | Defensible claims, auditable analysis. |
<div class="mt-8 p-4 rounded-lg" style="background: var(--uw-purple-light); color: #1a0a30;">
<strong>The skill is not writing the prompt. The skill is building the harness.</strong><br><br>
Skills + semantic layers + quality gates + context scoping = analysis you can stake your name on.
</div>
<!--
This is the closing thesis. Let it land.

If there are 15 minutes left, open for Q&A.
If there are fewer than 10, move straight to the next slide.
-->

---
layout: default
class: hero
---

<div class="uw-label mb-6">What Next</div>

# Take This With You

<div class="uw-rule mt-3 mb-8"></div>
**Fork the repo:** `github.com/BrettReifs/data-storytelling-workshop`

Everything you saw today is in there: the data, the skills, both workspaces, the slide deck.

**Try with your own data.** The coffee shop files are a scaffold. The skills work on any tabular dataset.

**Install skills on your AI platform.** The `.agents/skills/` directory in the harnessed workspace is self-contained.

**Explore the ecosystem.** `github.com/nimrodfisher/data-analytics-skills` has 31 portable analytics skills. `github.com/anthropics/skills` has Anthropic's official library.
<div class="mt-8 flex gap-4">
  <a class="gold-cta" href="https://github.com/BrettReifs/data-storytelling-workshop">Fork the Repo</a>
  <a class="purple-cta" href="https://github.com/nimrodfisher/data-analytics-skills">Analytics Skills</a>
</div>
<!--
Stay available for the Q&A. Common questions:
- "Can I use this with ChatGPT?" Yes — skills are markdown files, platform-portable.
- "What if my company won't let me use Claude?" The skill files work with any instruction-following model.
- "How do I get started with my own data?" Fork the repo, drop your CSV in workspace-naive/data/, run Milestone 1.
-->

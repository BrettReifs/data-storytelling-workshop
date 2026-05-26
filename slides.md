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
    You will prototype a story with data in the next 45 minutes.
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
layout: default
class: reveal
---

<div class="agenda-page">
<div class="uw-label mb-4">The Plan</div>

# 4 Milestones

<div class="uw-rule mt-3 mb-5"></div>

<div class="agenda-shell">
<div class="agenda-grid">
  <div class="agenda-item">
    <div class="agenda-icon agenda-icon-1">
      <svg viewBox="0 0 120 120" aria-hidden="true" class="agenda-svg">
        <rect x="18" y="24" width="58" height="46" rx="8" class="stroke-icon fill-soft" />
        <path d="M18 40h58M18 54h58M37 24v46M56 24v46" class="stroke-icon" />
        <circle cx="79" cy="71" r="15" class="stroke-icon magnify-lens" />
        <path d="M89 82l12 12" class="stroke-icon magnify-lens" />
      </svg>
    </div>
    <div class="agenda-step"><span>1</span> Naive pass</div>
  </div>
  <div class="agenda-item">
    <div class="agenda-icon agenda-icon-2">
      <svg viewBox="0 0 120 120" aria-hidden="true" class="agenda-svg">
        <rect x="18" y="24" width="84" height="58" rx="10" class="stroke-icon fill-soft" />
        <path d="M18 39h84" class="stroke-icon" />
        <circle cx="29" cy="32" r="3" class="fill-icon" />
        <circle cx="39" cy="32" r="3" class="fill-icon" />
        <circle cx="49" cy="32" r="3" class="fill-icon" />
        <path d="M34 69l14-16 12 9 18-21 10 10" class="stroke-icon" />
        <path d="M33 74h54" class="stroke-muted" />
      </svg>
    </div>
    <div class="agenda-step"><span>2</span> Visual draft</div>
  </div>
  <div class="agenda-item">
    <div class="agenda-icon agenda-icon-3">
      <svg viewBox="0 0 120 120" aria-hidden="true" class="agenda-svg">
        <ellipse cx="45" cy="31" rx="22" ry="9" class="stroke-icon fill-soft" />
        <path d="M23 31v30c0 5 10 9 22 9s22-4 22-9V31" class="stroke-icon fill-soft" />
        <path d="M23 46c0 5 10 9 22 9s22-4 22-9M23 61c0 5 10 9 22 9s22-4 22-9" class="stroke-icon" />
        <circle cx="83" cy="61" r="19" class="stroke-icon" />
        <path d="M83 51v20M73 61h20" class="stroke-icon" />
      </svg>
    </div>
    <div class="agenda-step"><span>3</span> Data enrichment</div>
  </div>
  <div class="agenda-item">
    <div class="agenda-icon agenda-icon-4">
      <svg viewBox="0 0 120 120" aria-hidden="true" class="agenda-svg">
        <rect x="24" y="20" width="54" height="72" rx="8" class="stroke-icon fill-soft" />
        <path d="M36 39h30M36 52h30M36 65h22" class="stroke-icon" />
        <circle cx="86" cy="74" r="16" class="fill-icon" />
        <path d="M79 74l5 5 10-11" class="stroke-check" />
      </svg>
    </div>
    <div class="agenda-step"><span>4</span> Confident narrative</div>
  </div>
</div>
</div>
</div>

<style scoped>
.agenda-page {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.agenda-shell {
  display: flex;
  align-items: center;
}

.agenda-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.85rem;
  align-items: start;
  width: 100%;
}

.agenda-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.7rem;
  min-width: 0;
}

.agenda-icon {
  position: relative;
  width: 100%;
  height: 8.2rem;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.agenda-svg {
  width: 74%;
  height: 74%;
}

.agenda-icon-1 {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 55%, #93c5fd 100%);
}

.agenda-icon-2 {
  background: linear-gradient(140deg, #fef3c7 0%, #fde68a 55%, #fcd34d 100%);
}

.agenda-icon-3 {
  background: linear-gradient(140deg, #ede9fe 0%, #ddd6fe 55%, #c4b5fd 100%);
}

.agenda-icon-4 {
  background: linear-gradient(140deg, #dcfce7 0%, #bbf7d0 52%, #86efac 100%);
}

.stroke-icon {
  fill: none;
  stroke: rgba(26, 10, 48, 0.78);
  stroke-width: 4.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.stroke-muted {
  fill: none;
  stroke: rgba(26, 10, 48, 0.38);
  stroke-width: 4;
  stroke-linecap: round;
}

.fill-soft {
  fill: rgba(255, 255, 255, 0.46);
}

.fill-icon {
  fill: rgba(26, 10, 48, 0.68);
}

.magnify-lens {
  stroke: rgba(26, 10, 48, 0.82);
}

.stroke-check {
  fill: none;
  stroke: #ffffff;
  stroke-width: 5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.agenda-step {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  padding: 0 0.3rem;
  font-weight: 700;
  font-size: 1.1rem;
  text-align: center;
  line-height: 1.2;
  color: #1a0a30;
}

.agenda-step span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.45rem;
  height: 1.45rem;
  border-radius: 9999px;
  background: #4b2e83;
  color: #ffffff;
  font-size: 0.82rem;
  line-height: 1;
}
</style>

<!--
Frame this as the journey map for the next 45 minutes, one stop per milestone.
-->

---
layout: none
class: demo
clicks: 3
---

<RecipeDemo
  mode="cinematic"
  eyebrow="Milestone 1 of 4 · Live Demo · Desktop 2"
  title="The Naive Pass"
  meta="★ 3/5 · workspace-naive · ~8 min walkthrough"
  :ingredients="[
    { label: 'Workspace', value: 'workspace-naive/', note: 'no skills, no CLAUDE.md' },
    { label: 'Data', value: 'shop-sales.csv', note: '~46k rows, 6 months' },
    { label: 'Platform', value: 'Claude.ai / ChatGPT / Copilot', note: 'any platform, file upload' },
    { label: 'Commands', value: 'upload + one open-ended prompt' },
  ]"
  overview="Unstructured AI analysis is fast and readable — and missing the foundation you need to defend any finding."
  :steps="[
    {
      kicker: 'Step 1',
      title: 'Load the data',
      heroCaption: 'Upload shop-sales.csv — no framing, no context',
      detail: 'Upload shop-sales.csv to your platform. No framing, no context, no instructions.',
      expected: 'File accepted; platform ready to receive a prompt.',
    },
    {
      kicker: 'Step 2',
      title: 'Run the naive prompt',
      heroCaption: 'Analyze this data and tell me what is interesting.',
      detail: 'Prompt the AI bare: Analyze this data and tell me what is interesting. No guidance.',
      expected: 'Confident output: revenue trends, top shops, volume stats. No caveats.',
    },
    {
      kicker: 'Step 3',
      title: 'Audit one finding',
      heroCaption: 'Push on a claim — ask it to cite the rows',
      detail: 'Push on any claim. Ask: which rows in the data support this finding?',
      expected: 'Agent cites a range OR restates without proof. The gap is visible.',
    },
  ]"
/>

<!--
Switch to Desktop 2 (workspace-naive). No CLAUDE.md, no skills directory.
Load shop-sales.csv into whichever AI platform you're demoing.
Run the prompt live. Don't guide it. Students follow along on their own platforms simultaneously.
The goal is not to show failure — raw AI analysis is genuinely useful. The lesson is about
what it cannot tell you: where the numbers came from, what was assumed, and what was skipped.
-->

---
layout: none
class: demo
clicks: 3
---

<RecipeDemo
  mode="cinematic"
  eyebrow="Milestone 2 of 4 · Live Demo · Desktop 2"
  title="The Infographic"
  meta="★ 3/5 · workspace-naive · ~8 min walkthrough"
  :ingredients="[
    { label: 'Workspace', value: 'workspace-naive/', note: 'same session as M1' },
    { label: 'Data', value: 'shop-sales.csv loaded', note: 'no re-upload needed' },
    { label: 'Output', value: 'standalone HTML report', note: 'open in browser to review' },
    { label: 'Commands', value: 'one infographic prompt' },
  ]"
  overview="Professional presentation can make an analysis look more authoritative than the evidence behind it."
  :steps="[
    {
      kicker: 'Step 1',
      title: 'Generate the report',
      heroCaption: 'One prompt: HTML infographic with 3+ charts',
      detail: 'Ask for a standalone HTML infographic with 3+ charts and professional styling.',
      expected: 'Self-contained HTML with charts, metric cards, and formatted layout.',
    },
    {
      kicker: 'Step 2',
      title: 'View as a stakeholder',
      heroCaption: 'Open in browser — not as the developer who built it',
      detail: 'Open in browser. View it as your VP would — not as the developer who built it.',
      expected: 'Polished report, looks presentation-ready. No data quality disclosures visible.',
    },
    {
      kicker: 'Step 3',
      title: 'Challenge one number',
      heroCaption: 'Ask: which rows support this metric exactly?',
      detail: 'Pick any displayed metric. Ask: which rows in the file support this number?',
      expected: 'Agent hedges or cannot cite rows. Surface quality exceeded the foundation.'
    },
  ]"
/>

<!--
Still on Desktop 2 (workspace-naive). The same data is already loaded from M1.
Run the infographic prompt. Let it generate. Open the HTML output in VS Code Live Server
or drag to Chrome.
Students on their own platforms: generate the same HTML and open it locally.
The tension: the report looks credible. It isn't defensible. That gap is the lesson.
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
layout: none
class: demo
clicks: 4
---

<RecipeDemo
  mode="cinematic"
  eyebrow="Milestone 4 of 4 · Live Demo · Desktop 3"
  title="The Confident Narrative"
  meta="★ 5/5 · workspace-harnessed · ~10 min walkthrough"
  :ingredients="[
    { label: 'Workspace', value: 'workspace-harnessed/', note: 'CLAUDE.md active, all skills' },
    { label: 'Data', value: 'data/coffee-shops/', note: 'all 5 files, same as M1' },
    { label: 'Output', value: 'final-report.html', note: 'confidence scores + spotlight tour' },
    { label: 'Commands', value: '/confidence-scorer · /infographic-builder', note: '+ /spotlight-walkthrough' },
  ]"
  overview="Same data, same question — confidence scores, source lineage, and findings you can stake your name on."
  :steps="[
    {
      kicker: 'Step 1',
      title: 'Generate the final report',
      heroCaption: 'Invoke all three output skills in one prompt',
      detail: 'Invoke all three output skills in one prompt. Let them run without interruption.',
      expected: 'HTML with confidence score (0–1) on every claim, assumptions logged, row citations.',
    },
    {
      kicker: 'Step 2',
      title: 'Run the spotlight tour',
      heroCaption: 'Launch the Shepherd.js guided walkthrough',
      detail: 'Open the report in browser. Launch the Shepherd.js guided walkthrough from the menu.',
      expected: 'Tour walks 4–6 narrative beats in the order a stakeholder should read them.',
    },
    {
      kicker: 'Step 3',
      title: 'Compare to M2',
      heroCaption: 'The data did not change. The harness did.',
      detail: 'The data did not change between M2 and M4. Name the specific differences aloud.',
      expected: 'Confidence scores, source lineage, audience variants — all absent from M2.',
    },
    {
      kicker: 'Step 4',
      title: 'Watch for context bleed',
      heroCaption: 'Risk: multiple datasets, no scoping = silent blending',
      detail: 'Loading multiple datasets without scoping lets the agent blend context silently.',
      expected: 'Use CLAUDE.md dataset scoping. Explicit references prevent cross-dataset confusion.',
    },
  ]"
/>

<!--
Still on Desktop 3 (workspace-harnessed). All skills active from M3.
Run the full narrative prompt invoking data-confidence-scorer, html-infographic-builder,
and spotlight-walkthrough together. Open the output HTML in browser and run the tour.
For Step 3: open both M2 and M4 HTML files side by side in the browser — 30 seconds.
For Step 4 (context bleed): this is a callout, not a live demo. Point to the CLAUDE.md
scoping rules on screen and explain the risk clearly. Students should internalize this
as a design pattern for their own projects.
-->

---
layout: default
class: section
---

<div class="uw-label mb-1">Recap</div>

# The 4-Layer Progression

<div class="uw-rule mt-1 mb-3"></div>

| Milestone | Method | What Changed |
|-----------|--------|-------------|
| 1. Naive Pass | Raw prompt | Baseline. Fast, ungrounded. |
| 2. Infographic | Raw prompt + HTML | Polished surface, same foundation. |
| 3. Enrichment | Skills + interview | Systematic reasoning, flagged issues. |
| 4. Confident Narrative | Full harness + scoping | Defensible claims, auditable analysis. |
<div class="mt-2 p-3 rounded-lg" style="background: var(--uw-purple-light); color: #1a0a30;">
<strong>Data skills are not defined by writing the query or prompt. <br><br>The skills that will distinguish you are crafting context and harnessing the narrative.</strong><br><br>
Skills + semantic layers + quality gates + context scoping = analysis you can stake your name on.
</div>

<style scoped>
h1 { font-size: 2em !important; line-height: 1.1 !important; margin: 0 0 0.15em !important; }
table { font-size: 0.88em; margin: 0; }
table thead th, table tbody td { padding: 0.28em 0.6em; }
</style>
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

**Explore the ecosystem.** `github.com/anthropics/skills` has Anthropic's official library.
<div class="mt-8 flex gap-4">
  <a class="gold-cta" href="https://github.com/BrettReifs/data-storytelling-workshop">Fork the Repo</a>
</div>
<!--
Stay available for the Q&A. Common questions:
- "Can I use this with ChatGPT?" Yes — skills are markdown files, platform-portable.
- "What if my company won't let me use Claude?" The skill files work with any instruction-following model.
- "How do I get started with my own data?" Fork the repo, drop your CSV in workspace-naive/data/, run Milestone 1.
-->

# Live-Demo Recipe Slide — copy-pasteable templates

Drop into `slides.md` and replace placeholder content. Both templates assume `<RecipeDemo>` is auto-registered (Slidev auto-imports `components/*.vue`).

---

## Cinematic template (each step = new visual)

Use for demos where the presenter jumps between screens, files, or terminals.

````md
---
layout: none
class: demo
clicks: 4
---

<RecipeDemo
  mode="cinematic"
  eyebrow="Milestone X of 4 · Live Demo · Desktop Y"
  title="<Recipe name>"
  meta="★ 5/5 · <workspace or artifact> · ~N min walkthrough"
  :ingredients="[
    { label: 'Workspace', value: '<dir>/',         note: '<one-line orientation>' },
    { label: 'Skills',    value: '<paths>',        note: '<count + intent>' },
    { label: 'Data',      value: '<dir>/' },
    { label: 'Commands',  value: '<slash-commands or terminal calls>' },
  ]"
  overview="<One sentence: what the demo accomplishes overall.>"
  :steps="[
    {
      kicker: 'Step 1',
      title: '<Step name>',
      heroCaption: '<caption shown on the hero image>',
      detail: '<one sentence for Card B during this step>',
      expected: '<observable output the audience should see>',
      // heroSrc: '/m<N>/step1.png',
    },
    {
      kicker: 'Step 2',
      title: '<Step name>',
      heroCaption: '<caption>',
      detail: '<sentence>',
      expected: '<observable output>',
      // heroSrc: '/m<N>/step2.png',
    },
    {
      kicker: 'Step 3',
      title: '<Step name>',
      heroCaption: '<caption>',
      detail: '<sentence>',
      expected: '<observable output>',
      // heroSrc: '/m<N>/step3.png',
    },
    {
      kicker: 'Step 4',
      title: '<Step name>',
      heroCaption: '<caption>',
      detail: '<sentence>',
      expected: '<observable output>',
      // heroSrc: '/m<N>/step4.png',
    },
  ]"
/>

<!--
Presenter notes — the spoken script.
The audience tracks progress on Desktop 1; the live demo runs on Desktop Y.
Press → / Space to advance through the N steps.
-->
````

---

## Annotated template (one image, several callouts)

Use when the demo's value is **showing what to notice on a single screen** (e.g., the final HTML report with confidence scores, lineage, assumptions, audience variants).

````md
---
layout: none
class: demo
clicks: 4
---

<RecipeDemo
  mode="annotated"
  eyebrow="Milestone X of 4 · Live Demo · Desktop Y"
  title="<Recipe name>"
  meta="★ 5/5 · <artifact> · ~N min"
  heroSrc="/m<N>/composite.png"
  :ingredients="[
    { label: 'Artifact', value: '<path/to/file>' },
    { label: 'Skills',   value: '<paths>' },
  ]"
  overview="<One sentence framing the single screen and what to look for.>"
  :steps="[
    {
      kicker: 'Callout 1',
      title: '<What this pin highlights>',
      detail: '<one sentence>',
      expected: '<what the audience should observe>',
      pin: { top: '24%', left: '22%' },
    },
    {
      kicker: 'Callout 2',
      title: '<...>',
      detail: '<...>',
      expected: '<...>',
      pin: { top: '58%', left: '60%' },
    },
    {
      kicker: 'Callout 3',
      title: '<...>',
      detail: '<...>',
      expected: '<...>',
      pin: { top: '72%', left: '34%' },
    },
    {
      kicker: 'Callout 4',
      title: '<...>',
      detail: '<...>',
      expected: '<...>',
      pin: { top: '36%', left: '76%' },
    },
  ]"
/>

<!--
Presenter notes — the spoken script.
The pin coordinates above are placeholders. Once /public/m<N>/composite.png lands,
nudge each top/left % so each pin sits over the correct region of the screenshot.
-->
````

---

## Field-by-field guidance

| Field | Voice | Length |
|---|---|---|
| `title` | The recipe name. Concrete, evocative. No filler. | ≤ 4 words |
| `meta` | Rating + source + duration. Mimics the lasagne reference. | one line |
| `ingredients[i].label` | UPPERCASE-style key (rendered as mono). | 1 word |
| `ingredients[i].value` | The actual path / command / count. | ≤ 40 chars |
| `ingredients[i].note` | Muted secondary line. Optional. | ≤ 50 chars |
| `overview` | One sentence. What the demo accomplishes in total. | 1 sentence |
| `steps[i].title` | Imperative verb-led. "Open the workspace", "Trigger the interview". | ≤ 5 words |
| `steps[i].detail` | One sentence shown in Card B during this step. | 1 sentence |
| `steps[i].expected` | Observable result, not aspiration. Renders in the "Done looks like" ribbon. | ≤ 90 chars |
| `steps[i].kicker` | Small uppercase eyebrow on the hero caption. | `Step N` or `Callout N` |
| `steps[i].heroCaption` | The caption shown over the hero image during this step. | ≤ 80 chars |

## Sanity check before commit

- `clicks: N` in frontmatter equals `steps.length`.
- Every step has a non-empty `expected`.
- For annotated mode, every step has a `pin: { top, left }` or you accept the default 4-pin grid (pins 1–4 only).
- Run `npm run build`. Zero errors expected.
- In `npm run dev`, click through every step. No card or hero image should extend below the visible slide boundary after any click. This is a hard verification gate — do not commit until all steps pass on-canvas.

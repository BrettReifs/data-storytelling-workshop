# Components

Reusable Slidev components for the workshop deck. All `*.vue` files in this directory are auto-registered as global components by Slidev and can be used in any slide.

## `RecipeDemo.vue`

A reusable "recipe card" layout for live-demo walkthrough slides. Inspired by the [Edmondscooking.co lasagne template](../prototypes/_index.html) and built from the Round 3 prototypes (`prototypes/m3-v2b-*`, `prototypes/m3-v2c-*`).

Renders a 16:9 slide with:

- **Title row**: eyebrow + bold black title + meta (rating/source/duration).
- **Hero image (left half)**: either crossfading per step, or static with overlay pins.
- **Two stacked cream cards (right half)** that morph as the presenter advances:
  - Card A: **Ingredients** → **Step-by-step** (active step glows gold, done steps check off).
  - Card B: **Overview** → **What changes** (per-step expected output in a monospace ribbon).
- **Footer**: progress rail with one pip per step.

### Two modes

Pick the mode based on whether the demo steps share a single visual surface.

| Mode | When to use | Production cost |
|---|---|---|
| `cinematic` | Each step **jumps to a new topic** that demands its own visual (workspace → terminal → output, etc.). | One hero image per step. |
| `annotated` | All steps **highlight different regions of a single image** (one composite screenshot with sub-step callouts). | One hero image total + pin coordinates. |

### Slidev integration

The component reads the current click count from `useSlideContext().$slidev.nav.clicks`. Click `0` is the briefing state (Ingredients + Overview). Clicks `1..N` reveal each step.

**Set `clicks: N` in the slide frontmatter** where `N` equals `steps.length`. The Slidev navigation will then advance through all states with `→` / `Space` before moving to the next slide.

```yaml
---
layout: none
class: demo
clicks: 4
---
```

### Prop API

| Prop | Type | Required | Notes |
|---|---|---|---|
| `mode` | `"cinematic" \| "annotated"` | yes | See table above. |
| `eyebrow` | string | no | Small uppercase tag above the title (e.g. `Milestone 3 of 4 · Live Demo · Desktop 3`). |
| `title` | string | yes | Large bold title (the "recipe name"). |
| `meta` | string | no | The star/source/duration line (e.g. `★ 5/5 · workspace-harnessed · ~6 min`). |
| `ingredients` | `Array<{ label, value, note? }>` | no | Shown on Card A during briefing. `label` is uppercase mono key, `value` is mono content, `note` is muted secondary line. |
| `overview` | string | no | Shown on Card B during briefing. One sentence: what the demo accomplishes. |
| `steps` | `Array<Step>` | yes | One entry per click. See Step shape below. |
| `heroSrc` | string | no | **Annotated mode only.** Path under `public/` for the single hero image. Falls back to a gradient placeholder. |

#### `Step` shape

```ts
{
  kicker: string,        // small uppercase, e.g. "Step 2"
  title: string,         // step name, shown bold in card A and in caption
  detail?: string,       // sentence shown in card B during this step
  expected: string,      // "Done looks like" ribbon — what the audience should see
  heroSrc?: string,      // CINEMATIC ONLY: per-step hero image path under public/
  heroCaption?: string,  // optional override for the caption shown on the hero
  pin?: { top: string, left: string }, // ANNOTATED ONLY: percentage strings for pin position
}
```

If `heroSrc` is omitted, the component renders a distinct gradient placeholder per step so the slide works before any photos are produced.

### Example — cinematic (M3 Enrichment)

See `slides.md` at the `Milestone 3 — Live Demo` slide for the canonical example. Each step jumps to a different workspace area (CLAUDE.md → terminal → answer-flow → EDA output), so cinematic is the right fit.

### Example — annotated (one image, four callouts)

```html
---
layout: none
class: demo
clicks: 4
---

<RecipeDemo
  mode="annotated"
  eyebrow="Milestone 4 of 4 · Live Demo · Desktop 3"
  title="The Confident Narrative"
  meta="★ 5/5 · final HTML report · ~4 min"
  heroSrc="/m4/final-report.png"
  :ingredients="[
    { label: 'Report', value: 'workspace-harnessed/output/m4.html' },
    { label: 'Skills', value: 'data-confidence-scorer · spotlight-walkthrough' },
  ]"
  overview="One image, four signals: confidence scores, lineage, assumptions, audience variants."
  :steps="[
    {
      kicker: 'Callout 1',
      title: 'Confidence scores',
      detail: 'Every claim shows a 0–1 score plus method.',
      expected: 'Each headline number has a tooltip with score and source.',
      pin: { top: '24%', left: '22%' },
    },
    {
      kicker: 'Callout 2',
      title: 'Source lineage',
      detail: 'Hover any chart for file + row range.',
      expected: 'Tooltip shows shop-sales.csv:103-218.',
      pin: { top: '58%', left: '60%' },
    },
    {
      kicker: 'Callout 3',
      title: 'Assumptions log',
      detail: 'A panel lists every interview answer that shaped the analysis.',
      expected: '4 assumptions listed, each linked to where it was applied.',
      pin: { top: '72%', left: '34%' },
    },
    {
      kicker: 'Callout 4',
      title: 'Audience variants',
      detail: 'One report, three lenses: manager, VP, vendor committee.',
      expected: 'Tab selector switches the framing without changing the numbers.',
      pin: { top: '36%', left: '76%' },
    },
  ]"
/>
```

### Adapting to M1, M2, M4

The component is intentionally generic. To apply it to the other live-demo slides:

1. Pick the mode (cinematic for topic-jumping steps, annotated for sub-callouts on one image).
2. Set `clicks: N` in the slide frontmatter where `N` is the number of steps.
3. Drop in `<RecipeDemo ... :steps="..." />` with your content.
4. (Optional) Add hero images under `public/m1/`, `public/m3/`, etc. and reference them via `heroSrc`. Without them, gradient placeholders ship.

### Visual tokens

The component uses the deck's existing UW palette CSS variables (`--uw-purple`, `--uw-purple-deep`, `--uw-gold-bright`, `--uw-purple-light`) and adds three warm tones for the cream cards: `#F2EFE9` (card A), `#EDE9DF` (card B), `#6B6356` (muted text).

### Related

- `prototypes/m3-v2b-recipe-cinematic.html` — standalone cinematic prototype.
- `prototypes/m3-v2c-recipe-annotated.html` — standalone annotated prototype.
- `prototypes/_index.html` — review page for all variants.

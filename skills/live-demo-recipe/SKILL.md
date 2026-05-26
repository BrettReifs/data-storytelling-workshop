---
name: live-demo-recipe
description: Author or convert workshop live-demo slides to the RecipeDemo component (recipe-card hero + morphing ingredients/step cards). Use when user says "add a live demo slide", "convert M1/M2/M4 to the recipe card", "make this slide a walkthrough", "use RecipeDemo for", or wants to apply the M3 pattern elsewhere.
tools: [read, search, edit, create, bash]
---

# Live-Demo Recipe Slide

Apply the `RecipeDemo` component (`components/RecipeDemo.vue`) to any live-demo slide in `slides.md`. The canonical example is the **Milestone 3 — The Enrichment** slide; mirror that structure when authoring M1/M2/M4 demo slides or adding new ones.

## Mode selection (the one decision that matters)

| Demo shape | Mode | Why |
|---|---|---|
| Each step jumps to a different screen / file / topic | `cinematic` | One hero image per step, crossfading. |
| All steps point at different regions of a **single composite image** | `annotated` | One hero + numbered pins that light up per step. |

If unsure, default to `cinematic`. The presenter can always switch later — only the `mode` prop and per-step image fields change.

## Required slide frontmatter

```yaml
---
layout: none
class: demo
clicks: <N>          # MUST equal steps.length
---
```

`clicks: N` is non-optional. Without it, Slidev advances to the next slide before the funnel finishes.

## Prop checklist when authoring

- `mode` — `"cinematic"` or `"annotated"`
- `eyebrow` — `"Milestone X of 4 · Live Demo · Desktop Y"`
- `title` — short bold name of the demo (the "recipe name")
- `meta` — `"★ 5/5 · <workspace or artifact> · ~N min walkthrough"`
- `ingredients` — 3–5 `{ label, value, note? }` rows. Cover Workspace, Skills, Data, Commands.
- `overview` — one sentence: what the demo accomplishes overall.
- `steps` — array; one entry per click. Each step needs `kicker`, `title`, `detail`, `expected`. Add `heroSrc` for cinematic or `pin: { top, left }` for annotated.
- `heroSrc` (top-level) — annotated mode only: path under `public/` for the single composite image.

The `expected` field renders inside a "Done looks like · …" ribbon — phrase it as observable output, not aspiration.

## Image conventions

- Drop assets under `public/m<milestone>/` (e.g. `public/m3/step2.png`, `public/m4/final-report.png`).
- Reference via root path: `heroSrc: "/m3/step2.png"`.
- If images don't exist yet, omit `heroSrc` — the component renders distinct gradient placeholders so the slide ships immediately.
- For annotated mode, pin positions are percentage strings relative to the hero box (`{ top: "28%", left: "22%" }`). Nudge after the real photo lands.

## Authoring workflow

1. Locate the target slide in `slides.md` (search for `Live Demo · Desktop`).
2. Replace its body with the `<RecipeDemo ... />` invocation. Update frontmatter to `layout: none`, `class: demo`, `clicks: N`.
3. Keep the Slidev presenter notes (`<!-- ... -->`) — they remain the spoken script.
4. Run `npm run build`. Build failure = component prop error or missing `clicks`.
5. (Optional) `npm run dev` to walk the slide with `→` / `Space` and verify the funnel feels right.

## Differentiation from the `slidev` skill

The `slidev` skill covers general Slidev mechanics (layouts, magic-move, transitions). This skill is opinionated about ONE pattern — the recipe-card walkthrough — used for live-demo slides in this workshop. Use the general `slidev` skill for everything else.

## References

- `components/RecipeDemo.vue` — component source and inline docs.
- `components/README.md` — full prop API, both example invocations, adaptation notes.
- `slides.md` (Milestone 3 — The Enrichment slide) — canonical cinematic example.
- `prototypes/m3-v2b-recipe-cinematic.html`, `prototypes/m3-v2c-recipe-annotated.html` — standalone visual references.
- `EXAMPLES.md` (sibling file) — copy-pasteable templates for cinematic and annotated invocations.

## After editing

Run `npm run build` to verify. After this file lands, run `/sync-skills-index` once to register it in `AGENTS.md`.

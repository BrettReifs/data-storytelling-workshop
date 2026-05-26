# Slide Design Prototypes — Milestone 3 Pilot

Three alternative designs for the **Milestone 3 "Enrichment" live-demo slide** in `../slides.md`, each translating a different culinary-instruction pattern from the research in `../components/` onto a 16:9 Slidev canvas.

## Why this exists

The current M3 demo slide (the "Live Demo · Desktop 3" block in `slides.md`) shows a workspace path, a slash command, and a "Switch to Desktop 3" line. That's it. During the walkthrough, the slide does almost no instructional work — the presenter carries the entire load, and remote/follow-along students have nothing to scan.

The two long-form documents in `../components/` describe how culinary instruction designers solved the equivalent problem (dense, time-sensitive, multi-variable procedure on a single page). These prototypes adapt three of those patterns to the workshop demo slide.

## How to review

Open `_index.html` in any modern browser. It iframes all three variants side-by-side at locked 16:9 aspect ratio.

```powershell
start prototypes\_index.html
```

Or open each variant directly:

- `m3-v1-mise-en-place.html`
- `m3-v2-parametric-matrix.html`
- `m3-v3-picture-cook.html`

## The three variants

| File | Pattern | Density | Best for |
|---|---|---|---|
| `m3-v1-mise-en-place.html` | Mise en place + numbered steps with semantic bolding | Medium-high text, ordered | Mirrors presenter flow: "here's what's installed, here's what we run, here's what you'll see" |
| `m3-v2-parametric-matrix.html` | TRN / Modernist parametric matrix (inputs × phases, hover-dim) | High info-density, scannable | Lets remote student grasp whole harness at a glance, then track presenter position via focus dimming |
| `m3-v3-picture-cook.html` | Picture-Cook iconographic flow, near-zero text | Low text, high visual | Big-picture moment; lowest cognitive load; weakest for follow-along typing |

## Image placeholder convention

Where a variant calls for a real image (hero shot, full diagram, screenshot) that's beyond inline SVG, the prototype renders a **labeled dashed-border placeholder** at the exact target dimensions. Inside each placeholder:

- The intended `src` path (e.g., `assets/m3-workspace-tree.png`)
- A `<details>` block titled **"Image generation prompt"** with a ready-to-paste prompt tuned to the variant's aesthetic and the UW palette
- A suggested **alt-text** for accessibility

To drop in a real image later, create `prototypes/assets/`, save the generated file there, then replace the placeholder block with an `<img src="assets/...">`.

## Evaluation rubric

When picking a winner (or a mash-up), score each variant on:

1. **Scannability** — can a student catch up after 3 seconds of looking?
2. **Instruction density** — how much of the walkthrough is on the slide vs. in the presenter's head?
3. **Follow-along ability** — can a student typing in their own AI platform keep pace?
4. **Presenter clarity** — does the slide give the presenter clear "now point here" anchors?
5. **Accessibility** — readable at the back of a classroom, screen-reader-friendly?
6. **Reusability** — does the pattern generalize cleanly to M1, M2, M4 demo slides?

## After the pilot

Pick one variant (or describe a hybrid). I'll promote the winning pattern into `slides.md`, replace the M3 demo slide, then apply the same pattern to M1, M2, and M4 demo slides.

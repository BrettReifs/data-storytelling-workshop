<!--
  RecipeDemo — reusable Slidev component for live-demo walkthrough slides.

  Renders the "recipe card" layout: title row + hero image (left) + two stacked
  cream cards (right). The cards morph from Ingredients/Overview into Step-by-step/
  Done-looks-like as the presenter advances clicks.

  Two modes:
    - mode="cinematic" : a different hero image per step, crossfading.
      Use when each step jumps to a new topic that demands its own visual.
    - mode="annotated" : a single hero image with numbered pins that light up
      per step. Use when one image has multiple sub-regions to call out.

  Slidev integration: total clicks = steps.length. Click 0 shows the setup
  state (Ingredients + Overview). Clicks 1..N reveal each step.

  Set `clicks: <steps.length>` in the slide frontmatter so → and Space advance
  through all states before moving to the next slide.

  Example (cinematic):
    <RecipeDemo
      mode="cinematic"
      eyebrow="Milestone 3 of 4 · Live Demo · Desktop 3"
      title="The Enrichment"
      meta="★ 5/5 · workspace-harnessed · ~6 min"
      :ingredients="[
        { label: 'Workspace', value: 'workspace-harnessed/' },
        { label: 'Skills', value: '.agents/skills/' },
      ]"
      overview="The harness gives the agent a framework for what to ask before drawing conclusions."
      :steps="[
        {
          kicker: 'Step 1',
          title: 'Open the workspace',
          heroSrc: '/m3/step1.png',
          heroCaption: 'CLAUDE.md visible in the editor',
          expected: 'Skills are auto-loaded and listed in the chat',
        },
        ...
      ]"
    />

  Example (annotated): same as above but mode="annotated", omit per-step
  heroSrc, set top-level heroSrc, and add `pin: { top: '28%', left: '22%' }`
  to each step.
-->
<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  mode: { type: String, default: 'cinematic' }, // 'cinematic' | 'annotated'
  eyebrow: { type: String, default: '' },
  title: { type: String, required: true },
  meta: { type: String, default: '' },
  ingredients: { type: Array, default: () => [] },
  overview: { type: String, default: '' },
  steps: { type: Array, default: () => [] },
  // annotated mode: single hero image used for all steps
  heroSrc: { type: String, default: '' },
})

const { $slidev } = useSlideContext()

const stepIndex = computed(() => {
  const c = $slidev?.nav?.clicks?.value ?? $slidev?.nav?.clicks ?? 0
  return Math.min(Math.max(c, 0), props.steps.length)
})
const isSetup = computed(() => stepIndex.value === 0)
const activeStep = computed(() => (isSetup.value ? null : props.steps[stepIndex.value - 1]))

const cardATitle = computed(() => (isSetup.value ? 'Ingredients' : 'Step-by-step'))
const cardABadge = computed(() => (isSetup.value ? `${props.ingredients.length} items` : `${stepIndex.value} of ${props.steps.length}`))
const cardBTitle = computed(() => (isSetup.value ? 'Overview' : 'What changes'))
const cardBBadge = computed(() => (isSetup.value ? 'briefing' : `step ${stepIndex.value}`))

function stepClass(i) {
  if (stepIndex.value === 0) return ''
  if (i === stepIndex.value - 1) return 'active'
  if (i < stepIndex.value - 1) return 'done'
  return ''
}
function pinClass(i) {
  if (isSetup.value) return 'dim'
  if (i === stepIndex.value - 1) return 'active'
  if (i < stepIndex.value - 1) return 'done'
  return ''
}
function frameClass(i) {
  // frame 0 is the setup hero, frames 1..N are per-step
  return i === stepIndex.value ? 'active' : ''
}
function pipClass(i) {
  if (isSetup.value) return ''
  if (i === stepIndex.value - 1) return 'active'
  if (i < stepIndex.value - 1) return 'done'
  return ''
}
</script>

<template>
  <div class="rd-slide" :data-mode="mode">

    <!-- HEAD -->
    <header class="rd-head">
      <div v-if="eyebrow" class="rd-eyebrow">{{ eyebrow }}</div>
      <h2 class="rd-title">{{ title }}</h2>
      <div v-if="meta" class="rd-meta">{{ meta }}</div>
    </header>

    <!-- BODY -->
    <div class="rd-body">

      <!-- LEFT: HERO -->
      <div class="rd-hero">

        <!-- Cinematic: crossfading frames, one per state (0 = setup) -->
        <template v-if="mode === 'cinematic'">
          <div
            class="rd-frame"
            :class="frameClass(0)"
            data-frame="0"
          >
            <div class="rd-bg"></div>
            <div v-if="!heroSrc" class="rd-placeholder">
              <div class="rd-ph-icon">▢</div>
              <div class="rd-ph-label">Overview frame</div>
              <div class="rd-ph-desc">Drop /public/{{ mode }}/setup.jpg</div>
            </div>
            <img v-else class="rd-img" :src="heroSrc" alt="" />
            <div class="rd-caption">
              <div class="rd-kicker">Briefing</div>
              <div class="rd-cap-title">{{ overview || title }}</div>
            </div>
          </div>

          <div
            v-for="(s, i) in steps"
            :key="`f-${i}`"
            class="rd-frame"
            :class="frameClass(i + 1)"
            :data-frame="i + 1"
          >
            <div class="rd-bg"></div>
            <div v-if="!s.heroSrc" class="rd-placeholder">
              <div class="rd-ph-icon">{{ String(i + 1).padStart(2, '0') }}</div>
              <div class="rd-ph-label">{{ s.kicker || `Step ${i + 1}` }}</div>
              <div class="rd-ph-desc">{{ s.heroCaption || s.title }}</div>
            </div>
            <img v-else class="rd-img" :src="s.heroSrc" :alt="s.heroCaption || s.title" />
            <div class="rd-caption">
              <div class="rd-kicker">{{ s.kicker || `Step ${i + 1}` }}</div>
              <div class="rd-cap-title">{{ s.heroCaption || s.title }}</div>
            </div>
          </div>
        </template>

        <!-- Annotated: single hero image with positioned pins -->
        <template v-else-if="mode === 'annotated'">
          <div class="rd-frame active" data-frame="static">
            <div class="rd-bg"></div>
            <div v-if="!heroSrc" class="rd-placeholder">
              <div class="rd-ph-icon">▢</div>
              <div class="rd-ph-label">Composite hero image</div>
              <div class="rd-ph-desc">Drop image with regions for {{ steps.length }} pins</div>
            </div>
            <img v-else class="rd-img" :src="heroSrc" alt="" />

            <div
              v-for="(s, i) in steps"
              :key="`pin-${i}`"
              class="rd-pin"
              :class="pinClass(i)"
              :style="s.pin ? { top: s.pin.top, left: s.pin.left } : {}"
            >
              <span class="rd-pin-num">{{ i + 1 }}</span>
              <span class="rd-pin-label">{{ s.title }}</span>
            </div>

            <div class="rd-caption">
              <div class="rd-kicker">{{ isSetup ? 'Briefing' : activeStep?.kicker || `Step ${stepIndex}` }}</div>
              <div class="rd-cap-title">{{ isSetup ? (overview || title) : (activeStep?.heroCaption || activeStep?.title) }}</div>
            </div>
          </div>
        </template>
      </div>

      <!-- RIGHT: STACKED CARDS -->
      <div class="rd-stack">

        <!-- CARD A: Ingredients ↔ Step-by-step -->
        <div class="rd-card">
          <div class="rd-card-head">
            <h3>{{ cardATitle }}</h3>
            <div class="rd-badge">{{ cardABadge }}</div>
          </div>

          <ul v-if="isSetup" class="rd-ing-list">
            <li v-for="(it, i) in ingredients" :key="`ing-${i}`">
              <span class="k">{{ it.label }}</span>
              <span class="v">
                {{ it.value }}
                <small v-if="it.note">{{ it.note }}</small>
              </span>
            </li>
          </ul>

          <ol v-else class="rd-step-list">
            <li
              v-for="(s, i) in steps"
              :key="`st-${i}`"
              :class="stepClass(i)"
            >
              <strong>{{ s.title }}</strong>
              <div v-if="s.detail" class="rd-step-detail">{{ s.detail }}</div>
            </li>
          </ol>
        </div>

        <!-- CARD B: Overview ↔ Done looks like -->
        <div class="rd-card accent">
          <div class="rd-card-head">
            <h3>{{ cardBTitle }}</h3>
            <div class="rd-badge">{{ cardBBadge }}</div>
          </div>
          <div class="rd-ovw">
            <template v-if="isSetup">
              <p>{{ overview }}</p>
            </template>
            <template v-else>
              <p v-if="activeStep?.detail">{{ activeStep.detail }}</p>
              <div v-if="activeStep?.expected" class="rd-expect">{{ activeStep.expected }}</div>
            </template>
          </div>
        </div>

      </div>
    </div>

    <!-- FOOT: progress rail -->
    <footer class="rd-foot">
      <div class="rd-crumb">{{ isSetup ? 'Briefing' : `Step ${stepIndex} of ${steps.length}` }}</div>
      <div class="rd-rail">
        <span
          v-for="(s, i) in steps"
          :key="`pip-${i}`"
          class="rd-pip"
          :class="pipClass(i)"
        ></span>
      </div>
      <div class="rd-crumb">{{ stepIndex < steps.length ? 'Press → to advance' : '✓ End of demo' }}</div>
    </footer>

  </div>
</template>

<style scoped>
:root {
  --rd-cream:      #F2EFE9;
  --rd-cream-warm: #EDE9DF;
  --rd-text-muted: #6B6356;
}

.rd-slide {
  width: 100%; height: 100%;
  background: #FFFFFF; color: #1a0a30;
  display: grid; grid-template-rows: auto 1fr auto;
  padding: 1.6% 2.2%;
  box-sizing: border-box; overflow: hidden;
  font-size: clamp(11px, 1.15vw, 17px);
  border-top: 4px solid var(--uw-gold-bright, #D4A853);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
}

/* HEAD */
.rd-head { margin-bottom: 0.7em; }
.rd-eyebrow {
  font-family: var(--mono, "JetBrains Mono", ui-monospace, monospace);
  font-size: 0.58em; text-transform: uppercase; letter-spacing: 0.16em;
  color: var(--uw-gold-bright, #D4A853); font-weight: 700;
  margin-bottom: 0.3em;
}
.rd-title {
  font-size: 2.1em; margin: 0;
  color: #1a0a30; font-weight: 800;
  letter-spacing: -0.015em; line-height: 1;
}
.rd-meta {
  margin-top: 0.45em;
  font-size: 0.78em; color: #6B6356; opacity: 0.85;
}

/* BODY */
.rd-body {
  display: grid;
  grid-template-columns: 1fr 0.95fr;
  gap: 1.1em;
  min-height: 0;
}

/* HERO */
.rd-hero {
  position: relative;
  border-radius: 16px; overflow: hidden;
  min-height: 0; background: #1F1430;
}
.rd-frame {
  position: absolute; inset: 0;
  opacity: 0; transition: opacity 0.42s ease;
}
.rd-frame.active { opacity: 1; }
.rd-bg { position: absolute; inset: 0; }
.rd-img {
  position: absolute; inset: 0;
  width: 100%; height: 100%; object-fit: cover;
}
.rd-placeholder {
  position: absolute; inset: 0;
  display: grid; place-items: center; text-align: center; padding: 1.5em;
  z-index: 1;
}
.rd-ph-icon {
  font-family: var(--mono, monospace); font-size: 2.4em;
  color: rgba(255,255,255,0.35); margin-bottom: 0.2em;
}
.rd-ph-label {
  font-family: var(--mono, monospace); font-size: 0.65em;
  text-transform: uppercase; letter-spacing: 0.16em;
  color: rgba(255,255,255,0.65); font-weight: 700;
}
.rd-ph-desc {
  font-size: 0.85em; color: rgba(255,255,255,0.7);
  margin-top: 0.3em; max-width: 28ch; line-height: 1.4;
}

/* Distinct gradient treatments per cinematic frame */
.rd-frame[data-frame="0"] .rd-bg {
  background:
    radial-gradient(ellipse at 30% 30%, rgba(212,168,83,0.30) 0%, transparent 60%),
    radial-gradient(ellipse at 70% 70%, rgba(123,93,176,0.35) 0%, transparent 60%),
    linear-gradient(135deg, #2D1A52 0%, #4B2E83 100%);
}
.rd-frame[data-frame="1"] .rd-bg {
  background:
    linear-gradient(180deg, #1A1A2E 0%, #16213E 100%);
}
.rd-frame[data-frame="2"] .rd-bg {
  background:
    radial-gradient(ellipse at 40% 50%, rgba(212,168,83,0.35) 0%, transparent 55%),
    linear-gradient(180deg, #2D1A52 0%, #1a0a30 100%);
}
.rd-frame[data-frame="3"] .rd-bg {
  background:
    radial-gradient(ellipse at 60% 40%, rgba(237,232,245,0.20) 0%, transparent 55%),
    linear-gradient(135deg, #4B2E83 0%, #7B5DB0 100%);
}
.rd-frame[data-frame="4"] .rd-bg {
  background:
    repeating-linear-gradient(45deg, rgba(212,168,83,0.08) 0 8px, transparent 8px 16px),
    linear-gradient(180deg, #1a0a30 0%, #2D1A52 100%);
}
.rd-frame[data-frame="5"] .rd-bg {
  background:
    radial-gradient(ellipse at 50% 30%, rgba(212,168,83,0.30) 0%, transparent 60%),
    linear-gradient(180deg, #16213E 0%, #1a0a30 100%);
}
.rd-frame[data-frame="static"] .rd-bg {
  background:
    radial-gradient(ellipse at 50% 50%, rgba(212,168,83,0.20) 0%, transparent 70%),
    linear-gradient(135deg, #2D1A52 0%, #4B2E83 60%, #1a0a30 100%);
}

/* CAPTION */
.rd-caption {
  position: absolute; left: 0; right: 0; bottom: 0; z-index: 2;
  background: linear-gradient(180deg, transparent 0%, rgba(20,8,40,0.92) 100%);
  color: #FFFFFF;
  padding: 1.4em 1em 0.85em;
  display: grid; gap: 0.2em;
}
.rd-kicker {
  font-family: var(--mono, monospace); font-size: 0.6em;
  text-transform: uppercase; letter-spacing: 0.14em;
  color: var(--uw-gold-bright, #D4A853); font-weight: 700;
}
.rd-cap-title { font-size: 0.95em; font-weight: 700; line-height: 1.3; }

/* PINS (annotated mode) */
.rd-pin {
  position: absolute; z-index: 3;
  width: 2.4em; height: 2.4em; border-radius: 999px;
  background: #FFFFFF; color: #2D1A52;
  display: grid; place-items: center;
  font-family: var(--mono, monospace); font-weight: 700; font-size: 0.95em;
  box-shadow: 0 4px 16px rgba(0,0,0,0.5), 0 0 0 3px rgba(255,255,255,0.6);
  transform: translate(-50%, -50%);
  transition: transform 0.3s ease, opacity 0.3s ease, background 0.3s ease;
  cursor: default;
}
.rd-pin-label {
  position: absolute;
  left: 110%; top: 50%; transform: translateY(-50%);
  background: rgba(20,8,40,0.92); color: #FFFFFF;
  font-family: Inter, sans-serif; font-weight: 600;
  font-size: 0.55em; padding: 0.4em 0.7em; border-radius: 4px;
  white-space: nowrap; opacity: 0; transition: opacity 0.3s ease;
  pointer-events: none;
}
.rd-pin.dim { opacity: 0.32; transform: translate(-50%, -50%) scale(0.8); }
.rd-pin.active {
  background: var(--uw-gold-bright, #D4A853); color: #2D1A52;
  transform: translate(-50%, -50%) scale(1.18);
  animation: rd-pulse 1.8s ease-in-out infinite;
}
.rd-pin.active .rd-pin-label { opacity: 1; }
.rd-pin.done {
  background: #EDE8F5; color: #2D1A52;
  opacity: 0.7;
}
.rd-pin.done .rd-pin-num { display: none; }
.rd-pin.done::before { content: "✓"; }
@keyframes rd-pulse {
  0%, 100% { box-shadow: 0 0 0 6px rgba(212,168,83,0.35), 0 4px 16px rgba(0,0,0,0.5); }
  50%      { box-shadow: 0 0 0 14px rgba(212,168,83,0.08), 0 4px 16px rgba(0,0,0,0.5); }
}
/* Default 4-pin layout if pin positions are not provided */
.rd-pin:nth-of-type(1):not([style*="top"]) { top: 28%; left: 24%; }
.rd-pin:nth-of-type(2):not([style*="top"]) { top: 56%; left: 58%; }
.rd-pin:nth-of-type(3):not([style*="top"]) { top: 72%; left: 36%; }
.rd-pin:nth-of-type(4):not([style*="top"]) { top: 38%; left: 76%; }

/* STACKED CARDS */
.rd-stack {
  display: grid;
  grid-template-rows: 1.45fr 1fr;
  gap: 0.8em; min-height: 0;
}
.rd-card {
  background: #F2EFE9; border-radius: 16px;
  padding: 0.9em 1.05em;
  display: grid; grid-template-rows: auto 1fr;
  gap: 0.45em; min-height: 0;
}
.rd-card.accent { background: #EDE9DF; }
.rd-card-head {
  display: flex; align-items: center; justify-content: space-between; gap: 0.5em;
}
.rd-card-head h3 {
  margin: 0; font-size: 1em; font-weight: 700;
  color: #1a0a30; letter-spacing: -0.005em;
}
.rd-badge {
  font-family: var(--mono, monospace); font-size: 0.6em;
  color: var(--uw-purple, #4B2E83);
  background: #FFFFFF; border: 1px solid #E5E0F0;
  padding: 2px 9px; border-radius: 999px;
  font-weight: 600; letter-spacing: 0.06em;
}

/* Ingredients */
.rd-ing-list {
  margin: 0; padding: 0; list-style: none;
  display: grid; align-content: start;
  min-height: 0; overflow: hidden;
}
.rd-ing-list li {
  border-top: 1px solid rgba(0,0,0,0.07); padding: 0.4em 0;
  font-size: 0.84em; color: #1a0a30; line-height: 1.35;
  display: grid; grid-template-columns: auto 1fr; gap: 0.55em; align-items: baseline;
}
.rd-ing-list li:first-child { border-top: none; }
.rd-ing-list li .k {
  font-family: var(--mono, monospace); font-size: 0.85em;
  color: var(--uw-purple, #4B2E83);
  font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em;
  white-space: nowrap;
}
.rd-ing-list li .v { font-family: var(--mono, monospace); font-size: 0.9em; color: #1a0a30; }
.rd-ing-list li .v small {
  display: block; color: #6B6356; font-size: 0.85em;
  margin-top: 0.05em; font-family: var(--mono, monospace);
}

/* Steps */
.rd-step-list {
  margin: 0; padding: 0; list-style: none; counter-reset: rdstp;
  display: grid; align-content: start; gap: 0.45em; min-height: 0;
}
.rd-step-list li {
  counter-increment: rdstp;
  display: grid; grid-template-columns: 1.6em 1fr;
  gap: 0.6em; align-items: start;
  font-size: 0.85em; color: #1a0a30; line-height: 1.35;
  opacity: 0.32; transition: opacity 0.3s ease;
}
.rd-step-list li.active { opacity: 1; }
.rd-step-list li.done { opacity: 0.55; }
.rd-step-list li::before {
  content: counter(rdstp);
  font-family: var(--mono, monospace); font-weight: 700; font-size: 0.82em;
  color: #FFFFFF; background: var(--uw-purple, #4B2E83);
  width: 1.6em; height: 1.6em; border-radius: 4px;
  display: inline-flex; align-items: center; justify-content: center; line-height: 1;
}
.rd-step-list li.done::before {
  content: "✓"; background: var(--uw-gold-bright, #D4A853); color: #2D1A52;
}
.rd-step-list li.active::before {
  background: #2D1A52;
  box-shadow: 0 0 0 3px rgba(212,168,83,0.4);
}
.rd-step-list li strong { color: #2D1A52; font-weight: 700; }
.rd-step-detail { font-size: 0.92em; color: #6B6356; margin-top: 0.15em; }

/* Overview / Expected */
.rd-ovw { font-size: 0.88em; color: #1a0a30; line-height: 1.5; align-self: start; }
.rd-ovw p { margin: 0; }
.rd-expect {
  margin-top: 0.5em; padding: 0.5em 0.7em;
  background: #FFFFFF;
  border-left: 3px solid var(--uw-gold-bright, #D4A853);
  border-radius: 0 4px 4px 0;
  font-family: var(--mono, monospace); font-size: 0.82em; color: #1a0a30;
}
.rd-expect::before {
  content: "Done looks like · ";
  font-size: 0.85em; font-weight: 700;
  color: var(--uw-purple, #4B2E83);
  text-transform: uppercase; letter-spacing: 0.08em;
}

/* FOOT */
.rd-foot {
  margin-top: 0.75em;
  display: grid; grid-template-columns: auto 1fr auto;
  align-items: center; gap: 0.8em;
}
.rd-crumb {
  font-family: var(--mono, monospace); font-size: 0.66em;
  color: var(--uw-purple, #4B2E83); opacity: 0.7; letter-spacing: 0.05em;
}
.rd-rail {
  display: flex; gap: 0.4em;
  align-items: center; justify-content: center;
}
.rd-pip {
  width: 2.5em; height: 4px; background: #E5E0F0;
  border-radius: 999px; transition: background 0.25s, transform 0.25s;
}
.rd-pip.done { background: var(--uw-gold-bright, #D4A853); }
.rd-pip.active { background: #2D1A52; transform: scaleY(2); }
</style>

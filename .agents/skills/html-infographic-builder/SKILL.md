---
name: html-infographic-builder
description: Generate a standalone HTML data report with Chart.js visualizations, UW purple/gold color palette, card-based responsive layout, and professional typography hierarchy. Use when the user asks to create a data report, infographic, visual summary, HTML dashboard, or says "make this visual" or "generate a report from this data."
---

# HTML Infographic Builder

Generates a single-file, self-contained HTML data report using Chart.js and UW branding. No build step, no external dependencies beyond CDN links.

## When to Use

- User asks to create a data report, infographic, or visual summary from tabular data
- User wants an HTML artifact they can open in a browser and share
- Any request to "visualize," "report on," or "summarize" a dataset in a presentable format
- Supplement to a data analysis — after findings are established, render them visually

## Inputs

- Tabular data (CSV, JSON, markdown table, or paste)
- Optional: target audience (manager / executive / technical team)
- Optional: specific metrics or claims to highlight

## Process

1. Identify 3-5 key findings from the data before generating any HTML
2. Select chart types appropriate to the data shape:
   - Comparisons across categories: bar chart
   - Trends over time: line chart
   - Part-to-whole: donut/pie (use sparingly)
   - Distribution: histogram or box plot (use Chart.js custom logic)
   - Rankings: horizontal bar chart
3. Draft a narrative arc: headline finding → supporting evidence → context → recommendation
4. Generate a single HTML file with:
   - `<meta charset="UTF-8">` and `<meta name="viewport">`
   - Chart.js loaded from CDN: `https://cdn.jsdelivr.net/npm/chart.js`
   - Inter font from Google Fonts
   - Inline CSS using UW design tokens (see token reference below)
   - Card-based grid layout, responsive
   - One chart per card
   - Summary stats row at the top
   - Footer with data source citation and generation date

## Design Tokens (UW Palette)

```css
--uw-purple:      #4B2E83;
--uw-purple-mid:  #7B5DB0;
--uw-gold:        #D4A853;
--uw-gold-pale:   #FAF5E8;
--text-primary:   #1C1917;
--text-muted:     #78716C;
--surface:        #FFFFFF;
--surface-alt:    #F5F5F5;
--border:         #E7E5E4;
font-family: Inter, ui-sans-serif, system-ui, sans-serif;
```

Chart color sequence (use in order): `#4B2E83`, `#D4A853`, `#7B5DB0`, `#B7A57A`, `#9C8AAE`

## HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- meta, fonts, Chart.js CDN, inline CSS -->
</head>
<body>
  <header><!-- title, subtitle, date --></header>
  <section class="stats-row"><!-- 3-4 headline KPIs --></section>
  <main class="card-grid">
    <!-- One .card per chart or finding -->
    <div class="card">
      <h2 class="card-title">...</h2>
      <canvas id="chart-1"></canvas>
      <p class="card-note">Source: [filename], [row range]</p>
    </div>
  </main>
  <footer><!-- data source, generated date, caveats --></footer>
  <script>
    // Chart.js initialization — one chart per canvas element
  </script>
</body>
</html>
```

## Outputs

- Single `report.html` file, self-contained (open with any browser)
- File name: `[topic]-report-[YYYY-MM-DD].html`

## Quality Rules

- Every chart must have a plain-English caption explaining what it shows
- Data source citation must appear below each chart (file name + row range if applicable)
- Footer must include: data source, generation date, and any known data quality caveats
- No chart without a label axis or legend
- Do not include raw data tables in the HTML (keep it visual, not a spreadsheet dump)
- If sample size is under 30, add a note: "Small sample — interpret with caution"

## Acceptance Criteria

- [ ] HTML opens in browser with no console errors
- [ ] At least 2 charts present, each with a caption
- [ ] Headline KPI row visible above the fold
- [ ] Data source citations present for each chart
- [ ] File is self-contained (no broken asset links)
- [ ] Color palette matches UW tokens

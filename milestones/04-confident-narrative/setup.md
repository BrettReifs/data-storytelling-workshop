# Milestone 4 — Setup

## Dataset Loading for Context Bleed Demo

Both datasets must be loaded into the harnessed workspace before starting Milestone 4.

Verify both are present:
```
workspace-harnessed/data/coffee-shops/  (5 files)
workspace-harnessed/data/job-market/    (3 files)
```

If any files are missing, run from the repo root:
```bash
python scripts/generate_data.py
```
Then copy to the workspace:
```bash
# macOS / Linux
cp data/coffee-shops/* workspace-harnessed/data/coffee-shops/
cp data/job-market/*   workspace-harnessed/data/job-market/

# Windows (PowerShell)
Copy-Item data\coffee-shops\* workspace-harnessed\data\coffee-shops\ -Force
Copy-Item data\job-market\*   workspace-harnessed\data\job-market\ -Force
```

## Forking for Your Own Use

To use this milestone framework with your own data:

1. Replace the data files in `workspace-harnessed/data/` with your own CSV/JSON files
2. Update the "Known Quality Issues" section in `workspace-harnessed/CLAUDE.md` to match your data
3. Update the dataset scoping rules in `CLAUDE.md` to name your actual file paths
4. Run the `data-refinement-interview` skill — it generates questions from your actual data, not hardcoded templates

The skills are dataset-agnostic. They work with any tabular data.

## Audience Variant Customization

The three audience variants (shop manager / campus VP / vendor committee) are specific to the coffee shop scenario.

For your own data, define your audience variants in `CLAUDE.md`:
```
## Audience Variants
When generating reports, produce variants for:
- [Audience A]: emphasize [their key metrics]
- [Audience B]: emphasize [their key metrics]
```

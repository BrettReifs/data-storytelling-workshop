#!/usr/bin/env bash
# setup.sh — Student quickstart for data-storytelling-workshop
# Run from repo root: bash scripts/setup.sh

set -e

echo "Data Storytelling Workshop — Student Quickstart"
echo "================================================"
echo ""

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VER=$(node --version)
    echo "[PASS] Node.js $NODE_VER"
else
    echo "[WARN] Node.js not found. Install from https://nodejs.org (v18+ required for Slidev)"
fi

# Check Python
if command -v python3 &> /dev/null; then
    PY_VER=$(python3 --version)
    echo "[PASS] $PY_VER"
else
    echo "[WARN] Python 3 not found. Required only if regenerating data files."
fi

# Check data files
echo ""
echo "Checking data files..."

COFFEE_DIR="data/coffee-shops"
JOB_DIR="data/job-market"
REQUIRED_COFFEE="shop-sales.csv menu-catalog.json social-signals.csv vendor-bids.csv shop-profiles.md"
REQUIRED_JOB="job-postings.csv internship-programs.csv skills-demand.csv"

MISSING=0

for f in $REQUIRED_COFFEE; do
    if [ -f "$COFFEE_DIR/$f" ]; then
        echo "[PASS] $COFFEE_DIR/$f"
    else
        echo "[FAIL] $COFFEE_DIR/$f — missing"
        MISSING=$((MISSING+1))
    fi
done

for f in $REQUIRED_JOB; do
    if [ -f "$JOB_DIR/$f" ]; then
        echo "[PASS] $JOB_DIR/$f"
    else
        echo "[FAIL] $JOB_DIR/$f — missing"
        MISSING=$((MISSING+1))
    fi
done

if [ "$MISSING" -gt 0 ]; then
    echo ""
    echo "Regenerating $MISSING missing data file(s)..."
    python3 scripts/generate_data.py
    echo ""
    echo "Syncing to workspaces..."
    cp data/coffee-shops/* workspace-naive/data/
    cp data/coffee-shops/* workspace-harnessed/data/coffee-shops/
    cp data/job-market/*   workspace-harnessed/data/job-market/
fi

# Check skills in harnessed workspace
echo ""
echo "Checking harnessed workspace skills..."
SKILLS_DIR="workspace-harnessed/.agents/skills"
REQUIRED_SKILLS="html-infographic-builder data-confidence-scorer spotlight-walkthrough data-refinement-interview"

for s in $REQUIRED_SKILLS; do
    if [ -f "$SKILLS_DIR/$s/SKILL.md" ]; then
        echo "[PASS] $s"
    else
        echo "[WARN] $s not found in $SKILLS_DIR — copying from skills/"
        mkdir -p "$SKILLS_DIR/$s"
        cp "skills/$s/SKILL.md" "$SKILLS_DIR/$s/SKILL.md"
    fi
done

echo ""
echo "Setup complete."
echo ""
echo "Next steps:"
echo "  1. Open workspace-naive/ in your editor for Milestones 1-2"
echo "  2. Open workspace-harnessed/ in your editor for Milestones 3-4"
echo "  3. See milestones/01-naive-pass/README.md to begin"
echo ""
echo "Workshop repo: https://github.com/BrettReifs/data-storytelling-workshop"

# setup.ps1 — Student quickstart for data-storytelling-workshop
# Run from repo root: .\scripts\setup.ps1

$ErrorActionPreference = "Stop"

Write-Host "Data Storytelling Workshop -- Student Quickstart"
Write-Host "================================================"
Write-Host ""

# Check Node.js
try {
    $nodeVer = node --version 2>&1
    Write-Host "[PASS] Node.js $nodeVer"
} catch {
    Write-Host "[WARN] Node.js not found. Install from https://nodejs.org (v18+ required for Slidev)"
}

# Check Python
try {
    $pyVer = python --version 2>&1
    Write-Host "[PASS] $pyVer"
} catch {
    Write-Host "[WARN] Python not found. Required only if regenerating data files."
}

# Check data files
Write-Host ""
Write-Host "Checking data files..."

$coffeeDir = "data\coffee-shops"
$jobDir    = "data\job-market"
$requiredCoffee = @("shop-sales.csv","menu-catalog.json","social-signals.csv","vendor-bids.csv","shop-profiles.md")
$requiredJob    = @("job-postings.csv","internship-programs.csv","skills-demand.csv")

$missing = 0

foreach ($f in $requiredCoffee) {
    $path = Join-Path $coffeeDir $f
    if (Test-Path $path) {
        Write-Host "[PASS] $path"
    } else {
        Write-Host "[FAIL] $path -- missing"
        $missing++
    }
}

foreach ($f in $requiredJob) {
    $path = Join-Path $jobDir $f
    if (Test-Path $path) {
        Write-Host "[PASS] $path"
    } else {
        Write-Host "[FAIL] $path -- missing"
        $missing++
    }
}

if ($missing -gt 0) {
    Write-Host ""
    Write-Host "Regenerating $missing missing data file(s)..."
    python scripts\generate_data.py
    Write-Host ""
    Write-Host "Syncing to workspaces..."
    Copy-Item "$coffeeDir\*" "workspace-naive\data\" -Force
    Copy-Item "$coffeeDir\*" "workspace-harnessed\data\coffee-shops\" -Force
    Copy-Item "$jobDir\*"    "workspace-harnessed\data\job-market\" -Force
}

# Check skills in harnessed workspace
Write-Host ""
Write-Host "Checking harnessed workspace skills..."

$skillsDir = "workspace-harnessed\.agents\skills"
$requiredSkills = @("html-infographic-builder","data-confidence-scorer","spotlight-walkthrough","data-refinement-interview")

foreach ($s in $requiredSkills) {
    $skillPath = Join-Path $skillsDir "$s\SKILL.md"
    if (Test-Path $skillPath) {
        Write-Host "[PASS] $s"
    } else {
        Write-Host "[WARN] $s not found -- copying from skills\"
        New-Item -ItemType Directory -Path (Join-Path $skillsDir $s) -Force | Out-Null
        Copy-Item "skills\$s\SKILL.md" (Join-Path $skillsDir "$s\SKILL.md")
    }
}

Write-Host ""
Write-Host "Setup complete."
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Open workspace-naive\ in your editor for Milestones 1-2"
Write-Host "  2. Open workspace-harnessed\ in your editor for Milestones 3-4"
Write-Host "  3. See milestones\01-naive-pass\README.md to begin"
Write-Host ""
Write-Host "Workshop repo: https://github.com/BrettReifs/data-storytelling-workshop"

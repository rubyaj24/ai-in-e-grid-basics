# setup.ps1
# Run this once to create a virtual environment and install everything:
#   PowerShell -ExecutionPolicy Bypass -File setup.ps1

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -LiteralPath $ProjectRoot

Write-Host "=== AI in E-Grid Basics — Setup ===" -ForegroundColor Cyan

# Step 1: Create virtual environment
if (-not (Test-Path -LiteralPath "venv")) {
    Write-Host "[1/4] Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
} else {
    Write-Host "[1/4] Virtual environment already exists, skipping." -ForegroundColor Green
}

# Step 2: Activate and upgrade pip
Write-Host "[2/4] Upgrading pip..." -ForegroundColor Yellow
& "venv\Scripts\python.exe" -m pip install --upgrade pip

# Step 3: Install dependencies
Write-Host "[3/5] Installing dependencies..." -ForegroundColor Yellow
& "venv\Scripts\pip.exe" install -r requirements.txt

# Step 4: Install project package
Write-Host "[4/5] Installing project package..." -ForegroundColor Yellow
& "venv\Scripts\pip.exe" install -e .

# Step 5: Generate data
Write-Host "[5/5] Generating synthetic smart meter data..." -ForegroundColor Yellow
& "venv\Scripts\python.exe" -m egrid_learning.data.generator

Write-Host ""
Write-Host "=== All done! ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "What next?"
Write-Host "  Run a notebook:        venv\Scripts\jupyter.exe notebook notebooks\01_explore_the_data.ipynb"
Write-Host "  Run a demo:            venv\Scripts\python.exe demos\01_forecasting.py"
Write-Host "  Launch the dashboard:  venv\Scripts\streamlit.exe run demos\03_interactive_dashboard.py"
Write-Host ""
Write-Host "Need help? Open docs\00-quickstart.md"

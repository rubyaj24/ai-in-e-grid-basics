#!/usr/bin/env bash
# setup.sh — Run once to create venv and install everything
#   bash setup.sh

set -euo pipefail
cd "$(dirname "$0")"

echo "=== AI in E-Grid Basics — Setup ==="

# Step 1
if [ ! -d "venv" ]; then
    echo "[1/4] Creating virtual environment..."
    python3 -m venv venv
else
    echo "[1/4] Virtual environment exists, skipping."
fi

# Step 2
echo "[2/4] Upgrading pip..."
venv/bin/python -m pip install --upgrade pip

# Step 3
echo "[3/4] Installing dependencies..."
venv/bin/pip install -r requirements.txt

# Step 4
echo "[4/4] Generating synthetic smart meter data..."
venv/bin/python -m egrid_learning.data.generator

echo ""
echo "=== All done! ==="
echo ""
echo "What next?"
echo "  Run a notebook:       venv/bin/jupyter notebook notebooks/01_explore_the_data.ipynb"
echo "  Run a demo:           venv/bin/python demos/01_forecasting.py"
echo "  Launch the dashboard: venv/bin/streamlit run demos/03_interactive_dashboard.py"
echo ""
echo "Need help? Open docs/00-quickstart.md"

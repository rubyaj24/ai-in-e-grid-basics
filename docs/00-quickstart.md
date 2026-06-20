# 00 — Quickstart: Your first 5 minutes

Welcome. This is the place where AI meets the power grid — and you do
not need to know anything about either to get started.

## What you will have in 5 minutes

A working Python environment with:
- Synthetic smart meter data (no real data needed, no internet)
- Four demos that each teach one AI concept through a grid problem
- An interactive dashboard you can play with like a video game

## Step 1: Set up

If you are on **Windows**, open PowerShell and run:

```powershell
.\setup.ps1
```

If you are on **Mac or Linux**, open a terminal and run:

```bash
bash setup.sh
```

This will:
1. Create a virtual environment (a safe sandbox for Python packages)
2. Install everything we need
3. Generate the synthetic dataset

Takes about 2-3 minutes on a decent connection.

## Step 2: Run a demo

Once setup finishes, try the forecasting demo:

```bash
# On Windows:
venv\Scripts\python.exe demos\01_forecasting.py

# On Mac / Linux:
venv/bin/python demos/01_forecasting.py
```

You will see three numbers printed — error scores for three different
ways of predicting electricity load. One of them is basically guessing.
One uses math. One uses machine learning. You will see which wins.

## Step 3: Launch the fun one

```bash
# Windows:
venv\Scripts\streamlit.exe run demos\03_interactive_dashboard.py

# Mac / Linux:
venv/bin/streamlit run demos/03_interactive_dashboard.py
```

A page will open in your browser with sliders for hour, day, and
temperature. Move them. Watch the prediction change. That is AI
responding to you in real time.

## What to read next

| You want to... | Read this |
|---|---|
| Understand what a smart grid actually is | `01-what-is-a-smart-grid.md` |
| See how the data was created | `02-understanding-data.md` |
| Walk through the forecasting demo step by step | `03-forecasting.md` |
| Learn how anomaly detection works | `04-anomaly-detection.md` |
| Play with the interactive dashboard | `05-interactive-app.md` |
| Peek at grid optimization | `06-grid-optimization.md` |
| Figure out what to learn next | `07-whats-next.md` |

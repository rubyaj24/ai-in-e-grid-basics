# AI in E-Grid Basics

Learn AI by working through real smart grid problems — forecasting,
anomaly detection, and optimization. No experience needed.

## What you will learn

Three AI tasks that every smart grid application falls into:

| Task | Grid problem | What you'll build |
|---|---|---|
| **Predict** | How much power tomorrow? | Load forecasting model |
| **Detect** | Theft or fault? | Unsupervised anomaly detection |
| **Optimize** | When to charge the battery? | Grid simulation with dispatch |

## Quick start

```powershell
# 1. Set up (2 minutes)
.\setup.ps1                     # Windows
# or: bash setup.sh             # Mac / Linux

# 2. Run a demo
venv\Scripts\python.exe demos\01_forecasting.py

# 3. Play with the interactive dashboard
venv\Scripts\streamlit.exe run demos\03_interactive_dashboard.py
```

## Project structure

| Path | What's there |
|---|---|
| `demos/` | 4 demos you run from the terminal |
| `notebooks/` | 4 Jupyter notebooks for hands-on exploration |
| `docs/` | 8 walkthrough docs — start with `00-quickstart.md` |
| `quizzes/` | Self-check questions with answers |
| `src/egrid_learning/` | Reusable code (generator, models, viz, grid sim) |

## The three AI tasks (the framework)

Every AI application in the power grid does one of three things:

1. **Predict** something — demand, solar generation, electricity price
2. **Detect** something — faults, theft, equipment failure
3. **Optimize** something — battery dispatch, storage scheduling

Each demo maps to one of these. Keep this framework in mind.

## Demos

| Demo | What it does | Run it |
|---|---|---|
| **1 — Forecasting** | Compares naive, linear, and ML approaches | `python demos/01_forecasting.py` |
| **2 — Anomaly Detection** | Catches injected theft/fault events | `python demos/02_anomaly_detection.py` |
| **3 — Interactive Dashboard** | Live slider-controlled prediction app | `streamlit run demos/03_interactive_dashboard.py` |
| **4 — Grid Optimization** | Simulates solar + battery dispatch | `python demos/04_grid_optimization.py` |

## Learning path

| Step | What | Time |
|---|---|---|
| 1 | Read `docs/00-quickstart.md` and get set up | 5 min |
| 2 | Read `docs/01-what-is-a-smart-grid.md` | 10 min |
| 3 | Open `notebooks/01_explore_the_data.ipynb` | 15 min |
| 4 | Read `docs/03-forecasting.md` then run demo 1 | 30 min |
| 5 | Read `docs/04-anomaly-detection.md` then run demo 2 | 25 min |
| 6 | Read `docs/05-interactive-app.md` then launch demo 3 | 15 min |
| 7 | Read `docs/06-grid-optimization.md` then run demo 4 | 15 min |
| 8 | Take the quizzes in `quizzes/` | 10 min |
| 9 | Try `notebooks/04_challenge_yourself.ipynb` | 20 min+ |

## Notes

- All data is synthetic and reproducible — results match exactly across machines.
- The time-based train/test split in forecasting is a deliberate teaching point
  (randomly shuffling time series leaks future information into training).
- Everything runs offline after setup. No real hardware or live grid data needed.
- Swap `data/smart_meter_data.csv` for any real smart meter dataset — just
  adjust column names.

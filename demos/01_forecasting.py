"""
DEMO 1: Load Forecasting — see why ML beats guessing

We compare three approaches:
  - Naive baseline ("same time yesterday")
  - Linear Regression
  - Random Forest

Then we show you which features the Random Forest thinks matter most.
"""

import pandas as pd
from src.egrid_learning.models.forecasting import run_all, FEATURES
from src.egrid_learning.visualization.plots import (
    plot_forecast,
    plot_model_comparison,
)

DATA_PATH = "data/smart_meter_data.csv"

print("=" * 55)
print("  DEMO 1: Load Forecasting with AI")
print("=" * 55)

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
results = run_all(df)

print("\n=== Forecasting results (Mean Absolute Error, kW) ===")
print(f"  Naive 'same time yesterday' baseline : {results['baseline_mae']:.3f}")
print(f"  Linear Regression                    : {results['lin_mae']:.3f}")
print(f"  Random Forest                        : {results['rf_mae']:.3f}")

# Which model won?
best = min(
    ("baseline", results["baseline_mae"]),
    ("linear regression", results["lin_mae"]),
    ("random forest", results["rf_mae"]),
    key=lambda x: x[1],
)
print(f"\n  Winner: {best[0]} (MAE = {best[1]:.3f} kW)")

print("\n=== What the Random Forest learned matters most ===")
for feat, imp in results["feature_importances"].items():
    print(f"  {feat:20s}  {imp:.3f}")

plot_model_comparison(results)
plot_forecast(
    results["test_timestamps"],
    results["y_test"],
    results["lin_pred"],
    results["rf_pred"],
    save_path="assets/images/forecast_result.png",
)

print("\nTip: Open docs/03-forecasting.md to walk through what each model does.")

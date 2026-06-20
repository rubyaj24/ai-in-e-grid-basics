"""
DEMO 2: Anomaly Detection — catching what doesn't belong

We inject fake "theft" and "fault" events into normal data, then try
to find them using:
  - Rolling z-score (statistical baseline)
  - Isolation Forest (an ML approach)

Compare recall and precision to see the trade-offs.
"""

import pandas as pd
from src.egrid_learning.models.anomaly import run_all
from src.egrid_learning.visualization.plots import plot_anomaly_detection

DATA_PATH = "data/smart_meter_data.csv"

print("=" * 55)
print("  DEMO 2: Anomaly / Theft / Fault Detection")
print("=" * 55)

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
results = run_all(df)

z = results["zscore_metrics"]
iso = results["iso_metrics"]

print(f"\nInjected anomalous points (for testing): {z['total_anomalies']}")
print()
print(f"{'Method':22s} {'Flagged':>8s}  {'Recall':>7s}  {'Precision':>10s}")
print("-" * 52)
print(f"{'Z-score (rolling)':22s} {z['flagged']:8d}  {z['recall']:.2f}  {z['precision']:.2f}")
print(f"{'Isolation Forest':22s} {iso['flagged']:8d}  {iso['recall']:.2f}  {iso['precision']:.2f}")

if iso["recall"] > z["recall"]:
    print("\n  Isolation Forest caught more anomalies (higher recall).")
else:
    print("\n  Z-score caught more anomalies (higher recall) this run.")

if iso["precision"] > z["precision"]:
    print("  Isolation Forest had fewer false alarms (higher precision).")
else:
    print("  Z-score had fewer false alarms (higher precision) this run.")

print("\n  Real-world takeaway: you can't maximize both at once.")
print("  The right balance depends on the cost of a missed fault vs.")
print("  the cost of a false alarm.")

plot_anomaly_detection(results["plot_df"],
    save_path="assets/images/anomaly_result.png")

print("\nTip: Open docs/04-anomaly-detection.md to dig into the details.")

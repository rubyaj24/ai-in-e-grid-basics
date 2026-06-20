"""
Anomaly detection for smart meter data.

Compares a statistical baseline (rolling z-score) against an ML approach
(Isolation Forest). Both are unsupervised — they don't need labeled
"this is an anomaly" data, which is the real-world scenario grid operators
face most of the time.

Includes synthetic anomaly injection for evaluation.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def inject_anomalies(df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """Add synthetic theft (dips) and fault (spikes) to the load column."""
    np.random.seed(seed)
    df = df.copy()
    df["is_anomaly_true"] = 0
    n = len(df)

    # Type 1: Theft — sudden near-zero dip (meter bypass)
    theft_idx = np.random.choice(n, size=6, replace=False)
    for i in theft_idx:
        span = slice(i, min(i + 8, n))
        df.loc[span, "load_kw"] *= 0.1
        df.loc[span, "is_anomaly_true"] = 1

    # Type 2: Fault — sudden spike (equipment failure)
    spike_idx = np.random.choice(n, size=6, replace=False)
    for i in spike_idx:
        span = slice(i, min(i + 4, n))
        df.loc[span, "load_kw"] *= 3.5
        df.loc[span, "is_anomaly_true"] = 1

    return df


def rolling_zscore(
    df: pd.DataFrame, window: int | None = None, threshold: float = 3.0
) -> pd.DataFrame:
    """Statistical baseline: flag points where rolling z-score exceeds threshold."""
    if window is None:
        window = 24 * 4 * 7
    df = df.copy()
    roll_mean = df["load_kw"].rolling(window, center=True, min_periods=24).mean()
    roll_std = df["load_kw"].rolling(window, center=True, min_periods=24).std()
    df["zscore"] = (df["load_kw"] - roll_mean) / roll_std
    df["flag_zscore"] = (df["zscore"].abs() > threshold).astype(int)
    return df


def isolation_forest_detect(
    df: pd.DataFrame, contamination: float = 0.02, features: list[str] | None = None
) -> pd.DataFrame:
    """ML-based unsupervised anomaly detection with Isolation Forest."""
    if features is None:
        features = ["load_kw", "hour", "dayofweek", "temperature_c"]
    df = df.copy()
    iso = IsolationForest(contamination=contamination, random_state=42)
    df["flag_isoforest"] = (iso.fit_predict(df[features]) == -1).astype(int)
    return df


def detection_metrics(df: pd.DataFrame, flag_col: str) -> dict:
    """Compute recall and precision for a given flag column against ground truth."""
    true_pos = ((df[flag_col] == 1) & (df["is_anomaly_true"] == 1)).sum()
    total_true = (df["is_anomaly_true"] == 1).sum()
    flagged = (df[flag_col] == 1).sum()

    recall = true_pos / total_true if total_true else 0.0
    precision = true_pos / flagged if flagged else 0.0
    return {
        "true_positives": int(true_pos),
        "total_anomalies": int(total_true),
        "flagged": int(flagged),
        "recall": recall,
        "precision": precision,
    }


def run_all(df: pd.DataFrame) -> dict:
    """Run both detection methods, inject anomalies, return comparison."""
    df = inject_anomalies(df)
    df = rolling_zscore(df)
    df = isolation_forest_detect(df)

    z_metrics = detection_metrics(df, "flag_zscore")
    iso_metrics = detection_metrics(df, "flag_isoforest")

    # Pick a window that contains anomalies for plotting
    # (we find the first anomaly index)
    anomaly_indices = df[df["is_anomaly_true"] == 1].index
    plot_start = max(anomaly_indices.min() - 50, 0) if len(anomaly_indices) else 0
    plot_end = min(plot_start + 800, len(df))
    plot_df = df.iloc[plot_start:plot_end]

    return {
        "df": df,
        "zscore_metrics": z_metrics,
        "iso_metrics": iso_metrics,
        "plot_df": plot_df,
    }

"""
Shared plotting helpers for all demos.
Keeps chart styling consistent across the project.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_forecast(
    timestamps: pd.Series,
    y_actual: np.ndarray,
    y_lin: np.ndarray,
    y_rf: np.ndarray,
    window_days: int = 3,
    save_path: str | None = None,
):
    """Plot actual vs predicted load for the last N days of test data."""
    window = 24 * 4 * window_days
    plt.figure(figsize=(12, 5))
    plt.plot(
        timestamps.iloc[-window:], y_actual[-window:],
        label="Actual", linewidth=2, color="#2c3e50",
    )
    plt.plot(
        timestamps.iloc[-window:], y_lin[-window:],
        label="Linear Regression", alpha=0.8, color="#e67e22",
    )
    plt.plot(
        timestamps.iloc[-window:], y_rf[-window:],
        label="Random Forest", alpha=0.8, color="#27ae60",
    )
    plt.xlabel("Time")
    plt.ylabel("Load (kW)")
    plt.title("Smart Meter Load Forecast: Actual vs Predicted")
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=120)
        print(f"Saved plot to {save_path}")
    plt.show()


def plot_anomaly_detection(
    plot_df: pd.DataFrame,
    save_path: str | None = None,
):
    """Plot load data with true anomalies and Isolation Forest flags."""
    plt.figure(figsize=(13, 5))
    plt.plot(
        plot_df["timestamp"], plot_df["load_kw"],
        label="Load (kW)", linewidth=1.2, color="#34495e",
    )
    true_anom = plot_df[plot_df["is_anomaly_true"] == 1]
    flagged_iso = plot_df[plot_df["flag_isoforest"] == 1]
    plt.scatter(
        true_anom["timestamp"], true_anom["load_kw"],
        color="orange", label="True injected anomaly", zorder=5, s=40,
    )
    plt.scatter(
        flagged_iso["timestamp"], flagged_iso["load_kw"],
        facecolors="none", edgecolors="red",
        label="Flagged by Isolation Forest", zorder=6, s=90,
    )
    plt.xlabel("Time")
    plt.ylabel("Load (kW)")
    plt.title("Anomaly Detection: Isolation Forest vs Injected Anomalies")
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=120)
        print(f"Saved plot to {save_path}")
    plt.show()


def plot_grid_dispatch(
    hours: np.ndarray,
    solar_profile: np.ndarray,
    load_profile: np.ndarray,
    grid_import: np.ndarray,
    battery_soc: list,
    save_path: str | None = None,
):
    """Two-panel plot: power flows + battery state of charge."""
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

    axes[0].plot(hours, solar_profile, label="Solar generation (MW)", color="orange")
    axes[0].plot(hours, load_profile, label="Neighborhood load (MW)", color="steelblue")
    axes[0].plot(hours, grid_import, label="Net grid import (MW)", color="black", linestyle="--")
    axes[0].axhline(0, color="gray", linewidth=0.5)
    axes[0].set_ylabel("MW")
    axes[0].set_title("Rule-Based Battery Dispatch on a 5-Bus Feeder")
    axes[0].legend()

    axes[1].plot(hours, battery_soc[:-1], label="Battery state of charge (%)", color="green")
    axes[1].set_xlabel("Hour of day")
    axes[1].set_ylabel("SOC (%)")
    axes[1].legend()

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=120)
        print(f"Saved plot to {save_path}")
    plt.show()


def plot_model_comparison(results: dict):
    """Bar chart comparing MAE across baseline, linear, and random forest."""
    models = ["Naive Baseline\n(same time yesterday)", "Linear Regression", "Random Forest"]
    values = [results["baseline_mae"], results["lin_mae"], results["rf_mae"]]
    colors = ["#95a5a6", "#e67e22", "#27ae60"]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(models, values, color=colors, edgecolor="white", linewidth=1.5)
    for bar, val in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
            f"{val:.3f}", ha="center", va="bottom", fontweight="bold",
        )
    plt.ylabel("Mean Absolute Error (kW)")
    plt.title("Forecasting Model Comparison")
    plt.tight_layout()
    plt.show()

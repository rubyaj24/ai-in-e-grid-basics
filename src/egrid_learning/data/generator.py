"""
generate_data.py -> src/egrid_learning/data/generator.py

Creates a realistic synthetic household/feeder load dataset.
No internet needed — everything runs offline.

Run:  python -m egrid_learning.data.generator
Writes: data/smart_meter_data.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path


def generate(output_dir: str | None = None) -> pd.DataFrame:
    """Generate 60 days of synthetic 15-minute smart meter readings.

    Returns a DataFrame with columns:
        timestamp, hour, dayofweek, is_weekend, temperature_c, load_kw
    """
    np.random.seed(42)

    periods = 60 * 24 * 4
    start = pd.Timestamp("2026-01-01")
    timestamps = pd.date_range(start, periods=periods, freq="15min")

    df = pd.DataFrame({"timestamp": timestamps})
    df["hour"] = df["timestamp"].dt.hour + df["timestamp"].dt.minute / 60
    df["dayofweek"] = df["timestamp"].dt.dayofweek
    df["is_weekend"] = (df["dayofweek"] >= 5).astype(int)

    # Daily load shape: base + morning peak + evening peak
    daily_shape = (
        1.0
        + 0.6 * np.exp(-((df["hour"] - 7.5) ** 2) / (2 * 1.2 ** 2))
        + 1.0 * np.exp(-((df["hour"] - 19.5) ** 2) / (2 * 1.5 ** 2))
    )

    weekend_adjustment = np.where(df["is_weekend"] == 1, 0.85, 1.0)
    seasonal = 1 + 0.15 * np.sin(2 * np.pi * df.index / (60 * 24 * 4))
    noise = np.random.normal(0, 0.07, size=periods)

    n_days = periods // (24 * 4) + 1
    daily_factor = np.random.normal(1.0, 0.18, size=n_days)
    daily_factor = np.repeat(daily_factor, 24 * 4)[:periods]

    temperature = (
        15
        + 8 * np.sin(2 * np.pi * (df.index - 2000) / (60 * 24 * 4))
        + np.random.normal(0, 1.5, size=periods)
    )
    df["temperature_c"] = temperature

    load_kw = 3.0 * daily_shape * weekend_adjustment * seasonal * daily_factor + noise
    load_kw += 0.02 * np.clip(temperature - 18, 0, None)
    load_kw += 0.015 * np.clip(5 - temperature, 0, None)
    load_kw = np.clip(load_kw, 0.2, None)

    df["load_kw"] = load_kw

    if output_dir:
        out_path = Path(output_dir) / "smart_meter_data.csv"
    else:
        out_path = Path(__file__).resolve().parents[3] / "data" / "smart_meter_data.csv"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path}")
    return df


if __name__ == "__main__":
    generate()

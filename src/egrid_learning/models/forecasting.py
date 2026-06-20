"""
Forecasting models for smart grid load prediction.

Three approaches, escalating in complexity:
  1. Naive baseline — "same time yesterday"
  2. Linear Regression
  3. Random Forest

Teaches why ML beats simple heuristics for time-series prediction.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add cyclical time features so the model understands hour/day as circular."""
    df = df.copy()
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["dow_sin"] = np.sin(2 * np.pi * df["dayofweek"] / 7)
    df["dow_cos"] = np.cos(2 * np.pi * df["dayofweek"] / 7)
    return df


FEATURES = ["hour_sin", "hour_cos", "dow_sin", "dow_cos", "is_weekend", "temperature_c"]


def train_test_split_time(df: pd.DataFrame, train_frac: float = 0.8):
    """Time-based split (never shuffle time-series data!)."""
    split = int(len(df) * train_frac)
    return (
        df.iloc[:split],
        df.iloc[split:],
    )


def naive_baseline(df: pd.DataFrame, test_df: pd.DataFrame) -> float:
    """Predict load = load from 24 hours ago. Returns MAE."""
    lag = 24 * 4
    pred = df["load_kw"].shift(lag).iloc[len(df) - len(test_df):]
    valid = ~pred.isna()
    if valid.sum() == 0:
        return float("nan")
    return mean_absolute_error(test_df["load_kw"][valid], pred[valid])


def train_linear_regression(X_train, y_train, X_test, y_test) -> tuple:
    """Train and evaluate linear regression. Returns (model, mae)."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    return model, mae, pred


def train_random_forest(
    X_train, y_train, X_test, y_test,
    n_estimators: int = 200, max_depth: int = 8,
) -> tuple:
    """Train and evaluate Random Forest. Returns (model, mae, predictions)."""
    model = RandomForestRegressor(
        n_estimators=n_estimators, max_depth=max_depth, random_state=42
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    return model, mae, pred


def run_all(df: pd.DataFrame) -> dict:
    """Run all three forecasting approaches and return results."""
    df = engineer_features(df)
    train_df, test_df = train_test_split_time(df)

    X_train = train_df[FEATURES]
    y_train = train_df["load_kw"]
    X_test = test_df[FEATURES]
    y_test = test_df["load_kw"]

    baseline_mae = naive_baseline(df, test_df)
    _, lin_mae, lin_pred = train_linear_regression(X_train, y_train, X_test, y_test)
    rf_model, rf_mae, rf_pred = train_random_forest(X_train, y_train, X_test, y_test)

    return {
        "test_timestamps": test_df["timestamp"],
        "y_test": y_test.values,
        "baseline_mae": baseline_mae,
        "lin_mae": lin_mae,
        "lin_pred": lin_pred,
        "rf_mae": rf_mae,
        "rf_pred": rf_pred,
        "rf_model": rf_model,
        "feature_importances": pd.Series(
            rf_model.feature_importances_, index=FEATURES
        ).sort_values(ascending=False),
    }

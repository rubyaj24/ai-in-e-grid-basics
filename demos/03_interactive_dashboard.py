"""
DEMO 3: Interactive Forecasting Dashboard

A live, clickable app where you move sliders and watch the AI's
prediction update instantly. The "wow" moment of the workshop.

Run:  streamlit run demos/03_interactive_dashboard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Smart Grid Load Forecaster", layout="centered",
    page_icon="⚡")

st.title("Smart Grid Load Forecaster")
st.write(
    "A Random Forest model trained on 60 days of synthetic smart meter data. "
    "Move the sliders and watch the prediction change instantly."
)

DATA_PATH = "data/smart_meter_data.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["dow_sin"] = np.sin(2 * np.pi * df["dayofweek"] / 7)
    df["dow_cos"] = np.cos(2 * np.pi * df["dayofweek"] / 7)
    return df


@st.cache_resource
def train_model(df):
    features = ["hour_sin", "hour_cos", "dow_sin", "dow_cos", "is_weekend", "temperature_c"]
    model = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=42)
    model.fit(df[features], df["load_kw"])
    return model, features


df = load_data()
model, features = train_model(df)

with st.sidebar:
    st.header("Controls")
    hour = st.slider("Hour of day", 0.0, 23.75, 18.0, step=0.25)
    dow_label = st.selectbox(
        "Day of week",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        index=4,
    )
    temperature = st.slider("Temperature (°C)", -5, 40, 20)

    st.divider()
    st.caption("Try changing the temperature to see how AC/ heating affects load.")

dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(dow_label)
is_weekend = 1 if dow >= 5 else 0

input_row = pd.DataFrame([{
    "hour_sin": np.sin(2 * np.pi * hour / 24),
    "hour_cos": np.cos(2 * np.pi * hour / 24),
    "dow_sin": np.sin(2 * np.pi * dow / 7),
    "dow_cos": np.cos(2 * np.pi * dow / 7),
    "is_weekend": is_weekend,
    "temperature_c": temperature,
}])

prediction = model.predict(input_row[features])[0]

col1, col2, col3 = st.columns(3)
col1.metric("Time", f"{int(hour):02d}:{int((hour % 1) * 60):02d}")
col2.metric("Day", dow_label)
col3.metric("Predicted Load", f"{prediction:.2f} kW")

# Daily curve
hours_range = np.arange(0, 24, 0.25)
day_curve = pd.DataFrame({
    "hour_sin": np.sin(2 * np.pi * hours_range / 24),
    "hour_cos": np.cos(2 * np.pi * hours_range / 24),
    "dow_sin": np.sin(2 * np.pi * dow / 7),
    "dow_cos": np.cos(2 * np.pi * dow / 7),
    "is_weekend": is_weekend,
    "temperature_c": temperature,
})
day_curve["predicted_load"] = model.predict(day_curve[features])

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(hours_range, day_curve["predicted_load"],
    label=f"Predicted curve ({dow_label})", linewidth=2)
ax.axvline(hour, color="red", linestyle="--", alpha=0.7)
ax.scatter([hour], [prediction], color="red", zorder=5, s=80)
ax.set_xlabel("Hour of day")
ax.set_ylabel("Predicted load (kW)")
ax.set_title("How load changes across the day")
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

with st.expander("How does this work?"):
    st.write("""
        **The model**: A Random Forest with 200 decision trees trained on 60 days
        of 15-minute smart meter readings. It learned:
        - Morning and evening peaks in demand
        - Lighter load on weekends
        - Extra load when it's hot (AC) or cold (heating)

        **What happens when you move a slider**: The app builds a new input row
        with your chosen values and runs it through the trained model. The model
        predicts the load *for that exact moment*. No retraining happens —
        it's just a single prediction from a fixed model.
    """)

with st.expander("Experiment ideas"):
    st.write("""
        - Set temperature to 35°C. How much does the load jump?
        - Compare a Tuesday at 8 AM vs a Saturday at 8 AM.
        - What happens at 3 AM on a weekday? Is the load higher or lower than noon?
        - Try the same time on Monday vs Sunday. Can you explain the difference?
    """)

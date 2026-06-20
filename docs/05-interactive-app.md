# 05 — Interactive App: where AI becomes a toy you can play with

> **The AI task**: Predict (same model as Demo 1)
> **The format**: A live web app you control with sliders
> **The demo**: `demos/03_interactive_dashboard.py`

## The story

So far we have been running scripts that print numbers and save plots.
That is fine for learning, but it does not *feel* like AI.

This demo changes that. You move sliders. The prediction updates
instantly. It feels like magic — but now you know the magic is just
a Random Forest model doing a single prediction.

## How to launch it

```bash
# Windows:
venv\Scripts\streamlit.exe run demos\03_interactive_dashboard.py

# Mac / Linux:
venv/bin/streamlit run demos/03_interactive_dashboard.py
```

A browser tab will open. You will see:
- Three sliders on the left (hour, day of week, temperature)
- A prediction displayed as a big number
- A chart showing the predicted load curve for the whole day

## What to try

Here are some experiments to build intuition:

### 1. Find the daily peak
Set the hour slider to 8 AM. Note the prediction. Now slide to
7 PM. Which is higher? Can you guess why before reading the answer?

*(Answer: Evening peak is usually higher because people are home
using lights, cooking, watching TV, and charging devices.)*

### 2. Weekend vs weekday
With everything else the same, switch from Tuesday to Sunday.
Does the load go up or down? Why?

*(Answer: Weekends have slightly lower and flatter load because
commercial buildings use less power and people's schedules are
more spread out.)*

### 3. The temperature effect
Set the time to 3 PM on a weekday. Now slide temperature from
20°C to 35°C. Watch the load increase — that is air conditioning.

Now slide from 20°C down to -5°C. You will see load increase again —
that is heating.

### 4. The overnight valley
Set the time to 3 AM on a weekday. The load should be at its lowest.
This is when most people are asleep, and it is the cheapest time to
charge electric vehicles or run appliances.

## Under the hood

When you move a slider, the app builds a single row of data with your
chosen values, encodes the hour and day as cyclical features, and runs
`model.predict()` on that row. The model was trained once when the app
started and stays fixed — no retraining.

The chart shows what the model thinks the entire day's load curve
would look like if *all* hours had your chosen temperature and
day of week. This helps you see where your selected moment sits
relative to the rest of the day.

## Why this is the "wow" moment

In our workshop experience, this is when things click for people.
They have been reading about features, models, predictions — and
then suddenly they are *controlling* the model and watching it
respond in real time. The abstract becomes tangible.

Take a few minutes to play before moving on.

---

**Your turn**: Try to find the combination of settings that produces
the highest possible load prediction. How much can you push it?
What combination gives the lowest?

**Check yourself**:
- Does the model retrain when you move a slider?
- Why does the chart show a curve even though you only selected one
  time point?

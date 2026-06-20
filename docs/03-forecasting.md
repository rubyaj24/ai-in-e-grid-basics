# 03 — Forecasting: teaching a computer to predict the future

> **The AI task**: Predict
> **The grid problem**: How much power will we need tomorrow?
> **The demo**: `demos/01_forecasting.py`

## The story

Remember our baker from the first doc? They need to guess how many
loaves to bake tomorrow. If they bake too few, customers leave angry.
If they bake too many, bread gets stale and money is wasted.

Grid operators have the same problem — except electricity cannot be
stored cheaply (yet). They need to match supply and demand *every
second*. A good forecast saves millions of dollars in wasted fuel
and prevents blackouts.

## How the demo works

We take our smart meter data and ask: can we predict the load for the
next 15 minutes? We try three approaches, going from simple to smart:

### Approach 1: The naive baseline ("same time yesterday")

This is the simplest possible prediction: whatever the load was 24 hours
ago, that is our guess for now. It is not terrible — load does follow
daily patterns — but it is also not great, because yesterday might have
been colder, or a holiday, or just different.

We call this a **baseline**. If a fancy ML model cannot beat this, it is
not worth using.

### Approach 2: Linear Regression

This is the simplest ML model. It learns a formula like:

```
load = 0.3 × (hour feature) + 0.1 × (temperature) + 1.2 × (weekend flag) + ...
```

It finds the best numbers (called "coefficients" or "weights") that
minimize the error on the training data.

Linear regression is fast, interpretable, and often works well enough.
But it assumes the relationship between features and load is a straight
line — which is not true for things like the morning peak.

### Approach 3: Random Forest

A Random Forest builds **200 decision trees**. Each tree is like a
flowchart that asks questions like "is it after 7 AM?" → "is the
temperature above 25°C?" → "is it a weekend?" and arrives at a
prediction.

Why 200 trees instead of one? A single tree can overfit — memorize
the training data instead of learning general patterns. Averaging
200 trees smooths out the mistakes of individual trees, giving a
more reliable prediction.

## What we measure: Mean Absolute Error (MAE)

We evaluate each approach using MAE — the average difference between
the predicted load and the actual load, in kilowatts. Lower is better.

If the naive baseline has MAE = 0.25 kW and the Random Forest has
MAE = 0.15 kW, the Random Forest's predictions are, on average,
0.1 kW closer to reality. That might not sound like much, but
multiply it by millions of homes and it is a huge difference.

## What the model learns (feature importances)

After training, the Random Forest can tell us which features it found
most useful. You will see output like:

```
hour_sin         0.423
temperature_c    0.251
dow_sin          0.142
...
```

The interpretation: hour of day is the strongest signal (people follow
daily routines), temperature matters (heating and cooling), and day of
week matters least (the weekly pattern is weaker).

This is useful for discussion: "Should we add a feature for holidays?
School vacation? A local sports event?"

## Common pitfall (worth a conversation)

If we had shuffled the data before splitting into train/test, our model
would have appeared to perform much better than it actually does. It
would have memorized patterns from the future and used them to predict
the past — which works great in a test but fails in production.

This is one of the most common mistakes in applied machine learning.
You will impress people if you catch it.

---

**Your turn**: In `demos/01_forecasting.py`, try changing
`n_estimators=200` to `n_estimators=10`. Does the Random Forest still
beat linear regression? What about `n_estimators=500`? Does
performance keep improving?

**Check yourself**:
- Why do we need a baseline model?
- What does MAE measure?
- Why would a grid operator prefer a slightly less accurate model that
  they can explain to regulators?

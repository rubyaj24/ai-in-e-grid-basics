# Quiz: Forecasting

Cover the answers with your hand, think, then check.

---

**Q1**: Why do we use a "naive baseline" instead of just jumping to ML models?

<details>
<summary>Answer</summary>
A baseline tells us whether the ML model is actually adding value. If the fancy model can't beat "predict yesterday's number," it's not worth using.
</details>

---

**Q2**: What does Mean Absolute Error (MAE) measure?

<details>
<summary>Answer</summary>
The average absolute difference between predicted values and actual values. Lower is better. A MAE of 0.2 kW means predictions are, on average, 0.2 kW off from reality.
</details>

---

**Q3**: Why must we split time-series data chronologically instead of randomly?

<details>
<summary>Answer</summary>
Random shuffling lets the model "peek" at future data during training. It would look great in testing but fail in the real world where the future is unknown.
</details>

---

**Q4**: The Random Forest feature importance shows `hour_sin` is most important. What does that tell us?

<details>
<summary>Answer</summary>
Time of day is the strongest predictor of electricity load. People's daily routines (waking up, cooking dinner) drive demand more than temperature or day of week.
</details>

---

**Q5**: If you could add one new feature to improve the forecast, what would it be and why?

<details>
<summary>Answer</summary>
Open-ended! Good ideas: a holiday calendar, school vacation periods, a lag feature (load from 1 hour ago), or weather forecast features (cloud cover, wind speed).
</details>

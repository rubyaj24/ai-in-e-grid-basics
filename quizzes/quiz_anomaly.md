# Quiz: Anomaly Detection

Cover the answers, think, then check.

---

**Q1**: What makes anomaly detection in the grid an "unsupervised" problem?

<details>
<summary>Answer</summary>
We rarely have labeled data saying "this reading was a theft" or "this was a fault." We have to detect unusual patterns without knowing what they look like ahead of time.
</details>

---

**Q2**: What is the trade-off between recall and precision?

<details>
<summary>Answer</summary>
High recall means catching most anomalies but also having more false alarms (low precision). High precision means flagged points are usually real but you might miss some (low recall).
</details>

---

**Q3**: If a utility company can't afford to miss any faults (e.g., a transmission line fault), which metric matters most?

<details>
<summary>Answer</summary>
Recall — they need to catch every fault, even if it means investigating some false alarms. The cost of a missed fault (blackout, equipment damage) far exceeds the cost of a false alarm.
</details>

---

**Q4**: Why might a rolling z-score struggle to detect an anomaly that lasts several hours?

<details>
<summary>Answer</summary>
The rolling window gradually "adjusts" to the anomaly. If load drops for 4 hours, the rolling mean drops too, and the z-score no longer sees it as unusual. This is called "anomaly masking."
</details>

---

**Q5**: Isolation Forest was trained on features [load_kw, hour, dayofweek, temperature_c]. If you removed "hour," would detection get better or worse? Why?

<details>
<summary>Answer</summary>
Worse — hour helps distinguish between a normal evening peak and an anomalous spike. Without it, the model might flag normal high-load hours as anomalies.
</details>

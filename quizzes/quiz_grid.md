# Quiz: Grid Concepts

Cover the answers, think, then check.

---

**Q1**: What is the key difference between the "old grid" and the "smart grid"?

<details>
<summary>Answer</summary>
The old grid was one-directional (power plant → home) with predictable generation. The smart grid has bidirectional flow (homes with solar send power back), intermittent renewables, batteries, and massive amounts of data from smart meters.
</details>

---

**Q2**: What does a power flow calculation tell us?

<details>
<summary>Answer</summary>
Whether the voltages and currents in the network obey the laws of physics — i.e., whether the grid can safely handle the current operating conditions without overloading lines or violating voltage limits.
</details>

---

**Q3**: Why is rule-based battery dispatch "dumb" even though it works?

<details>
<summary>Answer</summary>
It follows fixed rules that don't adapt. It can't look ahead at tomorrow's weather, respond to real-time electricity prices, or coordinate with other batteries in the neighborhood.
</details>

---

**Q4**: The three AI tasks we cover are Predict, Detect, and Optimize. Give a grid example of each.

<details>
<summary>Answer</summary>
- Predict: Forecasting tomorrow's peak load
- Detect: Finding a meter that's been tampered with
- Optimize: Deciding when to charge/discharge a battery to minimize cost
</details>

---

**Q5**: Why is synthetic data used in this project instead of real smart meter data?

<details>
<summary>Answer</summary>
Real smart meter data is privacy-sensitive — it reveals when people are home, when they sleep, their daily routines. Synthetic data lets us learn the same concepts without privacy concerns, and works fully offline.
</details>

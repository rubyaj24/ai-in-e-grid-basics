# 04 — Anomaly Detection: finding the needle in the haystack

> **The AI task**: Detect
> **The grid problem**: Is that meter broken, or is someone stealing power?
> **The demo**: `demos/02_anomaly_detection.py`

## The story

Imagine you are a security guard watching 10,000 security cameras.
Most of the time, everything is normal — people walking, cars driving.
But once in a while, something unusual happens: someone climbs a fence,
a door opens at 3 AM, a package is left in the corner.

You cannot watch all 10,000 screens at once. You need an automated
system that says "hey, look at this one."

That is anomaly detection.

## The grid problem

Grid operators have millions of meters reporting every 15 minutes.
Most readings are normal. But some are not:

- **Theft / meter bypass**: A reading suddenly drops to near-zero
  because someone tampered with the meter.
- **Fault / equipment failure**: A reading spikes because a
  transformer is failing or a line is damaged.
- **Data error**: The meter itself is broken and sending garbage.

The challenge: we usually do not have labeled examples of "this is
what theft looks like." We have to detect anomalies **without
knowing what they look like** — this is called unsupervised learning.

## How the demo works

### Step 1: We inject fake anomalies

Since real anomaly data is hard to come by, we create our own:
- 6 events where load drops to 10% of normal (simulating theft)
- 6 events where load spikes to 350% of normal (simulating a fault)

Now we know exactly where the anomalies are, so we can check whether
our detection methods find them.

### Step 2: Try a statistical baseline (rolling z-score)

The z-score measures how many standard deviations a point is from the
recent average. If a reading is more than 3 standard deviations away
from the average of the last week, we flag it.

This is simple and fast. But it struggles when:
- An anomaly lasts for hours (it starts to look "normal" as the window
  adjusts)
- The data has natural variation (solar panels ramp down at sunset —
  that is not an anomaly, but the z-score might flag it)

### Step 3: Try an ML approach (Isolation Forest)

Isolation Forest works on a clever idea: anomalies are "few and
different." It randomly splits the data and measures how many
splits it takes to isolate each point. Anomalies are isolated
quickly (they are unusual), normal points take many splits
(they are similar to many others).

### Step 4: Compare precision and recall

We use two metrics:

**Recall**: Of all the actual anomalies, what fraction did we catch?
- High recall = we catch most bad things
- But we might also flag a lot of normal points as "anomalies"

**Precision**: Of all the things we flagged, what fraction were
actually anomalous?
- High precision = when we flag something, it is usually real
- But we might miss a lot of anomalies

There is always a trade-off. If you flag everything, you have perfect
recall but terrible precision. If you flag nothing, you have perfect
precision but zero recall.

## Why this matters for the grid

A utility company cares about both:
- Missing a fault (low recall) could cause a blackout
- False alarms (low precision) waste workers' time investigating
  things that are nothing

The right balance depends on the cost of each type of mistake.
This is not a technical decision — it is a business decision.

---

**Your turn**: In `demos/02_anomaly_detection.py`, find where
`contamination=0.02` is set. Change it to `0.01` (fewer expected
anomalies) and then `0.05` (more). How do recall and precision
change?

**Check yourself**:
- Why is unsupervised anomaly detection harder than supervised
  classification?
- If you set the z-score threshold to 2 instead of 3, what happens
  to recall and precision?
- What is the real-world cost of a false alarm for a utility company?

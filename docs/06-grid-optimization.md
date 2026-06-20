# 06 — Grid Optimization: where things get interesting

> **The AI task**: Optimize
> **The grid problem**: When should we charge and discharge the battery?
> **The demo**: `demos/04_grid_optimization.py`

## The story

You have a solar panel on your roof and a battery in your garage.
During the day, your solar panel produces more power than you need.
Do you:
- Sell the extra power back to the grid (make money now)?
- Store it in your battery (use it tonight when rates are high)?
- Both — some now, some later?

Now multiply this by 10,000 homes, and add a utility company that also
has a giant battery, a wind farm, and a contract to buy power from a
neighboring city. Deciding when to charge and discharge everything is
a **complex optimization problem**.

This demo shows you the tip of that iceberg.

## What the demo builds

We use a Python library called **pandapower** to simulate a tiny
electricity network:

```
Substation ── Bus 1 ── Bus 2 (Solar)
                  ├── Bus 3 (Battery)
                  └── Bus 4 (Homes)
```

Five nodes (called "buses" in power system terminology), connected
by power lines. One neighborhood with solar panels, one battery, and
one connection to the main grid.

## Power flow: the physics check

First, we run a **power flow** calculation. This checks whether the
voltages and currents in our network obey the laws of physics. If a
line is overloaded or a voltage is too high, the network is not safe
to operate.

You will see output like:

```
Bus voltages (per-unit):
Substation     1.000
Bus 1          0.995
Bus 2 (Solar)  0.993
...
```

This tells us the grid is operating within acceptable limits (voltages
between 0.95 and 1.05 per unit). If not, we would need to reconfigure
or upgrade the network.

## Rule-based battery dispatch

Next, we simulate a full day. The sun rises, solar production peaks
at noon, the sun sets, and evening demand peaks at 7 PM.

Our battery follows two simple rules:

1. **If solar production exceeds demand AND battery is not full**:
   charge the battery
2. **If it is after 5 PM AND battery has charge left**:
   discharge the battery to reduce grid imports

This is called **rule-based dispatch**. It is simple, predictable,
and easy to explain. But it is also dumb — it does not adapt.

## Where AI comes in

A learned policy (using reinforcement learning or optimization) could:

- **Look ahead**: "Tomorrow will be cloudy, so I should save today's
  solar for tomorrow"
- **Respond to prices**: "Grid power is cheap at 2 AM, I should buy
  then instead of using my battery"
- **Coordinate**: "Ten other batteries in my neighborhood are
  discharging right now. I will wait."

This is an active area of research and a field where AI can have a
huge real-world impact.

## Why this is a "teaser"

This demo is intentionally not hands-on. pandapower has a learning
curve, and power flow physics takes time to understand. The goal is
to show you where the field goes after forecasting and detection.

If this excites you, the "Next steps" doc has resources for going
deeper.

---

**Your turn**: In `demos/04_grid_optimization.py`, find the line where
`discharge_hour = 17`. Change it to 21. How does the evening load
curve change? What happens if you set it to 12?

**Check yourself**:
- What information does a power flow calculation give you?
- Why is rule-based dispatch "dumb" even though it works?
- If you could add one more feature to the battery controller, what
  would it be?

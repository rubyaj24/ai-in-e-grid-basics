# 01 — What is a smart grid (and why does it need AI)?

Imagine you are baking bread for a neighborhood. You have been doing it
long enough to know that most people buy bread around 8 AM (breakfast)
and again around 6 PM (dinner). You bake extra on weekends. You know
that when it gets really hot, fewer people want the oven on at home,
so they buy more bread.

Now imagine you are asked to bake for a city of a million people — and
you cannot store bread longer than a few hours. If you bake too much,
you waste it. If you bake too little, people get angry. And you have
to make these decisions *every few seconds*.

That is basically the job of a power grid operator.

## The old grid vs the smart grid

The **old grid** was simple: big power plants sent electricity one way
to homes. Operators guessed how much power people would need tomorrow
based on past patterns and the weather forecast. They had no choice but
to over-provision — keep extra power plants idling just in case.

The **smart grid** is different because:

1. **Solar and wind** — power generation is no longer predictable.
   The sun does not always shine when people need electricity.

2. **Batteries** — we can store energy now, but deciding *when* to
   charge and *when* to discharge is a hard problem.

3. **Data** — smart meters report power usage every 15 minutes.
   That is 35,000+ readings per meter per year. A city with a million
   smart meters creates *35 billion data points a year*.

4. **Two-way flow** — homes with solar panels send power *back* to
   the grid. The grid needs to handle flow in both directions.

## Where AI comes in

All that data is useless unless we can make sense of it. Human operators
cannot look at 35 billion data points. So we teach computers to do three
things — which happen to be the three demos in this project:

| AI Task | Grid problem | What we build |
|---|---|---|
| **Predict** | How much power will we need tomorrow? | A model that forecasts load based on time and weather |
| **Detect** | Is that meter broken — or is someone stealing power? | A model that flags unusual readings |
| **Optimize** | When should we charge and discharge the battery? | A simulation that shows the difference between rules and learned policies |

## Three tasks, one framework

Every AI application in the power grid — whether it is a research paper
or a product used by a utility company — is almost always doing one of
these three things:

1. **Predict** something (load, solar generation, electricity price)
2. **Detect** something (faults, theft, equipment failure)
3. **Optimize** something (dispatch, storage scheduling, demand response)

Keep this framework in mind as you go through the demos. If someone asks
you "what does AI do in the grid?" you can answer: predict, detect, or
optimize.

---

**Your turn**: Look around your home. Can you find three things that
produce data a smart grid might care about? (Hint: your thermostat,
your water heater, your EV charger...)

**Check yourself**: Before moving on, make sure you can answer:
- What makes the "smart grid" different from the old grid?
- What are the three AI tasks for the grid?

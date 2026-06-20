# 02 — Understanding your data

Before we can do any AI, we need data. In our case, that means smart
meter readings — measurements of how much electricity a home (or a
small neighborhood) is using every 15 minutes.

## What the data looks like

Open `data/smart_meter_data.csv` in any text editor or spreadsheet
program. You will see columns like this:

| timestamp | hour | dayofweek | is_weekend | temperature_c | load_kw |
|---|---|---|---|---|---|

Each row is one reading. We have 60 days of data at 15-minute intervals,
which gives us 60 × 24 × 4 = **5,760 rows**.

## What each column means

- **timestamp**: When the reading was taken (e.g., `2026-01-01 00:00:00`)
- **hour**: The time as a decimal number (0.0 = midnight, 23.75 = 11:45 PM)
- **dayofweek**: 0 = Monday, 6 = Sunday
- **is_weekend**: 1 if Saturday or Sunday, 0 otherwise
- **temperature_c**: Outdoor temperature at that time in Celsius
- **load_kw**: How much electricity was being used, in kilowatts

## How the data was made (spoiler: it is fake)

We generated this data ourselves, because we wanted you to be able to
run everything offline without hunting for a real dataset. But we made
it *realistic*:

- There is a **morning peak** around 7:30 AM (people wake up, make coffee)
- There is a **evening peak** around 7:30 PM (dinner, TV, lights)
- **Weekends** have flatter, slightly lower usage
- **Temperature affects load** — hot days mean AC, cold days mean heating
- **Random daily variation** — because no two days are exactly the same

That last point is important. If every day were identical, we would not
need AI — we could just use yesterday's numbers. The randomness is what
makes the problem interesting (and realistic).

## Why synthetic data is fine for learning

Real smart meter data is hard to share for privacy reasons — it tells
you when people are home, when they sleep, when they go on vacation.
Synthetic data lets us learn the same concepts without anyone's privacy
being at risk.

If you later want to try real data, the UCI "Individual household
electric power consumption" dataset or Kaggle's smart meter datasets
work as drop-in replacements. You will just need to adjust some
column names.

## One important rule about time-series data

Here is something that trips up even experienced data scientists:

**Never shuffle time-series data before splitting into training and test sets.**

Why? Because if you shuffle, the model gets to "peek" at the future during
training. It looks like it is performing amazingly — until you use it in
the real world, where it cannot see tomorrow's data.

In all our demos, we train on the first 80% of the timeline and test on
the last 20%. That way, the model never sees the future.

---

**Your turn**: Open `src/egrid_learning/data/generator.py` and change
the morning peak hour from 7.5 to 9.5. Re-run the generator and see
how the data changes. Does the forecasting model still work well?

**Check yourself**:
- Why do we use synthetic data instead of real meter data?
- What happens if you shuffle a time-series dataset before training?

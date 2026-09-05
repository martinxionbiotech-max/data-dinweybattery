---
description: Battery selection for diesel generators — how generator starting batteries differ from vehicle batteries and the standby sulfation problem.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: What battery does a diesel generator use?
    a: Diesel generators use a starting battery matched to the engine's cranking requirement, often a heavy-duty flooded or AGM battery. Larger generators may use 24V starting systems.
  - q: How is a generator battery different from a vehicle battery?
    a: The chemistry is identical; the duty is not. A vehicle battery is recharged daily by the alternator, while a generator battery sits idle and self-discharges 3–5% a month — 9–15% of a 135 Ah battery in three idle months — yet must still deliver 850–1100+ CCA on demand. That is why a float charger, not the alternator, keeps it alive.
  - q: How often should I replace a generator battery?
    a: Generator batteries typically last 3–5 years, but standby units that sit idle need regular charging to avoid sulfation. Test annually and replace proactively.
  - q: Why do standby generator batteries fail?
    a: Sulfation, not use. A battery that sits at 70% charge for months self-discharges 3–5% a month and progressively sulfates, losing capacity invisibly until the one cold night it must crank. A float charger or maintainer prevents it.
  - q: What group size do generators use?
    a: It depends on the generator size. Large industrial generators often use heavy-duty batteries (JIS N150/N200 or equivalent), but always match the manufacturer's specification.
---

# Batteries for Diesel Generators

**TL;DR** — A diesel generator battery must deliver 850–1100+ CCA on demand after sitting idle
for months, and a battery with no load still self-discharges ~3–5% a month — a 135 Ah N150
sheds 9–15% in three idle months. A float charger, not the CCA label, is what keeps a standby
unit able to start.

## Key Takeaways

1. **Standby sulfation is the real killer, not usage** — a battery that sits at 70% charge for months starts the generator fine on a mild day, then fails on the cold night when the oil is thick and every amp matters.
2. **The float charger is not optional equipment** — a battery left off the charger self-discharges 3–5% a month (9–15% of a 135 Ah N150 in three idle months), so it is the difference between a generator that starts and one that does not.
3. **Replace at 3–5 years and load-test annually** — confirm the battery still delivers its rated CCA; test once a year regardless of how few times the generator actually ran.
4. **Large diesels still need 850–1100+ CCA** — and industrial installations often run 24V (two 12V in series), where the matched-pair rule applies on replacement.
5. **The least-used component is the most likely to fail** — a generator that starts 12 times a year still relies on a battery that must deliver 850–1100+ CCA on the one emergency day it is actually needed, after months at 70% charge or less.

## Generator vs Vehicle Duty

Generator batteries face a different challenge than vehicle batteries:

| Factor | Vehicle | Generator (standby) |
|---|---|---|
| Usage pattern | Frequent use | Long idle, occasional starts |
| Main risk | Vibration, cycling | Sulfation from sitting discharged |
| Charging | Alternator while driving | Maintainer / float charger |

The irony of standby power is that the component most likely to fail is the one that gets used
least. A generator engine that starts a dozen times a year still relies on a battery that must
deliver full cranking current on the one day it is actually needed — often in an emergency.

## Selection Criteria

1. **CCA** — match the generator engine's cranking requirement (large diesels need 850–1100+
   CCA)
2. **Group size** — match the generator's battery tray (heavy-duty JIS N150/N200 or
   equivalent)
3. **Technology** — flooded for standard duty; AGM for reliability in demanding environments
4. **Charging** — pair with a float charger or maintainer for standby units

## The Standby Sulfation Problem

A battery left partially discharged sulfates — lead sulfate crystals harden on the plates,
permanently reducing capacity. Standby generators are especially vulnerable because they sit
idle. The fix is a float charger that keeps the battery at full charge.

Even with no load, a battery self-discharges at roughly 3–5% per month at room temperature. On
a 135 Ah N150 that is 4–7 Ah lost every month — after three idle months the battery has shed
12–20 Ah, or roughly 9–15% of its capacity, before the generator has cranked once. A float
charger erases this loss by holding the battery at full charge; without one, self-discharge is
quietly eating the margin you will need on the one cold night the generator is actually called
on.

Sulfation is progressive and largely invisible until it is too late. A standby battery that
sits at 70% charge for months will start the generator fine on a mild day, then fail on the
cold night when the engine oil is thick and every amp matters. This is why the float charger is
not optional equipment for a standby unit — it is the difference between a generator that
starts and one that does not.

## Maintenance for Generator Batteries

- **Keep on a maintainer** — prevents sulfation during idle periods
- **Test annually** — load-test to confirm the battery still delivers rated CCA
- **Clean terminals** — corrosion adds resistance at the worst time
- **Replace proactively** — at 3–5 years or when load-test fails

Temperature also drives aging. The long-standing rule of thumb is that battery life roughly
halves for every 10 °C rise in sustained operating temperature: a generator battery in a hot
machine room at a sustained 35 °C ages at about twice the rate of one held at 25 °C. That is
why the "3–5 years" window is an estimate, not a guarantee — for standby units in warm
climates, err toward the short end of it.

The cost of a short life needs no price tag to see. A battery lasting 3 years instead of 5
costs 67% more per year of use (1/3 ÷ 1/5 ≈ 1.67), whatever it cost up front. That is why
skipping a float charger — to "save" — is the most expensive economy in a standby room.

Float voltage precision matters more than the CCA label. An AGM floats at 13.5–13.8 V and a
flooded battery at 13.2–13.5 V; a charger that holds above ~14.4 V dries out an AGM (water loss
→ thermal runaway), and one that holds below ~13.2 V under-charges and sulfates the plates. A
standby battery spends 90%+ of its life on float, so the charger's accuracy — not the battery's
CCA — determines whether it survives to year 5.

## 24V and Larger Installations

Large industrial generators often use 24V starting systems for the same reason heavy trucks do:
halving the current for the same power. If the generator uses two 12V batteries in series, the
matched-pair rule applies — replace both together, same model and age. See
[12V vs 24V systems](../12v-vs-24v/index.md) and
[24V wiring guide](../24v-wiring-guide/index.md).

## References

1. [SAE J537 (cold cranking amp test standard)](https://www.sae.org/standards/content/j537_201711/)
2. [SAE International — diesel engine systems](https://www.sae.org/)

## Related

- [What is CCA](../what-is-cca/index.md)
- [How to maintain a truck battery](../how-to-maintain-truck-battery/index.md)
- [Starting vs deep cycle](../starting-vs-deep-cycle/index.md)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/24v/) (24V battery systems) or [contact us](https://dinweysbattery.com/contact/) for a quote.

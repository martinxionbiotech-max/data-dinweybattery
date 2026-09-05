---
description: What is reserve capacity (RC) in a truck battery — the minutes it delivers 25A at 27°C, and how RC differs from CCA and Ah.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: What is reserve capacity in a battery?
    a: Reserve capacity (RC) is the number of minutes a battery can deliver 25 amps at 27°C before dropping below 10.5V. It measures emergency runtime without the alternator.
  - q: What is a good reserve capacity for a truck battery?
    a: Heavy-duty truck batteries typically range from roughly 130 to 320 minutes RC. The right figure depends on your electrical load — telematics, refrigeration and accessories push you toward the higher end.
  - q: Is reserve capacity the same as amp-hours?
    a: No. RC is minutes at a fixed 25A load; amp-hours (Ah) is total energy at a specified discharge rate. They are related but measured differently.
  - q: Is CCA or reserve capacity more important for trucks?
    a: CCA matters most for cold-climate starting; RC (minutes at 25 A, e.g. 220 vs 320 min) matters most for runtime if the alternator fails or accessory loads are heavy. Both should be specified for demanding fleets.
  - q: How is reserve capacity tested?
    a: The battery is fully charged, discharged at a constant 25A at 27°C (80°F), and the time until voltage drops below 10.5V is recorded in minutes.
---

# What Is Reserve Capacity (RC)?

**TL;DR** — Reserve capacity (RC) is the number of minutes a battery can deliver 25 amps at
27°C before dropping below 10.5V. It measures emergency runtime without the alternator — a
different thing from CCA (cold-start power) or Ah (total energy). Heavy-duty truck batteries
typically range from ~130 to 320 minutes RC.

## Key Takeaways

1. **RC is measured in minutes, not amps** — the test is a steady 25A draw at 27°C until voltage drops below 10.5V, so it answers endurance, not starting power.
2. **The truck RC span is 130–320 minutes** — heavy-duty batteries range from roughly 130 to 320 minutes, and the right figure depends entirely on your electrical load.
3. **RC, CCA and Ah do not predict each other** — the 190H52 carries 320 minutes RC while the 58827 carries just 150, and neither figure tells you the other's CCA; specify the metric that matches your dominant risk.
4. **RC often outranks CCA in developing markets** — older vehicles suffer more electrical faults, so a roadside alternator failure favors a 220–320 minute JIS battery over a high-CCA one.
5. **A fleet must decide its fear** — a cold no-start points to CCA, but a roadside alternator failure while running refrigeration points to RC, where a 320-minute 190H52 buys far more buffer than a 150-minute 58827.

## What RC Measures

RC answers one question: **if the alternator fails, how long can the battery keep critical
systems running?**

The standard test:

1. Fully charge the battery
2. Discharge at a constant 25 amps at 27°C (80°F)
3. Measure the time until voltage drops below 10.5V

The result is expressed in minutes.

## RC vs CCA vs Ah

| Rating | Measures | Unit | When it matters |
|---|---|---|---|
| CCA | Cold-start power | Amps | Cold climates, engine cranking |
| RC | Emergency runtime at 25A | Minutes | Alternator failure, accessory loads |
| Ah (C20) | Total energy storage | Amp-hours | Heavy accessory/electronics loads |

These three ratings measure different things. A battery can have high CCA but modest RC, or
vice versa — do not assume one predicts the others.

### Why Three Separate Ratings Exist

Each rating answers a different real-world question, and they are measured under different
conditions. CCA tests a short, cold, high-current burst. RC tests a steady, warm, moderate draw.
Ah tests total energy at a slow discharge. A battery optimized for one is not automatically
optimized for the others — which is why a complete datasheet lists all three and why you should
specify the one that matches your dominant risk. For the CCA side see [what is CCA](../what-is-cca/index.md).

## Typical RC for Heavy-Duty Batteries

| DINWEY model | Standard | RC |
|---|---|---|
| 145G51 (N150) | JIS | 220 min |
| 190H52 (N200) | JIS | 320 min |
| 58827 (DIN88) | DIN/EN | 150 min |
| 60038 (DIN100) | DIN/EN | 170 min |

### Converting RC to Amp-Hours

RC is quoted in minutes, but the energy behind it is one multiplication away. During the test
the battery holds a constant 25 amps, and energy is current × time, so the ampere-hours
delivered before the battery drops below 10.5V is simply 25 A × (minutes ÷ 60). Applied to the
table above:

| Model | RC | Ah delivered (25 A × min ÷ 60) |
|---|---|---|
| 145G51 | 220 min | 25 × 220 ÷ 60 ≈ 92 Ah |
| 190H52 | 320 min | 25 × 320 ÷ 60 ≈ 133 Ah |
| 58827 | 150 min | 25 × 150 ÷ 60 ≈ 63 Ah |
| 60038 | 170 min | 25 × 170 ÷ 60 ≈ 71 Ah |

So the 320-minute 190H52 delivers roughly 133 Ah before hitting 10.5V — more than double the
≈63 Ah of the 150-minute 58827. One caveat: this is the energy actually delivered during the RC
test, not the nameplate C20 Ah rating. Because a 25A draw is far faster than the 20-hour rate,
the RC-derived figure reads lower than a full C20 Ah rating for the same battery — which is
exactly why RC and Ah stay separate specifications.

## Why RC Matters for Commercial Vehicles

Modern trucks carry more electrical load than ever — telematics, refrigeration, lighting,
sleeper-cab accessories. If the alternator fails or the engine idles for long periods, a
higher RC gives more buffer before the battery is drained to a damaging level.

For fleets operating in developing markets with older vehicles, RC is often the more critical
specification (per Chengguang Energy technical documentation), because electrical faults are
more common.

The practical implication: a fleet that mostly fears a cold no-start should prioritize CCA; a
fleet that mostly fears a roadside alternator failure while running refrigeration should
prioritize RC. Many heavy-duty fleets specify both. See
[CCA vs reserve capacity](../cca-vs-reserve-capacity/index.md) for the combined view.

## References

1. [About lead batteries — Battery Council International](https://batterycouncil.org/battery-facts-and-applications/about-lead-batteries/)
2. [Battery Council International — lead battery technology](https://batterycouncil.org/)

## Related

- [What is CCA](../what-is-cca/index.md)
- [Truck Battery Complete Guide](../complete-guide/index.md)
- [JIS N150 vs N200](../jis-n150-vs-n200/index.md)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/fleet/) (fleet battery programs) or [contact us](https://dinweysbattery.com/contact/) for a quote.

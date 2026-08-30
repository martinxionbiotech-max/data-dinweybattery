---
description: What is reserve capacity (RC) for a truck battery? How RC differs from CCA and Ah, typical RC ranges, and why it matters for commercial vehicles with heavy electrical loads.
type: article
date_published: 2026-08-30
date_modified: 2026-08-30
faq:
  - q: What does reserve capacity (RC) mean?
    a: Reserve capacity is the number of minutes a fully charged battery can deliver 25 amps at 27°C before dropping below 10.5V. It measures how long the battery can run electrical loads if the alternator fails.
  - q: What is a good reserve capacity for a truck battery?
    a: Heavy-duty truck batteries typically have RC values around 130–320 minutes. Larger models (like the JIS N200 at 320 min) provide more emergency runtime.
  - q: How is RC different from CCA?
    a: CCA measures short, high-current cold-start power; RC measures sustained lower-current runtime. They are different dimensions and are not interchangeable.
  - q: How is RC different from Ah?
    a: Ah measures total energy storage at a 20-hour discharge rate; RC measures runtime at a fixed 25-amp draw. Both relate to capacity but are measured differently.
  - q: Why does RC matter for trucks?
    a: Trucks increasingly carry electrical loads (telematics, refrigeration, lighting) that may run when the engine is off or the alternator fails. Higher RC provides more emergency runtime.
---

# What Is Reserve Capacity (RC) for a Truck Battery?

**TL;DR** — Reserve capacity (RC) is the number of minutes a battery can deliver 25 amps at
27°C before dropping below 10.5V. It measures emergency runtime without the alternator — a
different thing from CCA (cold-start power) or Ah (total energy). Heavy-duty truck batteries
typically range from ~130 to 320 minutes RC.

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

## Typical RC for Heavy-Duty Batteries

| DINWEY model | Standard | RC |
|---|---|---|
| 145G51 (N150) | JIS | 220 min |
| 190H52 (N200) | JIS | 320 min |
| 58827 (DIN88) | DIN/EN | 150 min |
| 60038 (DIN100) | DIN/EN | 170 min |

## Why RC Matters for Commercial Vehicles

Modern trucks carry more electrical load than ever — telematics, refrigeration, lighting,
sleeper-cab accessories. If the alternator fails or the engine idles for long periods, a
higher RC gives more buffer before the battery is drained to a damaging level.

For fleets operating in developing markets with older vehicles, RC is often the more critical
specification (per Chengguang Energy technical documentation), because electrical faults are
more common.

## Related

- [What is CCA](../what-is-cca/index.md)
- [Truck Battery Complete Guide](../complete-guide/index.md)
- [JIS N150 vs N200](../jis-n150-vs-n200/index.md)

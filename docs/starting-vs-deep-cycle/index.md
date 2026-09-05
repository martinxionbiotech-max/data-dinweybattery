---
description: Starting vs deep cycle batteries for trucks — why SLI batteries crank the engine and deep-cycle batteries run loads, and how to use both in the same vehicle.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: What is the difference between a starting and deep cycle battery?
    a: A starting (SLI) battery delivers a short, high-current burst to crank the engine. A deep cycle battery delivers lower current over a long time and tolerates deep discharge. They are built differently and are not interchangeable.
  - q: Can I use a deep cycle battery to start my truck?
    a: Not recommended. Deep cycle batteries are not built for the high current of engine cranking and will degrade rapidly under that load.
  - q: Can I run accessories off my starting battery?
    a: No. Repeated deep discharge will quickly ruin a starting battery's thin plates. Use a separate deep cycle or auxiliary bank for continuous loads.
  - q: What is a dual-purpose battery?
    a: A dual-purpose battery offers both starting power and some deep-cycle capability — a compromise for vehicles that need both but cannot fit two batteries. Separate batteries are better for demanding use.
  - q: How do I power a reefer or lift gate?
    a: Use a separate deep-cycle or AGM auxiliary bank isolated from the starting battery with a battery isolator or DC-DC charger.
---

# Starting vs Deep Cycle Battery for Trucks

**TL;DR** — Starting (SLI) batteries deliver a short, high-current burst to crank the engine;
deep cycle batteries deliver lower current over a long time and tolerate deep discharges. Use
a starting battery for the engine and a separate deep cycle or auxiliary bank for accessories.

## Key Takeaways

1. **Depth of discharge is the real dividing line** — starting batteries are built for shallow 10–20% discharges, deep-cycle for 50–80%; pulling a starter into deep discharge is what destroys its thin plates.
2. **200–300 vs hundreds-to-thousands cycles flips the value math** — a starting battery lasts 200–300 cycles, a deep-cycle hundreds to thousands; the higher price is a different failure mode, not a markup.
3. **A dual-purpose battery compromises both jobs** — thin plates crank at the cost of depth, thick plates cycle at the cost of cranking amps; a dual-purpose unit cannot match a dedicated bank's full 50–80% cycling depth.
4. **Starting on a deep-cycle battery wears it out fast** — deep-cycle plates are not built for cranking current, so even a 50–80%-tolerant bank degrades quickly under starter load.
5. **Run auxiliaries off a separate bank or ruin the starter** — refrigeration, telematics and lift gates must sit behind an isolator or DC-DC charger; deep-cycling the starter cuts its 200–300 cycle life short.

## The Two Battery Jobs

| Characteristic | Starting (SLI) | Deep cycle |
|---|---|---|
| Discharge style | Short, high current | Long, low current |
| Depth of discharge | Shallow (10–20%) | Deep (50–80%) |
| Plate design | Thin, many plates | Thick, fewer plates |
| Cycle life | 200–300 cycles | Hundreds to thousands |
| Primary job | Crank the engine | Run loads, tolerate cycling |

## Why the Plate Design Differs

The difference is physical, not a marketing label. A starting battery has many thin plates,
which maximizes the surface area exposed to electrolyte — that is what delivers the enormous
short-duration current burst of cranking. A deep-cycle battery has fewer, thicker plates, which
sacrifices some peak current in exchange for surviving repeated deep discharge without shedding
active material. Asking one battery to do both jobs means compromising on both.

## Why You Should Not Mix Them Up

- **Using a deep cycle to start** — deep cycle batteries are not built for the high current of
  engine cranking and will degrade rapidly under that load.
- **Using a starting battery for deep loads** — repeated deep discharges will quickly ruin a
  starting battery's thin plates.

Depth of discharge and cycle life trade off roughly inversely — and the article's own numbers make the trade exact. A starting battery that earns its **300-cycle** ceiling at a **20%** depth of discharge carries a lifetime throughput of roughly **300 × 0.20 = 60** "full-cycle-equivalents" (cycles × depth). Drag that same battery to an **80%** depth and the same 60 units divide by 0.80 to give only **60 ÷ 0.80 = 75 cycles** — a 4× deeper discharge (80% ÷ 20% = 4×) buying a 4× shorter life (300 ÷ 75 = 4×). That is the arithmetic behind the warning that deep-cycling a starter "quickly ruins" it: the 80% depth a deep-cycle bank is built to survive for hundreds of cycles would exhaust a starter's entire lifetime throughput in roughly 75 discharges. Deep-cycle batteries don't break this rule — they engineer a far larger throughput constant by using thick plates instead of thin ones.

## Powering Auxiliary Equipment

Trucks increasingly carry heavy auxiliary loads — refrigeration, telematics, sleeper-cab power,
lift gates. The correct approach is:

1. Keep the **starting battery** dedicated to engine cranking
2. Add a **separate deep cycle or auxiliary bank** for auxiliary loads
3. Isolate them with a battery isolator or DC-DC charger

For a concrete example of this split, see
[cold-chain & refrigerated transport](../cold-chain-refrigerated/index.md).

## What About Dual-Purpose Batteries?

A dual-purpose battery provides both starting power and some deep-cycle capability. It is a
compromise for vehicles that need both but cannot fit two separate batteries. For demanding
applications, separate batteries are the better solution.

## References

1. [Battery Council International — deep-cycle batteries](https://batterycouncil.org/)
2. [About lead batteries — Battery Council International](https://batterycouncil.org/battery-facts-and-applications/about-lead-batteries/)

## Related

- [Truck Battery Complete Guide](../complete-guide/index.md)
- [What is reserve capacity](../what-is-reserve-capacity/index.md)
- [AGM vs flooded](../agm-vs-flooded/index.md)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/jis-heavy-duty/) (starting batteries) or [contact us](https://dinweysbattery.com/contact/) for a quote.

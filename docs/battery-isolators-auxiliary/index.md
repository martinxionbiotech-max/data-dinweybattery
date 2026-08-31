---
description: Battery isolators and DC-DC chargers for trucks — how to run an auxiliary battery bank for sleeper-cab, reefer and lift-gate loads without draining the starting batteries.
type: article
date_published: 2026-08-31
date_modified: 2026-08-31
faq:
  - q: What does a battery isolator do?
    a: A battery isolator separates the starting battery from an auxiliary battery bank so auxiliary loads (sleeper cab, reefer, lift gate) cannot drain the starting battery. When the engine runs, the alternator charges both; when it stops, the two banks are isolated.
  - q: What is the difference between an isolator and a DC-DC charger?
    a: An isolator simply blocks current from flowing back to the starting battery when the engine is off. A DC-DC charger does that and also provides a proper multi-stage charge to the auxiliary bank, which deep-cycle and AGM batteries need to stay healthy.
  - q: Do I need an auxiliary battery in a truck?
    a: Only if you run loads with the engine off — sleeper-cab HVAC, refrigeration, inverters or lift gates. If everything runs while driving, the starting battery and alternator are usually enough.
  - q: Can I charge two batteries with one alternator?
    a: Yes — through an isolator or DC-DC charger the alternator charges both banks while the engine runs, while keeping them electrically separate when it stops.
  - q: What battery should I use for the auxiliary bank?
    a: A deep-cycle or AGM battery, sized to the load's continuous draw and required runtime. A starting battery is the wrong tool for sustained hotel loads.
---

# Battery Isolators & Auxiliary Systems for Trucks

**TL;DR** — A battery isolator (or DC-DC charger) lets a truck run a separate auxiliary
battery bank for sleeper-cab, reefer and lift-gate loads, while protecting the starting
battery from being drained. Use a deep-cycle or AGM auxiliary battery sized to the load.

## Why a Second Battery System Exists

A modern truck carries two very different electrical jobs:

| Job | What it needs | Right battery |
|---|---|---|
| Start the engine | Short, high-current burst | Starting (SLI) battery |
| Run hotel loads | Long, steady draw | Deep-cycle / AGM auxiliary bank |

The problem is that these two jobs need opposite battery designs. A starting battery has thin
plates built for a big current burst; a deep-cycle battery has thick plates built to survive
repeated discharge. Running a reefer or sleeper-cab HVAC off the starting battery deep-discharges
it, permanently damaging the plates — and leaves you stranded in the morning.

## What an Isolator Does

A battery isolator sits between the two banks. While the engine runs, it lets the alternator
charge both. When the engine stops, it blocks current from flowing back from the auxiliary bank
to the starting battery — so a night of hotel loads cannot touch the starting battery.

The isolator is the minimum-viable separation. It is cheap, simple and solves the core problem:
protecting the start.

## Isolator vs DC-DC Charger

| Feature | Isolator | DC-DC charger |
|---|---|---|
| Protects starting battery | Yes | Yes |
| Multi-stage charging | No | Yes |
| Suits flooded auxiliary | Yes | Yes |
| Suits AGM / deep-cycle | Marginal | Yes (proper profile) |
| Cost | Lower | Higher |

A basic isolator simply connects and disconnects the two banks. A DC-DC charger does that *and*
applies a proper bulk-absorption-float charge profile to the auxiliary bank. For an AGM or
deep-cycle auxiliary battery that will be cycled hard, the DC-DC charger is the better
investment — it keeps the auxiliary bank healthy over hundreds of cycles.

## Sizing the Auxiliary Bank

The auxiliary bank must be sized to two numbers:

- **Continuous draw** of the load (amps) — from the reefer or inverter specification
- **Required runtime** — how long the load runs between charges

Multiply the two and add margin. For example, a 25 A reefer running 8 hours needs roughly
200 Ah of usable capacity — and since lead-acid should not be discharged below ~50% for
service life, that means a bank of roughly 400 Ah or more. For runtime planning see
[what is reserve capacity](../what-is-reserve-capacity/index.md).

## Where This Pattern Applies

- **Sleeper-cab hotel loads** — HVAC, fridge, inverter, lighting on long-haul trucks
- **Refrigerated trailers** — see [cold-chain & refrigerated](../cold-chain-refrigerated/index.md)
- **Lift gates and hydraulic equipment** — on delivery trucks
- **Semi-trailers and heavy haulers** — see [semi-trailer](../semi-trailer/index.md)

## How It Connects to the Electrical System

The auxiliary bank is a second, parallel electrical system, not a replacement for the
starting side. It still lives in the same 12V (or 24V) architecture as the rest of the truck.
For the underlying system-voltage logic see [12V vs 24V](../12v-vs-24v/index.md), and for
wiring the two-battery configuration see [24V wiring guide](../24v-wiring-guide/index.md).

## References

1. [Battery Council International — deep-cycle batteries](https://batterycouncil.org/)
2. [Battery Council International — VRLA / AGM technology](https://batterycouncil.org/)

## Related

- [Starting vs deep cycle](../starting-vs-deep-cycle/index.md)
- [Cold-chain & refrigerated](../cold-chain-refrigerated/index.md)
- [12V vs 24V systems](../12v-vs-24v/index.md)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/fleet/) (fleet & auxiliary battery programs) or [contact us](https://dinweysbattery.com/contact/) for a quote.

---
description: Battery selection for cold-chain and refrigerated trucks — why reefers need a starting battery plus a separate deep-cycle auxiliary bank.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: What battery does a reefer truck need?
    a: A refrigerated truck needs two separate systems: a starting battery for the engine (850–1100+ CCA for a large diesel), and a deep-cycle or AGM auxiliary bank for the refrigeration unit.
  - q: Can I run the reefer off the starting battery?
    a: No. A 25 A refrigeration unit draws ~200 Ah over 8 hours and will deep-discharge a starting battery, damaging it and risking a no-start. Use a separate auxiliary bank.
  - q: What battery is best for the refrigeration unit?
    a: Deep-cycle batteries (or AGM) are best for the reefer's continuous draw — they tolerate repeated discharge to ~50% without the plate damage a starting battery suffers.
  - q: How do I keep the reefer from draining the starting battery?
    a: Use a battery isolator or DC-DC charger to separate the starting battery from the auxiliary bank, so the reefer cannot drain the starting battery. A plain isolator drops ~0.3–0.7 V; a DC-DC charger adds a proper charge profile.
  - q: How do I size the auxiliary bank for a reefer?
    a: Size it to the reefer's continuous current draw and required runtime. A 25 A unit over 8 hours needs ~200 Ah usable — ~400 Ah at the 50% depth-of-discharge limit. Confirm the unit's draw from its specification.
---

# Batteries for Cold-Chain & Refrigerated Transport

**TL;DR** — Refrigerated trucks need two things: a starting battery with adequate CCA (850–1100+
for large diesels) for the engine, and a separate deep-cycle auxiliary bank for the reefer. A
25 A reefer running 8 hours draws ~200 Ah — which needs ~400 Ah of bank at the 50% discharge
limit. Never run it off the start battery.

## Key Takeaways

1. **2 loads demand 2 battery types** — a starting (SLI) battery for the 850–1100+ CCA burst and a separate deep-cycle bank for the reefer's continuous draw; one battery cannot serve both jobs.
2. **Never run the reefer off the starting battery** — a 25 A unit draws ~200 Ah over 8 hours and deep-discharges the plates; the truck starts fine on the lot, then strands the driver mid-route after an overnight stop.
3. **A basic isolator only blocks reverse current, with a ~0.3–0.7 V drop** — a DC-DC charger also applies a proper multi-stage charge, which a cycled deep-cycle bank needs to stay healthy over many cycles.
4. **For a reefer that runs 8+ hours a night, the DC-DC charger is the better investment** — the isolator protects the start but does nothing for auxiliary-bank longevity, so the cheaper option is a false economy.
5. **Match the starting battery to your market group size (JIS N150/N200 or DIN88/DIN100)** — and consider AGM for the auxiliary bank, since it tolerates cycling better than flooded.

## Two Separate Loads

Cold-chain transport has two distinct electrical loads:

| Load | Requirement | Battery type |
|---|---|---|
| Engine starting | High CCA burst | Starting (SLI) battery |
| Refrigeration unit | Continuous power | Deep cycle / auxiliary bank |

## Why Separation Matters

The refrigeration unit draws power continuously — often with the engine off or at idle. A
starting battery is built for short, high-current bursts, not sustained deep discharge. Running
a reefer off the starting battery will:

- Deep-discharge it, damaging the plates
- Shorten its service life dramatically
- Risk a no-start when the truck needs to move

The failure mode is the worst kind: the truck starts fine on the lot, then strands the driver
mid-route because the reefer quietly drained the starting battery during an overnight stop.

## Recommended Configuration

1. **Starting battery** — dedicated to engine cranking, matched CCA to the engine and climate
2. **Auxiliary bank** — deep cycle batteries for the refrigeration unit
3. **Isolation** — a battery isolator or DC-DC charger prevents the reefer from draining the
   starting battery

Size the bank to the load, not the tray. A reefer unit drawing 25 A for 8 hours uses 200 Ah
(25 × 8); because a deep-cycle battery should not be discharged below ~50%, that means a bank
of ~400 Ah. Double-check the actual draw — a 40 A unit over 10 hours needs 400 Ah usable, or
~800 Ah at 50%.

### Isolator vs DC-DC Charger

A basic **battery isolator** simply blocks current from flowing back from the auxiliary bank to
the starting battery when the engine is off. A **DC-DC charger** does more: it provides a
proper multi-stage charge to the auxiliary bank, which matters for deep-cycle batteries that
need a controlled charge profile. For a reefer that runs for hours, a DC-DC charger is the
better investment because it keeps the auxiliary bank healthy over many cycles.

## Battery Selection Tips

- Match the starting battery's group size and CCA to the vehicle (JIS N150/N200, DIN88/DIN100)
- Size the auxiliary bank to the reefer unit's continuous draw and required runtime
- Consider AGM for the auxiliary bank — it tolerates cycling better than flooded

For how deep-cycle batteries differ from starting batteries, see
[starting vs deep cycle](../starting-vs-deep-cycle/index.md). For runtime planning, see
[what is reserve capacity](../what-is-reserve-capacity/index.md).

## References

1. [Battery Council International — deep-cycle batteries](https://batterycouncil.org/)
2. [Battery Council International — lead battery technology](https://batterycouncil.org/)

## Related

- [Starting vs deep cycle](../starting-vs-deep-cycle/index.md)
- [Fleet battery management](../fleet-battery-management/index.md)
- [What is reserve capacity](../what-is-reserve-capacity/index.md)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/fleet/) (fleet battery solutions) or [contact us](https://dinweysbattery.com/contact/) for a quote.

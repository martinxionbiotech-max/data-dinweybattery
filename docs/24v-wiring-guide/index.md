---
description: 24V truck battery wiring guide — wiring two 12V batteries in series for 24V, correct terminal connections, cable sizing and wiring mistakes to avoid.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: How do I wire two 12V batteries for 24V?
    a: Connect the positive terminal of battery 1 to the negative terminal of battery 2 with a jumper cable. The remaining positive terminal of battery 1 and negative terminal of battery 2 become the 24V output.
  - q: What happens if I wire batteries in parallel instead of series?
    a: Parallel wiring keeps the voltage at 12V but doubles capacity (Ah). You will not get 24V — use series for 24V systems.
  - q: What cable gauge do I need for 24V truck batteries?
    a: Cable sizing depends on starter current draw and cable length. A 24V system draws half the current of an equivalent 12V system, allowing thinner cables — but always size cables to the actual starter load.
  - q: Do I need matching batteries for a 24V pair?
    a: Yes. Use 2 identical batteries of the same model, rating, age and ideally the same batch, and replace both together.
  - q: Do 24V truck batteries need a special charger?
    a: Yes. Use a charger rated for 24V (or charge each 12V battery separately). A 12V charger will not properly charge a 24V series pair.
---

# 24V Truck Battery Wiring Guide

**TL;DR** — A 24V truck system is built from two 12V batteries in series: connect battery 1's
positive to battery 2's negative, then take 24V from the remaining positive and negative
terminals. Always use two identical batteries and replace them as a pair.

## Key Takeaways

1. **Series is one jumper away** — connect Battery 1 positive to Battery 2 negative, then take +24V and 0V from the two remaining terminals; the wiring is trivial, the discipline is not.
2. **Series raises voltage, parallel doubles Ah** — series holds amp-hours constant at 24V; parallel holds 12V while doubling capacity, and wiring one when you meant the other is the most common 24V mistake.
3. **24V halves current, enabling thinner wire** — but still size cables to actual starter draw and length; a long run on a large diesel can demand heavy gauge even at 24V.
4. **Use 2 identical batteries, replaced together** — same model, rating, age and batch; mixing flooded and AGM in one pair guarantees imbalance.
5. **A 12V charger cannot charge a 24V pair** — use a 24V-rated charger across +24V/0V, or disconnect and charge each 12V individually; otherwise one battery under-charges.

## Series Wiring Step by Step

```
       ┌─────────────────────────────────────┐
       │  Battery 1           Battery 2      │
       │  (+) ─── jumper ─── (−)             │
       │   │                    │            │
       │   └── +24V output      └── 0V output│
       └─────────────────────────────────────┘
```

1. Place the two 12V batteries side by side.
2. Connect a jumper cable from **Battery 1 positive (+)** to **Battery 2 negative (−)**.
3. The **remaining positive** (Battery 1) is your **+24V**.
4. The **remaining negative** (Battery 2) is your **0V / ground**.

## Series vs Parallel

| Configuration | Result | Use case |
|---|---|---|
| Series (+ to −) | 24V, same capacity | Heavy trucks, buses |
| Parallel (+ to +, − to −) | 12V, doubled capacity | Extended 12V runtime |

The distinction matters because the two configurations solve opposite problems. Series raises
voltage while holding amp-hours constant — that is what a 24V starter needs. Parallel holds
voltage at 12V while doubling amp-hours — that is what a long 12V hotel-load runtime needs.
Wiring one when you meant the other is the most common 24V mistake.

## Wiring Rules

1. **Use two identical batteries** — same model, rating, age and batch.
2. **Replace both together** — mismatched pairs charge unevenly.
3. **Size cables correctly** — to the actual starter current draw and cable length.
4. **Use proper terminals** — clean, tight connections prevent voltage drop and heat.
5. **Mark polarity clearly** — prevents costly reverse-connection mistakes.

## Cable Sizing: Why 24V Allows Thinner Wire

Power is voltage × current. A 24V system delivers the same cranking power as a 12V system at
half the current, which means lower voltage drop over a given cable and — in principle —
thinner, lighter wiring. This is one of the reasons heavy trucks moved to 24V in the first
place.

In practice, still size cables to the *actual* starter draw and total cable length: a long run
on a large diesel engine can demand a heavy gauge even at 24V. When in doubt, follow the
vehicle manufacturer's wiring diagram rather than guessing.

## Charging a 24V Pair

A 24V series pair needs a 24V charger. Two practical options:

- Use a charger rated for **24V nominal** output, connected across the +24V and 0V terminals.
- Or charge each **12V battery individually** by disconnecting the pair — slower, but safe and
  simple when a 24V charger is not available.

A 12V charger connected across the full pair will not charge it properly and can leave the two
batteries imbalanced. For charge voltages, rates and multi-battery practices, see the
[battery charging guide](../battery-charging-guide/index.md).

## Common Mistakes

- Wiring in parallel when 24V is needed (stays 12V)
- Replacing only one battery of the pair
- Mixing flooded and AGM batteries in the same pair
- Loose or corroded jumper connections
- Charging the whole pair with a 12V charger

## References

1. [SAE International — vehicle electrical systems](https://www.sae.org/)

## Related

- [12V vs 24V systems](../12v-vs-24v/index.md)
- [Battery isolators & auxiliary banks](../battery-isolators-auxiliary/index.md)
- [Truck Battery Complete Guide](../complete-guide/index.md)
- [DINWEY 24V systems](https://dinweysbattery.com/products/24v/)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/24v/) (24V battery systems) or [contact us](https://dinweysbattery.com/contact/) for a quote.

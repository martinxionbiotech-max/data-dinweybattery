---
description: JIS vs DIN battery engineering — why DIN packs more cold-cranking power per litre while JIS thick-plate batteries trade energy density for cycle life.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: Why do DIN batteries have higher CCA than JIS batteries of similar size?
    a: DIN batteries use a more compact cell layout, delivering more cold-cranking power per litre (60038: 870 A EN in a 393×175×190 mm case). JIS thick-plate batteries trade some energy density for deeper cycling and vibration tolerance.
  - q: What is CCA density?
    a: CCA density is the cold-cranking amps divided by the battery's physical volume (CCA per litre) — e.g. a DIN 60038 packs 870 A into ~13 L vs a JIS N150's 900 A into ~23.9 L. It shows how much starting power fits in a given space.
  - q: Is a JIS battery better or worse than a DIN battery?
    a: Neither is universally better — DIN suits compact European trays with cold winters, while JIS thick-plate suits the heavier cycling (to ~50% DoD), vibration and heat of Asian and African commercial duty.
  - q: Can I fit a DIN battery in place of a JIS battery?
    a: Only if the dimensions (e.g. DIN88 353×175×190 mm vs JIS N150 508×222×212 mm), terminal type and polarity all match. The two standards have different footprints and terminals, so they are not directly interchangeable.
  - q: Why does the same Ah rating not mean the same CCA?
    a: Ah measures energy storage while CCA measures cold-start power. A DIN battery typically delivers more CCA per Ah (870 A / 100 Ah ≈ 8.7 A/Ah) than a JIS battery of similar capacity (1100 A / 200 Ah ≈ 5.5 A/Ah), because of its different plate design.
---

# JIS vs DIN Battery Engineering: A Density Analysis

**TL;DR** — We calculated CCA density (cold-cranking amps per litre) and CCA-per-Ah for the
DINWEY heavy-duty range. The result: DIN batteries pack roughly **2× the cold-cranking power
per litre** of JIS thick-plate batteries, while JIS batteries trade energy density for deeper
cycling. It is not "better vs worse" — it is two engineering philosophies.

## Key Takeaways

1. **DIN packs ~2× the cold-start power per litre** — 66–68 CCA/L (DIN88/DIN100) versus 35–38 CCA/L (N150/N200), so a DIN battery cranks far harder for the same physical space.
2. **~60% more CCA per Ah is the hidden gap** — DIN's CCA/Ah runs 8.7–9.1 versus JIS's 5.5–6.7, so two 100Ah batteries of different standards will not crank equally.
3. **JIS trades energy density for durability** — JIS's 5.6–6.3 Ah/L versus DIN's 7.5–7.7 reflects thicker Pb-Sb plates built for deep cycling and vibration, not compactness.
4. **The N200 is the density outlier** — the 190H52's 31.8 L volume yields only 34.6 CCA/L, below the N150's 37.6 CCA/L, so in JIS the bigger battery is actually less CCA-dense.
5. **Same Ah does not mean same CCA** — cold-start power is set by plate design (6.67 vs 9.09 CCA/Ah for the 145G51 vs 58827), not by capacity rating, which is why cross-standard CCA comparisons fail.

## The Calculation

Using the published specifications of the four DINWEY heavy-duty models, we calculated three
density metrics:

| Model | Standard | Volume (L) | CCA density (CCA/L) | CCA per Ah | Ah per litre |
|---|---|---|---|---|---|
| 145G51 (N150) | JIS | 23.9 | 37.6 | 6.67 | 5.6 |
| 190H52 (N200) | JIS | 31.8 | 34.6 | 5.50 | 6.3 |
| 58827 (DIN88) | DIN/EN | 11.7 | 68.2 | 9.09 | 7.5 |
| 60038 (DIN100) | DIN/EN | 13.1 | 66.6 | 8.70 | 7.7 |

*Volume is calculated from published length × width × height. All figures derive from the same
manufacturer's datasheets, so the comparison is internally consistent.*

## What the Numbers Reveal

### 1. DIN packs ~2× the cold-start power per litre

DIN CCA density (66–68 CCA/L) is roughly double JIS (35–38 CCA/L). A DIN battery delivers far
more cranking current for a given physical size — the signature of a design optimized for
European cold winters and compact under-bonnet trays.

### 2. DIN delivers ~60% more CCA per unit of capacity

The CCA-per-Ah ratio is 8.7–9.1 for DIN versus 5.5–6.7 for JIS. Two batteries with the same
100Ah capacity will not have the same cranking power — the DIN unit will crank harder in the
cold.

### 3. JIS trades energy density for durability

JIS thick-plate (Pb-Sb) batteries have lower Ah-per-litre (5.6–6.3 vs 7.5–7.7) because their
thicker plates and larger electrolyte reserve favour **deep cycling and vibration tolerance**
over compactness — the right trade-off for hot, demanding commercial duty.

## The Two Engineering Philosophies

| | DIN (European) | JIS (Asian/African) |
|---|---|---|
| Design goal | Compact, high cold-start power | Robust, deep-cycle, heat-tolerant |
| Plate design | Thinner, more plates | Thicker, fewer plates |
| CCA density | High (~66 CCA/L) | Lower (~36 CCA/L) |
| Best climate | Cold winters | Hot, high-vibration |
| Typical vehicle | European trucks, tight trays | Heavy trucks, buses, generators |

## Why This Matters When You Buy

- **Cold climate, compact tray** → a DIN battery gives you the most cranking power per unit
  space
- **Hot climate, heavy cycling** → a JIS thick-plate battery will outlast a compact DIN unit
- **Never compare CCA across standards directly** — the test conditions differ, and the design
  intent differs too

## Related

- [JIS vs DIN vs BCI standards](../jis-vs-din-vs-bci/index.md)
- [JIS N150 vs N200](../jis-n150-vs-n200/index.md)
- [DIN88 vs DIN100](../din88-vs-din100/index.md)
- [What is CCA](../what-is-cca/index.md)

## References

1. [SAE J537 (cold cranking amp test standard)](https://www.sae.org/standards/content/j537_201711/)
2. [Battery Council International — lead battery technology](https://batterycouncil.org/)

!!! note "Methodology"
    Density figures are original calculations from the manufacturer's published datasheet
    values (length × width × height → volume; CCA ÷ volume; CCA ÷ Ah; Ah ÷ volume). They are
    a comparative tool, not a universal rating.

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/din-heavy-duty/) (DIN heavy-duty batteries) or [contact us](https://dinweysbattery.com/contact/) for a quote.


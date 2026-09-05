---
description: JIS vs DIN vs BCI truck battery standards — how the three sizing and rating systems differ, their markets, and how to convert between them.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: What is the difference between JIS, DIN and BCI battery standards?
    a: They are three regional sizing and rating systems. JIS (Japan/Asia) uses model codes like N150/N200; DIN (Europe) uses capacity codes like DIN88/DIN100; BCI (North America) uses group numbers like 31/8D. Each also defines its own cold-cranking test.
  - q: Are JIS and DIN batteries interchangeable?
    a: Not directly. JIS (508×222×212 mm N150), DIN (393×175×190 mm DIN100) and BCI (330×173×240 mm Group 31) use different dimensions and terminals. You must match the standard your vehicle uses.
  - q: Can I convert CCA between standards?
    a: No simple universal conversion exists — the same battery can read differently across standards (e.g. ~870 SAE ≈ 957–1001 EN). Compare within the same standard, or consult manufacturer cross-reference data.
  - q: Which standard does my truck use?
    a: It depends on the market: JIS for Japan/Asia/Africa/Middle East, DIN for Europe, BCI for North America — 3 regional sizing systems that are not interchangeable. Check the battery label or vehicle manual for the correct standard.
  - q: Why does the same battery have different CCA ratings?
    a: Different standards test at different temperatures (JIS −15 °C vs SAE/EN −18 °C, a ~1.18% systematic bias) and voltage cutoffs, so the same battery can carry a higher number under one standard. Always compare like-for-like.
---

# JIS vs DIN vs BCI Truck Battery Standards

**TL;DR** — Three regional standards govern truck battery sizing and rating: JIS (model codes
like N150/N200), DIN (capacity codes like DIN88/DIN100) and BCI (group numbers like 31/8D).
They are not directly interchangeable — always match the standard your vehicle uses.

## Key Takeaways

1. **The 3°C test gap flatters JIS CCA** — JIS D5301 tests at −15°C while SAE J537 and EN 50342-1 test at −18°C, so the same battery reads higher under JIS; cross-standard CCA comparisons are meaningless.
2. **SAE ≈ (DIN × 1.5) + 40 is a planning rule, not a spec** — the conversion varies with battery design, so treating it as exact for a critical order is how buyers end up with the wrong battery.
3. **BCI group numbers define size only** — Group 31, 8D and 4D set dimensions and terminals independently of electrical rating, so two Group 31 batteries can have very different CCA. Verify fit and power separately.
4. **DIN codes encode real amp-hours, JIS codes don't** — DIN88 means 88Ah and DIN100 means 100Ah, but N150/N200 state no capacity; the 145G51 and 190H52 type numbers are the precise spec.
5. **Polarity flips from JIS right-positive to DIN left-positive** — JIS N150/N200 sit right-positive while DIN88/DIN100 sit left-positive, so a size-compatible cross-standard swap can still leave your cables unable to reach.

## Representative Models

| JIS heavy-duty (N150) | DIN heavy-duty (DIN88) |
|---|---|
| ![DINWEY 145G51 JIS N150 truck battery](../assets/145G51-N150.jpg) | ![DINWEY 58827 DIN88 truck battery](../assets/58827-DIN88.jpg) |

## The Three Standards at a Glance

| Standard | Issuing body | Primary markets | CCA test | CCA test temp | Heavy-duty codes |
|---|---|---|---|---|---|
| JIS | Japanese Industrial Standards | Japan, Asia, Africa, Middle East | JIS D5301 | **−15°C** | N150, N200 |
| DIN/EN | Deutsches Institut für Normung | Europe, Middle East, North Africa | EN 50342-1 | **−18°C** | DIN88, DIN100 |
| BCI | Battery Council International | North America, Latin America | SAE J537 | **−18°C** | Group 31, 8D |

## How the Codes Work

- **JIS** — large commercial batteries use a model code where the number tracks size and
  capacity (e.g. 145G51 = N150, 190H52 = N200). Terminals are typically right-positive.
- **DIN** — the code reflects capacity in amp-hours (e.g. DIN88 = 88Ah, DIN100 = 100Ah).
  Terminals are typically left-positive.
- **BCI** — group numbers define physical dimensions (Group 31, 8D, 4D) independently of
  electrical rating.

## Why They Are Not Interchangeable

1. **Different dimensions** — a JIS N150 and a BCI Group 31 are not the same physical size.
2. **Different terminals** — terminal type and left/right positive orientation differ.
3. **Different CCA tests** — the three standards test at different temperatures and cutoffs,
   so the numbers are not directly comparable.

### The Temperature Difference That Matters

One overlooked detail: the standards test cold-cranking at different temperatures.

- **SAE J537 and EN 50342-1** test at **−18°C** (0°F)
- **JIS D5301** tests at **−15°C**

Because JIS tests at a slightly warmer temperature, a JIS CCA figure is **not directly
comparable** to an SAE or EN figure — the same battery will show a higher number under JIS than
under SAE or EN. This is a common source of confusion when buyers compare batteries across
markets.

To put the 3°C gap in physical terms: the two test points sit at **255.15 K** (−18°C) and
**258.15 K** (−15°C) on the absolute temperature scale, so the JIS test is run at a point that
is **≈1.18% warmer** (3 ÷ 255.15 ≈ 0.0118). Because a lead-acid battery delivers more cranking
current as the electrolyte warms, that 1.18% warmer test point always shifts the reading *up* —
a JIS CCA figure is systematically flattered relative to the same battery measured at −18°C.
Three degrees sounds trivial, but it is a directional bias, not a rounding error: it is exactly
why no single conversion factor can reconcile JIS with SAE or EN.

### The Approximate SAE↔DIN Conversion

There is no exact universal conversion between standards, but battery manufacturers publish an
approximate relationship for planning. According to Yuasa's technical documentation, an
approximation of the SAE to DIN cold-cranking relationship is:

```
SAE ≈ (DIN × 1.5) + 40
```

!!! warning "Approximation only"
    This is a planning approximation that varies with battery design — it is not a precise
    specification. For critical applications, use the manufacturer's verified cross-reference
    data, never a general formula.

## Sourcing Implications

When importing or specifying batteries, match the standard to your target market:

| Your market | Use this standard | DINWEY availability |
|---|---|---|
| Southeast Asia, Middle East, Africa | JIS | Stocked (N150, N200) |
| Europe, Middle East, North Africa | DIN/EN | Stocked (DIN88, DIN100) |
| North America, Latin America | BCI | On request (Group 31/8D) |

## References

1. [Battery Council International](https://batterycouncil.org/)
2. [DIN — German Institute for Standardization](https://www.din.de/en)
3. [Battery Council International — lead battery technology](https://batterycouncil.org/)
4. [Battery codes explained: DIN, EN & JIS — Suzuki Battery](https://suzukibattery.sg/blog/basics/car-battery-codes)
5. [Battery specifications guide — Yuasa](https://www.yuasa.com/uk/info-hub/guide-to-understanding-battery-specifications)

## Related

**Standards & sizing — explore this topic:**

- [JIS vs DIN engineering — a density analysis](../jis-vs-din-engineering/index.md)
- [JIS & DIN model numbers](../jis-din-model-numbers/index.md)
- [BCI group sizes explained](../bci-group-sizes/index.md)
- [China GB vs JIS codes](../china-gb-vs-jis/index.md)
- [Maintenance-free vs serviceable JIS](../mf-vs-serviceable-jis/index.md)
- [JIS N150 vs N200](../jis-n150-vs-n200/index.md)
- [DIN88 vs DIN100](../din88-vs-din100/index.md)
- [Terminal types & orientation](../terminal-types-orientation/index.md)

**Related across the hub:**

- [Truck Battery Complete Guide](../complete-guide/index.md)
- [Truck Battery Selection Guide](../selection-guide/index.md)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/jis-heavy-duty/) (JIS heavy-duty batteries) or [contact us](https://dinweysbattery.com/contact/) for a quote.


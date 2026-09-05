---
description: Decoding JIS and DIN battery model numbers — what 145G51, 190H52, 58827 and 60038 mean and how the numbering systems work.
type: article
date_published: 2026-08-30
date_modified: 2026-08-31
faq:
  - q: What does the N in N150 mean?
    a: "N" is a JIS battery size class for larger heavy-duty batteries. N150 and N200 are widely used JIS heavy-duty truck battery designations. The number broadly indicates size, but the underlying JIS type number (like 145G51 or 190H52) is the precise identifier.
  - q: What does 145G51 mean in a JIS battery number?
    a: JIS type numbers encode dimensions, terminal layout and performance class — 145G51 means the 145-class size, G terminal, 51 case. The leading digits relate to size and performance; the full type number is the authoritative identifier.
  - q: What does DIN88 or DIN100 mean?
    a: DIN88 and DIN100 are common European shorthand for DIN-standard heavy-duty batteries, roughly tied to capacity class. The precise identifier is the full DIN/EN type number such as 58827 or 60038.
  - q: Why are there two numbers for the same battery?
    a: Manufacturers list both a market shorthand (like "N150" or "DIN88") and a formal type number (like 145G51 or 58827). The formal type number is what actually defines the physical and electrical specification.
  - q: How do I make sure I order the right battery?
    a: Read the full type number and dimensions (e.g. 190H52 = 520×278×220 mm) from your existing battery or manual, and confirm voltage, CCA, terminal type and polarity. The type number — not the shorthand — is the exact specification.
---

# Decoding JIS & DIN Battery Model Numbers

**TL;DR** — Battery model numbers look cryptic, but they encode real information. JIS
heavy-duty batteries use type numbers like 145G51 (sold as "N150") and 190H52 ("N200"); DIN
batteries use numbers like 58827 ("DIN88") and 60038 ("DIN100"). The full type number is the
authoritative spec — the shorthand is just a convenient name.

## Key Takeaways

1. **The "N" name is a class, not a spec** — N150 and N200 are size classes; only the type numbers 145G51 and 190H52 define exact dimensions, terminal layout and performance class.
2. **Same shorthand can hide different terminals** — the trailing letter-number in 145G51/190H52 sets the terminal configuration, so two batteries sold under one "N" name can differ in terminal position or case height.
3. **DIN88/DIN100 are capacity classes, not exact identifiers** — 88Ah and 100Ah are shorthand; the 58827 (88Ah/800A EN) and 60038 (100Ah/870A EN) type numbers are the real spec.
4. **Put the type number on the order, not the shorthand** — order 145G51 or 58827, never just "N150" or "DIN88", or you risk the wrong terminal layout arriving.
5. **The size gap hides in the type number** — 190H52 at 520×278×220mm is clearly larger than 145G51 at 508×222×212mm; the shorthand "N150/N200" gives you no way to see that.

## JIS: The "N" Shorthand vs the Type Number

In JIS markets, heavy-duty truck batteries are often sold by a short "N" name:

| Market shorthand | JIS type number | Capacity | CCA |
|---|---|---|---|
| N150 | 145G51 | 135 Ah | 900 A |
| N200 | 190H52 | 200 Ah | 1100 A |

The "N" name is a broad size class. The **type number** (145G51, 190H52) is the precise
identifier — it defines the exact dimensions, terminal layout and performance class.

### What the JIS Number Actually Encodes

A JIS type number such as **145G51** is not random. The leading digits track the physical size
and performance class (larger numbers generally mean larger, higher-capacity batteries), while
the trailing letter-and-number combination identifies the terminal configuration and case
layout. The point for a buyer is practical: two batteries with the same shorthand name can
still differ in terminal position or case height, which is why the full type number — not the
"N" name — is what should go on a purchase order.

## DIN: The "DIN88" Shorthand vs the Type Number

European heavy-duty batteries follow the same pattern:

| Market shorthand | DIN type number | Capacity | EN rating |
|---|---|---|---|
| DIN88 | 58827 | 88 Ah | 800 A EN |
| DIN100 | 60038 | 100 Ah | 870 A EN |

## Why the Type Number Matters

The type number encodes the physical and electrical specification. Two batteries that look
similar in a shorthand name may have different dimensions or terminal layouts. When ordering or
specifying:

1. Read the **full type number** from the existing battery label
2. Confirm **dimensions** (the N200 is physically larger than the N150)
3. Confirm **voltage, CCA, terminal type and polarity**

The leading digits in a JIS type number are an index, not a spec. Divide to expose the miss:
**135 Ah ÷ 145 = 0.93** (so 145G51 carries ~7% *less* than its number implies), while
**200 Ah ÷ 190 = 1.05** (190H52 carries ~5% *more*). The error is nearly equal in size —
**10 Ah** — but points in opposite directions (145 overstates, 190 understates), so there is no
fixed offset to add or subtract. DIN runs the opposite game: **DIN88 = 88 Ah** and
**DIN100 = 100 Ah**, so capacity is readable straight off the shorthand, while the type numbers
58827 and 60038 encode nothing readable at all. The practical rule: treat a JIS leading number as
a rough size index (accurate only to about ±7%), and read DIN capacity from the "DINxx" name,
never the type number.

## DINWEY Model Reference

| Model | Standard | Type number | Capacity | CCA | Dimensions (mm) |
|---|---|---|---|---|---|
| 145G51 | JIS | N150 | 135 Ah | 900 A | 508×222×212 |
| 190H52 | JIS | N200 | 200 Ah | 1100 A | 520×278×220 |
| 58827 | DIN/EN | DIN88 | 88 Ah | 800 A EN | 353×175×190 |
| 60038 | DIN/EN | DIN100 | 100 Ah | 870 A EN | 393×175×190 |

For the full comparison within each standard, see
[JIS N150 vs N200](../jis-n150-vs-n200/index.md) and
[DIN88 vs DIN100](../din88-vs-din100/index.md).

## Related

- [JIS N150 vs N200](../jis-n150-vs-n200/index.md)
- [DIN88 vs DIN100](../din88-vs-din100/index.md)
- [How to read a battery datasheet](../how-to-read-datasheet/index.md)

## References

1. [Battery Council International — lead battery technology](https://batterycouncil.org/)
2. [SAE J537 (cold cranking amp test standard)](https://www.sae.org/standards/content/j537_201711/)

## Find the Right Battery

Need a specific model or datasheet? Browse the [DINWEY product range](https://dinweysbattery.com/products/jis-heavy-duty/) (JIS heavy-duty batteries) or [contact us](https://dinweysbattery.com/contact/) for a quote.

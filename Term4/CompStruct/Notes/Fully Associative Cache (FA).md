---
aliases: FA cache
tags: 50.002
---
[[Comp Struct|50.002]]
[[Memory Hierarchy]]

[[Cache]]

## Structure
![](https://dropbox.com/s/yoj1kl3kg3do86c/facache.png?raw=1)

`TAG` and `CONTENT` are made of [[Static Random-Access Memory (SRAM)|SRAM]] cells:
-   `TAG` contains **all bits** of address `A`.
-   `CONTENT` contains all bits of `Mem[A]`.

> It will be 32 bits of data and 32 bits of address for [[Building Beta CPU|beta CPU]]

Note the presence of a device called the *tri-state buffer*.
![](https://dropbox.com/s/hu22kodm6etknl5/tsbuffer.png?raw=1)

## Truth Table
| $A$ | $X$ | $Y$    |
| --- | --- | ------ |
| 0   | 1   | 0      |
| 1   | 1   | 1      |
| 0   | 0   | High-Z |
| 1   | 0   | High-Z |

High-Z (High impedance):\
A state when the output is **not driven** by any of the inputs.

We can equivalently say that the output is _neither high (1) nor low (0)_ and is _electrically disconnected_ from the circuit.

## Characteristics
### Expensive
Made of [[Static Random-Access Memory (SRAM)|SRAM]]s for both `TAG` and `DATA` (Content) field:
64 bits total for $\beta$

Also has lots of other hardware:
- Bitwise comparator at each *cache-line* (an 'entry': `TAG-Content` illustrated as a row in the figure above)
- Tri-state buffer at each row
- Large `OR` gate to compute `HIT` [[Cache|HIT]]

### Very fast
Does **parallel** lookup when given an incoming [[Memory Addressing|address]]
- Comparison between incoming [[Memory Addressing|address]] and all `TAG` in each cache line happens *simultaneouly*

### Flexible
[[Memory Addressing|Memory address]] `A` + its content `Mem[A]` can be **copied** and **stored** on *any cache-line*: `TAG-Content` entry.

## Conclusion
FA cache is the **gold standard** on how well a cache should perform

See other:
[[Direct Mapped Cache (DM)|DM cache]]
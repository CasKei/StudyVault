---
aliases: average cache performance
tags: 50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]

## What
We can compute **average [[Cache]] performance** by counting how many `HIT`s and `MISS`es there are given `N` queries in sequence, and dividing the number of `HIT` with `N`, given its hardware specification such as [[Cache Block size]], [[Replacement policy]] and [[cache]] sze.

If query sequences repeat itself, we can compute the number of `HIT` and `MISS` from its **steady state**.

## Example
We want to measure the performance of a [[Fully Associative Cache (FA)|FA cache]] that has `4` cache lines with [[Replacement policy#Least Recently Replaced LRR|LRR]] replacement policy.

Assume [[Cache]] **initially empty** (or has redundant values).\
Let [[Anatomy of the Beta CPU|CPU]] execute the following program consisted of 9 `READ` (`LD`) requests for a few rounds:

`At t=0: 0x0014` 
`At t=1: 0x0011` 
`At t=2: 0x0022` 
`At t=3: 0x0014` 
`At t=4: 0x0043`
`At t=5: 0x0012`
`At t=6: 0x0014`
`At t=7: 0x00AB`
`At t=8: 0x0033`

*Repeat* the same sequence for `t=9` to `t=17` for a *second* round.
*Repeat* the same sequence for `t=18` to `t=26` for a *third* round.

To benchmark this cache we need to count how many `MISS` and `HIT` at **steady state**. Hence we need to figure out *which rounds make up the steady state*.

### First round
**At the first round**, `t=0` to `t=8`, we have:

`At t=0: 0x0014` → `MISS` (and cached)

> Cache content after: **`0x0014`**, `EMPTY`, `EMPTY`, `EMPTY`. Oldest entry is bolded.

`At t=1: 0x0011` → `MISS` (and cached).

> Cache content after: **`0x0014`,** `0x0011`, `EMPTY`, `EMPTY`.

`At t=2: 0x0022` → `MISS` (and cached).

> Cache content after: **`0x0014`**, `0x0011`, `0x0022`, `EMPTY`.

`At t=3: 0x0014`→ `HIT` 

`At t=4: 0x0043`→ `MISS` (and cached)

> Cache content after: **`0x0014`**, `0x0011`, `0x0022`, `0x0043`.

`At t=5: 0x0012` → `MISS` (and cached by replacing oldest entry:`0x0014`)

> Cache content after: **`0x0011`**, `0x0022`, `0x0043`, `0x0012`.

`At t=6: 0x0014`→ `MISS` (and cached by replacing oldest entry:`0x0011`)

> Cache content after: **`0x0022`**, `0x0043`, `0x0012`, `0x0014`.

`At t=7: 0x00AB` → `MISS` (and cached by replacing oldest entry:`0x0022`)

> Cache content after: **`0x0043`**, `0x0012`, `0x0014`, `0x00AB`.

`At t=8: 0x0033` → `MISS` (and cached by replacing oldest entry:`0x0043`)

> Cache content after: **`0x0012`**, `0x0014`, `0x00AB`, `0x0033`.

### Second round
Now during the **second round**, `t=10` to `t=19`, we have the same 9 input sequences. Let’s observe the result:

`At t=10: 0x0014` → `HIT`

`At t=11: 0x0011` → `MISS` (and cached by replacing oldest entry:`0x0012`)

> Cache content after: **`0x0014`**, `0x00AB`, `0x0033`, `0x0011`.

`At t=12: 0x0022` → `MISS` (and cached by replacing oldest entry:`0x0014`)

> Cache content after: **`0x00AB`**, `0x0033`, `0x0011`, `0x0022`.

`At t=13: 0x0014`→ `MISS` (and cached by replacing oldest entry:`0x00AB`)

> Cache content after: **`0x0033`**, `0x0011`, `0x0022`, `0x0014`.

`At t=14: 0x0043`→ `MISS` (and cached by replacing oldest entry:`0x0033`)

> Cache content after: **`0x0011`**, `0x0022`, `0x0014`, `0x0043`.

`At t=15: 0x0012` → `MISS` (and cached by replacing oldest entry:`0x0011`)

> Cache content after: **`0x0022`**, `0x0014`, `0x0043`, `0x0012`.

`At t=16: 0x0014`→ `HIT`

`At t=17: 0x00AB` → `MISS` (and cached by replacing oldest entry:`0x0022`)

> Cache content after: **`0x0014`**, `0x0043`, `0x0012`, `0x00AB`.

`At t=18: 0x0033` → `MISS` (and cached by replacing oldest entry:`0x0014`)

> Cache content after: **`0x0043`**, `0x0012`, `0x00AB`, `0x0033`.

### Third round
Running the cache for **another round** (the third time) at `t=19` to `t=27` with the same 9 input sequences:

`At t=19: 0x0014` → `MISS` (and cached by replacing oldest entry:`0x0043`)

> Cache content after: **`0x0012`**, `0x00AB`, `0x0033`, `0x0014`.

`At t=20: 0x0011` → `MISS` (and cached by replacing oldest entry:`0x0012`)

> Cache content after: **`0x00AB`**, `0x0033`, `0x0014`, `0x0011`.

`At t=21: 0x0022` → `MISS` (and cached by replacing oldest entry:`0x00AB`)

> Cache content after: **`0x0033`**, `0x0014`, `0x0011`, `0x0022`.

`At t=22: 0x0014`→ `HIT`

`At t=23: 0x0043`→ `MISS` (and cached by replacing oldest entry:`0x0033`)

> Cache content after: **`0x0014`**, `0x0011`, `0x0022`, `0x0043`.

`At t=24: 0x0012` → `MISS` (and cached by replacing oldest entry:`0x0014`)

> Cache content after: **`0x0011`**, `0x0022`, `0x0043`, `0x0012`.

`At t=25: 0x0014`→ `MISS` (and cached by replacing oldest entry:`0x0011`)

> Cache content after: **`0x0022`**, `0x0043`, `0x0012`, `0x0014`.

`At t=26: 0x00AB` → `MISS` (and cached by replacing oldest entry:`0x0022`)

> Cache content after: **`0x0043`**, `0x0012`, `0x0014`, `0x00AB`.

`At t=27: 0x0033` → `MISS` (and cached by replacing oldest entry:`0x0043`)

> Cache content after: **`0x0012`**, `0x0014`, `0x00AB`, `0x0033`.

### Fourth round onwards
If we run it again for the _fourth_ round, we will have the same `HIT` and `MISS` sequences as the _second_ round. This implies that the result of running it for the _fifth_ round will be identical to the _third_ round.

Hence _on average_ we can count the number of `HIT` for the second and third round: 3 `HIT` in total for 18 address calls.

We ignore results from the first round because that result will never repeat itself again as we begin with empty cache only once in the beginning.

That means out of the 18 address calls, we have 15 `MISS`. The miss rate of this cache is therefore pretty high at $83.33\%$.



Test yourself: If the FA cache uses LRU, will it have a better performance? i.e: less miss rate. What about when DM cache of same size (4 cache lines) is used? _Which cache design is better for this particular program running in a loop_?
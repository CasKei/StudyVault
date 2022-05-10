---
aliases:
tags: 50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]

Previously, we used **byte addressing** by convention.

However, for ease of calculation in practice questions and problem sets, we can use **word addressing** instead.

Given a [[Anatomy of the Beta CPU|memory unit]] of fixed size `M`, can use 2 bits less if we use word instead of byte addresseing.

For [[Direct Mapped Cache (DM)|DM cache]]/[[Associativity|NWSA]] cache with `8` blocks and **word addressing**, we need to divide the original requestied address into the same **3 segments**, but but we don't have the default `00` in the lawest 2 bits of the address anymore.

![](https://dropbox.com/s/2dsjsjurxtndevq/wordbyte.png?raw=1)

- Lowest `b`-bits to index each word in a cache line block.
- `K`-bits to index each cache line or set.
- Highest (remainder) `T`-bits of the original requested address to be stored in the `TAG` field.
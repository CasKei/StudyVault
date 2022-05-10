---
aliases: NWSA, N-way set associative cache
tags: 50.002
---
[[Comp Struct|50.002]]

![[Cache Design Issues#^33c36d]]

# Improving Associativity
Here we learn a new cache design called the **N-way set associative cache (NWSA)**: a *hybrid* between [[Fully Associative Cache (FA)|FA cache]] and [[Direct Mapped Cache (DM)|DM cache]] architecture.

## Motivation
[[Direct Mapped Cache (DM)|DM cache]] cheap BUT suffers from the **contention problem**.
> [[Direct Mapped Cache (DM)#Contention|Contention]] mostly occurs within a certain block of addresses (called independent hot-spots), due to the [[Memory Hierarchy#Reason why this works|locality of reference]] in each different address range.

E.g.
	If instructions for 
	Program A is in [[Memory Addressing|memory address]] range `0x1000` to `0x1111`, and 
	Program B is in [[Memory Addressing|memory address]] range `0xB000` and `0xB111`, and
	`k=3` in the [[Anatomy of the Beta CPU|CPU]] [[Direct Mapped Cache (DM)|DM cache]],

**Concurrent execution** of Program A and B will cause major [[Direct Mapped Cache (DM)|contention]].

Hence, some degree of associativity is needed.
Full associativity is expensive, so we just try to have some.

## N-Way Set Associative Cache
Cheaper than [[Fully Associative Cache (FA)|FA cache]], more expensive than [[Direct Mapped Cache (DM)|DM cache]].
Less risk of [[Direct Mapped Cache (DM)|contention]] (proportional to value of `N`)

![](https://dropbox.com/s/jbg0b7ajjcn79mg/nway.png?raw=1)

- Made of `N` [[Direct Mapped Cache (DM)|DM cache]]s, connected in **parallel**
- Cells in same **row**: belong in same **set**
- Cells in same **column**: being in same **way**. Each way is a [[Direct Mapped Cache (DM)|DM cache]] that has $2^K$ cache lines.

Given a combination of `K`-bits lower address, the higher `T` bits `TAG` and its `Content` can be stored in **any of the N cache lines in the same set**

Given a query address `A`:
- We need to wait for the device to decode its last `K` bits and find the right set
- Then, device will perform a **parallel lookup** operation for all `N` cache lines in the same set.
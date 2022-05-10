---
tags: 50.002
---
[[Comp Struct|50.002]]

## Overview
Recall: [[Cache]] is a small and fast and expensive and made of [[Static Random-Access Memory (SRAM)|SRAM]] [[Anatomy of the Beta CPU|memory unit]] assebled near the [[Anatomy of the Beta CPU|CPU]] core, which function is to *reduce the average time and energy required for the [[Anatomy of the Beta CPU|CPU]] to access some requested data `Mem[A]` located in the Main Memory ([[Dynamic Random-Access Memory (DRAM)|RAM]]).*

You know them commercially as the L1, L2, or L3 caches. We simplify them in this course by just referring to them as a single _cache_.

The [[Cache]] contains a **copy** of some recently or frequently used *data* `Mem[A]` and its *address* `A`. The hardware is assembled in such a way that the [[Anatomy of the Beta CPU|CPU]] will always look for that particular data in the [[Cache]] first, and only look for the requested information in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] if cache `MISS` occurs (and then the [[Cache]] will be updated to contain this new info).

Note: [[Anatomy of the Beta CPU|CPU]] can both **read** and **write** to the [[Cache]] (like normal `LD` and `ST` to the [[Dynamic Random-Access Memory (DRAM)|RAM]])

Without the [[Cache]] device, [[Anatomy of the Beta CPU|CPU]] has to frequently access [[Dynamic Random-Access Memory (DRAM)|RAM]]. Frequent `LD` and `ST` to the [[Dynamic Random-Access Memory (DRAM)|physical memory]] becomes the main *bottleneck* for [[Anatomy of the Beta CPU|CPU]] performance. This is because the time taken for a **write and read** in [[Dynamic Random-Access Memory (DRAM)|DRAM]] is significantly longer than the optimum [[Anatomy of the Beta CPU|CPU]] `CLK` cycle.

**This chap**: Various [[Cache]] design issues such as:
- (hardware) Parameters
	- Block size
	- Cache size
	- Associativity
- Management
	- Write policy
	- Replacement policy

## Cache Design Issues
- [[Associativity]] ^33c36d
	- We need to determine how many *different* cache lines can *one address* be stored to.
	- ==Implies choice==.
	- Note there can only be *one copy* of that address (tag) in the entire cache.
	- [[Direct Mapped Cache (DM)|DM cache]]: 
		- There is ==no choice== on which cache line is used or looked up.
		- A **1-to-1** mapping between each combination of the last $k$ bit of the query address `A` to the [[Cache]] line (entry) is required. Hence [[Direct Mapped Cache (DM)|DM cache]] has **no associativity**.
	- [[Fully Associative Cache (FA)|FA cache]]:
		- Has **complete associativiy**.
		- We have `N` choices of cache lines in a [[Fully Associative Cache (FA)|FA cache]] of size `N`
		- Any `TAG-Content` can reside on any cache line in FA cache.
- [[Replacement policy]] ^2657a0
	- Refers to the decision on which entry of the cache should we replace in the event of a cache `MISS`
- [[Cache Block size]] ^249c20
	- Refers to the problem on deciding how many sets of 32-bit data we want to *write* to the cache at a time
- [[Write policy]] ^842e09
	- Refers to the decision on *when* to *write* (updated entries) from cache to [[Dynamic Random-Access Memory (DRAM)|main memory]]

## [[Fully Associative Cache (FA)|FA cache]] VS [[Direct Mapped Cache (DM)|DM cache]]
| Metric                 | [[Fully Associative Cache (FA)]]                                     | [[Direct Mapped Cache (DM)]]                 |
| ---------------------- | -------------------------------------------------------------------- | -------------------------------------------- |
| `TAG` field            | All address bits                                                     | Higher `T` address bits                      |
| `Content` field        | All N bits of data: `Mem[A]`                                         | All N bits of data: `Mem[A]`                 |
| `TAG` indexing         | None                                                                 | Lower `K` address bits                       |
| [[Cache]] size         | Any                                                                  | $2^K$                                        |
| Memory cell technology | [[Static Random-Access Memory (SRAM)\|SRAM]]                         | [[Static Random-Access Memory (SRAM)\|SRAM]] |
| Performance            | Very fast (gold standard)                                            | Slower than FA on average                    |
| Contention risk        | None                                                                 | Inversely proportional to cache size         |
| Cost                   | Expensive                                                            | Cheaper                                      |
| [[Replacement policy]] | LRU, LRR (FIFO), Random                                                    | Not Applicable                               |
| [[Associativity]]      | Fully associative: any `TAG-Content` can be placed on any cache line | None. Each cache line can only contain matching lower `k`-bits `TAG`                                             |

It is obvious each design has its own pros and cons depending on its application.
[[Fully Associative Cache (FA)|FA cache]] better in applications where small cache size is sufficient.
[[Direct Mapped Cache (DM)|DM cache]] suffers severe contention when cache size is small, but perform reasonably well on average when size is large.


## The Helper Bits
[[Helper Bits]]

## Word Addressing Convention
[[Word addressing]]

## Cache Benchmarking
[[Cache benchmarking]]

## The Caching Algorithm
[[Caching algorithm]]

## Summary
The 4 cache design issues are:
- [[Associativity]]
- [[Replacement policy]]
- [[Write policy]]
- [[Cache Block size]]

There is no one design that suits all situations.
Performance depends on use case.

E.g. associativity less important when `N` is large because risk of contention is inversely proportional to `N`.

Can attempt to analyse cache performance by building intuition from simple examples or using simulations of cache behaviours on real programs. Through various analysis with different use cases, we can fine tune and establish the basis for cache design decisions.
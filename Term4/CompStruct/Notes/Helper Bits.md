---
aliases: Valid bit, Dirty bit, LRU bits, helper bit
tags:50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]

## Overview
The [[Cache]] device may need to store not just `TAG-Content` per cache line, but  also some helper bits that are used to perform some [[Write policy]] or [[Replacement policy]], and the overall [[Caching algorithm]].

## V: Valid Bit
> The valid bit is used to indicate whether the particular cache line contains\
> **valid and important values** (valid copy of data from [[Anatomy of the Beta CPU|memory unit]])\
> and **not an invalid or redundant in value**.

	Note: Info is encoded in voltage. Device does not know what is the difference between valid and invalid stuff in a memory cell until it attempts to compute its value, which takes time.

	It also cannot tell the difference between redundant (old) and new info. Therefore, valid bit is a quick indicator whether the content in cache line is important or not.

The [[Cache]] performance can be further sped up if it is made to check (compare `TAG`) if `V=1` for the cache line, and skip comparison of `TAG` when `V=0`.

This allows for a faster `HIT` computation in the event of [[Cache]] `MISS`.

*Cost:* just 1 extra storage bit per cache line.
For cache lines with block size larger than 1, there's still only one `V` bit per cache line (so the entire `b` block of words are either *present* or *not present*)


## D: Dirty Bit
> The dirty bit is used to indicate whether we need to update the [[Anatomy of the Beta CPU|memory unit]] to reflect the new updated version in the [[Cache]].

- `1`: **iff** cache line is updated ([[Anatomy of the Beta CPU|CPU]] writes new value to [[Cache]]) but new value not yet stored to [[Dynamic Random-Access Memory (DRAM)|physical memory]].

IOW, copy in [[Dynamic Random-Access Memory (DRAM)|physical memory]] is outdate.


## LRU: Least Recently Used Bits
[[Replacement policy|LRU]]
The LRU bit is present in each cache line for [[Fully Associative Cache (FA)|FA cache]] and [[Associativity|NWSA]] [[Cache|cache]] only regardless of [[Cache Block size]].
[[Direct Mapped Cache (DM)|DM cache]] does not have a [[Replacement policy]].

For a [[Cache|cache]] of size $N$, we need $N\log{N}$ bits per cache.


## Summary
Helper bits can be illustrated in a diagram like below. Below we have a sample of 3WSA [[Cache]] with [[Cache Block size]] of `2`.

![](https://dropbox.com/s/jdzkblgoyb6dh7i/3way.png?raw=1)
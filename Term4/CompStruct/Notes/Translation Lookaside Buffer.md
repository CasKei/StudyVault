---
aliases: TLB
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]
[[Pagetable]]

## Why
> [[Pagetable]] is stored in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] for practical resons because of is huge ass size.

Costly to use [[Static Random-Access Memory (SRAM)|SRAM]] based memory device. The OS Kernel manages a portion of the [[Dynamic Random-Access Memory (DRAM)|physical memory]], dedicated to store the pagetable.

The MMU has a component called `Pagetable Pointer` which can be set to point to the first entry of the pagetable in the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

**Problem**: we need to access the slow [[Dynamic Random-Access Memory (DRAM)|physical memory]] twice.
1. Look up Pagetable to translate [[Virtual Address|VA]] to [[Memory Addressing|PA]].
2. Get content `Mem[PA]`

*Cheap solution costs performance.*

**Solution**
Build a small [[Static Random-Access Memory (SRAM)|SRAM]] based memory device to [[Cache]] a few of the most recently used entries of the pagetable. This is called the [[Translation Lookaside Buffer]].

## What
The TLB is a small [[Fully Associative Cache (FA)|FA cache]] to store a copy of some recently used Pagetable entries:
![](https://dropbox.com/s/g0ydenuirecwtwo/mmutlb.png?raw=1)

We also use a [[Memory Hierarchy|hierarchy]] of memory devices here. Similarly [[Cache]] a few of the most recently used contents and its address in another faster but smaller [[Static Random-Access Memory (SRAM)|SRAM]]-based memory device to reduce the frequency of access to the slower but larger [[Dynamic Random-Access Memory (DRAM)|DRAM]]-based [[Dynamic Random-Access Memory (DRAM)|physical memory]] device.

## Super Locality of Reference
We know that there is [[Memory Hierarchy|locality of reference]] in [[Memory Addressing|memory address]] reference patterns. Therefore there is ==super locality== of page number reference patterns (hit-rate of the TLB $99\%$ in practice).

Note: [[Replacement policy|LRU]] bits in the TLB is **not the same** as [[Replacement policy|LRU]] bits in [[Pagetable]].
Reason:
The number of `N` entries in the TLB is always the `N` most recently accessed pages out of $2^v$ possible entries in the pagetable, where $N<2^v$ in practice.

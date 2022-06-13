---
aliases: cache
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Memory Hierarchy]]

# 50.005
## Cache
[[Cache]]
Used to speed up performance.
Storing a few of the most recently used instruction pages.
Wired directly to [[Anatomy of the Beta CPU|CPU]] so CPU has direct access.

Limited size, so management is important [[Cache Design Issues]].

[[OS Kernel]] dictates details pertaining to cache management, such as which supported [[Replacement policy]] should be used.

## Cache Performance
**Caching** is an important principle of computer systems. We perform the [[Caching algorithm]] each time the CPU needs to execute a new piece of instruction or fetch new data from the main memory. Remember that cache is hardware, built into CPU:
![](https://natalieagus.github.io/50005/assets/images/week1/14.png)
Note:
"DMA" = [[Direct addressing|Direct memory access]] from [[Device Controller]] onto [[Dynamic Random-Access Memory (DRAM)|RAM]].

Data transfer between [[Hard Disk Drive (Disk)|disk]] and [[Dynamic Random-Access Memory (DRAM)|main memory]] is usually controlled by [[OS Kernel]] (requires [[Context switch]]ing), while data transfer between CPU registers to CPU cache is a hardware function **without kernel intervention**. There is too much *overhead* if kernel is tasked to do that.

Recall Kernel is responsible to program and set up cache and [[Pagetable|MMU]] hardware, and manage the entire [[Virtual Memory]]. Kernel memory management routines are triggered when processes running in [[Kernel mode and User mode|user mode]] encounter [[Demand Paging|page fault]] related interrupts. Careful selection of page size and a [[Replacement policy]] can result in greatly increased performance.

Given a cache hit ratio $\alpha$, a cache miss access time $\epsilon$, and cache hit access time $\tau$, we can compute the **cache effective access time** as:
$$\alpha \tau + (1-\alpha ) \times \epsilon$$

# 50.002 
## What
> **Cache**
> A small storage device assembled close to a processor core within a [[Anatomy of the Beta CPU|CPU]].

Contains:
**Temporary copies** of **selected [[Memory Addressing|memory address]] `A` and their content `Mem[A]`**.

[[Anatomy of the Beta CPU|CPU]] will always look for the requested instruction or data on the cache first, before starting to loop for it in [[Dynamic Random-Access Memory (DRAM)|physical memory]] in the event of a cache `MISS`.

## Principles
1. Upon any [[Beta Instruction Cycles|instruction]] fetch, or any instruction involving `LD` or `ST`, [[Anatomy of the Beta CPU|CPU]] will first look for requested data in cache.
2. **Cache** `HIT`: If the information is found in the cache, return the content to the [[Anatomy of the Beta CPU|CPU]]
3. **Cache** `MISS`: Not found in cache.

In the event of a cache `MISS`,
1. Look for the requested content in the [[Dynamic Random-Access Memory (DRAM)|physical memory (RAM)]].
2. Once this content is found, *replace* some (unused) cache content with this new content.

In the event that the content is also not found in [[Dynamic Random-Access Memory (DRAM)|RAM]], we look for the content in the *swap space* region of the disk, and perform necessary updates on both the [[Dynamic Random-Access Memory (DRAM)|physical memory]] and the [[Cache]].\
*Swap space* is a a dedicated space on the disk that is set aside to serve as an (virtual) _extension_ of the RAM. We will learn more about this in the [[Cache Design Issues|next chapter]].

![[Pasted image 20220328144044.png]]

## Metrics
### Hit Ratio
$$
\alpha = \dfrac{\text{hits}}{\text{hits} + \text{misses}}
$$
### Miss Ratio
$$
1-\alpha = \dfrac{\text{misses}}{\text{hits} + \text{misses}}
$$
### Average Memory Access Time
$$
\begin{align}
t_{\text{ave}} &= \alpha t_c + (1-\alpha)(t_c + t+m)\\
&= t_c + (1-\alpha)t_m
\end{align}
$$
- $\alpha$: [[#Hit Ratio]]: count of requests with hit/total request count
- $t_c$: cache access time
- $t_m$: [[Dynamic Random-Access Memory (DRAM)|physical memory]] access time

> You easily simply extend the formula to incorporate the events where disk is used.

## Details
The above steps are very simplified and incomplete. It does not address more details such as how we can store data in the cache, what to do in the event of a cache miss in more detail, what happens when the RAM is full, etc.

We will perfect the cache principle to form the **caching algorithm** in the [[Cache Design Issues|next lesson]].

## Modern Cache
Most modern [[Anatomy of the Beta CPU|CPU]]s have at least 3 independent caches:
- Instruction cache: speed up executable instruction fetch
- Data cache: speed up data fetch and store
- Translation Lookaside Buffer (TLB): speed up virtual-to-physical address translation for both (executable) instructions and data.

Data caches is usually organised as a hierarchy of more cache levels. (L1, L2, L3, L4, etc)

In this course, we simplify by assuming there is only one cache for both instructions and data, and one level of cache.
We will learn more about TLB in the [[Cache Design Issues|next chapter]].

## Types of Caches/ Cache Design
There are 2 flavours in cache design. Each has its own benefits and drawbacks.
[[Fully Associative Cache (FA)]]
[[Direct Mapped Cache (DM)]]
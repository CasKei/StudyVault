---
aliases: locality of reference
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]

## 50.005
The storage structure in a typical [[Computer System]] is made up of [[Sequential Logic|register]]s, [[Cache]]s, [[Dynamic Random-Access Memory (DRAM)|main memory]], and non-volatile [[Hard Disk Drive (Disk)|secondary storage]] such as disk. In increasing speed and cost from bottom up:
![](https://natalieagus.github.io/50005/assets/images/week1/3.png)

- The [[Anatomy of the Beta CPU|CPU]] can load instructions only from memory, so any programs to run must be stored there
- General-purpose computers run most programs from rewritable memory called [[Dynamic Random-Access Memory (DRAM)|main memory]].
- At each [[Anatomy of the Beta CPU|CPU]] clock cycle, instructions are fetched from [[Dynamic Random-Access Memory (DRAM)|main memory]] to [[Anatomy of the Beta CPU|CPU]].

### RAM
[[Dynamic Random-Access Memory (DRAM)|RAM]]
Ideal: permanent storage
Not possible:
- Main mem too smol
- Volatile and loses contents when powered off

Recall that the memory unit sees only a stream of memory addresses; it does not know how they are generated (by the instruction counter, indexing, indirection, literal addresses, or some other means) or what they are for (instructions or data).

### Cache
[[Cache]]
Used to speed up performance.
Storing a few of the most recently used instruction pages.
Wired directly to [[Anatomy of the Beta CPU|CPU]] so CPU has direct access.

Limited size, so management is important [[Cache Design Issues]].

[[OS Kernel]] dictates details pertaining to cache management, such as which supported [[Replacement policy]] should be used.

## 50.002 Overview
![](https://dropbox.com/s/88up5y3aitc893l/p1.png?raw=1)
[[Building Beta CPU|beta CPU]] has its own internal storage [[Anatomy of the Beta CPU|REGFILE]], consisted of a limited amount of [[Sequential Logic|registers]].

The $\beta$ can also **write to** and **read from** an external [[Anatomy of the Beta CPU|memory unit]].\
This memory unit can be arbitrary in size depending on how many bits are used for addressing.

> Note: A 32-bit address can address $2^{32}$ different bytes, and therefore up to 4GB of data.

Since $\beta$ is a 32-bit CPU, it can supply at most 32-bit of address to the [[Anatomy of the Beta CPU|memory unit]], and therefore it can access at most 4GB of **address space** at a time without the help of other hardware.

>Note: This limitation can be removed on certain x86 32-bit architectures via the use of a particular memory management hardware called the [PAE (Physical Address Extension)](http://en.wikipedia.org/wiki/Physical_Address_Extension). PAE was first introduced by Intel in their Pentium Pro processor, and later by AMD (Athlon processor). We will not touch about PAE in this course.


[[Anatomy of the Beta CPU|REGFILE]]\
**Very expensive to manufacture** But ***Extremely fast***:\
We can write to or read from the [[Anatomy of the Beta CPU|REGFILE]] unit at a very high frequency (low latency)

Expensive [[Anatomy of the Beta CPU|REGFILE]]: can only affort to pack a few [[Sequential Logic|registers]] within the [[Anatomy of the Beta CPU|CPU]] while keeping it at reasonable cost, and **extend the storage space** using some external memory device we labelled as the [[Anatomy of the Beta CPU|memory unit]].

[[Anatomy of the Beta CPU|Memory Unit]]\
**Cheaper** than regfile.\
Bigger storage space at a fraction of the price.

Depending on the technology, *writing* to or *reading* from the external memory unit can be _much slower_ (than the REGFILE), and therefore memory access becomes the **bottleneck** of the computer performance.

| Type                                    | Space/Capacity | Latency      | Cost     |
| --------------------------------------- | -------------- | ------------ | -------- |
| [[Anatomy of the Beta CPU\|Register]]                             | 100s of bytes  | 20ps         | \$\$\$\$ |
| [[Static Random-Access Memory (SRAM)]]  | 100s of KB     | 1ns          | \$\$\$   |
| [[Dynamic Random-Access Memory (DRAM)]] | 100s of MB     | 40ns         | \$       |
| [[Solid-State Drive (SSD)]]             | 100s GB        | 100$\micro$s | \$\$     |
| [[Hard Disk Drive (Disk)]]              | 1TB            | 10ms         | c        |
| What we want                            | HIGH           | LOW          | CHEAP    |

> Goal: have a **large** memory space at a **cheap** cost and **minimum latency**.
> To do: incorporate the concept of [[Memory Hierarchy]] in our system.

## Memory Technologies
[[Static Random-Access Memory (SRAM)]]
[[Dynamic Random-Access Memory (DRAM)]]
[[Hard Disk Drive (Disk)]]
[[Solid-State Drive (SSD)]]

## Memory Addressing
[[Memory Addressing]]

##  Memory Hierarchy Strategy
![](https://dropbox.com/s/9v2wj0zf64zbclo/memhierarchy.png?raw=1)

> Goal: Perform with [[Static Random-Access Memory (SRAM)|SRAM]] speed at the cost of [[Hard Disk Drive (Disk)|HDD]].
--> a large, fast and cheap memory

We need to use a **hierarchy of memory technologies** to form the external [[Anatomy of the Beta CPU|memory unit]].
- Keep data used most often at a small device made of [[Static Random-Access Memory (SRAM)|SRAM]]s, called [[Cache]]. Assembled near the processor core and is considered part of the [[Anatomy of the Beta CPU|CPU]].
- Refer to [[Dynamic Random-Access Memory (DRAM)|physical memory]] (DRAM/RAM) rarely.
- Refer to [[Solid-State Drive (SSD)|secondary storage]] (disk) even more rarely.

## Reason why this works
This can give the user an illusion that they are running at [[Static Random-Access Memory (SRAM)|SRAM]] speed at all times due to:
> **Locality of reference**\
> Reference to mmory location $X$ at time $t$ implies that\
> reference to $X + \Delta X$ at $t + \Delta t$ \
> becomes **more probable** as $\Delta X, \Delta t \to 0$.

In laymen terms: there exists the tendency of a CPU to access the _same set of memory locations_ **repetitively** over a short period of time.

Evidence that memory reference patterns exhibit locality of reference:
- Local [[Stack and Procedures|stack]] frame grows nearby to one another
- Related program instructions are near one another
- Data are also nearby one another


## The Cache Idea
[[Cache]]

## Cache Designs
[[Fully Associative Cache (FA)]]
[[Direct Mapped Cache (DM)]]

## Summary
We have a glimpse of varius memory technology: from slowest to fastest, cheapest to most costly.

We use a hierarchy of memory technology in our computer system to give it a illusion that it is running at a high [[Static Random-Access Memory (SRAM)|SRAM]] speed and the size and cost of a [[Hard Disk Drive (Disk)|disk]].
The idea is to use a small but fast (and costly) device made of [[Static Random-Access Memory (SRAM)|SRAM]]s to [[Cache]] most recently and frequently used information, and refer to the [[Dynamic Random-Access Memory (DRAM)|physical memory]] or [[Hard Disk Drive (Disk)|disk]] as rarely as possible.

This is because of *locality of reference*: allows us to predict and keep a small copy of recently used instruction and data in cache.

We were then introducedto two basic types of cache design that can be integrated into our [[Anatomy of the Beta CPU|CPU]]: the [[Fully Associative Cache (FA)|FA cache]] (gold standard but expensive) and [[Direct Mapped Cache (DM)|DM cache]] (cheaper, but suffers contention and slower).

In next chapter, we learn various cache issues and how to tackle them to meet our goal of a fast and cheap computer with massive storage space.
[[Cache Design Issues]]
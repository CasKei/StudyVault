---
aliases: MMU, pagetable, pagemap, memory management unit
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Virtual Memory]]
[[Week 1 - Introduction to Operating System]]

# 50.005
## Configuring the MMU
The MMU (Memory Management Unit) is a computer **hardware** component that primarily handles translation of [[Virtual Address]] to physical memory address. It relies on data on the system’s RAM to operate: e.g utilise the **pagetable**. The [[OS Kernel]] sets up the pagetable and determine rules for the address mapping.

Recall from 50.002 that the CPU always operates on virtual addresses (commonly **linear**, `PC+4` unless branch or JMP), but they’re translated to physical addresses by the MMU. The [[OS Kernel]] is aware of the translations and it is ==solely responsible== to **program** (configure) the MMU to perform them.

# 50.002
## Purpose
Each `VA` has to be mapped to a `PA`, so that the system may return the requested data to the [[Anatomy of the Beta CPU|CPU]] upon instruction fetch (`LD`), or complete the executionof `ST` related instructions. This mapping is done via the **memory management unit** (MMU).

 **MMU**:
> A small hardware unit where all memory references from the [[Anatomy of the Beta CPU|CPU]] is passed through itself, and its primary function is to translate from `VA` to `PA`.
> Refer to [[Pagetable]] for more information.

The OS Kernel maintains a **Pagetable**, aka pagemap, that keeps track of the translation between each [[Virtual Address|VA]] of each program to its corresponding [[Memory Addressing|PA]]

>**Pagetable**
>contains **all possible combination of virtual address of a program**
>but not all [[Virtual Address|VA]] has a corresponding [[Memory Addressing|PA]] at a time in the [[Dynamic Random-Access Memory (DRAM)|RAM]] (it may be in the [[Hard Disk Drive (Disk)|disk]]).

## How
The memory management unit (MMU) utilises the pagetable to translate every memory reference request from the [[Anatomy of the Beta CPU|CPU]] to an actual [[Memory Addressing|physical address]]:
![](https://dropbox.com/s/rek05rsjagk2m43/mmuusage.png?raw=1)

The pagetable stores the mapping of the ==higher== $v$ bits of [[Virtual Address|VA]] (called the `VPN` - Virtual Page Number) to a corresponding `PPN` (physical page number).

==Exactly one entry is needed for every possible virtual page== so ==the numberoof entries in the pagetable is $2^v$==

The [[Memory paging|PO]] field of [[Virtual Address|VA]] is the same as the [[Memory paging|PO]] field of its [[Memory Addressing|PA]]. If you always have `00` at the back of the [[Memory paging|PO]] it simply means BYTE ADDRESSING is used, buit the number of bits of [[Memory paging|PO]] includes the last two bits. The figure above is just for illustration purposes only.

## What
The MMU is the device that helps to perform these operations upon [[Anatomy of the Beta CPU|CPU]] memory reference requests:
1. Extract `VPN` out of [[Virtual Address|VA]]
2. Find corresponding entry in the Pagetable
3. Extract the [[Memory paging|PPN]] if any
4. Perform necessary tasks (page-fault handling) if the entry is not resident
5. If [[Memory paging|PPN]] found, append [[Memory paging|PO]] to form a complete [[Memory Addressing|PA]]
6. Pass [[Memory Addressing|PA]] to other relevent units so [[Anatomy of the Beta CPU|CPU]] request can be completed

There are 3 other columns, `D`, `R` and `LRU` (if [[Replacement policy|LRU]] is the chosen [[Replacement policy]]) in the pagetable that contains [[Helper Bits]], analogous to the ones we learned in [[Cache]] before:
1. Resident bit / valid bit `R`:
	1. `R=1`, then requested content (`Mem[PA]`) is in [[Dynamic Random-Access Memory (DRAM)|physical memory]]. [[Memory paging|PPN]] in the pagetable can be returned immediately for further processing to result in a complete [[Memory Addressing|PA]]. 
	2. `R=0`: requested content is not in physical memory but in [[Hard Disk Drive (Disk)|disk]] swap space. **Page-fault exception** occurs and it has to be handled. 
2. Dirty bit `D`
	1. `D=1`: a write update of the data to the [[Solid-State Drive (SSD)|secondary storage]] has to be done before it is replaced/removed from the [[Dynamic Random-Access Memory (DRAM)|physical memory]]
3. The [[Replacement policy|LRU]] bit
	1. Present only if [[Replacement policy]] is [[Replacement policy|LRU]]
	2. Indicates the [[Replacement policy|LRU]] ordering of the pages resident in [[Dynamic Random-Access Memory (DRAM)|physical memory]]
	3. Number of [[Replacement policy|LRU]] bits needed per entry in the pagetable is $v$ bits, since the number of entries in the pagetable is $2^v$. We assume a vanilla, naive [[Replacement policy|LRU]] implementation here, although in practice various optimisation may be done. The LRU bits simply behaves as a *pointer* to the row *containing* the [[Replacement policy|LRU]] [[Memory paging|PPN]], therefore we need at least $v$ bits and not $\#PPN$ bits.

 ## Arithmetic
 Assume **byte addressing**.
 Given a [[Virtual Address|VA]] of $(v+p)$ bits and a [[Memory Addressing|PA]] of $(m+p)$ bits,
 - Size of [[Virtual Memory]]: $2^{v+p}$ bytes
 - Size of [[Dynamic Random-Access Memory (DRAM)|physical memory]]: $2^{m+p}$ bytes
 - Pagetable must store: $(2+m)\times 2^v$ bits ^5ea83f
	 - $2^v$ rows
		 - each has $m$ bits of [[Memory paging|PPN]], $2$ for `D` and `R`, $v$ for [[Replacement policy|LRU]] bits
		 - $v$ VPN bits are not exactly stored as entries in the pagetable, but used as indexing (addressing, e.g. using a [[Logic Synthesis#Decoder Demux|decoder]] to select exactly one pagetable row using $v$ bits as the selector to the decoder.)
		 - Note that the $v$ bits is often drawn as the first column of the Pagetable. This is to make computation easier, but they're actually used for *indexing* only,
	 - $2^p$ bytes per page.

## Location
> Pagetable is stored in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] for practical resons because of is huge ass size.

Costly to use [[Static Random-Access Memory (SRAM)|SRAM]] based memory device. The OS Kernel manages a portion of the [[Dynamic Random-Access Memory (DRAM)|physical memory]], dedicated to store the pagetable.

The MMU has a component called `Pagetable Pointer` which can be set to point to the first entry of the pagetable in the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

**Problem**: we need to access the slow [[Dynamic Random-Access Memory (DRAM)|physical memory]] twice.
1. Look up Pagetable to translate [[Virtual Address|VA]] to [[Memory Addressing|PA]].
2. Get content `Mem[PA]`

*Cheap solution costs performance.*

**Solution**
Build a small [[Static Random-Access Memory (SRAM)|SRAM]] based memory device to [[Cache]] a few of the most recently used entries of the pagetable. This is called the [[Translation Lookaside Buffer]].
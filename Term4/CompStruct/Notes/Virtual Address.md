---
aliases: VA
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]

When we open a program, the OS Kernel allocates a **dedicated virtual address space** for all its instructions (and data for execution) - spanning from low address `0` up to some high address.

Therefore, the addresses requested by the `PC` are actually **virtual addresses** (`VA`) instead of physical [[Memory Addressing|addresses]] (`PA`).

> Physical address (PA): actual addresses of each 32 bit word in the physical memory

Each `VA` has to be mapped to a `PA`, so that the system may return the requested data to the [[Anatomy of the Beta CPU|CPU]] upon instruction fetch (`LD`), or complete the executionof `ST` related instructions. This mapping is done via the **memory management unit** (MMU).
![](https://dropbox.com/s/s5mgxqim69a98o6/cpummu.png?raw=1)

> **MMU**:
> A small hardware unit where all memory references from the [[Anatomy of the Beta CPU|CPU]] is passed through itself, and its primary function is to translate from `VA` to `PA`.
> Refer to [[Pagetable]] for more information.

^7c1303

The [[Anatomy of the Beta CPU|CPU]] frequently makes memory references through instruction fetch from [[Anatomy of the Beta CPU|PC]], or LD and ST related instructions.

This arrangement allows each program to have the **same set of `VA`**.
e.g. its [[Anatomy of the Beta CPU|PC]] can always start from 0, but are in reality physically separate from one another
![](https://dropbox.com/s/1h5q5heph7vp3yy/detailVM.png?raw=1)

There are 2 concurrently running programs, process 1 and 2, each running in its [[Virtual Memory]]. The actual content of each VM may reside on [[Dynamic Random-Access Memory (DRAM)|physical memory]] or [[Hard Disk Drive (Disk)|disk]] swap space.

The processes themselves are not aware than their actual memory space are not contiguous and spans over 2 or more different storage hardware. The virtual addresses, however, are contiguous.

Reminder, only contents in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] has a physical address (PA).

Content on the disk swap space does not have a `PA`. If they are needed for access by the [[Anatomy of the Beta CPU|CPU]], the OS Kernel needs to migrate them over to the [[Dynamic Random-Access Memory (DRAM)|RAM]] first, so they have a corresponding `VA - PA` translation and are accessible by the [[Anatomy of the Beta CPU|CPU]]
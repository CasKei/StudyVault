---
aliases: page fault, page fault exception, replacing resident pages
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]

## What
> A method of [[Virtual Memory]] management.

The OS Kernel is responsible in the implementation of demand paging and it may vary from system to system.

> Main idea:
> Data is not copied from the swap space to the [[Dynamic Random-Access Memory (DRAM)|physical memory]] until they are needed or demanded by some program.

We ignore the presence of data [[Cache]] and [[Translation Lookaside Buffer|TLB]] for now, for simplicity.
- When program has just been opened, entire content is in swap space of [[Hard Disk Drive (Disk)|disk]].
- Pages will only be brought to [[Dynamic Random-Access Memory (DRAM)|physical memory]] if the program ocde asks for it.

When computer is turned off, every bit of information is stored in its non-volatile memory storage ([[Hard Disk Drive (Disk)|disk]], [[Solid-State Drive (SSD)|NAND flash]], etc).

The [[Dynamic Random-Access Memory (DRAM)|physical memory]] is incapable of storing any information when it does not receive power.

## OS Kernel
OS Kernel is one of the first programs that is loaded onto the [[Dynamic Random-Access Memory (DRAM)|physical memory]] when computer is started up. It maintains an organised **array of pages on [[Hard Disk Drive (Disk)|disk]]**.

==Bootstrap next term==: how to load the OS Kernel from [[Solid-State Drive (SSD)|secondary storage]] to the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

## How
The moment a request to open a program is made, the OS Kernel:
1. Allocates and prepares the *almost entire [[Virtual Memory]] space* for this program on [[Hard Disk Drive (Disk)|disk]] swap space
2. Copies contents required for execution over to this designated swap space from the storage part of the disk

Note:
- Only a small subset, essentially the program's entry point (elf table, main function, initial stack) is put into the [[Dynamic Random-Access Memory (DRAM)|physical memory]] and everything else is loaded later
- All instructions necessary for the program to run, its [[Stack and Procedures|stack]] space, heap space etc are nicely prepared by the OS Kernel before the program begins execution.

Therefore almost all [[Virtual Address|VA]] initially corresponds to some address on [[Hard Disk Drive (Disk)|disk]].

## Page-Fault Exception
Upon execution of the first few lines of instruction of the program’s entry point, the [[Anatomy of the Beta CPU|CPU]] will request to refer to some [[Virtual Address|VA]], and it will result in **page-fault** exception because almost all of its virtual addresses _aren’t resident_ in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] yet at this point.

The OS Kernel will handle this "missing" page and start copying them over to [[Dynamic Random-Access Memory (DRAM)|physical memory]] from the swap space, hence turning these pages **resident** and has a [[Memory paging|PPN]] assigned to it.

The kernel updates the corresponding entry of the [[Pagetable]] and the [[Translation Lookaside Buffer|TLB]].

Many page faults will occur as the program begins its execution until most of the working set of pages are in [[Dynamic Random-Access Memory (DRAM)|physical memory]] (not entire program as some may be way larger than your [[Dynamic Random-Access Memory (DRAM)|physical memory]].)

In other words, OS Kernel bring only the necessary pages that are going to be executed onto the [[Dynamic Random-Access Memory (DRAM)|physical memory]] as the program runs, thus the name [[Demand Paging]] for this technique.

## Replacing Resident Pages
This process of fetching new pages from swap space to [[Dynamic Random-Access Memory (DRAM)|physical memory]] eventually fills up the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

If a non-resident [[Virtual Address|VA]] is enquired and the [[Dynamic Random-Access Memory (DRAM)|physical memory]] is full, the OS Kernel needs to remove some pages ([[Replacement policy]] (LRU/FIFO)) that are currently resident to make space for this newly requested page.

If these to-be-removed pages are dirty, a write onto the [[Hard Disk Drive (Disk)|disk]] swap space is required before they are overwritten.

## Termination
When program terminates, OS Kernel frees up all space initially allocated for this program's [[Virtual Memory]] (both on [[Dynamic Random-Access Memory (DRAM)|physical memory]] and [[Hard Disk Drive (Disk)|disk]] swap space).

[[Termination of demand paging example]]
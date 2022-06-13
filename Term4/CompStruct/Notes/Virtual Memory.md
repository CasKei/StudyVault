---
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

# 50.005
## VM Implementation
The [[OS Kernel]] implements the Virtual Memory.
It has to:
- **Support [[Demand Paging]] protocol**
- **Keep track** of which parts of memory are currently being used and by whom
- **Decide** which processes and data to move into and out of memory
- **Mapping files** into process address space
- [[C dynamic memory allocation|Allocate and deallocate]] memory space as needed
	- If [[Dynamic Random-Access Memory (DRAM)|RAM]] full, migrate some contents (e.g. [[Replacement policy|LRU]]) onto swap space on [[Hard Disk Drive (Disk)|disk]].
- **Manage** the [[Pagetable]] and any operation associated with it.

> CPU [[Cache]]s are managed entirely by **hardware** (cache [[Replacement policy]], determining cache `HIT` or `MISS`, etc). Depending on the cache hardware, the [[OS Kernel]] may do some initial setup (caching policy to use, etc).


# 50.002
## Overview
> **Program**: a group of instructions made to carry out a specified task.

> **Process**: a program that is currently run, or a program in execution.

We can open and run the same program `N` times simultaneously, forming `N` distinct processes.

The [[Dynamic Random-Access Memory (DRAM)|physical memory]] can contain all kinds of [[Basics of Information|information]], and is typically segmented to run a single **process**.
![](https://dropbox.com/s/m1vg38rki9m5z1i/memimage.png?raw=1)
Lower addresses: `0` onwards: typically have executable instructions loaded there ([[Anatomy of the Beta CPU|PC]] starts from `0`).

[[Stack and Procedures|Stack]] can grow during runtime mainly due to recursion and creation of local variables.
[[Heap data structure]] grows upwards (towards lower addresses) and is used to store global variables. [external materials](http://www.enderunix.org/docs/memory.pdf)

Note: an OS may not know in advance whether stack or heap will be used predominantly before the program is actually run. Therefore, an OS must layout these 2 memory regions ina way to guarantee maximum space for both.

The illustration shows that a single [[Dynamic Random-Access Memory (DRAM)|physical memory]] is not enough to hold all information required to open too many programs at once.

We often open and run several programs simultaneouly.
When each of these programs are run, they are first **loaded** (copied) from [[Hard Disk Drive (Disk)|disk]] onto the [[Dynamic Random-Access Memory (DRAM)|physical memory]] before they can be accessed and executed by the [[Anatomy of the Beta CPU|CPU]]. The total space required to contain all the information needed to run these programs at the same time is definitely more than the typical size of [[Dynamic Random-Access Memory (DRAM)|physical memory]] in general-purpose computers.

Hence, we need to "borrow" some free space on the [[Hard Disk Drive (Disk)|disk]] that are not used to store data to store the **state** of **currently-run programs**. This is called the [[Hard Disk Drive (Disk)|disk]] **swap space** and it serves as an extension to out [[Dynamic Random-Access Memory (DRAM)|physical memory]].

> When `N` programs are open we do not use all at once, these are processes that are *idling* and *not currently in use*. ==These are the ones that are stored in the **swap space**.== They will be loaded to [[Dynamic Random-Access Memory (DRAM)|physical memory]] again when users resume their usage on the programs. The part of the computer system that is responsible for process management is the **Operating System Kernel**. We will learn more about it next term.


This motivates the idea of the **virtual memory**.

> **Virtual memory**:
> A **memory management technique** that provides an **abstraction** of the storage resources so that:
> 1. It is **easier** for `N` processes to share limited physical storage *without interfering with one another*
> 2. It gives the **illusion** to users of a very large physical memory space without being limited by *how much space is actually available* on the physical memory device.

In virtual memory, we use a part of the [[Hard Disk Drive (Disk)|disk]] as an extension to the [[Dynamic Random-Access Memory (DRAM)|physical memory]], and let programs work in the virtal address space instead of the physical (actual) addiress space. This is so that it is possible for *many programs to seemingly loaded onto the [[Dynamic Random-Access Memory (DRAM)|physical memory]] and run at the same time*, even when their total size exceeds the [[Dynamic Random-Access Memory (DRAM)|physical memory]] capacity.

## Memory Paging
Before we dive into how virtual memory works, this is an important concept to highlight.
[[Memory paging]]

## Virtual Memory
Reminder: programs are **loaded** to [[Dynamic Random-Access Memory (DRAM)|physical memory]] only when we **open/run** them, so that the [[Anatomy of the Beta CPU|CPU]] has direct access to its instructions for execution later on.

Majority of your installed programs that are not open/run stays on [[Hard Disk Drive (Disk)|disk]].

For ease of execution and security, the burden of process management is passed to a very special program: the OS Kernel.

Each process does not know the existence of another process and everything else that lives in [[Dynamic Random-Access Memory (DRAM)|physical memory]]. They don't have to keep track fo which addresses in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] is occupied or free to use, and one process won't be able to corrupt another.

==This provides a layer of [[Abstraction]], as the OS Kernel is the only program that needs to be carefully designed to perform good memory management.==

The rest of the processes in the computer can proceed *as if they are the only process running in the computer*.

This way we can say that each program has their own memory, that is the **virtual memory**.

> Recap: **virtual memory**
> a memory management technique that provides abstraction, in the sense that it allows the system to give each process an illusion that it is running on its own memory space isolated from other processes.

## Virtual Address
When we open a program, the OS Kernel allocates a **dedicated virtual address space** for all its instructions (and data for execution) - spanning from low address `0` up to some high address.

Therefore, the addresses requested by the `PC` are actually **virtual addresses** (`VA`) instead of physical [[Memory Addressing|addresses]] (`PA`).

[[Virtual Address]]

## Pagetable
Each `VA` has to be mapped to a `PA`, so that the system may return the requested data to the [[Anatomy of the Beta CPU|CPU]] upon instruction fetch (`LD`), or complete the executionof `ST` related instructions. This mapping is done via the **memory management unit** (MMU).

[[Pagetable]]

> Pagetable is stored in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] for practical resons because of is huge ass size.

Costly to use [[Static Random-Access Memory (SRAM)|SRAM]] based memory device. The OS Kernel manages a portion of the [[Dynamic Random-Access Memory (DRAM)|physical memory]], dedicated to store the pagetable.

The MMU has a component called `Pagetable Pointer` which can be set to point to the first entry of the pagetable in the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

**Problem**: we need to access the slow [[Dynamic Random-Access Memory (DRAM)|physical memory]] twice.
1. Look up Pagetable to translate [[Virtual Address|VA]] to [[Memory Addressing|PA]].
2. Get content `Mem[PA]`

*Cheap solution costs performance.*

**Solution**
Build a small [[Static Random-Access Memory (SRAM)|SRAM]] based memory device to [[Cache]] a few of the most recently used entries of the pagetable. This is called the [[Translation Lookaside Buffer]].

## Demand Paging
Demand paging is a method of virtual memory management. This section explains how _demand paging_ works.

- How
- Page fault exception
- Replacing resident pages
- Termination

[[Demand Paging]]

## Context Switch
[[Context switch]]

## Using Cache with VM
[[Use of cache with virtual memory]]
Assemble [[Cache]] before or after [[Pagetable|MMU]]?

## Summary
_Virtual Memory_ is a **memory management technique** that provides an **abstraction** of the storage resources so that programs can be written as if they have **full access** to the physical memory without having to consider where other programs reside .

A small hardware called the **MMU** is used to implement support this technique.

Since each program is running in an isolated manner from one another (in its own _virtual space_, unaware of the presence of other programs), the OS Kernel can switch execution between programs – giving the users an _illusion_ as if these programs are running **simultaneously** with just a single CPU. The procedure that allows for this to happen seamlessly is called **rapid context switching.**

Context switching allows for **timesharing** among several programs.

The OS Kernel simply loads the appropriate context number and pagetable pointer when switching among programs. This way, the CPU can have access to instructions or data required to execute each program and switch executions between program.

In the next chapter we will learn more about how the OS Kernel is specially privileged program is responsible of managing hardware resources in a system and scheduling processes to share these limited resources, thus allowing each process to run independently on its own [[Virtual Machine]].
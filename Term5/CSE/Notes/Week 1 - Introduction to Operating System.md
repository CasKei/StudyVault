---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

## Recap
[[Memory Hierarchy]]
[[Dynamic Random-Access Memory (DRAM)|RAM]]
[[Cache]]

## Kernel
[[Operating System]]
- [[OS Kernel]]
- [[Kernel mode and User mode|kernel mode]]
- [[Dual Mode Hardware Support]]

[[Computer System]]
- [[Device Driver]]
- [[Device Controller]]

[[Booting]] (not tested)

## Resource Allocator and Coordinator
[[Interrupt-Driven IO Operations]]
- [[Hardware Interrupt]]
	- [[Vectored Interrupt System]]
	- [[Polled Interrupt System]]
	- [[Scheduling multiple interrupts|Multiple interrupts]]
	- [[Raw device polling]]
	- [[Interrupt timeline]]
- [[Software Interrupt]]

[[Combining Hardware Interrupt and Trap]]

if not preemptive, scheduler will not yeet the process out of kernel mode if it aint done.
if not reentrant, p1 higher priority but cannot make system call while p0 is suspended in km

blocking: if no enter, it hang
non-blocking: always return

[[Re-entrancy]]
[[Preemption]]
- [[Strong, preemptive measure]]
- [[Weak, non-preemptive measure]]

[[Scheduling multiple interrupts|Multiple interrupts]]

[[Timed Interrupt]]
[[Exceptions]]

## Memory and Process Management
> The Kernel has to **manage** all memory devices in the system (disk, physical memory, cache) so that they can be shared among many other running user programs. The hierarchical storage structure requires a concrete form of memory management since the same data may appear in different levels of storage system.

### Memory
[[Memory Hierarchy]]
![[Pasted image 20220520185313.png]]
Storage systems organised in hierarchy: speed, cost, volatility.
#### Caching
Multitasking environments must be careful to use most recent value no matter where in storage hierarchy.
[[Multiprocessor System|Multiprocessor]] environment must provide cache *coherency* in hardware such that all CPUs have most recent value in their cache.
![[Pasted image 20220520193122.png]]


[[Virtual Memory]]
[[Pagetable|MMU]]
[[Cache]]

### Process
The Kernel is also responsible for managing all processes in the system and support **multiprogramming** and **timesharing** feature.
[[Multiprogramming]]
[[Timesharing]]
[[Process vs Program]]
[[Process Manager]]

## Providing Security and Protection
[[Kernel Security]]

## Summary
We have learned that the Operating System is a software that acts as an **intermediary** between a user of a computer and the computer hardware. It is comprised of the Kernel, system programs, and user programs. Each OS is shipped with different flavours of these programs, depending on its design.

In general, an operating system is made with the following goals in mind:

-   **Execute** user programs and make solving user problems easier
-   Make the computer system **convenient** to use
-   Use the computer hardware in an **efficient** manner

It is a huge piece of software, and usually are divided into separate subsystems based on their roles:

1.  Process Management
2.  Resource Allocator and Coordinator
3.  Memory and Storage Management
4.  I/O Management,

… and many others. There’s too many to count since modern OSes kept getting expanded to improve user experience.

The **Kernel** is the heart of the OS, the central part of it that holds important pieces of instructions that support the roles stated above in the bare minimum. In the next chapter, we will learn how to **access** crucial OS Kernel services.

## Appendix1: Multiprocessor System
[[Multiprocessor System]]
- [[Symmetric architecture]]
- [[Multi-core architecture]]
- [[Asymmetric multiprocessing]]

## Appendix2: Clustered System
[[Clustered system]]

---
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[Virtual Memory]]
[[50.005 Computer System Engineering|50.005]]


## What
A single core [[Anatomy of the Beta CPU|CPU]] is capable of running many programs seemingly at the same time. 

Actually, the [[Anatomy of the Beta CPU|CPU]] **switches** between the execution of the each program so rapidly  that it appears as if all programs are running on their own [[Anatomy of the Beta CPU|CPU]]. 

This technique is known as **rapid context switching**. 

> Context switch (50.005)
> The mechanism of **saving** the states of the current [[Week 4 - Processes and Thread management|process]] and **restoring** (loading) the state of a different process when switching the CPU to execute another process.

>  Context switch (50.002)
>  The procedure a [[Anatomy of the Beta CPU|CPU]] must follow when changing the execution of one process to another. 
>  This is done to ensure that the process can be restored and the program execution can be resumed again later. 

Proper hardware support to allow this is crucial for users to multitask when using the machine. 

## [[OS Kernel]] and [[Process table and Process control block|PCB]]
When a CPU switches execution between one process to another, the [[OS Kernel]] has to **store** all of the process states onto its corresponding [[Process table and Process control block|PCB]], and **load** the new process’ information from its PCB before resuming them as shown below, (_image screenshot from SGG book_):

![](https://natalieagus.github.io/50005/assets/images/week3/4.png)
There is ==time== spent between switching from process to process that both of them idle. This is called **context switch overhead**. This can be afforded if you have a fast CPU and give the illusion the process is running at the same time : [[Concurrent Programming|concurrency]].

## Benefits
> Gives the illusion of [[Concurrent Programming|concurrency]] in a uni-processor system
> - Improve system **responsiveness and interactability**, ultimately allowing [[Timesharing]] (users can interact with each program when it is running)
> - To support [[Multiprogramming]]: optimise CPU usage, cannot just let one program run all the time esp if that program *blocks* execution when waiting for IO (idle, have nothing important to do)

## Drawbacks
[[Context switch]] time is pure **overhead** because the system **does no useful work while switching**.

To minimise downtime due to overhead, context switch times are highly dependent on hardware support -- some hardware supports rapid context switching by having a *dedicated unit* for that (effectively bypassing the CPU)

## VS [[Kernel mode and User mode|mode switch]]
- Requires both saving states and loading states to resume execution
- Can be caused by either [[Timed Interrupt]] or [[System calls]] that leads to a `yield()`, e.g. when waiting for something

Some things require only [[Kernel mode and User mode|mode switch]] but not [[Context switch]]

## How
Each program has its own [[Virtual Memory]] to give the illusion that they each have their own independent [[Dynamic Random-Access Memory (DRAM)|physical memory]] for themselves. 

Therefore each program is written assuming it has access to all memory without considering other programs. 

To distinguish between one program's [[Virtual Address|VA]] address sspace from another, the OS Kernel assigns a unique identifier `C` called **context number** for each program. 

> Context: a set of mapping from [[Virtual Address|VA]] to [[Memory Addressing|PA]]. 

The context number can be appended to the requested VPN to find the it's correct [[Memory paging|PPN]] mapping:
- A [[Sequential Logic|register]] can be used (aadded to [[Pagetable|MMU]] to hold the current ccontext number `C`
- [[Translation Lookaside Buffer|TLB]] `TAG` field contains both `C`  and VPN
- If `MISS` [[Pagetable]] pointer is updated to point to beginning of the [[Pagetable]] section for context `C`, and the index based on VPN finds the corresponding entry.

![](https://dropbox.com/s/ckevn475pf7ar4s/mmuusagecontext.png?raw=1)

This way **we do not have to "flush" the [[Translation Lookaside Buffer|TLB]] whenever the [[Anatomy of the Beta CPU|CPU]] changes context** - that is *switching the execution of one program with another*.

It only needs to update the [[Pagetable]] pointer so that it points to the start of the [[Pagetable]] section for this new context.
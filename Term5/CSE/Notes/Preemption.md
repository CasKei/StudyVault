---
aliases: preemptive
tags:50.002, 50.005
---
[[Comp Struct|50.002]]
[[Scheduling multiple interrupts]]
[[Strong, preemptive measure]]
[[Weak, non-preemptive measure]]
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## Pre-emptive Kernel
> A pre-emptive [[OS Kernel]] **allows the scheduler** to **interrupt** processes in [[Kernel mode and User mode|kernel mode]] to execute the highest priority task that are ready to run, thus enabling kernel functions to be **interrupted** just like regular user functions. The CPU will be assigned to perform other tasks, from which it later returns to finish its kernel tasks. In other words, the scheduler is permitted to **forcibly** perform a [[Context switch]].

> Likewise, in a non-preemptive kernel the scheduler is not capable of rescheduling a task while its CPU is executing in the kernel mode.

## Example
In the example of Process 1 and 2 above, assume a scenario whereby there’s a periodic scheduler interrupt to check _which_ Process may resume next. Assume that Process 1 is in the middle of handling its `async_load` system call when the timer interrupts.

-   In a non-preemptive Kernel: If Process 1 does not voluntarily `yield` while it is still in the middle of its system call, then Process 2 will not be able to forcibly interrupt Process 1.
-   In a preemptive Kernel: When Process 2 is ready, and has a higher priority than Process 1, then the scheduler may **forcibly** suspend Process 1.

[[Worked example on scheduling policies]]

## [[Re-entrancy]] VS [[Preemption]]
A kernel can be reentrant but not preemptive: That is if each process voluntarily `yield` after some time while in the Kernel Mode, thus allowing other processes to progress and enter Kernel Mode as well. 

However, a kernel **cannot** be preemptive and not reentrant (it doesn’t make sense!).

Fun fact: Linux Kernel is reentrant and preemptive.


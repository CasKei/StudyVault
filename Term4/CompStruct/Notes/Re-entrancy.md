---
aliases: re-entrant
tags: 50.002, 50,005
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Multiplexing]]
[[Hardware Support for OS Multiplexing]]
[[50.005 Computer System Engineering|50.005]]

# 50.005
![[#^73ab1a]]
-   In a non-reentrant kernel: although it could be suspended in kernel mode, that would still **block** kernel mode execution on **all other processes**.
-   For example, consider Process 1 that is **voluntarily** paused (suspended) when it is in the middle of handling its `async_load` system call. It is **suspended in [[Kernel mode and User mode|kernel mode]]** by `yielding` itself.
    -   In a ==reentrant== kernel: Process 2 is currently executed; able to be handling its `print` system call as well.
    -   In a ==non-reentrant== kernel: Process 2, although currently executed must **wait** for Process 1 to exit from the Kernel Mode if Process 2 wishes to execute its `print` system call.

In simple [[Operating System]]s, incoming [[Hardware Interrupt]]s are typically **disabled** while another interrupt (of same or higher priority) is being processed to prevent a lost interrupt i.e: when user states are currently being saved before the actual interrupt [[Asynchronous Interrupt Handler|service routine]]  began or various ***reentrancy problems***[3](https://natalieagus.github.io/50005/os_notes/week1_resource#fn:4).

## [[Re-entrancy]] VS [[Preemption]]
A kernel can be reentrant but not preemptive: That is if each process voluntarily `yield` after some time while in the Kernel Mode, thus allowing other processes to progress and enter Kernel Mode as well. 

However, a kernel **cannot** be preemptive and not reentrant (it doesn’t make sense!).

Fun fact: Linux Kernel is reentrant and preemptive.

# 50.002
## What
> A _reentrant_ kernel is made such that it allows **multiple** processes (running in different cores) to be executing in the kernel mode _at any given point of time_ without causing any consistency problems among the kernel data structures. If a kernel is not re-entrant, a process can only be suspended *while it is in [[Kernel mode and User mode|user mode]]*.

^73ab1a

When the [[Anatomy of the Beta CPU|CPU]] is in [[Kernel mode and User mode|kernel mode]] (i.e. [[Asynchronous Interrupt Handler|handling an interrupt]], `PC31 == 1`), it is important to consider **whether or not we should allow interrupts to occur.**

> Interruptible handlers are called **re-entrant**.

In [[Building Beta CPU|beta CPU]], handlers are **not re-entrant**. Interrupts are *disabled* in [[Kernel mode and User mode|kernel mode]].

`IRQ` signal is ignored in [[Kernel mode and User mode|kernel mode]].
While user programs can be interrupted, kernel programs are not.

Reason: prevent kernel from corrupting itself.

Drawback: no way to get the system to work again if the kernel is buggy and runs into an infinite loop, except via hard reset. Kernel has to be written very carefully so as to not contain such bugs.

Consider the scenario where the interrupt handler is in the middle of saving program states. Allowing another interrupt to occur in the middle of a save might cause data corruption.

## Example
[[Example of basic kernel scheduler]]
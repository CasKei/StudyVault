---
aliases: re-entrant
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Multiplexing]]
[[Hardware Support for OS Multiplexing]]

## What
> A _reentrant_ kernel is made such that it allows multiple processes (running in different cores) to be executing in the kernel mode _at any given point of time_ without causing any consistency problems among the kernel data structures.

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
---
tags: 50.002
---
[[Comp Struct|50.002]]

## Overview
A single [[Anatomy of the Beta CPU|CPU]] can only do one thing at a time: execute an operation, load from one memory location, branch to another location, store to one memory location, attend to I/O requests (fetch input or write output to other devices), etc.

OS Kernel allows users to multitask, by performing rapid [[Context switch]]ing between processes, and giving each process the abstraction of being the only process running in its own isolated [[Virtual Machine]].

We can attach multiple I/O devices to a computer. ==Each runs independently of [[Anatomy of the Beta CPU|CPU]]. They are asynchronous and not controlled by [[Anatomy of the Beta CPU|CPU]].==
- Have own simple processing units (logic devices), and memory units to contain temporary data, e.g. input values such as mouse click or keyboard key presses - that will eventually be fetched by the [[Anatomy of the Beta CPU|CPU]].
- Typically orders of magnitude slower than [[Anatomy of the Beta CPU|CPU]] in operation and data processing.

In this chapter, we will learn how I/O requests are handled. The main idea for asynchronous I/O handling is follows:
-   Each process that requires usage of I/O devices will have to make a supervisor call. This **traps** to the Kernel mode, and the Kernel will handle this request.
-   Each I/O devices will invoke an (asynchronous) **interrupt request** when there’s data in it that has to be fetched (mouse click, keyboard touch, touch screen input, incoming fax, etc). Whenever possible, the execution of the running process will be paused, and the Kernel will tend to this request.

Upon completion (of either case), the Kernel will return control (of CPU) to the originating process (_resume the process_).

## Recap: OS Kernel
[[OS Kernel]]

## The Supervisor Call
[[Supervisor Call]]

## Asynchronous Input Handling
[[Asynchronous Input Handling]]

## Real-Time I/O Handling
[[Real-Time IO Handling]]

## Scheduling multiple interrupts
[[Scheduling multiple interrupts]]

## Effective Interrupt Load
[[Effective Interrupt Load]]

## Summary
In this chapter, we have learned that there are two parts of _device interface_:
1.  **Device side:** via asynchronous interrupt requests.
2.  **Application (process) side:** via supervisor calls.

The OS Kernel acts as an intermediary between processes and shared hardware.

It has to carefully schedule real-time interrupt requests such that each can be serviced without violating the deadlines. We learned a couple of policies: weak non-preemptive and strong pre-emptive measure. Real-time constraints are however complex to solve, and each policies have its own pros and cons. It is also not a trivial job to determine the best priority ordering for each device or handler.

We have come to the end of this course, and we have learned quite a great deal on how a computer is built, what it means by having a “general-purpose” device and how to design an instruction set for it, along with memory and machine virtualisation. The OS Kernel is a program that enables machine abstraction; in a way such that each process can run in isolation from one another (great for both convenience in development and system security).

In the next term, we will build on this knowledge and learn more about the fuller extent of the role of an OS Kernel: supporting interprocesses communcation, synchronizing between processes, and guarding shared resources between processes running in the system.
---
tags: 50.002
---
[[Comp Struct|50.002]]

## Overview
There are multiple processes running.
There has to be some manager program that oversees the execution of htese processes as we only have limited resources (CPU cores, RAM size, cache size, etc.).
This manager program is called the **Operating System**.

The part of the OS that is responsible for process management is the OS Kernel.

## OS Kernel
[[OS Kernel]]
OS Kernel is a special program written to manage and oversee the execution of all other processes in system.

Has highest privilege in computer system: can terminate any program, has access to all kinds of hardware.

Important role in memory management, I/O handling, process scheduling.

More next term.

## A Complete Process Context
[[Complete Process Context]]

## Building a Virtual Machine
[[Kernel mode and User mode]]

## OS Multiplexing and Context Switching
[[Context switch]]
[[Multiplexing]]

## Hardware Support for OS Multiplexing
[[Hardware Support for OS Multiplexing]]
- [[Beta Asynchronous Interrupt Hardware]]
- [[Asynchronous Interrupt Handler]]
- [[Dual Mode Hardware Support]]
- [[Re-entrancy]]
- [[Example of basic kernel scheduler]]

## Trap
[[Trap]]

## Summary
In summary, we have learned how the presence of OS Kernel and hardware support provide an abstraction for each running process, thus allowing them to run in an isolated manner; on their own virtual machine.

The Kernel **manages** the execution of all processes, as well as all I/O devices, and provides **services** to all these processes. There are two ways to transfer CPU control between user programs to kernel programs:

-   Firstly, is through **asynchronous interrupt**: `IRQ` is set to `1`
-   Secondly, is through **s ynchronous interrupt**: when the process generates an **exception** hence **trapping** itself to the handler and enters Kernel mode.

During either case of interrupt, `PC+4` is stored at `Reg[XP]` so that the system knows how to resume the process later on.

In β\betaβ ISA, the Kernel is **non-preemptive** (the CPU cannot be interrupted while in Kernel Mode). It is designed as such to prevent security breach, data loss if it traps into itself while still being in the Kernel Mode, etc. However, careful writing and construction of the Kernel program is required.
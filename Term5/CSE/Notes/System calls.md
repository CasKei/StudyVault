---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]

## System Calls
Besides using the GUI, we can access [[OS Services]] using its programming interface (system calls), meaning that we **develop** our own programs that rely on OS services to utilise the computer system’s hardware and I/O devices.

> System calls are programming interfaces provided by the [[OS Kernel]] for users to access kernel services. Unlike I/O interrupts, system calls are [[Software Interrupt|software]] generated interrupts (trap instruction).

When application programs make system calls, the execution of its original instruction is temporarily suspended and switches to the [[Kernel mode and User mode|kernel mode]] to execute the system call routine. System calls are one of the **controlled** ==entry points to the kernel== (besides interrupts and reset), meaning that we cannot make our program such that our `PC` directly executes arbitrary parts of the kernel space. ==System calls are the only way for user-mode processes to change into kernel-mode processes via software instructions.==

This is usually supported by :

1.  **Hardware**, e.g.: PC cannot perform `JMP` to code with raw RAM addresses starting with MSB of ‘1’: [[Dual Mode Hardware Support]]
2.  **Virtualisation**, user programs operate on virtual memory: [[Virtualisation]]

System calls are mostly accessed by programs through **APIs** (application program interface) [[System call via API]], although we can certainly make system calls directly in assembly. There are plenty of examples in the next few sections.

> A system call does **NOT** generally require a **full** [[Context switch]]; instead, it is processed in the context of whichever process invoked it.

![[Pasted image 20220530121344.png]]

## Accessing System Calls
[[Accessing system calls]]

## System Call via API
[[System call via API]]

## System call implementation
[[System call implementation]]

## Types of system calls
[[Types of system calls]]


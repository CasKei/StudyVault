---
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Virtual Machine]]
[[Asynchronous Handling of IO Devices]]

# 50.005
## Contains
1. Vector IRQ [[Vectored Interrupt System]]
2. Prepare instructions
3. Handlers for IO ([[Supervisor Call|SVC]], IRQ) [[Interrupt-Driven IO Operations]]
4. Scheduler ([[Asynchronous Interrupt Handler|process table]], scheduling handler)
5. [[Device Driver]]s

## Entry
1. IRQ (async) [[Interrupt-Driven IO Operations]]
2. SVC (software/trap) [[Supervisor Call|SVC]] [[Software Interrupt]] [[Trap]]
3. Reset
4. Exception [[Exceptions]]

## Whaddis
The one **program** that is running at all times in the computer is the kernel.
The Kernel is the **heart** of an operating system.

- Operates on **physical space**: has full knowledge on all[[Memory Addressing|physical addresses]] instead of [[Virtual Address]]es, and has complete privilege over all hardware of the [[Computer System]].
- Only way to access kernel code is when a process runs in [[Kernel mode and User mode|kernel mode]], via specific controlled entry points (`ILLOP`, `IRQ`, `RESET`).

Tis unique.
- Special priviledges
- **Hardware support** required
	- at least [[Dual Mode Hardware Support]], maybe [[Hardware Support for OS Multiplexing]]
	- **System calls** let (unprivileged, untrusted user programs) access kernel services (privileged, trusted)

## Roles
There are several purposes of an operating system: as a **resource** allocator, **controls** program execution, and guarantees **security** in the computer system. The next few notes will touch on each of these topics.

## Providing security and protection
[[Kernel Security]]

## Kernel mode
[[Kernel mode and User mode|kernel mode]]
[[Dual Mode Hardware Support]]

## Resource allocator and coordinator
The kernel **controls** and **coordinates** the use of hardware and I/O devices among various user applications. Examples of I/O devices include mouse, keyboard, graphics card, disk, network cards, among many others.
### Interrupts and Traps
[[Interrupt-Driven IO Operations]]
- [[Hardware Interrupt]]
- [[Software Interrupt]]
- [[Combining Hardware Interrupt and Trap]]

[[Re-entrancy]], [[Preemption]]
[[Timed Interrupt]], [[Exceptions]]
### Memory management
[[Virtual Memory]]
[[Pagetable|MMU]]
[[Cache]]
### Process management
[[Multiprogramming]]
[[Timesharing]]
[[Process vs Program]]
[[Process Manager]]
### Kernel is not a process!
It is easy to perhaps **misunderstand** that the kernel is a process.
The kernel is **not** a process in itself (albeit there are kernel _threads_, which runs in kernel mode from the beginning until the end, but this is _highly specific, e.g: in Solaris OS_).
For instance, I/O handlers are not processes. They do not have **context** (state of execution in registers, stack data, heap, etc) like normal processes do. They are simply a piece of **instructions** that is written to **handle** certain events.

You can think of a the kernel instead as made up of just :
-   Instructions, data:
    -   Parts of the kernel deal with memory management, parts of it with scheduling portions of itself (like drivers, etc.), and parts of it with scheduling processes.
-   Much like a state-machine that user-mode processes executes to complete a particular **service** and then return to its own instruction
    -   User processes running the kernel code will have its mode changed to [[Kernel mode and User mode|kernel mode]]
    -   Once it returns from the handler, its mode is changed back to [[Kernel mode and User mode|user mode]]

Hence, the statement that the **kernel is a program that is running at all times** is technically true because the kernel **IS** **part of each process**. Any process may switch itself into Kernel Mode and perform system call routines (software interrupt), or forcibly switched to Kernel Mode in the event of hardware interrupt.

The Kernel **piggybacks** on any process in the system to run.

If there are no system calls made, and no hardware interrupts, the kernel does nothing at this instant since it is not entered, and there’s nothing for it to do.

# 50.002
## 50.002 : Virtual Machine
OS Kernel is a special program written to manage and oversee the execution of all other processes in system.

Has highest privilege in computer system: can terminate any program, has access to all kinds of hardware.

Important role in memory management, I/O handling, process scheduling.

## 50.002 : Async Handling of I/O
The Kernel (the core of an OS) is a **set of instructions** that lives in the "kernel space" of the [[Dynamic Random-Access Memory (DRAM)|physical memory]], and it manages the execution of all apps in the computer, as well as the hardware (including the I/O).

Note that the Kernel **is not** the entire OS. There are other parts of an OS (that is not run in [[Kernel mode and User mode|kernel mode]]), and we will learn more about these other parts of the OS next semester.

Kernel serves as an **intermediary** between any I/O devices and user processes. It provides a level of [[Abstraction]] such that programs can be written and run as if it has access to the entire machine to itself.
![](https://dropbox.com/s/5p53t1w1towhslg/osview.png?raw=1)


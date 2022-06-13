---
aliases: 
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Virtual Machine]]
[[Multiplexing]]
[[Kernel mode and User mode|dual mode]]
[[Hardware Support for OS Multiplexing]]

# 50.005
![](https://natalieagus.github.io/50005/assets/images/week1/4.png)

The dual mode is possible **iff** it is supported by the hardware. The kernel is also **uninterruptible** and this interruptible feature is also supported by the hardware.

## Differences between architectures
In [[Comp Struct|50.002]] we leaned that the [[Anatomy of the Beta CPU|control logic unit]] prevents the [[Anatomy of the Beta CPU|PC]] to `JMP` to [[Memory Addressing|memory address]] with MSB of `1` when it is at memory address with MSB `0`.

Also it does not [[Trap]] the [[Anatomy of the Beta CPU|PC]] onto the handler when an interrupt signal is present if the [[Anatomy of the Beta CPU|PC]] is running in [[Kernel mode and User mode|kernel mode]].

In Linux, low memory given to kernel, high memory to user. Hardware prevents PC from jumping *illegally* (not via handlers) to a lower memory address.

## Overall of dual mode
[[Kernel mode and User mode|dual mode]]
A general purpose CPU has at least dual mode operation that should supported by its hardware:

1.  ****The Kernel mode**** (privileged) : the executing code has complete and unrestricted access to the underlying hardware.
2.  ****The User mode**** (unprivileged) : all user programs such as a web browser, word editor, etc and also system programs such as compiler, assembler, file explorer, etc. Runs on _virtual machine_

User programs have to perform **system calls** (supervisor call [[Supervisor Call|SVC]]) when they require services from the kernel, such as access to the hardware or I/O devices. When they perform **system calls**, the user program changes its mode to **the kernel mode** and began executing the kernel instructions handling that call instead of their own program instructions. When the system call returns, the `PC` resumes the execution of the user program.

# 50.002
## Why
The OS Kernel is a program that manages the execution of all other processes in the system. So it is **crucial to restrict access to the Kernel for safety reasons**.

That is, to prevent a normal program from jumping to the address in memory that contains Kernel code and "hack" the system.

This prevention is done via hardware.

## Notation
MSB (most significant bit) of the [[Anatomy of the Beta CPU|PC]] register: **Supervisor bit**.

If [[Anatomy of the Beta CPU|PC]] executes any code where PC register MSB is 1, it is in [[Kernel mode and User mode|kernel mode]], if 0 then [[Kernel mode and User mode|user mode]].

So we can divide [[Dynamic Random-Access Memory (DRAM)|physical memory]] address spce into 2 sections:
- **User space:** from `0x0000 0000` to `0x7FFF FFFF`
- **Kernel space:** from `0x8000 0000` to `0xFFFF FFFF`.

Kernel program and kernel data (privileged infromation, data structures etc) are stored in Kernel space. The rest of the program in the system live in the user space.

## How
With the notation, it is easy to enforce restricted access to the kernel space.

Programs in [[Kernel mode and User mode|user mode]] (`PC31 == 0`) 
- Cannot branch or jump to instructions in the kernel space.
	- Computations of next instruction address in `BEQ`, `BNE`, and `JMP` cannot change `PC31` value from `0` to `1`.
- Cannot load/store data from/to kernel space
	- Computations of addresses in `LD`, `LDR` and `ST` ignores the MSB.

Entry to [[Kernel mode and User mode|kernel mode]] can only be done via restricted entry points. In [[Building Beta CPU|beta CPU]], there are only 3 entry points:
-   Interrupts (setting PC to `Xaddr: 0x8000 0008`),
-   Illegal operations (setting PC to `ILLOP: 0x8000 0004`), or
-   Reset (setting PC to `RESET: 0x8000 0000`)

## Example
[[Example of basic kernel scheduler]]
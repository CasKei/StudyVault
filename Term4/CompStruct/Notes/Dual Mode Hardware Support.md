---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Multiplexing]]
[[Kernel mode and User mode|dual mode]]
[[Hardware Support for OS Multiplexing]]

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
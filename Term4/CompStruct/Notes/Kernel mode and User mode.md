---
aliases: dual mode, dual mode system, kernel mode, user mode, mode switch
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Virtual Machine]]

# 50.005
[[OS Kernel]] runs with special privileges. Can do what normal user programs cannot:
1. Ultimate access and control to all hardware in [[Computer System]]
2. Know and lives in [[Memory Addressing|physical address]] space and manage [[Memory Hierarchy]]
3. Interrupt other user programs
4. Manage other user program locations on [[Dynamic Random-Access Memory (DRAM)|RAM]], [[Pagetable|MMU]], and [[Example of basic kernel scheduler|schedule]] user program executions

Must support dual mode operation

## Hardware Support
[[Dual Mode Hardware Support]]

## Mode switching
- The **privilege** of a [[Week 4 - Processes and Thread management|process]] changes.
- Singply escalates privilege from [[Kernel mode and User mode|user mode]] to [[Kernel mode and User mode|kernel mode]] to access kernel [[OS Services]]
- Done by:
	- [[Hardware Interrupt]]
	- [[System calls]] ([[Software Interrupt|trap]])
	- [[Exceptions]]
	- [[CPU reset]]

Mode switch MAY NOT ALWAYS LEAD TO [[Context switch]]. Depending on implementation, Kernel code decides whether or not it is necessary.

# 50.002
## Overview
To support a safe [[Virtual Machine]] for each process, we need to establish the notion of *dual mode system*, that is a system that has a **Kernel mode** (privileged mode) and a **User mode** (non-privileged mode).

The Kernel will **handle** the need of these programs running in user mode for access to various hardware resources: access to I/O devices, interprocess communication, allocation/deallocation of shared memory space, etc.

This is a **major benefit**: programs can be easily written as if they have _absolute_ access to _all_ hardware resources (not just the physical memory), without having to worry about sharing them with other running processes.

## Kernel Mode
The OS Kernel runs in full privilege mode.
Oversees the execution of all processes in the computer system, handles real I/O devices, and emulate virual I/O device for each process.

## User Mode
All other programs do not have such privileged features.
- No direct access to actual hardware
- No direct access to other process' address space
- No knowlesge about other processes' context and processor state

## Hardware support
[[Dual Mode Hardware Support]]
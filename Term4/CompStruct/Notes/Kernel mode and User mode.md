---
aliases: dual mode, dual mode system, kernel mode, user mode
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]

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
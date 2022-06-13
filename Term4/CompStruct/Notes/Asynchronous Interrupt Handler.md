---
aliases: process table, service routine, interrupt handler
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Virtual Machine]]
[[Multiplexing]]
[[Hardware Support for OS Multiplexing]]
[[Hardware Interrupt]]

# 50.005
[[Operating System|OS]] preserves state of CPU by storing registers and PC.

Determines which type of interrupt has occured:
- [[Polled Interrupt System|polling]]
- [[Vectored Interrupt System]]

Separate segments of code determine what action should be taken for each type of interrupt

[[Asynchronous Interrupt Handler|Interrupt handling]] is done in [[Kernel mode and User mode|kernel mode]] by the service routine ([[Asynchronous Interrupt Handler|interrupt handler]])

[[Process table and Process control block]]
![](https://natalieagus.github.io/50005/assets/images/week3/3.png)

# 50.002
## What
The asynchronous interrupt handler is located at `XAddr`, which is usually a predetermined [[Memory Addressing|memory address]].

In [[Building Beta CPU|beta CPU]], `XAddr` is set at `0x8000 0008`.

## Process table
A Kernel [[Data Types and Data Structures|data structure]] that stores all the states of running processes in the machine.

Lives in the Kernel memory space.

Kernel keeps track on which process is currently scheduled to run in the [[Anatomy of the Beta CPU|CPU]].
![[xfxywyzk.bmp]]

## How
### 1: save
The first few instructions of the interrupt handler saves **current process states** in the process table.
- `R0` to `R30` contents
- [[Anatomy of the Beta CPU|PC]] state
- [[Stack and Procedures|Stack]] state
- etc

### 2: call service routine (scheduler)
Then the handler will figure out which specific **service routine** needs to be called to service the interrupt, e.g. scheduler or I/O routines.

### 3: return to handler
Afterwards, the service routine returns back to this interrupt handler.
The handler finally sets `PC <- Reg[XP] - 4`.
The value of this depends. The **service routine** may or may not change the value of `Reg[XP]` before returning to the interrupt handler.
- If value of `Reg[XP]` is unchanged, then the interrupted program resumes
- Otherwise, it means that the [[Anatomy of the Beta CPU|CPU]] executes another program.

In any case, `Reg[XP]-4` contains the address of instruction that the CPU should execute when the interrupt handler returns.
---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## Overview
Interrupt-Driven I/O operations allow the CPU to efficiently handle interrupts without having to waste resources; waiting for asynchronous interrupts. This notes explains how interrupt-driven I/O operations work in a nutshell. There are **two kinds of interrupts**:

1.  [[Hardware Interrupt]]: input from external devices activates the interrupt-request-line, thus pausing the current execution of user programs.
2.  [[Software Interrupt]]: a software generated interrupt that is invoked from the instruction itself because the current execution of user program needs to access Kernel services.

## More about interrupts
Interrupt transfers control to the interrupt service routine, generally, trhough the **interrupt [[Vectored Interrupt System|vector]]**, which contains the addresses of all the service reoutines.

Interrupt architecture must save teh address of the interrupted instruction.

**Incoming interrupts are disabled** while another interrupt of same or higher priority is being processed to prevent a *lost interrupt* or [[Re-entrancy]] problems.

A [[Trap]] is a [[Software Interrupt|Software-generated interrupt]] caused either by error or a request by user code,
Latter allows a user program to invole an [[Operating System|OS]] function (system call) and run it on [[Kernel mode and User mode|kernel mode]]. Hence, entry points into [[OS Kernel]] are carefully controlled.

Modern [[Operating System|OS]] are **interrupt-driven**.

## Interrupt Handling
[[Operating System|OS]] preserves state of CPU by storing registers and PC.

Determines which type of interrupt has occured:
- [[Polled Interrupt System]]
- [[Vectored Interrupt System]]

Separate segments of code determine what action should be taken for each type of interrupt

[[Asynchronous Interrupt Handler|Interrupt handling]] is done in [[Kernel mode and User mode|kernel mode]] by the service routine ([[Asynchronous Interrupt Handler|interrupt handler]])

## Interrupt timeline
[[Interrupt timeline]]
- [[Interrupt timeline#Receiving asynchronous input|Receiving asynchronous input]]
- [[Interrupt timeline#Consuming the input|Consuming the input]]





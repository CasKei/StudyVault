---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]

## Overview
CPU has a **interrupt-request line** that is sense by [[Anatomy of the Beta CPU|control unit]] before each instruction execution.

Upon the presence of new **input**: from **external** events such as keyboard press, mouse click, mouse movement, incoming fax, or **completion of previous I/O requests** made by the drivers on **behalf** of user processes, the device controllers will invoke an **interrupt** request by setting the **bit** on this **interrupt-request line**.

Remember that this is a **hardware interrupt**: an interrupt that is caused by setting the interrupt-request line.

## Interrupt handler
This forces the CPU to **transfer** control to the [[Asynchronous Interrupt Handler|interrupt handler]]. This switch the currently running user-program to enter the [[Kernel mode and User mode|kernel mode]]. The interrupt handler will do the following routine:
1.  **Save** the *register states* first (the interrupted program instruction) into the process table
2.  And then transferring control to the appropriate interrupt service routine — depending on the device controller that made the request.

## Interrupt systems
[[Vectored Interrupt System]]
[[Polled Interrupt System]]

[[Scheduling multiple interrupts|Multiple interrupts]]

## Raw device polling
[[Raw device polling]]

## Timeline
[[Interrupt timeline]]

## Combining [[Hardware Interrupt]] and [[Software Interrupt|trap]]
[[Combining Hardware Interrupt and Trap]]
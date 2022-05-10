---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Multiplexing]]

## Overview
To allow for proper [[Multiplexing]], 4 things must be supported in hardware:
1. A way to **asynchronously interrupt** a currently running program *periodically* via hardware, since that program is currently using the [[Anatomy of the Beta CPU|CPU]] and will not stop voluntarily.
2. Hardware has to know **how to direct** the [[Anatomy of the Beta CPU|PC]] [[Anatomy of the Beta CPU|CPU]] to the right handler program when **interrupt** occurs
3. [[Kernel mode and User mode|dual mode]] in system
4. Other interrupts must be disabled when this process of "saving state" occurs (otherwise data will be lost)

## Beta Asynchronous Interrupt Hardware
[[Beta Asynchronous Interrupt Hardware]]

## Asynchronous Interrupt Handler
[[Asynchronous Interrupt Handler]]
The asynchronous interrupt handler is located at 

## Dual Mode Hardware Support
[[Dual Mode Hardware Support]]

## Reentrancy
[[Re-entrancy]]

## Example
[[Example of basic kernel scheduler]]
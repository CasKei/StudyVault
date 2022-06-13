---
aliases: exception
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## What
> Exceptions are [[Software Interrupt]] that occur due to **errors** in the instruction: such as division by zero, invalid memory accesses, or attempts to access [[OS Kernel]] space illegally. 

This means that the CPU’s hardware may be designed such that it checks for the presence of these **serious** errors, and immediately invokes the appropriate handler via a pre-built **event-vector table**. Below is an example of ARMv8-M event vector table. The table is typically implemented in the **lower** physical addresses in many architecture.
![](https://natalieagus.github.io/50005/assets/images/week1/13.png "Image taken from https://developer.arm.com/documentation/100701/0200/Exception-properties")

Each exception has an ID (associated number), a vector **address** that is the exception **entry** point in memory, and a **priority** level which determines the order in which multiple pending exceptions are handled. In ARMv8-M, the lower the priority number, the higher the priority level.

**You don’t have to memorise these, don’t worry.**
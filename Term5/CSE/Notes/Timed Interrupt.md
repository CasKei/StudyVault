---
aliases: timer interrupt
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]

## Why
We must ensure the [[OS Kernel]], as a **resource allocator**, maintains *control* over the CPU.

We cannot allow a user program to get stuck in an infinite loop and never return control to the [[Operating System|OS]].

We also cannot trust a user program to voluntarily return control to the [[Operating System|OS]].

To ensure that no user program can occupy a CPU for indefinitely, a computer system comes with a (**hardware**)-based timer.

A timer can be set to invoke the [[Hardware Interrupt]] line so that a running user program may transfer control to the kernel after a specified period. Typically, a **scheduler** will be invoked each time the timer interrupt occurs.

## Hardware support
In the hardware, a timer is generally implemented by a **fixed-rate clock** and a counter. The kernel may set the starting value of the counter, just like how you implement a custom clock in your 1D 50.002 project, for instance:

-   Every time the sytem clock ticks, the counter is decremented.
-   When the counter reaches 0, the timer raises the **interrupt request line**
    -   For instance, a 10-bit counter with a 1-millisecond clock can be set to trigger interrupts at intervals anywhere from 1 millisecond to 1,024 milliseconds, in steps of 1 millisecond.
-   This transfers control over to the interrupt handler:
    -   **Save** the current program’s state
    -   Then call the **scheduler** to perform context switching
    -   The scheduler may then reset the counter before restoring the next process to be executed in the CPU. This ensures that a proper timed interrupt can occur in the future.
        -   Note that a scheduler may allocate **arbitrary** amount of time for a process to run, e.g: a process may be allocated a longer time slot than the other. We will learn more about process management in Week 3.


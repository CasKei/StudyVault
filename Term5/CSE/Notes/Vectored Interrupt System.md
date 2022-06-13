---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]
[[Hardware Interrupt]]

## Vectored interrupt system
Interrupt-driven system may use a **vectored interrupt system**:

> the interrupt signal that **INCLUDES** the identity of the device sending the interrupt signal, hence allowing the kernel to know exactly which interrupt service routine to execute. 

> This is more **complex** to implement, but more **useful** when there are sparse I/O requests.

Since only a predefined number of interrupts is possible, **a table of pointers to interrupt routines** can be used instead to provide the necessary speed. The interrupt routine is called indirectly through the table, with no intermediate routine needed. Generally, the table of pointers is stored in low memory (the first hundred or so locations), and its values are determined at boot time. These locations hold the addresses of the interrupt service routines for the various devices. This array, or **interrupt vector**, of addresses is then indexed by a unique device number, given with the interrupt request, to provide the address of the interrupt service routine for the interrupting device. Operating systems as different as Windows and UNIX dispatch interrupts in this manner.

> This interrupt mechanism accepts an **address**, which is usually one of a small set of numbers for an offset into a table called the **interrupt vector.** This table holds the addresses of routines prepared to process specific interrupts.
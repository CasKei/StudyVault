---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]
[[Hardware Interrupt]]

-   The interrupted program enters a general interrupt polling routine **protocol**, where CPU **scans** (polls) devices to determine which device made a service request.
-   Unlike [[Vectored Interrupt System]], there’s no such _interrupt_ signal that includes the identity of the device sending the interrupt signal.
-   In the polled system, the kernel must send a signal out to each controller to **determine** if any device made a service request **periodically, or at any fixed interval**.

This is simpler to implement, but more time-wasting if there’s sparse I/O requests. Does Linux implement a Polled interrupt or Vectored interrupt system? See [here](https://linux-kernel-labs.github.io/refs/heads/master/lectures/interrupts.html) for clues.
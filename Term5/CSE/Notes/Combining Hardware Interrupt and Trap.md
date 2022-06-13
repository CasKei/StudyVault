---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]

## Combining [[Hardware Interrupt]] and [[Software Interrupt|trap]]
Consider another scenario where you want to open a **very large file** from disk. It takes some time to **load** (simply transfer your data from disk to the disk controller), and your CPU can proceed to do other tasks in the meantime. Here’s a simplified timeline:

![](https://natalieagus.github.io/50005/assets/images/week1/12.png)

Imagine that at first, the CPU is busy executing process instructions in user mode. At the same time, the device is idling.

1.  The process requests for Kernel services (e.g: load data asynchronously) by making a **system call**.
    -   The register state (context) of the process are saved by the trap handler
    -   Then, the appropriate system call service routine is called. Here, they may require to load appropriate **device drivers** so that the CPU may communicate with the device controller.
2.  The **device controller** then makes the instructed I/O request to the device itself on behalf of the CPU, **e.g: a disk,** as instructed.
    -   Meanwhile, the service handler returns and may resume the calling process as illustrated.

> The I/O device then proceeds on responding to the request and **transfers** the data from the **device** to the **local buffer** of the device controller.

When I/O transfer is **complete**, the device controller makes an **hardware interrupt** request to signal that the transfer is done (and data needs to be fetched). The CPU may respond to it by saving the states of the currently interrupted process, handle the interrupt, and resume the execution of the interrupted process.

Note:

1.  [[Supervisor Call|SVC]] **delay** and IRQ **delay**: time elapsed between when the request is invoked until when the request is first executed by the CPU.
2.  Before the user program is resumed, its state must be **restored**. Saving of state during the switch between User to Kernel mode is implied although it is not drawn.
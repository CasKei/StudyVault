---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[OS structures]]

## Monolithic Structure
A monolithic kernel is an operating system architecture where the entire [[Operating System]] is working in kernel space. It can operate **with** or **without** [[Kernel mode and User mode|dual mode]].

## Without Dual Mode
[[Single-tasking system|MS-DOS]]

The figure below (screenshot from SGG book) shows the structure of MS-DOS, one of the **simplest** OS made in the early years:

-   The interfaces and levels of functionality are **not well separated** (**all** programs can access the hardware) - i.e: at the time, MS-DOS was written for the Intel 8088 architecture, which has no mode bit and therefore no dual mode.
-   For instance, application programs are able to access the basic I/O routines to write directly to the display and disk drives.
-   Such freedom leaves MS-DOS **vulnerable** to errant (or malicious) programs, causing entire system crashes when user programs fail.

![](https://natalieagus.github.io/50005/assets/images/week2/8.png)

## With Dual Mode
The early UNIX OS was also simple in its form as shown below. In a way, it is layered to a **minimal** extent with very simple structuring.

![](https://natalieagus.github.io/50005/assets/images/week2/9.png)

The kernel provides file system management, CPU scheduling, memory management, and other operating-system functions through system calls. That is an **enormous** amount of functionality to be combined into one level.

-   **Pros**: distinct **performance advantage** because there is very little overhead in the system call interface or in communication within the kernel.
-   **Cons**: difficult to implement and maintain.

Other examples of monolithic OS with dual-mode: BSD, Solaris
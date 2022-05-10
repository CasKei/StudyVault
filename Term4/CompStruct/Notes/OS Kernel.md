---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Asynchronous Handling of IO Devices]]

## 50.002 : Virtual Machine
OS Kernel is a special program written to manage and oversee the execution of all other processes in system.

Has highest privilege in computer system: can terminate any program, has access to all kinds of hardware.

Important role in memory management, I/O handling, process scheduling.

## 50.002 : Async Handling of I/O
The Kernel (the core of an OS) is a **set of instructions** that lives in the "kernel space" of the [[Dynamic Random-Access Memory (DRAM)|physical memory]], and it manages the execution of all apps in the computer, as well as the hardware (including the I/O).

Note that the Kernel **is not** the entire OS. There are other parts of an OS (that is not run in [[Kernel mode and User mode|kernel mode]]), and we will learn more about these other parts of the OS next semester.

Kernel serves as an **intermediary** between any I/O devices and user processes. It provides a level of [[Abstraction]] such thta programs can be written and run as if it has access to the entire machine to itself.
![](https://dropbox.com/s/5p53t1w1towhslg/osview.png?raw=1)


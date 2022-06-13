---
aliases: manage processes, scheduler
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[OS Kernel]]

## What
Part of [[OS Kernel]] code.
Part of **scheduler subroutine**.
May be called either when there's [[Timed Interrupt]] by the timed interrupt handler or trap handler when there's [[Software Interrupt|system call]] made.

It creates, manages and keeps track of the system-wide [[Asynchronous Interrupt Handler|process table]], a data structure containing all sorts of information about current processes in the system.

## Role
The process manager is responsible for the following tasks:
1.  **Creation** and **termination** of both user and system processes
2.  **Pausing** and **resuming** processes in the event of **interrupts** or **system calls**
3.  **Synchronising** processes and provides **communications** between virtual spaces (Week 4 materials)
4.  Provide mechanisms to handle deadlocks (Week 5 materials)

## Long and Short Term Scheduler
[[Process scheduling]]
Scheduler is typically divided into two parts: long term and short term. They manage each queue accordingly as shown:

![](https://natalieagus.github.io/50005/assets/images/week3/7.png)

---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]

![[Pasted image 20220523145508.png]]

## Overview
[[User Programs]] can make [[System Calls]] whenever it needs to elevate its privileges and run in kernel mode to access hardware or IO devices.
> [[Operating System|OS]] provides services for [[User Programs]]

## Brief list of OS services
> These services are usually provided via [[OS Interfaces]].

### To help user
Basic support for computer system usage via [[System Calls]] routines

| Supported service         | Description                                                                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Program execution ([[Week 4 - Processes and Thread management]])        | System must be able to load program to memory, run upon request. End execution normally or with error.                                                                             |
| IO Operations ([[Week 1 - Introduction to Operating System]])            | A running program may require IO, may involve a file or IO device. [[Interrupt-Driven IO Operations]] and [[Asynchronous Input Handling]] and [[Asynchronous Interrupt Handler]]   |
| File-system manipulation ([[Week 6 - Files]]) | Programs need to read/write files and directories, create/delete, search, list file info, manage permissions.                                                                      |
| [[Process Control]](communication) | Processes may exchange information, on same computer or between computers over a network. Communications may be shared via memory or through message passing (packets moved by OS) |
| Error detection           | OS needs to be constantly aware of errors. <ol><li>May occur in CPU, memory, IO devices, [[User Programs]] </li> <li> For each error, OS should isolate or recover via appropriate actions</li> <li>Debugging facilities can enhance user and programmer abilities to use system correctly</li></ol>                                                                                                                                                                                   |

### For efficient operation of the system via resource sharing
Diagnostics report and computer sharing feature.

| Service          | Description                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Resource sharing | When multiple users/jobs run concurrently, how to allocate resources? (general goals: efficiency, fairness) |
| Accounting       | Keep track of who use how much and what kinds of resources (even if you don't charge money for the usage)                                                                                                            |

### Protection
Owners of information stored in a multiuser or networked computer system may want to control use of that information; concurrent processes should not interfere logically with each other.

| Service    | Description                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------- |
| Protection | Ensure accesses to resources or information are legal and valid                                                       |
| Security   | Protects against active attackers (usually from outside the system, but not always) who deliberately plan and do harm | 


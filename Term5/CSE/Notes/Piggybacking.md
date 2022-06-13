---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Piggybacking
From this point onwards, we are going to refer simply to the scheduler as the [[OS Kernel]]. Remember this is just a running code ([[Asynchronous Interrupt Handler|service routine]]) with kernel privileges whose task is to [[Process Manager|manage processes]]. Scheduler in itself, is part of the kernel, and is **not** a process.

Recall how the system calls **piggyback** the currently running user-process which mode has been changed to kernel mode. Likewise, the scheduler is just a set of instructions, part of the kernel realm whose job is to **manage** other processes. It is inevitable for the scheduler to be executed as well upon invoking certain system calls such as `read` or get `stdin` input which requires some **waiting** time.


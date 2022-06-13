
---
aliases: task control block, PCB
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

[[Asynchronous Interrupt Handler|process table]]

## Process table
> The system-wide [[Asynchronous Interrupt Handler|process table]] is a **data structure** maintained by the [[OS Kernel]] to facilitate [[Context switch]]ing and [[Process scheduling]].
> - Made up of an array of PCBs, containing information about **current processes in the system**.

## Process control block (PCB)
> Each process metadata is **stored** by the [[OS Kernel]] in a particular data structure called the **process control block (PCB)**.

Also called a **task control block**.

PCB contains info associated with a specific process. These information are ==updated== each time when a process is **interrupted**:
1. **[[Process scheduling state|Process state]]**: new, ready, running, waiting, terminated
2. **Program counter** [[Anatomy of the Beta CPU|PC]]: addr of the *next instruction* for this process
3. **CPU [[Sequential Logic|register]]s**: contents of registers in the CPU when an interrupt happens, including [[Stack and Procedures|stack]] pointer, *exception pointer, stack base, linkage pointer, etc.* These contents are saved each time to allow the process to be continued correctly afterward
4. **[[Process scheduling]] information**: access priority, pointers to scheduling queues, and other scheduling parameters
5. **Memory management information**: [[Pagetable]], [[Pagetable|MMU]] related information, memory limits
6. **Accounting information**: amt of CPU and real time used, time limits, account numbers, processs id (**pid**)
7. **IO status information**: list of IO devices allocated to the process, a list of open files

## Linux task_struct
In Linux system, the [[Process table and Process control block|PCB]] is created in C using a data structure called `task_struct`. The diagram below illustrates some of the contents in the structure: ![](https://natalieagus.github.io/50005/assets/images/week3/2.png)

Do not memorize the above, it’s just for illustration purposes only.

Within the Linux kernel, all active processes are represented using a [[Arrays and Linked Lists|doubly linked list]] of `task_struct.` The kernel maintains a `current_pointer` to the process that’s currently **running** in the CPU.

![](https://natalieagus.github.io/50005/assets/images/week3/3.png)

## Context Switching
[[Context switch]]
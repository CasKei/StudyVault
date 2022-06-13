---
aliases: OS-level thread
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Kernel level thread
Kernel level threads (sometimes known as OS-level threads) are threads that are:

1.  Scheduled by the Kernel, having its own stack and register values, but share data with other Kernel threads.
2.  Can be viewed as **lightweight processes**, which perform a certain task asynchronously.
3.  A kernel-level thread need not be associated with a process; a kernel can create them whenever it needs to perform a particular task.
4.  Kernel threads cannot execute in user mode.
    -   Processes that create kernel-level threads use it to **implement background tasks in the kernel**.
    -   E.g: handling **asynchronous** events or **waiting** for an event to occur.

All modern operating systems support kernel level threads, allowing the kernel to perform multiple simultaneous tasks and/or to **service** multiple kernel system calls simultaneously.

Most programming languages will provide an **interface** to create kernel-level threads, and the API for kernel-level threads are system-dependent. The C-API for creating kernel threads in Linux:

```c
#include <kthread.h>
kthread_create(int (*function)(void *data), void *data, const char name[], ...)
```

Mapping:
[[Thread mapping]]
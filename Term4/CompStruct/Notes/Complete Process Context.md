---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]

## A Complete Process Context
[[Complete Process Context]]
[[Virtual Memory|Previously]] we learned that each process has its own [[Virtual Address|VA]] to [[Memory Addressing|PA]] mapping we call as part of a process [[Context switch|context]], hence allowing it to run on its own [[Virtual Memory]].

Assigning a separate context for each process has 2 benefits:
1. Timesharing among processes (multitask, switching)
2. Allow each process to run in isolation - every program can be written as if it has access to all memory

Kernel needs to store more info about a process so that it can pause and resume execution without conflict.

List of components that make up a process context:
- Values of `R0, R1, ..., R30`
- [[Virtual Address|VA]] to [[Memory Addressing|PA]] mapping
- [[Anatomy of the Beta CPU|PC]] value
- [[Stack and Procedures|Stack]] state
- Program and shared code
- Virtual I/O devices (console etc)

Below: `N` processes: `P1`, `P2`, ... `PN` : each having its own information:
These processes are isolated from one another as they run on separate virtual memory.
![](https://dropbox.com/s/fvo6fllqrwwg2qr/context.png?raw=1)

Writing a OS Kernel is not a trivial task as one has to consider a lot of issues (security, performance, memory management, scheduling, etc).

But with its presence it is easier to write all other programs.

> It provides a layer of abstraction, allowing each program to run on a [[Virtual Machine]], devoid of any knowledge of other processes.

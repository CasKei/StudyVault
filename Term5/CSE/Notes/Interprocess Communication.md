---
aliases: IPC
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Interprocess Communication
Processes executing [[Concurrent Programming|concurrent]]ly in the [[Operating System]] may be either **independent** processes or **cooperating** processes:

-   By default, processes are **independent** and isolated from one another (runs on its own virtual machine)
-   A process is **cooperating** if it can affect or be affected by the other processes executing in the system.

Processes need to **cooperate** due to the following possible **reasons**:

1.  Information *sharing*
2.  Speeding up *computations*
3.  *Modularity* (protect each segments) and convenience

*Cooperating* processes require Interprocess Communication **(IPC)** mechanisms – these mechanisms are provided by or supported by the [[OS Kernel]]. There are two ways to perform IPC:

1.  [[Shared Memory]]
2.  [[Message Passing]] (e.g: [[Socket]])

[[Shared Memory vs Message Passing]] 
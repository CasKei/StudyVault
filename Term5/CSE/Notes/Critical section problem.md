---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]

## Supporting [[Critical section]]
To support the CS, we need to design a **protocol** that the processes can use to cooperate or synchronize.

> It is a challenging problem to **guarantee** a critical section. Therefore, having a critical section in your program is a **problem**, and it requires complex synchronisation solutions.

There are **two** basic forms of synchronization:

-   **The mutual exclusion**: No other processes can execute the critical section if there is already one process executing it.
-   **Condition synchronization**: Synchronize the execution of a process in a CS based on certain conditions instead.

[[Critical section solutions]]


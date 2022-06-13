---
aliases:
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Week 5 - Process Synchronisation]]

## Critical Section
> We define the **regions** in a program whereby atomicity must be guaranteed as the **critical section**.

Consider a system consisting of `n` processes `{P0, P1,..., Pn−1}`. Each process may have a **segment** of instructions, called a `critical section` (CS). The important **feature** of the system is that **when one process is executing its critical section, no other process is allowed to execute its critical section**.

In the consumer producer sample code above, the critical section in the producer’s code is the instruction `counter++` while the critical section in the consumer’s code is `counter-—`.

In the critical section the (asynchronous) processes may be:

-   Changing **common** variables,
-   Updating a **shared** table,
-   Writing to a **common** file, and so on.

To support the CS, we need to design a **protocol** that the processes can use to cooperate or synchronize.

> It is a challenging problem to **guarantee** a critical section. Therefore, having a critical section in your program is a **problem**, and it requires complex synchronisation solutions.

There are **two** basic forms of synchronization:

-   **The mutual exclusion**: No other processes can execute the critical section if there is already one process executing it.
-   **Condition synchronization**: Synchronize the execution of a process in a CS based on certain conditions instead.


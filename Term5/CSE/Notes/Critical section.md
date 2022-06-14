---
aliases: critical region
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]

## Critical Section
> We define the **regions** in a program whereby atomicity must be guaranteed as the **critical section**.

In [[Concurrent Programming]], concurrent accesses to shared resources can lead to unexpected or erroneous behavior, so parts of the program where the shared resource is accessed need to be protected in ways that avoid the concurrent access. This protected section is the **critical section** or **critical region**. It cannot be executed by more than one process at a time.

https://en.wikipedia.org/wiki/Critical_section

Consider a system consisting of `n` processes `{P0, P1,..., Pn−1}`. Each process may have a **segment** of instructions, called a `critical section` (CS). The important **feature** of the system is that **when one process is executing its critical section, no other process is allowed to execute its critical section**.

In the consumer producer sample code above, the critical section in the producer’s code is the instruction `counter++` while the critical section in the consumer’s code is `counter--`.

In the critical section the (asynchronous) processes may be:

-   Changing **common** variables,
-   Updating a **shared** table,
-   Writing to a **common** file, and so on.

[[Critical section problem]]
[[Requirements for critical section solution]]
[[Critical section solutions]]
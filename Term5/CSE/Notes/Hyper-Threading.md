---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Intel Hyper-Threading
Hyper-threading was Intel’s first effort (proprietary method) to bring parallel computation to end user’s PCs by fooling the kernel to think that there exist more than 1 processors in a single processor system:

-   A **single** CPU with **hyper-threading** appears as two or more **logical** CPUs (with all its resources and registers) for the operating system kernel
-   This is a process where a [CPU](https://www.tomshardware.com/reviews/cpu-buying-guide,5643.html) splits each of its physical [cores](https://www.tomshardware.com/news/cpu-core-definition,37658.html) into virtual cores, which are known as threads.
-   Hence the kernel assumes two CPUs for each single CPU core, and therefore **increasing the efficiency of one physical core**.
    -   It lets a single CPU to fetch and execute instructions from two memory locations **simultaneously**

This is **possible** if a big chunk of CPU time is wasted as it waits for data from cache or RAM.
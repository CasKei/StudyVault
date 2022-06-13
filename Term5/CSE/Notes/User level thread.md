---
aliases: green thread
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## User level thread
User level threads (sometimes known as green threads) are threads that are:

1.  Scheduled by a **runtime library** or virtual environment instead of by the Kernel.
2.  They are **managed in user space** instead of kernel space, enabling them to work in OS that do not have native thread support.
3.  **This is what programmers typically use.** (e.g when we create Thread in C or Java above).

Mapping:
[[Thread mapping]]
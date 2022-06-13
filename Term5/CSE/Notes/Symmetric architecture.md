---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Multiprocessor System]]

There are different architectures for multiprocessor system, such as a **symmetric** architecture — we have multiple CPU chips in a computer system:

![](https://natalieagus.github.io/50005/assets/images/week1/15.png)

Notice that each processor has its own set of registers, as well as a private or local cache; however, all processors share the **same** physical memory. This brings about design issues that we need to note in symmetric architectures:

1.  Need to carefully control I/O o ensure that the data reach the **appropriate** processor
2.  Ensure load **balancing**: avoid the scenario where one processor may be sitting idle while another is overloaded, resulting in inefficiencies
3.  Ensure cache coherency: if a process supports multicore, makes sure that the data integrity spread among many cache is maintained.

Another example of symmetric archi: [[Multi-core architecture]].
---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[OS structures]]


Hybrid kernels attempt to **combine** between **microkernel** and **monolithic** kernel aspects and benefits.

**Example**: macOS is partly based on [[Microkernel system structure]] + [[Monolithic structure]] approach (image taken from SGG):

1.  Mach provides: IPC, scheduling, memory management
2.  BSD provides: [[CLI]], file system management, networking support, POSIX APIs implementations

![](https://natalieagus.github.io/50005/assets/images/week2/13.png)
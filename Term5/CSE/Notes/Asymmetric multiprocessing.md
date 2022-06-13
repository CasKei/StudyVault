---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Multiprocessor System]]

In the past, it is not so easy to add a second CPU to a computer system when operating system had commonly been developed for single-CPU systems. Extending it to handle multiple CPUs **efficiently** and reliably took a long time. To fill this gap, operating systems intended for single CPUs were initially extended to provide **minimal** support for a second CPU.

This is called **asymmetric** multiprocessing, in which each processor is assigned a **specific** task with the presence of a super processor that controls the system. This scheme defines a **master–slave** relationship. The master processor **schedules** and **allocates** work to the slave processors. The other processors either look to the master for instruction or have predefined tasks.
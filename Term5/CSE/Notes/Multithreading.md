---
aliases: multithreaded process architecture
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

# Multithreading Benefits
## Responsiveness

Threads make the program seem more **responsive**. Multithreading an interactive application may allow a program to continue running even if **part** of it is **blocked** or is performing a lengthy operation, thereby increasing **responsiveness** to the user.

For example, a multithreaded **server architecture** below _(taken from SGG book)_: ![](https://natalieagus.github.io/50005/assets/images/week3/18.png)

Multithreading us to reap the benefits of true **parallel** programming in [[Multiprocessor System]] architecture, where threads may be running in **parallel** on different processing cores.

## Easy Resource Sharing and Communication

Easier means for resource sharing and communication (since code, data, and files are shared among threads of the same process and they have the **same** address space), as compared to creating multiple processes. On the other hand, multiple processes can only share resources through techniques such as [[Shared Memory]] and [[Message Passing]].

## Threads are Lighter

Creating new threads requires **cheaper** resources than creating new processes. Performing thread [[Context switch]] is also a **cheaper** process.

-   Allocating memory and resources for [[Process creation]] is **costly**.
-   Because threads **share** the resources of the process to which they belong, it is more economical to **create** and **context-switc**h threads.

> Remember, [[Context switch]] is **pure** overhead.
---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

# Thread Mapping
Since there are two types of threads: [[Kernel level thread]] and [[User level thread]], there should exist some kind of mapping between the two. The mapping of user threads to kernel threads is done using virtual processors. We can think of kernel level threads as **virtual processors** and user level threads as simply **threads**.

There are three types of mapping.

## Many to one
> Maps **many** [[User level thread]] to **one** [[Kernel level thread]].

**Advantage**:
-   Thread management is done by the thread library in user space, so it is more **efficient** as opposed to kernel thread management.
-   Developers may create as many threads as they want

**Disadvantage**:
-   **The entire process will block** if a thread makes a blocking system call since kernel isn’t aware of the presence of these user threads
-   Since only one thread can access the kernel at a time, multiple threads are unable to run in parallel on multicore systems

![](https://natalieagus.github.io/50005/assets/images/week3/19.png)

## One to one
> Maps **each** [[User level thread]] to a [[Kernel level thread]].

**Advantage**:

-   Provides **more [[Concurrent Programming|concurrency]]** than the [[#Many to one]] model by allowing another thread to run when a thread makes a blocking system call.
-   Allows **multiple** threads to run in parallel on [[Multiprocessor System|multiprocessors]].

**Disadvantage**:
-   Creating a [[User level thread]] requires creating the corresponding [[Kernel level thread]] (a lot of **overhead**, [[System calls]] must be made)
-   **Limited** amount of threads can be created to not burden the system

The modern Linux implementation of pthreads uses a 1:1 mapping between pthread threads and [[Kernel level thread]], so you will always get a [[Kernel level thread]] with `pthread_create().` ![](https://natalieagus.github.io/50005/assets/images/week3/20.png)
Originally had no [[User level thread]] switch. So when `yield()`, results in [[System calls]]. Now might be different.

## Many to many
> **[[Multiplexing|Multiplexes]]** many [[User level thread]]s to a smaller or equal number of [[Kernel level thread]].

This is the best of both worlds (hybrid-ish):
-   Developers can **create** as many [[User level thread]]s as necessary,
-   The corresponding [[Kernel level thread]] can run in **parallel** on a [[Multiprocessor System|Multiprocessor]].

![](https://natalieagus.github.io/50005/assets/images/week3/21.png)
That middle thing is a user-level library. Mapping is done on the fly.

A variation of many-to-many mapping, the **two-level model**: both [[Multiplexing]] user threads and allowing some user threads to be mapped to just one kernel thread.

![](https://natalieagus.github.io/50005/assets/images/week3/22.png)

In some systems, especially in many-to-many or two-level models, there is some way for kernel threads to communicate with kernel threads via **scheduler activation**, i.e: a mechanism whereby kernel can *allocate more threads to the process* **on demand**.
---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Motivation
The objective of [[Multiprogramming]] is to have some [[Process vs Program|process]] running at all times, to maximize CPU utilization.

The objective of [[Timesharing]] is to [[Context switch]] the CPU among processes so frequently that users can interact with each program while it is running.

To meet **both** objectives, the [[Process Manager|process scheduler]] selects an available process (possibly from a set of several available processes) for program execution on the CPU.

-   For a single-processor system, there will never be more than one actual running process at any instant.
-   If there are more processes [[Multiprocessor System|Multiprocessing]], the rest will have to wait in a queue until the CPU is free and can be rescheduled.

For Linux scheduler, see the man page [here](https://man7.org/linux/man-pages/man7/sched.7.html). We can set [[Worked example on scheduling policies|scheduling policies]] : `SCHED_RR`, `SCHED_FIFO`, etc. We can also set [[Handler Priority Level|priority value]]  and `nice` value of a process (the latter used to control the priority value of a process in user space.

## Process Scheduling Queues [[Stacks and Queues data structure|queue]]
There are 2 **queues** that are maintained by the process [[Process Manager|scheduler]]:
1. **JOB QUEUE**: set of all processes in the system (can be both in main memory and swap space of disk)
2. **READY QUEUE**: set of all processes residing in main memory, ready and waiting to execute (queueing for CPU)
3. **DEVICE QUEUES**: set of processes waiting for an IO device (one queue for each device)

Each queue contains the **pointer** to the corresponding [[Process table and Process control block|PCB]]s that are waiting for the **resource** (CPU, or IO)

#### Example
The diagram below shows a system with ONE ready queue, and FOUR device queues (_image screenshot from SGG book_):

![](https://natalieagus.github.io/50005/assets/images/week3/5.png)

#### Queueing Diagram
A common representation of process scheduling is using a queueing diagram as shown below:

![](https://natalieagus.github.io/50005/assets/images/week3/6.png)

Legends:

-   **Rectangular** boxes represent queues,
-   **Circles** represent resources serving the queue
-   All types of queue: job queue, ready queue and a set of device queues (I/O queue, I/O Req, time exp, fork queue, and wait `IRQ`)

A new process is initially put in the **ready** queue. It waits there until it is selected for execution, or dispatched. Once the process is allocated the CPU, a few things **might** happen afterwards (that causes the process to leave the CPU):

-   If the process issue an I/O request, it will be placed onto the **I/O queue**
-   If the process `forks` (**create** new process), it may queue (wait) until the child process finishes (terminated)
-   The process could be forcily removed from the CPU (e.g: because of an interrupt), and be put back in the **ready** queue.

### Long and Short Term Scheduler
[[Process Manager|scheduler]]
Scheduler is typically divided into two parts: long term and short term. They manage each queue accordingly as shown:

![](https://natalieagus.github.io/50005/assets/images/week3/7.png)
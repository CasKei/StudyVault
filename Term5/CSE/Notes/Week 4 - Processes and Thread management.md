---
aliases: process, thread
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

# Processes
## Process vs Program
[[Process vs Program]]
- [[Process vs Program#A Process Context|A process context]]
- [[Process vs Program#Concurrency and Protection|Concurrency and protection]]

## Piggybacking
[[Piggybacking]]

## Process scheduling states
[[Process scheduling state]]

## Process table and Process control block
[[Process table and Process control block]]
- Linux task_struct
- [[Context switch]]ing

## Rapid Context Switching and Timesharing

| [[Timesharing]] | [[Context switch]] |
| --------------- | ------------------ |


## Mode switch vs Context switch
| [[Kernel mode and User mode]]                 | [[Context switch]]                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------- |
| sinply escalate privileges                    | require both saving states of old processes and loading states of new processes |
| by hardware int, sys calls, exceptions, reset | by timed interrupt, sys call that leads to `yield()`                                                                                |

## Process Scheduling
[[Process scheduling]]

## Operations on Processes
We can perform various **operations** on a process: spawning child processes, terminate the process, set up inter-process communication [[Interprocess Communication]] channels, change the process priority, and many more. All of these operations require a [[System calls]] (switching to [[Kernel mode and User mode|kernel mode]]). In this example, we use the **C API** to make the system call.

[[Operations on Processes]]
- [[Process creation]]
	- [[Process creation#Process Tree]]
	- [[Process creation#Process Id]]
	- [[Process creation#Child Process vs Parent process]]
		- [[Process creation#How fork works]]
			- fork return value
			- execlp
			- wait
			- the fork tree
- [[Process Termination]]
	- [[Process Termination#Orphaned processes]]
	- [[Process Termination#Zombie processes]]
		- [[Process Termination#Zombie making]]

## Interprocess Communication (IPC)
[[Interprocess Communication]]
- [[Shared Memory]]
	- [[Shared Memory#Procedure]]
	- [[Shared Memory#IPC without SVC]]
	- [[Shared Memory#IPC with SVC(unsync)]]
	- [[Shared Memory#Removing Shared Memory]]
- [[Message Passing]]
	- [[Socket]]
		- [[Socket#IPC using socket]]
	- [[Message Queue]]

[[Shared Memory vs Message Passing]] 
Application: [[Chrome Browser Multi-process architecture]]

# Threads
> Threads is defined as a **segment** of a process. A process has **at least** one thread.

A process can have **multiple** threads, and we can define thread as a basic unit of CPU utilization; it comprises of:

-   A **thread ID**,
-   A **program counter**,
-   A **register** set, and
-   A **stack**.

A thread can execute **any** part of the process code, including parts currently being executed by another thread.

The figure below _(taken from SGG book)_ shows the illustration of a single-threaded and multi threaded processes. As shown, it **shares** with other threads belonging to the same process its code section, data section, and other operating-system resources, such as open files and signals. Multiple threads in the same process operates in the **same address space**.

![](https://natalieagus.github.io/50005/assets/images/week3/17.png)

## Multithreading
- [[Multithreading]]
	- [[Multithreading#Responsiveness]]
	-  [[Multithreading#Easy Resource Sharing and Communication]]
	-  [[Multithreading#Threads are Lighter]]

## Multithreading vs Multiprocessing
| Thing                      | [[Multiprocessor System]]                                                                                   | [[Multithreading]]                                                                                                                                        |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Protection and concurrency | Processes have both. Processes are isolated, so there is fault isolation.                                   | Threads only have concurrency but no protection, since code, data, and files are shared between threads of the same process. There is no fault isolation. |
| Communication              | IPC expensive, requires system calls and context switch between processes has high overhead.                | Thread communication has low overhead since they share the same address space. Context switching (thread switching) between threads is much cheaper       |
| Parallel execution         | Parallel process execution always available on multicore system                                             | Parallel thread execution is not always available. Depends on types of threads.                                                                           |
| Synchronisation            | We can rely on OS services (system calls) to synchronise execution between processes, i.e. using semaphores | Careful programming is required (burden on developer) to synchronise between threads                                                                      |
| Overhead cost              |  Processes entirely managed by kernel scheduler: <ul><li>Switch between process executions: FULL(costly) context switch + system call required</li><li>Context of process is large, including flushing cache, managing MMU, since each process lives in different virtual space</li></ul>                                                                                                           |     Threads managed by Thread Scheduler (user space, depending on language):  <ul><li>Lighter context switch sufficient to switch between thread executions</li><li>Context of thread lighter since threads live in same virtual space. Contents that need to be switched involve mainly only registers and stack</li><li>May or may not need to perform system call to access Thread API, depending on types of thread</li></ul>                                                                                                                                                    |


## Thread Examples: Java and C Thread
[[Java Thread]]
[[C Thread]]

## Types of Threads
We can create two types of threads, **kernel** level threads and **user** level threads.

[[User level thread]]
[[Kernel level thread]]

[[User vs Kernel level thread]]

## Thread Mapping
[[Thread mapping]]
- [[Thread mapping#Many to one]]
-  [[Thread mapping#One to one]]
-  [[Thread mapping#Many to many]]

## Intel Hyper-Threading
not tested
[[Hyper-Threading]]

## Multicore Programming
[[Multi-core architecture]]
[[Amdahl's Law]]

# Appendix

[[Daemon Processes]]
[[Desktop environment]]
[[Booting]]

1.  A virtual processor (VP) is a library entity that is usually implicit. For a user thread, the VP behaves like a CPU. In the library, the VP is a kernel thread or a structure bound to a kernel thread. (taken from https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/generalprogramming/thread_models_virtual.html)
2.  cron is a Linux utility which schedules a command or script on your server to run automatically at a specified time and date. A cron job is the scheduled task itself. 


![[Pasted image 20220603150022.png]]

![[Pasted image 20220603145937.png]]
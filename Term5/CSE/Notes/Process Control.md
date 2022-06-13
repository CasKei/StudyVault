---
aliases: process abort, process load, process execute, process load and execute, process communication
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[Week 4 - Processes and Thread management]]
[[System calls]]

In this section we choose to explain one particular type of system calls: **process control** with a little bit more depth.

## Process Abort
A running process can either **terminate** **normally** (end) or **abruptly** (abort). In either case, system call to **abort** a process is made.

If a system call is made to terminate the currently running program **abnormally**, or if the program runs into a problem and causes an error **trap**, a dump of memory (called [`core dump`](https://en.wikipedia.org/wiki/Core_dump)) is sometimes taken and an error message generated.

It consists of the recorded state of the program memory at that specific time when the program **crashed**. The dump is written to disk and may be examined by a debugger; a type of system program. It is assumed that the user will issue an appropriate command to respond to any error.

## Process Load and Execute
Loading and executing a new process in the system require system calls. It is possible for a process to call upon the execution of another process, such as creating background processes, etc.

-   For instance the **shell** creates a new process whenever it receives a new command, and requests to execute that command in the **new process** [[Week 4 - Processes and Thread management]]

## Process communication
Having created new jobs or processes, we may need to **wait** for them to **finish** their execution, e.g: the shell only gives the next prompt after the previous command has completed its execution.

-   We may want to wait for a certain amount of time to pass `(wait time)`; more probably, we will want to wait for a specific event to occur `(wait event)`.
-   The jobs or processes should then signal when that event has occurred `(signal event)`.
-   Also, sometimes two or more processes **share** data and multiple processes need to **communicate** (e.g: a web server communicating with the database server).
-   All these features to `wait, signal event`, and other means of process **communication** are done by making system calls since each process is run in **isolation** by default, operating on [[Virtual Address]]es.

## Single-tasking system vs multi-tasking system
There are so many facets of and variations in process and job control that we need to clarify using examples: MS-DOS and FreeBSD.

![](https://natalieagus.github.io/50005/assets/images/week2/7.png)

[[Single-tasking system]]
[[Multi-tasking system]]
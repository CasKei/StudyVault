---
aliases: process, program
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Week 4 - Processes and Thread management]]
[[OS Kernel]]

## Program
> A program resides on _disk_ and isn’t currently used. It **does not** take up **resources**: CPU cycles, RAM, I/O, etc while a process need these resources to run.

## Process
> **A process is a program in execution**. It is a unit of work within the system, and a process has a **context** (regs values, stack, heap, etc) while a program does not.

## Process vs program
| Process                                                                           | Program                                                               |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| A passive, **static** entity. Just lines of instructions.                                     | An active, **dynamic** entity. State change over time as instructions are executed |
| Needs resources like CPU cycles, RAM, IO, etc.                                    | Resides on disk and isn't currently used, does not take up resources. |
| When created, [[OS Kernel]] allocates these resources so it can begin to execute. | Managed by PC                                                         |
| When terminated, resources are freed by kernel                                    |                                                                       |

A typical general-purpose computer runs multiple processes at a time.

If you are interested to find the list of processes in your Linux system, you can type `top` in your terminal to see all of them in real time. A single CPU achieves [[Concurrent Programming|concurrency]] by [[Multiplexing]] (perform rapid [[Context switch]]ing) the executions of many processes.

## A Process Context
[[Complete Process Context]]
A single process includes all of the following information:

1.  The **text** section (code or ==instructions==)
2.  Value of the Program Counter (**PC**)
3.  Contents of the processor’s **registers**
4.  Dedicated **address space** (block of location) in memory
5.  **Stack** (==temporary data== such as function parameters, return address, and local variables, grows downwards),
6.  **Data** (==allocated memory== during compile time such as global and static variables that have predefined values)
7.  **Heap** (==dynamically allocated memory== – typically by calling `malloc` in C – during process runtime, grows upwards) These information are also known as a process **state**, or a process **context**:

The same program can be run `n` times to create `n` processes simultaneously.

-   For example, separate tabs on some web browsers are created as **separate processes**.
-   The **program** for all tabs are the same: which is the part of the web browser code itself.

> A program becomes a process when an **executable** (binary) file is **loaded** into memory (either by double clicking them or executing them from the command line)

## Concurrency and Protection
>  A process couples **two abstractions**: [[Concurrent Programming|concurrency]] and **protection**.

Each process runs in a different address space and sees itself as running in a virtual machine – unaware of the presence of other processes in the machine. Multiple processes execution in a single machine is [[Concurrent Programming|concurrent]], managed by the **kernel scheduler**.
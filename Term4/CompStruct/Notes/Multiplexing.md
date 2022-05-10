---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]

## What
> **Multiplexing**
> A method of sharing the resources in a computer system for multiple running programs at the same time.

The OS Kernel handles the multiplexed execution of various running programs in a single [[Anatomy of the Beta CPU|CPU]] - [[Context switch]]ing so rapidly - that for users, the computer is seemingly able to run multiple processes in "parallel".

## How
E.g. 2 processes `P1` and `P2` sharing a single system:
![](https://dropbox.com/s/p5r7q2uit6vbdkz/process.png?raw=1)

The arrow illustrates timeline of execution.
- At first CPU run some task from `P1`
- After some time $t$, imagine a *timed interrupt* (caused by other asynchronous hardware, e.g. a timer) occurs. This causes the [[Anatomy of the Beta CPU|CPU]] to execute part of the kernel program that handles such **asynchronous interrupt**, hence pausing the execution of `P1`.
- This **interrupt handler** takes control of the [[Anatomy of the Beta CPU|CPU]] when hardware interrupt occurs, and **saves** the current states ([[Anatomy of the Beta CPU|PC]], [[Sequential Logic|register]]s, etc) of `P1` to a dedicated space (**Kernel stack**) in the [[Anatomy of the Beta CPU|memory unit]], before performing a [[Context switch]]:
	- Load states of `P2` to [[Anatomy of the Beta CPU|CPU]] (and also the required resources, mapping, etc), and
	- Resume execution of `P2`
- `P2` runs and progresses for some time $t$ before another **hardware interrupt** occurs. The entire [[Context switch]] process is repeated to pause `P2`, resume `P1` and so on.

In practice, the _interrupt handler_ will examine the _cause_ of the asynchronous interrupt. In the event of periodic interrupt caused by a timer, the handler will delegate the task to the **kernel scheduler** whose job is to decide _which_ process to run next, and prepare the necessary information / context to load this process back into the CPU so that the selected process may resume smoothly. When the scheduler returns to the handler, the handler resumes execution of the CPU by simply setting $PC \leftarrow Reg[XP] - 4$.

The key technology that allows for OS Multiplexing is the **asynchronous hardware interrupt.**

We will simply call asynchronous interrupt as just “interrupt” for simplicity. A synchronous interrupt is called as “[[Trap]]” instead.

## Hardware Support for OS Multiplexing
[[Hardware Support for OS Multiplexing]]

## Example
[[Example of basic kernel scheduler]]
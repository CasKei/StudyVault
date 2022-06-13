---
aliases: multicore programming, data parallelism, task parallelism
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Multiprocessor System]]
[[Week 4 - Processes and Thread management]]

## Architecture
Another example of a (Multiprocessor) [[Symmetric architecture]] is to have **multiple cores on the** *same chip* as shown in the figure below:

![](https://natalieagus.github.io/50005/assets/images/week1/16.png)

This carries an advantage that on-chip communication is **faster** than across chip communication. However it requires a more delicate hardware design to place multiple cores on the same chip.

## Multicore Programming
> On a system with multiple cores and supported kernel mapping, [[Concurrent Programming|concurrency]] means that the threads can run in parallel, because the system can assign a separate thread to each core.

E.g. $T_i$ = thread $i$,

| Multicore parallel execution | Concurrent execution with single core |
| ---------------------------- | ------------------------------------- |
| ![[yiilyy1b.bmp]]            | ![[e3cu0x73.bmp]]                     | 

Multicore is faster.

There are 2 types of parallelism that we can achieve via multicore programming:
- **Data Parallelism**: focus on distributing subsets of the same data across multiple computing cores and perforing the same operation on each core
- **Task parallelism**: involves distributing not data but tasks (threads) across multiple computing cores
	- Each thread is performing a unique operation
	- Different threads may be operating on the same data, or they may be operating on different data

Note: [[Amdahl's Law]]


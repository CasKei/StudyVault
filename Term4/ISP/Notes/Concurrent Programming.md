---
aliases: concurrent, concurrency
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 3]]

[Website](https://www.educative.io/edpresso/what-is-concurrent-programming)

## What
Concurrency: events or circumstances that are happening or existing at the same time.

> Concurrent programming:
> A technique in which 2 or more processes start, run in an interleaved fashion through [[Context switch]]ing, and complete in an overlapping time period by managing access to *shared resources* e.g. on a single core of CPU

This doesn't necessarily mean that multiple processes will be running at the same instant, even if results make it seem like it,

![[Pasted image 20220328222317.png]]

## Android
We want our applications to handle different tasks simultaneously. In [[Android 3|this]] app, we are going to query a web API to retrieve data.

The length of time this task will take depends on
- internet connection
- file size, etc

While data is retrieved, you want UI to remain responsive and inform the user that the download is still in progress,

This means that **download** should be done on a *separate thread* from the **UI**.

## [[Week 4 - Processes and Thread management|thread]]
> A unit of executing sequences in a program.

A concurrent program consists of multiple threads and an **executor (scheduler)** which orchestrates the actual execution/scheduling of the threads.

In the presence of multiple processing units ([[Anatomy of the Beta CPU|CPU]] cores), the [[Process Manager|scheduler]] might be able to execute/schedule multiple threads simultaneously in different processing units, otherwise, the scheduler will interleave the executions of the given set of scheduled threads.

This is often [[Abstraction|abstracted]] away from the programmers, so as to prevent deadlock or other abnormal outcomes.

## Java
[[The Executor Class]]

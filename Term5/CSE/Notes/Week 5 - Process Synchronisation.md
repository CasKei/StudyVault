---
aliases: process synchronisation, synchronisation
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

# Process and Thread Synchronisation
## Producer Consumer Problem
[[Producer Consumer problem]]

## Race Condition
[[Race condition]]

## Critical Section
[[Critical section]]
[[Critical section problem]]
[[Critical section solutions]]

## Java Synchronisation
[[Java synchronisation]]

## Summary
There are a few **solutions** to the CS problem. The CS problem can be divided into two types:

-   **Mutual exclusion** [[Mutex]]
-   **Condition synchronization**

There are also a few solutions listed below.

[[Software Mutex Algorithm]] provide mutex via [[Spinlock|busy waiting]].

**Hardware** synchronisation methods [[Hardware supported spinlocks|hardware spinlock]] provide mutex via **atomic** instructions.

> Other software spinlocks and mutex algorithms can be derived using these special atomic assembly instructions

[[Sephamores]] provide **mutex** using binary semaphores.

Basic **condition** variables provide **condition synchronization** and are used along with a mutex lock.

**Java anonymous** default synchronization object provides mutex using reentrant binary lock (`this`), and provides condition synchronisation using `wait()` and notifyAll() `or` notify()`

**Java named synchronization** object provides mutex using named reentrant binary lock (`ReentrantLock()`) and provides condition sync using condition variables and `await()/signal()`

It is entirely up to you to figure out which one to use for your application.
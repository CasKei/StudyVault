---
aliases: sephamore
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section problem]]
[[Critical section solutions]]

## Sephamore
> Can be seen as a **generalised [[Mutex lock]]. Provides [[Mutex]]**.

- Implemented at [[Kernel level thread|kernel level]]: its execution requires the calling process to change into the [[Kernel mode and User mode|kernel mode]] via [[Software Interrupt|trap]] ([[Supervisor Call|SVC]]) sephamore instructions
- Is a high-level **software** solution that relies on [[Hardware supported spinlocks|synchronisation hardware]] (like those special atomic instructions) and is considered a more *robust* tool than [[Mutex lock]].

> Peterson’s solution and the hardware-assisted solutions all require busy waiting. However using semaphore, you can express a solution to the CS problem without busy waiting.

## Definition
> -   An **integer variable** that is maintained in the kernel, initialized to a certain value that represents the number of **available** resources for the sharing processes
> -   Is accessed only through two standard **atomic** [[System calls]] operations: `wait()` and `signal()`.

Since calls to `signal()` or `wait()` for sephamores must be atomic, they are often implemented using one of the [[Hardware supported spinlocks|synchronisation hardware]] mechanisms (to support [[Multi-core architecture]] synchronisation) or [[Software Mutex Algorithm]]s such as [[Peterson's Solution]], when restriction applies.

## Usage
- **Binary sephamore**: `0` or `1`
- **Counting sephamore**: any int from `0` to `N`

## Implementation
How semaphores avoid busy waiting (well, _mostly_): it integrates implementation with CPU scheduler, hence the need to make [[System calls]] throughout. It will put the calling process that attempts to `acquire()` on suspension if the semaphore is not currently available.

There are two common CPU scheduling operations ([[System calls]]): `block()` and `wakeup()`. Both are used to implement `wait()` and `signal()` semaphore functions.

-   Whenever the process/thread needs to `wait()`, it **reduces** the semaphore and if the current semaphore value is negative, it blocks itself.
-   It is added to a **waiting queue** of processes/threads associated with that semaphore. This is done through the system call `block()` on that process.
    
    ```c
    wait(semaphore *S)
    {  S <- value--;
     if (S <- value < 0)
     {
         add this process to S <- list; // this will call block() 
     }
    }
    ```
    
-   When a process is completed it calls a `signal()` function and one process in the queue is resumed, by using the `wakeup()` system call.
    
    ```c
    signal(semaphore *S)
    {
     S <- value++;
     if (S <- value >= 0)
     {
         remove a process P from S <- list;
         wakeup(P);
     }
    }
    ```
    

Further notes about the above simple implementation of Semaphore `wait` and `signal` System Calls:

-   Semaphore values may be **negative**, but this is typically **hidden** from user
    -   On the surface, semaphore values are never negative under the classical definition of semaphores with busy waiting.
-   If the semaphore value is **negative**, **its magnitude** is the number of processes waiting on that semaphore
-   The list (a queue of processes waiting to acquire the semaphore) can be easily implemented by a link field in each process control block ([[Process table and Process control block|PCB]]).
    -   Each semaphore data structure for example, can contain an **integer** value and a **pointer to a list of PCBs.**

Note that semaphore implementation may vary between different libraries, but the idea remains the same.

> NOTE: `wait()` and `signal()` are [[Critical section solutions]]
> If [[Re-entrancy|re-entrant]], more than one process can be in the kernel, but `wait` and `signal` are in kernel. So potential [[Race condition]] in kernel and that's bad.



## Circular Dependency
How can we implement `signal()` and `wait()` atomically **without** [[Spinlock|busy waiting]], if it relies on [[Hardware supported spinlocks|synchronisation hardware]] in [[Multiprocessor System]] or even basic [[Software Mutex Algorithm]]s (e.g: if on uniprocessor systems) that **requires** [[Spinlock|busy waiting]]?

> The answer is that semaphore **DOES NOT** completely eliminate [[Spinlock|busy waiting]],

Specifically: it **ONLY busy waits in the [[Critical section]] of semaphore** function itself: `wait()`, `signal()` that is relatively **SHORT** if implemented properly

> We do NOT busy-wait in the CS of the program itself (which can be considerably longer).

In practice, the critical section of the `wait()` and `signal()` implementation of the semaphore in the library is almost never occupied (meaning it’s rare that two processes or threads are making the same wait and signal call on the same semaphore), and busy waiting occurs rarely, or if it does happen, it happens for only a short time.

In this specific situation, busy waiting is **completely acceptable** and still remains efficient.

## Applying Sephamore to MPC Problem
[[Producer Consumer problem]]
Now that we know how semaphore works, it’s useful to think about how they can be applied to tackle the **multiple** **producer-consumer**(MPC in short) problem that we analyzed earlier in this section above.

The pseudocode below illustrates the idea on how the semaphore can be used to replace `counter`, and **protect** the consumer/producer code against multiple (more than 1 of each) consumer/producer threads [[Race condition|racing]] to execute their respective instructions, and sharing resources:

-   write index `in` (shared among consumer processes)
-   read index `out` (shared among producer processes)
-   `char buf[N]` (shared among all processes)
-   Two semaphores: one binary and one counting semaphore

Shared resources:

```c
char buf[N];
int in = 0; int out = 0;

semaphore chars = 0; // to sync between 1 p and 1 c
semaphore space = N; // to sync between 1 p and 1 c
semaphore mutex_p = 1; // to sync between multiple p
semaphore mutex_c = 1; // to sync between multiple c
```

Producer program:

```c
void send (char c){
   wait(space);
   wait(mutex_p);

   buf[in] = c;
   in = (in + 1)%N;

   signal(mutex_p);
   signal(chars);
}
```

Consumer program:

```c
char rcv(){
   char c;
   wait(chars);
   wait(mutex_c);

   c = buf[out];
   out = (out + 1)%N;

   signal(mutex_c);
   signal(space);
}
```

![[Pasted image 20220619092629.png]]
![[Pasted image 20220619102559.png]]
(mutex, empty, full)
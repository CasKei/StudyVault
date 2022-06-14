---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section problem]]
[[Critical section solutions]]
[[Software spinlocks and mutex locks]]

## Mutex Lock
[[Mutex]]
Some other libraries (like C POSIX library) implement another type of lock called **mutex lock** that does not cause [[Spinlock|busy waiting]].

Mutex locks are also supported by special atomic assembly instructions implemented at ==hardware== level, and requires **integration** with the [[Process Manager|kernel scheduler]] because it will put the requesting thread/process to **sleep** if the lock has already been acquired by some other thread.

Example of POSIX Mutex usage:

```c
// initialize mutex
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_lock(&mutex); // this is  acquire() equivalent, atomic and might invoke kernel scheduler and context switch if mutex not available  
// CRITICAL SECTION HERE ...
pthread_mutex_unlock(&mutex); // this is  release() equivalent, atomic and might invoke kernel scheduler as well to wake up other waiting processes/threads
// REMAINDER SECTION HERE ...
```

The problem with mutexes is that putting threads to sleep and waking them up again are both rather **expensive** operations, they’ll need quite a lot of CPU instructions **overhead** due to the integration with the Kernel Scheduler.

If the [[Critical section]] is short, then the overhead of using mutexes might be **more** than the time taken to “spin” when using a [[Spinlock]]. It is up to the programmer which one to use for their purposes.
---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## Deadlock
> Deadlock is a situation whereby a set of **blocked processes** (none can make **progress**) each holding a [[System resource]] and waiting to acquire a resource held by another process in the set.

The locking tools we learned ([[Critical section solutions]]) **prevents** [[Race condition]], but if not implemented prperly can cause **deadlock**.

## Example
Consider 2 [[Mutex lock]]s being initialised.
```csharp
pthread_mutex_t first_mutex;
Pthread_mutex_t second_mutex;
pthread_mutex_init(&first_mutex,NULL); 
pthread_mutex_init(&second_mutex,NULL);
```

2 [[Week 4 - Processes and Thread management|thread]]s doing these work [[Concurrent Programming|concurrent]]ly potentially results in deadlock:
```c
// Thread 1 Instructions
pthread_mutex_lock(&first_mutex); 
pthread_mutex_lock(&second_mutex); 
/**
* Do some work
*/
pthread_mutex_unlock(&second_mutex); 
pthread_mutex_unlock(&first_mutex);
pthread_exit(0);
/************************************/


// Thread 2 Instructions
pthread_mutex_lock(&second_mutex); 
pthread_mutex_lock(&first_mutex); /**
/**
* Do some work
*/
pthread_mutex_unlock(&first_mutex); 
pthread_mutex_unlock(&second_mutex);
pthread_exit(0);
/************************************/
```

Consider a scenario where Thread 1 acquires `first_mutex` and then gets suspended, then Thread 2 acquires `second_mutex`.
- **Neither thread gives up** their currently held `mutex`
- But they need each other's [[Mutex lock]] to *continue*, hence **neither has made progress** and they are in **deadlock**.

## Necessary conditions
> **Deadlock may arise if all 4 hold simultaneously in a system**

These are necessary but not sufficient conditions.

| Condition             |                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Mutual exclusion**  | At least one resource must be held in a **non-sharable mode**<br> If another process requests that resoruce that is currently held by others, the requesting process must be **delayed** until the resource has been released. |
| **Hold and wait**     | A process must be **holding** at least one [[System resource]] and **waiting** to acquire additionl resources that are currently being held by other processes.                                                                |
| **No [[Preemption]]** | [[System resource]]s can only be **released** **after** that process has **completed** its task, **voluntarily** by the process holding it.                                                                                    |
| **Circular wait**     | There exists a cycle in the [[Resource allocation graph]]                                                                                                                                                                                                                               |

These conditions are necessary but not sufficient, meaning that if all four are present, it is not 100% guaranteed that there is currently a deadlock.

> Think! Since these conditions are _necessary_ for deadlock to happen, **removing** just one of them **prevents** deadlock from happening at all.
> [[Deadlock prevention]]
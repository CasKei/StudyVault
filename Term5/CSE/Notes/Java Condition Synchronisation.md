---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]

## Java Condition Synchronisation
Similarly, Java allows for condition synchronization using `wait()` and `notify()` method, as well as its own condition variables.

Example: suppose a few threads are trying to execute the same method as follows,

```java
public synchronized void doWork(int id)
{
   while (turn != id) // turn is a shared variable
   {
       try
       {
           wait(); 
       }
       catch (InterruptedException e)
       {
       }
   }
   // CRITICAL SECTION
   // ... 
   turn = (turn + 1) % N;
   notify();
}
```

Suppose `N` threads are running this `doWork` function **[[Concurrent Programming|concurrent]]ly** with argument `id` varying between `0` to `N-1`, i.e: 0 for thread 0, 1 for thread 1, and so on.

In this example, the condition in **question** is that ONLY thread whose `id == turn` can execute the CS.

When calling `wait()`, the lock for [[Mutex]] **must** be held by the caller (same as the conditional variable in the section above). That’s why the `wait` to the conditional variable is made inside a `synchronized` method. If not, disaster might happen, for example the following execution sequence:

-   At `t=0`,
    -   Thread Y check that `turn != id_y`, and then Y is suspended.
-   At `t=n`,
    -   Thread X **resumes** and **increments** the `turn`. This causes `turn == id_y`.
    -   Suppose X then calls `notify()`, and then X is suspended
-   At `t=n+m`,
    -   Thread Y **resumes** execution and enters `wait()`.
-   However at this time, the value of `turn` is ALREADY `== id_y`.

We can say that thread Y **misses** the `notify()` from X and might `wait()` forever. We need to make sure that BETWEEN the check of `turn` and the call of `wait()`, no OTHER THREAD can change the value of `turn`.

Since we MUST invoke `wait()` while holding a lock, it is important for `wait()` to **release** the object lock eventually (when the thread is waiting). If you call another method to `sleep` such as `Thread.yield()` instead of `wait()`, then it **will not** release the lock while waiting. This is **dangerous** as it will result in indefinite waiting or [[Week 5, 6 - Deadlock|deadlock]].

Upon return from `wait()`, the Java thread would have **re-acquired** the mutex lock **automatically**.

In summary,

-   When a thread calls the `wait()` method, the following happens:
    -   The thread **releases** the lock for the object.
    -   The state of the thread is set to **blocked**.
    -   The thread is placed in the **wait set** for the object.
-   When it calls `notify()`:
    -   Picks an **arbitrary** thread T from the list of threads in the wait set
    -   Moves T from the wait set to the **entry** set
    -   The state of T will be changed from blocked to **runnable**, so it can be scheduled to reacquire the [[Mutex lock]].

![[NotifyAll]]
![[Wait in a loop]]
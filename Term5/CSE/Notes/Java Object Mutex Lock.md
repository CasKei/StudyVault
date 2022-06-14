---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]

## Java Object Mutex Lock
[[Mutex lock]]
The Java programming language provides two basic synchronization idioms: synchronized **methods** and synchronized **statements**.

Each Java **object** has an associated binary **lock**:

-   Lock is `acquired` by invoking a synchronized method/block
-   Lock is `released` by exiting a synchronized method/block

With this lock, mutex is guaranteed for this object’s **method**; at most only one thread can be inside it at any time.

Threads **waiting** to acquire the object lock are waiting in the **entry** set, status is still `blocked` and not runnable until it acquires the lock. Once the thread acquires the lock, it becomes `runnable`.

The wait set is NOT equal to the entry set – it contains threads that are **waiting for a certain condition (NOT WAITING FOR THE LOCK)**.

![](https://natalieagus.github.io/50005/assets/images/week4/3.png)

These sets (entry and waiting) are **per object**, meaning each object instance only has **ONE** lock.

-   Each object can have many synchronized methods.
-   These methods share one lock.

### Synchronised Method (Anonymous)
Below is an how you can declare a synchronized method in a class. The mutex lock is **itself** (`this`). The fact that we don’t use other objects as a lock is the reason why we call this the **anonymous** synchronisation object.

```java
public synchronized returnType methodName(args)
{
       // Critical section here
       // ...
}
```

### Synchronised Statement using Named Object

And below is a synchronized block based on a **specific** named object (not `this` instance).

```java
Object mutexLock = new Object();
public returnType methodName(args)
{
   synchronized(mutexLock)
   {
       // Critical section here
       // ...
   }

   // Remainder section
}
```

You can also do a `synchronized(this)` if you’d like to use a synchronised statement anonymously.
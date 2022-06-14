---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]

If we want to perform fine grained condition synchronization, we can use Java’s **named** [[Conditional variables]] and a [[Reentrant Lock]]. Named conditional variables are created explicitly by first creating a `ReentrantLock()`. The template is as follows:

```java
Lock lock = new ReentrantLock();
Condition lockCondition = lock.newCondition(); // call this multiple times if you have more than 1 condition

// Step 1: LOCK
lock.lock(); // remember, need to lock before calling await()

// Step 2a: WAIT
// To wait for specific condition: 
lockCondition.await();

// OR Step 2b: SIGNAL
// To signal specific thread waiting for this condition: 
lockCondition.signal();
// ... 
// ...

// Step 3: UNLOCK
lock.unlock();
```

At first, we associate a [[Conditional variables]] with a lock: `lock.newCondition()`. This **forces** us to always hold a lock when a condition is being signaled or waited for.

We can modify the example above of N threads which can only progress if `id == turn` to use **conditional variables** as follows:

```java
// Create arrays of condition
Lock lock = new ReentrantLock();
ArrayList<Condition> condVars = new ArrayList<Condition>();
for(int i = 0; i<N; i++) condVars.add(lock.newCondition()); // create N conditions, one for each Thread
```

The Thread function is changed to incorporate a wait to each `condVars[id]`:

```java
// the function
public void doWork(int id)
{
   lock.lock();
   while (turn != myNumber)
   {
       try
       {
             condVars[id].await(); 
	}
       catch (InterruptedException e){}
   }
   // CS
   // assume there's some work to be done here...
   turn = (turn + 1) % 5;
   condVars[turn].signal(); 
   lock.unlock();
}
```
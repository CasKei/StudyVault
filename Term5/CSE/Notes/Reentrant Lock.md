---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]

## Reentrant Lock
[[Re-entrancy]]

A lock is re-entrant if it is **safe** to be acquired **again** by a caller that’s **already holding the lock**. You can create a `ReentrantLock()` object explicitly to allow reentrancy in your critical section.

Java synchronized methods and synchronized blocks with intrinsic lock (recall: every object has an intrinsic lock associated with it) **are reentrant**.

For example, a thread can safely **recurse** on blocks guarded by reentrant locks (sync methods, sync statement)

```java
// Method 1
Public synchronized void foo() {
   // some condition ... 
   foo(x-1); // recurse does not cause error
}

// Method 2
public void foo(int x) {
   synchronized(this) { // note that 'this' is the lock. Otherwise, non-reentrant
	// some condition ... 
       foo(x-1); // recurse does not cause error
   }
}

// Method 3
Object obj1 = new Object(); 
synchronized(obj1){
   System.out.println("Try out object ack 1");
   synchronized(obj1){ // intrinsic lock is reentrant
       System.out.println("Try out obj ack 2"); // will be printed
   }
}
```

- [[Reentrance Lockout]]
- [[Releasing locks]]
- [[Fine-grained Condition Synchronisation]]
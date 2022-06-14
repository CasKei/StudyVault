---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]
[[Java Condition Synchronisation]]
[[Reentrant Lock]]

If you use a **non-reentrant lock** and recurse OR try to acquire the lock again, you will suffer from **reentrance lockout**. We demonstrate it with the custom lock below:

```java
public class CustomLock{

 private boolean isLocked = false;

 public synchronized void lock() throws InterruptedException{
   while(isLocked){
     wait();
   }
   isLocked = true;
 }

 public synchronized void unlock(){
   isLocked = false;
   notify();
 }

}
```

And the usage:

```java
CustomLock lock = new CustomLock()

// Thread 1 code
public void doSomething(int argument){
   lock.lock();
   // recurse
   doSomething(argument-1);
   lock.unlock();
}
```

A thread that calls `lock()` for the first time will **succeed**, but the second call to lock() will be blocked since the variable `isLocked == true`.
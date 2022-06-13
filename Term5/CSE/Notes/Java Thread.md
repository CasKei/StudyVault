---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

# Java Thread
Java threads are managed by the JVM. You can create Java threads in two ways.

## [[The Executor Class|Runnable]] [[Interfaces|interface]]
Implement a [[The Executor Class|Runnable]] [[Interfaces|interface]] and call it using a thread:

1. Implement a runnable interface and its `run()` function

```java
public class MyRunnable implements Runnable {
	public void run(){
		System.out.println("MyRunnable running");
    }
}
```

2. Create a new Thread instance and pass the runnable onto its [[Week 2 - Constructors|constructor]]. Call the `start()` function to begin the execution of the thread:
```java
Runnable runnable = new MyRunnable(); 
Thread thread = new Thread(runnable);
thread.start();
```

## Thread subclass
The second way is to create a **subclass** of `Thread` and override the method `run():`

e.g.
```java
public class CustomThread extends Thread {
	public void run(){
		System.out.println("CustomThread running");
	}
}
```
Create and start `CustomThread` instance to start the thread:
```java
CustomThread ct = new CustomThread();
ct.start();
```

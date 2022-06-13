---
aliases: precedence constraints
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Week 5 - Process Synchronisation]]

## Producer-consumer problem
> 2 **asynchronous** processes or threads are trying to write to and read from the same bounded $N$-character buffer [[Concurrent Programming|concurrent]]ly.

> **Asynchonous** and [[Concurrent Programming|concurrent]]: both processes or threads make progress, but we cannot assume anything about their relative speed of execution.

![](https://natalieagus.github.io/50005/assets/images/week4/1.png)

## Real life examples
In real life, a producer process produces information that is consumed by a consumer process. e.g.
- [[Assemblers and Compilers|Compiler]] (producer) producing [[Assemblers and Compilers|assembly code]] that is consumed by an [[Assembler]] (consumer)
- The [[Assembler]] can also be a producer wrt the **loader**: it produces object modules that are consumed by the loader.
- A web server produces HTML files and images, which are consumed by the client web browser requesting the source.

## Precedence constraints
> For these asynchronous processes:
> -   **Producer cannot produce too much before consumer consumes**
> -   **Consumer cannot consume before producer produces**

## What happens if there is no synchronisation?
If we don't synchronise both [[Week 4 - Processes and Thread management|processes]]/[[Week 4 - Processes and Thread management|threads]], let's see a very simple **producer** program.

Let `counter` and `buffer` of size `N` be a [[Shared Memory|shared variable]] between the producer and the consumer.

`counter` keeps track of how many items there are in `buffer`/
```c
while (true) {
	/* produce an item in next produced */
	while (counter == BUFFERSIZE); /* do nothing */
	buffer[in] = nextproduced;
	in = (in + 1) % BUFFERSIZE;
	counter++;
}
```
And the following very simple **consumer** program:
```c
while (true) {
    while (counter == 0); /* do nothing */
    next consumed = buffer[out]; 
    out = (out + 1) % BUFFERSIZE; 
    counter--;
    /* consume the item in next consumed */
}
```

Each code is correct on its own, but, incorrect when executed [[Concurrent Programming|concurrent]]ly.

We don't know how many lines of assembly is one line of C code, it may be different. If they run concurrently and suddenly switch before their job is done, the other can't do its work.

So, without proper synchronisation attempts, the [[#Precedence constraints]] will be violated.

This is due to the presence of [[Race condition]].
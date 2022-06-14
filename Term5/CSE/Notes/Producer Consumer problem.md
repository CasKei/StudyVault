---
aliases: precedence constraints
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
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

## Sample C code
In this sample, we try to tackle the ==single== producer single consumer problem with counting semaphore. The shared resources will be an integer array named `buffer` in this example, of size `10`.

The idea is to ensure that producer **does not overwrite** unconsumed values, and to ensure that consumer **does not consume anything before** producer puts anything new into the buffer.

Main process to initialise Producer and Consumer Threads:

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <fcntl.h>


#define RESOURCES 10
#define REPEAT 100

sem_t *blank_space;
sem_t *content;

int buffer[RESOURCES];
int write_index = 0;
int read_index = 0;

int main()
{
   // instantiate named semaphore, works on macOS
   // sem_t *sem_open(const char *name, int oflag,
   //                   mode_t mode, unsigned int value);
   // @mode: set to have R&W permission for owner, group owner, and other user
   blank_space = sem_open("blank_space", O_CREAT,
                          S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH,
                          RESOURCES);
   printf("%p \n", (void *)blank_space);
   if (blank_space == (sem_t *)SEM_FAILED)
   {
       printf("Sem Open Failed.\n");
       exit(1);
   }
   content = sem_open("content", O_CREAT,
                      S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH,
                      0);
   printf("%p \n", (void *)content);
   if (content == (sem_t *)SEM_FAILED)
   {
       printf("Sem Open Failed.\n");
       exit(1);
   }

   pthread_t producer, consumer;
   pthread_create(&producer, NULL, producer_function, NULL);
   pthread_create(&consumer, NULL, consumer_function, NULL);

   printf("Joining threads\n");
   pthread_join(producer, NULL);
   pthread_join(consumer, NULL);

   // if you don't destroy, it persists in the system
   // run the command: ipcs -s
   // to remove: ipcrm -s <sem_id>
   sem_unlink("blank_space");
   sem_unlink("content");
   return 0;
}
```

Producer Thread instruction:

```c
void *producer_function(void *arg)
{
   for (int i = 0; i < REPEAT; i++)
   {
       // wait
       sem_wait(blank_space);
       // write to buffer
       buffer[write_index] = i;
       // advance write pointer
       write_index = (write_index + 1) % RESOURCES;
       // signal
       sem_post(content);
   }

   return NULL;
}
```

Consumer Thread instruction:

```c
void *consumer_function(void *arg)
{
   for (int i = 0; i < REPEAT; i++)
   {
       // wait
       sem_wait(content);
       // read from buffer
       int value = buffer[read_index];
       printf("Consumer reads: %d \n", value);
       // advance write pointer
       read_index = (read_index + 1) % RESOURCES;
       // signal
       sem_post(blank_space);
   }

   return NULL;
}
```

Paste the two functions above before `main()`. After you compile and run the code, you should have an output as such where consumer thread nicely prints out the numbers put into the buffer by producer in sequence (and stops at 100):

![](https://natalieagus.github.io/50005/assets/images/week4/2.png)
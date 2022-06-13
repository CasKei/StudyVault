---
aliases: pthread
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

# C Thread
We can also equivalently create threads in C using the `pthread` library. The code below shows how we can create threads in C:

1.  Create a **function** with `void*` return type (generic return type)
2.  Use `pthread_create` to **create** a thread that executes this function
3.  Use `pthread_join` to **wait** for a thread to finish

## Program: pthread creation
We can pass **arguments** to a thread, **wait** for its completion and get its **return** value.

==Threads from the same process share heap and data==. A global variable like `shared_integer` in the example below is **visible** to both main thread and created thread.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int shared_integer; // instantiate integer in fixed memory

void *customThreadFunc(void *vargp)
{
   sleep(1);
   char argument = *(char *)vargp;
   printf("Printing helloWorld from spawned thread with argument: %c\n", argument);
   shared_integer++;

   char answer = 'a'; // in stack
   char *answer_heap = malloc(sizeof(char)); // in heap

   *answer_heap = 'a';
   pthread_exit((void *)answer_heap);

   // pthread_exit((void *) &answer); // will result in segfault
}

int main()
{
   shared_integer = 10;
   pthread_t thread_id;

   char input_argument = 'b'; // to pass to thread
   char *result;              // to hold return value

   // pthread_create(pthread_t* thread_id, NULLABLE thread attributes, void* function_for_thread, NULLABLE void* argument)
   pthread_create(&thread_id, NULL, customThreadFunc, &input_argument);

   sleep(1);
   printf("shared_integer: %d\n", shared_integer); // potential race condition

   // pthread_join(pthread_t thread_id, void return_value);
   // Second argument of type void : pass the address of "result", which is a pointer to the supposed return value of the thread

   // blocking
   pthread_join(thread_id, (void )&result);
   printf("After thread join...\n");

   printf("shared_integer: %d\n", shared_integer);
   printf("result: %c\n", *result);

   exit(0);
}
```

## Return value
In the example above, we created `answer_heap` using [[C dynamic memory allocation|malloc]], therefore this answer resides in the `heap` (shared with all threads in the entire process, persists for as long as the process is not terminated).

However, if we **return** a [[C pointer|pointer]] to variable that’s initialized in the thread’s **stack**, then you will end up with a **segfault error**.


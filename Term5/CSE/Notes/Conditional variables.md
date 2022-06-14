---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section problem]]
[[Critical section solutions]]

## Conditional Variables
Conditional variables allow a process or thread to wait for completion of a given **event** on a particular object (some shared state, data structure, anything). It is used to **communicate** between processes or threads when certain conditions become `true`.

> The “**event**” is the _change_ in state of some condition that thread is interested in. Until that is satisfied, the process waits to be awakened later by a signalling process/thread (that actually **changes** the condition).

Conditional variables are and **should** always be implemented with [[Mutex lock]]s. When implemented properly, they provide **condition synchronization**.

For example, we can initialize a [[Mutex]] guarding certain CS:

```c
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
```

And in this example, we assume that a particular CS in Process/Thread 2 cannot be executed if `bool x == false`. Therefore we can create a condition to represent this:

```c
pthread_cond_t cond_x = PTHREAD_COND_INITIALIZER;
```

Now consider Process/Thread 1 instructions:

```c
pthread_mutex_lock(&mutex);
// CRITICAL SECTION
// ...
cond_x = true;
pthread_cond_signal(&cond);
pthread_mutex_unlock(&mutex);
```

… and Process/Thread 2 instructions:

```c
pthread_mutex_lock(&mutex);
while (cond_x == false){
   pthread_cond_wait(&cond_x, &mutex);  // yields mutex, sleeping
}
// CRITICAL SECTION, can only be executed iff cond_x == true
// ...
pthread_mutex_unlock(&mutex);
```

It is clear that the [[Mutex]] guards the CS. However, Process 2 should **not** proceed to its CS if `cond_x` is `false` in this example.

Process 2 can be put to sleep by calling `condition_wait()`; the implementation of this function is integrated into the process scheduler which does the following:

-   It **gives** up the [[Mutex]] **AND**
-   **Sleeps**, will not [[Spinlock|busy wait]]

When Process 1 has set the variable `cond_x` into `true`, it signals Process 2 to **continue** before **giving** up the [[Mutex]].

-   It is important to call `wait()` after acquiring the mutex and checking the condition.
    -   You cannot use `unlock()` to release the mutex.
-   When Process 2 `waits` and eventually sleep, it will **give** up the lock so as to allow other threads needing the lock to proceed.
-   When Process 2 has woken up from the `wait()`, it **automatically** reacquires the mutex lock
    -   If Process 1 hasn’t given up the lock, Process 2 will not execute although `cond_x` has been fulfilled

> This is crucial because it will re-check the state of `cond_x` again before continuing to the [[Critical section]]. It is also crucial to re-check `cond_x` before continuing to the CS. **Why?**


A conditional variable is effectively a **signalling** mechanism under the [[Complete Process Context|context]] of a given [[Mutex lock]]. With mutex lock alone, we cannot easily block a process out of its [[Critical section]] based on any **arbitrary condition** even when the [[Mutex]] is **available**.

## Sample C code
Consider a main function with a shared variable `count`, two `mutexes` and one `condition`:

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t condition_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condition_cond = PTHREAD_COND_INITIALIZER;

void *functionCount1();
void *functionCount2();
int count = 0;
#define COUNT_DONE 10
#define COUNT_HALT1 3
#define COUNT_HALT2 6

int main()
{
  pthread_t thread1, thread2;

  pthread_create(&thread1, NULL, &functionCount1, NULL);
  pthread_create(&thread2, NULL, &functionCount2, NULL);
  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);

  return 0;
}
```

Suppose an example where we Thread 1 running `functionCount1()` is to be **halted** whenever the `count` value is between 3 (`COUNT_HALT1`) and 6 (`COUNT_HALT2`).

-   Otherwise, either thread can increment the counter.
-   We can use the condition variable and condition wait to ensure this behavior in `functionCount1()`:

```c
void *functionCount1()
{
  for (;;) // equivalent to while(true)
  {
     pthread_mutex_lock(&count_mutex);
     while (count >= COUNT_HALT1 && count <= COUNT_HALT2)
     {
        pthread_cond_wait(&condition_cond, &count_mutex);
     }

     count++;
     printf("Counter value functionCount1: %d\n", count);
     pthread_mutex_unlock(&count_mutex);

     if (count >= COUNT_DONE)
        return (NULL);
  }
}
```

We can then use `cond_signal` in `functionCount2()` executed by Thread 2:

```c
void *functionCount2()
{
  for (;;) // equivalent to while(true)
  {
     pthread_mutex_lock(&count_mutex);
     if (count < COUNT_HALT1 || count > COUNT_HALT2)
     {
        pthread_cond_signal(&condition_cond);
     }
     count++;
     printf("Counter value functionCount2: %d\n", count);
     pthread_mutex_unlock(&count_mutex);

     if (count >= COUNT_DONE)
        return (NULL);
  }
}
```
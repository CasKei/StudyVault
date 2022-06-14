---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

## Mutex
> Mutually exclusive.

https://en.wikipedia.org/wiki/Mutual_exclusion

A property of [[Concurrent Programming|concurrency]] control, to prevent [[Race condition]]s. It is the requirement that one thread never enters a [[Critical section]] while a [[Concurrent Programming|concurrent]] thread of execution is already accessing [[Critical section]], which refers to an interval of time during which a thread of execution accesses a [[Shared Memory|shared resource]].

The [[Shared Memory|shared reource]] is a data object which 2 or more concurrent threads are trying to modify. Mutex algo ensures that if a process is writing on a data, no other object can write to the same data until this process finished.

```whatever
When I am having a big heated discussion at work, I use a rubber chicken which
I keep in my desk for just such occasions.
The person holding the chicken is the only person who is allowed to talk.
If you don't hold the chicken you cannot speak.
You can only indicate that you want the chicken and wait until you get it
before you speak.
Once you have finished speaking, you can hand the chicken back to the moderator
who will hand it to the next person to speak.
This ensures that people do not speak over each other, and also have their own
space to talk.

Replace Chicken with Mutex and person with thread and you basically have
the concept of a mutex.

Of course, there is no such thing as a rubber mutex. Only rubber chicken.
My cats once had a rubber mouse, but they ate it.

Of course, before you use the rubber chicken, you need to ask yourself whether
you actually need 5 people in one room and would it not just be easier with
one person in the room on their own doing all the work.
Actually, this is just extending the analogy, but you get the idea.
```

## Sample C code
In the example below, we attempt to increase a shared variable `counter`, guarded by a `mutex` to prevent [[Race condition]].
```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *functionC();
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int counter = 0;

int main()
{
  int rc1, rc2;
  pthread_t thread1, thread2;

  /* Create independent threads each of which will execute functionC */

  if ((rc1 = pthread_create(&thread1, NULL, &functionC, NULL)))
  {
     printf("Thread 1 creation failed: %d\n", rc1);
  }

  if ((rc2 = pthread_create(&thread2, NULL, &functionC, NULL)))
  {
     printf("Thread 2 creation failed: %d\n", rc2);
  }

  // Main thread waits until both threads have finished execution

  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);

  return 0;
}

void *functionC()
{
  pthread_mutex_lock(&mutex);
  counter++;
  printf("Counter value: %d\n", counter);
  pthread_mutex_unlock(&mutex);
}
```
---
aliases: ipcs, ipcrm
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]
[[Interprocess Communication]]

## POSIX Shared Memory
Shared memory is a region in the RAM that can be **created** and shared among multiple processes using [[System calls]].

1.  [[OS Kernel]] **allocates** and **establishes** a region of memory and return to the caller process.
2.  Once shared memory is established, all accesses are treated as routine **user memory accesses** for writing or reading to or from it, and **no assistance from the kernel is required**.

## Procedure
> This section is here to enhance your understanding. You can skip this if you want.

Both reader and writer get the shared memory identifier (an integer) using system call `shmget`. `SHM_KEY` is an integer that has to be unique, so any program can access what is inside the shared memory if they know the `SHM_KEY`. The Kernel will return the memory identifier associated with `SHM_KEY` if it is already created, or create it when it has yet to exist. The second argument: `1024`, is the size (in bytes) of the shared memory.

```c
int shmid = shmget(SHM_KEY, 1024, 0666 | IPC_CREAT);
```

Then, both reader and writer should attach the shared memory onto its address space (i.e: map the allocated segment in physical memory to the VM space of the calling process). You can type cast the return of `shmat` onto any data type you want. In essence, `shmat` returns an address of your address space that translates to the shared memory block[1](https://natalieagus.github.io/50005/os_notes/week3_comms#fn:6).

```c
char *str = (char*) shmat(shmid, (void*)0, 0);
```

Afterwards, writer can write to the shared memory:

```c
sprintf(str, "Hello world \n");
```

Reader can read from the shared memory:

```c
printf("Data read from memory: %s\n", str);
```

The figure below illustrates the steps above: ![](https://natalieagus.github.io/50005/assets/images/week3/13.png)

Once both processes no longer need to communicate, they can detach the shared memory from their address space:

```c
shmdt(str);
```

Finally, one of the processes can destroy it, typically the reader because it is the last process that uses it.

```c
shmctl(shmid, IPC_RMID, NULL);
```

Of course one obvious issue that might happen here is that BOTH writer and reader are accessing the shared memory concurrently, therefore we will run into **synchronisation** problems whereby **writer overwrites before reader finished reading** or **reader attempts to read an empty memory value before writer finished writing**.

We will address such synchronisation problems in the next chapter.

## IPC without SVC
[[Supervisor Call|SVC]]
Will the value of `shared_int` and `shared_float` be the same in the parent and child process?

```c
#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
   pid_t pid;

   int shared_int = 10;

   static float shared_float = 25.5;

   pid = fork();

   if (pid < 0)
   {
       fprintf(stderr, "Fork has failed. Exiting now");
       return 1; // exit error
   }
   else if (pid == 0)
   {
       shared_int++;
       printf("shared_int in child process: %d\n", shared_int);
       shared_float = shared_float + 3;
       printf("shared_float in child process: %f\n", shared_float);
   }
   else
   {
       printf("shared_int in parent process: %d\n", shared_int);
       printf("shared_float in parent process: %f\n", shared_float);
       wait(NULL);
       printf("Child has exited.\n");
   }
   return 0;
}
```

## IPC with SVC(unsync)
Parent and child processes can share the same segment, but we are faced with a **synchronization** problem, something called “race condition” (next week’s material).

```c
#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main(int argc, char const *argv[])
{
   pid_t pid;
   int *ShmPTR;
   int ShmID;

   /**
       This process asks for a shared memory of 4 bytes (size of 1 int) and attaches this
       shared memory segment to its address space.
    **/

   ShmID = shmget(IPC_PRIVATE, 1 * sizeof(int), IPC_CREAT | 0666);
   if (ShmID < 0)
   {
       printf("* shmget error (server) *\n");
       exit(1);
   }

   /**
       SHMAT attach the shared memory to the process
       This code is called before fork() so both parent
       and child processes have attached to this shared memory.

       Pointer ShmPTR contains the address to the shared memory segment.
    **/

   ShmPTR = (int *)shmat(ShmID, NULL, 0);

   if ((int)ShmPTR == -1)
   {
       printf("* shmat error (server) *\n");
       exit(1);
   }
   printf("Parent process has created a shared memory segment.\n");

   pid = fork();

   if (pid < 0)
   {
       fprintf(stderr, "Fork has failed. Exiting now");
       return 1; // exit error
   }
   else if (pid == 0)
   {
       *ShmPTR = *ShmPTR + 1; // dereference ShmPTR and increase its value
       printf("shared_int in child process: %d\n", *ShmPTR);
   }
   else
   {
       printf("shared_int in parent process: %d\n", *ShmPTR); // race condition
       wait(NULL); // move this above the print statement to see the change in ShmPTR value
       printf("Child has exited.\n");
   }
   return 0;
}
```

## Removing Shared Memory
In the code above, we didn’t detach and remove the shared memory, so it still persists in the system. Run the command `ipcs -m` to view it. To remove it, run the command `ipcrm -m [mem_id]`
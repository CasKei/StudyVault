---
aliases: fork, process tree, execlp, fork tree, pid
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]
[[Operations on Processes]]

## fork()
We can create new processes using `fork()` [[System calls]].

1.  The process creator is called a **parent** process, the new processes are called the **children** of that process.
2.  Each of these new processes may in turn create more child processes, forming a **tree** of processes.

## Process Tree
We can illustrate multiple process creation as a **process tree**:

![](https://natalieagus.github.io/50005/assets/images/week3/8.png)

In the example above, there are 5 processes in total. Process 2,3, and 4 are direct **children** of Process 1. Process 5 is created by Process 2.

## Process Id
> Each process is identified by an integer called the process id (`pid`). Pid is **unique** in the system.

You can type the command `ps [options]` to observe all running processes in your system, along with the `pid` of each process. For instance,

![](https://natalieagus.github.io/50005/assets/images/week3/9.png)

**Why? Don't they have a name? Is it necessary?**\
It cheaper to identify them by integers. Faster to compare integers than to compare a string. Same as path system. The paths each have its id. Files also have their id. Kernel does not work with string comparisons or namespace.

## Child Process vs Parent process
The **new** process consists of the ==entire copy of the address space== (code, stack, process of execution, etc) of the **original** parent process at the point of `fork()`.

> In other words, the child process inherits the parent process’ state **at the point of** `fork()`.

Parent and child processes operate in **different address space** (isolation). Since they are different processes, parent and children processes execute **concurrently**.

Practically, a parent process **waits** for its children to terminate (using `wait()` system call) to read the child process’ exit status and **only then** its [[Process table and Process control block|PCB]] entry in the [[Asynchronous Interrupt Handler|process table]] can be removed.

Child processes **cannot** `wait` for their parents to terminate. Since children processes are a duplicate of their parents (inherits the whole address space), they can either

1.  **Execute** the same instructions as their parents [[Concurrent Programming|concurrent]]ly, or
2.  **Load** a new program into its address space

## How fork works
### Example
It is best to explain how `fork()` process creation works by example.

```c
#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
   pid_t pid;

   pid = fork(); // parent executes fork. 
   // lets call this addr A. Both PC of child and parent is at addr A
   printf("pid: %d\n", pid);

   if (pid < 0)
   {
       fprintf(stderr, "Fork has failed. Exiting now");
       return 1; // exit error
   }
   else if (pid == 0)
   {
       execlp("/bin/ls", "ls", NULL);
   }
   else
   {
       wait(NULL);
       printf("Child has exited.\n");
   }
   return 0;
}
```

The simple C program above is executed and when the execution system call `fork()` returns, **two processes are present**.

![](https://natalieagus.github.io/50005/assets/images/week3/10.png)

Both have the **same** copy of the text (code) and resources (any opened files, etc). The parent process is **cloned**, resulting in the child process. They’re at a **different** address space, executed [[Concurrent Programming|concurrent]]ly by the system.

### fork return value
> `fork()` returns 0 in the child process while in the parent process it returns the pid of the child (>0).

We can write just **one instruction** for **both parent and child process** but each will take a different **branch** of the `if` clause. In the example code above:

-   The child executes the line if-clause: `execlp`
-   The parent process executes the `else` clause where it `wait` for the child process to `exit`

![](https://natalieagus.github.io/50005/assets/images/week3/11.png)

### execlp
`execlp` is a [[System calls]] that loads a new program called `ls` onto the child process’ address space, effectively **replacing** its text (code), data, and stack content.

### wait
Concurrently, the parent process executes `wait(NULL)`, which is a system call that **suspends** the parents’ execution until this child process that is executing `ls` has returned.
This is a [[Types of system calls|blocking]] [[System calls]].

## The fork tree
**Compile** and **run** the C program below.

How many processes are created in total? (excluding the parent process). Can you draw the process tree?

```c
#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
   int level = 3;
   pid_t pid[level];

   for (int i = 0; i < level; i++)
   {
       pid[i] = fork();

       if (pid[i] < 0)
       {
           fprintf(stderr, "Fork has failed. Exiting now");
           return 1; // exit error
       }
       else if (pid[i] == 0) // this is in child process
       {
           printf("Hello from child %d \n", i);
       }
   }

   return 0;
}
```

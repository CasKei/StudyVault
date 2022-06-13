---
aliases: exit, kill, wait, waitpid
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]
[[Operations on Processes]]

## Process termination
A process needs certain resources (CPU time, memory, files, I/O devices) to run and accomplish its task. These resources are **limited**.

> A process can terminate **itself** using `exit()` [[System calls]]. A process can also terminate **other processes** using the `kill(pid, SIGKILL)` system call.

Once a process is terminated, these resources are **freed** by the kernel for **other** processes. Parent processes may **terminate** or **abort** its children as it knows the `pid` of its children.

## Orphaned processes
If a parent process with live children is terminated, the children processes become **orphaned** processes:

-   Some operating system is designed to either **abort** all of its orphaned children (cascading termination) or
-   **Adopt** the orphaned children processes (`init` process usually will adopt orphaned processes)

#### About `init`

In UNIX-like OS, `init` is the first process started by the kernel during [[Booting]] of the computer system. `Init` is a [[Daemon Processes]] that continues running until the system is shut down (see [[Daemon Processes]]). It is the direct or indirect **ancestor** of all other processes, and automatically adopts all orphaned processes.

`Init` is a **user** process like any other processes, and hence it is using virtual memory. The only special thing about `init` is that it is one of the two processes that the kernel started initially. When `init` is started by the kernel, it goes into user mode. When `init` calls system call `fork(),` it traps into the kernel mode, and the kernel does certain things to _create the new process,_ and the new process _will be scheduled in the future._ When the `fork()` returns, the original process is back to user mode. The equivalent of `init` in macOS is [`launchd`](https://en.wikipedia.org/wiki/Launchd).

## Zombie processes
> **Zombie** processes are processes that are **ALREADY TERMINATED**, and memory as well as other resources are **freed**, but its exit status is not read by their parents, hence its **entry** ([[Process table and Process control block|PCB]]) in the [[Asynchronous Interrupt Handler|process table]] remains.

A parent process **must** call `wait` or `waitpid` to read their children’s exit status. A call to `wait` or `waitpid` **blocks** the calling process until one of its child processes exits or a signal is received. **Otherwise, their child process becomes a zombie process.**

-   Children processes can **terminate** themselves after they have finished executing their tasks using `exit(int status)` system call.
-   The kernel will **free** the memory and other resources from this process, **but not the PCB entry**.
-   Parent processes are supposed to call `wait` or `waitpid` to obtain the exit status of a child.
-   Only after `wait` or `waitpid` in the parent process returns, the kernel can **remove** the child PCB entry from the system wide process table.
-   If the parents didn’t call `wait` or `waitpid` and instead continue execution of other things, then children’s entry in the pcb remains; **a zombie process remains**.
    -   A zombie process generally takes up very little memory space, but `pid` of the child remains
    -   Recall that pid is **unique**, hence in a 32-bit system, there’re only 32768 available pids.

Having too many zombie processes might result in inability to create new processes in the system, simply because we may run out of pid.

> Note: if a parent process has died as well, then all the zombie children will be **cleared** by the kernel. To **observe** zombie children, you need to artifically suspend the parent process after the children have terminated.

All processes transition to this zombie state when they terminate, but generally they exist as zombies only **briefly**. Once the parent calls `wait, waitpid` the `pid` of the zombie process and its entry in the process table are released.

## Zombie making
**Compile** and **run** the C program below. It will suspend itself at `scanf`, waiting for input at `stdin`. Do not type anything, leave it hanging there.

What’s the (possible) maximum number of zombies created by this process?

```c
#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    int level = 5;
    pid_t pid[level];

    for (int i = 0; i < level; i++)
    {
        pid[i] = fork();

        if (pid[i] < 0)
        {
            fprintf(stderr, "Fork has failed. Exiting now");
            return 1; // exit error
        }
        else if (pid[i] == 0)
        {
            printf("Hello from child %d \n", i);
            return 0;
        }
    }

    int testInteger;
    printf("Enter an integer: "); // artificially blocking parent
    scanf("%d", &testInteger);

    return 0;
}
```

We can enter the `ps aux | grep 'Z'` command to list all zombie processes in the system caused by running the program above. ![](https://natalieagus.github.io/50005/assets/images/week3/12.png)
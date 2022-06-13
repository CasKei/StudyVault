---
aliases: FreeBSD
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[Week 4 - Processes and Thread management]]
[[System calls]]
[[Process Control]]

There are so many facets of and variations in process and job control that we need to clarify using examples: [[Single-tasking system|MS-DOS]] and [[Multi-tasking system|FreeBSD]].
![](https://natalieagus.github.io/50005/assets/images/week2/7.png)

#### Multi-tasking system

An example of a multi-tasking system is FreeBSD. The FreeBSD operating system is a **multi-tasking** OS that is able to create and manage multiple processes at a time:

-   When a user logs on to the system, the **shell** (command interpreter) of the user’s choice is run.
-   This shell is similar to the MS-DOS shell in that it accepts commands and executes programs that the user requests.
-   However, since FreeBSD is a multitasking system, the command interpreter may **continue running** while another program is executed:
    -   The possible state of a RAM with FreeBSD OS is as shown in the figure above
    -   To **start** a new process, the shell executes a `fork()` system call.
    -   Then, the selected program is loaded into memory via an `exec()`[8](https://natalieagus.github.io/50005/os_notes/week2_syscall#fn:9) system call, and the program is executed normally until it executes `exit()` system call to end normally or `abort` system call.
-   Depending on the way the command was issued, the shell then either **waits** for the process to finish or runs the process “in the background.”
    -   In the latter case, the shell immediately requests another command.
-   The kernel is responsible to ensure that [[Context switch]]ing is properly done (and [[Timesharing]] as well if enabled).

To run a command in the background, add the ampersand symbol (`&`) at the end of the command:

```nasm
command &
```
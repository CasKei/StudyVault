---
aliases: MS-DOS
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[Week 4 - Processes and Thread management]]
[[System calls]]
[[Process Control]]

There are so many facets of and variations in process and job control that we need to clarify using examples: [[Single-tasking system|MS-DOS]] and [[Multi-tasking system|FreeBSD]].
![](https://natalieagus.github.io/50005/assets/images/week2/7.png)

#### Single-tasking System

An example of a single-tasking system is MS-DOS, shown in the figure on the left.

-   It has a simple command **interpreter** (that is invoked when the computer is started as shown in the figure above, labeled as (a)).
-   Upon opening a new program, it **loads** the program into memory, **writing over most of itself** (note the shrinking portion of command interpreter codebase) to give the program **as much memory as possible** as shown in (b) above.

Next, it sets the **instruction pointer** to the first instruction of the program.

-   The program then runs, and either an **error** causes a [[Software Interrupt|trap]], or the program executes a [[System calls|system call]] to **terminate**.
-   In either case, the error code is saved in the system memory for later use.

Following this action, the **small** portion of the command interpreter that was not overwritten resumes execution:

-   Its first task is to reload the rest of the command interpreter from disk.
-   Then the command interpreter makes the previous error code available to the user or to the next program.
-   It stands by for more input command from the user.
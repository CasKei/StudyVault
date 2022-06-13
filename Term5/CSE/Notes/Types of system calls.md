---
aliases: blocking, non-blocking, blocking or non-blocking
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[System calls]]

## Types of system calls
In general, each OS will provide a **list** of system calls that it supports. System calls can be grouped (but not limited to) roughly into six major categories: [[OS Services]]

1.  [[Process Control]]: end, abort, load, execute, create and terminate processes, get and set process attributes, wait for time, wait for event, signal event, allocate, and free memory
2.  **File manipulation**: create, delete, rename, open, close, read, write, and reposition files, get, and set file attributes
3.  **Device manipulation**: request and release device, read from, write to, and reposition device, get and set device attributes, logically attach or detach devices
4.  **Information maintenance**: get or set time and date, get or set system data, get or set process, file, or device attributes
5.  **Communication**: create and delete pipes, send or receive packets through network, transfer status information, attach or detach remote devices, etc
6.  **Protection**: set network encryption, protocol

If you are curious about Linux-specific system call types, you can find the list [here](http://asm.sourceforge.net/syscall.html).

## Blocking vs Non-Blocking System call
> A **blocking** system call is one that must **wait** until the action can be completed.

For instance, `read()` is **blocking**:

-   If no input is ready, the calling process will be **suspended**
    -   `yield()` the remaining quanta, and schedule other processes first
-   It will only resume execution after some input is ready. Depending on the scheduler implementation it may either:
    -   Be scheduled again and **retry** (e.g: round robin)
        -   The process re-executes `read()` and may `yield()` again if there’s no input.
        -   Repeat until successful.
    -   **Not** scheduled, use some `wait` flag/status to tell the scheduler to not schedule this again unless some input is received
        -   `wait` flag/status cleared by interrupt handler (more info in the next topic)

> On the other hand, a **non blocking** system call can return almost immediately without waiting for the I/O to complete.

For instance, [`select()`](https://linux.die.net/man/2/select) is non-blocking.

-   The `select()` system call can be used to **check** if there is new data or not, e.g: at `stdin` file descriptor.
-   Then a blocking system call like `read()` may be used afterwards knowing that they will complete immediately.
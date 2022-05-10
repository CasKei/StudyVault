---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]

## What
> **Trap**
> A type of **synchronous interrupt** caused by an exceptional condition when the [[Anatomy of the Beta CPU|CPU]] executes an instruction, such as illegal operations, division by zero, invalid memory access, system calls, etc.

This results in a switch to [[Kernel mode and User mode|kernel mode]] via **trap handler** (e.g `PC <- ILLOP`).
The handler will examine the cause of the trap, and perform appropriate action (if possible) before returning control to the originating process.

If not possible to return control, kernel may choose to terminate it.

User processes do not have privileged access, meaning that they do not directly control the use of any hardware I/O devices, such as getting keyboard input, mouse click, perform disk saves, etc, _without the help of the OS Kernel program_.

This is because hardware devices **are actually shared** among all processes in the system, but their programs are written with complete disregard for other processes in the memory.

Therefore, user processes may utilise **traps** to synchronously interrupt themselves, and _legally_ switch to the [[Kernel mode and User mode|kernel mode]] whenever they need access to the I/O devices (or other kernel services).

There are many types of Kernel services, one of them includes read/write access from/to the I/O devices. They are typically _indexed_, and the process needs to leave the index of the needed system call in `Reg[R0]` before trapping itself to the Kernel Program. We will learn about Kernel services next term.

The datapath in the event of _illegal operation_ is:
![](https://natalieagus.github.io/50002/assets/contentimage/beta/illop.png)

During this event,
-   [[Anatomy of the Beta CPU|CLU]] sets `PCSEL = 011`, and saves `PC+4` into `Reg[XP]`
-   The [[Anatomy of the Beta CPU|PC]] will execute the instruction at location `ILLOP` in the _next cycle_ where the illegal operation handler resides.
-   The _illop_ handler will look at `Reg[R0]` and invoke the right _service routine_ to provide the requested service.
    -   Upon returning, the service routine will put its return the result in `Reg[R0]`.
-   The _illop_ handler resumes the execution of the originating process:
    -   `Reg[XP] = Reg[XP] -4`
    -   `JMP[XP]`

One common scenario where a process running in user mode needs the Kernel service is when it asks for keyboard / mouse input, for example:
```C
int c;
c = getchar();
```

The function `getchar` contains several instructions that perform a **supervisor call** in order to fetch any character input from the keyboard. When translated into assembly, the supervisor call is made by _trapping_ the process into the _illop_ handler, thus **transferring** CPU control to the Kernel so that it can fetch any character input from the keyboard, and **resuming** the process execution after the task is done.

The process stores the character input left at `Reg[R0]` by the Kernel into memory location `c`.
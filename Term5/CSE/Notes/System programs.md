---
aliases: system utilities
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]

## What
> System programs, also known as system **utilities**, provide a convenient environment for program development and execution:

1.  They are **basic** tools used by many users for common low-level activities.
2.  These tools are very **generic**, thus can be considered as part of the “system” instead of individual user apps that we typically install
3.  Note that sometimes system programs and [[System calls]] have the same name, but they are nowhere the same. For example: _
    1.  `write` as a command that can be typed on the terminal (type `man write` to find out what these arguments are.)[1](https://natalieagus.github.io/50005/os_notes/week2_designstructure#fn:10)
    2.  `write` is also a system call API and an actual system call name

> System programs runs on [[Kernel mode and User mode|user mode]], just like any other user-level applications. When it requires kernel services, they make [[System calls]] just like any other [[User Programs]].

[[System vs Application Programs]]

## Categories
### Package Managers: file management and modification
These programs create, delete, copy, rename, print, dump, list, and generally manipulate files and directories. For example: all commands that you can enter in [[CLI]] that involves file management in UNIX systems is actually the **name** of system programs that can be found in the `$PATH`. These include `ls, rm, mkdir, cp, touch` among many others.

Modern OS usually comes with default **package managers** that simplifies installation of softwares (and also managing versions, updates, running background services, etc). For instance, `brew` for macOS and `apt` for Debian-based Linux distributions.

Several text editors provided (`nano`, `vi`) may be available to create and modify the content of files stored on disk or other storage devices. There may also be special commands to search the contents of files or perform transformations of the text like `grep, awk, tr`.

### Status information
Some programs simply ask the system for various status **information**: date, time, amount of available memory or disk space, number of users, etc. Others are more complex, providing detailed performance, logging, and debugging information. Example include `top, ls, df` among many others.

Typically, these programs format and print the output to the terminal or other output devices or files or display it in a window of the [[GUI]]. Some systems also support a **registry**, which is used to store and retrieve system **configuration** information.

### Programming-language support
**Compilers**, **assemblers**, **debuggers**, and **interpreters** for common programming languages (such as C, C++, Java, and Python) are often provided with the operating system or available as a separate download. Package managers such as `npm, pip` are also available by default in modern OS to make it easier for users to develop.

### Program loading and execution
Once a program is assembled or compiled, it must be **loaded** into memory to be executed. The system may provide absolute **loaders**, relocatable loaders, **linkage** editors, and overlay loaders. Runtime debugging systems for either higher-level languages or machine language are needed as well.

### Communications
These programs provide the mechanism for creating **virtual** connections among processes, users, and computer systems. They allow users to send messages to one another’s screens, to browse Web pages, to send e-mail messages, to log in remotely, or to transfer files from one machine to another. Example include `ssh, pipe (|)`.

### Background services
All general-purpose systems have methods for **launching** certain system-program processes at boot time (upon startup): network-related system programs, some [[Device Driver]]s (although there are drivers that run in [[Kernel mode and User mode|kernel mode]], these are not system programs), etc

-   Constantly running system-program processes are known as **services**, **subsystems**, or **daemons**.
-   One example is the network daemon:
    -   A system needed a service to **listen** for network connections in order to connect those requests to the correct processes.
-   Other daemon examples include:
    -   The `init` process (specifically called`systemd` in Linux, `launchd` in macOS)
    -   Process **schedulers** that start processes according to a specified schedule,
    -   System **error monitoring** services,
    -   Print **servers**

Typical systems have **dozens** of daemons. In addition, operating systems that run important activities in user mode rather than in kernel mode may use daemons to run these activities.
---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[OS Interfaces]]

## What
> Command Line Interface / Command Interpreter
> Allows direct command entry

Sometimes implemented in [[OS Kernel]], sometimes by [[System programs]]

Sometimes multiple flavours implemented -- [[shell]]s

CLI provides means of interacting with a computer program where the user issues **successive** commands to the program in the form of text. The program which handles this interface feature is called a command-line interpreter. We have experimented with this during Lab 1.

## Command Line Interpreter
In `UNIX` systems, the particular program that acts as the **interpreters** of these commands are known as **shells**. Users typically interact with a Unix shell via a [[#Terminal Emulator]], or by **directly** writing a shell script that contains a bunch of successive commands to be executed.

For a system that comes with multiple command line interpreters (shells), a user may choose which one to use. Common shells are the Bourne shell, C-shell, Bourne-Again shell, and Korn shell.

-   [Bourne-Again shell](https://www.ibm.com/docs/en/aix/7.1?topic=shells-bourne-shell) (bash): written as part of the GNU Project to provide a superset of Bourne Shell functionality. This shell can be found installed and is the default interactive shell for users on most Linux distros and macOS systems.

![](https://natalieagus.github.io/50005/assets/images/week1/17.png)

-   [Z shell](https://zsh.sourceforge.io) (zsh) is a relatively modern shell that is backward compatible with bash. It’s the default shell in macOS since 10.15 Catalina.

![](https://natalieagus.github.io/50005/assets/images/week1/18.png)

-   [PowerShell](https://docs.microsoft.com/en-us/powershell/) – An object-oriented shell developed originally for Windows OS and now available to macOS and Linux.

In short, the shell primarily **interprets** a series of commands from the user and executes it. There are two ways to implement commands:

1.  **Built-in**: the command interpreter itself contains the code to execute the command.
    -   For example, a command to **delete** a file may cause the command interpreter to jump to a section of its code that sets up the parameters and makes the appropriate system call.
    -   In this case, the number of commands that can be given determines the size of the command interpreter, since each command requires its own implementing code.
2.  **System programs** (typically found in default `PATH` such at `/usr/bin`): command interpreter does not understand the command in any way; it merely uses the command to identify a file to be loaded into memory and be executed. This is used by UNIX, among other operating systems.
    -   You can type `echo $PATH` on your terminal to find out possible places on where these system programs are.

You will be required to implement a Shell in Programming Assignment 1.

## Terminal Emulator
A terminal emulator is a **text-based** user interface (UI) to provide easy access for the users to issue commands. Examples of terminal emulators that we may have encountered before are [iTerm](https://iterm2.com), MacOS terminal, [Termius](https://termius.com), and Windows Terminal.

Almost every system-administrative actions that we can perform on the OS GUI can be done via the CLI. For example, if we want to delete a file in different locations using the OS GUI, we need to perform the following steps:

1.  Hover our mouse to click folder after folder until we arrive at a final folder where the target file resides
2.  Right click, press delete (or use keyboard shortcut)
3.  Repeat until all files are deleted in various paths

Equivalently, we can perform the same action using the CLI. In UNIX systems, we can write the following commands in our terminal emulator:

1.  `cd <path>`
2.  `rm <filename>`

### Executing Commands

From Lab 1, you should’ve had the experience in trying out some simple shell commands. The implementation of the two commands `cd` and `rm` are as follows:

1.  The first line is implemented within the shell program itself (**changing** directory with `chdir` system call).
2.  The second line will tell the shell to **search** for a **system program** named `rm` and execute it with the parameter `<filename>`.
    -   **System Programs** are simply programs that come with the OS to help users use the computer. They are run in **user** mode and will help users make the appropriate **system calls** based on the tasks given by the users. More about System Program will be explained in the latter part.
    -   The function associated with the `rm` command (removing a file) would be defined completely within the code in the program called `rm`.
    -   In this way, programmers can **add** new commands to the system easily by creating new system programs whose name matches the **command**.
    -   The command-interpreter program, which can be small, does not have to be changed for new commands to be added.

From Lab 1, you should have been able to find out where your system programs like `ls, mkdir, rm, pwd, ps` reside.
---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]

## What
A shell is a [[System programs]].

A **shell** is a user application that acts as an interface to allow users to **access [[Operating System|OS]] services**.

Name: shell: seen as an "outer" layer around the [[OS Kernel]].

OS shells are either
- Command line interface ([[CLI]]), OR
	- users provide commands via text
- Graphical user interface ([[GUI]])
	- users provide commands via mouse clicks

To use CLI, we need to be familliar with their **commands** and their calling **syntax**.

We are concerned in particular with **UNIX-type** shells (POSIX is an IEEE standard that acts as a standard UNIX version) in this course.

Some shells:
[(Bash) zsh](https://en.m.wikipedia.org/wiki/Bash_(Unix_shell))
[z-shell](https://en.m.wikipedia.org/wiki/Z_shell)
[fish](https://en.m.wikipedia.org/wiki/Fish_(Unix_shell))

[[CLI basics]]

## Find shell
-   **Open** your terminal/command line window.
-   The terminal window in front of you contains a `shell`, which enables you to use commands to access [[OS Services]].

To find your current shell, type the command: `ps -p $$`
```bash
bash-3.2$ ps -p  $$
  PID TTY           TIME CMD
70846 ttys003    0:00.01 bash
bash-3.2$
```


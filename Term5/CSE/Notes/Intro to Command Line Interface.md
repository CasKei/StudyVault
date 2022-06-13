---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

## Overview
An [[OS Kernel]]'s job is to provide **services** so that softwares can communicate with hardware. It manages computer system hardware, memory, and processes (among all others). Its services are exposed via the system call interface, which in itself is wrapped in C standard Library to provide an API that user applications can interact with. Various user applications are made so that the OS services are usable to humans. These services are those you encounter daily when using a computer, for example:
- File management (rename, create, list files, delete, etc),
- Process management (run and terminate),
- System diagnostics (RAM used, CPU %, disk space),
- I/O operations like printing, reading from disk, communication via network, resource management (overclock speed, [[Virtual Memory]] size),
- Protection (security and permission settings), etc.

## Shell
[[shell]]

## CLI Basics
[[CLI basics]]

## Scripts and compilation
[[shell scripting]]
[[compiling programs]]
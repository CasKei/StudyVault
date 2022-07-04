---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

## Case 1
> Multiple [[File Descriptor Table]] entries can point to the same [[System-Wide Open File Table (swoft)]].

e.g.
1. $\geq 2$ processes read same file via
	1. file descriptors are created by one and passed though socket, or
	2. child inherit parent's file descriptor after `fork()`. Note child and parent processes have separated [[File Descriptor Table]] (as they are 2 different separate processes)
2. 1 process that has $\geq 2$ file descriptors referencing to the same file
	1. do this via sys call `dup()` or `dup2()`

### Example
[[Example with dup and dup2]]

## Case 2
> Multiple [[System-Wide Open File Table (swoft)]] entries can point to same file in [[Inode table]].

Call `open` to the **same file** from multiple different processes.
The system call `open()` creates a **new entry** in the swoft.

Both cases are considered [[Thread mapping#Many to one]] mapping.
---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[File System]]

## UNIX File System Data Structure
![](https://natalieagus.github.io/50005/assets/images/week6/4.png)
Simplified UNIX file system data structure in-memory.
All these are implemented in kernel space.

- [[File Descriptor Table]]
- [[System-Wide Open File Table (swoft)]]
- [[Inode table]]

## Example
To observe per-process [[File Descriptor Table]].
Suppose there is a [[Types of system calls|blocking]] C-code as follows, compiled, and its binary output called `out` is stored at `/Users/natalie_agus/Desktop`:
```c
#include <stdio.h>
#include <stdlib.h>


int main(){
   char str1[20];

  printf("Enter name: ");
  scanf("%s", str1);

  printf("Name entered : %s \n", str1);
  fprintf(stdout, "EXIT! \n");
  return 0;
}
```

The blocking instruction `scanf` is there to make the process not terminate yet so we have time to observe the [[File Descriptor Table]]. Running this **twice**, then running `ps | grep ./out | grep -v grep` in the third terminal results in:
![](https://natalieagus.github.io/50005/assets/images/week6/5.png)

There are 2 instances of `./out` at 2 terminals" `ttys009` and `ttys011`.
We can examine its file descriptor table content with the command `lsof -p [pid]`.

There are 3 standard `fd` per process:
- `0u`: `stdin` (standard input stream), obtained from terminal, e.g. `/dev/ttys011`
- `1u`: `stdout`, directed to terminal
- `2u`: `stderr`, directed to terminal

Currently `scanf` is blocking as it is 'listening' from `stdin` (fd 0). What we type at terminal can be passed to the process then passed back to `stdout`. The function `printf()` automatically outputs to `stdout`. Otherwise, we can explicitly "ask" the program to print to `stdout` using `fprintf(stdout, ...)`.

Both processes are pointing to file with inode id `54133720`, which is the inode id of the binary `out` (program code)

```ad-note
This is an example of how the same program can be used to create multiple processes.


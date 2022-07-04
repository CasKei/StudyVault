---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[UNIX File System Data Structure]]

> Managed by Kernel, contains ==list of opened files and its entries== created by `open()`

Opened files in system may include disk files, named pipes, network sockets, and devices opened by ==all== processes.

Fields of each opened file contains:
- `cp` : current pointer offset, point to specific byte in the file
- **Access status**: read, write, execute, etc
- **Open count**: how many [[File Descriptor Table|fd table]] entries point to it. Cannot remove open file table entry if reference count is more than 0
- **Inode pointer**: a pointer to UNIX [[Inode table]]


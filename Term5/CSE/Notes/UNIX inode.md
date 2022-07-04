---
aliases: inode, index node
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

![](https://natalieagus.github.io/50005/assets/images/week6/10.png)

The inode is a data structure in a UNIX-style [[File System]]  that ==describes a file-system object such as a [[File]] or a [[Directory]]==, as shown in the image. Can think of it as the UNIX kernel's internal data structure to manage its [[File System]]. The kernel maintains the [[Inode table]] (a collection of inodes). Each inode stores the attributes and disk block locations of the object's data.

**Inode is the file, excluding its content**, identified by a **unique idone number**.
A filename is just metadata in the file system that refers to a file. A single file/inode can have multiple filenames ([[File Links]])

## Summary
In UNIX-like file systems:

-   An inode is a data structure containing **attributes** about all files in the system.
-   These are the **references** to the actual file content: anonymous chunks of data, each given an inode number.
-   A file in its entirety is _not_ an inode, a file has an associated inode with it. inode contains only the file attributes (metadata).

> It is pretty difficult for users to find their files based on inode numbers. Therefore, we have **directories** which allows us to traverse the file system using named paths.
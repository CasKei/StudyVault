---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[Directory Structure]]

![](https://natalieagus.github.io/50005/assets/images/week6/7.png)

> In the above example, there’s a directory (blue border), with five entries in it, each pointing to a separate file (pink circle).

This way we can say that all files are contained in the **same** directory, which is easy to support and understand. The square nodes are the file names (inside the directory), and the circle nodes are files.

This is the simplest method as all we have is just one _giant_ list of all the files on the disk. The entire system will contain only **one** directory which is supposed to mention all the files present in the file system. The directory contains one entry per each file present on the file system.

However, since all files are in the same directory (same **namespace**), when the number of files increases or when the system has more than one user, they must have ==unique **names**==. This makes the system ==hardly usable==.

> Note that the file names (readme.md, ls, myprog.c, etc) that we see here illustrates how a directory entry points to an inode (not drawn) which finally leads us to the file itself.

If we were to use a single-level directory in our system and the GUI file-manager shell, we will see simply all directory entries (or as we will normally say, ‘all filenames’) in our entire mounted secondary storage.
---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[File Links]]

Let’s begin with an example. A containing `helloworld` characters is created, with inode `54346159`. We name it `input`. At this point, a directory entry named `input` pointing to this file containing `helloworld` is created within the directory named `Links`.

> We call this entry the original filename.

![](https://natalieagus.github.io/50005/assets/images/week6/14.png)

All files in a directory-based file system must have at least one hard link (mapping) giving what we call the original name for each file.

### Reference Count
Each hard link **increases** the reference count to the [[Inode table]] entry it is pointing to by 1. Notice how after `hard_link` is created then the reference to [[UNIX inode|inode]] `54346159` is 2 in the screenshot above.

### Subdirectories

In some operating systems, such as Linux, when you create new subdirectories, you’re creating a new entry to the existing directory.

![](https://natalieagus.github.io/50005/assets/images/week6/15.png)

The reference count for `subdir` is 2 by default, shown in the screenshot above. UNIX-like [[File System]] will create two entries in every [[Directory]]:

-   `.` pointing to the directory itself (thus increasing the reference count of itself by 1 – resulting in 2 that we see in the screenshot above)
-   `..` pointing to its **parent** (thus increasing the reference count of its parent: `Links`)

This provided an **easy** way to traverse the filesystem, both for applications and for the OS itself.

### Hard Links to Link Directories

In UNIX-like systems, you **cannot** create more hard links to link directories, only files. **This is to prevent cycles using hard links**.

> By effectively prohibiting multiple references to directories, UNIX-like OS like Linux maintains an acyclic-graph structure (more about this structure later). However this is not always true for all OS.

![](https://natalieagus.github.io/50005/assets/images/week6/16.png)

### Path Names

Links have path names, e.g: `/Users/natalie_agus/Desktop/Links/input_hardlink`.

![](https://natalieagus.github.io/50005/assets/images/week6/17.png)
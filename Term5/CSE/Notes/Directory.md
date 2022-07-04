---
aliases: dir
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]
[[CLI basics]]

## Lab
The file system has many directories, starting from the **ROOT** (symbolised as a single forward slash /) and you can have directories within a directory thus forming a **hierarchy** of directories. Each “level” is separated by the forward slash symbol.

If your directory has spaces in its name, you need to use the **backslash**) to indicate that it is part of the string, eg: `/Users/natalie_agus/Google\ Drive`

Find your starting context by running the command `pwd`, followed by `ls`:
-   The command `ls` lists **all** files that exist in this **context**, which is the Desktop directory in the example above (`/Users/natalie_agus/Desktop`)
-   When you run the command **ls** by itself, it uses your **current** directory as the context, and lists the files that are in the directory you are in.
-   You can use the `ls` command to list the files in a directory that’s **not** your current directory, e.g: `ls /Users/natalie_agus/Downloads`

Now try another command called `cd` to **change** the current working directory:
-   Change the current working directory into any directory that’s accessible from the current context
-   The command cd is analogous to **double clicking** a folder in the GUI
-   You can go “back” to one previous directory level using the command `cd ..` (or you can chain it to go two levels up for instance, `cd ../..`

## Directories
[[Week 6 - Files]]
> **Directories** are the [[File System]] cataloguing structure that contains metadata (references) to **organize** files in a **structured name space** (path). In computing, a namespace is a **set of symbols** that are used to organize objects of various kinds, so that these objects may be referred to by **name**.

In UNIX-based system, a directory is implemented as a file of a special type, an **executable** whose **content** is a named collection of other files + its corresponding inode id. No diff from regular file, but its contents are controlled by the OS: its content are lists of names assigned to [[UNIX inode|inode]]s that can be interpreted by the OS.

You can think of a directory as some kind of dictionary; a _symbol_ table that **translates** file names or as lists of association structures, each of which contains one filename and one inode number.

-   They form lists of names assigned to inodes.
    -   Remember, inodes have numbers associated for each file but not filenames. **File names to inode mapping is done by the directory.**
-   Each of the entries in the directory contains a **mapping** between **filename** and its associated **inode** number, plus _just enough_ other information to translate from a filename to an inode to get to the actual content.

> Most of the metadata about the file is stored within the inode associated with the file, not the directory entry.

## Searching for a file
Since a directory is also a file, it also has its own inode numbers, and its contents are other filenames and their inode numbers. Most famous is the inode 2 which is `/root` directory.

> A directory can also contain the name of other directories. We know this as a **subdirectory**.

The file system [[Device Driver|driver]] (part of OS) must **use** the directory when looking for a particular filename and then convert the filename to the correct corresponding inode number. It will start from the `root` node and **recursively** search for the file name.

## More
[[Directory Structure]]
- [[Single-level directory]]
- [[Two-level Directory]]
- [[Tree-Structured Directory]]
[[Directory Traversal]]
[[Directory operations]]
---
aliases: dir
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]
[[CLI basics]]

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
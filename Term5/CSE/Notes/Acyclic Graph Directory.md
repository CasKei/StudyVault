---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[Graph Directory Structure]]

In acyclic graph directories, we can have the **same** file, but with **multiple** names (through [[Symbolic Link]]/[[Hard Link]]).

> Note that in **tree** graph directory in the previous section we can’t have more than 1 path to reach the same file entry denoted in pink.

In the graphical representation of a directory, we draw ==edges== to represent any ==links==, be it symbolic or hard link.

> This diagram is just an example. Don’t try to make much sense about the file names.

![](https://natalieagus.github.io/50005/assets/images/week6/22.png)

From the example above, notice that `/Users/Guest/readme.md` is a _hard_ link to `/Users/Guest/readme.txt` and `/bin/readme` is a _symbolic_ link to the **same** file pointed by `/Users/Guest/readme.txt`.

-   If we do `rm /Users/Guest/readme.md` AND `rm /Users/Guest/readme.txt`, the underlying file is **removed**. The [[UNIX inode|inode]] for this file is removed, and we can say that our file is _erased_. The symbolic link becomes a _dangling_ pointer, references to a non-existent file.
    
-   If we do `rm /bin/readme`, the underlying file is **not** removed, because there’s still _another_ hard-link reference to the file.
    
    -   The [[Inode table]] entry (for the file) is completely removed only when its reference count is zero.
    -   An inode entry cannot be deleted as long as the reference count to it is more than 0, meaning that there’s 1 or more directory entry that points to the inode entry.


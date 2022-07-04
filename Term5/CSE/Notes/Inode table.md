---
aliases: index node table, File Control Block, FCB
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[UNIX File System Data Structure]]

> A ==database== of all file attributes and **location** of file contents.

Does not contain content or file name.

Each file is associated with an ==[[UNIX inode|inode]]== and a ==unique inode number==.
View inode number of each file in the current directory using `ls -i`.

File name is stored in another file system cataloguing structure called [[Directory]].
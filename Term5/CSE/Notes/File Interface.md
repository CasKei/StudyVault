---
aliases: file creation, file read and write, file deletion, file truncation, file reposition, combining file operations
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[File Abstract Data Type]]

## Operations
We can perform **operations** on files, and these operations are possible through the file interface or methods, analogous to the interface/methods we implement for classes in OOP.

Operations that can be performed on files are: create, read, write, delete, reposition, and truncate among many others.

## File creation
Ensure 2 things done:
- free ==space in system storage==
- make ==entry in directory== for new file

## File read and write
First have ==permission to open file==. If permitted:
1. ==Open file==
	1. [[System calls]] `open()` or other methods depending on programming language
2. Perform read/write operation using its respective ==file pointer== to indicate where exactly in the file we wan to read or write, byte by byte
3. ==Close file==
	1. `close()`

## File Deletion
Search the ==directory== to find the file given the file's path, then remove it from [[File System]]. Also frees the space initially occupied by the file content.

## File truncation
Keep all [[File Attributes]] but remove the content. Search directory given path. Once found, file length is reset to 0, file space for content is released.

## File reposition
First have permision to `open` the file and gain a file pointer
Then reposition the valeof the file pointer to point to another portion of the file (e.g. byte `N` of the file)
Done in C using `lseek()`

## Combining file operations
3 basic operations can then be combined to perform more **complex file operations**
e.g.
`copy` by ==creating==, then ==opening and reading== from old file and ==writing== to new file.


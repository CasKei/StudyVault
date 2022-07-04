---
aliases: file metadata
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[File Abstract Data Type]]

## Attributes
File has attributes (metadata) similar to how class/object has states.

| Attribute                       | Description                                                                                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                            | The symbolic file name is the only info kept in human readabe form (stored in directory)                                                                            |
| Identifier                      | A unique tag, usually a number, identifies the file within the file system; it is the non-human-reaable name for the file (stored in inode, also known as inode id) |
| Type/Format                     | Info needed for systems that support different types of files                                                                                                       |
| Location                        | This information is a pointer to a device and locaion of the file on that device                                                                                    |
| Size                            | Size of file (bytes, words or blocks) and possibly the max allowed size are included in this attr                                                                   |
| Protection                      | Access-control info determines who can read, write, execute, etc                                                                                                    |
| Time, date, user identification | Info kept for creation, last modification, last use. Useful for protection ,security, usage monitoring.                                                                                                                                                                    |

Use command `ls -ali` to list all files in the current directory, together with its identifier (inode number).
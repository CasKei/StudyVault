---
aliases: fd table
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[UNIX File System Data Structure]]

> The fd table ==exists per-process==

Whenever a process `open()` or `dup()` a file, the opened file is associated with a ==file descriptor==.

- File descriptor is a number that ==uniquely== (in that process) identifies an open file in a computer's OS
- Has file `pointer` field, that is a pointer to the ==system wide open-file-table==.
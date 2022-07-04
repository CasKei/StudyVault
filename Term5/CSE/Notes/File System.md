---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

## File System
> Controls how data is ==stored and retrieved== in a system.

A ==set of rules and features== applicable to determine the way data is stored. A physical disc can be separated int multiple physical partition, where each has diff file system.

### Purpose
> Maintain and organise [[Solid-State Drive (SSD)|secondary storage]].

File system ==logically separates== segments of data on disk and gives each piece a unique name. Each group of data is content, and [[File Attributes]] may be stored elsewhere.

Operates using specific data structure and has specific format. Its ==interface== is part of the OS, so they vary between operating systems.

Examples of common file system includes (no need to memorise):

1.  File allocation table (**FAT**) is supported by the Microsoft Windows OS
2.  New Technology File System (**NTFS**) is the default file system for Windows products from Windows NT 3.1 OS onward
3.  **ext4** is a file system for many Linux Distributions
4.  Universal Disk Format (**UDF**) is a vendor-neutral file system used on optical media and DVDs
5.  Hierarchical file system (**HFS**) was developed for use with Mac operating systems. HFS is succeeded by HFS+
6.  Apple File System (**APFS**) for macOS

In this subject we are focused on the UNIX-specific file system and its data structure.


- [[UNIX File System Data Structure]]
	- [[File Descriptor Table]]
	- [[System-Wide Open File Table (swoft)]]
	- [[Inode table]]
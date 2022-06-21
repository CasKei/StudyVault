[[BH22]]

## Characteristics of Linux OS
### What is Linux and Unix
Unix
- POSIX(Portable Operation System Interface + uniX)
	- Acc to this specification, ti is called a Unix-like OS even if it is not directly related to Unic (LINUX)
- Most important OS
- Everything is a file

Linux
- an OS that uses the Linux kernel
- not the same as UNIX
- Linux belongs to UNIx family
### Advantages and disadvantages
#### Advantages
1. Open source OS
	1. more security (anyone can edit error in code)
	2. various distros (Debian, ubuntu, Redhat...)
2. Perfect compatibility with UNIX
3. Free
4. Multiuser and [[Multiprocessor System|Multiprocessing]] system
5. High protability and scalability
	1. since it is written in assembly and C, only assembly part can be newly created and C part can be recompiled to easily be transplanted into another system.

#### Disadvantages
1. Lack of techincal support
	1. most applications are non-commercial products, impossible for developers to provide technical support individually. it is up to users to solve the problem
2. Hard to use and learn
	1. very difficult due to [[CLI]], which requires impt settings or direct modification of files
	2. widely used OS is Windows. Programs that rely on Windows dont run on Linuz
3. Incovenience in practical use.
### Why use Linux
Android uses Linux.

## Components of Linux OS
### Kernel & Shell CLI
Kernel = Heart of OS.
- based on C
- multi-user
- has [[System calls]] interfaces
- kernel management processes

[[shell]]
- a system program in which the OS interrupts a user's command between kernel and user and sprays the processing result

[[CLI]]
- Stable and fast, consume fewer resources
- ![[Pasted image 20220619121659.png]]
- when user enters a command, shell interprets this command and passes it to kernel.

### Applications
#### Applications
All software running on a shell
Chrome, GNU software, daemon, etc.

### Daemon
[[Daemon Processes|daemon]] is a kindof background process that runs first when a Linux system is [[Booting|booted]] up.
Also acts as a listener, waiting for user's requestand responding appropriately when one is received. e.g. httpd, mysqld, ftpd.
### Basic Linux Command
has relative and absolute paths
- rel: `./file`
- abs: `home/caskei/helloworld/file`

`id`: show user id/group id
`ls`: show dir
`cd`
`pwd`
`mkdir`
`cat`
`cp`
`rm`
`mv`
`rmdir`
`ps`: current process

## Fundamentals of Linux Permissions
### Importance of permission control
![[Pasted image 20220619122153.png]]
Multiuser: so permission control impt.
3 parts of permission:
- user
- group
- other

read, write, execute. file size in bytes. -: common file, d: directory
### Authorisation setting
`chmod`: change mode(permission)
`chown`: change owner
`chgrp`: change group
![[Pasted image 20220619122405.png]]

## File Structure and File System
### What is a file system?
Check file system by using `df` command
![[Pasted image 20220619122539.png]]
### Consideration of file structure
![[Pasted image 20220619122609.png]]
### I-node and linking![[Pasted image 20220619122632.png]]
Data structure is used in a traditional UNIX-file system. An i-node is a data structure that contains file or dir attribute info
When you create a file, it has a unique number. This number cannot be duplicated like a resident registration number.
The file system driver must search a directory looking for a particular filename and then convert the filename to the correct inode number.

2 linking methods:
![[Pasted image 20220619125149.png]]
- Hardlink
	- making a file copy
	- copied file has same I-node as original file
- Symbolic link
	- like a shortcut
### Linking command
`ln (option) (filename) (link file name)`
```shell
ln file hardlink
ln -s file symboliclink
```
![[Pasted image 20220619125426.png]]
![[Pasted image 20220619125433.png]]
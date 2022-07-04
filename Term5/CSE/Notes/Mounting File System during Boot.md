---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

All systems have a **root** partition, which contains the operating-system kernel and sometimes other system files, which are mounted **at boot time**. The system has an **in-memory mount table** that contains information about each mounted volume. Other volumes can be automatically mounted at boot or manually mounted later, depending on the operating system.

**The mount procedure:**

1.  The operating system is given the name of the **device** and the **mount point** — the location within the file structure where the file system is to be attached.
    
2.  Typically, a mount point is an _empty [[Directory]]._ For instance, on a UNIX system, a file system containing a user’s home directories might be mounted as `/home`; then, to access the directory structure within that file system, we could precede the directory names with `/home`,for example, `/home/alice`.
    
3.  Mounting that [[File System]] under `/users` instead would result in the path name `/users/alice`, which we could use to reach the same content under `alice`.
    

The in-memory (means these are in RAM, as long as the computer is alive) information about file system that is loaded at mount time are the three data structures we show above and a few more:

1.  **Mount-table**: contains information about each mounted volume. Notice the list of all mounted volumes in the screenshot below. Disk image, USB drives, all those are also mounted devices. ![](https://natalieagus.github.io/50005/assets/images/week6/11.png)
    
2.  **[[Inode table]]**: Contains directory structure and file **pointers** to the actual data on secondary storage or cached memory
    -   You can list the disk file directory and see how many inodes are present using `df -i`. You should be able to figure out by yourself what each column means, the leftmost one being the filesystem name.  
        ![](https://natalieagus.github.io/50005/assets/images/week6/12.png)
3.  **[[System-Wide Open File Table (swoft)]]**
    -   You might not want to print this out even if you can, as there’s hundreds, even thousands of files that are probably opened right now.
4.  Per-process **[[File Descriptor Table]]** (for currently alive processes)
    -   You can check opened files for your current terminal process opened files using `lsof -p $$` command. ![](https://natalieagus.github.io/50005/assets/images/week6/13.png)

_Details:_

```
FD –  the file descriptor. Some of the values of FDs are,
    cwd – current Working Directory
    txt – text file
    mem – memory mapped file
    mmap – memory mapped device
    <number> – the actual file descriptor. 
      the character after the number i.e ‘1u’ the MODE in which the file is opened:
      r: read, 
      w: write, 
      u: read and write
TYPE – specifies the type of the file. Some of the values of TYPEs are,
REG – regular File
DIR – directory
FIFO – first in first out policy
CHR – character special file
NODE - the inode id that it is pointing to. 
```

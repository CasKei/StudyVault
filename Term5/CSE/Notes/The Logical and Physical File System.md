---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

The **logical** file system is the level of the file system at which users can request file operations by system call. It is responsible for interaction with the user application. This is typically what we see.

The **physical** file system contains the **actual** data of the file system and the actual location. E.g: a huge file that is logically represented as one file is not necessarily physically stored near one another (it can be fragmented in the disk).

On disk, the physical file system contain information about how to:

-   Boot an operating system stored there,
-   The total number of blocks (recall blocksize from 50002)
-   The number and location of free blocks,
-   The directory structure, and
-   Individual files location

The four main components of the entire file system is:

1.  The **Boot** Control Block (per volume): contains information needed by the system to boot an operating system from that volume.
    
2.  The **Volume** Control Block (per volume): contains volume (or partition) details, such as the number of blocks in the partition, the size of the blocks, a free-block count and free-block pointers, and a free-FCB count and FCB pointers.
    
3.  The **Directory** Structure (per file system, it can span several volumes): used to organise the files.
    
4.  The **[[Inode table|File Control Block]]** (per file, also known as **[[UNIX inode|inode]]** in UNIX): contains file attributes, has a unique id, and is associated with directory entry.
    

*Side note about partition vs volume:*

-   Partition is always created on a single physical disk, however a volume can span multiple disks and have many partitions.
-   Partitions only identified by numbers, but volumes have names.
-   Finally, partitions are more suitable for individual devices, while volumes (especially logical volumes) are more flexible and suited for network attached storage.

**Example** on how user interacts with the logical file system to create a file (simplified):

1.  An application program calls the **logical** file system to **create** a file, e.g: by right click » create.
2.  The **logical** file system traverse the directory, and check the _requested_ location.
3.  To create a new file, it allocates a new **inode** or FCB.
4.  The system then update the directory it with the new file name and FCB, and writes it back to the disk.
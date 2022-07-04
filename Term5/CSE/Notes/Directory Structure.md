---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[Directory]]

Both dir structure and [[File]]s themselves reside on [[Hard Disk Drive (Disk)|disk]] and [[Cache]]d in memory.
Common [[File System]] organisation:
![](https://natalieagus.github.io/50005/assets/images/week6/6.png)
Each **volume/partition** that contains a file system must also contain information about the files in the system. This information is kept as **entries** in the device directory (a.k.a volume table of contents). The device directory (more commonly known simply as the directory) records some **important** information such as name, location, size, and type—for all files _in that volume_.

## Purpose
The **purpose** of having a directory structure is to **improve** user experience:

1.  **Efficiency**: locating a file or group of files quickly
2.  **File naming** in a user-friendly manner
    -   Users can pick the same name for their (different) files without conflicts
    -   Same name for files of _different_ types (different extensions)
    -   **Same file can have different names** (multiple logical purposes; reference of same file/folder from different points in the name space)
3.  **Organization** – logical grouping of files by various properties for ease of usage:
    -   Group files with the same user, project, purpose, type, etc.

## Folder
Note that directory is very _similar_ to the definition of a folder.

However folder is a [[GUI]] concept, associated with the common folder icons to represent collection of files. If you are referring to a _container of documents_, then the term folder makes more sense, related to the GUI.

However the term directory refers more **broadly** to the way **a structured list of document** is stored in the computer system.

## Structures
- [[Single-level directory]]
- [[Two-level Directory]]
- [[Tree-Structured Directory]]
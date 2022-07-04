---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

File manager and GUI [[shell]] like Finder for macOS and File Explorer for Windows **traverse** the [[Directory]] (depending on our clicks, which is the same as typing cd

It renders to us different **icons** for different filenames (inclusive of its extension), and subdirectories of the current working directory.

In fact, they are all simply opening directories and rendering its entries. Our files are not stored in the GUI (_if that makes sense_). The GUI is just a **logical** representation of the contents of our secondary storage.

Our disk does _not_ actually have places called `Desktop` or `Downloads`. These are just _logical representation_ of where our files are stored. The directory **maps** the file names (the way we are addressing our files) to its corresponding **[[UNIX inode|inode]]**, and then from there ([[Inode table]]), the system finally finds the **[[Memory Addressing|physical address]]** where the file is actually stored in the [[Solid-State Drive (SSD)|secondary storage]].

> Without the file system and the directory, the bytes that reside in our secondary storage are just a huge chunk of bytes with no discernible boundary separating the content of each file to another.


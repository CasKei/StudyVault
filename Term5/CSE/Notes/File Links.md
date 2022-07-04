---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

We can have different names for the same file by adding more than one entries pointing to the same [[UNIX inode|inode]] in the directory. These directory entries are formally called **links**.

Recall [[UNIX inode|inode]] and [[Directory]].

## Links
- [[Hard Link]]
- [[Symbolic Link]]

## Why link
Imagine having photos in your system, thousands of them. You want to **categorize** them for easier access.

-   You can categorize them as: photos of red things, photos of blue things, photos of green things.
-   You can also categorize them as: photos of vehicles, photos of trees, photos of flowers

Suppose you want to categorize them both ways. What you can do: **Method 1**: You could create a **copy** of the photos and categorize it multiple times in the way you want it.

-   This means you have two copies of the same file taking up two times the space.
-   It is not ideal to do this, especially with large amounts of data.

**Method 2**: Create hard links.

-   A hard link takes up almost no space at all. Y
-   ou could, therefore, store the same photo in various different categories (i.e. by color, by type, etc).

A symbolic link is much like a desktop **shortcut** within Windows. The symbolic link merely points to the location of a file. We have all been using it.

## Summary
![[iwnmw3b1.bmp]]

---
aliases: soft link
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[File Links]]

A symbolic link is simply a file whose content is a text string (i.e: reference to another file or directory) that is **automatically interpreted** and followed by the operating system as a path to another file or directory.

Symbolic links are also known as “shortcuts” or “soft links”.

![](https://natalieagus.github.io/50005/assets/images/week6/18.png)

### Symbolic Links to Link Directories

You **can** link [[Directory]] with symbolic links.

Unlike hard links, a symbolic link is **NOT** just a directory entry. **It is a [[File]]**. Of course as a consequence, this (symbolic link) file has a name and this name is a directory entry somewhere. As shown in the screenshot above, it has its **own** [[UNIX inode|inode]] number: `54354162`, indicating it is a **new file**.

### Link Properties

#### Broken Symlink

If you delete the **reference** [[Hard Link]] (file name) where the symbolic link is pointing to, the symbolic link will be **broken**. ![](https://natalieagus.github.io/50005/assets/images/week6/19.png)

If we recreate `input` (file with the same name), then `input_softlink` will work again. ![](https://natalieagus.github.io/50005/assets/images/week6/20.png)

Therefore from this we can know that `input_softlink` is a FILE with id `54354162`, whose **CONTENT** is path to input, e.g: `~/Desktop/Links/input`. It is automatically interpreted by the OS such that when you open input_softlink it will resolve `~/Desktop/Links/input` and open the referred file.

#### Reference Count

In the example above, although `input` was the original filename, since there’s one more hardlink (`input_hardlink`) pointing to the same inode `54346159`, then this file containing `helloworld` is not yet deleted. We can still access the file via this other hard link pointing to the same file.

Likewise, if you delete all hard links to the file, its entry in the [[Inode table]] will be removed (file completely deleted, space is freed).
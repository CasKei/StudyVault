---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[Directory Structure]]
[[Tree]]

![](https://natalieagus.github.io/50005/assets/images/week6/9.png)

In a tree structure directory, there’s only **one path** to reach each file, as shown above.

Multiple levels of hierarchy like this allow more **elaborate** organization of files, however:

-   Full paths can become really **long**
-   Notions of **current working directory** can shorten the path, e.g you can `cd` to a particular location and use files from your current directory without giving the full path.

Each **process** has its own current working directory, typically from the process who created it.

In this kind of structure, path names can be of two types: **absolute** and **relative**.

1.  An **absolute** path name begins at the root and follows a path down to the specified file, giving the directory names on the path.
2.  A **relative** path name defines a path from the current working directory.
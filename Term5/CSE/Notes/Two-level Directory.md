---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[Directory Structure]]

![](https://natalieagus.github.io/50005/assets/images/week6/8.png)

A two-level directory allows for a separate [[Directory]] for **each user**. Notions of subdirectory and paths become clearer, e.g: `/User1/readme.md`, or `/Guest/readme.md`

Each user has a **separate name space**, but still limited in logical grouping. To delete a file, the operating system confines its search to the _local_ user file directory thus, it cannot accidentally delete another user’s file that has the same name.
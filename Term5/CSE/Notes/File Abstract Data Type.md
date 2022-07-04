---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

A [[File]] can be seen as an ==abstract data type==, that will be implemented differently depending on the OS supporting it. Some file structures are universal (can be identified by any OS and the OS can find a suitable interpreter app in the system), such as `.txt` and `.pdf`. But some others are system specific.

Regardless of structure, we can abstract the concept of file as having
- [[File Attributes]]
- [[File Interface]]
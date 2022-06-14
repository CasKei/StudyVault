---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]

One final point to note is that some implementations require you to **release** the lock `N` times after **acquiring** it `N` times. You need to carefully **read the documentation** to see if the locks are auto released or if you need to explicitly release a lock `N` times to allow others to successfully acquire it again.
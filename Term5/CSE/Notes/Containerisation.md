---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]

If you’d like to expand your knowledge beyond regular OS, you may have further read about **virtualization** and **containerization**.

![](https://natalieagus.github.io/50005/assets/images/week2/18.png)

## Containerization
**Containers** allow a developer to package up an application with all of the parts it needs, such as **libraries** and other **dependencies**, and ship it all out as one package. Containers are not the same as Virtual Machines, and are generally faster to use. You can read more about the differences between the two [here](https://geekflare.com/docker-vs-virtual-machine/).

Note: “Host OS” in the picture above assumes that it is UNIX-based POSIX compliant OS. If you run Docker on Windows/Mac, it will download a Hypervisor + Guest Linux too before you can run the Docker Engine.

Example of softwares that support containerisation: [Docker](https://www.freecodecamp.org/news/docker-quick-start-video-tutorials-1dfc575522a0).
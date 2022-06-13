---
aliases: microkernel
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[OS structures]]

## Microkernel
A microkernel is a **very small** kernel that provides **minimal** process and memory management, in addition to a communication facility.

This method structures the operating system by removing all nonessential components from the kernel and implementing them as system and user-level programs. The result is a smaller kernel that does only tasks pertaining to:

1.  **Inter-Process Communication**,
2.  **Memory Management**,
3.  **Scheduling**

For instance, if a user program wishes to access a file, it must interact with the file server.

-   The client program and service never interact directly.
-   Rather, they communicate indirectly by exchanging messages with the microkernel as illustrated below:

![](https://natalieagus.github.io/50005/assets/images/week2/12.png)

| Pros                                                                                                                                        | Cons                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| extending the operating system easier. All new services are added to user space and consequently do not require modification of the kernel. | suffer in performance increased system-function overhead due to frequent requirement in performing [[Context switch]]. **Example**: Mach, Windows NT (first release was a microkernel). | 

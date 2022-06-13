---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

## OS Services and Interfaces
[[OS Services]]
- To help *user*
	- [[OS Interfaces]]
		- [[GUI]]
		- [[CLI]]
	- Program execution
	- IO Operations
	- File-system manipulation
	- Process Communication
	- Error detection
- For efficient operation of *system* via resource sharing
	- Resource allocation
	- Accounting
- *Protection* and security

## System calls
[[System calls]]
- [[Accessing system calls]]
- [[System call via API]]
- [[System call implementation]]
- [[Types of system calls]]


## OS Design and Structure
Apart from the Kernel and the user interface (GUI and/or CLI), a modern operating system also comes with **system programs** and **application programs**.

Most users’ view of an operating system is defined by the system programs, not the actual system calls because they are actually hidden from us (through API).
-   For example, when a user’s computer is running the macOS, the user might see the GUI, featuring a mouse-and-windows interface.

[[System programs]]
[[User Programs]]
[[System vs Application Programs]]

[[OS Design and implementation]]
- User and system goals
- Policy and mechanism separation

[[OS structures]]
- [[Monolithic structure]]
- [[Layered OS structure]]
- [[Microkernel system structure]]
- [[Hybrid OS structure]]

[[Java OS]]

## Summary
The figure below shows the summary of various OS structures.

![](https://natalieagus.github.io/50005/assets/images/week2/17.png)

For [[Layered OS structure]] architecture, note that the only difference with [[Hybrid OS structure]] and [[Microkernel system structure]] is that programs at level $N$ relies **ONLY** on services provided by programs at **one** level below it.

## Appendix
If you’d like to expand your knowledge beyond regular OS, you may have further read about **virtualization** and **containerization**.

![](https://natalieagus.github.io/50005/assets/images/week2/18.png)

[[Virtualisation]]
[[Containerisation]]
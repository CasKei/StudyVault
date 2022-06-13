---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## Consists of
4 components:
- **[[Operating System|OS]]**
	- Controls and coordinates use of hardware among various applications and users
- **Hardware**
	- Provides basic computing resources
	- CPU, memory, IO devices
- **Application programs**
	- Defines the ways in which the system resources are used to solve the computing problems of the users
	- Word processors, compilers, browsers, db systems, videogames
- **Users**
	- People, machines, other computers

![[Pasted image 20220517143356.png]]
![](https://natalieagus.github.io/50005/assets/images/week1/2.png)

## Organisation
2 types of hardware capable of running instructions:
- [[Anatomy of the Beta CPU|CPU]]
- IO [[Device Controller]]s

In other words, I/O devices and the CPU can execute **instructions** in parallel. They are independent of one another and are **asynchronous**

![](https://natalieagus.github.io/50005/assets/images/week1/6.png)

- $\geq 1$ [[Anatomy of the Beta CPU|CPU]]s, [[Device Controller]]s connect through *common bus* providing access to **shared memory**
- **Concurrent execution** of [[Anatomy of the Beta CPU|CPU]] and devices competing for memory cycles

## Operation
- CPU and IO devices/[[Device Controller]]s can both act autonomously (run code or start activities)
- IO devices and CPU can execute concurrently
- Each [[Device Controller]] is in charge or a paticular device type
- Each [[Device Controller]] has a local buffer
- CPU moves data from/to [[Dynamic Random-Access Memory (DRAM)|main memory]] to/from local buffers
- IO is from device to local buffer of controller
- CPU/controller needs coordination

## Device Drivers
[[Device Driver]]

## Device Controllers
[[Device Controller]]
alent to BIOS, but unfortu
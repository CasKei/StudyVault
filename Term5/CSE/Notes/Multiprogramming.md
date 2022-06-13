---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[OS Kernel]]

## Multiprogramming
Multiprogramming is a concept that is needed for **efficiency**. Part of the kernel code is responsible to ==schedule processes== in a computer system.

A kernel that supports multiprogramming increases **CPU utilization** by organizing jobs (code and data) so that the CPU always has one to execute.

Multiprogramming alone **does not** necessarily provide for user interaction with the computer system. For instance, even though the CPU has **something** to do, it doesn’t mean that it _ensures_ that there’s always interaction with the user, e.g: a CPU can run background tasks at all times (updating system time, monitoring network traffic, etc) and not run currently opened user programs like the Web Browser and Telegram.

## Why
**Single users must be prevented from keeping CPU and I/O devices busy at all times.**
- Clock of general purpose CPU is fast, we don't actually need 100% CPU power in most cases.
- Often too fast to be dedicated for just one program for the entire 100% of the time
- Hence if multiprogramming is not supported and each process has a fixed quantum (time allocated to execute), then the CPU might spend most of its time **idling**.

**The [[OS Kernel]] must organise jobs (code and data) efficiently so CPU always has one to execute:**
- A **subset** of total jobs in the system is kept in memory + swap space of the disk.
- One job is selected per CPU and run by the scheduler
- When a particular job has to wait (for I/O for example),  [[Context switch]] is performed.
	- For instance, Process A asked for user `input()`, enters [[Kernel mode and User mode|kernel mode]] via [[Supervisor Call]]
	- If there’s no input, Process A is **suspended** and **context switch** is performed (instead of returning back to Process A)
	- If we return to Process A, since Process A cannot progress without the given input, it will invoke another `input()` request again – again and again until the input is present. This will waste so much resources

Gives rise to [[Timesharing]]
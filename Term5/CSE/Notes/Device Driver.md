---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## What
A system must have **device drivers installed** for each device type. This driver is a specific program to **interpret** the behavior of each device type. We typically install/download _device drivers_ when we plug in **new** I/O units to our computers through the USB port.

![](https://natalieagus.github.io/50005/assets/images/week1/7.png)

> It provides a software **interface** to hardware devices so that the device controller is able to communicate with the OS or an application program.

## Running drivers
Default device drivers are in [[OS Kernel]] code, and may consist of interfaces that control one or more common devices that can be attached to a system, such as [[Hard Disk Drive (Disk)]], GPUs, keyboards, mouses, monitors, and network interfaces. IOW, they are modules that can be **plugged into** an [[Operating System|OS]] to handle a particular device or category of similar devices. Many run in [[Kernel mode and User mode|kernel mode]] (hence some need reboot upon installation), but some in [[Kernel mode and User mode|user mode]].

User mode ones are slower, since **frequent switching** to [[Kernel mode and User mode|kernel mode]] is required to access *serial ports* of the [[Device Controller]] that's connected to the external devices. But if poorly written will not endanger the system.

Kernel mode ones, if have **vulnerabilities**, can pose serious threat as they can allow an attacker to escalate privileges to the highest level and become highly **persistent**.
---
aliases: OS
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## Overview
> An operating system (OS) is a program that **manages computer hardware**.

Figure shows the hardware components of a common general computer. There are many user programs. OS is **intermediary application that enables many user programs to share the same set of hardware**.

![](https://natalieagus.github.io/50005/assets/images/week1/1.png)

## The OS
> A special program that acts as an intermediary between users and hardware.

### What
>A program that
> - acts as an intermediary between a user of a computer and computer hardware
> - used a lot by all users

### Goal
> - Execute user programs and make solving user problems easier
> - Make [[Computer System]] convenient to use
> - Use hardware efficiently

### Roles
To have a dedicated program to fulfil these roles:
1. **Resource allocator** and coordinator
	1. Control hardware and input/output requests, manage conflicting requests, manage interrupts
2. **Control program** execution
	1. Storage hierarchy manager
	2. Process manager
3. Limits program execution and ensure security
	1. Preventing illegal access to, or improper use of hardware

Once we have OS, it easier for users to use a program or write a program for other purposes within a [[Computer System]].

### Consists of
Many things, but generally:
1. [[OS Kernel]]
2. System programs
3. User programs

Definition and role of **operating system kernel** can be found in another section below, and it is the only program with **full** privileges, i.e: absolute access to control all the hardware in the computer system.

Both system programs and user programs run in **user mode**, with limited privileges, i.e: any of these programs have to send a _request_ to the kernel each time they require access to the I/O or hardware devices.

## Part of
OS is a part of [[Computer System]].

## Provides
OS provides an environment such that user programs can do work.

Since each user program runs in a [[Virtual Machine]] (written in a manner that the entire machine belongs to itself), there has to be some manager program that has higher privileges and oversees all programs that live on the [[Dynamic Random-Access Memory (DRAM)|RAM]] and reside on [[Hard Disk Drive (Disk)|disk]], as well as manage the [[Memory Hierarchy]].

This special program is the [[OS Kernel]].

## How does it start running
[[Booting]]
**Bootstrap program is loaded at power-up or reboot**
- Typically stored in ROM or EPROM, generally known as *firmware*
- Initialises all aspects of system
- Loads [[OS Kernel]] and starts execution

## OS Subsystems
- Memory management
- Storage management (including file systems) 
- Mass storage management
- IO management
- security
- etc

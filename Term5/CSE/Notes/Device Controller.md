---
aliases: IO operation
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

## What
> Electronic components inside a computer that are in charge of specific types of devices.

Attached to motherboard. Runs asynchronously, may run simple instructions. Has its own buffers, registers, and simple instruction interpreter. Usually transfer data to and fro the I/O device via standard protocols such as USB A/C, HDMI, DP, etc.

## Made up of
1. [[Sequential Logic|Registers]]
	1. Contains instructions that can be read by an appropriate **[[Device Driver]] program at the [[Anatomy of the Beta CPU|CPU]]**
2. Local memory **buffer**
	1. Contains instructions and data that will be fetched by [[Anatomy of the Beta CPU|CPU]] when executing the [[Device Driver]] program, and ultimately loaded onto the [[Dynamic Random-Access Memory (DRAM)|RAM]].
	2. A simple program to communicate with [[Device Driver]]

## IO Operation
> Happens when there is transfer of data between local memory buffer of [[Device Controller]] and the device itself

IO Operation simply means EITHER:
- Output: move data from [[Dynamic Random-Access Memory (DRAM)|RAM]] to local memory buffer
- Input: move data from [[Device Controller]] buffer to [[Dynamic Random-Access Memory (DRAM)|RAM]]

Since the device controller and our CPU are **asynchronous** (can operate independently, in parallel), we need to devise a way to **coordinate** between servicing I/O requests and executing other user programs. This **I/O handling** issue is handled by our [[OS Kernel]] (read along to understand _how_).
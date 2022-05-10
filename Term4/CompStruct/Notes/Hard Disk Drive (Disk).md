---
aliases: HDD, disk, secondary storage
tags: 50.002
---
[[Comp Struct|50.002]]
[[Memory Hierarchy]]

## What
> An old-school mechanical data storage device.

Data is typically *written* onto a round, spinning aluminum coated with *magnetic material* that we call a *disk*.

Several of these round platters are put together on a *shaft*, and they make up a *cylinder*.

These cylinders *spin* at around 7000 revolutions per min.

## Structure
Each round disk can be separated into concentric circles sections (*track*), and each track can be further separated into *sectors* as shown below.
![](https://dropbox.com/s/x32k130rfu8h7fm/disk.png?raw=1)

Each sector contains a *fixed number of bits*.

![File:Hard drive geometry - English - 2019-05-30.svg](https://lh4.googleusercontent.com/vgIqcmlZB6UhFWwBXjHKFXQ-marY1OqR7Lj0pgXDs0etkLdGQpSGyPqWJH2CWAWO-LJA3YQLAJn2aRxMqwg64Wl5a2zM1Rfn9I1zemY76wEzuGQejkNB214jRVa-CerIYsPNMfze)![[Pasted image 20220328114141.png]]

## Memory
A disk is able to retain its information even after they are not directly plugged to power supply anymore.

Therefore, unlike [[Anatomy of the Beta CPU|REGFILE]], [[Static Random-Access Memory (SRAM)|SRAM]] and [[Dynamic Random-Access Memory (DRAM)|DRAM]] that are **volatile**, a disk is a type of **low-power** and **non-volatile** storage device.

However, non-volatile memory that relies on *mechanism such as magnetic field changes to encode information* takes ==far longer== to change its values.

## Reading and Writing
To perform a read or write to a disk, **the device has to mechanically move the head of the disk and access a particular sector**. This takes up **a lot of time,** and thus resulting in **large latency** for _read and write_.

The [[Anatomy of the Beta CPU|CPU]] itself cannot directly [[Memory Addressing|address]] anything on a disk.

Each platter has its own read and write head, but all heads are mounted on a common arm assembly.

### Read
To access any data on disk, the [[Anatomy of the Beta CPU|CPU]] has to first give the command for a chosen *block of data* from some *sectors* to be **copied** into the [[Anatomy of the Beta CPU|RAM]].

After the entire block of data is in the RAM, the [[Anatomy of the Beta CPU|CPU]] can start accessing the specific 32-bit data (o `n` bit, depending on [[Designing an Instruction Set|architecture]])

### Write
The writing is done by a magnetic head, mounted at the end of an actuator arm that pivots in such a way that *the head can be positioned over any part of the platter*.

The same head may also read the stored data.

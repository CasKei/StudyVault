---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]

## What
A single core [[Anatomy of the Beta CPU|CPU]] is capable of running many programs seemingly at the same time. 

Actually, the [[Anatomy of the Beta CPU|CPU]] **switches** between the execution of the each program so rapidly  that it appears as if all programs are running on their own [[Anatomy of the Beta CPU|CPU]]. 

This technique is known as **rapid context switching**. 

>  Context switch
>  The procedure a [[Anatomy of the Beta CPU|CPU]] must follow when changing the execution of one process to another. 
>  This is done to ensure that the process can be restored and the program execution can be resumed again later. 

Proper hardware support to allow this is crucial for users to multitask when using the machine. 

## How
Each program has its own [[Virtual Memory]] to give the illusion that they each have their own independent [[Dynamic Random-Access Memory (DRAM)|physical memory]] for themselves. 

Therefore each program is written assuming it has access to all memory without considering other programs. 

To distinguish between one program's [[Virtual Address|VA]] address sspace from another, the OS Kernel assigns a unique identifier `C` called **context number** for each program. 

> Context: a set of mapping from [[Virtual Address|VA]] to [[Memory Addressing|PA]]. 

The context number can be appended to the requested VPN to find the it's correct [[Memory paging|PPN]] mapping:
- A [[Sequential Logic|register]] can be used (aadded to [[Pagetable|MMU]] to hold the current ccontext number `C`
- [[Translation Lookaside Buffer|TLB]] `TAG` field contains both `C`  and VPN
- If `MISS` [[Pagetable]] pointer is updated to point to beginning of the [[Pagetable]] section for context `C`, and the index based on VPN finds the corresponding entry.

![](https://dropbox.com/s/ckevn475pf7ar4s/mmuusagecontext.png?raw=1)

This way **we do not have to "flush" the [[Translation Lookaside Buffer|TLB]] whenever the [[Anatomy of the Beta CPU|CPU]] changes context** - that is *switching the execution of one program with another*.

It only needs to update the [[Pagetable]] pointer so that it points to the start of the [[Pagetable]] section for this new context.
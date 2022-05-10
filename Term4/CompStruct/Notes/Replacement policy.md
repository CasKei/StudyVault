---
aliases: LRU, LRR, Random
tags: 50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]
![[Cache Design Issues#^2657a0]]

## Motivation
[[Cache]] replacement policy is required in both [[Fully Associative Cache (FA)|FA cache]] and [[Associativity|NWSA]] cache. 

There are 3 common cache replacement strategies. Usually, they are **implemented in hardware**, and **carries varying degrees of overhead**.

> Overhead: additional cost (time, energy, money) to maintain and implement.

## Least Recently Used (LRU)
### Idea
To always replace the least recently used item in the cache.

### Overhead computation
To know which item is LRU, we need to **keep an ordered list** of `N` items in the [[Fully Associative Cache (FA)|FA cache]] or set **at all times**. This takes $\log{N}$ bits **per cache line**.
With total of `N` cache lines, we need to have some hardware of size $N\log_2{N}$ bits to contain the necessary information for supporting this policy.
[[Helper Bits#LRU Least Recently Used Bits|LRU bits]]

We also need a **complex logic unit** for implementing LRU algorithm and to reorder the [[Helper Bits#LRU Least Recently Used Bits|LRU bits]] *after every cache access*.

>The [[Helper Bits#LRU Least Recently Used Bits|LRU bits]] is updated at **every cache access**, regardless of whether there’s a replacement or not.

>Assume the **smallest** [[Helper Bits#LRU Least Recently Used Bits|LRU bit]] indicates the **most** recently accessed data

### Example
Given a [[Fully Associative Cache (FA)|FA cache]] of size `N=4`, and the event where we request addresses in this sequence: `0x0004,0x000C,0x0C08,0x0004,0xFF00,0xAACC` at `t=0,1,2,3,4,5` respectively.

At `t=2`, the state of the FA cache:

| TAG      | Content       | LRU |
| -------- | ------------- | --- |
| `0x0004` | `Mem[0x0004]` | 10  |
| `0x000C` | `Mem[0x000C]` | 01  |
| `0x0C08` | `Mem[0x0C08]` | 00  | 

At `t=3`, we access `A=0x0004` again. This **updates** all LRU bits:

| TAG      | Content       | LRU |
| -------- | ------------- | --- |
| `0x0004` | `Mem[0x0004]` | 00  |
| `0x000C` | `Mem[0x000C]` | 10  |
| `0x0C08` | `Mem[0x0C08]` | 01  | 

At `t=5`, the entry `0x000C-Mem[0x000C]` is replaced because its the _least recently used_ entry:

| TAG      | Content       | LRU |
| -------- | ------------- | --- |
| `0x0004` | `Mem[0x0004]` | 10  |
| `0xAACC` | `Mem[0xAACC]` | 00  |
| `0x0C08` | `Mem[0x0C08]` | 11  |
| `0xFF00` | `Mem[0xFF00]` | 01  | 

## Least Recently Replaced (LRR)
### Idea
To always replace the *oldest* recently used item in the [[Cache]], *regardless of the last access time*.

> The LRR is a pointer containing the index of the “oldest” item in the cache.

### Overhead computation
We need to know which is the **oldest cache line** in the device.
If there are `N` items in the cache, we need to have a **pointer** of size $O(\log_2{N})$ bits that can point to the oldest cache line.

We also need a (not as complex) **logic unit** to perform the LRR algorithm.

> Assume that we will always fill _empty_ cache from the smallest index to the largest index.

### Example
(Same as before)
Given an FA cache of size `N=4`, and the event where we request addresses in this sequence: `0x0004,0x000C,0x0C08,0x0004,0xFF00,0xAACC` at `t=0,1,2,3,4,5` respectively.

At `t=2`, the state of the FA cache:
`LRR: 00`

| TAG      | Content       |
| -------- | ------------- |
| `0x0004` | `Mem[0x0004]` |
| `0x000C` | `Mem[0x000C]` |
| `0x0C08` | `Mem[0x0C08]` |

At `t=3`, we access `A=4` again, but the `LRR` pointer **will not be updated.**

At `t=5`, the one that is replaced is `A=0x004`, and the `LRR` pointer can be increased to the next oldest entry (the next index): `LRR: 01`

| TAG      | Content       |
| -------- | ------------- |
| `0xAACC` | `Mem[0xAACC]` |
| `0x000C` | `Mem[0x000C]` |
| `0x0C08` | `Mem[0x0C08]` |
| `0xFF00` | `Mem[0xFF00]` | 

## Random
### Idea
To replace a random cache line.

### Overhead computation
We simply need some logic unit to behave like a random generator, and we use this to select the cache line to replace when the cache is full.

## Overall Comparison
There is no one superior replacement policy, depends on use case. i.e. pattern of addresses required.

| LRU                                                                                                                                  | LRR                                                                                     | Random                  |
| ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------------- |
| Comforms to [[Memory Hierarchy#Reason why this works\|locality of reference]], good when `N` is small (since expensive to implement) | Good on specific pattern of usage where we don't frequently revisit oldest cached data. | Good when `N` is large. |

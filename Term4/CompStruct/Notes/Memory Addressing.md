---
aliases: address, memory address, physical address, PA
tags: 50.002
---
[[Comp Struct|50.002]]
[[Memory Hierarchy]]

![](https://dropbox.com/s/kc5atqtnyuo5dg7/decoding.png?raw=1)

> Billions of these [[Static Random-Access Memory (SRAM)|SRAM]] or [[Dynamic Random-Access Memory (DRAM)|DRAM]] cells are assembled together to form a large [[Anatomy of the Beta CPU|memory unit]]. 

> Each _byte_ (8 cells) has a _specific address_.

## Decoding an Address
Split the address into:
- higher `N` address bits (selecting one of the rows) and 
- lower `M` address bits (selecting a group of the columns), 

then read the information out of the bitlines.

We often read hundreds of bits in parallel, for example, one _“row”_ might contains hundreds of bit lines, and the lower `M` address bits will select which of group of 32 bits (or 64 bits, depending on the [[Designing an Instruction Set|ISA]]) we want to read.
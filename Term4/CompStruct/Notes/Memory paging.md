---
aliases: paging, page, PPN, PO
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]

> **Paging**:
> a memory management scheme that is used to store and load data from the [[Hard Disk Drive (Disk)|disk]] (large capacity secondary storage) for use in the [[Dynamic Random-Access Memory (DRAM)|physical memory]] efficiently.

>**Page:**
>a fized-size block of data that forms *contiguous* [[Dynamic Random-Access Memory (DRAM)|physical memory]] [[Memory Addressing|addresses]]

![](https://dropbox.com/s/janbxcdijndlhc4/page.png?raw=1)

## Why
It is useful and efficient to transfer data in pages instead of by word between the [[Dynamic Random-Access Memory (DRAM)|physical memory]] and [[Hard Disk Drive (Disk)|disk]] due to [[Memory Hierarchy|locality of reference]].

## What
A **page** is identified by 2 things:
- Physical Page number (`PPN`) : this identifies the entire page
-  Page Offset (`PO`) : this identifies the **word** line in a page.

`PPN` and `PO` actually makes up the entire Physical Address `PA` space.

### Number of bits required for PO
Depends on how many 32-bit words are there in a page (page-size).

Suppose we have 9 words of data for each page like the page size in the figure above.
The minimum bits required for `PO` is
- **Word addressing**: $\max{(\log_2{9})} = 4$ bits
- **Byte addressing**: $\max{(\log_2{9})} + 2 = 6$ bits

### Number of bits required for PPN
Depends on how many pages there are that can fit in [[Dynamic Random-Access Memory (DRAM)|physical memory]] (physical memory size).

Suppose there are only 20 pages in total that can fit the physical memory.
The minimum bits required for `PPN` is
- $\max{(\log_2{20})} = 5$ bits

Note: page size has nothing to do with [[Cache Block size]].
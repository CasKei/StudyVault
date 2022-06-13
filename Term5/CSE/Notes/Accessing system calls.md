---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[System calls]]

(not in syllabus)

All processes running in a computer must be able to make [[System calls]]. As a result, at the minimum the **entry** points into the kernel have to be **mapped** into the current address space at all times.

To provide you with a context, let’s see a typical memory layout of a UNIX process (actual implementation may vary, e.g. Kernel is at low address space instead): ![](https://natalieagus.github.io/50005/assets/images/week2/1.png)

The [[Virtual Address]] space of a process is typically divided into two parts: **kernel** part in the higher address and **user** part in the lower address (or vice versa, depending on the Kernel implementation).

The kernel mapping part exists primarily for the **kernel-related purposes**, not user processes. Processes running in user mode don’t have access to the kernel’s address space (with different MSB), at all. In user mode, there is a **single** mapping for the kernel, shared across all processes, e.g: fixed address between `0xffffffff` to `0xC0000000` as illustrated above.

-   When a kernel-side page mapping changes, that change is reflected everywhere.

## Kernel Space

The kernel is divided into two spaces: **logical** and **virtual**, often called `lowmem` and `vmalloc` respectively.

In `lowmem`, it often uses a **one-to-one** mapping between virtual and physical addresses (its called logical mapping). That means [[Virtual Address]] `X` is mapped to physical address `X+C` (where `C` is some constant if any). This mapping is built during **boot**, and is **never** changed.

The kernel virtual address area (`vmalloc`) is used for **non-contiguous** physical memory location, so that it is **easier** to allocate them.

-   This allocation of process memory is **dynamic** and on demand.
-   On each allocation, a series of locations of physical [[Memory paging|pages]] are found for the corresponding kernel virtual address range, and the [[Pagetable|pagetable]] is **modified** to create the mapping.
-   If this is done, it might be **unsuitable** for DMA ([[Direct Mapped Cache (DM)|Direct Memory Access]]).
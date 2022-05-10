---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]
[[Demand Paging]]

## Termination
Finally when the program terminates, the OS Kernel and frees up all the space initially allocated for this program’s VM (both on physical memory and disk swap space).

### Example

![](https://dropbox.com/s/r8nia46u4gdw6gk/vmexample.png?raw=1)

The figure above shows a snapshot of the physical memory state at some point in time. There exist a pagetable with 16 entries and 8 pages of data labeled as `A` to `H` in the physical memory. LRU replacement policy with write back policy is used. **Lower** LRU means that the data is **more recently used.**

Each _page_ contains exactly 256 _bytes_ of data.

This information gives us five **clues**:

-   `VPN` is `4` bits long
-   `PPN` is at least `3` bits long
-   `PO` is `8` bits long
-   `VA` is `8+4 = 12` bits long
-   `PA` is `3+8 = 11` bits long

We can assume that _instructions_ are located at a separated physical memory (like our Beta), so we can spare ourselves the headache of resolving virtual to physical memory addresses on both instruction loading and data loading (`LD` and `ST` operations). **We assume for the sake of exercise in this course that we are looking at the portion of the RAM, Pagetable, and TLB that stores data only** and not instruction.  

**Example 1:** Now suppose the current instruction pointed by the PC is **`LD(R31, 0x2C8, R0)`**.

> A memory reference to address `0x2C8` is required.

`0x2C8` is _a virtual address_, and hence we need to obtain its physical address. Segmenting the `VA` into `VPN` and `PO`:

-   `VPN: 0x2` (higher 4 bits)
-   `PO: 0xC8` (lower 8 bits)

Looking at the pagetable, we see that `VPN: 0x2` is **resident**, and can be translated into `PPN: 100`. The translated physical address is therefore `100 1100 1000`. In hex, this is `0x4C8`. The content that we are looking for exists within page `E`.

**Example 2:** Suppose the next instruction is **`ST(R31, 0x600, R0)`.**

> This means a memory reference to address `0x600` is required:

We can segment the `VA` into:

-   `VPN: 0x6` (higher 4 bits)
-   `PO: 0x00` (lower 8 bits)

From the pagetable, we see that `VPN: 0x6` is **not resident.**

> Even though `PPN: 5` is written at the row `VPN: 6`, we can _ignore_ this value as the resident bit is `0`. **The values at the entry is irrelevant when `R=0`.**

This memory reference request will result in **page fault**. The OS Kernel will handle this exception, and bring the requested page (lets label it as page `I`) into the RAM.

**Now suppose the RAM is currently full.**

-   We need to figure out which page can be _replaced_
-   Since LRU policy is used, we need to find the _least recently used page_ with the biggest `LRU` index
-   This points to the last entry where `PPN:3` (containing page `D`) and `LRU:7`.

However, we cannot immediately _overwrite_ page `D` since its dirty bit is activated. A **write** (from the physical memory to the swap space of page `D`) must be performed first before page `D` is replaced with the new page `I`.

After page `D` write is done, the OS Kernel can copy page `I` over from the swap space to the physical memory, and **update the pagetable:**

-   `VPN:F` dirty bit is cleared, and resident bit is set to `0`.
-   `VPN:6` is updated, as now it is mapped to `PPN:3`. Its resident bit is set to `1`.
-   After _write_ (`ST`), its dirty bit is also set to `1`.
-   All entries’ LRU bits must be updated accordingly.

The state of the physical memory after **both** instructions are executed in sequence is:

> `I'` is just a symbol of an updated page `I` after a `ST` instruction is completed

![](https://dropbox.com/s/mis63e6z0nm0n3b/vmexample-after.png?raw=1)

The new changes are written in blue.

> Enhance your understanding by adding TLB into the picture. If a TLB of size 2 (stores the 2 most recently used mapping) is used, what will its state be in the beginning? After **`LD(R31, 0x2C8, R0)`** is executed? Then after **`ST(R31, 0x600, R0)`** is executed next?
---
aliases: synchronisation hardware, prevent interrupt, atomic instruction, lock memory bus, hardware spinlock
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section solutions]]

## Synchronisation Hardware
[[Peterson's Solution]] is pure software that is not guaranteed to work on modern computer architecture where `LD/ST` might not be atomic (e.g. many processors accessing the same location)

Hardware solution also possible. Use **hardware locking** to protect [[Critical section]]s. This is physically limited.

## Preventing interrupts
Only works in **single-core** systems and **not feasible** in [[Multiprocessor System]]:
- time consuming, need to [[Message Passing|pass message]] to all processors
- affect system clocks
- decrease efficiency, defeat purpose of [[Multiprocessor System|Multiprocessing]]

Ability to temporarily inhibit interrupts and ensure that the currently running process cannot be [[Context switch]]ed need to be supported at hardware. If no interrupt can occur during CS, then [[Mutex]] is **trivial**.

You know this as a [[Preemption|non-preemptive]] approach, and some kernels are non-preemptive (**non-interruptible**) and therefore will not face the [[Race condition]] in the kernel level itself.

## Atomic Instructions
> Implement a set of **atomic** instructions by **locking the memory bus**.
> [[Mutex]] thus trivial.

Typically used to provide [[Mutex]] in [[Symmetric architecture]] [[Multiprocessor System]].

### Common instructions
Used **directly** by [[Assemblers and Compilers|compiler]] and [[Operating System]] programmers byt are also abstracted and exposed as bytecodes and library functions in higher-level languages like C:
- Swap 2 memory words: `compare_and_swap()`
- Test original value of memory word and set its value: `test_and_set()`
- atomic `read` or `write`
- atomic `swap`
- `fetch-and-add`
- `load-link`/`store-conditional`

### Example
-   Lets say **CPU1** issues `test_and_set()`, the modern DPRAM (dual port ram) makes an internal note by **storing** the address of the memory location in its own dedicated place.
-   If **CPU2** also issues `test_and_set()` to the **same** location then DPRAM checks its internal note and notices that CPU1 is accessing it, so it will issue a **busy** interrupt to **CPU2**.
-   **CPU2** might be busy waiting (spinlock) to **retry** again (until succeeds). This happens at **hardware speed** so it is actually not very long at all.
-   After **CPU1** is done, the DPRAM erases the internal note, thus allowing **CPU2** to execute its `test_and_set()`.



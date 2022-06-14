---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section problem]]
[[Critical section solutions]]

We need hardware support for certain **special** atomic assembly-language instructions like `test-and-set` above. This can be used by application programmers to **implement** software locking without the need to switch to kernel mode or perform context switch (unless otherwise intended). On architectures without such hardware support for atomic operations, a non-atomic locking algorithm like [[Peterson's Solution]] can be used.

> However, such an implementation may require more memory than a [[Hardware supported spinlocks|hardware spinlock]]

## Software
[[Spinlock]]
[[Mutex lock]]

[[Sephamores]]
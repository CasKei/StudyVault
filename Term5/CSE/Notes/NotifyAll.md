---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]
[[Java Condition Synchronisation]]

However we are not completely free of another **potential** problem yet: `notify()` might not wake up the **correct** thread whose `id == turn`, and recall that `turn` is a shared variable.

We can solve the problem using another method `notifyAll()`: wakes up all threads in the wait set.
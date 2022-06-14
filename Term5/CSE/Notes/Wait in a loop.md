---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]
[[Java Condition Synchronisation]]

It is **important** to put the waiting of a condition variable in a `while` loop due to the possibility of:

1.  **Spurious** wakeup: a thread might get woken up even though no thread signalled the condition (`POSIX` does this for performance reasons)
2.  **Extraneous** wakeup: you woke up the correct amount of threads but some hasn’t been scheduled yet, so some other threads do the job first. **For example:**
    -   There are **two** jobs in a queue, and there’s two threads: thread A and B that got woken up.
    -   Thread A gets **scheduled**, and finishes the first job. It then finds the second job in the queue, and **finishes** it as well.
    -   Thread B finally gets scheduled and, upon finding the queue empty, crashes.
---
aliases: speedup
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Multiprocessor System]]
[[Week 4 - Processes and Thread management]]


## Amdahl's Law
> Not all programs can be 100% parallelised. ==Some programs required a portion of its instructions to be **serialised**==. We need to identify potential performance gains from adding additional computing cores to an application that has both serial (nonparallel) and parallel components.

Given that $\alpha$ is the **fraction** of the program that must be executed serially, the **maximum speedup** that we can gain when running this program with $N$ CPU cores (processors) is:
$$\dfrac{1}{\alpha + \dfrac{1-\alpha}{N}}$$
When $N = 0$, speedup $\infty$ or undefined.
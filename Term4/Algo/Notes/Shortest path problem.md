---
aliases: shortest path
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

## Shortest path problem

> **Problem**: Given $G = (V,E)$ a [[Shortest path problem|weighted]] and [[Graphs - further terminologies#Directed graph|directed]] [[Graphs|graph]], and two vertices $u$ and $v$, find a **shortest path** in $G$ from $u$ to $v$.

Let the [[Weight function]] of $G$ be $w:E\to \mathbb{R}$.\
Among all possible [[Path and Cycles|path]]s from $u$ to $v$, consider the weights of these paths.\
Let $\delta = \delta(u,v)$ be the smallest possible weight.\
$\delta(u,v)$ is called the *shortest-path weight* from $u$ to $v$.

## Shortest path
> A **shortest path** in $G$ from $u$ to $v$ is by definition **any** path from $u$ to $v$ with this posible weight $\delta$.

![[Pasted image 20220323090310.png]]

## Negative weight cycles
![[Pasted image 20220323090557.png]]
Consider this [[Weight function|weighted]], [[Directed acyclic graph (DAG)|directed]] [[Graphs|graph]] $G$.\
What is the shortest path weight $\delta(v_2, v_3)$?
![[Pasted image 20220323092400.png]]
Problem: cycle $(e_5, e_6)$ has negative weight -2!
There are paths from $v_2$ to $v_3$ with arbitrarily large negative weights! There is no shortest path.\
So we define $\delta(v_2, v_3) = -\infty$.

## Cycles in shortest path
Suppose we are given that $p$ is a shortest path from $v_1$ to $v_k$.\

### Negative weight cycles
CANNOT

### Positive weight cycle
NO!\
If $p = \langle v_1, \dots, v_k \rangle$ contains a positive weight cycle $\langle v_i, \dots, v_j \rangle$, then $v_i = v_j$, and we can remove this cycle from our shorter path to get an even shorter path. CONTRADICTION!

### Zero weight cycle
Yes this is possible.\
But we can always then find another shortest path without cycles.

## Subpaths of Shortest Paths are also Shortest Paths
> Let $G=(V,E)$ be a [[Weight function|weighted]], directed [[Graphs|graph]], and suppose that $\langle v_0, v_1, \dots, v_k \rangle$ is a shortest [[Path and Cycles|path]] from vertex $v_0$ to vertex $v_k$.\
> Then any subpath $\langle v_i, v_{i + 1}, \dots, v_j \rangle$ must be a shortest path from vertex $v_i$ to vertex $v_j$.

**Proof**\
If $\langle v_i, v_{i + 1}, \dots, v_j \rangle$ is not a shortest path from $v_i$ to $v_j$, then we can find another path $\langle v_i,v'_{i+1}, \dots, v_j \rangle$ from $v_i$ to $v_j$ with weight strictly smaller than the weight of $\langle v_i, v_{i + 1}, \dots, v_j \rangle$.

So we can replace the subpath $\langle v_i, v_{i + 1}, \dots, v_j \rangle$ in $\langle v_0, v_1, \dots, v_k \rangle$ with the new path to get a new path from $v_0$ to $v_k$ with strictly smaller weight. This contradicts our condition that $\langle v_0, v_1, \dots, v_k \rangle$ is a shortest path.
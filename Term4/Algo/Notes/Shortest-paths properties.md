---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

CLRS 24.5
## [[Triangle inequality]]
### Lemma 24.10
Let $G = (V,E)$ be a [[Weight function|weighted]] directed [[Graphs - further terminologies|graph]], let $s \in V$ be the source vertex, and let $w:E \to \mathbb{R}$ be the [[Weight function]] of $G$.

Then for all edges $(u,v) \in E$, we have
$$\delta(s,v) \leq \delta(s,u) + w(u,v)$$
### Proof
Suppose that $p$ is the [[Shortest path problem|shortest path]] from source $s$ to vertex $v$. Then $p$ has no more [[Weight function|weight]] than any other [[Path and Cycles|path]] from $s$ to $v$. Specifically, path $p$ has no more weight than the particular path that takes a shortest path from $s$ to $u$ and then takes edge $(u,v)$.

## Upper-bound property
### Lemma 24.11
==textbook== 
***

## Path Relaxation Property
Let $G = (V,E)$ be a [[Weight function|weighted]] directed [[Graphs - further terminologies|graph]], let $s \in V$ be the source vertex, and let $w:E \to \mathbb{R}$ be the [[Weight function]] of $G$.

[[Edge relaxation]]
### Lemma 24.15
If $p = \langle v_0, v_1, \dots, v_k \rangle$ is a [[Shortest path problem|shortest path]] from $v_0=s$ to $v_k$, then for any relaxation order of edges, where $(v_{i-1}, v_i)$ is [[Edge relaxation|relaxed]] before $(v_i, v_i)$ for all $1 \leq i \leq k - 1$,\
i.e. earlier edges in $p$ are relaxed before later edges in $p$,\
then $v.d$ = \delta(s,v)$ for all vertices $v$ in $p$.

### Important Consequence
Intuitively, if in the relaxation order, earlier edges in [[Shortest path problem|shortest paths]] always come before later edges in [[Shortest path problem|shortest paths]], then we only need to relax each directed edge once.

If for every vertex $v$ of $G$, there is a [[Shortest path problem|shortest path]] $p = \langle v_0, v_1, \dots, v_k \rangle$ from $v_0=s$ to $v_k = v$, such that the earlier edges in $p$ are relaxed before later edges in $p$, then $v.d = \delta(s, v)$ for all vertices $v$ in $G$.


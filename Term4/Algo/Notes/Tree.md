---
aliases: tree
tags: #50.004
---
[[Algo]]
[[Algo week 9]]
[[Graphs - further terminologies]]

## What is a tree
>An undirected [[Graphs|graph]] is a **tree** if it is [[Connectedness|connected]] and acyclic.

**Acyclic:** the graph contains no [[Path and Cycles|cycles]].
**Connected**: for every 2 vertices $u, v$ there is a [[Path and Cycles|path]] from $u$ to $v$.

Let $G$ be an undirected tree. Let $u, v$ be distinct vertices of $G$.
- There must be exactly one [[Path and Cycles|path]] from $u$ to $v$.
- This path must be a **simple** path.
**Simple graph**: no loops or multiple edges

> For every vertex $v \in V'$, there is a unique simple path from $s$ to $v$.

> A directed graph is called a tree if its underlying undirected graph is a tree.

## Vertices and Edges
>A tree with $n$ vertices must have $n-1$ edges.

## What is a rooted tree
> A **rooted tree** is a tree with a "specially distinguished" vertex called the **root** such that for every non-root $v$, there is exactly one [[Path and Cycles|path]] from the root to $v$.\
> A rooted tree can be directed or undirected.

If $r$ is the root, we say the tree is rooted at $r$.

Terminology & properties:\
Suppose $T = (V,E)$ is a tree rooted at $r$. Let $v \in V$ be a vertex.

> If $v \not = r$, then there is exactly one [[Path and Cycles|path]] $\langle r, \dots, v \rangle$ from $r$ to $v$.

> The **parent** of $v$ is the vertex immediately before $v$ in $\langle r, \dots, v \rangle$.

> A **child** of $v$ is a vertex whose *parent* is $v$.

> A **leaf** is a vertex with no children.

> An **ancestor** of $v$ is a vertex that comes before $v$ in $\langle r, \dots, v \rangle$.

> A **descendant** of $v$ is a vertex that has $v$ as one of its ancestors.
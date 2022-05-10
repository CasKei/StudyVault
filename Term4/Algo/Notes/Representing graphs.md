---
aliases: incidence list, incidence matrix, adjacency list, adjacency matrix
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

## Referencing vertices and edges
Whether a [[Graphs - further terminologies|graph]] $G = (V, E)$ is **directed** or **undirected**, an edge $e$ (an element in $E$) consists of 2 vertices, say $u$ and $v$.

**Directed G**: $e = (u, v)$\
**Undirected G**: $e = \set{u, v}$

$u$ and $v$ are **incident** to $e$.

Vertex is **isolated** if not *incident* to any edge.

**Adjacent** vertices are *incident* to the same edge. (informally, connected by an edge)

> RMB: Vertices **incident to** edges\
> Vertices **adjacent to** vertices

## Incidence List
Consider a graph $G = (V, E)$ with $n$ vertices.

> An **incidence list** is a [[Hash Table]] $A$ with $n$ slots, where each slot is a [[Arrays and Linked Lists|Linked List]] (i.e. [[Intro to hashing|collisions]] are resolved by chaining)

Each slot corresponds to some vertex $v$. The [[Arrays and Linked Lists|linked list]] in this slot consists of **edges incident** to $v$.
- When $G$ **undirected**, this LL contains **all** edges incident to $v$.
- When $G$ **directed**, this LL contains only those directed edges incident to $v$ for which $v$ is the tail. (edges going away from $v$)
![[Pasted image 20220322203824.png]]

## Incidence matrix
Consider a graph $G = (V, E)$ with $n$ vertices and $m$ edges.

> An **incidence matrix** is a $n$-by-$m$ matrix $M$, where the rows and columns correspond to vertices and edges respectively.

**Undirected**: $(i,j)^{th}$ entry of $M$ equals 1 if the $i$-th vertex is incident to the $j$-th edge, and 0 otherwise.\
**Directed**: $(i,j)^{th}$ entry of $M$ equals 1 if the $i$-th vertex is the head of the $j$-th edge, -1 if $i$-th vertex is tail of the $j$-th edge, and 0 otherwise.
![[Pasted image 20220322204638.png]]

## Adjacency List
Consider a graph $G = (V, E)$ with $n$ vertices.

> An **adjacency list** is a [[Hash Table]] $A$ with $n$ slots, where each slot is a [[Arrays and Linked Lists|linked list]]  (i.e. [[Intro to hashing|collisions]] are resolved by chaining)

Each slot corresponds to some vertex $v$. The linked list in htis slot consists of vertices **adjacent to** $v$.

**Undirected**: this LL contains all vertices **adjacent** to $v$\.
**Directed**: this LL contains only the vertices $u$ **adjacent to** $v$ for which $(v,u)$ is a *directed edge* in $G$, i.e. $v$ is the tail.
![[Pasted image 20220322205640.png]]

## Adjacency matrix
Consider a **simple** graph $G = (V, E)$ with $n$ vertices.

> An **adjacency matrix** is a $n$-by-$n$ **square** matrix $M$, where the rows and columns correspond to vertices of $G$.

**Undirected**: $(i,j)$-th entry equals 1 if $\set{v_i, v_j}$ is a edge of $G$, and 0 otherwise.\
**Directed**: $(i,j)$-th entry equals 1 if $(v_i, v_j)$ is a directed edge of $G$, and 0 otherwise.

If symmetrical, undirected.
![[Pasted image 20220322210337.png]]

---
tags: #50.004
---
[[Algo]]
[[Algo week 6]]
[[Depth-First-Search (DFS)|DFS]]
[[Directed acyclic graph (DAG)|DAG]]

## Topological sort
> Topological sort of a [[Directed acyclic graph (DAG)|DAG]]
> $G = (V, E)$

- Run [[Depth-First-Search (DFS)#Algorithm|DFS(G)]], compute finishing times of nodes for every vertex of $G$.
- Outputs the nodes in ==decreasing order of finishing times==. i.e. Return an ordered sequence of the vertices based on the reverse order of their finishing times.

> A topological sort of a directed [[Graphs - further terminologies|graph]] $G = (V,E)$ is a sorting of $V$ into an ordered sequence, such that i $(u,v)$ is any edge in $E$, then $u$ must come before $v$ in this ordered sequence.

## Properties
- Topological sort applies to a [[Directed acyclic graph (DAG)|DAG]]

- A topsort of [[Directed acyclic graph (DAG)|DAG]] G is a linear ordering of all its vertices such that if G contains an edge u pointing to v, then u appears before v in the ordering.

[[Shortest-paths properties#Path Relaxation Property|Topsort and the path relaxation property]]
Given a [[Weight function|weighted]] [[Directed acyclic graph (DAG)|DAG]], we can use a topologica sort toget a [[Edge relaxation]] order such that the earlier edges in [[Shortest path problem|shortest paths]] always come before later edges in [[Shortest path problem|shortest paths]].

## DFS Tree
Graph formed by DFS is called DFS tree, which is a DAG. Therefore, resultant topsort is the topsort for the DFS forest
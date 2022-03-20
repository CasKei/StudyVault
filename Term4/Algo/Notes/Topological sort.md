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

- Run [[Depth-First-Search (DFS)#Algorithm|DFS(G)]], compute finishing times of nodes.
- Outputs the nodes in ==decreasing order of finishing times==.

## Properties
Topological sort applies to a [[Directed acyclic graph (DAG)|DAG]]

A top sort of [[Directed acyclic graph (DAG)|DAG]] G is a linear ordering of all its vertices such that if G contains an edge u pointing to v, then u appears before v in the ordering.

## DFS Tree
Graph formed by DFS is called DFS tree, which is a DAG. Therefore, resultant topsort is the topsort for the DFS forest
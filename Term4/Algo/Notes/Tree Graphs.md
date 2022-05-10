---
aliases: forest
tags: #50.004
---
[[Algo]]
[[Algo week 6]]
[[Graphs]]

## Tree graphs
| Undirected                           | Directed                                                           |
| ------------------------------------ | ------------------------------------------------------------------ |
| Connected with no cycles             | [[Directed acyclic graph (DAG)]] and its underlying skeleton is a tree |
| ![[Pasted image 20220301133629.png]] | ![[Pasted image 20220301133640.png]]                                                                   |

When there are directions, we can define parent nodes and child nodes.
Directed edges always points away from parent towards child nodes.

## Forest
A [[Connectedness|disjoint]] union of tree graphs.

## Minimal Spanning Tree
> A MST `H` of a graph `G` is defined as follows:
> - `H` and `G` have the same set of vertices
> - `H` is a tree
> - The edges of `H` are a subset of the edges of `G`
>
> Mathematically,
> - $V_H = V_G$
> - `H` is tree
> - $E_H \subset E_G$

MSTs are not necessarily unique for a specific graph `G`.
If a graph is not [[Connectedness|connected]], then it has no MST.
![[Pasted image 20220301134030.png]]
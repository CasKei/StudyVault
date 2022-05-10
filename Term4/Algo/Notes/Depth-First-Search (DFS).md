---
aliases: DFS, predecessor subgraph, DFS tree, DFS forest
tags: #50.004
---
[[Algo]]
[[Algo week 6]]
[[Graph Search|DDW DFS]]

## What is DFS
Another algo for searching or traversing [[Tree Graphs|tree]] or [[Graphs|graph]] [[Data Types and Data Structures|data structures]].
Like exploring a maze.
From current `v`, move to another until you get stuck.
When stuck, backtrack until you find a new place to explore.
Searches as deeply as possible.
All vertices are explored.

Used in both undirected and directed graphs, just like [[Breadth-First-Search (BFS)|BFS]].
Can be used to perform [[Topological sort]]

## Idea
Similar to exploring a maze
- follow path till stuck
- backtrack along breadcrumbs
- [[Sorting, solving recursion|recursively]] explore

## Traversal Order
see also: [[Breadth-First-Search (BFS)|BFS]]
![[Pasted image 20220301140521.png]]

## Problem: Cycles
What happens if we ==unknowingly revisit== a vertex?
DFS: Go in circles.

Solution: Mark vertices if visited.

## Algorithm
Simplest
```python
parent = {s: None}

def DFS_visit(V, Adj, s)
	for v in Adj[s]
		if v not in parent
			parent[v] = s
			DFS_visit(V, Adj, v)
```

Using color and timestamp
```python
def DFS(G)
	for each vertex u in G.V
		u.color = WHITE
		u.p = NIL
	time = 0

	for each vertex u in G.V
		if u.color == WHITE
			DFS_visit(G, u)

def DFS_visit(G, u)
	time = time + 1 # white vertex u has just been discovered
	u.d = time
	u.color = GRAY

	for each v in G.Adj[u] # explore edge (u,v)
		if v.color == WHITE
			v.p = u
			DFS_visit(G,v)
	u.color == BLACK
	time = time + 1
	u.f = time # finishing time
```

![[Pasted image 20220301145957.png]]

## Predecessor Subgraph
AKA DFS [[Tree Graphs|tree]]/[[Tree Graphs|forest]].
Is a subgraph of the original graph.
Defined by:
>$G_{\pi} = (V, E_{\pi})$, where
>$E_{\pi} = \set{(v.\pi , v): v \in V \text{ and } v.\pi \not= NIL}$.

## Edge Classification
DFS can be used to classify edges wrt a DFS forest:
> **Tree edges**: edges in the DF forest $G_{\pi}$.
> Edge $(u,v)$ is a tree edge if `v` was first discovered by exploring edge $(u,v)$.

> **Back edges**: edges $(u,v)$ connecting a vertex `u` to an ancestor `v` in a DF tree.
> We consider self-loops, which may occur in directed graphs, to be back edges.

> **Forward edges**: non-tree edges $(u,v)$ connecting a vertex `u` to a descendant `v` in a DF tree.

> **Cross edges**: all other edges.
> Can go between vertices in the same DF tree, 
> as long as one vertex is not an ancestor of the other,
> or they can go between vertices in different DF trees.

## Properties of DFS
> Back edges:
> $v.d < u.d < u.f < v.f$

> Forward edges:
> $u.d < v.d < v.f < u.f$

> Cross edges:
> $v.d < v.f < u.d < u.f$

> Tree edges:
> First time $v$ is visited.

## Cycle detection
> Graph `G` has a cycle iff DFS has a back edge.
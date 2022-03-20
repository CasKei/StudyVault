---
aliases: BFS
tags: #50.004
---
[[Algo]]
[[Algo week 6]]
[[Graph Search#Breadth First Search BFS|DDW BFS]]

## What is BFS
An algorithm for searching a [[Graphs|graph]] [[Data Types and Data Structures|data structure]].
Discovers vertices in a breadth-wise manner.
Choose a start source node `v`.
Find all nodes distance 1 from `v`,
then distance 2 from `v`,
cont.

## Traversal Order
see also: [[Depth-First-Search (DFS)|DFS]]
![[Pasted image 20220301140543.png]]

## Procedure
- Start with vertex `v`
- List all neighbours distance 1 from `v`
- List all neighbouts distance 2 from `v`
- etc.

Algo starting at `v`
- Define frontier `F`
- Initially $F=\set{v}$
- repeat: $F' = \set{\text{all new neighbours of vertices in F}}$, $F=F'$
- until all possible vertices are found.

> **Frontier**: the last level of reachable nodes
> **Level**: stores the nodes seen so far and their distance from the root

 ## Problem: Cycles
What happens if we ==unknowingly revisit== a vertex?
BFS: get wrong notion of distance

Solution: Mark vertices if visited.

## Algorithm
[[Arrays and Linked Lists|Array]] + [[Graphs#Adjacency list|adjacency list]] implementation
```python
function BFS(s, Adj)
	level = {s: 0}
	parent = {s: None}
	i = 1
	frontier = [s]

	while frontier:
		next = []
		for u in frontier:
			for v in Adj[u]
				if v not in level
					level[v] = i
					parent[v] = u
					next.append(v)
		frontier = next
		i += 1
```

[[Stacks and Queues|Queue]] + [[Graphs#Adjacency list|adjacency list]] implementation
```python
function BFS(G, s)
	for each vertex u in G.V - {s}
		u.color = WHITE
		u.d = \infty
		u.p = NIL

	s.color = GRAY
	s.d = 0
	s.p = NIL
	Q = {}
	enqueue(Q, s)

	while Q != {}
		u = dequeue(Q)
		for each v in G.Adj[u]
			if v.color == WHITE
				v.color = GRAY
				v.d = u.d + 1
				v.p = u
				enqueue(Q,v)
		u.color = BLACK
```
(If replace [[Stacks and Queues|queue]] with [[Stacks and Queues|stack]], it becomes [[Depth-First-Search (DFS)|DFS]])

## Shortest Paths from S
The length of shortest path from `s` to `v` is
- `level[v]`
- $\infty$ (if unreachable from `s`)

To find shortest path from `s` to `v`,
Follow
`v` --> `parent[v]` --> `parent[parent[v]]` --> ... until `s`

## [[Connectedness|Disjoint]] graphs
BFS does not necessarily visit all vertices

## Examples
![[Pasted image 20220301143509.png]]
![[Pasted image 20220301143518.png]]

![[Pasted image 20220301143553.png]]
![[Pasted image 20220301143606.png]]
![[Pasted image 20220301143623.png]]

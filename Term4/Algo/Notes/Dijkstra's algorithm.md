---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

[[Single-source shortest path problem]]
## The Case of Non-Negative Weights
In many applications of this problem, the weights are non-negative.\
If all weights are non-negative, there is no negative weight-cycle.\
When extending a [[Path and Cycles|path]] by one more edge, the weigh of the new path is at least the weight of the original path.

Suppose we are given a [[Weight function|weighted]] directed [[Graphs|graph]] $G=(V,E)$, a source vertex $s$ and a [[Weight function]] $w$ satisfying $w(e) \geq 0 \text{ }\forall \text{ } e \in E$.

New approach to solve the [[Single-source shortest path problem]] for $G$
- As before, iteratively update $d$ nd $\pi$ values of all vertices
- Maintain a set $S$ of vertices $v$ whose shortest-paths weights have already been determined
	- i.e. we already know that $v.d = \delta(s,v)$
- iteratively update the set $S$, starting with $S=\emptyset$.

## Dijkstra's Algorithm
[[Directed acyclic graph (DAG)|DAG]]
[[Representing graphs|adjacency list]]
[[Iterative approach to estimate shortest path#Initialisation of d and pi values]]
[[Heap Operations#extract_max A]]
[[Priority Queue]]
[[Edge relaxation]]
```php
function Dijkstra(G,w,s)
	'''
	Require: A weight function w for G
	Require: A vertex s of G
	Require: A DAG G represented as an adj list, where G.Adj[u] isthe LL of vertices adj to u
	'''
	initialise_single_source(G,s)
	S <- ∅ // initialise S as empty set
	Q <- G.V // Q is a min-priority queue. Elements of Q are vertices, and keys of these elements are the d values
	while Q != ∅
		u <- extract_min(Q) // u has smallest d among vertices in Q, and it is removed from Q
		S <- S ∪ {u}
		for each vertex v in G.Adj[u]
			relax(u,v,w)
```

## Complexity
Complexity depends on how we implement $Q$ as a min-[[Priority Queue]].

Initialisation: $\Theta(|V|)$\
Initialise S as empty set: $\Theta(1)$\
extract_min(Q): implement [[Priority Queue]] as a min-[[Heap]]: $O(\log{|V|})$\
S <- S ∪ {u}: $\Theta(1)$\
[[Edge relaxation|relax]]: require [[PSet 1#^4bd01d|decrease_key]] operation when assigning new $d$ value, which has complexity $O(\log{|V|})$

Note: $Q$ can be implemented as a min-heap. Start with $G.V$ represented as an array, then run [[PSet 1#^74b861|build_min_heap]] on this array.

Overall complexity of Dijkstra using binary min-heaps: $O((|V| + |E|)\log{|V|})$


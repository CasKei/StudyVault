---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

[[Iterative approach to estimate shortest path]]

## Bellman-Ford Algorithm
[[Edge relaxation]]
```php
function Bellman_Ford(G,w,s)
	'''
	Require: A directed graph G wit vertex set G.V and edge set G.E
	Require: a weight function w for G. A vertex s of G
	'''
	// Main loop: update d and pi for all V
	for i = 1 to |G.V| - 1:
		for every directed edge (u,v) in G.E:
			relax(u,v,w)

	// Final check for whether G has no neg weight
	// cycles reachable from s
	// returns TRUE if no neg weight cycles, FALSE otherwise
	for every directed edge (u,v) in G.E:
		if v.d > u.d + w(u,v)
			return False
	return True
```
For this algo to make sense, we must specify the order of edges of $G$.\
IOW, we must specify the **relaxation order**.

## Examples


## Correctness
Let $G=(V,E)$ be a [[Weight function|weighted]] directed [[Graphs - further terminologies|graph]], let $s$ be a vertex of $G$, and let $w:E\to \mathbb{R}$ be the [[Weight function]] of $G$.

### Lemma 24.2
If $G$ contains no negative-weight cycles reachable from $s$, then after $|V| - 1$ iterations in the main loop of the Bellman-Ford algorithm, we have $v.d = \delta(s,v)$ for all vertices $v$ of $G$, no matter what order of edges is used for relaxation.

### Theorem 24.4: Bellman-Ford algorithm is correct
If $G$ contains no negative-weight cycles reachable from $s$, then the Bellan-Ford algorithm returns TRUE, $v.d = \delta(s,v)$ for all vertices $v$ of $G$, ad te $\pi$ values determine a [[Shortest-path tree]] rooted at $s$.

If $G$ contains at least one negative-weight cycle reachable from $s$, then the algo returns FALSE.

## More preperties
Chapter 24.5 of CLRS
[[Shortest-paths properties]]

## Complexity
Initialisation : $\Theta(|V|)$\
Main loop: $\Theta(|V| \cdot |E|)$\
Final check: $\Theta(|E|)$
[[Iterative approach to estimate shortest path#Initialisation of d and pi values]]
`initialise_single_source(G,s)`: $\Theta(|V|)$
---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]
[[Graphs - further terminologies]]

## Single-source shortest path problem
**Problem**
>Given $G = (V,E)$ a [[Weight function|weighted]] directed [[Graphs|graph]], and a single "source vertex" $s$, find a [[Shortest path problem|shortest path]] in $G$ from $s$ to every other possible vertex $v$ of $G$.

Let the [[Weight function]] of $G$ be $w: E \to \mathbb{R}$.\
Let $\delta(u,v)$ be the shortest-path weight from $u$ to $v$.

## Examples
### Navigation
Source vertex = start location\
Vertices = nagivation waypoints\
Edges = segments of roads\
Weights = distance/traffic info
### Integrated Circuit Design
Some 3D path for more efficient circuit or sth.

## To solve this problem:
For every vertex $v \in V$, $v \not= s$,

- Compute the shortest-path weight $\delta(s, v)$.
- Find at least one shortest [[Path and Cycles|path]] from $s$ to $v$, i.e. a path with weiht $\delta(s, v)$.

*Crucial idea:* Insetad of finding individual shortest paths, we find a *single* [[Tree]] rooted at $s$ that contains all required shortest paths.
> This tree is called the [[Shortest-path tree]].

[[Iterative approach to estimate shortest path]]
[[Bellman-Ford Algorithm]]

## What we know so far
### How to solve [[Single-source shortest path problem]]?
Compute a [[Shortest-path tree]] for given input [[Graphs|graph]] $G=(V,E)$.

### How to compute [[Shortest-path tree]]?
[[Edge relaxation]] iteratively on a suitable sequence of edges.
[[Bellman-Ford Algorithm]]: need to relax $(|V| - 1)|E|$ edges.
- **BAD** relaxation orders require all $(|V| - 1)|E|$ relaxations
- **GOOD** relaxation orders require as little as $|E|$ relaxations.
- We still need $(|V| - 1)$ iterations in the main loop, since we do not know beforehand whether our order is good or bad. This depends on $G$, weights and the source vertex.

Are there relaxation orders that are "good" for certain kinds of directed [[Weight function|weighted graphs]]?
![[Shortest-paths properties#Path Relaxation Property|Path Relaxation Property]]
![[Directed acyclic graph (DAG)#Single-source shortest path problem Single-source shortest path in DAGs|DAG shortest paths]]

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

[[Dijkstra's algorithm]]
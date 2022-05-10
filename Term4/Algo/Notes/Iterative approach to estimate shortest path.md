---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]
[[Single-source shortest path problem]]
## Iterative approach to estimate $\delta(s,v)$
[[Weight function|Weighted]] directed [[Graphs|graph]] $G$ with source vertex $s$.
![[Pasted image 20220323113811.png]]

For every vertex $v$ in $G$, we store a estimate for $\delta(s,v)$.
- Store this estimate as attribute $v.d$ for each $v$ in $G$.
- $s.d = 0$ since $\delta(s,s) = 0$
- For all other vertices $v$, initialise $v.d = \infty$

Given initial estimates $v.d$ for all $v$, we iteratively updte our estimates.
- $v.d$ is the current lowest weight found so far for a [[Path and Cycles|path]] from $s$ to $v$. Update $v.d$ only when a "strictly better" estimate has been found.
- Update process should be "exhaustive", so that if none of the attribute values $v.d$ can be further updated, then $v.d = \delta(s,v)$. 


![[Pasted image 20220323114619.png]]
To construct $G'$ from $G$, we need to specify the **parent** for every vertex $v \in V'$.\
To do so, we store the parent of $v$ as the attribute $v.\pi$.

## Initialisation of $d$ and $\pi$ values
Let $G = (V, E)$ be a [[Weight function|weighted]] directed [[Graphs|graph]], let $s$ be a vertex of $G$, and let $x: E \to \mathbb{R}$ be the [[Weight function]] of $G$.

**Assume**: every vertex $v$ of $G$ has 2 attributes $v.d$ and $v.\pi$
- $v.d$: an estimate of the value of $\delta(s,v)$
- $v.\pi$: the parentof the vertex $v$ in the [[Shortest-path tree]]

```php
function initialise_single_source(G,s):
	'''
	Require: G = (V, E) is a weighted directed graph
	Require: s in V is a vertex
	'''
	for every vertex v in V:
		v.d <- \infty
		v.pi <- NIL
	s.d <- 0
```
Note: `initialise_single_source(G, s)` has no output. Instead, this function assigns initial $d$ and $\pi$ values for all vertices in $G$.

## Using the [[Triangle inequality]]
Let $G = (V, E)$ be a [[Weight function|weighted]] directed [[Graphs|graph]], let $s$ be a vertex of $G$.
[[Triangle inequality|Recall]]
> If $(u,v)$ is an edge, then by the [[Triangle inequality]],
$$
\begin{align}
\delta(s,v) &\leq \delta(s,u) + \delta(u,v)\\
&\leq \delta(s,u) + w(u,v)\\
&\leq u.d + w(u,v)
\end{align}
$$

This means that $u.d + w(u,v)$ is an upper bound for $\delta(s, v)$.

If $u.d + w(u,v) < v.d$, i.e. this upper bound is strictly smaller than the current estimate for $\delta(s,v)$, then we can proceed to reassign a new updated value $v.d \gets u.d + w(u,v)$.

The new updated value $v.d$ is closer to $\delta(s,v)$.

## Relax the edges
![[Edge relaxation]]

Intuition: Run `initialise_single_source(G,s)` to initialise graph, then run `relax(u,v,w)` iteratively on multiple edges $(u,v)$, until no relaxation of edges will update the $d$ and $\pi$ values anymore.

## Solving the [[Single-source shortest path problem]]
**Problem**
>Given $G = (V,E)$ a [[Weight function|weighted]] directed [[Graphs|graph]], and a single "source vertex" $s$, find a [[Shortest path problem|shortest path]] in $G$ from $s$ to every other possible vertex $v$ of $G$.

Let the [[Weight function]] of $G$ be $w: E \to \mathbb{R}$.\
Let $\delta(u,v)$ be the shortest-path weight from $u$ to $v$.

**Approach**
Compute a [[Shortest-path tree|shortest-path tree]] $G'$ for $G$.

- Every vertex $v$ of $G$ has two attributes $v.d$ and $v.\pi$.
- Run `initialise_single_source(G,s)` to initialise attribute values.
- Iteratively update these attribute values by running [[Edge relaxation]] steps for a suitable sequence of edges.
	- Find $\pi$ values of the vertices determine a [[Shortest-path tree]]
	- Find $d$ value of each vertex $v$ is the [[Shortest path problem|shortest path]] [[Weight function|weight]] $\delta(s,v)$.

![[Bellman-Ford Algorithm]]
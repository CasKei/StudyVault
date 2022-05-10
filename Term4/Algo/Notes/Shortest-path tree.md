---
aliases: shortest-path tree
tags: #50.004
---
[[Algo]]
[[Algo week 9]]
[[Graphs - further terminologies]]

## Shortest-paths tree
Let $G = (V, E)$ be a [[Weight function|weighted]] directed [[Graphs|graph]] with [[Weight function]] $x: E \to \mathbb{R}$, and let $s$ be a vertex of $G$.

A **shortest-paths** [[Tree|tree]] for $G$ is a direted graph $G' = (V', E')$ that satisfies the following conditions:
- $G'$ is a subgraph of $G$ : $V' \subseteq V$, $E' \subseteq E$.
- $G'$ is a tree rooted at vertex $s$. The vertices of $G'$ are all vertices that are reachable from $s$.
	- Because of the [[Tree]] structure, we know that for every vertex $v \in V'$ there is a unique simple path from $s$ to $v$.
- For every $v \in V'$, the unique simple apthfrom $s$ to $v$ is a [[Shortest path problem|shortest path]] from $s$ to $v$

---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

## Triangle inequality for shortest paths
Let $\langle s, \dots, v \rangle$ be a [[Shortest path problem|shortest path]] from vertex $s$ to vertex $v$.

For any vertex $x$ in this shortest [[Path and Cycles|path]], we have the equation
$$\delta (s, v) = \delta(s, x) + \delta(x, v)$$
For any vertex $x'$ not in this shortest path, we have the inequality
$$\delta(s, v) \leq \delta(s, x') + \delta(x', v)$$ More generally, for any vertices $s,u,v$ in a [[Weight function|weighted]], directed [[Graphs|graph]], we have the **triangle inequality**, which says that
$$\delta(s, v) \leq \delta(s,u) + \delta(u, v)$$

## Useful consequence
If $(u,v)$ is a directed edge, then 
$$\delta(s, v) \leq \delta(s, u) + w(u,v)$$
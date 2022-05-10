---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

## Relaxation of edges
Let $G =(V, E)$ be a [[Weight function|weighted]] directed [[Graphs|graph]], let $s$ be a vertex of $G$, and let $x: E \to \mathbb{R}$ be the [[Weight function]] of $G$.

**Assume**:\
Every vertex $v$ of $G$ has 2 attributes $v.d$ and $v.\pi$
- $v.d$: an estimate of $\delta(s,v)$
- $v.\pi$: the parent of the vertex $v$.

```php
function relax(u, v, w)
	'''
	Require: (u, v) is a directed edge of G
	'''
	if u.d + w(u,v) < v.d then
		v.d <- u.d + w(u,v)
		v.pi <- u
```

## What does this do?
Running `relax(u,v,w)` would update the value of $v.d$ if this value is strictly larger than $u.d + w(u,v)$.

If $u.d = k < \infty$, then there is a path from $s$ to $u$ with weight $k$.

We can extend this path by the edge $(u,v)$, thereby giving a new path from $s$ to $v$ with weight $k+w(u,v)$.

If the current estimate $v.d$ is larger than $k+w(u,v)$, then we have found a better estimate; we replace $v.d$ with this new estimate.

Intuitively, we are checking if we can improve our estimate $v.d$ by trying out a path from $s$ to $v$ through the edge $(u,v)$.
![[Pasted image 20220323140449.png]]
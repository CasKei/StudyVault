---
aliases: path, cycle
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

> A **path** in [[Graphs|graph]] $G$ is a sequence of edges $(e_1,e_2, \dots, e_k)$ such that every 2 consecutive edges $e_i, e_{i+1}$ in this sequence are incident to a common vertex $v_i$.

> A **cycle** in a [[Graphs|graph]] $G$ is a **path** $(e_1,e_2, \dots, e_k)$ such that the first and last edges $e_1, e_k$ are **incident** to a common vertex.

> **Acyclic** graph has no cycles.

![[Pasted image 20220322211338.png]]

## A path from one vertex to another
Let $(e_1,e_2, \dots, e_k)$ be a **path** in graph $G$.

Suppose each edge $e_i$ is the pair $\set{v_{i-1}, v_i}$ or $(v_{i-1}, v_i)$.\
Then this path joins the sequence of vertices $v_0, v_1, \dots, v_k$.

We say this is a path from $v_0$ to $v_k$.

If all vertices $v_0, v_1, \dots, v_k$ are distinct, then the path is **simple**.\
*Coursebook*: We can also represent this path as the sequence $\langle v_0, v_1, \dots, v_k \rangle$.
![[Pasted image 20220322212509.png]]

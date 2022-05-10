---
aliases: weighted graph
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

Consider a [[Graphs|graph]] $G = (V,E)$ with $n$ vertices and $m$ edges.

Suppose $V = \set{v_1, \dots, v_n}$ and $E = \set{e_1, \dots, e_m}$.

Remember: Each edge $e_k$ is a pair $\set{v_i, v_j}$ or $(v_i, v_j)$.

> A **weight function** of $G$ is a function $w: E \to \mathbb{R}$.

i.e. an assignment of real values called *weights* to the edges of $G$

A **weighted graph** is a graph that has a weight function.

The weight of a edge $e$ can be written as $w(e)$.

The weight of a [[Path and Cycles|path]] $(e_1,e_2, \dots, e_k)$ is the sum of the weights of the edges in the path, i.e. $w(e_1) + \dots + w(e_k)$.
Can be written as $w(p)$.


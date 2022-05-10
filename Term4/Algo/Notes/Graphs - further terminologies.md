---
tags: #50.004
---
[[Algo]]
[[Algo week 9]]

Recall:\
A [[Introduction to Graph|graph]] $G$ consists of a set $V$ of vertices, and a set $E$ of edges.

We usually write "Let $G = (V, E)$ be a graph..."

## Directed graph
>**Directed graph** is a graph whose edges are **ordered pairs** of vertices.\
>i.e. $(u, v) \not= (v, u)$.

We interpret an edge $(u,v)$ as a **directed edge** from $u$ to $v$.\
$u$ is called the **tail** and $v$ is called the **head** of this edge.

## Undirected graph
> **Undirected graph** is a graph whose edges are **unordered pairs** of vertices.\
> i.e. $\set{u, v} = \set{v, u}$.

An edge $\set{u, v}$ is a set of 2 vertices. There is no head or tail.

## Simple graph
> **Simple graph** is a graph with no loops or multiple edges.

## Weighted graph
>**Weighted graph** is a graph where every edge is assigned a weight.
>(A weight is a numerical value).

## Graphs by default
By default, a graph is assumed to be simple, undirected, and unweighted, unless the context suggests otherwise (e.g. mention of weights)

![[Pasted image 20220322201507.png]]
Note: not every vertex of a graph has to be [[Connectedness|connected]] to edges.

Can have **isolated vertices**

[[Representing graphs]]
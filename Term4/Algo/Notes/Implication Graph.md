---
tags: 50.004
---
[[Algo]]
[[2SAT solver]]

> An **implication graph** is a directed [[Graphs|graph]] in which there is one vertex per variable or negated variable, and an edge connecting one vertex to whenever the corresponding variables are related by an implication in the implicative normal form of the instance.

An implication graph must be a skew-symmetric graph, meaning that it has a symmetry that takes each variable to its negation and reverses the orientations of all of the edges.

IOW: in order to satisfy all the clauses, when a literal is true, all the output edges from its corresponding vertex carryout the adjacent literal to be true. There must not be any other variabls where there is a path from that variable to its complement.
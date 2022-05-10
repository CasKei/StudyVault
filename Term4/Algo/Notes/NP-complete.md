---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## NP-Complete
> A problem is NP complete if it is both an [[NP problems|NP]] problem and an [[NP-hard]] problem.

Intuition:
NP-complete problem is the 'hardest' problem in NP.

## Examples
SAT problem, 3-SAT problem, graph coloring problem, 4-way matching problem, vertex cover problem, Hamiltonian path problem, longest path problem, clique problem, independent set problem, multiprocessor scheduling problem, max-cut problem, quadratic programming, integer linear programming, etc.

## Note
A [[Polynomial time]] algorithm to solve just one NP-complete problem would imply polynomial time algorithms to solve all NP-complete problems.

Given some B, if we can show a [[Polynomial-time reductions]] of the 3SAT to B, then B must be [[NP-hard]].
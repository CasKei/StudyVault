---
tags: 50.004
---
[[Algo]]
[[Boolean Satisfiability (SAT) with recursion]]
## Boolean Satisfiability Problem
> The problem of determining of a Boolean formula is satisfiable or unsatisfiable.

- **Satisfiable**: if the boolean variables can be assigend values such that the formula turns out to be true, then the formula is satisfiable
- **Unsatisfiable**: if it is not possible to assign such values, then the formula is unsatisfiable.



## 2SAT
A computational problem of assigning values to variables, each of which has 2 possible values, to satisfy a system of contraints on pairs of variables.

A special case of the general boolean satisfiability problem and constraint satisfaction problems.

But those are NP-complete. 2SAT can be solved in polynomial time.

## Instances of 2SAT problem
Can be expressed as boolean formulas called conjunctive normal form, or Krom formulas.

Alternatively expressed as a special type of directed [[Graphs|graph]], the [[Implication Graph]], which expresses the variables of an instance and their negations as vertices in the graph, and constraints on pairs of variables as directed edges.
Both of these kinds of inputs can be solved in linear time, either by backtracking or using the strongly conected components of the implication graph.

## Algorithms
Resolution and transitive closure

Limited backtraacking

[[Strongly connected components]]

Here we choose to use the notion of [[Strongly connected components]] from graph theory and [[Kosaraju's Algorithm]]. The 2SAT problem involves making the CNF true.

UNSAT if there exists a variable x such that
- there is a path from x to ~x in the graph
- there is a path from ~x to x in the graph.

## [[Kosaraju's Algorithm]]
First find groups of [[Strongly connected components]] by using [[Kosaraju's Algorithm]].

## Check SAT
After finding the [[Strongly connected components]], check if the variable and its complement exists within the same [[Strongly connected components]]. If it does, it is UNSAT as it is impossible for a variable to be both true and false.

## Procedure
Create [[Implication Graph]]

Find [[Strongly connected components]].
1. 2 [[Depth-First-Search (DFS)|DFS]]
	1. [[Depth-First-Search (DFS)|DFS]] 1 aims to arrange nodes in the stack based on which node vomes first
	2. Transpose to indentify paths between nodes where arrows are reversed to check for [[Strongly connected components]] on both paths x -> y or y -> x.
	3. [[Depth-First-Search (DFS)|DFS]] 2 on the transposed graph to find [[Strongly connected components]] between adjacent nodes.


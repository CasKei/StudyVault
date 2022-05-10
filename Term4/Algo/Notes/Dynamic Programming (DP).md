---
aliases: DP
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]
[Website](https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0)

## What is DP
> DP is an algorithmic technique for solving an optimisation problem by breaking it down into simpler subproblems and utilising the fact that the optimal solution to the overall problem depends on the optimal sulution to its subproblems.

A general method for algorithmic design with the following main ideas:
- Divide problem into sub-problems, so solutions can be combined
- Solve each sub-problem just once, and save its solution in a "look-up" table
	- Whenever a solution to a subproblem is found, first check table if solution already computed
		- if computed: retrieve
		- if not: solve

## When to use DP
2 criteria:
### Optimal substructure
An optimal solution to the problem can be obtained by combining optimal solutions to its sub-problems.
Each sub-problem or problem may have more than one optimal solution.

### Overlapping sub-problems
Problem can be broken down into subproblems that are reused several times.
e.g. A recursive algorithmic solution usually solves the same subproblem multiple times, so we say it overlaps.

## Why use DP (Design principle)
Reduce running time for solving the problem.

Instead of using *time* to solve the same subproblem repeatedly, solve just once and use *memory* to save its solution.

This is an example of a *time-memory trade-off*.

For many problems, using DP can reduce time complexity of an algorithmic solution, as compared to a solution to the problem that does not store the solutions to subproblems.

## DP vs [[Insertion Sort and Merge Sort|divide and conquer]]
Both approaches divide problems into subproblems which solutions can be combined into a solution for the problem.

But when sub-problems have repeated sub-problems:

| DP                                                                                                                    | Divide and Conquer                                                                     |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Sove each subsubprob once, then store solution in memory                                                              | Solve each subsubprob more than once                                                   |
| If solution to subsubproblem required subsequently, the solution is retrieved from memory, rather than computed again | If solution to subsubproblem is required subsequently, the solution is computed again. | 

Key difference: DP uses *memory* to store intermediate results.

## Why named DP?
Introduced by *Richard Bellman* in ~1950s

> Bellman ... explained that he invented the name "dynamic programming" to hide the fact that he was doing mathematical research at RAND under a Secrtary of Defence who "had a pathological fear and hatred of the term, research." He settled on "dynamic programming" because it would be difficult to give it a "pejorative meaning" and because "It was something not even a Congressman could object to."
> ~ John Rust 2006

## Applications
Usually used to solve **optimisation problems**.

An optimisation problem could have more than one "optimal" solution (min or max of some function)

Any  solution computed is called _an_ optimal solution (not *the* optimal solution)

DP is used on an optimisation problem that has overlapping subproblems, so as to reduce the time complexity of an algorithmic solution to the problem.
[[Knapsack problem]]
[[Compute Fibonacci Numbers]]
[[Rod-cutting problem]]
[[Text justification problem]]
[[Matrix chain parenthesization problem]]
[[Longest common subsequence problem]]

## Approaches
[[Memoization VS Tabulation]]

[[Top-down Dynamic Programming]]
[[Bottom-up Dynamic Programming]]

## Steps for using DP
Be clear about the exact problem to solve.
1. Define sub-problems of original problem
2. Identify base cases of these sub-problems that are either trivial to solve or solutions already given.
3. Find a recurrence that relates the sub-problems.
4. Use either [[Top-down Dynamic Programming]] or [[Bottom-up Dynamic Programming]]
	1. Top-down: Use recurrence to formulate a recursive algo, then [[Memoization VS Tabulation|memoize]] this recursive algo
	2. Bottom-up: Arrange the sub-problems according to "dependency" order, then [[Memoization VS Tabulation|tabulate]] the solutions to subproblems iteratively.
5. Solve the original problems by combining the computed solutions to sub-problems.

## Complexity for DP
[[Complexity for DP]]
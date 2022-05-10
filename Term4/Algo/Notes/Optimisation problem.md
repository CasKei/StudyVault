---
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Optimisation Problem
> A problem is called an optimisation problem if we want to find the "best" solution, given some input, and some constraints that the solution must satisfy.

Examples:
- [[Single-source shortest path problem]]: find a shortest path from source vertex to each other vertex
- [[Longest common subsequence problem]]: find a longest common subsequence of 2 given sequences
- [[Knapsack problem]]: choose a subset of items so that their value is maximised, while still satisfying the constraint that their total size does not exceed max capacity
- [[Travelling salesman problem]]: find a shortest route that visits each city exactly once and returns to the origin city

## Converting into decision problems
An optimisation problem can be converted into a [[Decision problem]].

Instead of finding a best solution, we are given a candidate solution and the goal is to decide whether the candidate solution is a best solution.

Examples:
- [[Single-source shortest path problem]]: the given candidate is a shortest path, yes/no?
- [[Longest common subsequence problem]]: the given candidate is an LCS, yes/no?
- [[Knapsack problem]]: the given candidate subset of items has maximised total value, yes/no?
- [[Travelling salesman problem]]: the given candidate route is a shortest route, yes/no?

## Solving "converted" decision problems
> If we have a solution to an [[Optimisation problem]], then we can use this solution to solve the "converted" [[Decision problem]].

Example: [[Travelling salesman problem]]
- Suppose we know how to solve this.
- This means we have an algorithm to find a shortest route that visits each city exactly once and returns to origin city
- This means any other shortest route found must have same total distance as the shortest route found
- Solving the decision problem: given a candidate, we can compute its total distance, and check if the value equals the total distance of your shortest route found.
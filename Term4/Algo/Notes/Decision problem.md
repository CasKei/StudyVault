---
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Decision Problem
> A problem is called a decision problem if its solution has 2 possible outcomes

Yes/No, True/False, 0/1, Accept/Reject

Examples:
- Go: white player can force a win, true/false?
- [[Solvable vs Unsolvable|halting problem]]: program `P` will terminate when executed with input `I`, true/false?

## Converting into decision problems
An [[Optimisation problem]] can be converted into a [[Decision problem]].

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

## Certificates
Consider 2 [[Verification algorithms]], one to verify that a 'yes' answer is correct, another to verify a 'no' answer is correct.

For each possible input $I$, we want to find a [[Verification algorithms|certificate]] that can verify the correct answer.

## Guessing
Consider a [[Verification algorithms]] $A(I,E)$ that verifies a "yes" answer to this decision problem.

- Guess
	- randomly generate a valid outcome $E$ for $A(I,E)$
- Verify the guess
	- compute value of $A(I,E)$.

If $A(I,E) = 1$, return "yes", otherwise guess again

Once we found some $E$ such that $A(I,E) = 1$, then this $E$ is a [[Verification algorithms|certificate]] for a "yes" answer to the [[Decision problem]].
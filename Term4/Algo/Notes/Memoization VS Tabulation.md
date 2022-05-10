---
aliases: memoization, tabulation, memoize, tabulate
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Memoization
Used in [[Top-down Dynamic Programming]].

Comes from the word “memorandum”, which means “a note recording something for future use”.

> Memoisation is the method of storing results of function calls

Usually used to store results of expensive functino calls
An example of [[Cache|caching]].

We can *memoize* a [[Sorting, solving recursion|recursive]] algo or function.
By definition, a recursive function calls itself during execution, so the function could eb called many times with different inputs.
To memoize a recursive function, store the output of the function in a table indexed by the possible inputs.

Memoization is usually implemented using a [[Hash Table]].
e.g. Python dictionary (key-value pairs are input-output pairs of function)

### Example: Fib
![[Compute Fibonacci Numbers#^79b625]]
[[Top-down Dynamic Programming]]

### Properties
- Can have many sub-problems, but finding an optimal solution to the problem may not necessarily require solutions to all possible sub-problems (e.g. [[Rod-cutting problem]])
- Only solutions to subproblems that must be solved are saved.
- Usually implemented with [[Hash Table]]

## Tabulation
Used in [[Bottom-up Dynamic Programming]].

### Properties
- Solutions to all possible sub-problems are saved, whether or not they are eventually used to find an optimal solution to the problem
- Tabulation $\approx$ filling in all entries of a table
- Usually implemented with [[Arrays and Linked Lists|array]]

### Example: fib
![[Compute Fibonacci Numbers#^80f9c2]]

Here, we are tabulating the solutions to all subproblems in A.
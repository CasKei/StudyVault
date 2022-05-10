---
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Problem
[[Decision problem]]
Given a set of integers $S$, determine (yes/no) if $S$ can be partitioned into 2 subsets $A$ and $B$, such that the integers in each $A$ and $B$ have exactly the same sums.

Note: a [[Verification algorithms|certificate]] is not a direct answer yes or no
It is "enough information" so that you can verify for yourself the answer for the given input set $S$.

This problem is [[NP problems|in NP]].

## Solving by guessing
Consider a [[Verification algorithms]] $A(I,E)$ that verifies a "yes" answer to this decision problem.

- Guess
	- randomly generate a valid outcome $E$ for $A(I,E)$
- Verify the guess
	- compute value of $A(I,E)$.

If $A(I,E) = 1$, return "yes", otherwise guess again

Once we found some $E$ such that $A(I,E) = 1$, then this $E$ is a [[Verification algorithms|certificate]] for a "yes" answer to the [[Decision problem]].

### Best case
First randomly generated $E$ consists of $A$ and $B$ have the same sums, conclude $A(I,E) = 1$, return "yes".

### Worst case
If each randomly generated $E$ keeps on yielding $A(I,E) = 0$, then the process does not end.

## Reduction
[[Partition problem]] can be reduced to [[Knapsack problem]].
Input to partition problem: a set $S=\set{a_1, \dots , a_n}$ of integers.

If $a_1, \dots , a_n$ do not add up to an even integer, then answer is no.
Else, $a_1+ \dots + a_n =2k$ for some integer $k$.

Reformulation: is there a subset $T \subseteq  S$ such that the integers in $T$ add up to $k$?
- Yes: then $S$ can be partitioned into 2 subsets $T$ and $S\backslash T$, each with the same sum $k$.
- Either of the two subsets can be a [[Verification algorithms|certificate]] for the reformulated problem.

### Key idea
Consider the [[Knapsack problem]] with maximum capacity $k$, and $n$ items, such that the $i$-th item has size $s_i = a_i$ and value $v_i = a_i$.
- Our goal is to find the maximum possible total value of any subset of the 𝑛 items that does not have a total size exceeding 𝑘

2 possibilities:
1. If this max possible total value is $k$, then we can find a subset of $\set{a_1, \dots , a_n}$ whose sum is exactly $k$.
2. If max possible total value is $<k$, then every possible subset $\set{a_1, \dots , a_n}$ whose sum is $\leq k$ must have a sum $<l$.

Conclusion:
By solving this [[Knapsack problem]], we can solve the reformulated partition problem, and thus solve the [[Partition problem]].


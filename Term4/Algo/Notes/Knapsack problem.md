---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Problem
Knapsack = backpack (in the past)

Given a knapsack of maximum capacity $m$, we want to pack inside it items chosen from a set of $n$ items:
- Item $i$ has size $s_i$ and value $v_i$.
- Assume: size and value are positive integers

***Goal***: pack items of total size at most $m$ such taht total value is *maximised*

This is an important problem studied in [[Dynamic Programming (DP)]]. Studied in **combinatorial optimization**.
- Very important problem in resource allocation
- Appeared as Google interview question in several guises
- You may have solved this problem when playing computer games...

This problem is [[NP problems|in NP]].

## Thought process
Idea: vary number of items and max capacity of knapsack.

Let $DP[i,j] =$  maximum possible total value for packing items chosen from item 1 to item $i$, such that the total size of chosen items does not exceed $j$. 

Problem: Compute $DP[n,m]$\
Subproblem: Compute $DP[i,j]$ for all $0 \leq i \leq n$, $0\leq j \leq m$.

## Recurrence relation
For all $1 \leq i \leq n$ and $1 \leq j \leq m$,
$$
DP[i,j] = 
\begin{align}
\begin{cases}
DP[i-1,j] &\text{, if }s_i > j\\
\max{\{DP[i-1,j]\ , \ v_i + DP[i-1, j-s_i]\}} &\text{, if } s_i \leq j
\end{cases}
\end{align}
$$
Intuition:
- If size of item $i$ exceeds capacity $j$, then can't pack
- Otherwise, 2 subcases:
	- If choice of items with max value for capacity $j$ includes item $i$, then the subset of items without item $i$ would have max value for capacity $j-s_i$.
	- If choice of items with max value for capacity $j$ does not include $i$, then this max value equals $DP[i-1,j]$ by definition

## Top-down Solution
[[Top-down Dynamic Programming]]
[[Memoization VS Tabulation|memoize]]
```php
Initialise memo = {}
function DP(i, j)
	if (i, j) in memo then
		return memo[(i, j)]
	if i == 0 or j == 0 then
		memo[(i, j)] <- 0
		return 0
	else
		if s_i > j then
			val <- DP(i-1, j)
			memo[(i, j)] <- val
			return val
		else
			val <- max{DP(i-1, j) , v_i + DP(i-1, j-s_i)}
			memo[(i, j)] <- val
			return val

run DP(n, m)
```

## Bottom-up Solution
alternative notation, `DP[i][j]`
```php
Initialise 2-dim arr DP, entries DP[i, j]
// Store base values 0. Not necessary if DP initialised as zero array
for i from 0 to n
	DP[i, 0] <- 0
for j from 1 to m
	DP[0, j] <- 0

for i from 1 to n
	for j from 1 to m
		if s_i > j then
			return DP[i-1, j]
		else
			DP[i, j] <- max{DP[i-1, j] , v_i + DP[i-1, j-s_i]}

print DP[n, m]
```

## Further questions
- Is there some value $v_i$ and $s_i$ that the greedy algo does not yield an optimal solution?
- In the original problem formulation, every item is either chosen or not. What if you allow fractional choices?
- What if you allow an item to be chosen multiple times? How should the recurrence be changed?
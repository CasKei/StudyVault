---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Problem
You work in a company selling steel rods.
- Different lengths fetch different prices
- Lengths (inches) assumed to be integers.

You are given a rod of length $n$ inches, and prices in dollars, for rods of different lengths.

| Length $i$ | Price $p_i$ |
| ---------- | ----------- |
| 1          | 1           |
| 2          | 5           |
| 3          | 8           |
| 4          | 9           |
| 5          | 10          |
| 6          | 17          |
| 7          | 17          |
| 8          | 20          |
| 9          | 24          |
| 10         | 30          |

**Goal**: determine the *maximum revenue obtainable* by cutting up the rod and selling the pieces.
It is possible that an optimal solution requires no cutting.

## Thought process
> Subproblem: Find max revenue for a rod of length $k$.

Introduce notation:
Let $DP[k] :=$ maximum revenue obtainable for rod of length $k$.

Precise sub-problem: Compute $DP[k]$ for $0 \leq k \leq n$
Precise problem: Compute $DP[n]$.

## Why [[Dynamic Programming (DP)|DP]]
![[Dynamic Programming (DP)#When to use DP|DP]]
- $DP[n]$ can be computed using the values of $DP[k]$ for $k < n$.
- As we consider $DP[k]$ for larger and larger values of $k$, we still need $DP[k']$ for smaller values $k' < k$, again and again.

## Base Case
$$DP[0] = 0$$

## Recurrence relation
$$
DP[k] = \max{\set{p_i + DP[k-i], \hspace{1em} 1 \leq i \leq k}} \hspace{2em} \forall k \geq 1
$$
Justification:\
Suppose we cut a rod of length $k$ optimally to get the max possible revenue $DP[k]$.\
Then, among the pieces, either there is a rod of length $i$, or there isn't.

If there is a rod of length $i$, then it contributes $p_i$ to the revenue, and obtainable revenue is $p_i + DP[k-i]$.

As we consider all possible $1 \leq i \leq k$, there will always be some $i$ such that our optimal cutting has a rod of length $i$.

## Top-down Solution
[[Top-down Dynamic Programming]]
[[Memoization VS Tabulation|memoization]]
```php
Initialise memo = {}//

function DP(k):
	if k in memo then//
		return memo[k]//
	if k = 0 then
		memo[k] <- 0//
		return 0
	else
		m <- max{p_i + DP(k-i) :1 <= i <= k}
		memo[k] <- m//
		return m

run DP(n)
```
list comprehension in python:
`m = max([p_i + DP(k-i) for i in range(1, k+1)])`
`p_i` may be `p(i)` or `p[i]` depending on implementation.

## Bottom-up Solution
[[Bottom-up Dynamic Programming]]
[[Memoization VS Tabulation|tabulation]]
```php
initialise array DP[0...n]
DP[0] <- 0
for k from 1 to n:
	DP[k] <- max{p_i + DP(k-i) :1 <= i <= k}

print DP[n]
```
```python
DP = [0 for i in range(n+1)]
for k in range(1, n+1):
	DP[k] = max([p_i + DP[k-i] for i in range(1, k+1)])
	
print(DP[n])
```

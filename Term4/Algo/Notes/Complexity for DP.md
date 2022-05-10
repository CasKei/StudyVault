---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Precursors
Every sub-problem is solved at most once, and any solution found is stored in the memory.

[[Bottom-up Dynamic Programming]]
Every subproblem solved exactly once

[[Top-down Dynamic Programming]]
It is possible that some sub-problems may not need to be solved


## Method to find time complexity for DP
Suppose there are $N$ sub-problems, such that the $i^{th}$ subproblem takes $f(i)$ steps to solve.
Assume that when solving each sub-problem, all "dependent" sub-problems have already been solved, so that accessing each "dependent" sub-problem takes 1 step.

Then, time complexity to solve the problem is
$$O\left(\sum^{N}_{i=1}f(i)\right)$$
If every sub-problem is solved exactly once (e.g. in bottom up)
then time complexity is exactly
$$
\Theta\left(\sum^{N}_{i=1}f(i)\right)
$$
## Method to find space complexity for DP
Space complexity is at most
$$
O\left(
\text{ no. of sub-problems }
+
\text{ no. of other auxiliary values to be stored }
\right)
$$
If every sub-problem is solved exactly once (e.g. in bottom up)
then space complexity is exactly
$$
\Theta\left(
\text{ no. of sub-problems }
+
\text{ no. of other auxiliary values to be stored }
\right)
$$

---
aliases:
tags: #50.004
---
[[Algo]]
[[Algo week 2]]
[[L02.02 - Master Theorem, Divide and Conquer, Peak Finding]]

## Peak Finding Problem (PFP): 1D array
---
Consider an array `A[1...n]`:
An element `A[i]` is a peak if it is geq all its neighbours.
Problem: find any peak.
Note: no matter what the array is, a peak always exists
***
### Algo 1
- Scan array from left to right
- Compare each `A[i]` with its neighbours
- Exit when peak found

Complexity
- Might need to scan all elements, so $$T(n) = \Theta(n)$$

### Algo 2
- Get middle element and compare it with neighbours
	- If left side larger, search for a peak among left section
	- else if right side larger, search for a peak among right section
	- else middle is peak

Complexity
- Recursion + time to compare middle with 2 meighbours
$$\begin{align}T(n) &= T(n/2) + O(1)\\&=O(\log{n})\end{align}$$

## Peak Finding Problem (PFP): 2D array
***
Consider a 2D array: `A[[1...n], [1...n]]`
Element `A[i]` is a 2D peak if it is geq its neighbours
Problem: find any peak
***
### Algo 1
Brute force:
- for each element, use `if` statements to compare the values in the square with its neighborus to see if it is a peak.

Complexity:
$$T(n) = \Theta(n^2)$$
### Algo 2
- For each column `j`, find global maximum `B[j]`
- Use 1D peak finder to find a peak of `B[1...n]`

Complexity:
- Find biggest value in an array: $\Theta(n)$
- Find biggest value in $n$ arrays: $\Theta(n^2)$
- 1D peak finding to find peak in the array of the biggest values of each column: $\lg{n}$
- Total: $\Theta(n^2) + \Theta(\lg{n})$
$$T(n) = \Theta(n^2)$$
Proof of correctness (informal)
- Vertically largest
- Horizontally largest

### Algo 3
- Pick middle column `j = n / 2`
- Find global maximum on column `j`, at `[i, j]`
- Compare `A[i, n/2]` to `A[i, n/2 - ]` and `A[i, n/2 + 1]`
	- if `A[i, n/2]` < `A[i, n/2 - 1]`
		- pick left columns `j=[1...n/2]`
	- else if `A[i, n/2]` < `A[i, n/2 + 1]`
		- pick right columns `j=[n/2 ...n]`
	- else `A[i, j]` >= `A[i, n/2 - 1]` and `A[i, n/2]` >= `A[i, n/2 + 1]`
		- `A[i, j]` is a 2D peak

You can solve the problem with half the number of columns recursively
When you have a single column, pick the maximum and you have found a 2D peak

Complexity:
$\Theta(m)$: Cost of finding the maximum $m$ number of columns
$$
\begin{align}
T(n) &= T(m/2) + \Theta(n)\\
&=T(m/4) + cn + cn\\
&=\dots\\
&=cn\log{m}\\
&=\Theta(n\log{n})
\end{align}
$$
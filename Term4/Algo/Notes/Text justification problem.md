---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Problem
> Given a paragraph of words, adjust the spacing between words such that every line is fully left and right justified.

![[Pasted image 20220506164901.png]]

**Intuition**: we do not want spaces that are too wide.

How to decide on a mathematical criterion to evaluate whether a solution is good or bad?
- Extra spaces in each line should be equally distributed
- A few long spaces should be "penalized" more than many short spaces

## Cost function
Define the cost of each solution to be 
$$cost = \sum_{\text{all lines}}(\text{number of extra space characters in line})^2$$
Unnecessary extra space characters would increase the cost, so we should try to minimise the cost.

Minimising cost also means the extra space characters are distributed more evenly among the lines.

## Sub-problems
**Problem**: Given text, minimise cost.
**Intuition**: Subproblem should solve part of the problem.
**Idea**: Given text, split into 2 lines so that the cost for the first line is minimized and justified with correct width.

Essentially, we are deciding where to end the first line, i.e. deciding where to end first line.
We solve this, can iteratively decide which word to end each line.

**Observations**:
- Given text is a sequence of $n$ words of different lengths.
- Each line must have a fixed width (number of characters), say $w$.

**New Idea 1**
Let $\text{length}(i,j)$ be the number of characters needed to write word $i$ to word $j-1$.
Indexing of words starts from 1 and ends with $n$.

Using $\text{length}(i,j)$, define a function $\text{lineCost}(i,j)$ to be the number of extra space characters needed to fit word $i$ to word $j-1$ into a single line with the given width $w$.
$$
\text{lineCost}(i,j) =
\begin{align}
\begin{cases}
\infty &\text{if length}(i,j)>w\\
\left(w-\text{length}(i,j)\right)^2 &\text{otherwise}
\end{cases}
\end{align}
$$
## Recurrence
**Original problem**
Assuming given text has $n$ words,
Let $DP[i] = \text{min cost for text from word }i\text{ to the last word}$

Base case:
$DP[n+1] = 0$

$$DP[i] = \min\{\text{lineCost}(i,j) + DP[j] \} \hspace{2em} j \in \{i+1, \dots, n+1\}$$
Precise sub-problems: Compute $DP[i]$ for $i=n+1, n, \dots, 1$.

Original problem: Compute $DP[1]$.

- Compute $DP[1]$ has optimal substructure and overlapping sub-problems.

## Bottom-up
[[Bottom-up Dynamic Programming]]
```php
Initialise array DP[1...n+1]
DP[n+1] <- 0
for i from n downto 0:
	DP[i] <- min(lineCost(i,j) + DP[j] : for j from i+1 to n+1)
return DP[1]
```

**Order for solving sub-problems**
$n+1$ down to $1$.
- The graph for dependency for solving sub-problems is a [[Directed acyclic graph (DAG)|DAG]]
- To find order of sub-problems to solve, use [[Topological sort]] on [[Directed acyclic graph (DAG)|DAG]]. 

![[Pasted image 20220506190535.png]]

## Top-down
[[Top-down Dynamic Programming]]

```php
Initialise memo = {}
function DP(i)
	if i in memo then
		return memo[i]
	if i = n+1 then
		memo[n+1] <- 0
		return memo[n]
	else
		m <- min{lineCost(i,j) + DP(j) : for j from i+1 to n+1}
		memo[i] <- m
		return m

Run DP(1)
```

## Complexity
There are $n+1$ sub-problems.
Each $i^{th}$ subproblem requires:
- Accessing solutions to $(n+1-i)$ sub-problems
- Accessing $\text{lineCost}(i,*)$ for $(n+1-i)$ different $*$ input values.
- 1 step for accessing each sub-problem solution or $\text{lineCost}$ value
- 1 step to add sub-problem solution and $\text{lineCost}$ value 

Solving the $i^{th}$ sub-problem takes $3(n+1-i)$ steps.

Time complexity
$$
\Theta \left(
\sum^n_{i=1} 3(n+1-i)
\right) = 
\Theta \left(
\dfrac{3}{2}\left(n^2 + n \right)
\right) = 
\Theta \left(n^2 \right)
$$

For top-down, every sub-problem is solved exactly once, so the time complexity is also the same.

## Complexity for computing lineCost
So far we have assumed that we can access the values of $lineCost(i,j)$, whihc have been computed beforehand.

What if we do not know these values, and we are only given the lengths (number of characters) of all $n$ words?
$$
\text{lineCost}(i,j) =
\begin{align}
\begin{cases}
\infty &\text{if length}(i,j)>w\\
\left(w-\text{length}(i,j)\right)^2 &\text{otherwise}
\end{cases}
\end{align}
$$
Suppose $L$ is an array where $L[i]$ is the length of the $i^{th}$ word.
$\text{length}(i,i+1) = L(i)$.

![[Pasted image 20220506193958.png]]

## Space complexity
![[Pasted image 20220506194520.png]]

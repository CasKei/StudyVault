---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Problem
Given $n$ matrices $M_1 , \dots , M_n$ such that the product of matrices $M_1\cdots M_n$ is well defined, determine the minimum number of scalar multiplications needed to compute $M_1\cdots M_n$.

Recall:
Given 2 matrices $A=[A_{i,j}]_{p\times q}$ and $B = [B_{i,j}]_{q\times r}$, the total number of scalar multiplications required to compute the product $AB$ is exactly $pqr$.

Observe:
To compute a matrix product $ABC$, we could either compute $(AB)C$ or $A(BC)$.
Both gives same answer, but the number of scalar multiplications required may be different.

A choice of parenthesization of a product of $\geq 3$ matrices would determine the exact steps needed to compute the product.

![[Pasted image 20220506200439.png]]

## Thought process for parenthesization
Every matrix product with parenthesization has some corresponding number of scalar multiplications needed for computing the product.

Let this number be the cost.
For all $1 \leq i \leq j \leq n$,
$$
c[i,j] = \text{minimun cost for multiplying }M_iM_{i+1}\cdots M_j,
$$
taken over all possible parenthesizations of $M_iM_{i+1}\cdots M_j$.

Note:
For the matrix product $M_1\cdots M_n$ to be well defined, there must be positive integers $p_0$, $p_1$, $\dots$, $p_n$, such that each matrix $M_k$ has size $p_{k-1} \times p_k$.

$c[i,i]=0$ and $c[i,i+1] = p_{i-1}p_{i}p_{i+1}$.

Problem: 
Compute $c[i,n]$

Sub-problem:
Compute $c[i,j]$ for all $1 \leq i \leq j \leq n$.

## Finding a Recurrence
The two outermost parentheses (and accompanying parentheses) would determine the final matrix multiplication.

E.g.
- $M_1(M_2M_3)(M_4((M_5M_6)M_7))$
- $(M_1\cdots M_k)(M_{k+1}\cdots M_n)$
	- Cost for final matrix multiplication: $p_0p_kp_n$.

For $j \geq i+1$,
$$
\begin{align}
c[i,j] &= \min\{c[i,k] + c[k+1,j] + \text{ cost for } (M_i\cdots M_k)(M_{k+1}\cdots M_j) \}\\
&= \min\{c[i,k] + c[k+1,j] + p_{i-1}p_kp_j \}
\end{align}
$$
where here we minimise over all possible $k\in \{ i, i+1, \dots, j-1 \}$.

Intuition:
If the final matrix multiplication for computing $M_i\cdots M_j$ is $(M_1\cdots M_k)(M_{k+1}\cdots M_j)$, then its min cost is the min cost for $M_i\cdots M_k$ plus min cost for $M_{k+1}\cdots M_j$ plus cost for final matrix multiplication.

Sub-problems:
Compute $c[i,j]$ for all $1 \leq i \leq j \leq n$.
- Optimal substructure, overlapping subproblems.

Main problem:
Compute $c[1,n]$

## Bottom-up
[[Bottom-up Dynamic Programming]]
```php
Initialise 2 dim array c, with entries c[i,j] for 1<=i , j<=n
for i from 1 to n
	c[i,i] <- 0
for i from n-1 to 1
	for j from i+1 to n
		c[i,j] <- min{c[i,k] + c[k+1,j] + p(i-1)p(k)p(j) : for k from i to j-1}
return c[1,n]
```

## Top-down
[[Top-down Dynamic Programming]]
```php
Initialise memo = {}
function c(i,j)
	if (i,j) in memo then
		return memo[(i,j)]
	if i=j then
		memo[(i,j)] <- 0
		return 0
	else
		m <- min{c(i,k) + c(k+1,j) + p(i-1)p(k)p(j) : for k from i to j-1}
		memo[(i,j)] <- m
		return m

run c(1,n)
```

## Complexity for parenthesization problem
Computing $c[i,j]$ takes $6(j-i)$ steps
- $(j-1)$ possible values for $k$
- For each $k$,
	- 1 step to access $c[i,k]$
	- 1 step to access $c[k+1,j]$
	- 2 steps to compute $p_{i-1}p_kp_j$
	- 2 steps for the 2 additions

All subproblems must be solved so
$$
\Theta\left(\sum^{n}_{j=2}\sum^{j-1}_{i=1} 6(j-i)\right) = \Theta\left(n^3\right)
$$

Or by visualisation:

Visualising $c$ as a $n\times n$ table, tabulate.
![[Pasted image 20220506225625.png]]
$$
\begin{align}
\text{Num. of steps} &= \Theta\left(\sum^{n-1}_{t=1}3(t+1)t \right)= \Theta\left(\sum^{n-1}_{t=1}3t^2 \right) + \Theta\left(\sum^{n-1}_{t=1}3t \right)\\
&= \Theta\left(\dfrac{(n-1)(n)(2n-1)}{2} + \dfrac{3}{2}(n-1)n\right)\\
&= \Theta\left(n^3 \right)
\end{align}
$$
Time complexity is $\Theta(n^3)$.

## Space Complexity
We need to store the solutions of all sub-problems, which are indexed by $[i,j]$ for $1 \leq i \leq j \leq n$.
There are a total of $\sum^{n}_{j} (j-1) = \dfrac{n(n-1)}{2}$ subproblems.
Thus space complexity is
$$
\Theta\left(\dfrac{n(n-1)}{2}\right) = \Theta\left(n^2\right)
$$
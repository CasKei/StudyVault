---
aliases: LCS
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Common subsequence
Let $X$ represent a sequence $x_1$, $x_2$, $\dots$, $x_n$ with $n$ elements.

> **Subsequence**
> of $X$ is a sequence $x_{i_1}$, $x_{i_2}$, $\dots$, $x_{i_{k}}$, such that $1 \leq i_1 < i_2 < \cdots < i_k \leq n$.
> - Elements of a subsequence must be the elements of the original sequence, in the same relative order.

> **Common subsequence**
> Given sequences $X=(x_1, \dots ,x_m)$ and $Y=(y_1,\dots ,y_n)$,
> $Z=(z_1 , \dots , z_k)$ is a **common subsequence** of $X$ and $Y$ if $Z$ is a **subsequence** of both $X$ and $Y$.

## Problem
>Given sequences $X=(x_1, \dots ,x_m)$ and $Y=(y_1,\dots ,y_n)$,
find a **common subsequence** of *maximum length* among all subsequences.

### Why is this problem important
Data/file copmarison
- Key step in comparison of 2 given files or datasets (treated as sequences).
- Used as key process of file synchronisation and back-up
	- Intuition: if there are only minor differences, synchronisation should only update those minor difference, and not the entire file.

Bioinformatic
- Key step in the alignment and comparison of DNA sequences or genome data
- Used especialy to detect differences in genetic markers.
	- Important for disease discovery, detection of genetic abnormalities

## Thought process
Consider sequences $X=(x_1, \dots ,x_m)$ and $Y=(y_1,\dots ,y_n)$.
Suppose $Z=(z_1 , \dots , z_k)$ is an LCS of $X$ and $Y$.

Let $X_t$ denote the subsequence $(x_1, \dots ,x_t)$.

Note that at least one of 3 cases must hold:
1. $x_m = y_n$
2. $x_m \not = y_n$ and $z_k \not = x_m$
3. $x_m = y_n$ and $z_k \not = y_n$

Either $x_m = y_n$ or not.
If not, $z_k$ can only equal to either one.
Cases 2 and 3 are not mutually exclusive. It is possible that $x_m \not = y_n$, $z_k \not = x_m$ and $z_k \not = y_n$.

### Case 1
$$
x_m = y_n \implies z_k = x_m = y_n
$$
Proof by contradiction:
If instead $z_k \not = x_m$, then we can append $Z$ by $x_m$ to get a common subsequence of $X$ and $Y$ with length $k+1$, which contradicts our condition that $Z$ is an LCS or $X$ and $Y$.
Hence, $z_k = x_m = y_n$.

$$
Z_{k-1} \text{ must be LCS of } X_{m-1} \text{ and } Y_{n-1}
$$
From above, we know htat $Z_{k-1}$ is a common subsequence of $X_{m-1}$ and $Y_{n-1}$.
If instead $Z_{k-1}$ is not an LCS of $X_{m-1}$ and $Y_{n-1}$, then it does not have a maximum length among all common subsequences of $X_{m-1}$ and $Y_{n-1}$, so there must be some LCS $Z'$ of $X_{m-1}$ and $Y_{n-1}$ with length $\geq k$.
Then we can append $Z'$ by $x_m$ to get a common subsequence of $X$ and $Y$ with length $\geq k+1$. This contradicts with our condition that the common subsequence $Z$ with length $k$ has maximum length.
Hence $Z_{k-1} \text{ must be LCS of } X_{m-1} \text{ and } Y_{n-1}$.

Conclusion
If $x_m = y_n$, then $z_k = x_m = y_n$
and $Z_{k-1} \text{ is a LCS of } X_{m-1} \text{ and } Y_{n-1}$.

### Case 2
$$
Z \text{ must be an LCS of } X_{m-1} \text{ and } Y
$$
Since $z_k \not = x_m$, we know that $Z$ is a common subsequence of $X_{m-1}$ and $Y$.
If instead $𝑍$ is not an LCS of $𝑋_{𝑚−1}$ and $𝑌$, then $𝑍$ doesn’t have maximum length among all common subsequences of $𝑋_{𝑚−1}$ and $𝑌$, so there must be some LCS $𝑍'$ of $𝑋_{𝑚−1}$ and $𝑌$ with length $\geq 𝑘 + 1$.
But then $𝑍'$ is a common subsequence of $𝑋$ and $𝑌$ with length $\geq 𝑘 + 1$. This contradicts our condition that the common subsequence $𝑍$ with length $𝑘$ has maximum length. Conclusion: $𝑍$ is an LCS of $𝑋_{𝑚−1}$ and $𝑌$.

Conclusion
$$
\text{If } x_m \not = y_n\text{ and } z_k \not = x_m \text{ , then } Z \text{ is an LCS of } X_{m-1} \text{ and } Y
$$

### Case 3
$$
\text{If } x_m \not = y_n\text{ and } z_k \not = y_n \text{ , then } Z \text{ is an LCS of } X \text{ and } Y_{n-1}
$$

### Problem
Find an LCS of $X_m$ and $Y_n$.
### Sub-problem
Find an LCS of $X_i$ and $Y_j$ for all $1 \leq i \leq m$ , $1\leq j \leq n$.
- Optimal substructure and overlapping sub-problems.

![[Pasted image 20220507202919.png]]

## Recurrence
Our 3 observations:
$$
\begin{align}
&x_m = y_n \implies z_k = x_m = y_n \text{ and } Z_{k-1} \text{ is a LCS of } X_{m-1} \text{ and } Y_{n-1}\\
&\text{If } x_m \not = y_n\text{ and } z_k \not = x_m \text{ , then } Z \text{ is an LCS of } X_{m-1} \text{ and } Y\\
&\text{If } x_m \not = y_n\text{ and } z_k \not = y_n \text{ , then } Z \text{ is an LCS of } X \text{ and } Y_{n-1}
\end{align}
$$
Let $DP[i,j]$ denote any LCS of $X_i$ and $Y_j$.
$$
\begin{align}
DP[i,j] =
\begin{cases}
DP[i-1,j-1].append(x_i) &x_i=y_j\\
max\{ DP[i-1,j] , DP[i,j-1] \}
\end{cases}
\end{align}
$$

## Recursive solution
```php
function DP(i,j)
	if i=0 or j=0 then
		return (empty sequence)
	if x(i) = y(j) then
		return DP(i-1, j-1).append(x(i))
	else
		if DP(i-1,j).length >= DP(i,j-1).length then
			return DP(i-1,j)
		else
			return DP(i,j-1)
run DP(m,n)
```

## Top-down
[[Top-down Dynamic Programming]]
```php
Initialise memo ={}
function DP(i,j)
	if (i,j) in memo then
		return memo[(i,j)]
	if i=0 or j=0 then
		memo[(i,j)] <- (empty sequence)
		return (empty sequence)
	if x(i) = y(j) then
		memo[(i,j)] <- DP(i-1, j-1).append(x(i))
		return memo[(i,j)]
	else
		if DP(i-1,j).length >= DP(i,j-1).length then
			memo[(i,j)] <- DP(i-1,j)
			return DP(i-1,j)
		else
			memo[(i,j)] <- DP(i,j-1)
			return DP(i,j-1)
run DP(m,n)
```

## Bottom-up
[[Bottom-up Dynamic Programming]]
```php
Initialise 2 dim array DP[i,j] , 0<=i<=m, 0<=j<=n
for i from 0 to m
	DP[i,0] <- (empty sequence)
for j from 0 to n
	DP[0,j] <- (empty sequence)
for i from 1 to m
	for j from 1 to n
		if x(i) = y(i) then
			DP[i,j] <- DP[i-1,j-1].append(x(i))
		else
			if DP[i-1,j].length >= DP[i,j-1].length then
				DP[i,j] <- DP[i-1,j]
			else
				DP[i,j] <- DP[i,j-1]
return DP[m,n]
```


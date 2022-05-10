---
tags: 50.004
---
# Cassie Chong 1005301 50.004 Pset2 CL01
![[Pasted image 20220408213843.png]]

## 1)
![[Pasted image 20220408213932.png]]
$n$ blocks, each with points, first block 0.
From question, we see blocks of lesser points will disappear, so it seems that we must jump for strictly increasing blocks only.
To maximise points, since all points are a positive integer, we need to find ==a sequence in the array where points keep increasing, and sum of points must be maximised==.
### i)
Find a recurrence for this problem. Specify the base cases for your recurrence. [3 points]
***
Let $J[1...i]$ be an array that keeps the maximum points that can be attained by jumping to blocks $1$ to $i$, where $1 \leq i \leq n$. 
If there are 0 blocks, sum is 0. $J[0] = \emptyset$. But then there's no game to play. Assume always at least 1 block?
If there is 1 block, sum is 0 (first block always 0). $J[1] = \set{A[1]}$

Consider maximum sum of smaller values already computed, pick maximum $J[j]$ and add current element $A[i]$ to it.

Score = sum of previously jumped blocks + target block.
For entry in jumped array $J[i]$ where $J[i]$ is max sum of points to jump to block $i$,
for all $1 < j \leq i \leq n$,
$$
\begin{align}
J[1] &= A[1]\\
J[i] &=
\begin{cases}
A[i] &,\not\exists \ j < i, &A[j] < A[i]\\
J[j] + A[i] &, \exists \ j < i, &A[j] < A[i]
\end{cases}
\end{align}
$$
where $j$ is a block before block $i$ that has been jumped on before reaching $i$.
### ii)
Design an algorithm to solve the problem with dynamic programming. Please give your algorithm in pseudocode. [5 points]
***
Remember each sums and update as we go along. Tabulate, ==bottom-up==.
Assume game has at least 1 block. (otherwise what's the game?)
```php
function maxPoints(A)
	'''
	Require: A[1...n] is an array of game points of n blocks
	Require: A[1] = 0
	Require: copying an array can be done with .copy, otherwise use a for loop to iterate through each item. Note: changing copy must not change original.
	'''
	// base case
	if A.length == 1 then return 0

	// create array J to store max sum of jumped blocks up till A[i]
	J = A.copy // start with memo being copy of A which is points of each block

	// for points in blocks, for previously jumped in each block
	for i from 1 to n
		for j from 1 to i
			// implement recurrence relation
			if (A[j] < A[i])
				if (J[j] + A[i] > J[i])
					J[i] <- J[j] + A[i]
	// now J has max points for game jumped up till each block
	return max(J) // this will be max possible points in this game
```

### iii)
Analyze the time and space complexities of your algorithm. [2 points]
***
Base case check: $O(1)$ time, $O(1)$ space.
Creating an array of size $n$ that consisted of points of $A$: $O(n)$ time, $O(n)$ space.
For every block in $A$: $O(n)$ time
For every jumped block in the past of each block in $A$: $O(n)$
$\therefore$ updating all entries of memo to be max sum of jumps up till each block: $O(n^2)$ time.
Finding maximum in $J$ array: searching in array: $O(n)$ time.

Overall: time $O(n^2)$, space $O(n)$.

## 2) Variant Knapsack Problem
![[Pasted image 20220408214116.png]]
Max capacity $m$. Pack from $n$ items. Size $s_i$ and value $v_i$ are positive numbers for each item $i$. Items selected cannot exceed $t_{\text{total}}$.
Difference from knapsack is we now have a limit of number of items.
Substructure: each item is in or not in.
One more condition than original, 3 dimensions?
### i)
Find a recurrence for this problem. Specify the base cases for your recurrence. [3 points]
***
Let $DP[i,j,k] =$ max value for "choose from items 1 to $i$, total size $\leq j$, for number of items $\leq k$". 
We want to solve $DP[n,m,t_{\text{total}}]$.
- If size of $i$ exceeds $j$, can't pack
- If number of packed items exceeds $k$, can't pack
- Otherwise:
	- If choice of items with max value for capacity $j$ includes item $i$, then the subset of items without item $i$ would have max value for capacity $j-s_i$.
	- If choice of items with max value for capacity $j$ does not include $i$, then this max value equals $DP[i-1,j,k]$ by definition
Base cases: $DP[i,j,k] = 0$ when at least any one of $i,j$ or $k$ is 0.
Recurrence:
For all $1 \leq i \leq n$, $1 \leq j \leq m$, and $1 \leq k \leq t_{\text{total}}$,
$$
\begin{align}
DP[i,j,k] = 
\begin{cases}
DP[i-1, j, k] &, s_i > j \text{ and/or } k > t_{\text{total}}\\
\max{(DP[i-1,j,k] , v_i + DP[i-1, j-s_i, k-1])} &, s_i \leq j \text{ and } k \leq t_{\text{total}}
\end{cases}
\end{align}
$$

### ii)
Design an algorithm to solve the problem with dynamic programming. Please give your algorithm in pseudocode. [5 points]
***
==Bottom-up==, make 3D array
Use $DP[i][j][k]$ notation to denote $DP[i,j,k]$, unlike in class, to split and see better.
```php
Initialise 3-D array DP, with all entries 0. Size is n*m*t_total.

for i from 1 to n
	for j from 1 to m
		for k from 1 to t_total
			if s_i > j or k > t_total
				return DP[i-1][j][k]
			else
				DP[i][j][k] <-
					max(
					DP[i-1][j][k],
					v_i + DP[i-1][j-s_i][k-1]
					)
print DP[n,m,t_total]
```

### iii)
Analyze the time and space complexities of your algorithm. [2 points]
***
A 3D array of size $n\cdot m \cdot t_{\text{total}}$ is created. Space complexity = $\Theta(n\cdot m \cdot t_{\text{total}})$.
Initialising such an array may take time complexity $O(n\cdot m \cdot t_{\text{total}})$.
Then we do nested loop across every entry of this 3D array, at most a scalar multiple of its number of entries in order to access answers to sub-problems. So time complexity is also $O(n\cdot m \cdot t_{\text{total}})$.
Obtaining the entry for the answer takes $O(1)$ as this is array query using indexing.

Overall: space $\Theta(n\cdot m \cdot t_{\text{total}})$, time $O(n\cdot m \cdot t_{\text{total}})$.

## 3)
![[Pasted image 20220408214235.png]]
$A[1\dots n]$, where $A[i]$ is price of 1 BTC on $i^{th}$ day.
$T[1\dots n]$, where $T[i]$ is transaction fee of $i^{th}$ day.
$0 < T[i] < A[i] \ \ \forall \  1 \leq i \leq n$.
Each day: either 0 or 1 transaction.
Transaction = either buy 1 or sell any integer of BC
Wha?? Buying no transaction fee?? Ok then.

### i)
Find a recurrence for this problem. Specify the base cases for your recurrence. [3 points]
***
Let maximum profit earned from day 1 to day $i$ be $P[i]$.
Let number of BTC in possession be $b$.

For every day $i$, I can choose to do 3 things:
- Buy 1 BTC: profit $-A[i]$
- Sell $k$ BTC where $1 \leq k \leq b$: profit $+ k\cdot A[i] - T[i]$
- Do nothing: profit = profit of previous day

If $b=0$, it is impossible to sell. Then we take the maximum of buying or doing nothing.
Otherwise when $b>0$, do maximum of all 3 options.

Base case when $i > n$, when no actions are possible, so return 0.

For $1 < i \leq n$ and $1 \leq k \leq b \leq n-1$,
$$
P[i] =
\begin{align}
\begin{cases}
\max{(P[i-1], P[i-1] - A[i])} &, b=0\\
\max{(P[i-1], P[i-1] - A[i]) , P[i-1] + k\cdot A[i] - T[i] )} &, b>0
\end{cases}
\end{align}
$$


### ii)
Design an algorithm to solve the problem with dynamic programming. Please give your  algorithm in pseudocode. [5 points]
***
```php
max_p <- 0 // max profit variable
Initialise memo <- {}
function BTC(A, T, i, b, p)
	'''
	Require: 0 < T[i] < A[i], A[1..n] and T[1..n] are integer arrays
	Require: i, b, p are integers
	'''
	if i in memo
		return memo[i]
	// base case
	if i > n
		memo[i] <- 0
		return max(memo)
	else
		// cannot sell
		if b == 0
			p <- max(BTC(A, T, i+1, b+1, p-A[i]) , BTC(A, T, i+1, b, p))
			max_p <- max(max_p , p)
			
		// can sell
		else
			for k from 1 to b
				p <- max(BTC(A, T, i+1, b+1, p-A[i]) , BTC(A, T, i+1, b, p))
				if i != 1 and A[i] > A[i-1]
					p <- max(p, BTC(A, T, i+1, b-k, p+k*A[i]-T[i]))
					max_p <- max(max_p , p)
			memo[i] <- max_p
	return max(memo)
```

### iii)
Analyze the time and space complexities of your algorithm. [2 points]
***
There is are subproblems for each day, for each bitcoin owned. All sub-problems must be solved.
Solving the $i^{th}$ subproblem, function is called at most $k$ times, at most $n-1$ times. This is $O(n)$.
We solve these subproblems for each day, so time complexity $O(n^2)$.
Memo keeps data for $n$ days, so space complexity is $O(n)$.

## 4)
![[Pasted image 20220408214435.png]]
![[Pasted image 20220408214448.png]]
Find minimum trials to guarantee if $F_{min} \leq N$ and actual $\lceil F_{min} \rceil$.
### i)
Find a recurrence for this problem. Specify the base cases for your recurrence. [3 points]
***
Solution depends on past trialled values of machine force.
Set of values of force that machine can give: $F \in \set{1, \dots, N}$
Let $T[i][j]$ denote number of trials needed to reach a conclusion on the set $f \in \set{i, \dots, j}$.
Original problem is then to solve $T[1][N]$.
We have $1 \leq i \leq j \leq N$.

Base case
$i = j \implies f \in \emptyset \implies T[i][j] = 0$

For some subsolution $T[i][j]$ for $1 \leq i \leq j \leq N$,
$T[i][j]$ can be computed from subsets of $f$, from $\set{i, \dots, k}$ to $\set{k+1, \dots, j}$, where if the block moves, we should use the lower set to decrease force, and if the block does not, we should use the upper set for more force.
So $T[i][j]$ depends on $T[i][k]$ or $T[k+1][j]$.
To be sure we get the answer we consider the worst-case subset, so we check $\max{(T[i][k] , T[k+1][j])}$ for all $i < k < j$.

Then we have to minimise over all $k$ cases as we want the minimum number of trials.
$$
\begin{align}
T[i][j] = \min \{
\max \{
T[i][k] , T[k+1][j]
\}
+ 1
&, \forall i < k < j
\}
\end{align}
$$

### ii)
Design an algorithm to solve the problem with dynamic programming. Please give your  algorithm in pseudocode. [5 points]
***
```php
Initialise memo <- {}
function T(i, j)
	if (i, j) in memo
		return memo[(i, j)]
	// base
	if i == j
		memo[(i, j)] <- 1
		return 1 // only 1 trial needed to finish testing, since set is empty

	else
		trials <- min(max(T(i, k) , T(k+1, j)) + 1 for k from i to j-1)
		memo[(i, j)] <- trials
		return memo[(i, j)]

run function T(1, N)
```

### iii)
Analyze the time and space complexities of your algorithm. [2 points]
***
We solve problem $(1,3)$ with number of subproblems:
$(1,3)$ : 1
$(1,2), (2,3)$ : 2
$(1,1), (2,2), (3,3)$ : 3

So for problem $(1,N)$ we have 
$$
\sum^{N}_{i = 1} i = 1 + 2 + \cdots + n = \frac{n(n+1)}{2}
$$
subproblems.

Each subproblem is solved once using a trivial base case and stored in a memo, which size is also the number of subproblems.

So time and space complexity is both
$$
O\left(\frac{n(n+1)}{2}\right) = O(n^2)
$$

## 5)
![[Pasted image 20220408214523.png]]
### i)
Find a recurrence for this problem. Specify the base cases for your recurrence. [3 points]
***
We have length of input strings $s_1$ and $s_2$ being $n$.
Let number of swaps needed from letter at index 1 to $i$ be $S_i$, where $1 \leq i \leq n$.
Base case:
when $s_1 = s_2 \implies done$ 
or $i = n \implies \text{not possible as }i = n+1 \text{ is out of range}$.

Recurrence: either
- Don't swap $i$
- Swap $i$ with $i+1$ since as we go along the previous letters are de facto sorted.

Procedure: swap letters of $s_1$ and save its permutations in a memo, check if equal to $s_2$

### ii)
Design an algorithm to solve the problem with dynamic programming. Please give your  algorithm in pseudocode. [5 points]
***
```php
// run function starting from swaps = 0 and i = 1
Initialise memo <- {}
function stringswap(s1, s2, i, swaps)
	'''
	Require: swaps is an integer count of how many swaps are done to reach this permutation
	Require: i is an integer for 1 <= i <= n
	Require: s1 and s2 are strings of equal length n, n >= 1
	'''
	if s1 in memo
		memo[s1] <- swaps
		return s1
	//base case
	if s1 == s2 or i == s1.length
		if s1 in memo
			memo[s1] <- min(swaps, memo[s1]) 
			// ^the smaller of current swap count and memoed value
		return s1
	else
		swappedS1, swappedS2 <- s1 //1: swap like mad, 2: store original s1
		for j from i to n-1 
			if swappedS1 in memo
				swaps <- memo[swappedS1]
			swappedS1 <- stringswap(swappedS1, s2, i+1, swaps)
			if swappedS1 in memo
				memo[swappedS1] <- min(swaps, memo[swappedS1])
			if swappedS2 in memo
				swaps <- memo[swappedS2]
			swap swappedS2 index i with index i+1
			swap++
			swappedS2 <- stringswap(swappedS2, s2, i+2, swaps)
			if swappedS2 in memo
				memo[swappedS2] <- min(swaps, memo[swappedS2])
	return swappedS2

run function stringswap(s1, s2, 1, 0)
```

### iii)
Analyze the time and space complexities of your algorithm. [2 points]
***
We may end up having all permutations of $s_1$ checked before it is equal to $s_2$. Hence, we have to solve a total of subproblems equal to the number of permutations of $n$ non-distinct letters, which is
$$\frac{n!}{r_1!r_2!\dots r_k!} \text{ , for some } 1 \leq k \leq 26$$
This same amount of data is stored in the memo, requiring the same amount of space.
Voila, a horrifying time and space complexity of $O(n!)$! Welp.

## 6)
![[Pasted image 20220408214601.png]]
### i)
Among all contiguous subarrays $A[i..j](1 ≤ i ≤ j ≤ n)$ of $A$, find the largest possible sum $| ∑^j_{k=i} A[k]|$. [5]
***
Let $DP(i)$ be largest possible sum of entries of all contiguous subarrays $A[k..i]$, for $k \in \set{1, \dots, i}$.

==Base case==: $i=1 \implies$ there is only 1 array with 1 entry $A[1]$, so $DP(1) = A[1]$.

Otherwise if $DP(i-1) > 0 \implies \exists A[1...i-1] + A[i]$ that has sum of all entries larger than $A[i]$, then $\implies DP(i) = D(i-1) + A[i]$.

Otherwise, subarray $A[i]$ (from $i$ to $i$, that is only one entry) has sum $A[i]$, with contiguous subarrays $A[k..i]$, for $k \in \set{1, \dots, i}$ will hold $sum \leq A[i] \implies DP(i) = A[i]$.

So for all $1 < j \leq n$,
$$
DP(i) = \max \{ DP(i-1) + A[i] , A[i] \}
$$
Make array of length $n$ with entries all base cases. Tabulate onwards. ==Bottom up==.
```php
function largestSum(A[1...n])
	'''
	Require: A[1...n] is an integer array, n is an integer >= 1
	'''
	Initialise DP as a 1D array of length n, with all entries being A[1]

	for i from 2 to n
		if DP[i-1] > 0
			DP[i] <- DP[i-1] + A[i]
		else
			DP[i] <- A[i]

	return max(DP[1], DP[2], DP[3], ... , DP[n])
```
All problems must be solved just once (bottom up) from 1 to $n$, so time and space complexities are both $O(n)$.

### ii)
Among all contiguous subarrays $A[i..j](1 ≤ i ≤ j ≤ n)$ of $A$, find the smallest possible  non-zero product $\Pi^j_{k=i} A[k]$. Note: Here “smallest” refer to the numbers, not their magnitudes. For example, −6 is smaller than 2. [5]
***
Let $DP(i)$ be smallest possible product of entries of all contiguous subarrays $A[k..i]$, for $k \in \set{1, \dots, i}$.

==Base case==: $i=1 \implies$ there is only 1 array with 1 entry $A[1]$, so $DP(1) = A[1]$.

Otherwise if $DP(i-1) > 0 \implies \exists A[1...i-1] \cdot A[i]$ that has product of all entries larger than $A[i]$, then $\implies DP(i) = D(i-1) \cdot A[i]$.

Otherwise, subarray $A[i]$ (from $i$ to $i$, that is only one entry) has product $A[i]$, with contiguous subarrays $A[k..i]$, for $k \in \set{1, \dots, i}$ will hold $\text{product} A[i] \implies DP(i) = A[i]$.

So for all $1 < j \leq n$,
$$
DP(i) = \min \{ DP(i-1) \cdot A[i] , A[i] \}
$$
Make array of length $n$ with entries all base cases. Tabulate onwards. ==Bottom up==.

```php
function smallestProduct(A[1...n])
	'''
	Require: A[1...n] is an integer array, n is an integer >= 1
	'''
	Initialise DP as a 1D array of length n, with all entries being A[1]

	for i from 2 to n
		if DP[i-1] > 0
			DP[i] <- DP[i-1] * A[i]
		else
			DP[i] <- A[i]

	return min(DP[1], DP[2], DP[3], ... , DP[n])
```
All problems must be solved just once (bottom up) from 1 to $n$, so time and space complexities are both $O(n)$.

### iii)
A contiguous subarray $A[i..j] (\text{for } 1 ≤ i ≤ j ≤ n)$ of $A$ is said to be roller-coaster-like, if for any two consecutive entries $A[k]$, $A[k + 1]$ in $A[i..j]$, both of them are non-zero and of different signs (i.e. one is negative if and only if the other is positive), and satisfy the  inequality $|A[k]| > |A[k + 1]|$. For example, a roller-coaster-like contiguous subarray may look like $[−7, 6, −4, 3, −1]$. Find the maximum length of a roller-coaster-like contiguous subarray of $A$. [5]
***
Alt between pos (P) and neg(N), and in decreasing magnitude. Length start from 1, add 1 if fulfil criteria.
Roller-Coaster-Like Contiguous Subarray (RCLCS)

For $1 \leq  i \leq n$, let
$$
\begin{align}
PN(i) := \text{max length of RCLCS of all subarrs $A[1...i]$ ending with A[i]} &: A[i]>0, A[i-1] <0\\
NP(i) := \text{max length of RCLCS of all subarrs $A[1...i]$ ending with A[i]} &: A[i]<0, A[i-1] >0
\end{align}
$$
Base case: $i=1 \implies PN(i) = 1, NP(i) = 1$.

For $2 \leq i \leq n$,
$$
\begin{align}
PN(i) = 
\begin{cases}
PN(i-1) + 1 &\text{, } A[i]>0 , A[i-1]<0\\
PN(1)=1 &\text{, otherwise}
\end{cases}
\\
NP(i) = 
\begin{cases}
NP(i-1) + 1 &\text{, } A[i]<0 , A[i-1]>0\\
NP(1)=1 &\text{, otherwise}
\end{cases}

\end{align}
$$
Of which count is incremented if the next $i$ fulfils the criteria, if not reset to base case.
We return the maximum of the two cases for all $i$:
$$
\max\set{PN(k) , NP(k) \hspace{2em}: \forall \ 1 \leq k \leq n}
$$

Build array: ==bottom-up==
```php
function maxLofRCLCS(A)
	'''
	Require: A[1...n] is an integer array, n >= 1
	'''
	Initialise PN[1...n] and NP[1...n] with all initial entries equal to 1
	for i from 2 to n
		if (A[i] > 0) and (A[i-1] < 0)
			PN[i] <- PN[i-1] + 1
			NP[i] <- 1
		else if (A[i] < 0) and (A[i-1] > 0)
			NP[i] <- NP[i-1] + 1
			PN[i] <- 1
		else
			PN[i] <- 1
			NP[i] <- 1
	return max(PN[1], PN[2], ..., PN[n], NP[1], NP[2], ..., NP[n])
```
All problems must be solved just once (bottom up) from 1 to $n$, for both recurrence relations for a total of $2n$ times, so time and space complexities are both $O(n)$.

## 7)
You are a professional robber planning to rob houses in multiple neighborhoods. Each house has a certain amount of money stashed. The only constraint stopping you from robbing all houses in all neighborhoods is that each neighborhood has a connected security system that will automatically contact the police when certain conditions are met. However, you have done your homework, and you are aware of exactly how the security system works for each neighborhood that you plan to rob.
### i)
For the first neighborhood, there are $n$ houses are lined up along a straight street. The connected security system for this first neighborhood will automatically contact the police if any two adjacent houses are broken into. Given an array of non-negative integers $A[1..n]$, representing the amount of money in dollars that each house has, determine the maximum amount of money in dollars that you can rob without alerting the police. Design an algorithm to solve this problem with dynamic programming. Find a recurrence for this problem. Specify the base cases for your recurrence. Please give your algorithm in pseudocode. Also, analyze the time and space complexities of your algorithm. [5 points]
***
 Robbable houses alternate each other. So there are 2 paths to rob from depending on how much money each path has, even or odd houses.

Let $Rob[i]$ denote maximum amount of money in dollars that you can rob without alerting the police, for houses $1$ to $i$.

Base cases:
For $i=1$, no police will come, just rob that one house. $Rob[1] = A[1]$ which is the money in that house.\
For $i=2$, police will come if you rob both, must choose 1, so choose the max: $Rob[2]=\max\set{A[1], A[2]}$.

Otherwise we have to choose a path as mentioned earlier, skipping over one each time.
$$
\begin{align}
Rob[i] &= \max\set{\text{path with i}, \text{ path alternating over i}} \\
&= \max\set{Rob[i-2] + A[i] \ ,\ Rob[i-1]}
\end{align}
$$
```php
function howToRob1(A)
	'''
	Require: A[1...n] is integer array, n>=1
	Require: all houses will not take money from me (entries >=0)
	'''
	Initialise Rob[1...n] with all entries A[1] // base case 1
	if n >= 2 // base case 2, >= to cover recurrence
		Rob[2] <- max(A[1], A[2])
	if n >= 3
		for i from 3 to n
			Rob[i] <- max(Rob[i-2] + A[i] , Rob[i-1])
	return Rob[n]
```
All subproblems must be solved just once (bottom up) from 1 to $n$, so time and space complexities are both $O(n)$.

### ii)
For the second neighborhood, there are $n^2$ houses arranged in an $n$-by-$n$ square grid of houses. Each house has a house number $(i, j)$, where $1 ≤ i ≤ n$, $1 ≤ j ≤ n$. Based on your knowledge of the security system for this second neighborhood, you know that once you have robbed house $(i, j)$, then you cannot rob any houses $(s, t)$ satisfying $s ≥ i$, or $t ≥ j$ (or both), otherwise the police will automatically be contacted by the security system. Given a 2D array of non-negative integers $A[1..n][1..n]$, where each $A[i][j]$ represents the amount of money in dollars that house $(i, j)$ has, determine the maximum amount of money in dollars that you can rob without alerting the police. Design an algorithm to solve this problem with dynamic programming. Find a recurrence for this problem. Specify the base cases for your recurrence. Please give your algorithm in pseudocode. Also, analyze the time and space complexities of your algorithm. [10 points]
***
Robbable house after a rob are houses to the top left of the rob.

Let $Rob[i][j]$ denote maximum amount of money in dollars that you can rob without alerting the police, for houses from row $1\leq i$ and column $1\leq j$.

Base cases:
$n=1 \implies$ there is only one house. Its free real estate. $Rob[1][j] = A[1][1]$.
$n>=2$ : $i=1$ XOR $j=1 \implies$ only one robbable house: $Rob[i][j] = A[i][j]$.

For $2 \leq i \leq n$ and $2 \leq j \leq n$,
$$
\begin{align}
Rob[i][j] = A[i][j] + \max
\set{
Rob[i-a][j-b] \hspace{2em}:\forall 1 \leq a < i, 1 \leq b <j
}
\end{align}
$$
```php
function howToRob2(A)
	'''
	Require: A[1...n][1...n] is a square. Entries are positive integers.
	'''
	Initialise 2D array Rob[1..n][1..n].
	for i from 1 to n // base 1
		for j from 1 to n
			Rob[i][j] <- A[1][1]

			if n >= 2
				if (i==1 xor j==1) // base 2
					Rob[i][j] <- A[i][j]
				else
					for i from 2 to n
						for j from 2 to n
							Rob[i][j] <- A[i][j] + max(
											{A[i][j] + Rob[i-a][j-b] : forall 1 <= a < i, 1 <= b < j}
										)
	
	return Rob[n][n]
```
Space: 2D array of size $n^2 \implies$ $O(n^2)$
Time: We solved subproblem $(i,j)$ once, but each subproblem calls for a smaller subproblem, if not base case.
$$
\begin{align}
O\left(\sum^{n}_{i=2} \sum^{n}_{j=2} \sum^{i}_{a=1} \sum^{j}_{b=1} 1\right) = O\left(\frac{1}{4}(n^2 + n - 2)^2 \right) = O(n^4)
\end{align}
$$

### iii)
For the third neighborhood, there are $n^2$ houses arranged in an $n$-by-$n$ square grid of houses. Each house has a house number $(i, j)$, where $1 ≤ i ≤ n$, $1 ≤ j ≤ n$. Based on your knowledge of the security system for this third neighborhood, you know that once you have robbed house $(i, j)$, then you cannot rob any houses $(s, t)$ satisfying ($s ≥ i$ and $t ≤ j$) or ($s ≤ i$ and $t ≥ j$), otherwise the police will automatically be contacted by the security system. Given a 2D array of non-negative integers $A[1..n][1..n]$, where each $A[i][j]$ represents the amount of money in dollars that house $(i, j)$ has, determine the maximum amount of money in dollars that you can rob without alerting the police. Design an algorithm to solve this problem with dynamic programming. Find a recurrence for this problem. Specify the base cases for your recurrence. Please give your algorithm in pseudocode. Also, analyze the time and space complexities of your algorithm. [10 points]
***
Robbable houses are either at top right or bottom left quadrant. We need to have a way to make sure we don't go back to the untouchable zones, make new array everytime?

Recursion simpler here. Top-down.
Base cases:
Any one, or combination of the following: $i<0, i>n , j<0 , j>n$

For $1 \leq i \leq n$ and $1 \leq j \leq n$,
$$
\begin{align}
Rob[i][j] = \max \set{Rob[i-1][j+1] , Rob[i+1][j-1]}
\end{align}
$$
```php
Initialise memo <- {}
function howToRob3(A, i, j)
	'''
	Require: A[1..n][1..n] is positive int 2D array
	'''
	if (i,j) in memo
		return memo[(i,j)]

	if i<0 or i>n or j<0 or j>n
		return 0
	else
		topright <- splice A[1..i-1][j..n]
		bottomleft <- splice A[i..n][1..j-1]]
		memo[(i,j)] <- max(howToRob3(topright, i+1, j-1) , howToRob3(bottomleft, i-1, j+1))
		return memo[(i,j)]

// test all starting points
moneyy <- 0
for i from 1 to n
	for j from 1 to n
		curr <- howToRob3(A, i, j)
		if moneyy < curr
			moneyy <- curr
print moneyy
```
Space: memo holds values of $(i,j)$ for all starting points, that is $O(n^2)$, of whch each has splices of the original array of also $O(n^2)$, so space $O(n^4)$.
Time:
$$
\begin{align}
O\left(\sum^{n}_{i=1} \sum^{n}_{j=1} \sum^{i}_{a=1} \sum^{j}_{b=1} 1\right) = O\left(\frac{1}{4}n^2(n + 1)^2 \right) = O(n^4)
\end{align}
$$

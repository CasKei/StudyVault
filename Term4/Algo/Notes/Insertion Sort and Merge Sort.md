---
aliases: sorting, recursion, divide and conquer, insertion, mergesort, merge sort
tags: #50.004
---
[[Algo]]
[[Algo week 2]]
[[L02.01 - Sorting, solving recursion]]
[[Analysing Complexity of Recursions]]

## Sorting Problem
**Input**: array `A[0...n-1]` of numbers
**Output**: `B`, a *permutation of `A`* such that $B[0] \leq B[1] \leq \cdots \leq B[n]$

**In-place sort**: if the sorted item occupy the same storage as the original one
**Out-of-space sort**: if the sorting algorithm used extra space to do the sorting

## [[Bubble Sort and Insertion Sort#Insertion Sort|Insertion Sort]]
![[Pasted image 20220204105033.png]]
```
for j = 2 to A.length
	key = A[j]
	//Insert A[j] into the sorted sequence A[1..j-1].
	i = j - 1
	while i > 0 and A[i] > key
		A[i + 1] = A[i]
		i = i - 1
	A[i + 1] = key
```
### [[Bubble Sort and Insertion Sort#Analysing Computation Time Computation Time|Complexity of Inertion Sort]]
- Worst-case running time $T(n)$ on input size $n$
$$
\begin{align}
T(n) &= i \text{ comparisons and swaps at step i}\\
&= \sum^{n-1}_{i=1}{i} = \dfrac{n(n-1)}{2} = \Theta(n^2)
\end{align}
$$
## [[Divide and Conquer| Divide and Conquer Revision]]
### Approach
- Break the problem into sveral subproblems that are similar to the original problem, but smaller in size
- Solve the subproblems recursively, and then combine these solutions to create a solution to the original problem
### Solution
- **Divide**: input into parts
- **Conquer**: each part recursively
- **Combine**: results to obtain solution of original
$$\begin{align}
T(n) &= \text{divide time}\\
&+ T(n_1) + T(n_2) + \cdots + T(n_k)\\
&+ \text{combine time}\\
&= aT(n/b) + f(n)
\end{align}$$
### Basic Concepts
> **Recursive case:** When the subproblems are large snough to solve recursively

> **Base case:** Once the subproblems become small enough that we no longer recurse, we say that the recursion 'bottomed out' and we have gotten to the base case.
> **Leaves**: sometimes base cases are also called leaves as they look like leaves on tree branches

> **Recurrence:** an equation or inequality that describes a function in terms of its value on smaller inputs. example:
$$
\begin{align}
T(n) = 
\begin{cases}
\Theta(1) &\text{if } n = 1,\\
2T(n/2) + \Theta(n) &\text{if }n>1
\end{cases}
\end{align}
$$

### Constructing a recursion
1. Read $n$ numbers: $\Theta(n)$
2. Compute middle of array: $O(1)$
3. 2 * Sort n/2 numbers: $2T(n/2)$
4. Merge n numbers: $\Theta(n)$
=> $T(n) = 2T(n/2) + \Theta(n)$

### How does Merge work?
One basic step consists of choosing the smaller of the two starting numbers in two input sequences, removing it from its original input sequence, and placing this number in the outut sequence.
We repeat this step until one input sequence is empty, at which time we just take the remaining input sequence and place it at the end of the output sequence.

#### Revision of splicing syntax:
```python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```
## [[Merge Sort]]
```
MERGE(A, p, q, r)
	n1 = q - p + 1
	n2 = r - q
	let L[0:n1+1] and R[n1+1:n2+1] be new arrays
	for i = 1 to n1:
		L[i] = A[p + i - 1]
	for j = 1 t n2
		R[j] = A[q + j]
	L[n1 + 1] = sentinel
	R[n2 + 1] = sentinel
	i = 1
	j = 1
	for k = p to r
		if L[i] <= R[j]
			A[k] = L[i]
			i = i + 1
		else A[k] = R[j]
			j = j + 1

MERGESORT(A, p, r)
	if p < r
		q = (p + r) // 2
		MERGESORT(A, p, q)
		MERGESORT(A, q + 1, r)
		MERGE(A, p, q, r)
```
Total: $T(n) = 2T(n/2) + \Theta(n)$

## Questions to think about
Does time complexity change when input array is already sorted?
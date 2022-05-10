---
aliases: k-th fibonacci 
tags: 50.004
---
[[Algo]]
[[Algo week 10 & 11]]
[[Dynamic Programming (DP)|DP]]

## Problem
The Fibonacci sequence is:
$$1,1,2,3,5,8,13,21,34,55, \dots$$
$k^{\text{th}}$ number in this sequence is called the Fibonacci number $F_k$.
$$F_1 = 1, F_2 = 1, \dots$$
Fibonacci numbers are defined by
$$
\begin{align}
F_n &= F_{n-1} + F_{n-2} &n > 2\\
\text{base cases } F_1 &= F_2 = 1
\end{align}
$$

## Initial algo
```php
function f(n):
	'''
	Require: n is a positive integer
	'''
	if n <= 2 then
		return 1
	else
		m <- f(n-1) + f(n-2)
		return m

print f(40)
```
```python
def f(n):
	# Require: n is a positive integer
	if n <= 2:
		return 1
	else:
		m = f(n-1) + f(n-2)
		return m

print(f(40))
```
This is [[Sorting, solving recursion|recursive]].

| Plotting running time                | Plot                                 |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20220328225416.png]] | ![[Pasted image 20220328225431.png]] |


## Use memo
```php
Initialise memo = {}
function fib(n):
	'''
	Require: n is a positive integer
	'''
	if n in memo then:
		return memo[n]
	if n <= 2 then:
		memo[n] <- 1
		return 1
	else:
		m <- fib(n-1) + fib(n-2)
		memo[n] <- m
		return m
print fib(40)
```

^79b625

```python
memo = {}
def fib(n):
	# Require: n is a positive integer
	if n in memo:
		return memo[n]
	if n <= 2:
		memo[n] = 1
		return 1
	else:
		m = fib(n-1) + fib(n-2)
		memo[n] = m
		return m
print(fib(40))
```

| Plotting running time                | Plot                                 |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20220328225416.png]] | ![[Pasted image 20220328230441.png]]|

## Compare
![[Pasted image 20220328230945.png]]
![[Pasted image 20220328231000.png]]

## Why
### fib
- memo store computation results
- check if fib(n) has already been computed and stored in memo
- If not computed, compute and store the result in memo

In last iteration: to compute `fib(40)`, we go to the `else` case, compute `fib(39) + fib(38)`, but both have been computed previously, so we can retrieve the values stored in memo.

### f
In the last iteration: to compute `f(40)`, we go to the `else` case, and compute `f(39) + f(38)`.
Even though  we have already computed both, these are not stored, and we have to compute `f(39)` first, then `f(38)`. 
~recursion~

## Tabulation
[[Bottom-up Dynamic Programming]]
```php
initialise array A[1..100]
A[1] <- 1; A[2] <- 1

for k from 3 to 100:
	A[k] <- A[k-1] + A[k-2]

print A[40]
```

^80f9c2

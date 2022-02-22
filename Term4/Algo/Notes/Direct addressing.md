---
aliases: direct address table
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

## Storing elements in arrays by key values
Assumptions:
- Every possible object that we may store in an array has an ==integer key value== `k` satisfying $0 \leq k < N$.
- Diff objects have diff key values (no repeats)

Initialise array `A` of length $N$.
Store pointers to the objects based on their corresponding key values.
- `A[x.key] = x` for every object `x`
![[Pasted image 20220220214622.png]]

`A` is called a [[#Direct address table]], since we can 'look-up' key values.

## Direct address tables
Array `A`, `A.length = 10`
Object `x` with $0 \leq x.key < 9$.

### Insert
```php
function insert(A, x):
	A[x.key] = x
```
Complexity $O(1)$
### Delete
```php
function delete(A, x):
	A[x.key] = NIL
```
Complexity $O(1)$
### Search
```php
function search(A, k):
	return A[k]
```
Complexity $O(1)$

![[Pasted image 20220221134302.png]]

## Limitations
- The set of all possible key values could be very large
	- May not fit in memory
	- Example: If the key values are telephone numbers, then the set of all possible key values has size 108 , so a direct address table would require a contiguous range of 108+ memory locations.
	- Even if the array fits into the memory, many of the entries could be NIL, which is a waste of memory.
- The max possible key value must be known in advance
	- such prior knowledge may not always be available
- Key values may not be integers
	- could be floating point numbers or strings

Solve by [[Hashing]] --> [[Intro to hashing]]
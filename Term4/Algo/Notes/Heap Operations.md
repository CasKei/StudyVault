---
tags: #50.004
---
[[Algo]]
[[Binary Heap and Heapsort]]

## Summary
| Operation        | Function                                                                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `build_max_heap` | Build a max-heap from an (unordered) input array. $O(n)$                                                                                  |
| `max_heapify`    | Corect a **single** violation of the [[Heap data structure#Types of heap\|max-heap property]] occuring **at the root of an input subtree**. $O(\log{n})$ |
| `insert`         | Insert element into an array, array must remain as a max heap. $O(\log{n})$                                                               |
| `extract_max`    | Return element with largest key and remove from array; array must remain as a max heap. $O(\log{n})$                                      |
| `increase_key`   | Increase key value of node with given input index; array must remain as a max heap. $O(\log{n})$                                          |
| `heapsort`       | Sort an array of length $n$ using a heap. $O(n\log{n})$                                                                                   |

## Heapify
[[Binary Heap and Heapsort#Heapify Maintaining the Heap Property]]
Given an array that violates the max-heap property, how do we modify the array into a heap?
`max_heapify(A, i)`
Assumptions:
- Node $i$ violates the max-heap property
- Children of $i$ with all nodes below them do not violate max-heap property.

Goal: To correct the violation of the max-heap property at node $i$

### Techincality: heap size of A
Assumption: Input array `𝐴` has an attribute called `heap_size`.
This attribute is assumed to be mutable.
We initialize `𝐴.heap_size ← 𝐴.length`, but in general, attributes `𝐴.heap_size` and `𝐴.length` could have different values. 
`𝐴. length` is the total number of elements in array `𝐴`.

Why do we need `heapsize` in addition to `length`?
We could set `𝐴.heap_size ← 𝑘` if we want to apply an operation (e.g. max_heapify) only on the first `𝑘` elements of the array, without having to make a new array that consists of the first `𝑘` elements of `𝐴`. This will become very useful when we want to sort an array using heap operations.
### Pseudocode
```php
function MAX_HEAPIFY(A, i)
	l ← left(i)
	r ← right(i)

	// find index of largest element among i and children
	if l <= heap_size(A) and A[l] > A[i]
		then largest ← l
		else largest ← i
	if r <= heap_size(A) and A[r] > A[largest]
		then largest ← r

	//if largest not i, swap with i with largest, run againt on subtree rooted at largest
	if largest != i
		then swap A[i] and A[largest]
		function MAX_HEAPIFY(A, largest)
```
### Complexity
Array size $n$,  complexity $O(\log{n})$. [[Master Theorem]]

## Build Max Heap
[[Binary Heap and Heapsort#Build a Heap with Heap Property]]
Input: array 𝐴, say of length 𝑛 Goal: To reorganize 𝐴 into a max-heap.
Note: nodes $\lfloor n/2 \rfloor + 1 , \dots, n$ must be leaves, since $2i>n \text{ for all }i \geq \lfloor n/2 \rfloor + 1$.
If 2𝑖 > 𝑛, then node 𝑖 has no left child (which must have index 2𝑖), so node 𝑖 must be a leaf.
The max-heap property can only be violated at top half of the tree.
### Pseudocode
```php
function BUILD_MAX_HEAP(A):
	heap_size(A) = length(A)
	for i ← floor(length(A)/2) downto 1
		do MAX_HEAPIFY(A, i)
```
### Complexity
`max_heapify` is called floor(n/2) times = $O(n)$
Each call of `max_heapify` takes $O(\log{n})$ steps
Complexity at most $O(n\log{n})$
$T(n) = O(n)$

## Heapsort
[[Binary Heap and Heapsort#Heapsort]]
Given an array `A` of length `n`
1. Build a max heap from `A`
2. Find maximum element: `A[1]`
3. Swap `A[heap_size]` and `A[1]`
4. Discard node n from heap: set `A.heapsize ← A.heapsize - 1`
5. `max_heapify(A,1)`
6. go to step 2

### Complexity
In every iteration (steps 2 - 5), `A.heapsize` decreasese by 1
After n iterations, heapsize becomes 0
Each iteration has a swap ($O(1)$) and a `max_heapify` ($O(\log{n})$).
Thus heapsort is $$T(n) = O(n\log{n})$$
![[Pasted image 20220212103015.png]]

## Insert(A,x)
Insert number X into heap, but violates max_heap property
Call maxheapify on the affected subtree

```php

```

Number of swaps required is at most the depth of the binary heap, which is $O(\log n)$, hence the complexity $$T(n) = O(\log{n})$$

## extract_max(A)
Remove root and store in variable
Swap `A[heap_size]` and `A[1]`
Apply max_heapify ($O(\log n)$)

```php
function extract_max(A)
	max = A[1]
	A[1] = A[A.heapsize]
	A.heapsize -= 1
	max_heapify(A,1)
	return max
```
$$T(n) = O(\log{n})$$

## Increase_key(A,i,k)
Inputs: array `A`, index `i`, value `k`.
Assume `i<= A.heapsize` and `A[i] <= k`
Goal: increase the value of `A[i]` to `k`, then update `A` so it remains as maxheap

```php
A[i] ← k
while i > 1 and A[parent(i)] < A[i]:
	swap A[i] with A[parent(i)]
	i ← parent(i)
```

The number of swaps required is at most the depth of node i, which is $O(\log n)$
So complexity is $$T(n) = O(\log{n})$$
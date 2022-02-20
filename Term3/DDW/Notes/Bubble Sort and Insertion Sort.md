Back to [[Data Driven World|DDW]]
# Sorting Algorithm
Sort some items in some way. Here with bubble and insertion, sort numbers from smallest to biggest.
Can be adapted to sort others.

## Bubble Sort
Given a sequence of numbers, sort the sequence in some order.
The simplest but pretty darned inefficient sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

If already sorted, the algorithm doesn't know, and will need one whole pass without any swap to know it is sorted.
```py
# geeksforgeeks
def bubble_sot(arr):
	n = len(arr)
	# Traverse through all array elements
	for i in range(n):
		# Last i elements already in place
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
```
```py
# sch
def bubble_sort(arr):
	n = len(arr)
	for i in range(1, n):
		for i in range(1, n):
			if arr[i] < arr[i-1]:
				array[i], array[i-1] = array[i-1], array[i]
```
### [[Analysing Computation Time|Computation Time]]
This always runs $O(n^2)$ even if array is already sorted.
It can be optimised by stopping the algorithm if inner loop did not cause any swap.
If no swap is made in one pass of outer iteration, we can stop the outer iterations.
```py
def bubble_sort(arr):
	n = len(arr)
	swapped = True
	while swapped == True:
		swapped = False
		for i in range(1, n):
			if arr[i] < arr[i-1]:
				array[i], array[i-1] = array[i-1], array[i]
				swapped = True
```
This stops after there is one pass of outer iteration that does not swap anything.
This has worst and average time complexity of $O(n^2)$
Best $O(n)$ when array is already sorted.
Auxiliary space: $O(1)$
Boundary cases: minimum O(n) when already sorted
Sort in place

Note that after each outer pass the last element is sorted.
Optimise further by reducing the number of outer iterations every turn.
```py
def bubble_sort(arr):
	n = len(arr)
	swapped = True
	while swapped == True:
		swapped = False
		for i in range(1, n):
			if arr[i] < arr[i-1]:
				array[i], array[i-1] = array[i-1], array[i]
				swapped = True
		n -= 1
```
This reduces the number of outer iterations after each outer iteration.

Note that if array is sorted even before that, it will still perform extra moves.
```py
def bubble_sort(arr):
	n = len(arr)
	swapped = True
	while swapped == True:
		swapped = False
		for i in range(1, n):
			if arr[i] < arr[i-1]:
				array[i], array[i-1] = array[i-1], array[i]
				swapped = True
				new_n = i
		n = new_n
```

## Insertion Sort
Another algorithm that solves the same problem.
Outer iterations still go from second element to end.
Inner iterations are not fixed, depends on:
- if item at leftmost position
- if item on its left is smaller
So this is more efficient that bubble, and perhaps most efficient when $n$ is small.
```py
def insertion_sort(arr):
	n = len(arr)
	for j in range(1, n):
		i = j
		while (i > 0) and arr[i] < arr[i-1]:
			arr[i], arr[i-1] = arr[i-1], arr[i]
			i -= 1
```
Instead of swapping and assigning elements in the inner iteration, we only assign the element once it finds its final position. To do this we store the element we are going to move in a temporary variable.
```py
def insertion_sort(arr):
	n = len(arr)
	for j in range(1, n):
		i - j
		temp = arr[i]
		while (i > 0) and (temp < arr[i-1]):
			arr[i] = arr[i-1]
			i -= 1
			arr[i] = temp
```
---
Geekforgeek version
```py
def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
```

### [[Analysing Computation Time|Computation Time]]

^e3453a

Time Complexity: $O(n^2)$
Auxiliary Space: $O(1)$
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order, and minimum time to sort (O(n)) when elements are already sorted.
Algorithmic Paradigm: Incremental Approach
Sort in place
Uses: Used when number of elements is small. Also useful when input array is almost sorted, only a few elements are misplaced in complete big array.
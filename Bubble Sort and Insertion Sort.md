Back to [[Data Driven World]]
#DDW, #Sorting, #Algorithm
# PCDIT framework
[[#Bubble Sort]]
- [[#B: Problem Statement]]
- [[#B: Test Cases]]
- [[#B: Design of Algo]]
- [[#B: Implementation]]
- [[#B: Testing]](not here)
[[#Insertion Sort]]
* [[#I: Problem Statement]]
* [[#I: Test Cases]]
* [[#I: Design of Algo]]
* [[#I: Implementation]]
* [[#I: Testing]] (not here)
---
# Bubble Sort

## B: Problem Statement
Given a sequence of numbers, write some steps to sort the sequence in some order. Usually, we sort from smallest to largest.
## B: Test Cases
`[16, 14, 10, 8, 7, 8, 3, 2, 4, 1]` --> `[1, 2, 3, 4, 7, 8, 8, 10, 14, 16]`
Have a pointer move from left to right.
Start from 2nd index, compare with left item.
Swap if out of order.
Shift pointer right and repeat to end.
Now return to 2nd index and repeat whole process $n-1$ times.
## B: Design of Algo
Inner iteration: compare pair and swap if needed
Outer iteration: repeat inner iteration starting from first pair again

There are $n-1$ inner and outer iterations each.

## B: Implementation
This is sorted in place.
```
Version 1
---
Input: array
Output: None, sort in place
---
for outer_i in range(1, len(arr)):
	for i in range(1, len(arr)):
		if arr[i] < arr[i-1]:
			swap
```
### Optimise 1
If sequence already in order, we can stop outer iterations.
```
Version 2
---
Input: array
Output: None, sort in place
---
n = len(arr)
swapped = True
while swapped == True:
	swapped = False
	for i in range(1, n):
		if arr[i] < arr[i-1]:
			swap
			swapped = True
```
The $n^{\text{th}}$ pass of the outer iteration will place the  $n^{th}$ largest number to its final position.

### Optimise 2
Notice the $n^{th}$ pass of the outer iteration will place the $n^{th}$ largest item to its final postion.
This means we can reduce the number of inner iterations after each pass of outer iteration.
```
Version 3
---
Input: array
Output: None, sort in place
---
n = len(arr)
swapped = True
while swapped == True:
	swapped = False
	for i in range(1, n):
		if arr[i] < arr[i-1]:
			swap
			swapped = True
	n -= 1
```
Now the number of outer iterations will reduce.

### Optimise 3
It can happen that more than one element is in their final position after one outer iteration pass. This means we don't have to decrease the number of inner iterations by 1 on each step of outer iteration. We can record down at which position was the last swap, and on next outer iteration we compare up till that last position.
```
Version 3
---
Input: array
Output: None, sort in place
---
n = len(arr)
swapped = True
while swapped == True:
	swapped = False
	new_n = 0
	for i in range(1, n):
		if arr[i] < arr[i-1]:
			swap
			swapped = True
			new_n = i
	n = new_n
```
Use a new variable to assign the end of the next outer pass.

---
# Insertion Sort
## I: Problem Statement
Given a sequence of numbers, write some steps to sort the sequence in some order. Usually, we sort from smallest to largest.
## I: Test Cases
`[16, 14, 10, 8, 7, 8, 3, 2, 4, 1]` --> `[1, 2, 3, 4, 7, 8, 8, 10, 14, 16]`
## I: Design of Algo
Outer iteration: from 2nd element to last element. Places $n^{th}$ element into its position.
Inner iteration: swap $n^{th}$ element until either
- reach first position
- number on left is smaller

$n-1$ number of outer iterations. Number of inner iterations is not fixed as it depends on how messed up that shyt is. (depends on the 2 conditions above)

## I: Implementation
```
Version 1
---
Input: array
Output: None, sort in place
---
n = len(arr)
for outer_i in range(1, n):
	inner_i = outer_i
	while (inner_i > 0) and (arr[inner_i] < arr[inner_i - 1]):
		swap
		inner_i = inner_i - 1
```
### Optimised
Reduce the number of assignment in the inner loop.
This means that instead of swapping and assigning elements in the inner iteration, we only assign the element once it finds its final position.
Store the element we are going to move into a termporary variable.
```
Version 2
---
Input: array
Output: None, sort in place
---
n = len(arr)
for outer_i in range(1, n):
	inner_i = outer_i
	temporary = arr[inner_i]
	while (inner_i > 0) and (temporary < arr[inner_i - 1]):
		arr[inner_i] = arr[inner_i - 1]
		inner_i -= 1
	arr[inner_i] = temporary
```
-   Note that the position stored in 2.4 is `inner_index` instead of `inner_index - 1`. The reason is that in the last iteration, we have executed `inner_i -= 1` which reduces the index by one.
-   Assignment from temporary variable to the array only happens at the end of _inner_ iteration.
Back to [[Data Driven World|DDW]]
# Merge Sort
Merge sort uses the [[Divide and Conquer]] approach.
The idea is to split the input sequence into 2 parts, call merge sort recursively on each part, then combine using merge.

We can divide mergesort into 2 algorithms:
First is the main steps that contain the recursive calls.
Second is the merge steps.

### Mergesort(arr, p, r)
Base case is when the array contains only one element.
In this case the array is trivially sorted.
Recursive case: split the array into two and call recursively the same steps, and combine them after they are sorted.
```py
def mergesort(arr, p, r):
	if (r-p) > 1:
		q = (p+r)//2
		mergesort(arr, p, q)
		mergesort(arr, q, r)
		merge(arr, p, q, r)
	else:
		return arr
```
### Merge(arr, p, q, r)
Have 3 indices, left, right and dest.
Start from beginning and compare the numbers pointed by left and right.
The smaller number will be placed in position pointed by dest.
```py
def merge(arr, p, q, r):
	nleft = q - p
	nright = r - q
	left_arr = arr[p:q]
	right_arr = arr[q:r+1]
	left = 0
	right = 0
	dest = p
	
	while (left < nleft) and (right < nright):
		if left_arr[left] <= right_arr[right]:
			arr[dest] = left_arr[left]
			left += 1
		else:
			arr[dest] = right_arr[right]
			right += 1
		dest += 1
	while (left < nleft):
		arr[dest] = left_arr[left]
		left += 1
		dest += 1
	while (right < nright):
		arr[dest] = right_arr[right]
		right += 1
		dest += 1
	return arr
```
### Main(arr)
```py
def main(arr):
	return mergesort(arr, 0, len(arr))
```
## G4G 1 function mergesort
```py
def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		
		mergeSort(L)
		mergeSort(R)
		
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the array
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()
# Driver code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)
```
Given array is 
12 11 13 5 6 7 
Sorted array is: 
5 6 7 11 12 13
## [[Analysing Computation Time|Computation Time]]
We will use the recursive tree method to analyse computation time.
$$T_{\text{mergesort}}(n) = O(1) + 2T_{\text{mergesort}}(n/2) + T_{\text{merge}}(n)$$
$O(1)$: calculation of index $q$ and the comparison
$2T_{\text{mergesort}}(n/2)$: two recursive calls of mergesort for the left and right arrays
$T_{\text{merge}}(n)$: the call to merge procedure

Thus we need to look into the computation time for merge.
Comparisons and calculating q all take constant time, contributing to $O(1)$.
Copying to left and right array depends on number of elements and so $O(n)$.
Inserting numbers into sorted array from left and right array done $n$ times because the final result is $n$ elements in the sorted array, so $O(n)$.
Steps inside while loops are all constant times repeated for $n$ times.

Therefore,
$$T_{\text{merge}}(n) = O(1) + O(n) + O(n) \times O(1)= O(n)$$

So combining, mergesort computation time:
$$
T(n) =
\begin{align}
\begin{cases}
O(1), &\text{if }n=1\\
2T(n/2)+O(n), &\text{if }n>1
\end{cases}
\end{align}
$$
So now for $n>1$, we have the recurrence relation:
$$T(n)=2T(n)+cn$$
where $c$ is a constant and $c>0$.
We can draw the recurrence tree as shown:
![[Pasted image 20211225150959.png]]
Note at the bottom of the tree there are $n$ leaves, where $n$ is the number of inputs in the array.
We can also calculate the level at the bottom.
At every level, computation time at each node in the tree is $\dfrac{cn}{2^i}$.
For example, at $i=1$, computation time is $\dfrac{cn}{2^1}=\dfrac{cn}{2}$.
At the bottom of the tree, we can only $c \times 1$, and so $\dfrac{cn}{2^{i_{\text{bottom}}}}=c \times 1$,
and we can get $i_{\text{bottom}}=\log_2 n$.
This means that the height of the tree is $h=1+\log_2 n$.
And if we sum up the computation time at each level, we will have $c \times n$.
For example at level $i=1$, we have $cn/2 + cn/2 = cn$; similar for every level.

Therefore, total computation time is the sum at each level multiplied by the number of level.
$$
\begin{align}
T(n) &= cn \times (1 + \log_2{n})\\
&= O(n \log{n})
\end{align}
$$
Here and the subsequent expressions we always use base 2 for our logarithmic function.
Note that the computation time is slower than linear but much faster than quadratic time. This means that mergesort gives a fasted computation time as compared to [[Bubble Sort and Insertion Sort|bubble and insertion sort]] and is similar to [[Binary Heap and Heapsort|heapsort]].
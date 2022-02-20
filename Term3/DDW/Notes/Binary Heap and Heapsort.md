Back to [[Data Driven World|DDW]]
# Binary Heap
![Binary Tree Satisfying Heap Property](https://www.dropbox.com/s/zmy2r3hbte1twc3/Binary_Heap.png?raw=1)
New data structure.
Heap: an array of object that we can view as a nearly complete binary tree.
Tree: upside-down, consist of **nodes** and one **root**.
Binary tree: each node has only 2 children which we call the **left** and **right** children, every node except the root has a **parent** node, node without children is called a **leaf**
Full binary tree: all nodes except leaves have 2 children
Complete binary tree: every level except possibly the last is completely filled, and all nodes are as far left as possible

Put the elements of our array into the tree from top to bottom and left to right sequence. With this we can calculate the index of the children and the parent for every node.
## Indices of Children and Parent in a Binary Heap
This is for binary tree.
Finding index of parent given current index:
```py
def parent(i):
	return int((i-1)/2)
```
Finding index of left child given current index:
```py
def left(i):
	return (i*2)+1
```
Finding index of right child given current index:
```py
def right(i):
	return (i+1)*2
```
Finding max child given parent's index and heapsize:
```py
def max_child(arr, i, size):
	if right(i) >= size:
		return left(i) # assume I have the left child
	else:
		if arr[left(i)] > arr[right(i)]:
			return left(i)
		else:
			return right(i)
```

## Heap Property
There are 2 kinds of heap: min-heap and max-heap. Here we only discus max-heap.
Both heaps must satisy **heap property**, which specifies the kind of heap we are dealing with.
Max-heap property:
```
For all nodes except the root:
A[parent(i)] >= A[i]
```
This means that in a max-heap, the parent nodes are always greater than their children.
Also implies that the largest node is at the root.
# Heapify: Maintaining the Heap Property
This is an algorithm to maintain the heap property. We will call this max_heapify.
The idea is that, for a given node, we will push down this node in such a way that the max-heap property is satisfied.
This assumes that the left child of the given node forms a tree that satisfies max-heap property. Similarly, the right child of the given node forms a tree that satisfies max-heap property.
The only part that does not satisfy the property is the current node and its 2 children.

Given an index of a node in a binary tree, where the children satisfies the max-heap property, restore the max-heap property of the tree starting from the current node.
```
Input: current index in heap
Output: None
Process: re-order the elements in the heap such that max-heap property is satisfied from the current index
Assumptions:
	- left child forms a tree that satisfies max-hap property
	- right child forms a tree that satsifies max-heap property
	- current node with its children may not satisfy max-heap property
```
The procedure of max-heapify will push the current node by swapping with the largest node along the way to satisfy the property. To do that, we will swap with the largest child.
```py
# Version 1: continues iterating even when max-heap property already satisfied

def max-heapify(A, i):
	curr_i = i
	while left(i) < size:
		max_child_i = max_child(arr, curr_i, size)
		if arr[max_child_i] > arr[curr_i]:
			arr[max_child_i], arr[curr_i] = arr[curr_i], arr[max_child_i]
		curr_i = max_child_i
```
Note we can stop iterating if the largest child is already less than the current node. Do this by checking if there is a swap. If no swap is needed then we are done. This is because we assume that the left child and the right child already satisfies the max-heap property.
```py
# Version 2: check if there is swap before continuing

def max-heapify(A, i):
	curr_i = i
	swapped = True
	while (left(i) < size) and swapped:
		swapped = False
		max_child_i = max_child(arr, curr_i, size)
		if arr[max_child_i] > arr[curr_i]:
			arr[max_child_i], arr[curr_i] = arr[curr_i], arr[max_child_i]
			swapped = True
		curr_i = max_child_i
```

The above are iterative/looping.
Recursive solution:
[[L03.02 - Heap Operations#Pseudocode|Recursive heapify]]

# Build a Heap with Heap Property
We can then use the previous max-heapify to build a binary heap data structure from any arbitrary array. The idea is to go through every node and heapify them. However, we do not need to d so for all nodes, only half. This is because we do not need to heapify the leaves.

We can show that elements from $n/2$ onwards are all leaves. We do not need to push down these nodes as they do not have any children. So we can start from the element at index $n/2 - 1$ and move up to element at position 0.
```
Input: array of integers
Output: None
Process: Re-order the elements such that the whole array satisfies the max-heap property.
```
--> Starting index = middle node. Call max-heapify on this node.
--> Move to the left and continue calling max-heapify until we reach the first element at index 0.
```py
def build_max_heap(arr):
	for i in range( len(arr)//2 - 1, -1, -1):
		max_heapify(arr, i, len(arr))
```

# Heapsort
For any arbitrary array, we can sort the integers in the array by first building a binary heap.
Once a heap is built, we know that the maximum is at the root.
We swap the root with the last element and remove that huge shyt.
Then restore that max-heap property after the swap becasue now the root node is small.
Do this repeatedly until there is no mroe element in the heap.
```
Input: array of integers
Output: None
Process: Sort the elements in order
```
- First, build a max-heap.
- Then start from the last element and swap it with the root. Leave the last element untouched as it is now sorted.
- Reduce the heap-end-pos to exclude the sorted element.
- Call max-heapify on the subarray
```py
def heapsort(arr):
	size = len(arr)
	build_max_heap(arr)
	while size > 0:
		arr[0], arr[size - 1] = arr[size - 1], arr[0]
		size -= 1
		max_heapify(arr, 0, size)
	return arr
```
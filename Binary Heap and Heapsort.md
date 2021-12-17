Back to [[Data Driven World]]
#DDW, #Sorting, #Algorithm
# Binary Heap and Heapsort
Previously, we discussed two sorting algorithms called [[Bubble Sort and Insertion Sort]]. In this section we will apply our programming skills to investigate another sorting algorithm called the Heapsort. We will then compare the performance of Heapsort with the previous [[Bubble Sort and Insertion Sort]]. We will discuss some notations on how to analyze these performance.

One reason why we introduce different sorting algorithms is to show you that there are many ways to solve the same problems. At the same time, these different ways may have different performances. After we introduce [[#binary heap]] and [[#heapsort]] algorithm, we will begin to introduce you how to analyze these different algorithms in terms of [[computation time]]. You will notice that Heapsort algorithm is a much better sorting algorithm as compared to Bubble sort and Insertion sort algorithms.

## Binary Heap
New Data Structure!
> The heap is an array of object that we can view as a nearly complete binary tree.

- Tree: upside down. Consists of nodes. Has one root node at the top
- Binary Tree: Each node has only 2 children called left and right child. Every child has a parent node except the root. Nodes without children is a leaf.
- Full binary tree: tree where all the nodes except the leaves have 2 children
- Complete binary tree: binary tree in whihc every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- Root: index 0
### Indices of Children and Parent
```py
def parent(i):
	return int((i - 1)/2)
def left(i):
	return (i*2) + 1
def right(i):
	return (i + 1)*2
```
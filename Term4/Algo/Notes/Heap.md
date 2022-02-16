---
aliases: tree, binary tree
tags: #50.004
---
[[Algo]]
[[Binary Heap and Heapsort]]
[[L03.01 - Heap]]

## Data Structure and Heap
A heap is a [[Data Types and Data Structures|data structure]].
- Recall: a data structure is a format to store and organise data, in order to facilitate acess and modification
- Heaps are built from arrays, but heaps are not arrays

Operations associated to the heap data structure are called **heap operations**.
- We can build algorithms involving these heap operations

Common use of heaps: to implement a kind of [[Data Types and Data Structures#Data types versus abstract data types ADT|ADT]] called a [[Priority Queue]].

## Visualising a heap
A heap is a data structure whose data storage format can be visualised as a binary tree.

> A binary tree is a tree in which every node has at most 2 children

- Root: top node
- Children: roots immediately below node x are children of node x
- Parent: node immediately above
- Leaf: node with no children

## What is a [[Binary Heap and Heapsort#Binary Heap|Heap]]?
> A Heap is a data structure whose data storage format can be visualised as a nearly complete binary tree.

i.e. in all levels, except possibly the last, every node has 2 children.

In heaps, data is still stored as an array, but given any such array, we can always determine its binary tree visualisation.

## Types of heap
> Max heap: A heap that satisfies the [[Binary Heap and Heapsort#Heap Property|max-heap property]]

The key of every node is greater than or equal to the keys of its children (if any).
So the root has the maximum possible key value.

> Min heap: A heap that satisfies the [[Binary Heap and Heapsort#Heap Property|min-heap property]]

The key of every node is less than or equal to the keys of its children (if any).
So the root has the minimum possible key value.

> Other kinds: non-binary heaps

The heaps we have seen so far are binary heaps
There are more general heaps, where for some fixed $d>2$, every node instead has at most $d$ children.
- Ternary heap: a nearly complete ternary tree: every node has at least 3 children.
- d-ary heap: a nearly commplete d-ary tree: every node has at least d children.

Since a min-heap becomes a max heap if we negate al the keys, we can just focus on binary max heaps.

## Depth of a heap
> Depth of a node $x$: number of edges in the downward path from the root to node $x$

Depth of root = 0
Depth of binary tree = maximum value among the depth of all nodes in the binary tree
Depth of a heap = depth of the binary tree that corresponds to the heap
![[Pasted image 20220211211222.png]]

## Height of a heap
> Height of a node $x$: the maximum possible number of edges in a downward path from the node $x$ to a leaf

Height of leaf = 0
Height of binary tree = maximum value among the heights of all nodes in the binary tree
Height of a heap = height of the binary tree that corresponds to the heap
![[Pasted image 20220211211420.png]]

## Storing Heaps as Arrays
[[Binary Heap and Heapsort#Indices of Children and Parent in a Binary Heap]]
For array `A[1...n]`,
Root: `A[1]`
Parent(i) = $\lfloor \frac{i}{2} \rfloor$
Left(i) = $2i$
Right(i) = $2i + 1$

## Basic Properties
- No pointers required
- Depth of binary heap with $n$ elements is $\lfloor \log_2{n} \rfloor$
- Depth of a heap with $n$ elements is $\Theta(\log{n})$
- Depth of any node in the heap is $O(\log{n})$
---
aliases: 
tags: #50.004
---
[[Algo]]
[[Algo week 4]]
Recall:
[[Binary Heap and Heapsort]]
[[Heap]]
[[Data Types and Data Structures]]

## What is a binary search tree?
> Binary search tree (BST) is a [[Data Types and Data Structures|data structure]] whose data storage format can be visualised as a [[Heap|binary tree]], such that the [[#Binary Search Tree Property]] is satisfied.
> - A BST is allowed to be very "imbalanced"
> - In contrast to heaps, this binary tree need not be complete
> - You can still have a child even if your parent does not have 2 children

Data is stored as either:
- array
- linked list

Every node `x` in a BST must have 4 attributes:
- `x.left`
- `x.right`
- `x.parent`
- `x.key`

Attributes may have NIL value

## Binary Search Tree Property
> A BST must satisfy the binary search tree property:
> For every node `x` of a BST, the following holds:
	> - `x.left != NIL`: any node `y` in left subtree of `x`, rooted at `x.left`, must have `y.key <= x.key`
	> - `x.right != NIL`: any node `z` in right subtree of `x`, rooted at `x.right`, must have `x.key <= z.key`
>
>Hence, `y.key <= x.key <= z.key` for any nodes `y` and `z` contained in left and right subtrees of `x` respectively.

Basically a max heap but left children must be smaller than right children, but can be messed up
![[Pasted image 20220214193618.png]]

## Uses
Similar to [[Heap]], BSTs can also be used to implement priority queues and sorting algorithms.

[[Traversals of a BST]]

[[Operations of BSTs]]
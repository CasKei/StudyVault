---
tags: #50.004
---
[[Algo]]
[[Algo week 4]]
Recall:
[[Heap data structure]]: [[Heap data structure#Depth of a heap|Depth of Heap]], [[Heap data structure#Height of a heap|Height of Heap]]
[[Data Types and Data Structures]]
[[What is a Binary Seach Tree]]
[[Traversals of a BST]]

## Some Operations on BSTs
| Operation     | What it does                                                                                                                                              | Complexity |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [[#tree_insert T x]] | Insert element into BST, must still be BST after                                                                                                          |  O(height of T)          |
| [[#tree_delete T x]] | Delete element from BST, must still be BST after                                                                                                          |O(height of T)            |
| [[#tree_max x and tree_min x\|tree_max x]]    | Given element `x`, return element with largest key value in subtree rooted at `x`                                                                         |O(height of x)            |
| [[#tree_max x and tree_min x\|tree_min x]]   | Given element `x`, return element with smallest key value in subtree rootedat `x`                                                                         |O(height of x)            |
| [[#tree_search x k]] | Given element `x` and value `k`, return first instance of an element with key value `k` in the subtree rooted at `x` if it exists, otherwise return `NIL` | O(height of x)           |
| [[#successor x]]  | Given element `x`, return the next element in the BST wrt [[Traversals of a BST#In-order traversal\|in-order]]                                            | O(height of T)           |
| [[#predecessor x]]| Fiven element `x`, return the previous elemen in the BST wrt the [[Traversals of a BST#In-order traversal\|in-order]]                                     |O(height of T)            |

Recap: [[What is a Binary Seach Tree#Binary Search Tree Property]]

## tree_insert(T, x)
Input: binary search tree `T`, element `x`
Assumptions: 
- `x.key != NIL`
- `x.left == x.right == NIL`

Goal: insert element `x` so that [[What is a Binary Seach Tree#Binary Search Tree Property|BST property]] still holds

```python
def tree_insert(T, x):
	'''code for finding y below'''
	y <- element in T that is available to be the parent of x
	
	x.parent <- y
	
	if T.root == NIL:
		T.root <- x
	elif x.key < y.key:
		y.left <- x
	else:
		y.right <- x
```
```python
def finding_y(T, x):
	y <- NIL
	z <- T.root

	while z != NIL:
		y <- z
		if x.key < z.key:
			z <- z.left
		else:
			z <- z.right
```

### Complexity
To find `y`, we traverse down the tree, starting from root.
So the maximum number of nodes visited is `h + 1`, where `h` is the height of the root node.
Thus the complexity of `tree_insert(T, x)` is $O(\text{height of }T)$.

## tree_max(x) and tree_min(x)
Input: element `x`
Goal: return element with largest/smallest key value among these elementsin subtree rooted at `x`

```python
def tree_max(x):
	while x.right != NIL:
		x <- x.right
	return x
```
```python
def tree_min(x):
	while x.left != NIL:
		x <- x.left
	return x
```

### Complexity
- **Tree_max**: To find the final output, we traverse down the binary tree. So the max number of nodes visited is `h + 1`, where `h` is the height of input `x`. Thus, the complexity of `tree_max` is $O(\text{height of }x)$.
- **Tree_min**: To find the final output, we traverse down the binary tree. So the max number of nodes visited is `h + 1`, where `h` is the height of input `x`. Thus, the complexity of `tree_min` is $O(\text{height of }x)$.

## tree_search(x, k)
Inputs: element `x`, a possible key value `k`
Goal: To return the first found instance of an element with key value `k` in subtree rooted at `x` if it exists, otherwise return `NIL`

```python
def tree_search(x, k):
	while x != NIL and k != x.key:
		if k < x.key: # by BST prop, element with k must be in left subtree of x
			x <- x.left
		else: # by BST prop, element with k must be in right subtree of x
			x <- x.right
	return x
```

### Complexity
To find the final output, we traverse down the binary tree, starting from node `x`. So the max number of nodes visited is `h + 1`, where `h` is the height of `x`.
Thus, the complexity of `tree_search(x, k)` is $O(\text{height of }x)$.

## successor(x)
Input: element `x`
Goal: To return the next element in BST wrt [[Traversals of a BST#In-order traversal|in-order]]
Note: key value of this next element is the next key value in sorted order from smallest to largest.

```python
def successor(x):
	# if x has right child, by BST prop, element with next smallest key value must be in right subtree
	if x.right != NIL: 
		return tree_min(x.right)

	# if x does not have right child, look at parent
		# if no parent, x is root with no right child, so no successor
		# if x is left child of parent, then successor(x) is x.parent
		# if x is right child of parent, then find closest ancestor y of x such that x is a descendant of y.left
	y <- x.parent 
	while y != NIL and x == y.right:
		x <- y
		y <- y.parent
	return y
```

### Complexity
Look at the sections of the code: We can divide this into the `if` block, and the `assignment + while` block.
- `if` block: Complexity $O(\text{height of }x)$
- Remaining `while` block:
	- We are finding the closest ancestor of `y` such that `x` is a descendant of `y.left`
	- To find `y`, we are traversing UP the binary tree, starting from `x`.
	- So the max number of nodes visited is: $(\text{depth of }x) + 1$.

Conclusion: `successor(x)` has complexity $O(\text{height of }T)$.

## predecessor(x)
Input: element `x`
Goal: To return the previous element in BST wrt [[Traversals of a BST#In-order traversal|in-order]]
Note: key value of this previous element is the previous key value in sorted order from smallest to largest.

```python
def predecessor(x):
	# if x has left child, by BST prop, element with next smallest key value must be in left subtree
	if x.left != NIL: 
		return tree_max(x.left)

	# if x does not have left child, look at parent
		# if no parent, x is root with no left child, so no successor
		# if x is right child of parent, then predecessor(x) is x.parent
		# if x is left child of parent, then find closest ancestor y of x such that x is a descendant of y.right
	y <- x.parent 
	while y != NIL and x == y.left:
		x <- y
		y <- y.parent
	return y
```

### Complexity
Look at the sections of the code: We can divide this into the `if` block, and the `assignment + while` block.
- `if` block: Complexity $O(\text{height of }x)$
- Remaining `while` block:
	- We are finding the closest ancestor of `y` such that `x` is a descendant of `y.right`
	- To find `y`, we are traversing UP the binary tree, starting from `x`.
	- So the max number of nodes visited is: $(\text{depth of }x) + 1$.

Conclusion: `predecessor(x)` has complexity $O(\text{height of }T)$.

## tree_delete(T, x)
Inputs: binary tree `T`, element `x`
Goal: To delete element `x` so that [[What is a Binary Seach Tree#Binary Search Tree Property|BST property]] still holds

There are 3 cases:

### Case 1: `x` is a leaf
Simply remove `x` without any further action as [[What is a Binary Seach Tree#Binary Search Tree Property|BST property]] still holds.

### Case 2: `x` has one child
"Promote" the child to replace `x`, then remove `x`. This way the [[What is a Binary Seach Tree#Binary Search Tree Property|BST property]] still holds.

### Case 3: `x` has 2 children
We need to find a suitable replacement for `x` among `x`'s descendants.

Let `z` be a suitable replacement for `x`, chosen from the descendants of `x`.
Choose `z` from the elements in the right subtree of `x` because:
- By [[What is a Binary Seach Tree#Binary Search Tree Property|BST property]], any such `z` will have a key value at least the key values of those in the left subtree of `x`.
- Hence just focus on the larger subtree.

#### Case 3a: `x.right` has no left child
=> Any element in the right subtree of `x` that is not `x.right` must be in the right subtree of `x.right`.
- Any element in `x.right` subtree has a key value at least the value of `x.right`
- `x.right == successor(x)`

Hence: "Promote" `x.right` to replace `x`, while still maintaining [[What is a Binary Seach Tree#Binary Search Tree Property|BST property]].

#### Case 3b: `x.right` has a left child
Let:
- `y = successor(x)`
- `x' = x.right`
- `y' = y.right`

=> `y` is the left child of the left child of ... the left child of `x'`.
=> `y` has no left child

Hence: "Promote" `y` to `x`, and shift the subtree rooted at `y` up to where `y` was.

### Pseudocode
In order to move subtrees within the binary tree, we define a subroutine `transplant(T, u, v)`, taking in the `T` tree, and replaces the subtree rooted at `u` with the subtree rooted at `v`.
Node `u`'s parent becomes `v`'s parent, and `u`'s parent ends up having `v` as its appropriate child.
```python
def transplant(T, u, v):
	# if u is root of T
	if u.parent == NIL:
		T.root <- v
	# if u is a left child
	elif u == u.parent.left:
		u.parent.left <- v
	# if u is a right child
	else:
		u.parent.right <- v
	# if v is non-NIL
	if v != NIL:
		v.parent <- u.parent
```
Note that `transplant(T,u,v)` does not attempt to update `v.left` and `v.right`; doing so or not is the choice of the caller.

With `transplant`, the following is `tree_delete`:
```python
def tree_delete(T, z):
	if z.left == NIL:
		transplant(T, z, z.right)

	elif z.right == NIL:
		transplant(T, z, z.left)

	else:
		y <- tree_min(z.right)
		if y.parent != z:
			transplant(T, y, y.right)
			y.right <- z.right
			y.right.parent <- y
		transplant(T, z, y)
		y.left <- z.left
		y.left.parent <- y
```

### Complexity
$O(\text{height of }T)$
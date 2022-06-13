---
aliases: balanced height
tags: #50.004
---
[[Algo]]
[[Algo week 4]]
[[Heap data structure]]
[[What is a Binary Seach Tree]]
[[Traversals of a BST]]
[[Operations of BSTs]]

## The Importance of Being Balanced
From [[Operations of BSTs]], we see that `height` affects the complexity of the operations the most.
![[Pasted image 20220215112859.png]]
### Strategy to maintain a balanced BST
- Augment every node with a new attribute
	- When inserting new elements, we must specify values for this new attribute.
- Define a new property that the BST must satisfy
	- Like some additional restriction or constraint that this new subfamily of BSTs must satisfy
- Show that this new property guarantees that the height of the BST is $\Theta(\log n)$.
- Design algorithms to compute values for this new attribute, and maintain the new property.

## AVL Trees: Definition, Balanced Height Property
_Adelson_-_Velskii_ & Landis
> New Attribute:
> Every node `x` has the attribute `x.height`
> - Recall leaves have height 0
> - Define NIL object to have `NIL.height = -1`

> New Property:
> For every node `x`, the height of `x.left` and `x.right` differ by at most `1`.
> - "Balanced height property"

> AVL Tree: A [[What is a Binary Seach Tree|BST]] that satisfies the balanced height property.

## Height of AVL Trees
> An AVL tree with `n` elements has height $h=\Theta(\log n)$.

### Proof:
Let $n_h$ be the minimum number of nodes in a non-empty AVL tree that has height $h$.
	By the balanced height property,
	$$\begin{align}
	n_h &\geq 1 + n_{h-1} + n_{h-2}\\
	&> n_{h-1} + n_{h-2}\\
	& \geq 2n_{h-2}
	\end{align}$$
	So using the relation $n_h > 2n_{h-2}$ recursively, we get
	$$n_h > 2n_{h-2} > 4n_{h-4} > 8n_{h-6} > \cdots$$
	where the last expression is 
	$$\begin{align}
	\begin{cases}
	2^{\frac{h}{2}}n_0 &\text{if $h$ is even}\\
	2^{\frac{(h-1)}{2}}n_1 &\text{if $h$ is odd}
	\end{cases}
	\end{align}$$
Since $n_1 \geq 2$ and $n_0 = 1$, we get in either case that $n_h > 2^{\frac{h}{2}}$.

From $n_h > 2^{\frac{h}{2}}$, we infer that
	$$\begin{align}
	\frac{h}{2} &< \log_2{n_h}\\
	\implies h &< 2\log_2{n_h}\\
	\implies h &= O(\log{n_h})
\end{align}$$
Next we find a lower bound for $h$.
Let $m_h$ be the maximum number of nodes in an AVL tree that has height $h$.
An AVL tree is a binary tree, so
$$\begin{align}
	m_h &\geq 1 + 2 + \cdots + 2^h\\
	&= 2^{h+1} - 1\\
	&< 2^{h+1}
	\end{align}
	$$
which means
$$\begin{align}
	h+1 &< \log_2{m_h}\\
	\implies h &= \Omega(\log{m_h})
\end{align}$$
Finally, since $n_h \leq n \leq m_h$, we get
$$
\begin{align}
h &= O(\log{n_h}) = O(\log n)\\
h &= \Omega(\log{m_h}) = \Omega(\log m_h)
\end{align}
$$
Therefore $h=\Theta(\log n)$.

## Rotations
Rotations maintain the [[Traversals of a BST#In-order traversal|in-order]] order of key values.
![[Pasted image 20220215120212.png]]
Rotations can reduce height.
![[Pasted image 20220215120304.png]]

### Left-Rotate(T, x)
```python
def left_rotate(T, x):
	y = x.right # set y
	x.right = y.left # turn y's left subtree into x's right subtree
	if y.left != T.NIL:
		y.left.parent = x

	y.parent = x.parent # link x's parent to y
	if x.parent == T.NIL:
		T.root = y
	elif x == x.parent.left:
		x.parent.left = y
	else:
		x.parent.right = y

	y.left = x # put x on y's left
	x.parent = y
```
### Right-Rotate(T, x)
```python
def right_rotate(T, x):
	y = x.left
	x.left = y.right
	if y.right != T.NIL:
		y.right.parent = x
	y.parent = x.parent
	if x.parent == T.NIL:
		T.root = y
	elif x == x.parent.right:
		x.parent.right = y
	else:
		x.parent.left = y
	y.right = x
	x.parent = y
```

## Destroying balance with insert and delete
![[Pasted image 20220215120450.png]]
- When `tree_insert(T, u)` is run on a BST `T` that is height-balanced, the resulting tree could become not balanced.
- Similarly, when `tree_delete(T, u)` is run on a BST `T` that is height-balanced, the resulting tree could also become not balanced.

## Define: Balanced, left-heavy, right-heavy
Let `x` be a node of a BST.
Assume all nodes of a BST has a `height` attribute, and by default, `NIL.height = -1`.
> `x` is **balanced** if both children of `x` have the same heights.
> - `x.left.height == x.right.height`
> 
> `x` is **left heavy** if left child has strictly larger height than the right child
> - `x.left.height >= x.right.height + 1`
> 
> `x` is **right heavy** if right child has strictly larger height than left child
> - `x.left.height + 1 <= x.right.height`

## Balancing an Imbalanced BST
Let `x` be a lowest node (largest depth) that violates the [[AVL Trees#AVL Trees Definition Balanced Height Property|balanced height property]].

Violation of [[AVL Trees#AVL Trees Definition Balanced Height Property|balanced height property]]:
- Left-heavy: `x.left.height >= x.right.height + 2`
- Right-heavy: `x.left.height + 2 <= x.right.height`

Let `y` be `x.right`.
There are 3 cases:
- [[#Case 1 y is right-heavy]]
- [[#Case 2: y is balanced]]
- [[#Case 3: y is left-heavy]]

### Case 1: y is right-heavy
We want to redistribute the weight leftwards.
[[#Left-Rotate T x|left_rotate(x)]]
![[Pasted image 20220215164502.png]]

### Case 2: y is balanced
[[#Left-Rotate T x|left_rotate(x)]]
![[Pasted image 20220215164532.png]]

### Case 3: y is left-heavy
Left rotate removes the violation at node `x`, but `y` now violates the [[AVL Trees#AVL Trees Definition Balanced Height Property|balanced height property]].
Hence, use 2 other rotations: [[#Right-Rotate T x|right_rotate(y)]], then [[#Left-Rotate T x|left_rotate(x)]]
![[Pasted image 20220215172024.png]]
The final BST is now height balanced.

## Note
For the insertion of a new element `x` into an AVL tree `T` with `n` elements, it is possible to use $O(\log n)$ steps so that the  [[AVL Trees#AVL Trees Definition Balanced Height Property|balanced height property]] of `T` is maintained, such that at most $O(1)$ rotations are used.
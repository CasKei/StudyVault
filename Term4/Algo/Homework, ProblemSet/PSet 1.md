---
tags: #50.004
---
# 50.004 PSet1
## Cassie Chong 1005301 CL01
## 1) Heaps[10]
Question 1 (Heaps). Illustrate all intermediate steps (as a sequence of binary trees) for the operation `Extract_Max()` applied to the max heap $A = [18, 13, 9, 5, 12, 8, 7, 3, 0, 2, 4]$. Your illustrations should also include both the initial max heap $A$, and the final max heap that $A$ becomes, after executing `Extract_Max(A)`.
***
Max heap: $A = [18, 13, 9, 5, 12, 8, 7, 3, 0, 2, 4]$
```php
function Extract_Max(A):
	if A.heapsize < 1:
		throw error
	max = A[1]
	A[1] = A[heapsize] //
	A.heapsize = A.heapsize - 1
	function Max_heapify(A, 1)
	return max
```
![[Pasted image 20220218105417.png]]
***
## 2) Heaps
### i) [5]
In class, we demonstrated the implementation of `Increase-key` on a max heap:
![[Pasted image 20220218102131.png]]
Design an efficient algorithm to ==decrease a key== in a ==max heap== (while maintaining the max-heap property), and analyze the running time complexity of your algorithm in terms of $n$, the size of the heap. Similar to the Increase key operation, your algorithm should not return any output, but rather, modifications should be made to the input max heap. State any ==assumptions== made on the input(s) of your algorithm. Please present your algorithm in pseudocode.
***
To decrease a key in an already given max-heap, just assign the decreased value to the index needed and then call `max_heapify(A,i)` on that index.
The pseudocode will look like this, with `max_heapify(A,i)` as a support function:
```php
function left(i)
	return (i*2)+1
function right(i)
	return (i+1)*2

function heap_size(A)
	return A.length

function Max_Heapify(A, i)
	l ← left(i)
	r ← right(i)

	// find index of largest element among i and children
	if ((l <= function heap_size(A)) and (A[l] > A[i]))
		then largest ← l
		else largest ← i
	if ((r <= function heap_size(A)) and (A[r] > A[largest]))
		then largest ← r

	//if largest not i, swap with i with largest, run againt on subtree rooted at largest
	if largest != i
		then swap A[i] and A[largest]
		function MAX_HEAPIFY(A, largest)

function Decrease_Key(A, i, k)
'''Require: A[1..n] is a max heap.
   Require: i is an integer, and 1<=i<=n
   Require: A[i] > k
'''
	A[i] <- k
	Max_Heapify(A, i)
```
- Assigning `A[i] <- k` takes complexity $\Theta(1)$
- Max_Heapify is called on index `i`
	- `l <- left(i)` and `r <- right(i)` are assignments and math computations, taking $\Theta(1)$ time.
	- The next block checks for largest child, comparisons and assignments take $\Theta(1)$ time.
	- The next block recursively calls back the function, meaning the index `i` in question traverses a maximum of the height of `i`, depending on whether a swap has taken place. This in the worst case is with `i=1` and swapping for the full height of the heap for $O(\log_2{n})$, since the heap is binary.
Hence overall complexity:
$$T(n) = O(\log_2{n})$$
<br>
### ii)[5]
Design an efficient algorithm to ==convert a max heap into a min heap== with the same elements, and analyze the running time ==complexity== of your algorithm in terms of $n$, the size of the heap. Your algorithm should not return any output, but rather, modifications should be made to the input max heap. State any ==assumptions== made on the input(s) of your algorithm. Please present your algorithm in pseudocode.
***
We need a `min_heapify(i)`, `left(i)`, `right(i)`, `heap_size(A)`.
`Min_heapify` from half the heap up.
```php
'''
Required: A[1...n] is a maxheap at input
Required: i is an integer, 1<= i <= n
'''
function left(i)
	return (i*2)+1
function right(i)
	return (i+1)*2
function heap_size(A)
	return A.length

function min_heapify(A, i)
	l <- left(i)
	r <- right(i)
	if ((l <= function heap_size(A)) and (A[l] < A[i]))
		then smallest <- l
		else smallest <- i
	if ((r <= function heap_size(A)) and (A[r] < A[smallest]))
		then smallest <- r

	if smallest != i
		then swap(A[i] , A[smallest])
		function min_heapify(A, smallest)

function convert_max_to_min(A) // basically a buildminheap
	i = (function heap_size(A) / 2) - 1 //floor div
	while i >= 1 do
		function min_heapify(A, i)
		i--
	return A
```
- First, `convert_max_to_min(A)` is called as a main function.
	- First line calculates the index to start calling min_heapify from: $O(1)$ complexity
	- Next is a `while` loop starting from the first non-leaf element from the bottom, with a maximum of $n/2$ iterations of this block.
		- Inside the loop, `min_heapify(A,i)` is called.
			- - `l <- left(i)` and `r <- right(i)` are assignments and math computations, taking $\Theta(1)$ time.
			- The next block checks for smallest child, comparisons and assignments take $\Theta(1)$ time.
			- The next block recursively calls back the function, meaning the index `i` in question traverses a maximum of the height of `i`, depending on whether a swap has taken place. This in the worst case is with `i=1` and swapping for the full height of the heap for $O(\log_2{n})$, since the heap is binary.
- So overall, with the while loop, the entire operation takes.
$$T(n) = O(1) + O((n/2)\cdot\log_2{n}) = O(n\log_2{n}) $$
But not all leaves are heapified, can be tighter.
Number of leaves at most:
$$2^{\log_2{(n)-(h+1)}}=\dfrac{n}{2^{h+1}}$$
Time complexity for height $h=\log_2{n}$:
$$\begin{align}
T(n) &= O \left( \sum^{\log_2{(n)}}_{h=0} \log_2{n} \cdot \dfrac{n}{2^{h+1}} \right)\\
&= O \left( n \sum^{\infty}_{h=0}  \dfrac{h}{2^{h}} \right)\\
&= O(n)
\end{align}$$
<br>
***
## 3) Balanced BSTs
### i)
We define a binary search tree with $n$ nodes to be ==self-balancing if its height is $O(log n)$==. For example, an AVL tree is a self-balancing binary search tree.
#### a) [3]
Let $T$ be a binary search tree, and for every node in $T$, we require that the height of its left and right subtrees differ by no more than $2$. Is $T$ a self-balancing binary search tree? Justify your answer.
***
If a binary search tree has height difference differ by at most 2, rotations can be done to balance the tree such that its height difference makes $O(\log{n})$. So this is still a self-balancing tree.
Let $n_h$ be the minimum number of nodes in a non-empty BST that has height $h$ that is self-balancing.
By condition where the BST height difference differs by at most 2,
$$n_h \geq 1 + n_{h-1} + n_{h-3} > n_{h-1} + n_{h-3} \geq 2n_{h-3}$$
So using the relation $n_h > 2n_{h-3}$ recursively, we get
$$n_h > 2n_{h-3}> 4n_{h-6} > 8n_{h-9} > \cdots$$
where the last expression is $2^{\frac{h}{2}}n_0$ if $n$ is even or $2^{\frac{h-1}{2}}n_1$ if $n$ is odd.
Since $n_1 \geq 2$ and $n_0 = 1$, we get $n_h > 2^{\frac{h}{2}}$.
$$\frac{h}{2} < \log_2{n_h} \implies h < 2log_2{n_h} \implies h=O(\log{n})$$
So this is still a self-balancing tree.
On further intuition it can have height restored through rotations.
<br>
#### b) [3]
Let $T$ be a binary search tree, and for every node in $T$, we require that the number of nodes in its left subtree and its right subtree are each no more than 90% of the total number of nodes in its subtree (including the node itself). Is $T$ a self-balancing binary search tree? Justify your answer.
***
If every subtree is at most 90% of the size of its parent, then the height of the tree is at most $\dfrac{\log{n}}{\log{0.90}}$, which means that $\text{height}=O(c\log{n})$, so the tree is still self-balancing.
<br>
### ii) [4]
Find an exact expression for the ==minimum possible depth== of a leaf in an AVL tree with height $h$. Justify your answer with details.
***
Depth of a node $x$: number of edges in the downward path from the root to node $x$.
Height of a node $x$: the maximum possible number of edges in a downward path from the node $x$ to a leaf.
An AVL tree has the height of the left and right subtrees differ by at most 1.
-->
Denote the minimum depth of a leaf in an AVL tree of height $h$ by $d_{min}(h)$.
The two subtrees of the roots must have either one with height $h-1$ and the other with either $h-1$ or $h-2$, by the definition of AVL trees.
Thus a leaf must have $d_{min}(h) = \min{(d(h-1), d(h-2))} + 1$.
With the depth function being non-decreasing, the statement can be reduced to:
$$d(h)=d(h-2)+1$$
This can be seen as a recurrence relation.
First we observe $d(0)=0$ and $d(1)=0$ (since we defined NIL to have value of -1).

$$
\begin{align}
d(h) &= d(h-2) + 1 \\
&= d(h-4) + 1 + 1 &= d(h-4) + 2 \\
&= d(h - 6) + 1 + 1 + 1 &= d(h-6) + 3 \\
&\vdots \\
&=d(h-2i) + i \\
& \vdots \\
&= d(h-h) + \frac{h}{2} &\text{, since d(0) = 0,}\\
&=\frac{h}{2} &\text{at lowest depth}
\end{align}
$$
Hence minimum possible depth is $h/2$, and this can be expressed as $$d(h) = \left\lfloor \frac{h}{2} \right\rfloor$$
<br>
***
## 4) BST
### i) [5]
Let $a$ and $b$ be two distinct elements in a binary search tree. When we run `Tree_delete` on $a$ followed by $b$, will it always give the same binary search tree as when we run `Tree_delete` on $b$ followed by $a$? If true, then explain in as much details as possible why it is true. If false, then give a counter-example, and explain your counter-example in detail.
***
![[Pasted image 20220220150139.png]]
Consider the above example with root 5 with children 3 and 7, and 6 a child of 7.
Let's say we delete 5 and 3.
- Deleting 5 will result in the successor 6 being promoted to take 5's place. (case 3b of delete operation)
- Then deleting 3, a leaf, will have no change. (case 1 of delete operation)
- This results in a tree with 6 as root and 7 as child.

Then we swap the order and delete 3 then 5.
- Deleting 3 first will simply remove the node as it is a leaf. (case 1 of delete operation)
- Then deleting 5, the root, we promote the only child that is 7 (case 2 of delete operation)
- This results in a tree with 7 as root and 6 as its child.

The two end results are not equal. Hence, performing `Tree_delete` on distinct elements $a$ then $b$ will not always give the same result as running `Tree_delete` on $b$ then $a$. (Counterexample)
<br>
### ii) [5]
Design an efficient **non-recursive** algorithm to print the key values of the elements of an input non-empty binary search tree (BST) in sorted increasing order. Analyze its running time complexity in terms of $n$, the number of elements in the input BST. State any assumptions made on the input(s) of your algorithm. Please present your algorithm in pseudocode. ==You may use any non-recursive BST operations discussed in the lectures or cohort classes==, but be careful that you only use inputs that are valid for these BST operations.
***
This requires in-order traversal that is non-recursive.
How to travel back? Make right point back. Make guiding pointer? Must be removed before pointer loops forever.
```php
function inorderIterative(node):
'''Require: start from root node
   Require: an index i to point to nodes
   Require: another pointer j to guide i
   Require: the tree is a BST (right child > left child)
   Require: methods node.left and node.right tell the index of left and right child of node, else NIL
   Require: method node.key returns value of node
'''
	i = node; // this is root at init
	while (i != NIL) do // pointer i still pointing at existing node
		if (i.left == NIL) then // since right surely larger, no left = i smallest
			print i.key // register smallest value that is i
			i <- i.right // point i to right child
		else // i has left child 
			j <- i.left // set guide to left child of i
			// for subtree rooted at i, successor is rightmost node of left subtree
			while (j.right != NIL and j.right != i) do
				j <- j.right // go to the rightmost node of left subtree of i

			// guide has no right child
			// connect j.right to where i is and it is safe to move i left
			if (j.right == NIL) then
				j.right <- i // point guide.right at where i is
				i <- i.left // move i to the left

			// this is if left subtree is completely visited
			// we can record i and move i to right subtree
			else
				j.right <- NIL
				print i.key
				i <- i.right
```
The algorithm traverses the tree, node by node, in the general direction from left subtrees to the right (for the increasing order since right subtrees are larger).
Each node is visited at most a constant time.
Hence complexity is just in order of $O(n)$.
<br>
***
## 5) AVL trees [10]
Starting with an empty AVL tree, insert nodes $a, b, c, d, e, f, g, h, i, j$ in order with key values $7, 1, 18, 15, 11, 4, 13, 19, 10, 8$ respectively. Illustrate all intermediate trees and all rotation steps. Assume that the AVL tree remains an AVL tree with every insertion operation.
***
![[Pasted image 20220219210205.png]]
<br>
***
## 6) AVL Trees, BSTs
### i) [10]
When we run AVL `insert(T, x)` for an AVL tree $T$ and a new element $x$ to be inserted into $T$, we know that at most 1 $node^1$ will have to be rebalanced to maintain the balanced height property. Is it true that at most one node has to be rebalanced when we run AVL `delete(T, x)` for an AVL tree $T$ and an element $x$ of $T$ to be deleted? Here, AVL `delete(T, x)` is an operation analogous to the BST operation `Tree_delete(T, x)`, with the requirement that $T$ remains an AVL tree after the deletion of $x$ from $T$. Justify your answer with as much details as possible.
$^1$This may require two rotations, in the left-right or right-left rotation cases
***
When inserting into an AVL tree, with a single insertion, the height of an AVL tree cannot increase by more than 1, so only one rotation is necessary to restore the balanced height property.
When deleting a node from an AVL tree that already might have a height difference of 1 or -1, the balanced height property may be violated at a low level and have to be rotated there, but still violated at higher levels and need to be rotated at a node with a higher height.
<br>
### ii) [15]
Design an efficient algorithm that, when given any binary search tree $T$ and a value $k$ as its inputs, returns two binary search trees $T_{≤}$ and $T_>$ as its outputs, where $T_{≤}$ contains only the elements of $T$ that are less than or equal to $k$, and $T_>$ contains only the elements of $T$ that are strictly greater than $k$. State any assumptions made on the input(s) of your algorithm. Please present your algorithm in pseudocode. Justify why your algorithm maintains the binary search tree property of the output, and analyse the running time complexity of your algorithm.
***
```php
'''Require: Every BST node has attributes .left, .right, .key, .root
   Require: creation of a Node is done by calling Node(item)
'''
arrBST <- []
index <- 0
function inorder(node)
	if (node == NIL) then
		return
	inorder(node.left)
	arrBST[index++] <- node.key
	inorder(node.right)

function makeBST(arr)
	if (arr.length == NIL) then
		return NIL
	mid = (arr.length / 2)
	rootnode = Node(arr[mid])
	rootnode.left = makeBST(arr[:mid])
	rootnode.right = makeBST(arr[mid+1:])
	return rootnode

function splitBST(T, k)
	inorder(T.root)

	BST1 <- arrBST[:k]
	BST2 <- arrBST[k+1:]

	BST_leq <- makeBST(BST1)
	BST_g <- makeBST(BST2)
	return BST_leq, BST_g
```
First we store the values of the tree T given inorder in an array.
This does not miss or add any elements, ensuring all elements are included.
Next we split into 2 arrays at k, with k being in the first array.
Making use of the fact that the left subtree has values smaller than the root of the subtree, we can recursively call the function to make the left child smaller and similarly the right child larger than the middle value.
This will create children of the root and descendants that satisfy the BST property.
Finally we return the root nodes of both initialised trees.

- Inorder traversal: $O(n)$ since all nodes must be visited at least a constant number of times.
- Slicing the array takes $O(n)$ as there are $n$ elements to be assigned into new arrays.
- MakeBST
	- $T(n) = 2T(n/2) + O(1)$: constant time is calculating middle and linking left and right root to subtrees, recursion splits into 2 subproblems and is done twice.
		- Level n: c
		- Level n/2, n/2: 2c
		- Level n/4, n/4, n/4, n/4: 4c
		- -> Last level has $2^{\log_2{n}}=n$ leaves
		- Which is $T(n) = c + 2c + 4c + ... + nc = 2n-1=O(n)$.
- Total $T(n) = O(n) + O(n) + O(n) = O(n)$.
<br>
***
## 7) d-ary heaps
As mentioned in Lecture L0301 Slide 23, we define a d-ary heap (for d ≥ 2) analogously like a binary heap, but instead, in the d-ary tree visualization of a d-ary heap, we allow every node to have at most d children. In this question, you will extend several binary heap operations to the case of d-ary heaps
### i) [5]
Find expressions for `D-ary-Parent(d, i)` and `D-ary-Child(d, i, j)`, which map a node in the array representation of a d-ary heap with index `i` to its parent and its `j`-th child $(1 ≤ j ≤ d)$ respectively. Justify your answers with details.
***
Heap is nearly complete: all nodes except leaves have d children.

Parent of `A[1]` is NIL. Parent of `A[i]` for $2\leq i \leq d+1$ is `A[1]`. Parent for $d+2 \leq i \leq 2d + 1$ is `A[2]`.
Parent is a factor of `d` above child, minus `1` for root:
	`D-ary-Parent(d, i) = ceil((i - 1) / d)`

Root be `A[1]` => d children in `A[2..d+1]`, (level 1, 2)
their children in `A[d+2]` to `A[d^2 + d + 1]`, (level 3), and so on
Child is a factor of `d` of its parent, plus root and `j`th child:
	`D-ary-Child(d, i, j) = d(i - 1) + j + 1`

### ii) [10]
Design an algorithm that ==extends== `Max_heapify(A, i)` to d-ary ==max== heaps $A[1..n]$. State any assumptions made on the inputs of your algorithm. In particular, d should be one of the inputs of your algorithm. Please present your algorithm in ==pseudocode==. Also, please analyze the running time ==complexity== of your algorithm in terms of $d$ and $n$.
***
Instead of concluding largest child is left or right child like `Max_heapify(A, i)`, we need to find largest child iteratively. Otherwise, the recursive comparisons are swaps should remain.
```php
function D_Max_Heapify(A, i)
'''Required: A[1...n] is a maxheap at input
   Required: i is an integer, 1<= i <= n
'''
	largest <- i
	for (index<-1 up to d)
		if (index <= heapsize) and (A[index] > A[largest]) then
			largest <- index

	if largest != i then
		swap A[i] <-> A[largest]
		D_Max_Heapify(A, largest)
```
Every call to `D_Max_Heapify` makes $\Theta(d)$ comparisons to find largest.
Recursive calls are done level by level so there are $O(\log_d{n})$ calls.
Total: $T(n) = O(d\log_d{n})$.

### iii) [10]
Design an algorithm that ==extends== `Build_max_heap(A)` to d-ary max heaps A[1..n]. State any assumptions made on the inputs of your algorithm. In particular, $d$ should be one of the inputs of your algorithm. Please present your algorithm in ==pseudocode==. Also, please analyze the running time ==complexity== of your algorithm in terms of $d$ and $n$.
***
Instead of calling from half the tree since bottom half are leaves, call from length/d up since more than that the nodes are leaves.
```php
function BuildD_max_heap(A)
'''Required: A[1...n] is a maxheap at input
   Required: i is an integer, 1<= i <= n
'''
	heapsize(A) <- length(A)
	for i ← ceil(length(A)/d) downto 1
		do D_Max_Heapify(A, i)
```
At height $h$, number of nodes:
$$d^{\log_d{(n(d-1))-(h+1)}}=\dfrac{n(d-1)}{d^{h+1}}$$
Each heapify call is $O(d\log_d{n})=O(dh)$, so running time for `BuildD_max_heap(A)` is
$$
\begin{align}
T(n) &= O \left( \sum^{\log_d{(n(d-1))}}_{h=0} dh \dfrac{n(d-1)}{d^{h+1}} \right)\\
&= O \left( n(d-1) \sum^{\infty}_{h=0}  \dfrac{h}{d^{h}} \right)\\
&= O \left( n(d-1)  \dfrac{1/d}{(1-1/d)^2} \right)\\
&= O \left(n \left(\dfrac{d}{d-1} \right)\right)\\
&= O(n)
\end{align}
$$
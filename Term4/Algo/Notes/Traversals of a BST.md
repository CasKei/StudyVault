---
tags: #50.004
---
[[Algo]]
[[Algo week 4]]
Recall:
[[Binary Heap and Heapsort]]
[[Heap]]
[[Data Types and Data Structures]]
[[What is a Binary Seach Tree]]

## How to order the elements of a BST?
If BST has `n` elements, how do we print them?

Three common kinds of tree traversals:
- [[#Pre-order traversal]]
- [[#In-order traversal]]
- [[#Post-order traversal]]

![[Pasted image 20220214194357.png]]
## Pre-order traversal
- Begin at top of the root node
- Traverse leftwards and trace the outside of the tree
- Record every new node visited starting from root

```python
def preorder(node):
	if node == NIL:
		return
	print(node.key)
	preorder(node.left)
	preorder(node.right)
```
Running `preorder(root_node)` will print the key values of the nodes in preorder
>![[Pasted image 20220214200036.png]]
>FBADCEGIH
## In-order traversal
- Begin at top of root node
- Traverse leftward and trace the outside of the tree
- When you visit an unrecorded node, record this node if
	- it has no left child
	- it has a visited left child

```python
def inorder(node):
	if node == NIL:
		return
	inorder(node.left)
	print(node.key)
	inorder(node.right)
```
>![[Pasted image 20220214200101.png]]
>ABCDEFGHI

The in-order of a BST is exactly the sorted order!

## Post-order traversal
- Begin at top of root node
- Traverse leftward and trace the outside of the tree
- When you visit an unrecorded node, record this node if
	- it is a leaf
	- it is the last time that you visit it

```python
def postorder(node):
	if node == NIL:
		return
	postorder(node.left)
	postorder(node.right)
	print(node.key)
```

>![[Pasted image 20220214201804.png]]
>ACEDBHIGF


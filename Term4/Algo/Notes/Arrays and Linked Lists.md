---
aliases: LL
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

[[Data Types and Data Structures]]
[[Fixed-Size Array and Linked List]]
## Pointers VS Objects
> Pointer: a pointer to an object is stored as the address of the first memory location of the object

Attributes of an object can be data or pointers to other objects.

Storing objects in computer memory
- Continuous range of memory locations, including attributes (e.g. arrays)
- Made up of 'smaller' objects stored in multiple ranges of memory locations (e.g. LL)

In [[Data Types and Data Structures|data structures]] such as [[Binary Seach Trees (BST)|BSTs]], their elements are stored as pointers
- [[Data Types and Data Structures|Data structures]] (e.g. [[Heap]]) or [[Data Types and Data Structures|datatypes]] (e.g. [[Priority Queue]]), even if implemented using arrays, could have attributes stored as pointers.


## Key values
In many [[Data Types and Data Structures|data structures]], each element `x` is asusmed to have an attribute `x.key`.

[[Heap]] and [[Binary Seach Trees (BST)]]:
- assume key values are numerical so we can make numerical comparisons

Other data structures where operations do not involve numerical comparisons of key values, we can allow non-numerical key values like strings

-> e.g. Python: a dictionary is implemented as a [[Hash Table]] (data structure), where the key of each item in a dictionary is not necessarily a numerical value.


## Storing pointers in arrays
Let $x_1, \dots , x_{100}$ be pointers to 100 objects.
We could store them in an array `A` with length `100`
The entire array `A` is an object stored in a contiguous range of 100k+ memory locations in the computer memory.
	- k: the number of memory locations used to store a single pointer
	- RMB we also need to store the attributes of `A`.

If we want to store one more pointer $x_{101}$, then we have to reinitialise a new array of length 101.
If the next memory location is already occupied, then we have to find another contiguous range to store the new array.

To avoid frequent re-initialisations, we can 'pre-allocate' memory by initialising an array of larger length.


## Linked Lists
[[Fixed-Size Array and Linked List#Linked List|Linked Lists DDW]]
Let $x_1, \dots , x_{100}$ be objects (possibly of different types).
(in many languages, when we create a LL, we are storing their pointers)

How to store LL
- Create 100 new objects $x_1, \dots , x_{100}$
- Each $x_k$ is a pointer to the $k$th object $X_k$ and has attributes `x_k.prev` and `x_k.next`
	- `x_k.prev = x_{k-1}`
	- `x_k.next = x_{k+1}`
	- `NIL` outside range
	- -> This is a doubly linked list

A new object `L` is created, with attribute `L.head = x_1`

Overall: 101 segments
A 'head' and the 100 elements.


### Searching and Deleting in LL
> Assumptions: `L` is a LL, `x` is an element of `L`, `k` is a key value.

Search for node with value k
```php
function list_search(L, k)
	x <- L.head
	while x != NIL and x.key != k
		x <- x.next
	return x
```
Worst case complexity $O(n)$

Delete node x
```php
function list_delete(L, x)
	if x.prev != NIL then
		x.prev.next <- x.next
	else:
		L.head <- x.next
	if x.next != NIL
		x.next.prev <- x.prev
```
Complexity $\Theta(1)$ (all cases)

Delete key with value k
```php
function list_delete_key(L, k)
	x <- list_search(L, k)
	list_delete(L, x)
```
Worst case complexity: $O(n)$


## Insertion: Array VS LL
[[Fixed-Size Array and Linked List#Inserting and Removing an Element]]
[[Fixed-Size Array and Linked List#Inserting an Element]]
Arrays:
	- Initialise `A = [NIL, ..., NIL]` of length 100
	- Inserting <= 100 elements is fast ($O(1)$ steps) but
	- Inserting > 100 elements requires re-initialising `A` (slow)

LL:
	- Inserting new elements into LL is always fast ($O(1)$ steps) no matter now many elements we insert.

Assumptions: `L` is a LL, `x` is a pointer of the object to be inserted
```php
function list_insert(L, x)
	x.next <- L.head
	if L.head != NIL then
		L.head.prev <- x
	L.head <- x
	x.prev <- NIL
```
Complexity $\Theta(1)$ (all cases)

## Searching: Array VS LL
LL:
	- Requires visiting elements one by one
	- $O(n)$: where $n$ is number of elements in `L`
	- $O(\log n)$: if `L` has [[AVL Trees]] structure
	- Searching whether `L` contains an element `x` (pointer) has complexity $O(n)$ (check pointers one by one)

Arrays:
	- If elements of an array `A` are ==stored arbitrarily==, then 
		- searching if `A` contains a specific element,
		- if `A` has an element with a specific key value,
	- would take $O(n)$ steps
Can we store the elements in a smarter way?
[[Direct addressing]]
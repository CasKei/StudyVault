---
aliases: FSarr, LL
tags: #linear, #datastructure, #ds
---
Back to [[Data Driven World|DDW]]
Back to [[Term 3]]
# Fixed-Size Array
Python does not have a fixed-size array data type.
However, many programming languages like C/C++ and Java have this more basic and primitive list-like data type.
You need to declare the size of the array and its type. For example in C or Java:
```java
int mynumber[10];
```
This declaration reserves 10 spaces in memory to store an array of `int` type.
If one `int` number takes 32-bit, then the program reserves 10 spaces of 32-bit in the memory as shown below.
![[Pasted image 20211228105012.png]]
You can access element using the index.
 In C programming language, the name of the array is also the address of the first element.

 Once it is declared to have 10 spaces, the array cannot be extended. You need to reallocate the memory if you have more numbers than what is declared.

 Each element has the same data type. The consequence of this is that each element occupies the same size in the memory. Since it occupies the same size, it is easy to know where the other data are. The advantage of this way of creating an array is that it is fast and simple.

 Though Python does not have such fixed-size array, Numpy library implements something similar in its Numpy's array. For example, numpy array must have the same data type. The difference, however, you can extend the numpy array and you need not declare how many elements are there in the array.
 ```py
import numpy as np

number1 = np.array([1, 2, 3])
print(number1, type(number1), number1.dtype)
 ```
 > [1 2 3] <class 'numpy.ndarray'> int64

 This is how to create a numpy array using `np.array()`. It takes in a list as its argument.
 Numpy will try to detect the data type and in the example above it was detected as `int64` which means a 64-bit integer.
 If one element is a float Numpy will consider all of them to be floats.

 However, Numpy provides additional functionalities to manipulate array such as to append or to insert.
 ```py
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.append(a, b)
print(c)
d = np.insert(c, 0, b)
print(d)
 ```
 > [1 2 3 4 5 6]
[4 5 6 1 2 3 4 5 6]


## Adding an Element When Array is Full
Initially, when the list is created, `MyArrayList` will create an empty array with some fixed initial size, say 16 elements.
When all the 16 elements are filled up, and a new data is appended, `MyArrayList` will double the size to 32 elements and put the new data at the next empty position. See figure below.
![[Pasted image 20211228112714.png]]
This is one way to work.
The disadvantage of this method is that we always have to reserve extra memory space to work.
The advantage is that since the size is fixed for each element, it is easy to locate the data at any position using its index.
## Inserting and Removing an Element
To insert one element, one can first check if there is enough space in the allocated memory. 
If there is not enough space, we can double the size of the array as in the case of adding an element at the end.
 If there is enough space for one more element, then no doubling of memory is needed and we can just shift all the element to the right by one position and insert the element at the position we want it.
 ![[Pasted image 20211228112843.png]]
 The above figure shows what happens when we insert the data at position 2 (third position). Assuming that the array is already full, we need to ensure that we have enough capacity to insert a new element. Therefore, we first need to increase the memory size by doubling the array. Once there is enough space, we shift all the elements to the right and modify the value of the element at position 2 (third position).
### [[Analysing Computation Time|Computation Time]]
 To create a new with double size and copy the old values to the new array takes $O(n)$ time.
 Shifting the values by one in the worst case scenario takes $O(n)$ time.
 Modifying the value takes constant time, i.e. $O(1)$.
 So we should expect such insert operation takes linear $O(n)$ complexity.

 Removing an element is similar.
 Shift left all the elements by one position.
 Depending on the design, we may want to choose to keep the empty space available once we reserve it.
 This, however, may not be a preferred option in systems with small memories like embedded systems.
# Linked List

^780eaa

Instead of just storing the element, a Linked List stores more information in one **node**. In a linked list, each node contains the following:
-   the element
-   and the reference to the next element
The linked list itself stores references to 2 nodes:
- Head
- Tail

![[Pasted image 20211228113132.png]]
This arrangement allows several flexibility.
1.  The element can be objects of different sizes. Since the way to get to some element is through the _next_ references, there is no constraint that the element must be of the same size.
2. You can add new element as needed by creating a new node and point the tail to the new node and the last element's next reference to this new node. In this way, you need not reserve any empty memory space as in the fixed size array.
3. Allows you to have a list with any size without declaring how many elements would be in the list.

Downsides:
It is slower than the fixed size array.
In a fixed size array, it is fast and simple to access the element at a particular position using the index since the size of each element is the same.
 $$\text{(address i)}=\text{(address 0)} + i \times \text{(size of one element)}$$
But in linked list, we have to traverse the nodes to reach the element that we want. This is slower than just computing the exact location.
## Inserting an Element
### Insert at First Position
1.  Create a new Node with the new element.
2.  Set the first node (i.e the current head) as the _next_ reference of the new node.
3.  Set the new node as the _head_ of the linked list.

![[Pasted image 20211228123255.png]]
### Insert at Last Position
1.  Create a new Node with the new element.
2.  Set the new Node as the _next_ reference of the _tail_ of the linked list.
3.  Set the new Node as the new _tail_ of the linked list.

The only tricky thing is when the linked list is empty. In this case, the _tail_ will refer to a NIL. In this case we use the new Node as both the _head_ and the _tail_ of the linked list.
![[Pasted image 20211228123327.png]]

### Insert between First and Last Position
1.  Traverse up to Node 1.
2.  Create a new node.
3.  Get the _next_ reference of Node 1 and set it as the _next_ of the new Node.
4.  Set the new Node as the _next_ of Node 1.

![[Pasted image 20211228123358.png]]
### [[Analysing Computation Time|Computation Time]]
Worst Case: insert a new element to the second last position. Traverse to the node before the tail, which takes $O(n-1) \approx O(n)$ time.
Other operations take constant time.
Hence overall inserting an elementtakes linear time $O(n)$.
## Removing an Element
### Remove from First Position
1.  Store the head into a temporary node variable
2.  We get the _next_ reference of the temporary node and set it as the new _head_
3.  We can store the element of the temporary node so that we can return it at the end
4.  Now, we can delete the temporary node, and
5.  return the element of the deleted node

![[Pasted image 20211228123550.png]]
### Remove from Last Position
1.  We first need to traverse to the node before the _tail_, set this as the current node.
2.  Set the current node as the new _tail_.
3.  Set the next of the new _tail_ to NIL.
4.  We can store the element of the deleted node.
5.  Delete the node and return the element only.
### Remove from between First and Last Position
1.  Traverse the nodes until the node before (i.e. Node 0 in this case) and set it as the current node.
2.  Save the next of the current node into a temporary variable. This is the deleted node.
3.  Set the next of the deleted node as the next of the current node, i.e. Node 2 as the next of Node 0 in the figure.
4.  Delete the node and return the element only.

![[Pasted image 20211228123646.png]]
### [[Analysing Computation Time|Computation Time]]
Since removing node involves traversing the linked list, the worst case complexity will be linear, i.e. $O(n)$.
# [[Inheritance and Abstract Base Class|ABC]] for List
Both kinds of list, however, can be designed to implement the same operations. This is where our lesson on inheritance can be applied. We can design a base class for our list that is inherited by the two ways of implementing a list.
![[Pasted image 20211228123938.png]]
In the UML above, we showed that `MyAbstractList` implements the Abstract Base Class of `Iterator`. 
To satisfy this, you need to define a method called `__iter__()` in `MyAbstractList` that returns an iterator object. 
The class `MyAbstractList` also defines some common property and methods for both `MyArrayList` and `MyLinkedList` such as:
-   `size`, which is an attribute that stores the number of items in the list.
-   `is_empty`, which is a computed property that returns whether the list is empty or not.
-   `add(item)`, which adds an item to the end of the list.
-   `remove(item)`, which removes an item from the list.
-   `__getitem__(index)`, which allows you to use the bracket operator to get an item, e.g. `mylist[index]`.
-   `__setitem__(index, value)`, which allows you to use the bracket operator and assignment operator to set a value at a particular index, e.g. `mylist[index] = value`.
-   `__delitem__(index)`, which allows you to use the `del` operator and the bracket operator to delete an item, e.g. `del mylist[index]`.
-   `__len__(index)`, which is called when you use the `len()` function on the list, e.g. `len(mylist)`.

This class `MyAbstractList` is inherited by the two classes `MyArrayList` and `MyLinkedList`. The class `MyArrayList` is implemented using fixed-size array while `MyLinkedList` is implemented using a linked list. Since the implementation is different, the code to add and remove items for these two classes will be different. Therefore, the `add(item)` method in the `MyAbstractList` would call a method `add_at(index, item)` which is implemented in the child class `MyArrayList` and `MyLinkedList`. This means that both `MyArrayList` and `MyLinkedList` have `add_at(index, item)` method in their class definitions. However, the implementation of this method is different between the two classes.

Similarly, the `remove(item)` method would call a method `remove_at(index)` which is implemented in both the `MyArrayList` and `MyLinkedList` classes. The `__getitem__(index)` method is called either when you use the square bracket operator as in `mylist[index]` or the get method as in `mylist.get(index)`. Since the way to access the element is different between the fixed-size array and the linked list, this method should be overridden in the child classes. Similarly, the method `__setitem__(index, value)` would have different implementation in the children classes. Therefore, our implemention of this method would call the method `set_at(index, item)` of the child class' method.

The parent class `MyAbstractList` inherits and implements `Iterator` class. This ensures that all our list are iterable. To implement `Iterator` class, we must define `__iter__()` method in our `MyAbstractList` which returns an iterator object. Both `MyArrayList` and `MyLinkedList` inherits this iterator method when they inherit from `MyAbstractList`.
---
aliases: stack, queue
tags: #data-structures, #DS
---
Back to [[Data Driven World|DDW]]
Back to [[Term 3]]
# Linear Data Structure
## Stack
LIFO (Last In First Out)
- Push: add to the stack by putting it at the top
- Pop: remove the top item
- Peek: look at the top item

* You cannot do things to the middle or bottom of a stack

![[Pasted image 20211226142438.png]]
## Queue

^55e4cd

FIFO (First In First Out)
![[Pasted image 20211226143243.png]]
- Enqueue: put item to rear
- Dequeue: take item out from front
- Peek: look at front without removing

# Applications
## Post-Fix Expression Evaluation (Stack)
Infix: $3+4 \times 2$
Postfix: $42 \times 3+$

Steps:
1. Read expression from left to right
2. If operand
	1. Put operand into stack
3. Elif operator
	1. pop the top of stack as right operand
	2. pop the top of stack as left operand
	3. evaluate the operator with the operands
	4. push the result into the stack
## Program's Stack
Computer actually uses stacks in recursion.
Visualise the stack calls: [pythontutor factorial](https://pythontutor.com/visualize.html#mode=display)
## Radix Sort (Queue)
Radix sort is a non-comparison sorting algorithm for integers by grouping integers by individual digits that share the same position and value.
It uses 10 'bins' numbered 0-9.

Radix sort will go trough each digit of all numbers and put them in the buckets matching their digit, and take them out again, repeating until all digits are checked.

There are 2 kinds of queues:
- Main bin x1
- Radix bin queues x10

Radix sort operation:
1. Put all items into main bin queue
2. Start with lowest digit, i.e. ones digit. Take out all items from main bin and put it into the respective radix bins.
3. Empty out the radix bin and put the item back into the main bin, starting from radix 0, until 9
4. Repeat until we reach the highest digits,

## Queue with Double Stack
Queue data structure may be implemented in different ways.
One way is just to use a list as its internal storage.
But the problem with using a list is that one of the Queue operation will be slow.

Consider we use
```py
def enqueue(self, item):
    self.items.append(item)
```
to add an item to the list.
We always add the item in this case to the back.
This operation takes $O(1)$ time.

However, the removal part must be written as
```py
def dequeue(self):
    return self.items.pop(0)
```
This is slow.
Python has to move all the elements after index 0 one position to the left.
This will take $O(n)$ time, where $n$ is the number of items in the Queue.

This motivates us to think whether there is another way to implement a Queue.

We use 2 stacks: left and right stack.
Example:
![[Pasted image 20211226192113.png]]
With this implementation, both enqueue and dequeue are at constant time $O(1)$.

What is tricky is when we try to dequeue an item while the Left Stack is empty.
To do this, we follow the following:
1. Copy all items from Right Stack to Left Stack
2. Reverse the items in the Left Stack
3. Remove the items on the Right Stack
4. Pop the requested item from the Left Stack
![[Pasted image 20211226192545.png]]

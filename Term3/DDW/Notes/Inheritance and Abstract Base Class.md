---
aliases: inheritance, abc, ABC
tags: #abc, #inheritance
---
Back to [[Data Driven World|DDW]]
# Inheritance
We can reuse the code from some base class by using inheritance.
Python syntax for deriving a class from some base class is:
```py
class SubClass(ParentClass):
	pass
```
By specifying the parent class, the child class inherits all the attributes and methods of the parent class.
We can then define the attributes that are unique to the child class, and the methods in the parent class we want to override, in the cild class.

Overriding: re-define methods of the parent class.
One commonly overridden method is the initialisation method.
```py
class Vertex:
    def __init__(self, id=''):
        self.id = id
        self.neighbours = {}
```
```py
import sys

class VertexSearch(Vertex):
    def __init__(self, id=""):
        super().__init__(id)
        self.colour = "white"
        self.d = sys.maxsize
        self.f = sys.maxsize
        self.parent = None
```
First line if the init calls the parent class' initialisation, and subsequent lines initialise attributes that are unique to the child class.
In this way, we need not rewrite all the initialisation codes of the parent class and simply reuse tem.
Note that in overriding a method, we use the same method's name and arguments as in the parent class.

More examples of inheritance below.
## Fraction and MixedFraction
![[Pasted image 20211228092655.png]]
In the above UML diagram, we choose not to have any additional attributes but only different initialization arguments. This means that we have to initialize the numerator and the denominator from the three arguments used in the initialization `MixedFraction(top, bottom, whole)`, i.e. $\text{numerator} = \text{whole} \times \text{bottom} + \text{top}$.

Similarly, there are no methods to do addition and subtraction, it depends on the parent method.
In fact, when Python cannot find the name of a particular method in the child class, it will try to find the same name in the parent class methods.
If there is no name matched in the parent's class methods, only then it will throw an error saying that such method is not defined.

Note `__str__()` methodis overriden in the child class. The name and argument is the same, yet behaviour is different.
## Queue and Deque
![[Pasted image 20211228093556.png]]
A `Deque` can have items inserted from either the front or the rear. Items can also be popped out from either.
This is when [[Stacks and Queues#Queue with Double Stack|Queue is implemented with double stack]].

Notice that in the UML diagram `/` is used to represent computed property.
Deque does not have any additional attributes or property, only new methods.
In here, `add_rear()` is the same as `enqueue()`, and `remove_front()` is the same as `dequeue()`, and `peek_front()` is the same as `peek()`. So we need not rewrite half the methods, just call its parent class methods.
# Abstract Base Class
Parent class only specifies what attributes and methods the child classes should have, and in itself has no implementations.
```py
class MyAbstractClass:
    def add(self, other):
        pass

class ChildOfMyAbstractClass(MyAbstractClass):
    def add(self, other):
        # contains implementation of adding the two objects
        ...
```
Child class overrides the methods.

Previously in [[#Fraction and MixedFraction]] we see that any method call to do addition and subtraction will be referred to the parent class. Here in ABC it is the opposite.
When we have an ABC with no implementation, we are forcing the implementation to be found in the child class.
However, there is nothing preventingthe child class not to implement the required method.

So, Python has some mechanism to ensure that the abstract method is implemented in the child.
Use `collections.abc` class. This is a ABC for containers.
For example, if we want a new data type belonging to type `Iterable`, we can inherit this new class from `collections.abc.Iterable`. Python will force the new class to define the method `__iter__()`, otherwise it will throw an error.
```py
import  collections.abc as c

class NotRightIterable(c.Iterable):
    def __init__(self):
        self.data = []

test = NotRightIterable()
```
> TypeError                                 Traceback (most recent call last)
<ipython-input-3-04bbdf83346f> in <module>
 5         self.data = []
 6 
----> 7 test = NotRightIterable()
TypeError: Can't instantiate abstract class NotRightIterable with abstract methods __iter__

Python will complain. To fix this, we need to define this method in the child class.
```py
import  collections.abc as c

class RightIterable(c.Iterable):
    def __init__(self):
        self.data = []
        
    def __iter__(self):
        return iter(self.data)

test = RightIterable()
```
There will be no error when you run the above cell. It simply returns an iterable object from `self.data`.
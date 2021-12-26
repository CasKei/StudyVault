---
aliases: OOP
tags: #oop, #OOP
---
Back to [[Data Driven World|DDW]]
Back to [[Term 3]]
# Object Oriented Programming
## What is OOP?
[[Object Oriented Programming|OOP]] is a programing paradigm based on the concept of 'objects'.
[Wikipedia for OOP](https://en.wikipedia.org/wiki/Object-oriented_programming)

As your program grows in complexity, you may need something more than simple built-in datatypes. In some cases, it is easier to organise your code around objects.
You can think of objects as your own user-defined datatypes.
These objects have 2 main things:
- attributes: defines the characteristics of the object
- methods: defines what the object can do
`list` and `str` in python are **built-in** objects. Here we can build our own.

See that user-defined obejcts are made of other data (attributes) and computations (methods).
Moreover, we will see that any code can be abstracted as an object, since any computer code are made of data and some computations.
## Attributes and Methods
Attributes are usually a noun, and defined as some kind of variable within the object.
Methods are usually a verb, describes what the object can do, so are a kind a function that applies to our user-defined type.

Say you want to create a computer game with a Robot Turtle as its character.
Define a new datatype called `RobotTurtle`.
Attributes: `speed`, `name`.
Methods: `move`.

The class definition tells Python about your user-defined object and how to create it.
It tells Python what attributes this object has using some existing buit-in data type or other defined objects.
It tells Python what methods this object can do.

Note: class definition is just like a template. The template does not create the object.
Instantiation is the step that actually creates the object.
```py
# Class definition
class RobotTurtle:
    # Attributes:
    def __init__(self, name, speed=1):
        self._name = name
        self._speed = speed
        self._pos = (0, 0)

    # Methods:
    def move(self, direction):
        update = {'up' : (self._pos[0], self._pos[1] + self._speed),
                  'down' : (self._pos[0], self._pos[1] - self._speed),
                  'left' : (self._pos[0] - self._speed, self._pos[1]),
                  'right' : (self._pos[0] + self._speed, self._pos[1])}
        self._pos = update[direction]
        
    def tell_name(self):
        print(f"My name is {self._name}")
```
The first method `__init__()` is special. This is called during object instantiation.
This method is called to instantialise the instantiation.

The object creation happens by doing the following:
```py
# Object Instantiation
my_robot = RobotTurtle("T1")
```
This is object instantiation.
Python instantiates an object of type `RobotTurtle` in memory.
Note:
- Object is instantiated by using classname and some values. This object points to the variable `my_robot`
- Arguments in instantiation passed into `__init__()` method.
- First argument of any method in a class is always called `self` following Python's [PEP8](https://www.python.org/dev/peps/pep-0008/). Refers to the particular object instance of the class. Can be used to access methods and attributes of the current object.

Once instantiated, we can access its attributes and methods.
```py
# Accessing object's method
my_robot.tell_name()
```
> My name is T1

This is the **dot operator***.

You can actually access the attributes directly and change it:
```py
# accessing object's attribute
print(my_robot._speed)
my_robot._speed = 2
print(my_robot._speed)
```
>1
>2
More examples:
```py
my_robot = RobotTurtle("T2", 2)

print(f'Robot {my_robot._name} initially at {my_robot._pos}')
for _ in range(4):
    my_robot.move('up')
    print(f'Robot {my_robot._name} now at {my_robot._pos}')
    my_robot.move('right')
    print(f'Robot {my_robot._name} now at {my_robot._pos}')
```
> Robot T2 initially at (0, 0)
Robot T2 now at (0, 2)
Robot T2 now at (2, 2)
Robot T2 now at (2, 4)
Robot T2 now at (4, 4)
Robot T2 now at (4, 6)
Robot T2 now at (6, 6)
Robot T2 now at (6, 8)
Robot T2 now at (8, 8)

We don't use the iteration variable so we make use of `_`.

## Encapsulation and Properties
Encapsulation: the idea that data should be bundled together with some methods to access it.
The data itself should be hidden from those outside of the object.
If anyone would like to change the state of the object or enquire about it, it has to do so using some **methods**.

One purpose of encapsulation is to make the object **transparent**.
Anyone working with the object does not need to know how the state or the data inside the object is implemented.

```py
my_robot._pos = "This is not supposed to be allowed"
print(my_robot._pos)
```
This is not supposed to be allowed
If it is allowed, then our `move()` method will produce an error.
```py
my_robot.move("up")
```
> TypeError                                 Traceback (most recent call last)
> <ipython-input-16-5345a1aa5909> in <module>
> ----> 1 my_robot.move("up")
> 
><ipython-input-10-012bc05876e6> in move(self, direction)
> 9     # Methods:
> 10     def move(self, direction):
> ---> 11 update = {'up' : (self._pos[0], self._pos[1] + self._speed), 12                   'down' : (self._pos[0], self._pos[1] - self._speed),
> 13                   'left' : (self._pos[0] - self._speed, self._pos[1]),
> 
> TypeError: can only concatenate str (not "int") to str
	
Therefore we do encapsulation to ensure any kind of access to the data should be done through specific methods.
There are 2 kinds of methods for this purpose:
- enquiry or getter
- modifier or setter

Do this in Python using the concept of **property**.
A **property** represents an attribute with its *getter* and *setter*.
	
Rewrite the class using property. Create 2 properties, one for `name` and another for `speed`.
Create another property for position only with a getter, so position can only be modified by calling the `move()` method.
```py
# Class definition
class RobotTurtle:
    # Attributes:
    def __init__(self, name, speed=1):
        self.name = name
        self.speed = speed
        self._pos = (0, 0)
        
    # property getter
    @property
    def name(self):
        return self._name
    
    # property setter
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value != "":
            self._name = value
            
    # property getter
    @property
    def speed(self):
        return self._speed
    
    # property setter
    @speed.setter
    def speed(self, value):
        if isinstance(value, int) and value > 0:
            self._speed = value

    # property getter
    @property
    def pos(self):
        return self._pos
    
    # Methods:
    def move(self, direction):
        update = {'up' : (self.pos[0], self.pos[1] + self.speed),
                  'down' : (self.pos[0], self.pos[1] - self.speed),
                  'left' : (self.pos[0] - self.speed, self.pos[1]),
                  'right' : (self.pos[0] + self.speed, self.pos[1])}
        self._pos = update[direction]

        
    def tell_name(self):
        print(f"My name is {self.name}")
```
The `@property` syntax is called a **decorator**. It allows you to modify the function defined in the line just after it.
The setter for `name` above will be called in the `__init__()` since the argument is assigned to the **property** `name` and not to the **attribute** `_name`, i.e. `self.name = name`.
So only certain types can be assigned to the attribute `_speed` and `_name`.

To use the properties,
```py
# this is to create a new object with property, make sure you run the cell with the class definition first
my_robot = RobotTurtle("T4")
```
```py
# enquire name and speed
print(my_robot.name)
print(my_robot.speed)
```
> T4
> 1

Notice that you use te property name, which are `name` and `speed` respectively instead of the attribute names `_name` and `_speed`.
This access calls the **getter** method of the respective properties.
```py
my_robot.name = "T4new"
print(my_robot.name)
my_robot.name = ""
print(my_robot.name)
```
> T4new
> T4new

This is how to change the value using the assignment operator which will call the **setter** method.

Notice we do ot have a setter method for position. The reason is we always want position tostart from (0, 0), and it can only change its position through the method `move()`.
Note we are using a **single leading underscore** as a convention for people not to touch it. We can still enquire the position using the property getter.

In Python it is a convention when you use a single leading underscore, people should not touch it directly. On the other hand, one can also use double leading underscores.
This allows [Name Mangling](https://stackoverflow.com/questions/7456807/python-name-mangling) that prevents accidental overloading of methods and name conflicts when you extend a class.
So:
- When in doubt, leave it public. We should not add anything to obscur the name of your class attribute.
- If you really want to send the message "Don't touch this" to your users, the usual way is to precede the variable with one underscore.
- The double underscore magic is mainly to avoid accidental overloading of methods and name conflicts with superclasses' attributes. It can be quite useful if you write a class that is expected to be extended many times.

## Computed Property
Both `name` and `speed` are what is commonly called **stored** properties.
For each stored property, there is a corresponding attribute.
We can also create what is called a **computed** property.
A computed property retrieves its value from soem other attribute and does not have a setter.

To illustrate, let's create a new object called `Coordinate`.
```py
import math
class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    @property
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
```
There is a compound property named `distance`. 

So when do we use a method that returns a value and when to use a computed property. Here are some considerations.
- A method can have arguments. This means that if your returned value requires some input other than the attributes, you must use a method rather than a computed property.
- A method describes an action. If the code performs some actions and returns the output of that action, then a method is more suitable.
* Use a computed property when it describes some intrinsic quality of the object. It is a noun.
* Use computed property when it is simple and cheap. Prefer it for simple values that can be obtained by simple calculation.
* Use computed property when it can be computed with only the attributes.

## Composition
An object can be composed of other objects.
Here `RobotTurtle` can be composed of a `Coordinate`.
```py
# Class definition
class RobotTurtle:
    # Attributes:
    def __init__(self, name, speed=1):
        self.name = name
        self.speed = speed
        self._pos = Coordinate(0, 0)
        
    # property getter
    @property
    def name(self):
        return self._name
    
    # property setter
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value != "":
            self._name = value
            
    # property getter
    @property
    def speed(self):
        return self._speed
    
    # property setter
    @speed.setter
    def speed(self, value):
        if isinstance(value, int) and value > 0:
            self._speed = value

    # property getter
    @property
    def pos(self):
        return self._pos
    
    # Methods:
    def move(self, direction):
        update = {'up' : Coordinate(self.pos.x, self.pos.y + self.speed),
                  'down' : Coordinate(self.pos.x, self.pos.y - self.speed),
                  'left' : Coordinate(self.pos.x - self.speed, self.pos.y),
                  'right' : Coordinate(self.pos.x + self.speed, self.pos.y)}
        self._pos = update[direction]

        
    def tell_name(self):
        print(f"My name is {self.name}")
```
So now we can use dot operator instead of indices.
This is a much clearer read.

## Special Methods
Some methods' names in Python can be overriden. One example is `__init__()` method, called during object instantiation.
There are other special methods, but for now we introduce some more, which is the `__str__()` method.
This method is called when Python tries to convert the object to a `str` object. One common instance is when you print it.
```py
p1 = Coordinate(2, 3)
print(p1)
```
> <__main__.Coordinate object at 0x7fc9e077df90>

Let's override the `__str__()` method.
```py
import math
class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    @property
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
```
Now we can print a `Coordinate` object.
```py
p1 = Coordinate(2, 3)
print(p1)
```
> (2, 3)

# UML Diagram
UML stands for *Unified Modeling Language* and it gives some specifications how to represent the classes visually.
![[Pasted image 20211226140252.png]]
The UML Class diagram consists of:
- Class name
- Properties and attributes
- Methods

Sometimes is useful to identify the property's type inside.

UML diagram allows us to specify the relationship between different classes. For example:
![[Pasted image 20211226140604.png]]
This is a specific kind of _association_ relationship called **composition**. This means that `RobotTurtle` is composed of a `Coordinate`. When the object `RobotTurtle` is destroyed, the `Coordinate` object associated with it is also destroyed. There are other kinds of relationship which we will introduce along the way.
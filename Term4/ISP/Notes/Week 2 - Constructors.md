---
tags: #50.001
---
[[IS & Programming|ISP]]
# Constructors
- Special kind of methods that are invoked to create a new object (create an instance, or instantiation)
```java
Circle() {

}
Circle(double newRadius) {
	radius = newRadius;
}
//method overloading:
// same method name, different argument list
```
**No-arg constructor**: constructor without parameter
Constructor must have same name as the class itself.
- No return type, not even void
Invoked with the `new` operator, play the role of initializing objects

## Creating objects using constructors / instantiation
```java
new ClassName();
```
## Default Constructor
A class can be defined without constructors.
In this case, a no-arg constructor with an empty body is implicitly declared in the class.
This constructor, called a **default constructor**, is provided automatically only if ==no constructors are explicitly defined in the class==.

## [[Chap 9 - Objects and Classes]]
A constructor is invoked to create an object using the new operator. 
Constructors are a special kind of method. 
They have three peculiarities: 
- A constructor must have the same name as the class itself.
- Constructors do not have a return type—not even void. 
- Constructors are invoked using the new operator when an object is created. Constructors play the role of initializing objects.

The constructor has exactly the same name as its defining class. Like regular methods, constructors can be [[Method Overloading & Overriding|overloaded]] (i.e., multiple constructors can have the same name but different signatures), making it easy to construct objects with different initial data values. It is a common mistake to put the `void` keyword in front of a constructor.

Constructors are used to construct objects. To construct an object from a class, invoke a constructor of the class using the new operator, as follows: 
```java
new ClassName(arguments);
```
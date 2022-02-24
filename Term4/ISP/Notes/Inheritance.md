---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Object Oriented Programming|OOP]]
[[Week 2 - OOP and Classes]]
[[Inheritance and Abstract Base Class]]

## Motivations
Define classes for objects with common features, properties, behaviours.
What is the best software design to avoid redundancy?

> Inheritance
> - Programming construct to allow inheriting code from one class (superclass) to another class (subclass)
> - Enables you to defined a general class (superclass) and later extend it to more specialised classes (subclass)

## Superclasses and Subclasses
Use keyword `extends`
Subclass inherits all accessible data fields and methods from the superclass, except constructors.

In a subclass inherited from a supercalss, you can
- add new properties
- add new methods
- override the methods of the superclass

- A subclass is not a subset of its superclass; often a subclass contains more information and methods than its superclass
- Inheritance is used to mode is-a relationship
- Java only allows single inheritance:
	- A java subclass inherits only one superclass
	- (multiple inheritance can be achieved through interface)

## Advantage of inheritance
- Avoid redundancy
	- Different classes may have common properties and behaviours
- Easy to maintain
- Easy to comprehend
	- Class relationship documented in the inheritance tree

## super
Superclass's constructors are not inherited.
They are invoked explicitly using `super` keyword.
If the keyword `super` us not explicitly used, the superclass' no-arg constructor is automatially invoked.

### To call a superclass constructor
- Use `super()` to call the superclass constructor
- Invoking the superclass constructor's name causes a syntax error
- `super` needs to appear first in the constructor
- Call to constructors (`this()`/`super()`) must be the first statement in the constructor
- Keyword `super` can also be used to call a superclass method (aren't they inherited? why need this?)

## Superclass' constructor is always invoked
A constructor may invoke an overloaded constructor or its superclass cosntructor.
If neither is invoked explicitly, the compiler puts `super()` as the first statement in the constructor

## Constructor Chaining
Constructing an instance of a class invokes all the superclass's constructors along the inheritance chain.
## Subclass
In a subclass inherited from a superclass, you can
- add new properties
- add new methods
- override methods of superclass
## Overriding methods
Sometimes it is necessary for the subclass to modify the implementation of a method defined in the superclass
```java
public class Circle extends GeometricObject {
	// Other methods are omitted

	/** Override the toString method defined in GeometricObject */
	public String toString() {
		return super.toString() + "\nradius is " + radius;
	}
}
```
An instance method can be overriden only if it is accessible:
Private methods cannot be overriden because it is not accessible outside its own class.
If a method defined is private in its superclass, the two methods are completely unrelated.

You can only override instance methods. You can hide instance attributes / static methods / static attributes (overriding vs hiding)

## java.lang.Object
Every class is descended from `java.lang.Object`
If no inheritance is specified, the superclass of the class is `Object`
Inherited methods from Object, e.g. `toString()`

```java
public class Circle {
...
}

// is equivalent to
public class Circle extends Object {
...
}
```

---
tags: #50.001
---
[[IS & Programming|ISP]]

# Object-Oriented Programming
- OOP: Porgramming using objects
	- VS *procedural programming* (step by step statements, procedure call)
	- **Program: interaction between objects
	- Abstraction, encapsulation, inheritance, polymorphism
- Enable development of large-scale software
- Object represents an entity in the real world
- An object has a unique identity, state, behaviours
	- State / data fields / properties / attributes
	- Behaviour / methods / action
## Why
OO problem solving (abstraction, encapsulation, etc) is fundamental in engineering.
E.g. Assemble your own computer:
- Put the components together, it would work
- No need to worry about the details of components
- Details of the components are encapsulated
- Need to ensure correct interface
## Objects
An object has both state and behaviour.
### Class Template
```
Class Name: Circle

Data Fields:
	radius is ____

Methods:
	getArea
```
### Instantiated objects
```
Circle Object1

Data Fields:
	radius is 1
```
## Classes
- Objects of the same type are defined by Class
- A class is a template / contract that defines the object's data fields and methods
- An object is an instance of a class
- Java variables: data fields
- Java methods: behaviours
- Constructors: special types of methods, invoked to construct objects from classes
```java
class Circle {
	double radius = 1.0; //data field

	Circle() { //constructor
	}
	Circle(double newRadius) { //constructor
	}

	double getArea() { //method
		return radius * radius * Math.PI;
	}
}
```
```java
public class MyClass {
	public static void main(String[] args) {
		Circle c = new Circle();
		System.out.println(c.getArea());
	}
}
```
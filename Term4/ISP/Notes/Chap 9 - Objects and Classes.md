---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 9.1 Introduction
[[Week 2 - OOP and Classes]]
[[Object Oriented Programming|OOP]]
Object-oriented programming enables you to develop large-scale software and GUIs effectively.

## 9.2 Defining Classes for Objects
A class defines the properties and behaviors for objects.
![[Pasted image 20220318104133.png]]
![[Pasted image 20220318104140.png]]
![[Pasted image 20220318104153.png]]

## 9.3 Example: Defining Classes and Creating Objects
Classes are definitions for objects and objects are created from classes.
![[Pasted image 20220318105157.png]]

## 9.4 Constructing Objects Using Constructors
[[Week 2 - Constructors]]
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

## 9.5 Accessing Objects via Reference Variables
An object’s data and methods can be accessed through the dot (.) operator via the object’s reference variable.

Objects are accessed via the object’s reference variables, which contain references to the objects. Such variables are declared using the following syntax:
`ClassName objectRefVar;`

A class is essentially a programmer-defined type. A class is a reference type. A variable of the class type can reference an instance of the class.

![[Pasted image 20220318112539.png]]
![[Pasted image 20220318113122.png]]
![[Pasted image 20220318113146.png]]

## 9.6 UsingClasses from the Java library
![[Pasted image 20220318113215.png]]
![[Pasted image 20220318113226.png]]
![[Pasted image 20220318113244.png]]
![[Pasted image 20220318113306.png]]

## 9.7 Static Variables, Constants, and Methods
[[Week 2 - Instance and static variables or methods]]
A static variable is shared by all objects of the class. A static method cannot access instance members of the class. If you want all the instances of a class to share data, use static variables, also known as class variables. Static variables store values for the variables in a common memory location.
![[Pasted image 20220318115451.png]]

## 9.8 Visibility Modifiers

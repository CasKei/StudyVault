---
tags: #50.001
---
[[IS & Programming|ISP]]

> An object of a subtype can be used wherever its supertype value is required.

## Dynamic Binding
Which implementation is used will be determined dynamically by the JVM at runtime.

Every instance of a subclass is also a instance of its superclass, but not vice versa
![[Pasted image 20220212105131.png]]

## Casting Object
Casting can be used to convert an object of one class type to another within an inheritance hierarchy. 
In the preceding section, the statement
`m(new Student());`
assigns the object `new Student()` to a parameter of the `Object` type.

This statement is equivalent to
`Object o = new Student();//implicit casting
`m(o);`

## Down-Casting
> Casting from superclass to subclass

Explicit casting must be used when casting an object from a superclass to a subclass. 
This type of casting may not always succeed
`Object y = new Circle();
`Circle x = (Circle)y;`

(Declared type vs Actual type)

## The instanceof Operator
Use the `instanceof` operator to test whether an object is an instance of a class
```java
Object myObject = new Circle();
...//some lines of code
/** Perform casting if myObject is an instance of Circle */
if (myOject instanceof Circle) {
	System.out.println("Diameter is " + ((Circle)myObject).getDiameter());
}

```

## The protected Modifier
Con be applied on data and methods in a class.
A protected data or method in a `public` class can be accessed b any class inthe same package or its subclasses, even if the subclasses are in a different package
`private`, `default`, `protected`, `public`

## Visibility Modifiers
![[Pasted image 20220212105857.png]]
![[Pasted image 20220212105910.png]]

## A subclass Cannot Weaken the Accessibility
A subclass may override a protected method in its superclass and change its visibility to `public`.
However, a subclass cannot weaken the accessibility of a method defined in the superclass.
For example, if a method is defined as `public` in the superclass, it must be defined as `public` in the subclass
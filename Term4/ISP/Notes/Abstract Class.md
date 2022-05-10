---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Inheritance and Abstract Base Class]]

## What
A class declared as `abstract` cannot be instantiated.

Typically, abstract classes have abstract methods, which is a *method signature* that includes the keyword `abstract`.

## Why
Define reused methods in an abstract class and provide their concrete implementation in the concrete subclass.

- What is to be done: is specified by the abstract methods (and [[Interfaces]] too)
- How it is to be done: is specified by their implementation

As abstract classes can behave like a datatype, it promotes *code reuse*.

## Principle: Program to a supertype
You may write methods that take in an abstract class as an input, and you are guaranteed that objects passed to it will have the abstract method implemented. (this also applies to [[Interfaces]])

## Example
```java
public abstract class GeometricObject {
	private String color;
	protected GeometricObject() {
		this.color = "yellow";
	}
	protected GeometricObject(String color) {
		this.color = color;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color;
	}
	public abstract double getArea();
}
```

## Properties
- **Cannot create instance** of abstract class using the `new` operator
- An abstract method is **defined without implementation**
- Implementation is provided by subclass
- A class that contains abstract methods must be defined as an abstract class
- Practical advantage: generic programming

## Generic Programming Example using Abstract Class
```java
public class TestGeoObject {
	public static boolean equalArea(GeometricObject o1, GeometricObject o2) {
		return o1.getArea() == o2.getArea();
	}

	public static void main (String[] args) {
		Circle c = new Circle();
		Rect r = new Rect();
		System.out.println(equalArea(r, c));
	}
}
```

## Constructors in Abstract Classes
Your abstract class can have [[Week 2 - Constructors|constructors]] specified.
One use case is if you would like to force the initialisation of any instance variables.

Remember: constructors are not [[Inheritance|inherited]].

Thus, in the constructor of the child classes, you will need to call the superclass constructor using the `super()` keyword.

To use an abstract class, sub-class it and implement any abstract methods.

## Examples
```java
abstract class Foo {
	int x = 0; // can specify instance var
	abstract void f() {System.out.println(x)} // error: cannot implement method
	void g(); // error: cannot create method (need abstract)
	abstract void h(); // no error
}
```

```java
public class TestAbstract {
	public static void main(String[] args) {
		Feline tora = new Tiger("Tiger", "Sumatran Tiger");
		makeSound(tora);
	}
	public static void makeSound(Feline feline) {
		feline.sound();
	}
}
```
```java
abstract class Feline {
	private String name;
	private String breed;

	public Feline(String name, String breed) {
		this.name = name;
		this.breed = breed;	
	}
	public String getName() {
		return name;	
	}
	public String getBreed() {
		return breed;
	}

	public abstract void sound();
}
```
```java
class Tiger extends Feline {
	//write the constructor and complete the class
	// must implement Feline.sound()
	//Implicit super Feline() is undefined, must define explict constructor
	public Tiger(String name, String breed) {
		super(name, breed);
	}

	@Override
	public void sound() {
		System.out.println("Rawrrr!");
	}
}
```

See also: [[Interfaces]]
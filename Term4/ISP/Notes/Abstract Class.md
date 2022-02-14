---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Inheritance and Abstract Base Class]]

## Why
Define reused methods in an abstract class and provide their concrete implementation in the concrete subclass

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
- Cannot create instance of abstract class using te `new` operator
- An abstract method is defind without implementation
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
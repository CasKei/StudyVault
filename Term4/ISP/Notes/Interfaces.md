---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W4]]

## Interface
> Interface is a **class-like** programming construct that contains only **constants** and **abstract methods**.

Similar to [[abstract class]] in many ways.

Intent is to **specify common behaviour/characteristics of objects** of related classes or unrelated classes, e.g. comparable, eatable, etc

2 common types: [[#Comparable Interface]] and [[#Comparator Interface]].

## Example
```java
public interface Eatable {
	public abstract String howToEat();
}

class Animal {
}
class Chicken extends Animal implements Eatable {
	public String howToEat() {
		return "chicken: fry it";
	}
}
class Dog extends Animal {
}
class Chocolate implements Eatable {
	public String howToEat() {
		return "chocolare: eat everyday";
	}
}
```

## Omittable modifiers
![[Pasted image 20220212112504.png]]

## Comparable Interface
`Comparable` object is capable of comparing itself with another object.
Class itself must implement the `java.lang.Comparable` interface to compare its instances.
Implement this interface and override the `compareTo()` method.

- Suppose you want to design a generic method to sort the objects of the same type: `circles,rectangles, students, fruits`
- We need common behavior for the objects: `comparable`
- Java provide the `Comparable` interface for this purpose
- Classes that implement the `Comparable` interface become comparable

```java
public interface Comparable<E> {
	public abstractintcompareTo(E o);
}
```
```java
class Circle extends GeometricObject implements Comparable<Circle> {
	private double radius = 1;
	Circle() {
	}
	Circle(double radius) {
		this.radius = radius;
	}
	public int compareTo(Circle c) {
		if (this.radius > c.radius) {
			return 1;
		} else if (this.radius == c.radius) {
			return 0;
		} else {
			return -1;
		}
	}
}
```

- Implements `Comparable<E>`: provides implementation for the abstract method `public int compareTo(E o)`
- Comparable interface is a generic interface,the generic type `E` is replaced by a `concrete` type when implementing the interface
- Classes `Integer`, `String`, `Date`, etc all implement `Comparable`, thus they are comparable

![[Pasted image 20220212112854.png]]
<br>
## Comparator Interface
`Comparator` is external to the element type we are comparing.
It is a separate class.
We create multiple separate classes that implement `Comparator` to compare by different members.
`Collections` class has a second `sort()` method and it takes `Comparator`.
The `sort()` method invokes the `compare()` method to sort objects.

Used to:
- Provide additional way of ordering
	- `Comparable<E>.compareTo()`: defines the 'natural' ordering for `E`
	- `Comparator<E>.compare()`: defines additional, alternative ordering for `E`
- Enables comparison for objects which their classes do not implement `Comparable`.

### Example: allow Integer to be ordered based on absolute value
To use this:
- Create a class that implements `Comparator`.
- Make an instance of the `Comparator` class.
- Call the overloaded `sort()` method, giving it both the list and the instance of the class that implements `Comparator`.
```java
public class IntegerAbsComparator implements Comparator<Integer> {
	public int compare(Integer a, Integer b) {
		if (Math.abs(a) > Math.abs(b)) {
			return 1;
		} else if (Math.abs(a) == Math.abs(b)) {
			return 0;
		} else {
			return -1;
		}
	}
	// Code skip
	Collections.sort(I, new IntegerAbsComparator());
}
```

## Comparable VS Comparator
| [[#Comparable Interface]]                                                                                | [[#Comparator Interface]]                                                                                             |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Provides a single sorting sequence. Can sort the collection on the basis of a single element such as id. | Provides multiple sorting sequences. Can sort the collection based on the basis of multiple elements such as id, etc. |
| Affects the original class: actual class is modified.                                                    | Does not affect original class.                                                                                       |
| Provides `compareTo()` method to sort elements                                                           | Provides `compare()` method to sort elements.                                                                         |
| Present in `java.lang` package.                                                                          | Present in `java.util` package                                                                                        |
| We can sort the list elements of `Comparable` type by `Collections.sort(List)` method.                   | We can sort the list elements of `Comparator` type by `Collections.sort(List, Comparator)` method.                                                                                                                      |

## [[Abstract Class]] VS [[Interfaces]]
![[Pasted image 20220212113032.png]]
![[Pasted image 20220212113044.png]]
![[Pasted image 20220212113056.png]]



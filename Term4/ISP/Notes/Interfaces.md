---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W4]]

## Interface
> Interface is a class-like programming construct that contains only constants and abstract methods

Similar to abstract class in many ways.

Intent is to specify common behaviour / characteristics of objects of related classes or unrelated classes, e.g. comparable, eatable, etc

## Example
![[Pasted image 20220212112441.png]]
## Omittable modifiers
![[Pasted image 20220212112504.png]]

## Comparable Interface
- Suppose you want to design a generic method to sort the objects of the same type: `circles,rectangles, students, fruits`
- We need common behavior for the objects: `comparable`
- Java provide the `Comparable` interface for this purpose
- Classes that implement the `Comparable` interface become comparable

```java
public interface Comparable<E> {
	public abstractintcompareTo(E o);
}
```
![[Pasted image 20220212112657.png]]

- Implements `Comparable<E>`: provides implementation for the abstract method `public int compareTo(E o)`
- Comparable interface is a generic interface,the generic type `E` is replaced by a `concrete` type when implementing the interface
- Classes `Integer`, `String`, `Date`, etc all implement `Comparable`, thus they are comparable

![[Pasted image 20220212112854.png]]

![[Pasted image 20220212112924.png]]

![[Pasted image 20220212112952.png]]

## [[Abstract Class]] VS [[Interfaces]]
![[Pasted image 20220212113032.png]]
![[Pasted image 20220212113044.png]]
![[Pasted image 20220212113056.png]]

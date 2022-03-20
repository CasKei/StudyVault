---
tags: #50.001
---
[[IS & Programming|ISP]]

## ArrayList
[[Week 1 - ArrayList, LinkedList, Generics]]
```java
List<Integer> a = new ArrayList<>();
a.add(1);
a.add(2);
a.add(1, 3); // add 3 in the position of 1
a.add(5);
System.out.println(a.toString());
```
> [1, 3, 2, 5]

## Private vs Public
[[Week 2 - Encapsulation]]
```java
class Point2D{  
	private double x;  
	private double y;  
  
	Point2D(){ //code not shown  
	}  
  
	Point2D(double x, double y){  
		this.x = x; this.y = y;  
	} 
	/** you don't need this.x because as long as there is no static keyword it refers to the instance. method is a instance method, not a class method.*/
	public double getX() {  
		return x;
	} 
	public double getY() {  
		return y;  
	}
}  
class Point3D extends Point2D{  
	private double z;  
	Point3D( double x, double y, double z ){  
		super(x,y);
		this.z = z; 
	} 
	public double getZ() {  
		return this.z;  
	}
}
```
`Point3D` cannot get x and y directly as they are private attributes. Cannot set or get them from `Point3D`. But you can use `getX()` and `getY` as they are public.

## Polymorphism
[[Polymorphism]]
3 types of polymorphism:
1. Subtype polymorphism: overriding
2. Ad Hoc polymorphism: overloading
3. Parametric polymorphism: generics

### Subtype polymorphism: overriding
[[Method Overloading & Overriding]]

Allows variables of a subclass to be used in the context where a superclass is expected.
```java
abstract class Dog {
	public void bark() {System.out.println("woof");}
	public void drool() {System.out.println("drool");}
}

class Hound extends Dog {
	public void sniff() { System.out.println("sniff ");}
	@Override
	public void bark() { System.out.println("growl");}
	public void drool(int time) { System.out.println("drool" + time);}
}
```
Given `Dog g = new Hound();`:
- `g.bark()`:  We are upcasting this object into the superclass. We are calling the child method because of `@Override`, so it returns `"growl"`
- `g.drool(1)`: compile error. You are expecting a drool method from Dog class that takes in an integer. We have upcasted `g` into a `Dog` class, so this cannot work.
- `g.drool()`: `"drool"`
- `g.sniff()`: compile error. Upcasted to `Dog` class. But `Dog` does not have sniff method.
  
`g` is referencing `Hound` object, but can be declared as an instance of the `Dog` class.
*Upcasting*: putting an object of the subtype in the context of the superclass. Does not override behaviours in the object.

To **override** a method in a super-class, the method signature must be the same.
The `@Override` annotation allows the compiler to help you check if you have this condition correct.
The methods available depends on the declared type.
If a method is overriden in the subclass, in *dynamic binding*, the JVM decides which method to invoke, starting from the actual type.
```java
class A {
	void f(int x) {
		System.out.println("Af");
	}
	void h(int x) {
		System.out.println("Ah");
	}
}
class B extends A {
	void f(int x) {
		System.out.println("Bf");
	}
	void g(int x) {
		System.out.println("Bg");
	}
}
```
Given `A x = new B();`
- `x.f(1)`: visible in A so this is fine
- `x.g(1)`: not visible in A, not possible
- `x.h(1)`: visible in A so this is fine

- By making use of the subtyping and inheritance
- Code for the super class is unchanged
- Requires overriding methods

### Ad Hoc polymorphism: overloading
[[Method Overloading & Overriding]]
**Overloading** allows a single method name to be shared across different implementations with different types of input parameters. Java run-time decides which particular implementation to be called based on the actual argument type.
```java
public void log(int x) {
	System.out.println(x.toString());
}
public void log(String s){
	System.outprintln(s);
}
```

- By reusing the same method name for different implementation given different input arguments

### Parametric polymorphism: Generics
[[Week 1 - ArrayList, LinkedList, Generics]]
**Generics** are type parameters, often used in augmenting some type constructors, e.g. `ArrayList<>`, `Optional<>`...

In the following the implementations of `getFirst()`, `setFirst()`, `getSecond()`, `setSecond()` and `swap()` are independent of what `T` and `S` are.

```java
import java.util.List;
import java.util.ArrayList;
public class Pair<T, S> {
	private T first;
	private S second;

	public Pair(T first, S second) {
		this.first = first;
		this.second = second;
	}
	public T getFirst() {
		return this.first;
	}
	public void setFirst(T, f) {
		this.first = f;
	}
	public S getSecond() {
		return this.second;
	}
	public void setSecond(S s) {
		this.second = s;
	}
	public Pair<S, T> swap() {
		return new Pair<S, T>(this.second, this.first);
	}

	public static void main(String[] args){
		Pair<Integer, String> p1 = new Pair<>(1, "hello");
		Pair<String, List<Integer>> p2 = new Pair<String, List<Integer>>("numbers", new ArrayList<>());
		System.out.println(p1.second);
		System.out.println(p2.first);
	}
}
```

- Makes underlying type into a type parameter
- One and only one piece of code shared by multiple instances of types

## Interface
[[Interfaces]]
Like a contract for the implementation of classes. Acts as a supertype for all classes that implement it.
```java
interface I {
	void m(int x);
}
class K implements I {
	void m(int x) {
		System.out.println("m");
	}
}
```
Which are legal?
- `K x = new K();` Yes
- `K x new I();` No
- `I x = new K();` Yes
- `I x = new I();` No


Interfaces help in the maintenance of software.\
Which method is better?
```java
void firstMethod(K k) {
	// code;
}
void secondMethod(I i) {
	// code;
}
```
A method that takes in an *interface* is *more flexible*.\
It will be able to *accept any object that implements that interface*.\
Suppose you create a new class implementing an interface that has a better implementation of `m`, you are able to pass it to this method implementing the interface without having to change its signature.

All method signatures in interfaces are **automatically abstract**. You do not have to specify the keyword.
```java
interface Pokemon {
	void adjustCP(int value);
	void attack();
	void defend();
}

class Bulbasaur implements Pokemon {
	void adjustCP() {
		// code not shown
	}
	void attack() {
		// code not shown
	}
}
```
Which methods does `Bulbasaur` still need to implement?
- `defend()` and `adjustCP(int)`

*Similar* to [[Abstract Class]], [[Interfaces]] leaves the inplementation details to its sub-classes. In *contrast* to abstract class,
- All *methods* in interfaces are *abstract*
- A *class* can *extend multiple interfaces*

## Exceptions
[[Exception]]
```java
public class TestExceptions1 {
	public static void main(String[] args) {
		try {
			f(-1);
			System.out.print("R");
		} catch (Exception e) {
			System.out.print("S");
		}
	}

	static void f(int x) throws Exception {
		if (x < 0) throw new Exception();
		System.out.print("P");
	}
}
```
`S`

```java
public class TestExceptions1 {
	public static void main(String[] args) {
		try {
			f(-1);
			System.out.print("R");
		} catch (Exception e) {
			System.out.print("S");
		}
	}

	static void f(int x) throws Exception {
		try {
			if (x < 0) throw new Exception();
			System.out.print("P");
		} catch (Exception e) {
			System.out.print("Q");
		}
	
	}
}
```
`QR`

- When an **exception** is thrown, the Java runtime searches through the *call stack* to find the first method that will handle the exception.
- The `finally` block is always executed regardless of what happens in the `try` block.
- It is good practice to specify exactly the type of exception that is handled in each `catch` block, as you will have specific details of the exception that occurred. Hence the examples here are not good...
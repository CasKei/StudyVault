---
aliases: overloading, overriding
tags: #50.001
---
[[IS & Programming|ISP]]
[[Polymorphism]]

| Method Overloading                                                               | Method Overriding                                                                                                    |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| A compile-time [[Polymorphism]]                                                  | A run-time [[Polymorphism]]                                                                                          |
| Helps increase readability of program                                            | Used to grant the specific implementation of the method which is already provided by its parent class or superclass. |
| Occurs within the class                                                          | Performed in 2 classes with inheritance relationships                                                                |
| May or may not require inheritance                                               | Always needs inheritance                                                                                             |
| Methods must have the same name and different signatures                         | Methods must have the same name and same signature                                                                   |
| Return type can or can not be the same, but we just have to change the parameter | Return type must be the same or co-variant.                                                                          |
| The method to call is determined at complie-time.                                | Method call is determined at the runtime based on the object type                                                    |
| If break, compile-time error will come and its easy to fix                       | If break, can cause serious issues in program because the effect will be visible at runtime.                                                                                                                     |

## Example of Overloading
```java
import java.io.*;

class MethodOverloadingEx {

	static int add(int a, int b)
	{
	return a + b;
	}

	static int add(int a, int b, int c)
	{
		return a + b + c;
	}

	public static void main(String args[])
	{
		System.out.println("add() with 2 parameters");
		System.out.println(add(4, 6));
	
		System.out.println("add() with 3 parameters");
		System.out.println(add(4, 6, 7));
	}
}
```
```
add() with 2 parameters
10
add() with 3 parameters
17
```

## Example of Overriding
```java
import java.io.*;

class Animal {

	void eat()
	{
		System.out.println("eat() method of base class");
		System.out.println("eating.");
	}
}

class Dog extends Animal {

	void eat()
	{
		System.out.println("eat() method of derived class");
		System.out.println("Dog is eating.");
	}
}

class MethodOverridingEx {

	public static void main(String args[])
	{
		Dog d1 = new Dog();
		Animal a1 = new Animal();

		d1.eat();
		a1.eat();

		Animal animal = new Dog();
		// eat() method of animal class is overridden by
		// base class eat()
		animal.eat();
	}
}
```
```
eat() method of derived class
Dog is eating.
eat() method of base class
eating.
eat() method of derived class
Dog is eating.
```
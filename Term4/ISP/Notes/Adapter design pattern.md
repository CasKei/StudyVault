---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 4]]
[[W5|design pattern]]

## Adapter Design Pattern
The word [[Interfaces|interface]] is an [[Method Overloading & Overriding|overloaded]] word.
- A type of class with method signatures only
- The set of methods that a class allows you to access (think of 'user interface')

An adapter design pattern converts the interface of one class into another that a client class expects.

## Example
Have [[Interfaces|interface]] `Duck` and class `MallardDuck`
```java
public interface Duck {  
	void quack();  
	void fly();  
}
```
```java
public class MallardDuck implements Duck {  
	@Override  
	public void quack() {  
		System.out.println("Mallard Duck says Quack");  
	}  
	@Override  
	public void fly() {  
		System.out.println("Mallard Duck is flying");  
	}  
}
```

Then you have a **client** that loops through all ducks and makes them all fly and quack.
```java
import java.util.ArrayList;  
public class DuckClient {  
	static ArrayList<Duck> myDucks;  
	
	public static void main(String[] args){  
		myDucks = new ArrayList<>();  
		myDucks.add( new MallardDuck());  
		makeDucksFlyQuack();  
	}  
	
	static void makeDucksFlyQuack(){  
		for(Duck duck: myDucks){  
			duck.fly();  
			duck.quack();  
		}  
	}  
}
```

Now you have a `Turkey` [[Interfaces|interface]].
```java
public interface Turkey {  
	public void gobble();  
	public void fly();  
}
```

How might we allow `Turkey` objcts to be used by the same **client**?

Write an adapter class that
- has the same Duck interface
- takes in a Turkey object

```java
public class TurkeyAdapter implements Duck {  
	Turkey turkey;  
	TurkeyAdapter(Turkey turkey){  
		this.turkey = turkey;  
	}  

	@Override  
	public void quack() {  
		//implement this  
	}  

	@Override  
	public void fly() {  
		//implement this  
	}  
}
```
This material was taken from “HeadFirst-Design Patterns”
![[Pasted image 20220502201457.png]]

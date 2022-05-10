---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 4]]
[[W5|design pattern]]

## Strategy Design Pattern
In this design patter, parts ofthe behaviours of an object are handed over to other objects. This is known as [[Delegation]].
This provides flexibility at run-time as you can change those behaviours.

```java
public abstract class Duck {  
	private FlyBehavior flyBehavior;  
	private QuackBehavior quackBehavior;  
	String name;  

	public Duck(){  
	}  

	public Duck(String name){  
		this.name = name;  
	}  

	public void setFlyBehavior(FlyBehavior flyBehavior) {  
		this.flyBehavior = flyBehavior;  
	}  

	public void setQuackBehavior(QuackBehavior quackBehavior) {  
		this.quackBehavior = quackBehavior;  
	}  

	public void performFly(){  
		flyBehavior.fly();  
	}  

	public void performQuack(){  
		quackBehavior.quack();  
	}  

	public abstract void display();  
}
```

In the [[Abstract Class]] above, the [[Delegation]] happens as follows:
- The flying behaviour is delegated to a `FlyBehaviour` object
- The quacking behaviour is delegated to a `QuackBehaviour` object

For FlyBehavior, we implement different objects that represent different behaviour.
```java
interface FlyBehavior {  
	void fly();  
}
```
```java
class FlapWings implements FlyBehavior {  
	@Override  
	public void fly() {  
		System.out.println("Flapping my Wings");  
	}  
}
```

Implement a class `CannotFly` that implements `FlyBehavior`
The `fly()` method prints out `“I cannot fly :(“`

Similarly for `QuackBehaviour` objects
```java
public interface QuackBehavior {  
	void quack();  
}
```
```java
public class LoudQuack implements QuackBehavior {  
	@Override  
	public void quack() {  
		System.out.println("QUACK");  
	}  
}
```

Finally we subclass Duck with our own object
```java
public class MallardDuck extends Duck {  
	MallardDuck(String name){  
		super(name);  
	}  
	@Override  
	public void display() {  
		System.out.println("I am " + name + ", the Mallard Duck");  
	}  
}
```

And we can run our MallardDuck object and set their behaviours at run time.
```java
public class TestDuck {  
	public static void main(String[] args){  
		Duck duck = new MallardDuck("Donald");  
		duck.setFlyBehavior(new FlapWings());  
		duck.setQuackBehavior(new LoudQuack());  
		duck.display();  
		duck.performFly();  
		duck.performQuack();  
	}  
}
```

We see here the **flexibility of composition over [[Inheritance]]**.
We develop our duck behaviours independent of the type of duck.
The behaviur of the duck is [[Delegation|delegated]] to separate objects.
You assemble your specific duck at run-time, giving you the flexibility to change its behaviour if needed.

[[RecyclerView]]
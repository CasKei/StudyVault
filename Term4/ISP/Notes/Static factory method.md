---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Static Factory Method
**Static factory method**: a [[Week 2 - Instance and static variables or methods|static method]] in a class definition that returns an instance of that class.

You can [[Method Overloading & Overriding|overload]] your [[Week 2 - Constructors|constructor]] to initialise your class with different states, but you are constrained by Java to have the same name for all constructors.

OTOH, you can give your static factory method meaningful names to describe what you are doing.

The [[Week 2 - Constructors|constructor]] can be declared private, in which case your class can only be instantiated by calling the static factory methods.
Recall that in [[Singleton design pattern]] design pattern. there is one static method.
```java
public class Tea {
	private boolean sugar;
	private boolean milk;

	Tea(boolean sugar, boolean milk) {
		this.sugar = sugar;
		this.milk = milk;	
	}

	public static Tea teh() {
		return new Tea(true, true);	
	}
	public static Tea tehkosong() {
		return new Tea(false, true);	
	}
}
```
Hence you invoke the static factory method like this:
```java
Tea tea = Tea.tehkosong();
```
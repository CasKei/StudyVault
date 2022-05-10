---
tags: 50.001
---
[[IS & Programming|ISP]]

[[Android 1]]
## [[Week 2 - Instance and static variables or methods|Static]] Nested Classes
[[Static Nested Classes]]
By declaring a [[Nested class]] as static, it is known as **static nested class**.
- It can only access static variables and methods in the outer class
- It can only be instantiated without an instance of the outer class

A static nested class behaves like a **top-level class** and is a way to organise classes that are used only by some other classes.

==Activity==
- Modify **`OuterClass.java`** by declaring **`InnerClass`** as static and adjusting other parts of the class accordingly e.g. which other variables must be static? Which methods do not work anymore?
- Write code to show that you can instantiate **`OuterClass`** and **`InnerClass`** separately.


[[Android 4]]
Recall that a class definition can contain [[Nested class]]es.

```java
public class OuterClass {
	//code
	class InnerClass {
		//code
	}
}
```

This is typically done when you have classes that logically depend on the outer class and are used together with the outer class.

One reason for having a static nested class is to have a model class to store data.
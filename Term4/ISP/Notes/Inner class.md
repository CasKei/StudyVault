---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## Inner Class
[[Inner class]]
A nested class that is not declared static is called an **Inner Class**. 
- To instantiate an inner class, you need an instance of the outer class, which is usually called the **enclosing class**. 
- The inner class can access all methods and variables of the enclosing outer class.

```java
public class OuterClass {
	int a;
	OuterClass() { a = 10; }
	void outerPrintA() { System.out.println(a); }

	class InnerClass {
		int c;
		InnerClass() { c = 100; }
		void innerPrintA() { System.out.println(a); }
		OuterClass giveBackOuter() { return OuterClass.this; }
	}
}
```
==Activity==. For **OuterClass**, complete the main function below to illustrate the following properties.
```java
public class TestOuterClass {
	public static void main(String[] args) {
		// Instantiate OuterClass
		OuterClass outerClass = new OuterClass();
		//Instantiate InnerClass
		OuterClass.InnerClass innerClass = outerClass.new InnerClass();

		// Show that InnerClass can access variables in OuterClass
		
		// Show that InnerClass stores a reference to OuterClass
	
	}
}
```

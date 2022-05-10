---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## Nested Classes
[[Nested class]]
A class definition can contain class definitions. We call these classes nested classes

```java
public class OuterClass {
	// code not shown 
	class InnerClass{
	 //code not shown 
	} 
}
```
This is typically done when you have classes that logically depend on the outer class and are used together with the outer class.

[[Static Nested Classes]]

## Further Reading
- [Nested classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html)
- [Anonymous classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html)
- Bloch, Effective Java, Item 22.
---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

[[Nested interface]]
## Delegation
[[Delegation]]
We go back to the **Foo** class and notice that what happens when **thirsty()** is executed depends on objects implementing the **Foo.Bar** that are passed to it.

In other words, the behaviour of **thirsty()** is ***delegated*** to objects that implement **Foo.Bar**.

This illustrates 2 design principles:
- **Program to a supertype**
	- Because the input to *thirsty()* is an interface, it can accept any object that implements **Foo.Bar**
- **Favour composition over [[Inheritance]]**
	- Since *thirsty()* can accept any object that implements **Foo.Bar**, the objects of the **Foo** class become more flexible and its behaviour can change at runtime.

```java
public class Foo {
	interface Bar{
		void drink();
	}

	Foo() {
	}

	void thirsty(Bar bar) {
		bar.drink();
	}
}
```

[[Strategy design pattern]]
[[RecyclerView]]
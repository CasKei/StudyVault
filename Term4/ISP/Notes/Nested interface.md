---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## Nested [[Interfaces]]
[[Nested interface]]
Recall that [[Interfaces]] makes your code reusable. We may nest interfaces as well.\
Recall also that interfaces are inherently [[Week 2 - Instance and static variables or methods|static]].\
In the following code, any object that implements **Foo.Bar** interface can be passed to **thirsty()**.
```java
public class Foo {
	interface Bar {
		void drink();
	}

	Foo() {
	}

	void thirsty(Bar bar) {
		bar.drink();	
	}
}
```

The [[Inner class]] **C** implements **Foo.Bar** and an instance is passed to **thirsty()**. The inner class is declared **static** becaise it is invoked from **main()**.
```java
public class TestFoo {

	public static void main(String[] argv) {
		Foo f = new Foo();
		f.thirsty( new C() );
	}

	static class C implements Foo.Bar {
		@Override
		public void drink() {
			System.out.println("gulp");
		}
	}
}
```
[[Delegation]]

## Further Reading
- [Nested classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html)
- [Anonymous classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html)
- Bloch, Effective Java, Item 22.
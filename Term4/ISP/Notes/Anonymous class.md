---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## Anonymous Class
[[Anonymous class]]
Often, if the [[#Inner Class]] is only used once, an laternative is an **Anonymous Inner Class**, to avoid declaring too many classes. You may not want to have too many inner classes that are practically only used once.\
The following code shows how the **TestFoo** example above can be implemented using an anonymous inner class.
```java
public class TestFool {
	public static void main(String[] argv){
		Foo f = new Foo();
		f.thirsty( new Foo.Bar(){
			@Override
			public void drink() {
				System.out.println("Gulp");
			}
		});
	}
}
```
The **new** keyword is used to instantiate an object that implements **Foo.bar**. Because **Foo.Bar** is an interface, the implementation os then specified immediately.

As you can see, we have an **anonymous class** because
- We do not name the class that implements the [[Interfaces|interface]]
- We do not assign a variable name to the class that implements the interface

*We see nested interfaces, nester static classes and anonymous classes in Android programming frequently.*

## Further Reading
- [Nested classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html)
- [Anonymous classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html)
- Bloch, Effective Java, Item 22.
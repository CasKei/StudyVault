---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]
[[W5|design pattern]]

When we discussed the `Tea` class, we saw how [[Static factory method]]s can be used.
Let's expand the tea class to four options.
```java
public class TeaTwo {
	private boolean sugar;
	private boolean milk;
	private boolean ice;
	private boolean toGo;
	// code not shown
}
```
If you were to write a [[Week 2 - Constructors|constructor]] or [[Static factory method]] for each possible combination of options, how many constructors must you write?

We solve this by introducing a [[Week 2 - Instance and static variables or methods|static]] [[Android 1#Nested Classes|nested class]], usually called a **builder class**, that has
- methods to allow the user to specify the options one by one
- One method that returns the actual object

If constructor is *private* and *takes in an instance of the builder class*, then the only way to instantiate your object would be to use the biulder class.
```java
public class TeaTwo {
	private boolean sugar;
	private boolean milk;

	private TeaTwo(TeaBuilder teaBuilder) {
		this.sugar = teaBuilder.sugar;
		this.milk = teaBuilder.milk;
	}

	static class TeaBuilder {
		private boolean sugar;
		private boolean milk;

		TeaBuilder(){}

		public TeaBuilder setSugar(boolean sugar){
			this.sugar = sugar;
			return this;
		}
		public TeaBuilder setMilk(boolean mlik){
			this.milk = milk;
			return this;
		}
		public TeaTwo build() {
			return new TeaTwo(this);
		}
	}
}
```
The builder is then used as follows:
```java
TeaTwo teaTwo = new
TeaTwo.TeaBuilder().setSugar(true).setMilk(true).build();
```
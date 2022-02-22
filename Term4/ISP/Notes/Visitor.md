---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W5]]


## What is it
Useful if you need to perform operations across a diverse set of objects

GoF: "Allows for one or more operations to ba applied to a set of objects at runtime, decoupling the operations from the object structure."

Provide additional functionality to a class without changing it.

E.g. postage
Postage calculation depends on the type of item: e.g. books, CD, clothing
Also depends on where the item is sent to
*Given a list of items of variety types, determine the total postage cost*

***
## Non-Visitor Design
```java
public static double calPostage(ArrayList<Object> items) {
	double total = 0;
	for (Object o: items) {
		if (o instanceof Book) {
			...
		} else if (o instanceof CD) {
			...
		} else if (o instanceof Clothing) {
			...
		} else {
			throw new AssertionError("not supported");
		}
	}
	return total;
}
```
***
## Visitor Design Pattern
Visitor Design Pattern is a more [[Week 2 - OOP and Classes|OO]] way to perform operation on a list of items.
![[Pasted image 20220222100011.png]]

![[Pasted image 20220222100146.png]]
`Visitor` and `Visitable` are interfaces.
`ConcreteVisitor` implements `Visitor`
`Items` implement `Visitable`
***
## Code
```java
public interface Visitor {
	void visit(Book b);
	void visit(CD d);
	void visit(Clothing c);
}
```
```java
public interface Vistable {
	void accept(Visitor v);
}
```

```java
class Book implements Visitable {
	private double weight;
	public Book(double weight) {
		this.weight = weight;
	}
	public double getWeight() {
		return this.weight;
	}

	public void accept(Visitor v) {
		v.visit(this);
	}
}
class Clothing implements Visitable {
	private int size;
	public Clothing(int size) {
		this.size = size;
	}
	public int getSize() {
		return this.size;
	}
	public void accept(Visitor v) {
		v.visit(this);
	}
}
class CD implements Visitable {
	private String title;
	public CD(String title) {
		this.title = title;
	}
	public String getTitle() {
		return this.title;
	}
	public void accept(Visitor v) {
		v.visit(this);
	}
}
```

```java
public class PostageVisitor implements Visitor {
		
	private double total = 0;
	public double getTotal() {
		return total;
	}
	public void setTotal(double total) {
		this.total = total;
	}

	@Override
	public void visit(Book b) {
		total += b.getWeight() * 10;
	}
	@Override
	public void visit(CD d) {
		if (c.getTitle() == "BTS") {
			total += 10;
		} else {
			total += 1;
		}
	}
	@Override
	public void visit(Clothing c) {
		if (c.getSize() > 10) {
			total += 20;
		} else {
			total += 10;
		}
	}
}
```

```java
import java.util.ArrayList;

public class MyClass {
	public static void main(String[] args) {
		ArrayList<Visitable> items = new ArrayList<>();

		PostageVisitor postage = new PostageVisitor();

		items.add(new Book(1));
		items.add(new CD("BTS"));
		items.add(new Clothing(12));

		for (Visitable o: items) {
			o.accept(postage);
		}

		System.out.println(postage.getTotal());

		//you can create more lists of items
		// the visitor can visit different lists
		// reusable code.

		// create another Visitor if needed to customise more visit actions

	}
}
```
***
## Remarks
- Different visit method for different object types to be processed
- Use method [[Method Overloading & Overriding|overloading]] to pick the method for processing (instead of if-then-else)
- Concrete implementation of `Visitor` provides the specifis of what to do with differnet object types
- `Visitable` interface: allows the `Visitor` to be passed in
- `Item` implements `Visitable`:![[Pasted image 20220222111130.png]]
	- Simple by important change to make in the class variable: dispatch of visit depends on `this`
- ![[Pasted image 20220222111306.png]] `Visitor` `postage` visits each item one by one, processes them, information kept inside `Visitor`


## Advantage of Visitor
- Separate out certain logic from the items themselves, keeping item classes simple
	- Item class only needs to implement Visitable
- Add methods to classes: another concrete class implements Visitor
	- No need to change item classes
- Enable static checking: code cannot be compiled without the visit method of the corresponding type.
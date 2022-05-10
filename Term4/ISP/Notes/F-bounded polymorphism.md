---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 3]]
[[Polymorphism]]

Recall the `Pair` class
```java
public class Pair<T, S> {
	public T first;
	public S second;
	public Pair(T first, S second) {
		this.first = first;
		this.second = second;
	}
}
```

And the [[Interfaces#Comparable Interface|Comparable Interface]]
```java
interface Comparable<T> {
	int compareTo(T that);
}
```

Suppose we want to modify the Pair class such that when two Pair objects are compared, we compare the `first` items. *If tie*, then compare the `second` items.
However, this would imply that the [[ArrayList, LinkedList, Generics|generic]] T and S are *not as generic* as before.

```java
public class Pair<T extends Comparable<T>, S extends Comparable<S>> implements Comparable<Pair<T,S>> {
	public T first;
	public S second;
	public Pair(T first, S second) {
		this.first = first;
		this.second = second;
	}
	@Override
	public int compareTo(Pair<T,S> that) {
		int r1 = this.first.compareTo(that.first);
		if (r1 == 0) {
			return this.second.compareTo(that.second);	
		} else {
			return r1;
		}
	}
}
```
In the above type constraint  `T extends Comparable<T>` restricts the type variable `T` must be a subtype of `Comparable<T>`. These constraints provide hints to the compiler that it is safe to call `this.first.compareTo(that.first)`. This is known as F-bounded [[Polymorphism]].
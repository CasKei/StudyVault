---
tags: #50.001
---
[[IS & Programming|ISP]]
# Data Field Encapsulation
- Keep attributes private, if possible
- Use `get` method (getter/accessor) to return the values of attributes, e.g. `double getRadius()`
- Use `set` method (setter/mutator) to update attributes, e.g. `void setRadius(double radius)()`

Design principles:
- Minimize the accessibility of classes and members
- In public classes, use accessor (getter) methods, not public attributes

# Passing objects to methods
Java: only pass-by-value
Primitive type: value is passed
Reference type: value (reference to an object) is passed
```java
public static void printAreas(Circle c, int times) {
	times = 0;
	c.setRadius(100.0);
}
int n = 5;
Circle.myCircle = new Circle(2.0);
printAreas(myCircle, n);
```
![[Pasted image 20220128093312.png]]

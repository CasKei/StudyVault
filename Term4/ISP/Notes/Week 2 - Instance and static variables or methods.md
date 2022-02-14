---
tags: #50.001
---
[[IS & Programming|ISP]]
# Object Reference Variables
To reference an object, assign the object to a reference variable.
To declare a reference variable, use the syntax:
```java
ClassName objectRefVar;
```
Example:
```java
Circle myCircle;
```
Template:
```java
ClassName objectRefVar = new ClassName();
```
Example:
```java
Circle myCircle = new Circle();
```
LHS: declaration
RHS: instantiation

# Access object
## Referencing the object's data
```java
objectRefVar.data;
//eg
myCircle.radius;
```
## Invoking the object's method
```java
objectRefVar.methodName(arguments);
//eg
myCircle.getArea();
```
# Example
```java
Circle myCircle = new Circle(5.0);
```
**Declaration**: associates a variable with an object type
**Instantiation**: new operator allocates memory, returns reference to the object memory, invokes constructor
**Initalization**: by constructor

# Instance Method
Method that refers to individual instances of a class
- `getArea()` is an instance method (without static keyword)
- Must be invoked from an object
- e.g. `myCircle.getArea()`
 
# Difference between variables of primitive data types and object types
|Primitive types|Object types|
|---|---|
|`int i = 1`|`Circle c`|
|Value is directly stored at this memory location| c, the reference, is stored at the memory location. This refers to the circle object somewhere in memory.|
|If assign `i = j`<br>content in `j` will update to `i`|if assign `c1 = c2`<br>Before: c1 --> Circle c1 & c2 --> Circle c2<br>After: c1, c2 --> Circle c2<br>The address reference changed, the objects are still in memory but not referenced<br>Garbage collected automatically by JVM (assigning reference variable to `null` helps garbage collection|

# Instance Variables and Methods
- Instance variables belong to a specific instance
- Instance methods are invoked by an instance of the class
# Static Variables and Methods
- Static variables are shared by all the instances of the class
- Are not tied to a specific object
- Use the `static` modifier
- Static method can be called without creating an instance of the class
![[Pasted image 20220127083556.png]]

# Visibility modifiers: public, private
By default, the class, variable or method can be accessed by any class ==in the same package==.
**Package**: organises Java classes into namespaces
- public: visibe to any class in any package
- default: package private, visible only to classes in the same package
- private: visible only by the declaring class 

![[Pasted image 20220127084106.png]]
![[Pasted image 20220127084116.png]]
## Why put data fields private
- To protect data
	- client can tamper the classes/objects
- To make class easy to maintain
	- impose class constraints / invariants
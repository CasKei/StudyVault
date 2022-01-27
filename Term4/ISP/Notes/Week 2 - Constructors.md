# Constructors
- Special kind of methods that are invoked to create a new object (create an instance, or instantiation)
```java
Circle() {

}
Circle(double newRarius) {
	radius = newRadius;
}
//method overloading:
// same method name, different argument list
```
**No-arg constructor**: constructor without parameter
Constructor must have same name as the class itself.
- No return type, not even void
Invoked with the `new` operator, play the role of initializing objects

## Creating objects using constructors / instantiation
```java
new ClassName();
```
## Default Constructor
A class can be defined without constructors.
In this case, a no-arg constructor with an empty body is implicitly declared in the class.
This constructor, called a **default constructor**, is provided automatically only if ==no constructors are explicitly defined in the class==.

---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]
[[Week 2 - Instance and static variables or methods]]
## 6.1 Introduction
Define reusable code and simplify coding.

## 6.2 Defining a Method
```java
modifier returnValueType methodName(list of parameters) {
	// Method body;
}
```
The method header specifies the modifiers, return value type, method name, and parameters of the method.

## 6.3 Calling a Method
Each time a method is invoked, the system creates an activation record that stores aprameters and variables for hte method and places the activation record  in an area of memory known as a call stack.
Also known as runtime stack, execution stack, machine stack.
Last in first out.

## 6.4 void Method Example
Does not return any value.\
A call to a void method must be a statement. Therefore it is invoked as a statement in the main method.

## 6.5 Passing Arguments by Values
Arguments are passed by value to parameters when invoking a method.

## 6.6 Modularising Code
Modularising makes the code easy to maintain and debug and enables the code to be reused.
Prime number method
```java
public static boolan isPrime(int number) {
	for (int divisor = 2; divisor <= number/2; divisor++) {
		if (number % divisor == 0) {
			return false;
		}
	}
	return true;
}
```

## 6.7 Case Study: Converting Hex to Dec
Horner's algorithm
```java
int decimalValue = 0; 
for (int i = 0; i < hex.length(); i++) { 
	char hexChar = hex.charAt(i); 
	decimalValue = decimalValue * 16 + hexCharToDecimal(hexChar); 
}
```

## 6.8 Overloading Methods
[[Method Overloading & Overriding|Overloading]] methods allows you to define the methods with the same name as long as their signatures are different.

The max method that was used earlier works only with the int data type. But what if you need to determine which of two floating-point numbers has the maximum value? The solution is to create another method with the same name but different parameters, as shown in the following code:
```java
public static double max(double num1, double num2) { 
	if (num1 > num2) 
		return num1; 
	else 
		return num2; 
}
```
If you call max with int parameters, the max method that expects int parameters will be invoked; if you call max with double parameters, the max method that expects double parameters will be invoked. This is referred to as method overloading; that is, two methods have the same name but different parameter lists within one class. The Java compiler determines which method to use based on the method signature.

Named same, args diff.

## 6.9 The Scope of Variables
The scope of a variable is the part of the program where the variable can be referenced.
You can declare a local variable with the same name in different blocks in a method, but you cannot declare a local variable twice in the same block or in nested blocks.

## 6.10 Case Study: Generating Random Characters
A character is coded using an integer. Generating a random character is to generate an integer.

As introduced in Section 4.3, every character has a unique Unicode between 0 and FFFF in hexadecimal (65535 in decimal). To generate a random character is to generate a random integer between 0 and 65535 using the following expression (note that since 0 <= Math.random() < 1.0, you have to add 1 to 65535):
```java
(int)(Math.random() * (65535 + 1))
```
Thus, a random integer between `(int)'a'` and `(int)'z'` is 
```java
(int)((int)'a' + Math.random() * ((int)'z' - (int)'a' + 1));
'a' + Math.random() * ('z' - 'a' + 1); // simplified but same
```
Random lowercase letter
```java
(char)('a' + Math.random() * ('z' - 'a' + 1))
```
Random char between any ch1 and ch2 with ch1 < ch2
```java
(char)(ch1 + Math.random() * (ch2 – ch1 + 1))
```

## 6.11 Method Abstraction and Stepwise Refinement
The key to developing software is to apply the concept of [[Abstraction]]
Method abstraction is achieved by separating the use of a method from its implementation. The client can use a method without knowing how it is implemented. Details of the implementation are [[Week 2 - Encapsulation|encapsulated]] in the method and hidden from the client whi invokes the method.

You can use either a “top-down” or a “bottom-up” approach. 

The top-down approach implements one method in the structure chart at a time from the top to the bottom. Stubs— a simple but incomplete version of a method—can be used for the methods waiting to be implemented. The use of stubs enables you to quickly build the framework of the program. Implement the main method first, and then use a stub for the printMonth method.

The bottom-up approach implements one method in the structure chart at a time from the bottom to the top. For each method implemented, write a test program, known as the driver, to test it.

The top-down and bottom-up approaches are equally good: Both approaches implement methods incrementally, help to isolate programming errors, and make debugging easy. They can be used together.


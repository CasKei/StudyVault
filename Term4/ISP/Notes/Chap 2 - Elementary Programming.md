---
tags: #50.001
---
## 2.1 Introduction
The focus of this chapter is on leaning elementary programming techniques to solve problems.
## 2.2 Writing a Simple Program
Writing a program involves designing a strategy for solving the problem ad then using a programming language to implement that strategy.
Variable: represents a value stored in the computer's memory
Descriptive names: use radius instead of x
Data type: bool, int, etc.
Primitive data types/fundamental types.
Floating point number is called a double in Java.

`ComputeArea.java`
```java
public class ComputeArea {
	public static void main(String[] args) {
		// Declaring variables
		double radius;
		double area;

		//Assign a radius
		radius = 20;
		//Compute area
		area = radius * radius * 3.14159;

		//Display results
		System.out.println("Area for circle of radius " + radius + " is " + area);
	}
}
```

Concatenate strings
`+`  sign.

## 2.3 Reading Input from the Console
Reading input from the console enables the program to accept input from the user.

`Scanner` is a class in `java.util` package used for obtaining the input of the primitive types like int, double, etc. and strings. It is the easiest way to read input in a Java program, though not very efficient if you want an input method for scenarios where time is a constraint like in competitive programming.

Java uses `System.out` to refer to the standard output dvice, and `System.in` to the standard inout  dvice.
By default, output device is monitor and input device is keyboard.
To perform console output, you simply use `println` method to display a primitive value or a string to the console.
Console input is not directly supported in Java, but you can use the `Scanner` class to create an object to read input from `System.in`:
```java
Scanner input = new Scanner(System.in);
```
`new Scanner(System.in)` : creates an object of the `Scanner` type.
`Scanner input`: declares that `input` is a variable wose type is `Scanner`.
To invoke its methods (ask the object to perform a task):
```java
double radius = input.nextDouble()
```

Listing 2.2 `ComputeAreaWithConsoleInput.java`
```java
import java.util.Scanner; //Scanner is in the java.util package, have to import

public class ComputeAreaWithConsoleInput {
	public static void main(String[] args) {
		//Create a Scanner object
		Scanner input = new scanner(System.in);

		// Prompt the user to enter a radius
		System.out.print("Enter a number for radius: ");
		double radius = input.nextDouble();

		// Compute area
		double area = radius * radius * 3.14159;

		// Display results
		System.out.println("The area for the circle of radius " + radius + " is " + area);
	}
}
```
The `System.out.print` is a prompt as it directs the user to enter an input.
`print`: does not advance to new line when completed
`println`: advances to new line when completed
`double radius = input.nextDouble()`: reads the input from the keyboard and assigns it to `radius`.

There are 2 kinds of `import` statements:
- Specific import
	- specifies a single class in the import statement
	- `import java.util.Scanner;`
- Wildcard import
	- imports all classes in a package by using asterisk as the woldcard.
	- `import java.util.*`

The info for classes in an imported package is not read at compile time or runtime unless the class is used in the program. The import statement simply tells the compiler where to locate the classes. There is no performance difference between a specific and wildcared import declaration.

Listing2.3: reading multiple inputs. `ComputeAverage.java`
```java
import java.util.Scanner; //Scanner is in the java.util package

public class ComputeAverage {
	public static void main(String[] args) {
		//Create a Scanner object
		Scanner input = new Scanner(System.in);

		// Prompt the user to enter three numbers
		System.out.print("Enter 3 numbers: ");
		double number1 = input.nextDouble();
		double number2 = input.nextDouble();
		double number3 = input.nextDouble();

		// Compute average
		double average = (number1 + number2 + number3) / 3;

		// Display results
		System.out.println("The average of " + number1) + " " + number2 + " " + number3 + " is " + average);
	}
}
```
## 2.4 Identifiers
Indentifiers are the names that identify the elements such as classes, methods, and variables in a program.

All identifiers obey the following rules:
- a sequence of characters that consists of letters, digits, underscores and dollarsigns
- must start with a letter, underscore, dollar sign. It cannot start with a digit.
- cannot be a reserved word
- cannot be `true`, `false`, or `null`
- can be of any length

## 2.5 Variables
Variables are used to represent values that may be changed in the program.

Variables are for representing data of a certain type. Declare it by telling the compiler its name as well as what type of data it can store.
Variable declaration tells the compiler to allocate appropriate memory space for the variable based on its data type
Syntax:
`datatype variableName;`

Datatypes: `int`, `double`, `byte`, `short`, `long`, `float`, `char`, `boolean`.

If of the same type, can be declared together:
`datatype var1, var2 ...;`

Can declare and initialise initial value in one step
`int x = 4;`
is equivalent to 
`int x;
`x = 4;`

Shorthand form to declare and initialise variables of the same type together
`int i = 1, j = 2;`

Every variable has a scope. The scope of a variable is the part of the program where the variable can be referenced.

## 2.6 Assignment Statements and Assignment Expressions
An assignment statement designates a value for a variable. An assignment statement can be used as an expression in Java.

Assignment statement: assign a variable to a declared variable
Assignment operator: equal sign
Expression: a computation involving values, variables and operators that taking them together, evaluates to a value.
Assignment Expression: an assignment statement.

## 2.7 Named Constants
A named constant is an identifier that represents a permanent value.
Syntax:
```java
final datatype CONSTANTNAME = value;
```

A constant must be declared and initialised in the same statement.
The word `final` is a java keyword for decalring a constant.

## 2.8 Naming Conventions
Sticking with the Java naming conventions makes your programs easy to read and avoids errors.

Descriptive names

Name variables and methods: use lowercase for variables and methods, concatenate multiple words, camelCase
Name classes: capitalise first letter, CapCase
Name constants: capitalise all letters, use underscores between words

## 2.9 Numeric Data Types and Operations
Java has 6 numeric types for ints and floats with operators `+`, `-`, `*`, `/`, and `%`.

### 2.9.1 Numeric Types
![[Pasted image 20220208104650.png]]
### 2.9.2 Reading Numbers from the Keyboard
![[Pasted image 20220208104747.png]]
### 2.9.3 Numeric Operators
![[Pasted image 20220208104820.png]]

Listing2.5 `DisplayTime.java`
```java
import java.util.Scanner;

public class DisplayTime {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.print("Enter an integer for seconds: ");
		int seconds = input.nextInt();

		int minutes = seconds / 60;
		int remainingSeconds = seconds % 60;

		System.out.println(seconds + "s is " + minutes + 'min , ' + remainingSeconds + "s.")
	}
}
```
### 2.9.4 Exponent Operations
`Math.pow(a, b)` method.
`pow` method is defined in the `Math` class in the Java API.
Invoke the method using syntax `Math.pow(a,b)`

## 2.10 Numeric Literals
A literal is a constant value that appears directly in a program.
### 2.10.1 Integer Literals
An integer literal can be assigned to an integer variable as long as it can fit into the variable.
e.g. `byte b = 128` will have compile error because range of a byte value is -128 to 127.
Assumed to be `int` type, value between $-2^{31} (-2147483648)$ and $2^{31} - 1 (2147483647)$.

To denote an integer literal of the `long` type, append the letter `L` or `l` to it.
### 2.10.2 Floating-Point Literals
Default `double` type.
Make a number a `double` by appending the letter `d` or `D`.
`float`: `f` or `F` 
### 2.10.3 Scientific Notation
`1.23456E2`
`1.23456E-2`
`E` or `e`

## 2.11 Evaluating Expressions and Operator Precedence
Java expressions are evaluated in the same way as arithmetic expressions.

Listing2.6 `FahrenheitToCelsius.java`
```java
import java.util.Scanner;

public 
```
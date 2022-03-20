---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 3.1 Introduction
Java provides *selection statements*: statements that let you choose actions with alternative courses.

Selection statements use Boolean expressions. A *Boolean expression* is an expression that evaluates to a Boolean value.

## 3.2 boolean Data type
The boolean datatype declares a variable with either `true` or `false`.
![[Pasted image 20220317161409.png]]

## 3.3 if Statements
One-way if statement:
```java
if (boolean_expression) {
	statement(s);
}
```

## 3.4 Two-way if-else Statements
Decides the execution path based on whether the condition is true or false.
```java
if (boolean_expression) {
	statement_if_true;
} else {
	statement_if_false;
}
```

## 3.5 Nested if and Multi-way if-else Statements
*An **if** statement can be inside another **if** statement t form nested **if** statements.*
```java
if (i > k) {
	if (j > k) {
		System,out.println("i and j greater than k");
	}
}
else
	System.out.println("i is less than or equal to k");
```
Use `else if` to reduce indentations.

## 3.6 Common Errors and Pitfalls
Forget necessary braces.
Wrong Semicolon at if line.
Redundant Testing of Boolean values.
Damngling else ambiguity.
Equality Test of Two Float-Point Values.

Simplifying Boolean Variable Assignment
Avoiding Duplicate Code in different cases

## 3.7 Generating random Numbers
*You can use `Math.random()` to obtain a random double value between 0.0 and 1.0, excluding 1.0.*

Listing3.3 SubtractionQuiz.java
```java
import java.util.Scanner;

public class SubtractionQuiz {
	public static void main(String[] args) {
		int number1 = (int)(Math.random() * 10);
		int number2 = (int)(Math.random()*10);

		if (number1 < number2) {
			int temp = number1;
			number1 = number2;
			number2 = temp;
		}
		System.out.print("What is " + number1 + "-" + number2 + "?");
		if (number1 - number2 == answer)
			System.out.println("You are correct!");
		else {
			System.out.println("Your answer is wrong.");
			System.out.println(number1 + "-" + number2 + " should be " + (number1 - number2));
		}
	}
}
```

## 3.8 Case Study: Computing BMI

## 3.9 Case Study: Computing Taxes

## 3.10 Logical Operators
*The logical operators `!`, `&&`, `||`, and `^` can be used to create a compount boolean expression.*

## 3.11 Case Study: Determining Leap Year
*A year is a leap year if it is divisible by 4 but not 100, or if it is divisible by 400.*

## 3.12 Case Study: Lottery


## 3.13 switch Statements
*A **switch** statement executes statements based on the value of a variable or an expression.*

```java
switch (switch_expression) {
	case value1: statement1(s);
				 break;
	case value2: statement2(s);
				 break;
	case valueN: statementN(s);
				 break;
	default: statement_for_default;
}
```
- switch_expression must yield a value of `char`, `byte`, `short`, `int`, `String` type, and must always be in parentheses.
- valueN must be same datatype as switch_expression, and are constants, cannot have variables.
- When value in a `case` statement matches the value of the switch_expression, statements starting from the case are executed until either a break or the end of the switch statement is reached.
- `default` is optional, can be used to perform actions when none of the specified cases matches the switch_expression
- `break` is optional, the `break` statmenet immediately ends the `switch` statement.

## 3.14 Conditional Expressions
*A conditional expression evaluates an expression based on a condition.*
```java
if (x > 0)
	y = 1;
else
	y = -1;
```
Alternatively,
```java
y = (x > 0) ? 1 : -1;
```

## 3.15 Operator Precedence and Associativity
Operator precedence and associativity determine the order in which operators are evaluated.

## 3.16 Debugging
JDK includes a command-line debugger, jdb, which is invoked with a class name. jdb is itself a Java program, running its own copy of Java interpreter. All the Java IDE tools, such as Eclipse and NetBeans, include integrated debuggers. The debugger utilities let you follow the execution of a program. They vary from one system to another, but they all support most of the following helpful features.
- Executing a single statement at a time
- Trace into or step over a method
- Set breakpoints
- Display variables
- Display call stacks
- Modify variables


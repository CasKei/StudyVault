# Java Syntax
How to describe the syntax of programmign languages?
## Backus Normal Form (BNF)
---
C++ BNF: 140 rules
Java BNF: 50 rules
Java has a simple syntax.
In programming languages, you have to specify characters.
\<character\> ::= \<letter\> | \<digit\> | ...
\<digit\> ::= "0" | "1" | ... | "9"

# Java is Portable
- Portable
	- Can run on any computer / device with Java Virtual Machine (JVM)
![[Pasted image 20220125070411.png]]
High-level programming languages have to be translted into machine language before the program can be executed by compiler
![[Pasted image 20220125070422.png]]
Machine codes are platform-specific, not portable, not suitable for connected computers.
- Java programs are compiled into a specific type of machine language called **bytecode**
- Bytecode can be run on any computer with a JVM
- JVM: a software that interprets Java bytecode

# Android Studio
- We use Android Studio to program Java
- IDE: Integrated development Environment
	- edit, compile, build, debug, etc
- Other IDE: Eclipse
## Create Project
File > New > New Project
- Select the form factors: Phone and Tablet
- Select 'No Activity'
- Application name: MyApp01
- Minimum SDK: API 21
- View > Tool Windows > Project
## Create Module
File > New > New Module
- Choose 'Java or Kotlin Library'
- Library name: lib01
- Class name: MyClass
- To remove a module: File ? Project structure, choose module, select '-'
```java
public class MyClass {
  public static void main(String[] args){
    System.out.println("Hello World");
  }
}
```
- Every Java program must contain at least one class that defines the data and methods (functions) 
- JVM executes the program from the main method
- void: does not have any return value
- public: accessibility modifier; MyClass can be used anyway in the program
## Run the Program
Run > Edit configurations
- Select '+' (Add new configuration) > Application
- Name: Java Application
- Select `<Project>.<module>`
- Main class: MyClass
Error message "Android Gradle plugin requires Java 11 to run. You are currently using Java 1.8"
File > Project Structure
- SDK location > Gradle Settings
- Gradle JDK > Android Studio Java home version 11.0.10
# Variables and Array
## Variables
- Variables are used to store data in a program
- In java you have to specify what type of data a variable reprsents: **variable declaration**
```java
int a = 0;
int b = 1;
```
Note: There are 4 types of variables:
- Non static
- Static 
- Local
- Parameters
http://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html

Class name start with Capital letter
variable name start with lower case letter.
```java
// declare and assign separately also works
int a;
a = 1;
```
## Array
Used to store a collection of data
```java
int[] c; // declare c as an integer array
c = new int[3]; // allocate memory for 3 int
c[0] = 17;
c[1] = 23;
c[2] = 38;
System.out.println("0th value:" + c[0]);
System.out.println("1st value:" + c[1]);
System.out.println("2nd value:" + c[2]);
```
c is declared as a variable of reference to an array of integers.
c is not the array or the integer.
Three int memory are allocated. The array reference is assigned to c.

# String
String is a sequence of characters
```java
String d = "HelloXDD";
int len = d.length()
System.out.println(d);
System.out.println(len);
System.out.println("1st value:" + c[1]);
```
Another way to create String object
```java
char[] dArray = {'h', 'e', 'l', 'l', 'o'};
String dString = new String(dArray);
System.out.println(dString);
```
# If-then, for-loop
## If-then-else
Selective statements and conditional execution
```java
int simonWeight = 99999; // in kg, oh no
String advice = ""; // declare an empty string
if (simonWeight <= 75) {
	advice = "fit";
} else if (simonWeight <= 100) {
	advice = "eat less";
} else if (simonWeight <= 150) {
	advice = "no dinner";
} else {
	advice = "no dinner no breakfast no tea no lunch";
}
```
## For-loop
Loop: program construct to control repeated execution of a block of statements
```java
for(int i=1; i<=4; i++){
	System.out.println("Count is: " + i);
}
```
(initial action) ; (loop continuation condition) ; (action after each iteration)
Output
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
```
# Method
 (function, operation)
```java
class Demo {
	public static void printHAHA() {
		System.out.println("HAHA") // declare a method
	}
	public static void main(String[] args) {
		printHAHA(); // use a method
	}
}
```
With argument
```java
class Demo {
	public static void printa(int a) { //printa: name of method
		System.out.println(a); // int a is argument
	}
	public static void main(String[] args) {
		printa(3); // will print out the number 3
	}
}
```
Return a value
```java
class Demo {
	public static int four() {
		return 4; //this method returns an int
	}
	public static void main(String[] args) {
		int answer = four() //answer will be equal to 4
	}
}
```
# Reference
[Documentation](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/index.html)
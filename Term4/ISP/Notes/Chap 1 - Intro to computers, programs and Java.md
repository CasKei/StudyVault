---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 1.1 Introduction
The central theme of this book is to learn how to solve problems by writing a program.
## 1.2 What is a Computer?
A computer is an electronic device that stores and prcesses data.
Hardware:
- CPU
- Main memory
- Storage devices
- Input devices
- Output devices
- Communication devices

Components are interconnected by a subsystemcalled a bus.
The bus is built into the computer's motherboard, which is a circuit case that connects all of the parts of a computer together.
### 1.2.1 CPU
Contral processing unit.
Receive instruction from memory and execute.
Has 2 conponents:
- Control unit
	- coordinates actions of other components
- Arithmetic/logic unit
	- performs numeric and logic operations

Built on transistors.

Every computer has internal clock, eitting electronic pulses at constant rate, to control and synchronise the pace of operations.
Clock speed means more instructions executed in a given period of time.

CPU we re originally developed with one core. The core is the part that performs the reading and executing of instructions. Now have multiple cores.
### 1.2.2 bits and Bytes
Bits: 0 or 1
Byte: 8 bits
Encoding scheme: a set of rules that govern how a computer translates characters, numbers and symbols into data the computer can actually work with.
### 1.2.3 Memory
Memory consists ofan ordered sequence of bytes for storing the programs as well as data that the program is working with. It is the computer's work area for executing a program.
Each byte has a unique address.
The address can be used to locate the byte and retrieve the data.
Since bytes can be accessed in any order, the memory is also referred to as random access memory RAM.
### 1.2.4 Storage decides
Long term memroy that can be moved to RAM when needed.
- Magnetic disk drives
- Optical disc drives
- USB flash drives (universal serial bu)

Drives are devices fo operating a medium, such as disks and CDs. A storage medium physically stores data and prgram isntructions. Drive reads data from medium and writes data onto the medium.
### 1.2.5 Input and Output Devices
Keyboard, Mouse,  Monitor, etc.
### 1.2.6 Communication Devices
- Dial-up modem: phone line
- Digital subscriber line (DSL) connection. Phone line but 20 times faster
- Cable modem: cable TV line, even faster
- Network interface card (NIC) connects a computer to a local area network (LAN).
- Wireless netwoking
## 1.3 Programming Languages
### 1.3.1 Machine Language
Binary code
### 1.3.2 Assembly Language
Uses a short descriptive word known as a mnemonic to represent each of the machine-language instructions.
### 1.3.3 High-level Language
English like.
Instructions are called statements.

Progrm is called a source program or source code.
Source code must be translated into machine code using an interpreter or a compiler.
- An interpreter reads one statement from source code, traslates it to machine code or virtual machine code, then executes it.
- A compiler translates the entire source code into a machine code file, then the file is executed.

## 1.4 Operating Systems
The OS manages and controls a computer's activities.
Allocates and assignes system resources.
Schedule operations.
### 1.4.1 Controlling and Monitoring System Activities
Security and management
### 1.4.2 Allocating and Assigning System Resources
Determine what resources a program needs and alloctes them.
### 1.4.3 Scheduling Operations
Multiprogramming: multiple programs to run simultaneously by sharing the same CPU
Multithreading: a single program to execute multiple tasks at the same time.
Multiprocessing/parallel processing: use 2 or more processors together to perform subtasks concurrently and then combine solutions to obtain a solution for the entire task.
## 1.5 Java, the WWW, and Beyond
Java: simple, object oriented, distributed, interpreted, robust, secure, architecture neutral, protable, high performance, multi-threaded, dynamic.

Full-featured, general-purpose.

The WWW is an electronic info repository accessible on the Internet. Java is attractive as Java programs canrun from a web browser, called applets.

Today you can create rich Internet Applications (RIA)..
## 1.6 The Java Language Specification, API, JDK, and IDE.
Java syntax is defined in the Java language specification
Java library is defined in the Java API
JDK is the software for developing and runnign Java rpograms
IDE is an integrated development for rapidly developing programs.
- Java SE: develop client side apps
- Java EE: develop server side apps
- Java ME: mobile devices

JDK consists of separate programs, each invoked from commandline, for developing and testing Java programs. 
Can use IDE to do the same with GUI by running with a button.
## 1.7 A Simple Java Program
A Java program is executed from the `main` method in the class.

Console is an old computer term that reters to the text entry and display device of a computer.
`Listing 1.1 Welcome.java`
```java
1. public class Welcome {
2.     public static void main(String[] args) {
3. 	       // Display message on console
4.		   System.out.println("Welcome to Java");
5.	   }
6. }
```
> Welcom to Java

Line 1: define a class. Every Java program must have at least one class. Each class has a name, by convention uppercase
Line 2: `main` method. The program is executed from the `main` method. A class may have several methods, but thsi si the entry point where program begins execution

A method is a construct that contains statements.
The `main` method in this program contains the `System.out.println` statement. This statement displays the string on the console.
String is a sequence of characters.
Every statement in Java ends with `;`, which is a statement terminator.

Reserved words, or keywords, have specific meaning to the compiler and cannot be used for other purposes. Here we have`class`, `public`, `static` and `void`.

Line 3 is a comment.

Curly braces form a block.
Each class has a class block that groups the data and methods together.
Each method has a method block that groups the statements of the method.
Blocks can be nested.

`Listing 1.2 TwoMessages.java`
```java
public class TwoMessages {
	public static void main(String[] args) {
 	    // Display message on console
		System.out.println("Welcome to Java");
		System.out.println("Welcome to Java");
	}
}
```
> Welcom to Java
> Welcom to Java

`Listing 1.3 Math.java`
```java
public class Math {
	public static void main(String[] args) {
		System.out.println(2+2-1)
	}
}
```
> 3

## 1.8 Creating, Compiling, and Executing a Java Program
You save a Java prgram in a .java file and compile it into a .class file. The .class file is executed by the JVM.
![[Pasted image 20220207134057.png]]
Bytecode: similar to machine instructions but is architecture neutral and can run on any platform that has a Java Virtual Machine (JVM)
Java bytecode can run on a variety of hardware platforms and operating systems. Java source code is compiled into Java bytecode and Java bytecode is interpreted by the JVM. Your Java code may use the code in the Java library. 
You can execute the bytecode on any platform with a JVM, which is an interpreter. It translates the individual instructions in the bytecode into the target machine language code one at a time rather than the whole program as a single unit. Each step is executed immediately after it is translated.
## 1.9 Programming Style and Documentation
Good programming style and proper documentation make a program easy to read and help programmers prevent errors
### 1.9.1 Appropriate Comments and Comment Styles
In addition to line comments (beginning with ``//``) and block comments (beginning with ``/*``), Java supports comments of a special type, referred to as javadoc comments. javadoc comments begin with `/** `and end with `*/`. They can be extracted into an HTML file using the JDK’s javadoc command. For more information, see Supplement III.Y, javadoc Comments, on the companion Website. Use javadoc comments (``/** ... */``) for commenting on an entire class or an entire method. These comments must precede the class or the method header in order to be extracted into a javadoc HTML file. For commenting on steps inside a method, use line comments (``//``).
### 1.9.2 Proper Indentation and Spacing
Indentation is used to illustrate the structural relationships between a program’s components or statements. Java can read the program even if all of the statements are on the same long line, but humans find it easier to read and maintain code that is aligned properly. Indent each subcomponent or statement at least two spaces more than the construct within which it is nested. A single space should be added on both sides of a binary operator.
### 1.9.3 Block Styles
A block is a group of statements surrounded by braces. There are two popular styles, next-line style and end-of-line style, as shown below.

## 1.10 Programming Error
Syntax errors, runtime errors, logic errors.
### 1.10.1 Syntax errors
Errors detected by the compiler.
### 1.10.2 Runtime errors
Errors that cause a program to terminate abnormally.
Input error, division by 0, etc.
### 1.10.3 Logic Errors
Does not perform as intended.
### 1.10.4 Common Errors
Missing a closing brace, missing a semicolon, missing quotation marks for strings, and misspelling names are common errors for new programmers.
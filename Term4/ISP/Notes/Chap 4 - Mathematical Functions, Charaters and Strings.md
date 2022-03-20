---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 4.1 Introduction
The focus of this chapter is to introduce mathematical functions, characters, string objects, and use them to develop programs

## 4.2 Common Mathematical Functions
*Java provides many useful methods in the `Math` class for performing common mathematical functions.*
![[Pasted image 20220317182458.png]]
![[Pasted image 20220317182516.png]]
![[Pasted image 20220317182536.png]]
![[Pasted image 20220317182558.png]]
![[Pasted image 20220317182612.png]]

## 4.3 Character Data Type and Operations
```java
char letter = 'A';
char numChar = '4';
```
You can use ASCII characters such as `X`, `1`, and `$` in a Java program as well as Unicodes.
![[Pasted image 20220317183801.png]]
These are equivalent
```java
char letter = 'A';
char letter = '\u0041'
```
![[Pasted image 20220317183901.png]]

A `char` can be *cast* into any numeric type and vice versa. When an integer is cast into a char, only its lower 16 bits of data are used; the other part is ignored.
```java
char ch = (char)0XAB0041; // lower 16 bits 0041 assigned to ch
System.out.println(ch); // ch is A
```
When floating point is cast, first it is converted to `int`, then cast to `char`.
```java
char ch = (char)65.25; // Decimal 65 is assigned to ch
System.out.println(ch); // ch is character A
```
When `char` is cast into numeric type, character's Unicode is cast.
```java
int i = (int)'A'; // The Unicode of character A is assigned to i
System.out.println(i); // i is 65
```

**Implicit casting** if result of casting fits into target variable, otherwise **explicit casting**.
For example, since the Unicode of 'a' is 97, which is within the range of a byte, these implicit castings are fine:
```java
byte b = 'a';
int i = 'a';
```
But the following casting is incorrect, because the Unicode \uFFF4 cannot fit into a byte: 
```java
byte b = '\uFFF4';
```
Explicit
```java
byte b = (byte)'\uFFF4';
```
Any positive integer between 0 and FFFF in hexadecimal can be cast into a character implicitly. Any number not in this range must be cast into a char explicitly.
Chars can be compared.
![[Pasted image 20220317191304.png]]

## 4.4 The String Type
```java
String message = "Welcome to Java";
```
String is a predefined class in the Java library, like `System` and `Scanner`.
It is known as a *reference type*.
![[Pasted image 20220317191621.png]]
Strings are objects. Methods can only be invoked from a specific string instance. These methods are [[Week 2 - Instance and static variables or methods|instance methods]]. A non-instance method is called a [[Week 2 - Instance and static variables or methods|static method]]. A static method can be invoked without using an object. 
```java
str.length()
s.charAt(index)
```
```java
String s3 = s1.concat(s2);
String s3 = s1 + s2;
String myString = message + " and " + "HTML";
String message += " and Java is fun";
```
```java
"Welcome".toLowerCase() //returns a new string welcome.
"Welcome".toUpperCase() //returns a new string WELCOME.
```

The `trim()` method returns a new string by eliminating whitespace characters from both ends of the string. The characters `' '`, `\t`, `\f`, `\r`, or `\n` are known as whitespace characters.

![[Pasted image 20220317195807.png]]
`==` tells whether variables refer to the same object, not whether its contents are the same. Use `equals` method.

```java
String message = "Welcome to Java"; 
String message = message.substring(0, 11) + "HTML"; 
//The string message now becomes Welcome to HTML.
```
![[Pasted image 20220317195938.png]]

Convert String to int
```java
int intValue = Integer.parseInt(intString);
```
String to double
```java
double doubleValue = Double.parseDouble(doubleString);
```
Number to string
```java
String s = number + "";
```

## 4.5 Case Studies

## 4.6 Formatting Console Output
*You can use the `System.out.printf` method to display formatted output on the console.*
![[Pasted image 20220317201449.png]]
![[Pasted image 20220317201501.png]]
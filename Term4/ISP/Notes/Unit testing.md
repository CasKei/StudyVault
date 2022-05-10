---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Unit Testing with JUnit4
A **unit** is the smallest component that can be tested in your software, usually it is a method in a class.
**Unit testing** thus ensures that each of these components behave as designed.

Why?
- Validates that your software works, even in the face of continual changes in your code
- Writing code for unit testing also forces your program to be modular

In the context of an android app,
- testing parts that dont involve UI: unit testing (easy)
- testing parts that involve UI: [[Instrumented testing]] (hard)

Hence, it is good prog practice to **separate the parts of your code that involve UI and those that don't**

**JUnit4** is a commonly used open-source framework to conduct unit testing.
Write your tests in a **test class**.

Android studio automatically generates the test class for you.

## Where and how to run unit tests
Test class is found in folder marked **(test)**

Default file generated contains one trivial unit test. You can write more.
To run the rests, right click **ExampleUnitTest -> Run 'ExampleUnitTest'**

If pass, should see all the tests have a green tick beside.

## How to write a unit test
For each unit test
- write a method that returns void with the `@Test` annotation
- within this method, use `assertEquals()` method to compare the actual object and the expected object

```java
@Test
public void addition_isCorrect() {
	assertEquals(expected, actual);
}
```
There are other assert methods available.

In the following unit tests in Examples 1 to 3, suppose that there is a class A that has a method called `someFunction()` that is [[Method Overloading & Overriding|overloaded]] and has the following specifications:  
- If no parameters are passed to it, it returns a `double` value of 2.95  
- If a string containing a number is passed to it, it returns a `BigDecimal` object initialized with that string  
- If a string is passed to it and it does not contain a number, it throws an `IllegalArgumentException`

![[Pasted image 20220323202137.png]]
![[Pasted image 20220323202200.png]]

**Discussion**. Commercial software applications tend to have a huge code base in size. With highly frequent releases, tight schedules, and limited resources. Software testing is always costly. Suppose you are a manager, how do you make software testing cost-effective without sacrificing the quality of the software?
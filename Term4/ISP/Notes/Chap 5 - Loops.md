---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 5.1 Introduction
*A loop can be used to tell a program to execute statements repeatedly.*

## 5.2 The while loop
```java
while (loop_continuation_condition) {
	Statement(s);
}
```

## 5.3 The do-while Loop
Excecutes loop body before checking condition.
```java
do {
	Statement(s);
} while (loop_continuation_condition);
```

## 5.4 The for Loop
```java
for (i = initialValue; i < endValue; i++) {
	//Loop body
}
```

## 5.5 Which to use?
nyeh

## 5.6 Nested Loops

## 5.7 Minimizing Numeric Errors
Floating points are approximations. Use double if possible. Or add smaller numbers before bigger numbers.

## 5.8 Case Studies
```java
int gcd = 1
int k = 2
while (k <= n1 && k <= n2) {
	if (n1 % k == 0 && n2 % k == 0)
		gcd = k;
	k++;
}
```

## 5.9 Keywords break and continue
break breaks out of loop.

continue ends current iteration and program control goes to the end of the loop body

So break gets out of loop while continue ends the current iteration so the rest of the statements in the loop body is not executed.

## 5.10 Case Study: Checking Palindromes
```java
import java.util.Scanner;

public class Palindrome {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.print("Enter a string: ");
		String s = input.nextLine();

		int low = 0;
		int high = s.length() - 1;
		boolean isPalindrome = true;
		while (low < high) {
			if (s.charAt(low) != s.charAt(high)) {
				isPalindrome = false;
				break;
			}
			low++;
			high++;
		}
		if (isPalindrome) {
			System.out.println(s + " is a palindrome");
		} else {
			System.out.println(s + " is not a palindrome");
		}
	}
}
```

## 5.11 Case Study: Displaying Prime Numbers
```java
public class PrimeNumber {
	public static void main(String[] args) {
	final int NUMBER_OF_PRIMES = 50; // Number of primes to display
	final int NUMBER_OF_PRIMES_PER_LINE = 10; // Display 10 per line int
	count = 0; // Count the number of prime numbers
	int number = 2; // A number to be tested for primeness
	System.out.println("The first 50 prime numbers are \n"); // Repeatedly find prime numbers
	while (count < NUMBER_OF_PRIMES) {
// Assume the number is prime
		boolean isPrime = true; // Is the current number prime?
    // Test whether number is prime
		for (int divisor = 2; divisor <= number / 2; divisor++) {
			if (number % divisor == 0) { // If true, number is not prime
				isPrime = false; // Set isPrime to false break; // Exit the for loop
			}
		}
		if (isPrime) {
			count++;
			if (count % NUMBER_OF_PRIMES_PER_LINE == 0) {
				System.out.println(number);
			} else
				System.out.print(number + " ");
		}
		number++;
		}
	}
}
```

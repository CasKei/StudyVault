# Cohort Questions
## Session 1
### 1. **Fibonacci Numbers Generator**
[5 points] Write a JAVA program that returns the first _n_ numbers in the fibonacci sequence, in this format:

 Eg. For _n_ = 5 the output is
 `0,1,1,2,3`

When submitting, return these numbers in this format as a string, instead of printing.

## Session 2
### 2. Iterating with Iterator
[5 points] Suppose that _integers_ is a variable of type `List<Integer>`. Write a program that uses an iterator to compute the sum of all integer values in the List.

(Test case inputs: `(1, 2, 3, 4, 5)` Expected output: `15`)
### 3. Iterating with For-Each
[5 points] Write a second program that does the same thing as in the previous question but using a for-each loop. (Test case inputs: `(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)` Expected output: `55`)
## Session 3
### 4. The Account Class
[10 points] Design a class name `Account` that contains:
Private `int` data field named `id` for the account (default 0)
Private double data field named `balance` for the account (default 0)
Private double data field named `annualInterestRate` that stores the current interest rate (in percentage, default 0). Assume all accounts have the same interest rate.
A private Date data field named `dateCreated` that stores the date when the account was created.
A no-arg constructor that creates a default account
A constructor that creates an account with the specified `id` and initial `balance`
The accessor and mutator methods for `id`, `balance`, and `annualInterestRate`
The accessor method for `dateCreated`
A method named `getMonthlyInterestRate()` that returns the monthly interest rate
A method named `getMonthlyInterest()` that returns the monthly interest
A method named `withdraw` that withdraws a specified amount from the account
A method named `deposit` that deposits a specified amount to the account
Write a test program that creates an Account object, with withdraw and deposit method to withdraw / deposit the amount, and print the balance, monthly interest and the date when the account was created. Note that the account balance is allowed to be negative.

Test case
```java
public class TestAccount{
	public static void main (String[] args) {
	Account account = new Account(1122, 20000);
	Account.setAnnualInterestRate(4.5);
	account.withdraw(2500);
	account.deposit(3000);
	System.out.println("Balance is " + account.getBalance());
	System.out.println("Monthly interest is " +
	account.getMonthlyInterest());
	}
}
```
Expected output
```
Balance is 20500.0
Monthly interest is 76.875
```
# Homework Questions
### 1.  Prime Number Checker
[5 points] Write a static method, that reads in a number (you can assume that the input number is always >=3). Return 1 if it is prime, return 0 if it is not prime.

Hints: use %. a%b= remainder of a/b. e.g. 13%5=3, 4%2=0

(Test case inputs: 4, 7, 14, 23, 99 Expected outputs: 0, 1, 0, 1, 0)
### 2. Geometry: The MyRectangle2D class
Define the `MyRectangle2D` class that contains:
• Two double data fields named `x` and `y` that specify the center of the rectangle with get and set methods: `getX`, `setX`,`getY`, `setY`. (Assume that the rectangle sides are parallel to x- or y- axes.)
• The double data fields width and height with get and set methods: `getWidth`, `setWidth`, `getHeight`, `setHeight`.
• A no-arg constructor that creates a default rectangle with (0, 0) for (x, y) and 1 for both width and height.
• A constructor that creates a rectangle with the specified x, y, width, and height: `MyRectangle2D(double x, double y, double width, double height)`
• A method `getArea()` that returns the area of the rectangle.
• A method `getPerimeter()` that returns the perimeter of the rectangle.
• A method `contains(double x, double y)` that returns `true` if the specified point (x, y) is inside this rectangle. See Figure 1(a).
• A method `contains(MyRectangle2D r)` that returns `true` if the specified rectangle is inside this rectangle. See Figure 1(b).
• A method `overlaps(MyRectangle2D r)` that returns `true` if the specified rectangle overlaps with this rectangle. See Figure 1(c).
![[Pasted image 20220126085050.png]]
Figure 1: (a) A point is inside the rectangle. (b) A rectangle is inside another rectangle. (c) A rectangle overlaps another rectangle.

Implement data fields, all constructors, methods getArea(), getPerimeter(), and contains(double x, double y), contains(MyRectangle2D r), and overlaps(MyRectangle2D r)

Please develop test cases to test your code properly before submission


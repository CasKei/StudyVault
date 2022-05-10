---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Exceptions
[[Exception]]
An exception object is thrown during events that prevents execution from continuing normally.
You handle these by putting code in a **try-catch** block.

**ArithmeticException**
- Subclass of **RuntimeException**, thrown by JVM
- **unchecked exception** - compiler does not force you to put the code in a try-catch block. (another exception is **NumberFormatException**)

```java
public class ExceptionsExample {
	public static void main(String[] args) {
		try {
			int a = quotientInt(5,0);
		} catch {
			ex.printStackTrace();
		}
	}
	public static int quotientInt(int a, int b) {
		return a / b;
	}
	// added
	public static double quotientDouble(double a, double b) {
		return a / b;
	}
}
```
Dividing a floating point number by zero does not cause an exception to be thrown.
Is the catch block activated?
Modify it such that it throws an ArithmeticException if b=0.
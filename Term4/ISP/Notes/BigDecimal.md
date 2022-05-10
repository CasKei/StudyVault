---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## BigDecimal class for financial calculations
Types such as `double` and `float` are not suited for financial calculations because accuracy is demanded but you will encounter floating point errors.
```java
System.out.println(0.7 + 0.1); // do you get 0.8?
```
Why?

In computers, decimal values are represented in 2 parts: the integer value `i` and the scale `c`.
Every decimal value is $i \ast b ^{-c}$, where $b$ is the base.

The **BigDecimal** class can be initialised with different types, but we stick wth **String**. If a **String** passed to the [[Week 2 - Constructors|constructor]] does not have a recognisable number, e.g. empty or text, a **NumberFormatException** is thrown.

Objects of **BigDecimal** class have methods that *add*, *subtract*, *multiply* and *divide*.
The **BigDecimal** is immutable, so these methods return a new object.
```java
BigDecimal a = new BigDecimal("1");
BigDecimal b = new BigDecimal("4");
BigDecimal c = a.divide(b);
System.out.println(c);
System.out.println("Scale: " + c.scale());
System.out.println("Unscaled value: " + c.unscaledValue());
```

If any operation results in recurring decimals, like 1/3, a **MathContext** object is needed, which encapsulates the number of significant figures and the mode of rounding.
```java
BigDecimal up = new BigDecimal("10");
BigDecimal down = new BigDecimal("7");
int sigFigures = 5;
MathContext mc = new MathContext(sigfigures, RoundingMode.HALF_UP);
BigDecimal result = up.divide(down, mc);
System.out.println(result);
```
There are different [rounding modes](https://www.baeldung.com/java-bigdecimal-biginteger), which you can read about.
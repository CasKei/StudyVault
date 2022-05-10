---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## Random Class
[[Random class]]
In many applications it is useful to generate random numbers. 

In Java, you do it by getting an instance of the Random class. In this class there are three useful methods
- **`nextInt()`** gives you an integer between $-2^{32}$ and $2^{32}$ (exclusive) 
- **`nextInt(n)`** gives you an integer between $0$ and $n$ (exclusive)
- **`nextDouble()`** gives you a double between $0.0$ and $1.0$

```java
Random r = new Random(); 
r.nextInt(); 
r.nextInt(100); 
r.nextDouble();
```

Random number generators usually need to be initialized with a seed. \
If you need the sequence of random numbers to be the same, you use the same seed. \
If not, one way to get a changing seed is to use the `Date` object.

```java
Date d = new Date(); 
Random r = new Random(d.getTime());
```

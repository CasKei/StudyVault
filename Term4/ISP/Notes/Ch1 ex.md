---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 1.1 
(Display three messages) Write a program that displays Welcome to Java, Welcome to Computer Science, and Programming is fun.
```java
public static void main(String[] args) {
	System.out.println("Welcome to Java");
	System.out.println("Welcome to Computer Science");
	System.out.println("Programming is fun");
}
```

## 1.2
(Display five messages) Write a program that displays Welcome to Java five times.
```java
public static void main(String[] args) {
	int count = 0;
	while (count < 5) {
		System.out.println("Welcome to Java");
		count ++;
	}
}
```

## 1.3
(Display a pattern) Write a program that displays the following pattern:
![[Pasted image 20220317132113.png]]
```java
public static void main(String[] args) {
	System.out.println("     J" + "     A" + "     V     V" + "     A");
	System.out.println("     J" + "    A A" + "     V   V" + "     A A");
	System.out.println("J    J" + "   AAAAA" + "     V V" + "     AAAAA");
	System.out.println(" J J" + "    A     A" + "     V" + "     A     A");
 }
}
```

## 1.4
(Print a table) Write a program that displays the following table
| a   | a^2 | a^3 |
| --- | --- | --- |
| 1   | 1   | 1   |
| 2   | 4   | 8   |
| 3   | 9   | 27  |
| 4   | 16  | 64  |


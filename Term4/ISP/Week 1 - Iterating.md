# Iteration Types
## For
![[Pasted image 20220125095359.png]]

## While
![[Pasted image 20220125095407.png]]
## Do
![[Pasted image 20220125095419.png]]
## Overview
![[Pasted image 20220125095437.png]]
# Iterating
```java
public static void Iterate1() {
	ArrayList<String> sentence = new ArrayList<String>();
	sentence.add("Hello");
	sentence.add("there, ");
	sentence.add("World!");
	int size = sentence.size();
	System.out.print("Try1: ");
	for (int i=0; i<size; i++) {
		System.out.print(sentence.get(i) + " "); // use i as index
	}
	System.out.println();
}
```
```java
public static void Iterate2() {
	String[] sentence = new String[]{"Hello", "there", "World!"};
	int size = sentence.lenght;
	System.out.print("Try2: ");
	for (int i=0; i< size; i++) {
		System.out.print(sentence[i] + " ");
	}
	System.out.println();
}
```
```java
public static void Iterate3() {
	String[] sentence = new String[]{"Hello", "there", "World!"};
	System.out.print("Try3: ");
	for (String s: sentence){ /* for-each loop*/
		System.out.print(s + " ")
	}
}
```
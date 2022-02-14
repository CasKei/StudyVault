---
tags: #50.001
---
[[IS & Programming|ISP]]

# ArrayList, LinkedList
## Array
Once the array is created, its size is fixed.
```java
int[] a = new int[10];
```
## ArrayList / LinkedList
Can be used to store unlimited number of objects
![[Pasted image 20220125090625.png]]
- Operations for ArrayList and LinkedList are similar (both implemented the List interface)
- Underlying mechansms are different:
	- [[Fixed-Size Array and Linked List#Fixed-Size Array|ArrayList]] stores elements in an [[Week 1 - Java Introduction#Array|array]];
		- If [[Fixed-Size Array and Linked List#Adding an Element When Array is Full|capacity is exceeded]], a larger new array will be created and all the elements are copied to the new array
	- LinkedList stores elements in a [[Fixed-Size Array and Linked List#Linked List|Linked List data structure]]
- Have different performance for various operations
	- ArrayList is more efficient to support random access through an index
![[Pasted image 20220125091619.png]]
## Performance: Random Access
```java
public class PerformanceCheck {
	public static void main(String[] args) {
		Integer[] a = new Integer[50000];

		List<Integer> w = new LinkedList<>(Arrays.asList(a));

		long started = System.nanoTime();
		int totalCnt = 100000;

		for (int k=0; k<totalCnt; k++) {
			w.get(25000);
		}
		long time = System.nanoTime();
		long timeTaken = time - started;
		System.out.println("time taken: " + timeTaken/1000000.0 + "ms");
	}
}
```
- ArrayList: 3.3ms
- LinkedList: 4269ms
## Performance: Insertion
```java
public class PerformanceCheck {
	public static void main(String[] args) {
		Integer[] a = new Integer[50000];

		List<Integer> w = new ArrayList<>(Arrays.asList(a));

		long started = System.nanoTime();
		int totalCnt = 100000;
		
		for (int k=0; k<totalCnt; k++) {
			w.get(5,2000); //insertion
		}
		long time = System.nanoTime();
		long timeTaken = time - started;
		System.out.println("time taken: " + timeTaken/1000000.0 + "ms");
	}
}
```
- ArrayList: 1859ms
- LinkedList: 13.33ms
# Generics
Generics is a programming language design to use type as parameter.
```java
ArrayList<String> w1 = new ArrayList<String>();
ArrayList<Integer> w2 = new ArrayList<Integer>();
ArrayList<String> w3 = new ArrayList<>();
```
- Detect error at compile time rather than runtime, i.e., static checking
- More reliable
```java
ArrayList<String> I = new ArrayList<String>();
I.add("hello");
I.add("bye");
I.add("haha");
I.add(2); // error detect at compile time
```
# Comparison: Array, ArrayList, LinkedList
|Array|ArrayList|LinkedList|
|---|---|---|
|Size cannot be changed| Size can be changed|Size can be changed|
| |consecutive|  |
|  |  better for access| better for manipulation|

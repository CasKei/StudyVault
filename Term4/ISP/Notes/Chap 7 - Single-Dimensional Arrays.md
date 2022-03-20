---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 7.1 Introduction
A single array variable can reference a large collection of data.
[[Week 1 - ArrayList, LinkedList, Generics]]
An efficient, organized approach is needed. Java and most other high-level languages provide a data structure, the array, which stores a fixed-size sequential collection of elements of the same type.

## 7.2 Array Basics
Once an array is created, its size is fixed. An array reference variable is used to access the elements in an array using an index.
**Declaration**
```java
elementType[] arrayRefVar;
double[] myList;
```
Creation: Unlike declarations for primitive data type variables, the declaration of an array variable does not allocate any space in memory for the array. It creates only a storage location for the reference to an array. If a variable does not contain a reference to an array, the value of the variable is null.
```java
arrayRefVar = new elementType[arraySize];
```
Can be combined.

When space for an array is allocated, the array size must be given, specifying the number of elements that can be stored in it.
**Length of array**
```java
arr.length
```

**Default values**
When an array is created, its elements are assigned the default value of `0` for the numeric primitive data types, **`\u0000`** for char types, and `false` for boolean types.

Each element in the array is represented using the following syntax, known as an **indexed variable:** 
```java
arrayRefVar[index];
```

Java has a shorthand notation, known as the **array initializer**, which combines the declaration, creation, and initialization of an array in one statement using the following syntax: 
```java
elementType[] arrayRefVar = {value0, value1, ..., valuek};
```

**Initializing arrays with input values:**
```java
java.util.Scanner input = new java.util.Scanner(System.in); 
System.out.print("Enter " + myList.length + " values: "); 
for (int i = 0; i < myList.length; i++) 
	myList[i] = input.nextDouble();
```

**Initializing arrays with random values:**
```java
for (int i = 0; i < myList.length; i++) {
	myList[i] = Math.random() * 100;
}
```

**Displaying arrays**
```java
for (int i = 0; i < myList.length; i++) {
	System.out.print(myList[i] + " ");
}
```

**Summing all elements:**
```java
double total = 0; 
for (int i = 0; i < myList.length; i++) {
	total += myList[i]; 
}
```

**Finding the largest element:**
```java
double max = myList[0]; 
for (int i = 1; i < myList.length; i++) { 
	if (myList[i] > max) max = myList[i]; 
}
```

**Finding the smallest index of the largest element:**
```java
double max = myList[0]; 
int indexOfMax = 0; 
for (int i = 1; i < myList.length; i++) { 
	if (myList[i] > max) { 
		max = myList[i]; 
		indexOfMax = i; 
	} 
}
```

**Random shuffling:**
```java
for (int i = myList.length – 1; i > 0; i––) {
	// Generate an index j randomly with 0 <= j <= i 
	int j = (int)(Math.random() * (i + 1)); 
	// Swap myList[i] with myList[j] 
	double temp = myList[i]; 
	myList[i] = myList[j]; 
	myList[j] = temp; 
}
```

**Shifting elements**
```java
double temp = myList[0]; // Retain the first element 
// Shift elements left 
for (int i = 1; i < myList.length; i++) { 
	myList[i - 1] = myList[i]; 
} // Move the first element to fill in the last position 
myList[myList.length - 1] = temp;
```

**Foreach Loops**
Traverse arrays sequentially without using index variable.
```java
for (double e: myList) { 
	System.out.println(e);
}
```

## 7.3 Case Study: Analysing Numbers

## 7.4 Case Study: Deck of Cards

## 7.5 Copying Arrays
To copy the contents of one array into another, you have to copy the array’s individual elements into the other array.
There are three ways to copy arrays: 
- Use a loop to copy individual elements one by one. 
- Use the static arraycopy method in the System class. 
- Use the clone method to copy arrays; this will be introduced in [[Chap 13 - Abstract Classes and Interfaces]].

Loop
```java
int[] sourceArray = {2, 3, 1, 5, 10}; 
int[] targetArray = new int[sourceArray.length]; 
for (int i = 0; i < sourceArray.length; i++) { 
	targetArray[i] = sourceArray[i]; 
}
```
arraycopy in java.lang.System
```java
arraycopy(sourceArray, srcPos, targetArray, tarPos, length); // syntax
System.arraycopy(sourceArray, 0, targetArray, 0, sourceArray.length);// copy
```

## 7.6 Passing Arrays to Methods
When passing an array to a method, the reference of the array is passed to the method.

Java uses pass-by-value to pass arguments to a method. There are important differences between passing the values of variables of primitive data types and passing arrays.
- For an argument of a primitive type, the argument’s value is passed. 
- For an argument of an array type, the value of the argument is a reference to an array; this reference value is passed to the method. Semantically, it can be best described as pass-by-sharing, that is, the array in the method is the same as the array being passed. Thus, if you change the array in the method, you will see the change outside the method.

## 7.7 Returning an Array from a Method
When a method returns an array, the reference of the array is returned.

## 7.8 Case Study: Counting the Occurrences of Each Letter
This section presents a program to count the occurrences of each letter in an array of characters.

## 7.9 Variable-Length Argument Lists
A variable number of arguments of the same type can be passed to a method and treated as an array.

You can pass a variable number of arguments of the same type to a method. The parameter in the method is declared as follows: 
```java
typeName... parameterName
public static void printMax(double... numbers) {
```

## 7.10 Searching Arrays
If an array is sorted, binary search is more efficient than linear search for finding an element in the array.

Listing7.6 LinearSearch.java
```java
public class LinearSearch {
	public static int linearSearch(int[] list, int key) {
		for (int i = 0; i < list.length; i++) {
			if (key == list[i])
				return i;
		}
		return -1;
	}
}
```

Listing7.7 BinarySearch.java
```java
public class BinarySearch {
	/** Use binary search to find the key in the list */
	public static int binarySearch(int[] list, int key) {
		int low = 0; 
		int high = list.length - 1;
		while (high >= low) { 
			int mid = (low + high) / 2; 
			if (key < list[mid])
				high = mid - 1; 
			else if (key == list[mid])
				return mid;
			else
				low = mid + 1; 
		}
		return –low - 1; // Now high < low, key not found
	}
}
```

## 7.11 Sorting Arrays
Sorting, like searching, is a common task in computer programming. Many different algorithms have been developed for sorting. This section introduces an intuitive sorting algorithm: selection sort.

Listing7.8 SelectionSort.java
```java
public class SelectionSort {
	public static void selectionSort(double[] list) {
		for (int i = 0; i < list.length - 1; i++) {
			double currentMin = list[i];
			int currentMinIndex = i;
			for (int j = i + 1; j < list.length; j++) {
				if (currentMin > list[j]) {
					currentMin = list[j];
					currentMinIndex = j;
				}
			}
			if (currentMinIndex != i) {
				list[currentMinIndex] = list[i];
				list[i] = currentMin;
			}
		}
	}
}
```

## 7.12 The Arrays Class
The `java.util.Arrays` class contains useful methods for common array operations such as sorting and searching.\
The `java.util.Arrays` class contains various static methods for sorting and searching arrays, comparing arrays, filling array elements, and returning a string representation of the array. These methods are overloaded for all primitive types.
![[Pasted image 20220318100933.png]]
![[Pasted image 20220318101413.png]]
![[Pasted image 20220318101422.png]]

## 7.13 Command-Line Arguments
The main method can receive string arguments from the command line.
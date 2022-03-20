---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Textbook notes]]

## 8.1 Introduction
Data in a table or a matrix can be represented using a two-dimensional array.

## 8.2 Two-Dimensional Array Basics
An element in a two-dimensional array is accessed through a row and column index.

**Declaring and Creating**
```java
elementType[][] arrayRefVar;
elementType arrayRefVar[][]; // Allowed, but not preferred

int[][] matrix;
int matrix[][]; // This style is allowed, but not preferred
```

**Obtaining the Lengths of Two-Dimensional Arrays**
![[Pasted image 20220318102646.png]]

**Ragged arrays**
![[Pasted image 20220318102709.png]]

## 8.3 Processing Two-Dimensional Arrays
Nested for loops are often used to process a two-dimensional array.

**Initialising arrays with input values**
```java
java.util.Scanner input = new Scanner(System.in); 
System.out.println("Enter " + matrix.length + " rows and " + matrix[0].length + " columns: "); 
for (int row = 0; row < matrix.length; row++) { 
	for (int column = 0; column < matrix[row].length; column++) { 
		matrix[row][column] = input.nextInt(); 
	} 
}
```

**Initialising arrays with random values**
```java
for (int row = 0; row < matrix.length; row++) { 
	for (int column = 0; column < matrix[row].length; column++) { 
		matrix[row][column] = (int)(Math.random() * 100); 
	} 
}
```

**Printing arrays**
```java
for (int row = 0; row < matrix.length; row++) { 
	for (int column = 0; column < matrix[row].length; column++) { 
		System.out.print(matrix[row][column] + " "); 
	} 
	System.out.println(); 
}
```

**Summing all elements**
```java
int total = 0; 
for (int row = 0; row < matrix.length; row++) { 
	for (int column = 0; column < matrix[row].length; column++) { 
		total += matrix[row][column]; 
	} 
}
```

**Summing elements by column**
```java
for (int column = 0; column < matrix[0].length; column++) { 
	int total = 0; 
	for (int row = 0; row < matrix.length; row++) 
		total += matrix[row][column]; 
	System.out.println("Sum for column " + column + " is " + total); 
}
```

**Which row has the largest sum?**
```java
int maxRow = 0; int indexOfMaxRow = 0; // Get sum of the first row in maxRow 
for (int column = 0; column < matrix[0].length; column++) { 
	maxRow += matrix[0][column]; 
} 
for (int row = 1; row < matrix.length; row++) { 
	int totalOfThisRow = 0; 
	for (int column = 0; column < matrix[row].length; column++) 
		totalOfThisRow += matrix[row][column]; 
	if (totalOfThisRow > maxRow) { 
		maxRow = totalOfThisRow; indexOfMaxRow = row; 
	} 
}
System.out.println("Row " + indexOfMaxRow + " has the maximum sum of " + maxRow);
```

**Random shuffling**
```java
for (int i = 0; i < matrix.length; i++) { 
	for (int j = 0; j < matrix[i].length; j++) { 
		int i1 = (int)(Math.random() * matrix.length); 
		int j1 = (int)(Math.random() * matrix[i].length);
		int temp = matrix[i][j]; 
		matrix[i][j] = matrix[i1][j1]; matrix[i1][j1] = temp; 
	} 
}
```

## 8.4 Passing Two-Dimensional Arrays to Methods
When passing a two-dimensional array to a method, the reference of the array is passed to the method.

## 8.5 Case Study: Grading a Multiple-Choice Test

## 8.6 Case Study: Finding the Closest Pair
This section presents a geometric problem for finding the closest pair of points.

## 8.7 Case Study: Sudoku
The problem is to check whether a given Sudoku solution is correct.

## 8.8 Multidimensional Arrays
A two-dimensional array consists of an array of one-dimensional arrays and a three-dimensional array consists of an array of two-dimensional arrays.
```java
double[][][] scores = new double[6][5][2];
```
![[Pasted image 20220318103836.png]]

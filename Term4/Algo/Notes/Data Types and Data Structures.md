---
aliases: datatype, data type, data structure
tags: #50.004
---
[[Algo]]
[[Binary Heap and Heapsort]]
[[L03.01 - Heap]]

## What is a Data Type
A type of data.
e.g. string, int, double

A data type has associated operations
e.g. concatenate strings, add int. etc

We can build new data types from existing data types
e.g. matrix: with associated operations like swap rows, multiply row by scalar, rref, etc
***
## Data types versus abstract data types (ADT)
ADT: we do not specify/restrict how the assciated operations of the data type are actually implemented
- e.g. matrix data type can be considered abstract if we do not worry about the specific implementations of its associated operations e.g. rref

>An abstract data type is an **abstract mathematical model** for objects of a certain type of data, together with operations on such objects, where **this model does not depend on specific implementations or the specific programming language**.
***
## Data Structures
A format to store and organise data, in order to facilitate access and modifincation
e.g. arrays, lists

We can use a data structure to implement a data type of ADT
- Data strctures refer to the way that data is stored
- e.g. we can use several data structures to implement the matrix data type

We can build new data structures from existing data structures e.g. lists of lists
---
aliases: array
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]
[[C derived data types]]

## Making array
Creaing arrays of basic types is easy. Use the common `[]` array declaration.

Add these to main function:
```c
  int vector_int[3] = {1,2,3};  
  float vector_float[3] = {0.3,0.4,0.5};  
  char characters[5] = {'a','i','u','e','o'};  
  
  printf("Contents of vector_int %d %d %d \n", vector_int[0], vector_int[1], vector_int[2]);  
  printf("Contents of vector_float %f %f %f \n", vector_float[0], vector_float[1], vector_float[2]);  
  printf("Contents of the second char: %c\n", characters[1]);
```

Compile and output:
```
Contents of vector_int 1 2 3
Contents of vector_float 0.300000 0.400000 0.500000
Contents of the second char: i
```

==Notice the array size cannot be dynamic and has to be a constant==

If you try to compile shyt like
```c
int array_size = 3;
int vector_int[array_size] = {1,2,3};
```
You will get error:
```
error: variable-sized object may not be initialized
```

This is because `array_size` is a variable.

## Non-static
With the `[]` you are declaring an object with automatic storage duration in [[Stack and Procedures|stack]]. This means **the array lives only as long as the function that calls it exists**.

## Static
You can also declare it in **static memory** ([[C dynamic memory allocation]]) using the keyword `static`:
```c
static int vector_int[3] = {1,2,3};
```
Then the array will only be initialised once and its content static memory will persist **for as long as the program lives**, but it is also **fized in size**.

## Sizing or persists outside function
If you want to create an array with a size that is determined later during runtime, or **persists outside the function calling it** (in heap), then you should use `malloc` or `calloc` to be discussed in [[C dynamic memory allocation]].

But before that learn [[C pointer]].
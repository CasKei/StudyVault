---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

[[Hello World in C]]

## Learning Objectives
In this intro class, we will learn how to:
1.  Create .c and header files 
2.  Create, manipulate, print different primary data types
3.  Create, manipulate, print different derived data types
4.  Loops and iterations
5.  Create functions, and pass value by reference
6.  Allocate and manage memory dynamically

## Stuff
[[c and h file extensions]]
[[C primary data types]]
[[C derived data types]]
[[C loops and iterations]]
[[C functions]]
[[C dynamic memory allocation]]

## Summary
Congrats. You are now C baby.
Next
1. function pointers
2. macking system calls in C
3. error handling
4. file I/O
5. process control
6. inter-process communication means

Notes
1. Careful when declaring [[C pointer|pointer]]s and [[C array|array]]s. Remind yourself on what each decalration method means and its scope.
2. Note the difference between **initialising** and **decalring** variables **inside** or **outside** of a [[C functions|function]]. For statically allocated memory location within a function, **its scope persists**. If you invoke `function1()` below, you can still print the string "HELLO" pointed b sentence. Also, *not all [[C global, static, local variables|static]] allocated memory is read-only*. 'Read-only' is simply a flag for constants so that no instructions can modify using runtime.

```c
int x[100]; //static arr with global scope
static int y[100]; //static arr with file scope
char *sentence = "Hello world"; // static arr, global scope, contant, readonly

char* function1(){
	int z[100]; //automatic arr (local, no clear doc on where implemented, but likely in stack)
	char *sentence = "HELLO"; //static readonly arr
	return sentence;
}
```
Will compile without warning, but if you return `sentence2` it will warn you that:
```bash
warning: address of stack memory associated with local variable 'sentence2' returned [-Wreturn-stack-address]
	return sentence2;
		   ^________
```

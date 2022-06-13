---
aliases: global variable, static variable, local variable, extern, global, static, local
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]
[[C dynamic memory allocation]]

## Global variable
**Visible in the entire process (across different [[c and h file extensions|.c]] file modules).**

In the other modules, we can access the global variable declared once in any of the .c files and accessed by all others using the `extern` keyword.
[More docs](http://www.theunixschool.com/2010/05/how-to-use-extern-variable-in-c.html)

## Static variable
Only visible within the module ([[c and h file extensions|.c]] file) itself.

## Local variable
Only visible within the function scope.

## Example
Header:
```c
int global_variable;  
  
void test_global(void);  
int test_static(void);  
int test_local(void);
```

Implementations to [[c and h file extensions|.c]] file:
```c
int test_static(void){  
  static int static_variable = 20;  
  static_variable += 1;  
  return static_variable;  
}  
  
int test_local(void){  
  int local_variable = 20;  
  local_variable += 1;  
  return local_variable;  
}  
  
void test_global(void){  
  global_variable ++;  
}
```

Call in main:
```c
   printf("The global variable is %d \n", global_variable);  
  test_global();  
  printf("The global variable is now %d \n", global_variable);  
  printf("The static variable is %d \n", test_static());  
  printf("The static variable is %d \n", test_static());  
  printf("The local variable is %d \n", test_local());  
  printf("The local variable is %d \n", test_local());
```

Output:
```
The global variable is 10
The global variable is now 11
The static variable is 21
The static variable is 22
The local variable is 21
The local variable is 21
```

Hence we can see:
- Global vars typically defined in [[c and h file extensions|header file]], and can be accessed anywhere.
- Static vars can be defined within functions and still are visible outside of it.
	- Calling `test_static` the second time skips the initialisation of `static_variable`.
	- Hence we have 22 in the second call


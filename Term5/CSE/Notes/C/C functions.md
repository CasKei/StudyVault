---
aliases: functions, function
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

## Learning Points
1.  Declare functions and structs first in the header files, before using it in the .c files
2.  Function declarations must include return type and argument types  
3.  Note the difference between passing argument by value vs by reference

## Declaring return type
The functions in C must be declared first before being utilized, so that the compiler knows the return type. For example, such usage:
```c
int main(int argc, char **argv)  
{  
  float output = square(3.f);  
  printf("Output is %f \n", output);  
}  
  
float square(float a){  
  return a*a;  
}
```
Results in compilation error

This is because the compiler doesn’t know the return type of `square`, so it will set it as an `int` by default. Then later on when you declare it as `float` return type, the error is generated.

## Declaring functions that does not exist
Obviously if you try to call a function that does not exist there’s the **linker** error because the compiler doesn’t know where does this function comes from. For example calling this `function1()` when you haven’t implemented it:
```c
  function1();
```

The **correct way** is to declare your function first in the [[c and h file extensions|header file]]:
```c
#include <stdio.h>  
#include <stdlib.h>  
#include <unistd.h>  
  
  
#define BUFFERSIZE 1024  
float square(float a);
```
And then implementing it in the [[c and h file extensions|.c file]] as above.

OTHERWISE you need to implement the function **ABOVE the main() declaration**:
```c
float square(float a){  
  return a*a;  
}  
  
int main(int argc, char **argv)  
{  
  float output = square(3.f);  
  printf("Output is %f \n", output);  
}
```

To be neat, it is recommended that you always declare your functions in the [[c and h file extensions|header file]] and only implement those in the .c files. Also, declare your [[C struct|structs]] in the [[c and h file extensions|header file]].

## Declaring the function
To declare a function, you need to define the:
1.  Return type
2.  The type of each argument

For functions without any return type, we just define it as `void`. For example, add these to your [[c and h file extensions|header file]]:
```c
// defining struct  
typedef struct Vector_Int  
{  
  int x;  
  int y;  
  int z;  
  char name[64];  
}Vector;  
  
void print_vector(Vector input);
```

Implement the function in your .c file:
```c
void print_vector(Vector input){  
  printf("{x:%d, y:%d, z:%d}\n", input.x, input.y, input.z);  
}
```

And call it in the main function:
```c
  Vector v1 = {3,7,10};  
  print_vector(v1);
```

We shall have the output:
```
{x:3, y:7, z:10}
```

## Arguments being values VS references
**The two examples of functions above receives argument by value and not by reference.**

To understand this, suppose we want to implement another function that’s job is to zero all the members of Vector. Declare this in the header file:
```c
void clear_vector(Vector input);
```
And the implementation:
```c
void clear_vector(Vector input){  
  input.x = 0;  
  input.y = 0;  
  input.z = 0;  
}
```
Calling these in the main function:
```c
  Vector v1 = {3,7,10};  
  print_vector(v1);  
  clear_vector(v1);  
  print_vector(v1);
```
Results in:
```
{x:3, y:7, z:10}
{x:3, y:7, z:10}
```

That is because the input vector is a new COPY of `v1`. Hence **modifying input does NOT affect `v1`**. In order to return the cleared vector, you need to change the return type into `Vector`:
```c
Vector clear_vector(Vector input);
```
```c
Vector clear_vector(Vector input){  
  input.x = 0;  
  input.y = 0;  
  input.z = 0;  
  return input;  
}
```
In main:
```c
  Vector v1 = {3,7,10};  
  print_vector(v1);  
  v1 = clear_vector(v1);  
  print_vector(v1);
```
Results in:
```
{x:3, y:7, z:10}
{x:0, y:0, z:0}
```

**Now while this works, it is NOT efficient. We require creation and destroy of memory space during runtime.**

If we just want the function to modify the created structure or array, then we are better off by creating a function and passing its argument **by reference**.

header:
```c
void clear_vector_byreference(Vector *input);
```
implement in main:
```c
void clear_vector_byreference(Vector *input){  
  input->x = 0;  
  input->y = 0;  
  input->z = 0;  
}
```
Note how to access the member of a [[C pointer|pointer]] to a [[C struct|struct]], we can use the arrow `->` instead of a dot.

main
```c
  Vector v2 = {31,99,21};  
  print_vector(v2);  
  clear_vector_byreference(&v2);  
  print_vector(v2);
```
Results in:
```
{x:3, y:7, z:10}
{x:0, y:0, z:0}
```

However, the difference becomes clear if we print the *address* of the members of input, and compare it with the address of the members of `v1` and `v2`. Add the address print statement on the functions:
```c
Vector clear_vector(Vector input){

  printf("Address of clear_vector input members: 0x%llx, 0x%llx, 0x%llx\n", &input.x, &input.y, &input.z);  
  input.x = 0;  
  input.y = 0;  
  input.z = 0;  
  return input;  
}  
  
void clear_vector_byreference(Vector *input){  
  printf("Address of clear_vector_byreference input members: 0x%llx, 0x%llx, 0x%llx\n", &input->x, &input->y, &input->z);  
  input->x = 0;  
  input->y = 0;  
  input->z = 0;  
}
```
And call these in the main:
```c
  Vector v1 = {3,7,10};  
  printf("Address of v1 members: 0x%llx, 0x%llx, 0x%llx\n", &v1.x, &v1.y, &v1.z);  
  print_vector(v1);  
  v1 = clear_vector(v1);  
  print_vector(v1);  
  
  Vector v2 = {31,99,21};  
  printf("Address of v2 members: 0x%llx, 0x%llx, 0x%llx\n", &v2.x, &v2.y, &v2.z);  
  print_vector(v2);  
  clear_vector_byreference(&v2);  
  print_vector(v2);
```

The output is:
![[Pasted image 20220515163747.png]]

As you can see, the `clear_vector`’s input members is located in totally different address as `v1`’s. To be specific, they’re created in the [[Stack and Procedures|stack]] space of `clear_vector` function.

However for `clear_vector_byreference`, this isn’t the case. We save on memory read/write and stack space if we use passing arguments by reference.

***
When to pass arguments by value and when to pass arguments by reference?
1.  Depends on the size of the arguments. For [[C primary data types]] and small [[C struct|structs]], it doens’t make much difference
2.  It makes a lot of difference in runtime for deeply recursive functions and large [[C struct|structs]]


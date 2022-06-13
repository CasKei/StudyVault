---
aliases: malloc, calloc
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

[[Heap]]
[[Stack and Procedures|stack]]
## Where memory
This memory is allocated in the **process’ [[Heap]]** (and not [[Stack and Procedures|stack]]), and therefore it **persists even after the caller function exits**.

**You need to explicitly free the memory when it is no longer needed**, otherwise it will populate your [[Heap]] space unnecessarily.

| Permanent storage area | Stack           |
| ---------------------- | --------------- |
| Global variables       | Local variables |
| Static variables       |                 |
| Program instructions   |                 |

![](https://lh6.googleusercontent.com/ESK5v5_8W__9Te5_Nc3gtm-sBk5QK-ph6OU88om5_h7Gun5DavaDtY53WR6Fz0WA8cYCRvB03ZUaJvsA2ElsNewLbj_K591obKhb9Md2yoXud92wqXlCbf4NdI2s7iI_8iR6okToRtIUXDQH2g)

## Global, static, local variables
[[C global, static, local variables]]

## Problem: static arrays?
We can declare [[C global, static, local variables|static]] [[C array|array]]s, but we cannot have [[C dynamic memory allocation]]. e.g.
```c
int test_static(void){  
  static int static_variable = 20;  
  static_variable += 1;  
  static int static_array[static_variable];  
  return static_variable;  
}
```
Results in error:
![[Pasted image 20220515203113.png]]
```
variable length array declaration cannot have 'static' storage duration
```

## Dynamically sized array
So in order to have an [[C array|array]] which size is dynamic:
**size determined later during runtime execution, we need to use `malloc` or `calloc`.

```c
  int buffersize;  
  printf("Enter total number of elements: ");  
  scanf("%d", &buffersize);  
  
  //allocates memory in heap  
  int *x = (int*) malloc(sizeof(int)*buffersize); //type cast it  
  //print the address x is pointing to  
  printf("Memory address allocated by malloc starts at 0x%llx\n", x);  
  //print the address of the pointer x  
  printf("This pointer is stored at address 0x%llx\n", &x);  
  
  // do something with the array  
  for (int i = 0; i<buffersize; i++){  
      x[i] = i;  
  }  
  
  printf("Enter additional number of elements: ");  
  scanf("%d", &buffersize);  
  
  //resize the array, buffersize can be smaller than original amount. The remainder is automatically freed  
  //the unused memory initially pointed by x is also automatically freed  
  int *y = realloc(x, buffersize);  
  printf("Memory address allocated by realloc starts at 0x%llx\n", y);  
  printf("This new pointer is stored at address 0x%llx\n", &y);  
  for (int i = 0; i<buffersize; i++){  
      printf("Original content element %d is %d \n", i, x[i]);  
      x[i] += i; //do something with the array  
  }  
  
  //free heap manually  
  free(y);
```

Output is 
![[Pasted image 20220515203337.png]]

## malloc
1. Program asks for array size: set to 3
2. Allocate memory using `malloc(total_byte_size)`, hence arg is
	1. `sizeof(int) * buffersize`
	2. `malloc` retrns a generic [[C pointer|pointer]] to this allocated place in [[Heap]]
	3. We need to type cast it
3. Address for [[C array|array]] is initialised at `0x7fdd3fd00000`. The [[C pointer|pointer]] to this address is stored at `0x7ffee23329f0`

**Persists outside scope of calling function**
[[c and h file extensions|header file]]
```c
int* test_malloc(int size_array);
```
implementation in [[c and h file extensions|.c]] file
```c
int* test_malloc(int size_array){  
  int *x_local = malloc(sizeof(int)*size_array);  
  for (int i = 0; i<size_array; i++){  
      x_local[i] = i*i;  
  }  
  printf("Local pointer is at address 0x%llx\n", &x_local);  
  printf("Pointer is pointing to address 0x%llx \n", x_local);  
  return x_local;  
}
```
call function in main file
```c
  int *pointer = test_malloc(10);  
  printf("Returned pointer is at address 0x%llx \n", &pointer);  
  printf("Pointer is pointing to address 0x%llx \n", pointer);  
  // test print content  
  for (int i = 0; i<10; i++){  
      printf("%d ", pointer[i]);  
  }  
  printf("\n");  
  
  //free the memory allocated  
  free(pointer);
```
Output
![[Pasted image 20220515210439.png]]

Notice how the [[C array|array]] is initialised inside the function `test_malloc`.
However in main, we can still print contents and the [[C array|array]] persists.
It is located at address starting at `0x77fa41e402670`.

Address of [[C pointer|pointer]] pointing to `0x77fa41e402670` varies (was `0x7ffee9f0c9c0`, then changed to `0x7ffee9f0c9f8`), as it was the [[C global, static, local variables|local]] variable inside `test_malloc`.

### Another way of using malloc
Pass the [[C pointer|pointer]] (returned by `malloc`) to another function to modify.
Similar to [[C functions#Arguments being values VS references|functions]] where you pass by reference.
[[c and h file extensions|header file]]
```c
void modify_array(int* array, int array_size);
```
Implement in [[c and h file extensions|.c]]
```c
void modify_array(int* array, int array_size){  
  for (int i = 0; i<array_size; i++){  
      array[i] += i;  
}
```
call it in main
```c
  int buffersize;  
  printf("Enter total number of elements: ");  
  scanf("%d", &buffersize);  
  
  //allocates memory in heap  
  int *x = (int*) malloc(sizeof(char)*buffersize); //type cast it  
  
  //initialize to some value  
  printf("The original array value is : ");  
  for (int i = 0; i<buffersize; i++){  
      x[i] = i;  
      printf("%d ", x[i]);  
  }  
  printf("\n");  
  
  //pass it to the function to modofy  
  modify_array(x, buffersize);  
  
  //print its content  
  printf("The new array value is : ");  
  for (int i = 0; i<buffersize; i++){  
        printf("%d ", x[i]);  
  }    
  printf("\n");  
  
  //free it  
  free(x);
```
The output is as expected, where the array is modified by the function:
```
Enter total number of element: 5
The original array value is : 0 1 2 3 4
The new array value is : 0 2 4 6 8
```

## realloc
1. Resize the array to size 5 using `realloc(original_pointer, new_size)`
	1. If `new_size` < original, then remainder is automatically freed
	2. Else, will increase size of memory allocated for the array
	3. New array location may or may not overlap the old array
	4. `realloc` migrates the old value of the array to the new one
	5. Example shows that the new [[C array|array]] location starts at the same place as the old one, but may not be the same depending on space in [[Heap]].

## calloc
1. It seems the two new locations at at index 3 and 4 has initial values 0. Note this isn't always the case for `malloc`. `malloc` can initialise the array with garbage values as well. Use `calloc(number, sizeof(type))` for auto initialisation to 0. Otherwise with `malloc` you need to loop through the [[C array|array]] after initialisation


Note that the memory block allocated by the `malloc` or `calloc` **must be explicitly freed** using `free(pointer)`, otherwise your program might run out of [[Heap]] space.
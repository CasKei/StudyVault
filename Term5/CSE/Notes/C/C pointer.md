---
aliases: pointer
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]
[[C derived data types]]

## Pointer in array
A **pointer** data type is indicated by the * (star) sign. You can make a pointer of any [[C primary data types]] or [[C derived data types]]. The pointer simply means ==the address of the data you are pointing to.==

Paste in main:
```c
   // recall int vector_int[3] = {1,2,3};  
  int *vector_int_pointer = vector_int;  
  printf("Address of vector_int array is 0x%llx\n", vector_int_pointer);  
  printf("Address of the first element in vector_int array is 0x%llx\n", &vector_int[0]);  
  printf("Address of the second element in vector_int array is 0x%llx\n", &vector_int[1]);  
  printf("Address of the third element in vector_int array is 0x%llx\n", &vector_int[2]);  
  
  printf("Printing address using pointer : \n");  
  printf("Address of the first element in vector_int array is 0x%llx\n", vector_int_pointer);  
  printf("Address of the second element in vector_int array is 0x%llx\n", vector_int_pointer+1);  
  printf("Address of the third element in vector_int array is 0x%llx\n", vector_int_pointer+2);
```

Output:
![[Pasted image 20220513154503.png]]

We create a pointer of type `int`.
The * can stick to either side, as long as it is between the data declaration and variable name.
Meaning **it points to the address of the first int element in vector_int**.

Notice **an array is basically a pointer** so we can just `int *vector_int_pointer = vector_int;`

As seen in print format, we can **print the content of the pointer** and we have `0x7ffeec216129bc` (we have a 64 bit system so address space is huge)

This is the **address of the first element of vector_int**. You can also manually print an address of your data using the `&` operator, e.g. `&vector_int[0]`

Notice **the address of the next two elements differ by 4 bytes**.
Rmb from [[C primary data types]] the `sizeof(int)` is 32 bits (4 bytes).
The **size of a pointer, however, is 64 bits** (8 bytes).
==This means that although it is a 64 bit system, we can access memory address like a 32 bit system where it differs by just 4 bytes instead of 8!==

We also know that **array is a contiguous block of memory**.
Therefore we can obtain the address of other elements by incrementing the pointer value by 1 (word of 4 bytes), which is what we are doing here
`printf("Address of the second element in vector_int array is 0x%llx\n", vector_int_pointer+1);`
obtaining the same output at `0x7ffeec216129c0`

## Change content of int array with pointer
Paste this into main:
```c
	//change the second element of vector_int  
	printf("The original second element is %d\n", vector_int_pointer[1]);  
	vector_int_pointer[1] = 5;  
	printf("The new second element is %d\n", vector_int_pointer[1]);  
	printf("The new second element is %d\n", *(vector_int_pointer+1));
```
And you have output:
```
The original second element is 2  
The new second element is 5  
The new second element is 5
```

Hence
1. You can **access content pointed using `[i]` like in arrays**. The `[i]` means:
	1. Compute the effective address EA using `vector_int_pointer + i*4`
	2. Obtain element at `Mem[EA]`
2. OR do it manually by computing EA yourself:
	1. Add 1 word (4 bytes, not 8) into the value of `value_int_pointer`: `vector_int_pointer + 1`
	2. Obtain the element pointer to by the content of the variable explicitly using the * operator. You can read this * operator as "value at".

## Create pointers to other primary types that's not an array
Paste:
```c
	int z = 5;  
	int *z_pointer = &z;  
	
	printf("Value of z is %d \n", z);  
	printf("Z is stored in address 0x%llx\n", z_pointer);  
	printf("The pointer to Z is stored in address 0x%llx\n", &z_pointer);  
	printf("Size of Z pointer is: %d \n", sizeof(z_pointer));  
	
	// change value of z through pointer  
	*z_pointer = 6;  
	printf("The new value of z is %d\n", *z_pointer);
```

Compile and run:
![[Pasted image 20220515120245.png]]

The integer `z` is stored at address `0x7ffeeab4c97c`.\
We create a pointer to it called `z_pointer`.\
`z_pointer` itself is stored at `0x7ffeeab4c970`.\
The content of `0x7ffeeab4c970` is `0x7ffeeab4c97c`, that is the address of `z`.\
Therefore `z_pointer` is a pointer because **it does not store a content but rather an address**.

Recall its a **64 bit system, so the size of pointer is 8 bytes**.\
We can **change the value that `z_pointer` is pointing to using the * operator** too.\
Recall the other operator `&` means obtaining the address of the variable it is operated on (address of).
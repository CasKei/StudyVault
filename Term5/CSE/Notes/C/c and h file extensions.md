---
aliases: .c, .h, header file
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

## .h
These are **header files**. They typically contain:
1. Function declaration
2. Constants declaration
3. Global variables
4. Struct declaration
5. Library imports

etc, that are required by the `.c` files.
These header files are then `#include`d in `.c` files where the bulk of the main code lies.

## .c
The files that contain the actual work.

## Example
`cclass_part1.c`
```C
#include "cclass.h"  
int main(int argc, char** argv){  
  printf("Hello World!\n");  
  printf("Constant BUFFERSIZE has a value of %d \n", BUFFERSIZE);  
}
```
`cclass.h`
```c
#include <stdio.h>  
#include <stdlib.h>  
#include <unistd.h>  
  
#define BUFFERSIZE 1024
```

Save both in same folder and compile:`gcc cclass_part1.c -o out`
Run `./out`

```
Hello World!
Constant BUFFERSIZE has a value of 1024
```

Notice how the `.c` can print the amount of BUFFERSIZE, which is a constant that is declared earlier in the header file imported.

## Learning points
1.  You can **import header file** using the  `#include` keyword and the header *file name* using the quotation marks, e.g: `#include "cclass.h"`  
2.  You can **import standard libraries** using the `#include` keyword and the *arrow brackets*: `#include <stdio.h>`
3.  There are many  different C **standard libraries**. These three are the most basic ones that allow you to perform *simple system calls* such as `print`. 
4.  You can **define int/float constants** using the keyword `#define NAME value`

Technically, you can dump everything within a single .c file, but you may find that you may want to share some function declarations for many different .c files. It is convenient then to declare them earlier in a single header file that’s imported by different .c files. 

To give you some context, a single program that’s written in C can be comprised of millions of lines. One of such examples is the interpreter of your favourite language, Python. Python interpreter (the program that you call when you type python / python3 in command line to run a .py script)  is written in C.
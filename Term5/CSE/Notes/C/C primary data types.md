---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

## Learning Points
1.  Primary data types: int, float, char
2.  Use print formatting 
3.  Variable naming follow the same rule as Java:
	1.  You can’t start with a digit
	2.  Upper and lower case is treated differently (Case sensitive)
	3.  You can’t use keywords as variable names

## Data types
[[Data Types and Data Structures|Data Type]]

| Type   | Size               |
| ------ | ------------------ |
| int    | 32 bits = 4 bytes  |
| char   | 8 bits = 1 byte    |
| float  | 32 bits = 4 bytes  |
| void   | nothing, undefined |
| double | 64 bits = 8 bytes  | 

Add these lines into main function:
```c
  int x = 5;  
  float y = 3.0;  
  char a = 'a';  
  char b = 'b';  
  char c = 'c';  
  
  printf("Printing integer x: %d \n", x);  
  printf("Printing float y: %f \n", y);  
  printf("Printing characters abc: %c %c %c \n", a,b,c);  
  printf("Printing characters as ASCII: %d %d %d \n", a,b,c);  
  
  printf("Size of int is %d bytes, size of float is %d bytes, size of char is %d bytes\n", sizeof(int), sizeof(float), sizeof(char));
```

Compile and see output.

```
Printing integer x: 5
Printing float y: 3.000000
Printing characters abc: a b c
Printing characters as ASCII: 97 98 99
Size of int is 4 bytes, size of float is 4 bytes, size of char is 1 bytes
```

## Formatting
The way you print primary types needs the "formatting" (similar to Java).
`%d` : int, `%f` : float, `%c` : char, and you supply the content later on.
https://linux.die.net/man/3/printf

| Fomat | Thing                             |
| ----- | --------------------------------- |
| %c    | character                         |
| %d    | decimal integer base 10           |
| %e    | exponential floating point number |
| %f    | floating point number             |
| %i    | integer base 10                   |
| %o    | octal number                      |
| %s    | a string of characters            |
| %u    | unsigned decimal int number       |
| %x    | number in hex                     |
| %\%   | print a percentage sign           |
| \\%    | print a percentage sign                                  |

## Power of Print
Print saves you in debugging. Better than nothing. Check work. Or use a debugger like a pro.
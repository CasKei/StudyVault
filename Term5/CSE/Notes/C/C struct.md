---
aliases: struct, structs, structure, structures
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]
[[C derived data types]]

## What
There are no classes/objects in C.
The closest is called `struct`.
These are [[Data Types and Data Structures|data structures]] that contain a collection of [[C primary data types]] and [[C derived data types]].

## Declaring struct
You can declare structures using the `struct` keyword, and then declare its members. 
Paste the following to your main function:
```c
	// defining struct  
	struct Vector_Int{  
		int x;  
		int y;  
		int z;  
		char name[64];  
	};  
	
	// structure variable declaration, empty member values  
	struct Vector_Int v1;  
	
	// manual member initialization  
	v1.x = 2;  
	v1.y = 3;  
	v1.z = 10;  
	sprintf(v1.name, "Vector 1");  
	
	// structure variable auto member initialization  
	struct Vector_Int v2 = {3,5,11, "Vector 2"};  
	
	printf("Values of v1 is x:%d y:%d z:%d name: %s\n", v1.x, v1.y, v1.z, v1.name);  
	printf("Values of v2 is x:%d y:%d z:%d name: %s\n", v2.x, v2.y, v2.z, v2.name);
```

Output:
```
Values of v1 is x:2 y:3 z:10 name: Vector 1
Values of v2 is x:3 y:5 z:11 name: Vector 2
```

## Nested struct
```c
	struct Info{  
		char name[32];  
		int age;  
		struct address{  
			char area_name[32];  
			int house_no;  
			char district[32];  
		} address;  
	};  
	
	struct Info my_Info = {"Alice", 25, "Somapah Road", 8, "Upper Changi"};  
	
	printf("Name: %s, age %d, area name %s, house number %d, district %s\n", my_Info.name, my_Info.age, my_Info.address.area_name, my_Info.address.house_no, my_Info.address.district);
```

And we can print out the members:
```
Name: Alice, age 25, area name Somapah Road, house number 8 , district Upper Changi
```

### Struct variable
Since `address` is a struct that is defined in `Info`, we can also now create a `struct` variable `addrss`:
```c
	struct address my_Addrs = {"Another Road", 15, "Lower Changi"};  
	printf("Another address %s %d %s \n", my_Addrs.area_name, my_Addrs.house_no, my_Addrs.district);
```
```
Another address Another Road 15 Lower Changi
```

## Double struct, one as member
This example does the same as the nested structs example above, but now address is a member in Info

```c
	struct address  
	{  
		char area_name[32];  
		int house_no;  
		char district[32];  
	};  
	
	struct Info  
	{  
		char name[32];  
		int age;  
		struct address address; //now this is a member  
	};  
	
	struct Info my_Info = {"Alice", 25, "Somapah Road", 8, "Upper Changi"};  
	
	printf("Name: %s, age %d, area name %s, house number %d, district %s\n", my_Info.name, my_Info.age, my_Info.address.area_name, my_Info.address.house_no, my_Info.address.district);  
	
	struct address my_Addrs = {"Another Road", 15, "Lower Changi"};  
	printf("Another address %s %d %s \n", my_Addrs.area_name, my_Addrs.house_no, my_Addrs.district);
```

```
Name: Alice, age 25, area name Somapah Road, house number 8 , district Upper Changi
```

## Byte size
> The byte size of structures is roughly the sum size of its members.

```c
	struct Vector_Int{  
		int x;  
		int y;  
		int z;  
		char name[64];  
	};  
	
	struct Vector_Int vector_sample;  
	
	printf("Size of Vector_Int struct is %d bytes\n", sizeof(struct Vector_Int));  
	printf("Size of its members are x %d bytes, y %d bytes, z %d bytes, and name %d bytes\n", sizeof(vector_sample.x), sizeof(vector_sample.y), sizeof(vector_sample.z), sizeof(vector_sample.name));
```
```
Size of Vector_Int struct is 76 bytes
Size of its members are x 4 bytes, y 4 bytes, z 4 bytes, and name 64 bytes
```
**This is because each int is 4 bytes, and the char is 64 bytes: 12 + 64 = 76 bytes.**

## Array of structures
[[C array|array]]
Just treat structs like a new datatype that is a collection of [[C primary data types]] and [[C derived data types]].

```c
  struct Info many_info[3] = {{"Alice", 25, "Somapah Road", 8, "Upper Changi"},  
                              {"Bob", 22, "Somapah Road", 19, "Upper Changi"},  
                              {"Michael", 30, "Another Road", 25, "East Changi"}};  
  
  for (int i = 0; i < 3; i++)  
  {  
      printf("Name: %s, age %d, area name %s, house number %d, district %s\n", many_info[i].name, many_info[i].age, many_info[i].address.area_name, many_info[i].address.house_no, many_info[i].address.district);  
  }
```
```
Name: Alice, age 25, area name Somapah Road, house number 8, district Upper Changi
Name: Bob, age 22, area name Somapah Road, house number 19, district Upper Changi
Name: Michael, age 30, area name Another Road, house number 25, district East Changi
```

## Neaten up the code
Use `typedef` is a keyword used in C language to **assign alternative names to existing datatypes**.
It is mostly used with user defined datatypes, when names of the datatypes become slightly complicated to use in programs.

So in the e.g. below, we can rename `struct Info` into just `InfoData` so that things look neater:

```c
  typedef struct Info InfoData;  
  InfoData many_info[3] = {{"Alice", 25, "Somapah Road", 8, "Upper Changi"},  
                              {"Bob", 22, "Somapah Road", 19, "Upper Changi"},  
                              {"Michael", 30, "Another Road", 25, "East Changi"}};  
  
  for (int i = 0; i < 3; i++)  
  {  
      printf("Name: %s, age %d, area name %s, house number %d, district %s\n", many_info[i].name, many_info[i].age, many_info[i].address.area_name, many_info[i].address.house_no, many_info[i].address.district);  
  }
```

The output is of course the same
```
Name: Alice, age 25, area name Somapah Road, house number 8, district Upper Changi
Name: Bob, age 22, area name Somapah Road, house number 19, district Upper Changi
Name: Michael, age 30, area name Another Road, house number 25, district East Changi
```

## Size of struct
Previously we say that structure size is roughly the sum of its members, but may not be exact.
The members of a struct are **allocated as contiguous blocks of memory**.
However, remember that int 32 bit, float 32 bit, char 8 bit.
So what happens if you have 3 chars and 1 float inside a struct?
The total number of "bytes" used is 1 each foreach char and 4 bytes for a float = 7 bytes.
Just like tetris, the size of the struct depends on the *order of declaration of the attributes*.

The compiler will **pad** unused bytes accordingly.

```c
#include <stdio.h>  
#include <string.h>  
/*  Below structure1 and structure2 are same.  
  They differ only in member's allignment */  
struct structure1  
{  
      int id1;  
      int id2;  
      char name;  
      char c;  
      float percentage;  
};  
struct structure2  
{  
      int id1;  
      char name;  
      int id2;  
      char c;  
      float percentage;                      
};  
int main()  
{  
  struct structure1 a;  
  struct structure2 b;  
  printf("size of structure1 in bytes : %d\n",  
          sizeof(a));  
  printf ( "\n   Address of id1        = 0x%llx", &a.id1 );  
  printf ( "\n   Address of id2        = 0x%llx", &a.id2 );  
  printf ( "\n   Address of name       = 0x%llx", &a.name );  
  printf ( "\n   Address of c          = 0x%llx", &a.c );  
  printf ( "\n   Address of percentage = 0x%llx",  
                  &a.percentage );  
  printf("   \n\nsize of structure2 in bytes : %d\n",  
                  sizeof(b));  
  printf ( "\n   Address of id1        = 0x%llx", &b.id1 );  
  printf ( "\n   Address of name       = 0x%llx", &b.name );  
  printf ( "\n   Address of id2        = 0x%llx", &b.id2 );  
  printf ( "\n   Address of c          = 0x%llx", &b.c );  
  printf ( "\n   Address of percentage = 0x%llx\n",  
                  &b.percentage );  
  return 0;  
}
```
```
size of structure1 in bytes : 16

	Address of id1 = 0x7ffeed60aa48
	Address of id2 = 0x7ffeed60aa4c
	Address of name = 0x7ffeed60aa50
	Address of c = 0x7ffeed60aa51
	Address of percentage = 0x7ffeed60aa54

size of structure2 in bytes : 20

	Address of id1 = 0x7ffeed60aa30
	Address of id2 = 0x7ffeed60aa34
	Address of name = 0x7ffeed60aa38
	Address of c = 0x7ffeed60aa3c
	Address of percentage = 0x7ffeed60aa40
```
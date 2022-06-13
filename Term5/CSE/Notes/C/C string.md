---
aliases: string, strings
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]
[[C derived data types]]

## What are strings
An array of characters.
```c
	char hello_world[12] = {'h','e','l','l','o',' ','w','o','r','l','d'};  
	printf("%s", hello_world);
```

![[Pasted image 20220515130658.png]]

Some garbage content at end. Because:
**`printf` with `%s` format will keep printing until it finds a NULL terminated character.**

Fix this with a null termination character such as `NULL` or `\0`
```c
	char hello_world[12] = {'h','e','l','l','o',' ','w','o','r','l','d', '\0'};  
	printf("%s\n", hello_world);
```

Then output will just print "hello world"

## String literal OR constant
It tedious to type characters one by one. 
Since a string is just an array of characters and a pointer works the same way as array identifiers, we can simply create a string using a `char` pointer.

This is called string literal (or equivalently, constant):
```c
	//allocates in a read-only portion of static memory, NOT modifiable, READ only  
	char *hello_world_readonly = "hello world";  
	printf("%s\n", hello_world_readonly);
	printf("Size of hello_world_better pointer %d\n",sizeof(hello_world_readonly));
```

NULL termination is conveniently automatically added for you.
```
hello world
Size of hello_world_better pointer 8
```

## Modifiable string
```c
	char hello_world_init[] = "hello world";  
	//change the letter in the string  
	hello_world_init[1] = 'u';  
	printf("The new string is %s\n", hello_world_init);
```
Previously the method is allocated in *read-only memory* which *cannot be modified during runtime.*

Initialising it with the `[]` **within a function** implies that it will be allocated in **heap/stack** (no formal documentation on this but this is usually how it is implemented).

```
The new string is hullo world
```

If you try to modify the static read-only string literal helloworld:
```c
	//allocates in a read-only portion of static memory, NOT modifiable, READ only  
	char *hello_world_readonly = "hello world";  
	printf("%s\n", hello_world_readonly);  
	
	hello_world_readonly[1] = 'u'; //this results in unpredictable behavior  
	printf("The new string is %s\n", hello_world_readonly);
```

error:
```
hello world
zsh: bus error ./out
```

## Define size
A very common way to initialise a string is by defining a size to the array declaration as an empty string. Then we can print strings to it using `sprintf`. It overwrites the entire buffer.

```c
	char sentence[BUFFERSIZE] = "";  
	sprintf(sentence, "Hello World");  
	printf("The sentence is: %s \n", sentence);  
	sprintf(sentence, "This is another sentence overwriting the previous one. Lets write a number %d. ", 5);  
	printf("The sentence now is modified to: %s \n", sentence);
```

You can use the same print fomats as `printf`. Of course, size of the buffer has to be big enough. Recall BUFFERSIZE is a constant defined in [[c and h file extensions|header file]].

```
The sentence is :Hello World
The sentence now is modified to: This is another sentence overwriting the previous one. Lets write a number 5.
```

## Concatenate 2 strings
Use `strcat(char *dest, char *source)`
```c
	char sentence_append[64] = "The quick brown fox jumps over a lazy dog";  
	strcat(sentence, sentence_append);  
	printf("%s \n", sentence);
```

The content of the second array is appended at the NULL termination of the first sentence, hence forming a new sentence:

```
The sentence now is modified to: This is another sentence overwriting the previous one. Lets write a number 5. The quick brown fox jumps over a lazy dog
```

## Operations
There are a whole lot of operations. The 9 most commonly used functions in the string library are:
- `strcat` - concatenate 2 strings
- `strchr` - string scanning operation
- `strcmp` - compare 2 strings
- `strcpy` - copy a string
- `strlen` - get string length
- `strncat` - concatenate one string with part of another
- `strncpy` - copy part of a string
- `strrchr` - string scanning operation
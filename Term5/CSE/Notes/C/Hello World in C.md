---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

## Code
`hello.c`
```C
#include <stdio.h>
int main()
{
	printf("Hello, World!");
	return 0;
}
```

Save it in directory of choice and `cd` into that directory.
To run, type
```bash
$ gcc -o directory hello.c
$ ./directory
```

And you should see the output.

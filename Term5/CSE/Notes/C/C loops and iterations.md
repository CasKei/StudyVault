---
aliases: loop, iteration
tags: 50.005
---
[[50.005 Computer System Engineering]]
[[C basics for babies]]

## Learning Points
1.  Three ways to perform loops: for-loop, while-loop, do-while loop
2.  Do-while loops execute the body at least once because it performs checks after
3.  break loops, or continue (same like Java, Python)
4.  Scope of loops for variables initialized inside or outside the loop

## For, while, do-while
Nothing new
```c
   float array_floats[8];  
  for (int i = 0; i<8; i++){  
      array_floats[i] = (float) i/8;  
      printf("%f, ", array_floats[i]);  
  }  
  printf("\n");  
  
  int i = 0;  
  while(i < 8){  
      array_floats[i] += 0.5f;  
      printf("%f, ", array_floats[i]);  
      i ++;  
  }  
  printf("\n");  
  
  i = 0;  
  do{  
      array_floats[i] -= 0.5f;  
      printf("%f, ", array_floats[i]);  
      i ++;  
  }while(i<8);  
  printf("\n");
```

![[Pasted image 20220515160453.png]]

In terms of execution time, the do-while loop might be a little faster. In the code above, the check  i<8 is done exactly 8 times in the do-while loop, but it is done 9 times in the while-loop.

## Break
You can also break out of the loop using the keyword break.

## Initialisation within loops
e.g. compare the two:
```c
  for (int i = 0; i<128; i++){  
      char c = i;  
      printf("%c ", c);  
  } // c does not exist out of the for-loop scope  
  
   
  char c;  
  for (int i = 0; i<128; i++){  
      c = i;  
      printf("%c ", c);  
  }  
  //c exists, as 127  
  printf("final c: %c.\n", c); //its a space
```

The difference between the two for-loops is the char c initialization. It is reinitialized in each loop for the first one, but initialized only once in the second loop. ==It might seem like the second loop is more efficient, but it does not make any much difference with modern compilers, since it is able to optimize the code above.== **In fact, the code above is safer because the scope of each variable is limited for within that ONE loop only.**


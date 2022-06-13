---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]

## Compile stuff
We can also compile and run programs from the **command** line, provided that you have the [[Interpreter and Compiler|compiler or interpreter]], e.g. `python3`, `gcc`, or `javac`.

To demonstrate this idea, download this starter code: `git clone https://github.com/natalieagus/makeFileDemo.git`

Read all the `.c` and `.h` files and get an understanding of what each file is supposed to do. To **compile** the files and **run** the executable:

1.  Navigate to this directory and type the command: `gcc -o prog.o main.c hello.c factorial.c binary.c`
2.  And then execute by typing `./prog.o`

Experiment with the program a little bit. You should see a prompt for you to key in a number. Simply type something and press enter.

![](https://natalieagus.github.io/50005/assets/images/lab1/21.png)

In case you haven’t connected the dots, `gcc` compiles all the input argument files: `main.c, hello.c, factorial.c, binary.c` and produces a binary **output** (this is what `-o` means) named `prog.o` which you can execute using `./prog.o` .

## Makefile
In this simple context, it is feasible to type out the source file one by one each time you want to compile your program. However in a large scale project with thousands of files, it is very tedious to type the compilation command all the time. Hence, the make command allows us to compile these files more easily. It requires a special file called the `makefile`.

1.  Now instead of typing gcc and all that above, type `make` instead
2.  After executing `make`, realize that prog.o is made. You can run the executable in the terminal by typing `./prog.o` or by simply clicking that executable in your shell GUI (your desktop).

Lets now examine how makefile is made.
```bash
# Define required macros here
REMOVE = rm
CC = gcc
DEPENDENCIES = main.c hello.c factorial.c binary.c
OUT = prog.o

# Explicit rules, all the commands you can call with make 
# (note: the <tab> in the command line is necessary for make to work) 
# target:  dependency1 dependency2 ...
#       <tab> command

#Called by: make prg 
#also executed when you just called make. This calls the first target. 
prog: main.c hello.c factorial.c binary.c
        gcc -o prog.o main.c hello.c factorial.c binary.c 

prog1: $(DEPENDENCIES)
        $(CC) $(DEPENDENCIES) -o $(OUT)

prog2: main.o hello.o factorial.o binary.o
        gcc -o prog2 main.o hello.o factorial.o binary.o


##make clean will remove myexecoutprog.o from the directory
clean:
        rm prog.o

clean1: 
        $(REMOVE) $(OUT)

clean2:
        rm prog2 *.o

#Implicit rules
main.o : main.c functions.h
factorial.o: factorial.c functions.h
hello.o: hello.c functions.h
binary.o: binary.c functions.h
```
1.  The first four lines are the MACROS, which are convenient shorthands you can make to make your life easier when typing these codes.
2.  Afterwards, there’s a bunch of explicit rules that you can call using make. So in this makefile, you can try calling these in sequence and observe what each rule do:
    -   `make prog`
    -   `make prog1`
    -   `make clean`
    -   `make clean1`

## Recompilation
Run this command consecutively:

-   `make clean`
-   `make prog2`

You should see the following output on your terminal as a result of `make prog2`: ![](https://natalieagus.github.io/50005/assets/images/lab1/22.png)

Now open `binary.c` in the `nano` and add another instruction in it, eg a `printf` function at the end: ![](https://natalieagus.github.io/50005/assets/images/lab1/23.png)

When you try to `make prog2` again, the output shows that we only compile files concerning `binary.c` and **not all files are recompiled**. Scroll down to the end of the makefile, and notice there’s **implicit** rules there to determine dependencies.

![](https://natalieagus.github.io/50005/assets/images/lab1/24.png)

This gives more **efficient** compilation. It only recompiles parts that are changed. The Figure below shows the data dependency between files that are specified in the makefile. Note: `File_1` → `File_2` means that `File_2` depends on `File_1`.
![](https://natalieagus.github.io/50005/assets/images/lab1/25.png)

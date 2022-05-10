---
aliases:
tags: #50.002
---
[[Comp Struct]]
[[Assemblers and Compilers]]

We are naturally more accustomed to higher level language. They’re more readable, concise, and portable.

Some higher level languages, like Java and C/C++ have to be **compiled** first using its respective **compilers** (`javac` for Java or `GCC` for C/C++), resulting in an executable (a sequence of binary instructions directly understandable by the CPU).

Compilers typically go through sophisticated steps of analysing the entire high-level source code to produce an optimized set of instructions for the machine. We will not be able to execute the program if the compiler meets an error, hence making it comparatively harder to debug. It slows down program _development_ but it will result in faster execution.

## Interpreter

Other languages like Python and Ruby are **_interpreted_**. The **interpreter** for these languages execute the program directly, often by translating each statement into a sequence of one or more standard subroutines, and finally into machine code.

There’s not too much _analysing_ of source code done, and will translate the program on the fly. It will execute the program until the first error is met, hence debugging will be comparatively easier than debugging compiled languages.

## Compiling Expressions
In this course, we will not dive into how compilers, assemblers, or interpreters work in too much detail. In fact, we are going to **hand compile** the high-level language (we will use C) ourselves into beta assembly (and then hand assemble them into the binary executable).

Don’t worry. Compilation to _unoptimized_ code is pretty straightforward. You won’t be required to write C-code either, only to read them.

There are several rules to keep in mind in order to do this well:
-  **Variables are assigned** to memory locations and accessed via `LD` and `ST`
-   Operators **translate** to [[Anatomy of the Beta CPU#ALU|ALU]]  [[Beta Datapaths#OP Datapath|`OP`]]
    -   Small constants translate to `c` (literal-mode) [[Anatomy of the Beta CPU#ALU|ALU]] instructions
    -   Large constants must be loaded to registers first
-   Conditionals and loops involve `BEQ` or `BNE` [[Beta Datapaths#Control Transfer Datapath]]

Let’s dive into simple examples to make this clearer.
To aid your learning, copy each snippet to `bsim` and observe the instruction execution step by step.

### Basic Variable Declarations
```C
int x,y;
x = 20
y = x + 5
```
```cpp
.include beta.uasm

LD(R31, x, R1)		| load the content of memory address x to R1
ADDC(R1, 5, R0)	| now that '20' is in R1, add it with 5, store it at R0
ST(R0, y, R31) 		| store the result (at R0) to location y
HALT()

x : LONG(20)	| label x points to where 20 is stored
y : LONG(0)		| label y points to where 0 is stored
```

### Arrays
```c
int x[5];
x[0] = 12; 
x[1] = 13;
x[2] = x[0] + x[1];
```
```cpp
.include beta.uasm

ADDC(R31, 12, R0)	| supposed content of x[0]
ST(R0, x)			| store '12' in R0 at address x
ADDC(R31, 13, R1)	| supposed content of x[1]
ADDC(R31, 4, R2) 	| index 1 (x[1] -> x+4)
ST(R1, x, R2)    	| store '13' in R1 at address (x+4)
ADD(R0, R1, R3) 	| x[0] + x[1] = 25
ADDC(R31, 8, R2) 	| index 2 (x[2] -> x+8)
ST(R3, x, R2) 		| store '25' in R3 at address (x+8)
HALT()

x : .
```
### Conditionals and Loops
```c
int n = 20;
int r = 1;

while (true){
	if (n <= 0) break;
	r = r*n;
	n = n-1;
}
```
```haskell
.include beta.uasm

LD(R31, n, R1)
LD(R31, r, R2) 

check_while: CMPLT(R31, R1, R0)	| compute whether n > 0
BNE(R0, while_true, R31) | if R0 != 0, go to while_true
ST(R2, r, R31)			 | store the result to location 'r'
HALT()

while_true: MUL(R1, R2, R2) | r = r*n
SUBC(R1, 1, R1) 			| n = n-1
BEQ(R31, check_while, R31) 	| always go back to check_while

n : LONG(20)
r : LONG(1)
```

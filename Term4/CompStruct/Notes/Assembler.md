---
aliases:
tags: #50.002
---
[[Comp Struct]]
[[Assemblers and Compilers]]

> An assembler is a *machine specific* program for writing programs. It also can be called as a _primitive compiler_.

It provides:
- A symbolic **language** (assembly language) for representing strings of bits. (`beta.uasm` in this course)
- A program for **translating assembly source code to machine code in binary**. (`bsim` in this course)

## UASM
In order to write a code thats runnable in BSIM conveniently, we need:
-   A **symbolic language** (UASM) for representing strings of bits
-   A Program for translating UASM source code into binary.

![[Pasted image 20220221093744.png]]
A UASM source file contains, in symbolic text, **values of successive bytes to be loaded into memory.** We can define various things in UASM source file:

### Basic values
**Decimals**, **binary** (with `0b` prefix), and **hexadecimal** (with `0x` prefix) – all will be loaded (from low to high address) as 1 byte each, separated by spaces.

For example,`5 6 7 8` will result as `08 07 06 05` in memory. Anything more than 256 (1 byte: 2^828): `256 257 258 259` will be truncated into 1 byte only, and resulted as the following in memory (only remainder left): `03 02 01 00`

### Symbols
Defined by the `=` sign allows us to “rename” basic values (like defining variables):
```haskell
x = 0x1000
y = 0x1004

R0 = 0 
R1 = 1
```

### Special Variable `.` 
 `.` (period): means _next_ byte address to be filled:
 ```haskell
. = 0x100
ADDC(R0, 3, R1) | means to load this instruction at address 0x100
 ```
 ### Labels
Symbols that represent memory addresses. Defined using `:` syntax:
 ```haskell
 . = 0x108
ADDC(R31, 3, R1)

| begin_loop is a label the address of SUBC instruction 
begin_loop : SUBC(R1, 3, R1)  
BEQ(R1, begin_loop, R31)
 ```
 `ADDC` is loaded at (byte) address `0x108`. Since `ADDC`’s length is 4 bytes, `SUBC` is loaded at the subsequent address : `0x10C`.

 ### Macroinstructions
Parameterized abbreviations, or shorthand.
-   These two macros, `WORD` and `LONG` allows us to assemble input `x` that is more than 256 into longer streams of bytes
-   There are two ways of storing bytes in memory: the **little endian** format where lowest byte stored at the lowest address and vice versa, and the **big endian** format where the highest byte is stored at the lowest address and vice versa.
-   The beta CPU follows the **little-endian** format

```haskell
.macro WORD(x) x%256 (x/256)%256 
.macro LONG(x) WORD(x) WORD(x >> 16)
```
For example, suppose we want to store the word `0xDEADBEEF` to memory address `0x0`. We start by loading `0xEF` to address `0x0`, then `0xBE` to address `0x1`, and so on. This is so tedious to do. Using the **macro**: `LONG(0xDEADBEEF)` has the same effect as storing: `0xEF 0xBE 0xAD 0xDE` to memory in sequence from low to high memory address, resulting in the following:

| Address | 0x0  | 0x1  | 0x2  | 0x3 |
| ------- | ---- | ---- | ---- | --- |
| Content | 0xEF | 0xBE | 0xAD | 0xDE    |

If one were to store `0xDEADBEEF` in big-endian format, it will result in:

| Address | 0x0  | 0x1  | 0x2  | 0x3  |
| ------- | ---- | ---- | ---- | ---- |
| Content | 0xDE | 0xAD | 0xBE | 0xEF |

**Note** that our `bsim.jar` program displays the memory address the other way around, that is **high address** on the **left** and **low address** on the **right**, so our little-endian format in $\beta$ _looks like_ the big-endian format for easy debugging:

| Address | 0x3  | 0x2  | 0x1  | 0x0  |
| ------- | ---- | ---- | ---- | ---- |
| Content | 0xDE | 0xAD | 0xBE | 0xEF |

β instructions are also created by writing **convenient** **macroinstructions**. For example, we want to load the following instruction into memory: `110000 00000 01111 1000 0000 0000 0000` The above is an `ADDC` instruction, to add contents of `R15` with `-32768` and store it at `R0`.

**Without any symbols**, would need to write them as: `0b00000000 0b10000000 0b00011111 0b11000000` to be loaded properly where the `OPCODE` is stored at a higher address than `Rc`, and `Rc` is at a higher memory address than `Ra`, and 16-bit constant `c` is at the lowest memory address of the entire word.

But the above is so unintuitive! We need to chop the original instruction into 1 byte chunks and “load” them from right to left so they’re stored from lowest to highest memory location to follow the little-endian format.

Better yet, we can define a macro called `betaopc` and `ADDC` that relies on the former:
Also `betaop`
```haskell
.macro betaop(OP, RA, RB, RC) {
	.align 4 | each instruction is 4 bytes
	LONG((OP<<26) + ((RC%32)<<21) + ((RA%32)<<16) + ((RB%32)<<11))
}
.macro ADD(RA,RB,RC) betaop(0x20,RA,RB,RC)
```

```haskell
.macro betaopc(OP,RA,CC,RC) {
	.align 4
	LONG((OP<<26)+((RC%32)<<21)+((RA%32)<<16)+(CC % 0x10000))
}
.macro ADDC(RA,C,RC) betaopc(0x30,RA,C,RC)
```
Then we can utilise it easily to load our instruction above in a more intuitive way:
```haskell
ADDC(R15, -32768, R0)
```

**In summary,** the file `beta.uasm` given for your lab provides support for all \betaβ instructions so that we can write instructions for beta in a _much more intuitive way without caring about the details on how to load these values properly into memory_ (**abstraction provided**).

```haskell
| BETA Instructions:

|| OP instructions
.macro ADD(RA,RB,RC) betaop(0x20,RA,RB,RC)
.macro AND(RA,RB,RC) betaop(0x28,RA,RB,RC)
.macro MUL(RA,RB,RC) betaop(0x22,RA,RB,RC)

|| OPC instructions
.macro ADDC(RA,C,RC) betaopc(0x30,RA,C,RC)
.macro ANDC(RA,C,RC) betaopc(0x38,RA,C,RC)
.macro MULC(RA,C,RC) betaopc(0x32,RA,C,RC) 

...
|| Memory Access instructions
.macro LD(RA,CC,RC) betaopc(0x18,RA,CC,RC)
.macro ST(RC,CC,RA) betaopc(0x19,RA,CC,RC)
.macro LDR(CC, RC) betabr(0x1F, R31, RC, CC)
...

|| Transfer Control instructions
.macro betabr(OP,RA,RC,LABEL)	betaopc(OP,RA,((LABEL-.)>>2)-1, RC)
.macro JMP(RA, RC) betaopc(0x1B,RA,0,RC)
.macro BEQ(RA,LABEL,RC) betabr(0x1D,RA,RC,LABEL)
.macro BNE(RA,LABEL,RC) betabr(0x1E,RA,RC,LABEL)
...
```
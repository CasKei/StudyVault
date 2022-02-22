---
aliases:
tags: #50.002
---
[[Comp Struct]]
## Overview
Goal of this chapter to help us understand how to improve the [[Turing Machine and Programmability#Programmability|programmability]] of the [[Building Beta CPU|beta]] (or any [[Designing an Instruction Set#Beta Instruction Set Architecture|ISA]]) in general.
The beta machine language is [[Basics of Information|encoded]] into 32-bit instructions each:

For example, the 32-bit `ADD` instruction is: 
`100000 | 00100 | 00010 | 00011 | 00000000000`

The [[Building Beta CPU|beta]] understands it as `Reg[R4] = Reg[R2] + Reg[R3]`

However, most of us would prefer to write: `ADD(R2, R3, R4)`, or even `a = b+c` because we couldn’t care less which registers are used as long as the [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] can add two variables together and produce the correct result.

We need to improve the programmability and usability of our machine by **providing abstraction**.

We can do this by writing various **softwares** that allow us to abstract some details so that it is easier to fulfil our tasks.

## Content
[[Abstraction]]
[[Assembler]]
[[Interpreter and Compiler]]

## Summary
There are a lot of ways to translate higher level language into a lower level language. The examples given above are not necessarily the _most optimised_ way, for example, we can ask ourselves:

-   Is it possible to reduce the number of instructions?
-   Is it possible to reduce the amount of `LD` and `ST`?

The examples above are also not exhaustive. There are several undiscussed parts:
-   How do we reuse boilerplate code?
-   How do we write functions? Declare structures?
-   Where do we keep local variables?

> We will address them in the [[Stack and Procedures|next chapter]].

Note that optimization in compilation is not a trivial task. For now, don’t worry too much about it. We simply only need to hand assemble C into beta assembly language, and have a general idea on what a compiler, interpreter, and assembler are for – that is to enhance the programmability of a computer by providing **software abstraction.**
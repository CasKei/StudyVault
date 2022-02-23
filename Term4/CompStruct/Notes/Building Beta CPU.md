---
aliases: beta CPU
tags: #50.002
---
[[Comp Struct]]

## Exam cheats
[[beta instruction + schematic + truth table]]


## Overview
We were introduced to the [[Designing an Instruction Set#Beta ISA Format|beta ISA]], a [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] [[Designing an Instruction Set#Preview The Beta CPU|blueprint]] that specifies what instructions the CPU can process, how it interacts with the [[Designing an Instruction Set#Memory Unit|memory unit]], the [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] components, [[Designing an Instruction Set#High Level language Assembly Language and Machine Language|instruction formats]], and many more.

In this chapter, we will study how each of the 32 beta isntructions is supposed to work, and how the beta CPU (an implementation of the beta ISA) is able to compute each and every one of them by reprogramming its datapath without physically changing its hardware.

The key is to have a proper [[Anatomy of the Beta CPU#Control Logic Unit|Control Logic Unit]] that is able to **_decode_** current instruction’s `OPCODE` and give out the correct control signals (PCSEL, RA2SEL, ASEL, etc) to reprogram the datapath. The complete truth table of the control logic unit is as shown below,
![[Pasted image 20220220100706.png]]
> This unit can be easily implemented using a [[Logic Synthesis#Read-Only-Memories ROM|ROM]].

We will go through the workings of each instruction and understand how the given beta datapath is able to execute the instruction properly by producing appropriate control signals as shown above.

## Contents
[[Beta Instruction Cycles]]
[[Anatomy of the Beta CPU]]
[[Beta Datapaths]]
[[Beta Exception Handling]]
[[CPU reset]]
[[CPU Benchmarking]]

## Summary
You may want to watch the post lecture videos here:

-   [Part 1: Beta Datapath](https://youtu.be/IXiSoP_0Kvc)
-   [Part 2: Beta Datapath Analysis - this is difficult!](https://youtu.be/4MmUEeAKmxc)

In this notes we have covered extensively how to create the beta CPU datapath given its ISA (blueprint). We can run some instructions written in machine language (`0`s and `1`s), but obviously it is not yet user friendly at all. Not to mention that this CPU alone _does not support reusable instructions_ (we know them as **functions**). The next lecture introduces us to [[Assemblers and Compilers]], which are softwares created to help us utilise the beta CPU better so that we are focused on _programming_ it and spending more time thinking about designing our program, and less time _writing_ the program.
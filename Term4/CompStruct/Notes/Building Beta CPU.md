---
aliases: beta
tags: #50.002
---
## Overview
We were introduced to the [[Designing an Instruction Set#Beta ISA Format|beta ISA]], a [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] [[Designing an Instruction Set#Preview The Beta CPU|blueprint]] that specifies what instructions the CPU can process, how it interacts with the [[Designing an Instruction Set#Memory Unit|memory unit]], the [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] components, [[Designing an Instruction Set#High Level language Assembly Language and Machine Language|instruction formats]], and many more.

In this chapter, we will study how each of the 32 beta isntructions is supposed to work, and how the beta CPU (an implementation of the beta ISA) is able to compute each and every one of them by reprogramming its datapath without physically changing its hardware.

The key is to have a proper [[Control Logic Unit]] that is able to **_decode_** current instruction’s `OPCODE` and give out the correct control signals (PCSEL, RA2SEL, ASEL, etc) to reprogram the datapath. The complete truth table of the control logic unit is as shown below,
![[Pasted image 20220220100706.png]]
> This unit can be easily implemented using a [[Logic Synthesis#Read-Only-Memories ROM|ROM]].

We will go through the workings of each instruction and understand how the given beta datapath is able to execute the instruction properly by producing appropriate control signals as shown above.

## Contents
[[Beta Instruction Cycles]]
[[Antomy of the Beta CPU]]
[[Control Logic Unit]]
[[Beta Datapaths]]
[[Beta Exception Handling]]
[[CPU reset]]
[[CPU Benchmarking]]
---
tags: #50.002
---
[[Comp Struct]]
[[Building Beta CPU]]
## Instruction Fetch
First thing a CPU must do:
- Compute the address of the instruction to execute next `ia[31:0]`
- Fetch (read) them from the Physical Memory Unit (RAM)

Instructions are produced by a compiler and are specific to the [[Designing an Instruction Set#Central Processing Unit CPU|CPU's]] [[Designing an Instruction Set#Beta Instruction Set Architecture|ISA]]. The [[Designing an Instruction Set#Central Processing Unit CPU|control unit in CPU]] will know what control signals to produce and which signals need to be _routed_ where for each type of instruction.


For example, when you double-click (run) an executable `.exe` on Windows, the code for that program is moved from Disk into the Memory Unit (RAM), and the CPU is told what address the first instruction of that program starts at.

The CPU **always** maintains an internal register called the Program Counter (PC) that holds the memory location of the next instruction to be executed.


Once the CPU knows the address of the very first instruction to be executed, it can fetch that first instruction from the Memory Unit and execute it. Figuring out the addresses of the subsequent instructions is easy:
-   The first instruction will then tell the CPU what to do next, where is the second instruction, and so on.
-   The second instruction will also tell the CPU what to do next, where is the third instruction, and so on.
-   This is repeated until the CPU met a `HALT()` instruction.

As of now, you always assume that the content of the PC [[Sequential Logic#Edge-Triggered D Flip-Flop Register|register]] is always initially zero (32-bit of zeroes), and that the first line of your program instruction is always put at memory address zero (`0x00000000`).

## Instruction Decoding
When the [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] has an instruction, it needs to figure out (decode) specifically what type of instruction it is. Each instruction will have a certain set of bits called the `OPCODE` that tells the [[Designing an Instruction Set#Central Processing Unit CPU|CPU]] how to interpret it.
In the [[Designing an Instruction Set#Beta Instruction Set Architecture|beta ISA]], the `OPCODE` can be found in the 6 most significant bits of the 32-bits instruction. The `OPCODE` is given as an input to the Control Unit, it will compute the appropriate control signals to program the datapath.

This decoding step depends on how complex the ISA is. An ISA like RISC (e.g: the \betaβ ISA) has a smaller number of instructions (a few dozens) while x86 has thousands. The most common family of instructions are:
-   **Memory Access**: anything regarding loading and storing of data between the REGFILE (CPU internal storage) and the Memory Unit. No other computation is performed.
-   **Arithmetic**: anything that requires computation using the, and inputs are taken from the REGFILE.
-   **Branch instructions**: anything pertaining to changing the value of PC Register to load instructions in different Memory Address, (_conditional_) based on a content of a specific register in the REGFILE.

## Instruction Types
- Arithmetic type 1: [[Beta Datapaths#OP Datapath|OP]]: anything that requires computation in ALU and both inputs from [[Anatomy of the Beta CPU#REGFILE|REGFILE]]
- Arithmetic type 2: [[Beta Datapaths#OPC Datapath|OPC]]: anything that requires computation in ALU and one input from [[Anatomy of the Beta CPU#REGFILE|REGFILE]], one input is CONSTANT.
- Memory type: [[Beta Datapaths#Memory Access Datapath|Memory access datapath]]: load and store between [[Anatomy of the Beta CPU#REGFILE|REGFILE]] and [[Anatomy of the Beta CPU#Program Counter and Physical Memory Unit|Data Memory]]
- Branch/jump type: [[Beta Datapaths#Control Transfer Datapath|control tranfer datapath]]: anything pertaining to change the value of the [[Anatomy of the Beta CPU#Program Counter and Physical Memory Unit|PC register]], based on the content of Z in [[Anatomy of the Beta CPU#REGFILE|REGFILE]]


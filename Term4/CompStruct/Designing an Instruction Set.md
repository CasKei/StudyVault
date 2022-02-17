---
aliases:
tags: #50.002
---
[[Comp Struct]]
[Website Notes](https://natalieagus.github.io/50002/notes/instructionset)
[Video](https://youtu.be/h1KGzAbJH4Q)

## Overview
To create a programmable control system suitable for general purposes (like the [[Turing Machine and Programmability#Universal Function|universal TM]]), we need to define a set of instructions for that system, such that it is able to support a rich repertoire of operations.

We can create a machien that is simply programmable, but also has to support:
- An expandable memory unit
- A rich repertoire of operations
- Ability to generate a new program and then execute it

In this document, we will begin by understanding what does it mean to simply create a (basic) _programmable_ machine, and how the current general-purpose computer model is both programmable and possess these three features.

## Example of a Basic Programmable Control System: Datapath
Suppose we have a simple [[Sequential Logic|sequential logic]] circuit called Machine $M$.
1 Input: $N$ bit
2 Outputs: $N$ bit `output1` and 1 bit `output2`.
We call this circuit a Datapath.
> Datapath: collection of functional units made up of [[Digital Abstraction#Combinational Device|combinational devices]], [[Sequential Logic#Edge-Triggered D Flip-Flop Register|registers]] and buses.

![[Pasted image 20220217125623.png]]

| ![[Pasted image 20220217125655.png]]                                                                     | Note that since machine receives $N$ bit inputs, there are $N$ units of each 2-to-1 [[Logic Synthesis#The Multiplexer\|multiplexers]] in parallel |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![[Pasted image 20220217125826.png]] \| The [[Sequential Logic\|registers]] are actually 1-bit registers |                                                                                                                                                   |

In diagrams they are drawn once, but you can differentiate between a single wire (caryring 1bit of info) with a bunch of wires that carry >1 bits of info by the "/" symbol.

In this example Machine $M$ also has 4 control signals, $A_{SEL}$, $B_{SEL}$, $A_{LE}$, $B_{LE}$.
These four signals will vary accordingly at each time step, hence changing the behaviour of the circuit above when we need it.
![[Pasted image 20220217130629.png]]
Other notable components:
- A decrement unit symbolised as `-1`
- Computation of `z = (input == 0) ? 1 : 0`
- A multiplier unit symbolised as `*`

IOW, we can control the processing of inputs at each time-step (CLK cycle) with a plugged in Control [[Finite State Machine|FSM]] unit.

If we can load another Control [[Finite State Machine|FSM]] unit that also produces these 4 signals but in differnet sequences, then we allow machine $M$ to be [[Turing Machine and Programmability#Programmability|programmable]]. The complete circuit after plugging in a Control [[Finite State Machine|FSM]] unit is:
![[Pasted image 20220217131349.png]]
Example: type A has this functional specificaiton with starting state S0:

| $s_i$ | $s_{i+1}$ | $A_{SEL}$ | $A_{LE}$ | $B_{SEL}$ | $B_{LE}$ |
| ----- | --------- | --------- | -------- | --------- | -------- |
| $S0$  | $S1$      | 1         | 1        | 0         | 1        |
| $S1$  | $S2$      | 0         | 1        | 1         | 1        |
| $S2$  | $S3$      | 0         | 1        | 0         | 0        |
| $S3$  | $S3$      | 0         | 0        | 0         | 0         |

This allows $M$ to be able to compute In X (In - 1) at the 4th clock cycle (counted from hte moment stable input is fed, assuming this is the first cycle t=0). The answer will be ready at `output1` port at t=3 later.

Now say we have another control [[Finite State Machine|FSM]] unit B that has:

| $Z$ | $s_i$ | $s_{i+1}$ | $A_{SEL}$ | $A_{LE}$ | $B_{SEL}$ | $B_{LE}$ |
| --- | ----- | --------- | --------- | -------- | --------- | -------- |
| --  | $S0$  | $S1$      | 1         | 1        | 0         | 1        |
| 0   | $S1$  | $S2$      | 0         | 1        | 1         | 1        |
| 1   | $S2$  | $S3$      | 0         | 1        | 0         | 0        |
| --  | $S3$  | $S3$      | 0         | 0        | 0         | 0        |

This allows machine $M$ to compute In factorial and produce it at `output1` port after certain time steps.

> The [[Turing Machine and Programmability#Programmability|programmability]] feature of machine $M$ allows us to reuse datapaths to solve new problems.

However it cannot be called a general purpose computer because:
- Limited storage: can only read input of $N$ bits, whatever that is being fed in
- Has a tiny repertoire of operations: $in!$ and $in \times (in - 1)$
- It is unable to generate a new program and execute it. We need to replace the entire Control [[Finite State Machine|FSM]] unit for it to be able to be 'reprogrammed'. In other words, there is no basic instruction set that can be used as building blocks to create a more complex program to control it.

Now it is clear what we need to do to create a general-purpose computer:
- Design a general purpose data path
- Design a proper instruction set

## The Von Neumann Model
Many architecture approaches to a general-purpose device have been explored, but the Von Neumann Model is what most modern and practical computers are based on.
![[Pasted image 20220217133506.png]]
The generic anatomy of a Von Neumann architecture is: 4 main components:

| Component                          | What is it                                                                                                                                                                                                                              |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[#Central Processing Unit (CPU)]] | The 'brain', made up of several [[Sequential Logic\|registers]] as internal storage, as well as [[Digital Abstraction#Combinational Device\|combinational logic units]] for performing a specified set of operations on their contents. |
| [[#Memory unit]]                   | External storage of data and programs that can be loaded onto the [[#Central Processing Unit (CPU)]] and executed                                                                                                                       |
| [[#Input/Output devices]]          | For communicating with the outisde world                                                                                                                                                                                                |
| [[#Data/Address bus]]              | Connects all components of the machine together.                                                                                                                                                                                                                                        |

### Central Processing Unit (CPU)
> CPU is a part of the computer that executes instructions. 
> A series of these instructions is called a computer program.

Before building a CPU, one usually designs a figurative blueprint for how the CPU operates and how all the internal systems interact with each other.
> This blueprint is called the Instruction Set Architecture.

There are many different types of ISAs a CPU can be built upon.
Some of the common ISA families are x86 (desktops and laptops) and ARM (embedded and mobile devices).

Basic anatomy of CPU: [[#Example of a Basic Programmable Control System Datapath|datapath]], Internal Storage called REGFILE, consisted of many [[Sequential Logic|registers]], the Arithmetic Logic Unit (ALU) and a Control Unit ([[Finite State Machine|FSM]]).
![[Pasted image 20220217135006.png]]

Functionalities of a CPU:
- Lead a series of instructions from the [[#Memory Unit]]
- Produce the corresponding control signals, hence effectively executing that loaded instruction using the ALU
- And store them in its (limited capacity) internal storage
- Store the computed output back into [[#Memory Unit]].

| Part                                                                    | What is it                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[#Example of a Basic Programmable Control System Datapath\|Data Path]] | An overarching infrastructure to control what input goes to each component, and where the output of each component in the CPU goes to.                                                                                                                                                                                                                                                                                                              |
| The Control Unit                                                        | Made of Program Counter (PC) nad a Control Unit (CU). PC: read an instruction at a time from the [[#Memory Unit]], so that the [[#Central Processing Unit CPU\|CPU]] can execute it. CU: gives us the control signals based on that current instruction read. These signals control the [[#Example of a Basic Programmable Control System Datapath\|datapath]] and enable us to route data to the appropriate components stated in the instruction. |
| The ALU                                                                 | Performs the 'work' -- computing basic functions such as addition, comparison, boolean, shifting, and multiplication.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### Memory Unit
> The [[#Central Processing Unit CPU]] is able to read and write bits of data to and from a memory unit connected to it -- an expandable storage device (known as RAM in practice)

The data stored in RAM is not just simply inputs, but also instructions that make up a program. This is where your instructions resides when it is about to be executed by the [[#Central Processing Unit CPU|CPU]].


### Input/Output devices
Input devices are typically keyboard and mouse.
Output typically sound and screen.

### Data/Address bus
Since the [[#Memory Unit]] can store a huge amount of data, the [[#Central Processing Unit CPU|CPU]] must be able to read just a particular $N$ bits of relevant data from the [[#Memory Unit]]. It is able to do this by giving an address as an input to the [[#Memory Unit]]. The [[#Memory Unit]] receives this address and output the data stored at the given address. To write to the [[#Memory Unit]], the [[#Central Processing Unit CPU|CPU]] must provide 2 inputs: the address where this $N$ bits of data should be stored, and the data itself.

We will learn more about the anatomy of the [[#Memory Unit]], but for now we can think of it as a device that can store a huge amount of data, separated into addressable segments that can hold $N$ bits of data each. It generally receives 3 kinds of input, 1-bit WE signal (write enable), address, and data input (bit size varies, depending on how much data can the memory holds).
![[Pasted image 20220217141035.png]]

==Impt==: List of conventions that explains why we illustrate the [[#Memory Unit]] as above.
- 4 segments per row: only for illustration, doesn't matter how you physically arrange the segments
- Each segment can contain exactly 1 bytes of data: by convention
- Each byte is addressable: by convention, data in the [[#Memory Unit]] is **byte addressable**
- In each row (4 segments), lower addresses on right, higher addresses on left
- Each rown has 4\*8 bits in total = 32 bits
- A [[#Memory Unit]] typically recieves $N$ bits of data input. Similarly, it outputs $N$ bits of data at a time, typically 32 or 64.
- **In this couse we learn a 32-bit toy architecture called the $\beta$ and therefore will be N=32.**
- Number of bits that can be received in ADDR input port is either fixed or depends on how many bits needed to address all the segments in the [[#Memory Unit]]
- Each row has 32 bits. We call a block of `32` bits a **word**. Since a [[#Memory Unit]] is byte addressable, a 32-bit word has 4 addresses. **By convention, we select the smallest of the four addresses to be the overall address of the word**.
	- So first word in first row has address `0x0000`
	- Subsequent word in second row `0x0004`
	- Each subsequent work increase address by 4
- Definition of a word may depend on the ISA.

### Programmability of a Von Neumann Machine
We can clearly see how electronic devices that are designed based on this model is _programmable_ (i.e: a **close** physical manifestation of a [[Turing Machine and Programmability#Universal Function|Universal Turing Machine]].

- [[#Memory Unit]]: "tape" that stores input and program
- [[#Central Processing Unit CPU|CPU]]: a complex [[Sequential Logic|sequential logic circuit]], a [[#Example of a Basic Programmable Control System Datapath|datapath]] whose job is to fetch and execute instructinos from the [[#Memory Unit]], one instruction at a time per clock cycle.
- Control Unit provides different control signals depending on the current instruction read. This allows us to reuse the same [[#Example of a Basic Programmable Control System Datapath|data paths]] for computing a set of different functions -- or in other words: provide [[Turing Machine and Programmability#Programmability|programmability]]. Programmable data paths give some algorithmic flexibility, achievable by just changing the control structure.

In this course we learn the [[#Beta Instruction Set Architecture]], a CPU blueprint that defines an abstract model of a general-purpose computer.

Its **implementation**: the $\beta$ **CPU**, is a 32-bit Von Neumann-based toy CPU created by MIT as a teaching tool to introduce students to _programmable datapaths_ and _instruction sets_, among all others. We can write any algorithm using a mixture of $\beta$ instructions. The CPU can emulate any machine behaviour that we want by executing it.

Modern ISAs (e.g: ARM, x86) and its corresponding CPU architecture is certainly much more complex than the $\beta$, however the $\beta$ is more than sufficient for us to understand and appreciate the basic concepts of programmable datapath and instruction sets. Some notable ISA in the past are [6502](https://www.masswerk.at/6502/6502_instruction_set.html), [AVR](http://ww1.microchip.com/downloads/en/devicedoc/atmel-0856-avr-instruction-set-manual.pdf), and [32-bit x86](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html).

## Beta Instruction Set Architecture
Recall that for a machine to be [[Turing Machine and Programmability#Programmability|programmable]], we need to design a set of well-defined operations that the machine should support. These operations can be used to form a larger - more complex program that if executed, allows the machine to emulate the behaviour of another program.

Beside defining the machine’s operation types, the ISA should also define the supported data types, the _registers_ (How many internal registers are there? How to address them? etc), and various other fundamental features such as addressing mode, input and output, and many more.

### Beta ISA Format
Each instruction that the $\beta$ supports is written in a specific encoding.
There are in total of 32 distinct operations/instructions that the $\beta$ should be able to execute, each having its own operation encoding (`OPCODE`).
[Documentation on each instruction](https://dropbox.com/s/2hzbawz9v51g6fu/beta_documentation.pdf?dl=0)

> Characteristics of the instructions
> -   Each instruction is encoded into **32-bits** of information.
> - Only **one instruction** is executed in each clock cycle. Each instruction is considered **atomic** and is presumed to **complete** _before_ the next instruction is executed.

### Beta Machine Model
The $\beta$ is a **general-purpose** 32-bit architecture. All registers are 32 bits wide. There are 33 registers in total (in the entire CPU):
- PC register: contain the address of the instruction
	- When loaded with an address, it can point to any location in the byte-addressed memory.
	- The [[#Memory Unit]] returns the instruction (32-bit data) stored at this address for the [[#Central Processing Unit CPU|CPU]] to decode and execute
- REGFILE registers (internal storage in [[#Central Processing Unit CPU|CPU]]): contains 32 registers in total (**and each register is 32 bits wide**), _addressable_ with 5 bits to identify `R0` to `R31` respectively.
	- All registers except `R31` can be read or written with new values.
	- For `R31`: when read, it is always 0; when written, the new value is discarded.
	- Notation: In **register transfer language**, the content of register with address `A` is often denoted as : `Reg[A]`. The symbol `Rx` refers to the address of a particular register `x` in the REGFILE. The symbol `Reg[Rx]` refers to the **content** of that register.

![[Pasted image 20220217154438.png]]
Note that :
- The Memory Unit (main memory) can also be referenced through **load** and **store** instructions that perform **no other computation**. The target _memory_ _address_ should be loaded in any registers in the REGFILE.
- **Conditional branch instructions** (BEQ and BNE) are _separated_ from comparison instructions (CMPLE, CMPLT, CMPEQ).

Branch instructions test the value of a register that can be the result of a previous compare instruction.

### Beta Instruction Encoding
There are **only two types** of instruction encoding: ==Without Literal (Type 1)== and ==With Literal (Type 2)==. All integer manipulation is between registers, with **up to two** source operands (one may be a sign-extended 16-bit literal), and **one destination** register.
-   **Instructions _without_ literals** (Type 1) include arithmetic and logical operations between two registers whose result is placed in a third register.
-   **Instructions with literals** (Type 2) include all other operations and instruction literals is represented in two’s complement.

![[Pasted image 20220217154555.png]]

The 32-bit instruction `I` is segmented to various sections:

The `OPCODE =I[31:26]` is 6 bits long. The `OPCODE` signifies different types of operation. They are summarised in the table below:
![[Pasted image 20220217154611.png]]
1.  For Type 1 instruction (without literal), we have these three segments: `Rc = I[25:21]`, `Ra = I[20:16]`, and `Rb = I[15:11]`, each 5 bits in length, to signify the target _address_ of the registers in the REGFILE. _The last 11 bits are unused._
    -   `Rc` is the destination register to write output to.
    -   `Ra`, and `Rb` contain the source data
 2.  For Type 2 instruction (with literal), we have these three segments: `Rc = I[25:21]`, `Ra = I[20:16]`, and `c = I[15:0]`.
    -   `Rc` is the destination register to write output to.
    -   `Ra` contains the source data.
    -   `c` is a 16-bit signed constant or literal.

The reason for this Type 2 instruction is that some operations require a constant instead. For examplem we want to add the _content_ of register `Ra` with a constant `c = 4` instead. Then we can encode `c=0000 0000 0000 0100` as the last 16 bits of the instruction.

It is imperative that you read the [beta documentation](https://www.dropbox.com/s/2hzbawz9v51g6fu/beta_documentation.pdf?dl=0) up until page 12, to understand all 32 basic instructions of the $\beta$ machine individually **before proceeding** to the next chapter. In the next few weeks, we will take this knowledge to the next level as you learn how to hand assemble C-language into this low-level machine language.
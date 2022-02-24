---
tags: #50.002
---
[[Comp Struct]]
[[Building Beta CPU]]

The beta datapath can be reprogrammed by setting the appropriate control signals depending on the current instruction’s `OPCODE`.
In general, we can separate the instructions into four categories, and explain the datapath for each:
-   The `OP` datapath (Type 1)
-   The `OPC` datapath (Type 2)
-   Memory access datapath (Type 2)
-   Control transfer datapath (Type 2)

## OP Datapath
Involves:
-   Any logical computations using the [[Anatomy of the Beta CPU#ALU|ALU]], and
-   The inputs to the `A` and `B` port of the ALU is taken from the contents of any two registers `Reg[Ra]` and `Reg[Rb]` from the [[Anatomy of the Beta CPU#REGFILE|REGFILE]].
-   The result is stored as a content of `Reg[Rc]`

The instructions that fall under `OP` category are: 
`ADD, SUB, MUL, DIV, AND, OR, XOR, CMPEQ, CMPLT, CMPLE, SHL, SHR`, and `SRA`. 
Its general format is:
![[Pasted image 20220221084315.png]]
The register transfer language for this instruction is: `PC` $\leftarrow `PC+4`  
`Reg[Rc]` $\leftarrow$ `Reg[Ra]` `(OP)` `Reg[Rb]`
-   The corresponding assembly instruction format runnable in BSIM is `OP(Ra, Rb, Rc)`

**Important:** Read the [beta documentation](https://www.dropbox.com/s/2hzbawz9v51g6fu/beta_documentation.pdf?dl=0) and fully study the functionalities of each instruction.

The figure below shows the datapath for all `OP` instructions:
![[Pasted image 20220221085207.png]]
The highlighted lines in **pink** show how the signals should flow in order for the beta to support `OP` instructions.

[[Building Beta CPU|see table]]
The control signals therefore must be set to:
-   `ALUFN = F(OP)`
    
    > the `ALUFN` signal for the corresponding operation `OP`, for example, if `OPCODE = SUB` then `ALUFN = 000001`, and so on.
    
-   `WERF = 1`
-   `BSEL = 0`
-   `WDSEL = 01`
-   `WR = 0`
-   `RA2SEL = 0`
-   `PCSEL = 000`
-   `ASEL = 0`
-   `WASEL = 0`
## OPC Datapath
The `OPC` (Type 2 instruction) datapath is similar to the `OP` datapath, except that input to the `B` port of the [[Anatomy of the Beta CPU#ALU|ALU]] must comes from `c = I[16:0]`.

**There is no `Rb` field in Type 2 instruction**.

The instructions that fall under `OPC` category are: `ADDC, SUBC, MULC, DIVC, ANDC, ORC, XORC, CMPEQC, CMPLTC, CMPLEC, SHLC, SHRC`, and `SRAC`. It’s general format is:
![[Pasted image 20220221085452.png]]
The register transfer language for this instruction is: `PC` ← `PC+4`  
`Reg[Rc]` ← `Reg[Ra]` `(OP)` `SEXT(C)`

-   The corresponding assembly instruction format runnable in BSIM is `OPC(Ra, c, Rc)`

The control signals for `OPC` instructions are almost identical to `OP` operations, except that we need to have `BSEL = 1`.

### Sample Code

Try it yourself by running this code step by step on BSIM and observe the datapath to familiarize yourself with how OP and OPC datapath works.

-   At each timestep, be aware of the value of PC and all Registers.
-   Familiarise yourself with how to translate from the assembly language to the 32-bit machine language

```haskell
.include beta.uasm

ADDC(R31, 5, R0)
SUBC(R31, 3, R1)
MUL(R0, R1, R2)
CMPEQ(R1, R1, R4) 
CMPLT(R0, R1, R4)
SHL(R1, R1, R5)
SRAC(R5, 4, R5)
SHRC(R1, 4, R6)
```
## Memory Access Datapath
There are three instructions that involve access to the Memory Unit: 
=> `LD`, `LDR` and `ST`. 
All of them are Type 2 instructions.
### LD Datapath
The general format of the `LD` instruction is:
![[Pasted image 20220221085811.png]]
The register transfer language for this instruction is: `PC` ← `PC+4`  
`EA` ← `Reg[Ra] + SEXT(C)`  
`Reg[Rc]` ← `Mem[EA]`

-   The LD instruction allows the CPU to **load** one word (32-bit) of data from the [[Designing an Instruction Set#Memory Unit|Memory Unit]] and store it to `Rc`
    
-   The **effective address** (`EA`) of the data is computed using the content of `Ra` (32-bit) added with `c` (sign extended to be 32-bit).
-   The corresponding assembly instruction format runnable in BSIM is `LD(Ra, c, Rc)`

The figure below shows the datapath for `LD`:![[Pasted image 20220221090144.png]] 
The control signals therefore must be set to:
-   `ALUFN = ADD (000000)`
-   `WERF = 1`
-   `BSEL = 1`
-   `WDSEL = 10`
-   `WR = 0`
-   `RA2SEL = --`
-   `PCSEL = 000`
-   `ASEL = 0`
-   `WASEL = 0`

### LDR datapath

The `LDR` instruction is similar to the `LD` instruction, except in the method of computing the `EA` of the data loaded.

The general format of the `LDR` instruction is:
![[Pasted image 20220221090251.png]]
The register transfer language for this instruction is: `PC` ← `PC+4`  
`EA` ← `PC+4*SEXT(C)`  
`Reg[Rc]` ← `Mem[EA]`  

-   The `LDR` instruction computes `EA` **relative** to the current address pointed by `PC`.
-   The corresponding assembly instruction format runnable in BSIM is `LDR(label, Rc)`, where `c` is **auto** computed as `(address_of_label - address_of_current_ins)/4-1`

The figure below shows the datapath for `LDR`:
![[Pasted image 20220221090351.png]]
The control signals therefore must be set to:
-   `ALUFN = 'A' (011010)`
    
    > The [[Anatomy of the Beta CPU#ALU|ALU]] is simply required to be _transparent_, i.e: “pass” the input at the `A` port through to its output port.
    
-   `WERF = 1`
-   `BSEL = --`
-   `WDSEL = 10`
-   `WR = 0`
-   `RA2SEL = --`
-   `PCSEL = 000`
-   `ASEL = 1`
-   `WASEL = 0`

### ST datapath
The `ST` instruction does the opposite to what the `LD` instruction does. 
It allows the [[Anatomy of the Beta CPU|CPU]] to store contents from one of its [[Anatomy of the Beta CPU#REGFILE|REGFILE]] registers to the [[Anatomy of the Beta CPU#Program Counter and Physical Memory Unit|Memory Unit]].

*Note that the instruction `ST` and `LD`/`LDR` allows the CPU to have access to an expandable memory unit without changing its datapath, although the CPU itself has a limited amount of internal storage in the REGFILE.*

The general format of the `ST` instruction is:
![[Pasted image 20220221090646.png]]
The register transfer language for this instruction is: `PC` ← `PC+4`  
`EA` ← `Reg[Ra]+SEXT(c)`  
`Mem[EA]` ← `Reg[Rc]`

-   The ST instruction **stores** data present in `Rc` to the Memory Unit.
    
-   Similar to how `EA` is computed for `LD`, the **effective address** (`EA`) of where the data is supposed to be stored is computed using the content of `Ra` (32-bit) added with `c` (sign extended to be 32-bit).
-   The corresponding assembly instruction format runnable in BSIM is `ST(Rc, c, Ra)`, notice the swapped `Rc` and `Ra` position.

The figure below shows the datapath for `ST`:
![[Pasted image 20220221090752.png]]
The control signals therefore must be set to:
-   `ALUFN = 'ADD' (000000)`
-   `WERF = 0`
-   `BSEL = 1`
-   `WDSEL = --`
-   `WR = 1`
-   `RA2SEL = 1`
-   `PCSEL = 000`
-   `ASEL = 0`
-   `WASEL = --`

### Sample Code

**Try it yourself** by running this code step by step on BSIM and observe the datapath to familiarize yourself with how OP and OPC datapath works.

-   At each timestep, be aware of the value of PC and all Registers.
-   Be aware on the value stored at certain memory locations
-   Familiarise yourself with how to translate from the assembly language to the 32-bit machine language using _labels_ and _literals_

```haskell
.include beta.uasm

LD(R31, x, R0)
LD(R31, x + 4, R1)
LD(R31, x + 8, R2)
LD(R31, x + 12, R3)
LDR(x, R4)
LDR(x+8, R5)
MUL(R0, R3, R0)
ADD(R1, R1, R1)
ADDC(R31, 12, R6)
ST(R0, x)
ST(R1, x, R6)

x : LONG(15) | this is an array
	LONG(7)
	LONG(9)
	LONG(-1)
```

## Control Transfer Datapath
There are three instructions that involves **transfer-of-control** (i.e: _branching_, or _jumping_), that is to change the value of `PC` so that we can execute instruction from other `EA` in the [[Anatomy of the Beta CPU#Program Counter and Physical Memory Unit|Memory Unit]] instead of going to the next line. 
These instructions are 
=> `BEQ`, `BNE`, and `JMP`.

We will not use the [[Anatomy of the Beta CPU#ALU|ALU]] at all when transferring control.

So far, we have only seen `PC` to be advanced by 4: `PC` ← `PC+4`. With instructions involving transfer-of-control or , we are going to set `PC` a little bit differently.

### BEQ datapath
This instruction allows the `PC` to _branch_ to a particular `EA` if the content of `Ra` is zero. It is commonly used when ==checking for condition prior to branching==, e.g: `if x==0, else`.

The general format of the `BEQ` instruction is:
![[Pasted image 20220221091212.png]]
The register transfer language for this instruction is: `PC` ← `PC+4`  
`Reg[Rc]` ← `PC`  
`EA` ← `PC + 4*SEXT(C)`  
`if (Reg[Ra] == 0)` then `PC` ← `EA`

-   The **address** of the instruction following the `BEQ` instruction is written to `Rc`.
-   If the contents of `Ra` are zero, the `PC` is loaded with the target address `EA`;
-   Otherwise, execution continues with the next sequential instruction.
-   The checking of the content of `Ra` is not done through [[Anatomy of the Beta CPU#ALU|ALU]], but rather through the 32-bit NOR gate that produces `Z` (1-bit), The value of `Z` is fed to the [[Anatomy of the Beta CPU#Control Logic Unit|Control Unit]] to determine whether PCSEL should be `001` or `000` depending on the value of `Z`.
-   The corresponding assembly instruction format runnable in BSIM is `BEQ(Ra, label, Rc)`* where `c` is **auto** computed as `(address_of_label - address_of_current_ins)/4-1`

The figure below shows the datapath for the `BEQ`:
![[Pasted image 20220221091442.png]]
The control signals therefore must be set to:
-   `ALUFN = --`
    
    > We aren’t using the [[Anatomy of the Beta CPU#ALU|ALU]] at all when transferring control.
    
-   `WERF = 1`
-   `BSEL = --`
-   `WDSEL = 00`
-   `WR = 0`
-   `RA2SEL = --`
-   `PCSEL = Z ? 001 : 000`
-   `ASEL = --`
-   `WASEL = 0`

## BNE datapath
`BNE` is similar to `BEQ`, but branches `PC` in the opposite way, i.e: when `Ra != 0`. It also utilizes the output `Z`.

The general format of the `BNE` instruction is:
![[Pasted image 20220221091528.png]]
The register transfer language for this instruction is: `PC` ← `PC+4`  
`Reg[Rc]` ← `PC`  
`EA` ← `PC + 4*SEXT(C)`  
`if (Reg[Ra] != 0)` then `PC` ← `EA`

The corresponding assembly instruction format runnable in BSIM is `BNE(Ra, label, Rc)`* where `c` is **auto** computed as `(address_of_label - address_of_current_ins)/4-1`

The figure below shows the datapath for the `BNE`:
![[Pasted image 20220221091625.png]]
The control signals therefore must be set to:
-   `ALUFN = --`
    
    > We aren’t using the [[Anatomy of the Beta CPU#ALU|ALU]] at all when transferring control.
    
-   `WERF = 1`
-   `BSEL = --`
-   `WDSEL = 00`
-   `WR = 0`
-   `RA2SEL = --`
-   `PCSEL = Z ? 000 : 001`
-   `ASEL = --`
-   `WASEL = 0`

### JMP Datapath
`JMP` also allows the CPU to change its `PC` value, but without any condition (_jump_).

The general format of the `JMP` instruction is:
![[Pasted image 20220221091702.png]]
The register transfer language for this instruction is: `PC` \leftarrow← `PC+4`  
`Reg[Rc]` \leftarrow← `PC`  
`EA` \leftarrow← `Reg[Ra] & 0xFFFFFFFC` (masked)  
`PC`\leftarrow← `EA`  

-   The **address** of the instruction following the `JMP` instruction is written to `Rc`, then `PC` is loaded with the contents of `Ra`.
-   The low two bits of `Ra` are **masked** to ensure that the target address is aligned on a 4-byte boundary.
-   The corresponding assembly instruction format runnable in BSIM is `JMP(Ra, Rc)`.

The figure below shows the datapath for the `JMP`:
![[Pasted image 20220221091736.png]]
The control signals therefore must be set to:

-   `ALUFN = --`
    
    > We aren’t using the [[Anatomy of the Beta CPU#ALU|ALU]] at all when transferring control.
    
-   `WERF = 1`
-   `BSEL = --`
-   `WDSEL = 00`
-   `WR = 0`
-   `RA2SEL = --`
-   `PCSEL = 010`
-   `ASEL = --`
-   `WASEL = 0`

### Sample Code

**Try it yourself** by running this code step by step on BSIM and observe the datapath to familiarize yourself with how OP and OPC datapath works.

-   At each timestep, be aware of the value of PC and all Registers.
-   Know where is the address of each instruction when loaded to memory
-   Note how to translate from `label` to `literal` when crafting the 32-bit machine language for `BEQ/BNE` instructions.

```
.include beta.uasm

ADDC(R31, 3, R0)

begin_check: CMPEQ(R31, R0, R1)
BNE(R1, is_zero, R10)
SUBC(R0, 1, R0)
BEQ(R31, begin_check, R10)

is_zero: JMP(R31)
```
---
aliases: CPU
tags: #50.002
---
[[Comp Struct]]
[[Building Beta CPU]]

The beta CPU is comprised of the following standard parts that typically make up a CPU: PC, REGFILE, ALU, and CU.

## Program Counter and Physical Memory Unit
>The PC is a 32-bit register (i.e: a set of **32** 1-bit registers). 
Its job is to store the **address** of the **current** instruction that is executed.

For now, we can safely assume that the ==initial content of the PC REG is always zero==.

The datapath of the components involving the ==PC== and the ==Physical Memory== is shown in the figure below:
![[Pasted image 20220221075503.png]]
 :

| Every clock cycle,                                                                                              | 2 important things happen.                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Output of PC register is conncted to `ia` port (input address port) of the Memory Unit (RAM or Physical Memory) | Hence the Memory Unit will produce the content of that address through the `Ins` port.                                                                                                                                                                                                                                                                         |
| The output of the PC REG will be added by 4                                                                     | If `PCSEL = 0` and `RESET = 0`, value (old PC +4) will enter the PC REG in the next CLK cycle, causing the PC to supply the address of the ==subsequent instruction word== in the next CLK cycle.<br>If `PSEL != 0` and `RESET = 0`, then the value in PC REG will be equivalent to either of the inputs to the PCSEL [[Logic Synthesis#The Multiplexer|mux]] (depending on what `PCSET` value is) |

If `RESET=1` then the value of the PC REG in the next cycle will be equivalent to `RESET`.

In short, `Reset = 0x80000000` all for beta instructions.
If `RESET=1`, the value in PC REG will will be set back to `0x0=80000000` in the next clock cycle instead of increased by 4.
You will learn in the [[Virtual Machine]] chapter on why the MSB of `RESET` is `1` instead of `0`, but for now you can take its purpose as simply _resetting_ the PC REG content back to `0`.

The memory unit is neatly segmented into **instruction** memory and **data** memory for the sake of **learning** and **simplicity**. In reality, this might not always be the case. Your operating system will do the memory management for you and decide where in the physical memory each process should reside and run.

## REGFILE
> The register file in [[Designing an Instruction Set#Beta Instruction Set Architecture|beta ISA]] is the [[Designing an Instruction Set#Central Processing Unit CPU|CPU's]] internal storage unit that is comprised of 32 sets of 32-bit [[Sequential Logic#Edge-Triggered D Flip-Flop Register|registers]], denoted as $R_0, R_1, \dots, R_{31}$.
> Each register is **addressable in 5 bits**.
> For example: `00000` is the address of $R_0$, `00001` is the address of $R_1$, `00010` is the address of $R_2$, and so on.

Remember, a 32-bit register simply means a set of **32** 1-bit registers
Anatomy of beta REGFILE:

![[Pasted image 20220221080835.png]]
Contains:
- 2 [[Digital Abstraction#Combinational Device|combinational]] **read** ports: `RD1` and `RD2`
- 1 clocked/[[Sequential Logic#|sequential]] **write** port: `WD`

**Reading:**
We can simultaneously **read** at the same CLK cycle 2 selected [[Sequential Logic#Edge-Triggered D Flip-Flop Register|registers]], addressable in 5 bits denoted as `Ra` and `Rb`
-   The 5-bit address `Ra` is supplied through port `RA1`
-   The 5-bit address `Rb` is supplied through `RA2`

**Writing:**
We can also **write** data supplied at the `WD` port to any of the [[Sequential Logic#Edge-Triggered D Flip-Flop Register|registers]] in the REGFILE:
-   In order to write, a valid `1` must be supplied at the `WE` port
-   The address of the register to write into is determined by the 5-bit input supplied at the `WA` port.

#### The Write Enable Signal

[[Sequential Logic#Edge-Triggered D Flip-Flop Register|Recall]] that a register / D Flip-Flop “captures” a NEW input at each CLK rise, and is able to maintain that **stable** value for the period of the CLK.

However, in practice, we might ==not== want our register to ==“capture” new input all the time==, but ==only on certain moments==. Therefore, there exist a `WE` signal such that:
-   When it’s value is `1`, the register “captures” and stores the current input.
-   Otherwise, the register will ignore the input and will output the last stored value regardless of the CLK edge.

#### Detailed Anatomy of the REGFILE
To understand how the `WE` signal works more clearly, we need to dive deeper into the inner circuitry of the REGFILE. The figure below shows a more detailed anatomy of the REGFILE unit.
![[Pasted image 20220221081433.png]]

*Note: `R31`'s **content** is **always** `0x00000000`, regardless of what values are written to it. Therefore it is not a regular register like the other 30 registers in the REGFILE. It is simply giving out `0x00000000` as output when `RA1` or `RA2` is `11111`, which is illustrated as the 0 on the rightmost part of each read muxes.*

The `WE` signal is fed into a 1-to-32 [[Logic Synthesis#Decoder Demux|demultiplexer]] unit. The `WA` signal is the selector of this demux. As a result, only 1 out of the 32 outputs of the [[Logic Synthesis#Decoder Demux|demux]] will follow exactly the value of `WE`.

The outputs of the [[Logic Synthesis#Decoder Demux|demux]] is used as a selector (`EN` port) to each of the _2-to-1_ 32-bit [[Logic Synthesis#The Multiplexer|mus]] connected to each 32-bit [[Sequential Logic|register]].

*Note: although not drawn (to not clutter the figure further), all the registers are synchronized with the same CLK.*

#### The [[Digital Abstraction#The Static Discipline|Static]] and [[Sequential Logic#The Dynamic Discipline|Dynamic]] Discipline of the REGFILE
As mentioned [[#REGFILE|above]], the REGFILE unit has **2 combinational read ports** that is made up by the two large _32-to-1_ 32-bit multiplexers drawn at the bottom of the figure. 

We can supply two read addresses: `RA1` and `RA2`. 
They are the selector signals of these two multiplexers. 
Therefore the ==time taken== to produce valid output (32-bit) data at `RD1` and `RD2` is ==at least== the $t_{pd}$ of the multiplexer and $t_{pd}$ of the DFFs depending on when exactly the addresses become valid.

This unit also have **1 sequential write port**. 
The write data is always supplied at `WD`. 
When the `EN` signal of a target register is a valid `1`, we need to ==wait until the nearest CLK rise edge== in order for `WD` to be reflected at the `Q` port of that register.

In register transfer language, the content of register with address `A` is often denoted as : `Reg[A]`

The timing diagram for read and write is shown below. Please take some time to study them:
![[Pasted image 20220221081925.png]]
Notice how the new data denoted as `new Reg[A]` supplied at port `WD` (to be written onto `Reg[A]`) must fulfill both $t_S$ and $t_h$ requirement of the hardware.

## Control Logic Unit
>The heart of the control logic unit (CU) is a [[Digital Abstraction#Combinational Device|combinational logic device]] that receives 
> - 6-bit `OPCODE` signal, 
> - 1-bit `z` signal, 
> - 1-bit `RESET` signal, and 
> - 1-bit `IRQ` signal as input. 
> 
> We will discuss about `RESET`, `z` and `IRQ` much later on.

**At each CLK cycle**, the PC will supply a new 32-bit address to the Memory Unit,
and in turn, 32-bit instruction data is produced by the Memory Unit. 
**The first 6 bits of the instruction, called the `OPCODE` is supplied as an input to the CU.**

The CU will then decode the input combination consisted of `OPCODE`, `z`, `RESET`, and `IRQ`, and **produce various control signals** as shown in the figure below. In practice, this unit can be made using a [[Logic Synthesis#Read-Only-Memories ROM|ROM]].
![[Pasted image 20220221082439.png]]
Note that the `ALUFN` is 6 bits long, 
`PCSEL` is 3 bits long, 
`WDSEL` is 2 bits long, 
`RA2SEL`, `BSEL` `ASEL`, `WASEL`, `WR`, and `WERF` (`WE` to REGFILE) are all 1 bit long. 
The total number of output bits of the CU is therefore **_at least_ 17 bits long**.

In our Lab however, the output signal of the control unit is 18 bits long. We don’t have to memorise these, as long as we get the main idea.

>Notice the presence of the 1-bit register that **samples** the IRQ signal. This is because the IRQ signal actually an **asynchronous** interrupt trigger.
>
>In the later weeks, we will learn that _asynchronous interrupts_ are generated by **other hardware devices** at _arbitrary_ times with respect to the CPU clock signals. Therefore, we need another sequential logic device to **condition/synchronize** it such that it doesn’t cause unwanted changes to the Control Unit in the middle of execution (in the middle of a clock cycle). This sampling device that receives the external `IRQ` signal allows the CPU to **sample** the input IRQ signal during the beginning of each instruction _cycle_, and will respond to the trigger only _if_ the signal `IRQ` is asserted when sampling _occurs_.

In the Lab however, we also simplify this part. We simply assume that the IRQ signal given by the test file is guaranteed to be stable for the entire CPU clock cycle, and already fulfils the $t_S$ and $t_H$ requirements of the CPU clock cycle.

**For simplicity, we no longer display this register unit in the diagrams to explain the datapaths below.** The presence of the `CLK` signal there is written to remind you that the CPU should be able to _sample_ the asynchronous `IRQ` signal for each clock cycle. ==However, the heart of the Control Unit itself is [[Digital Abstraction|combinational logic device]] (e.g: [[Logic Synthesis#Read-Only-Memories ROM|ROM]]) and not a [[Sequential Logic#|sequential]] one==.
## ALU
> The ALU is a [[Digital Abstraction#Combinational Device|combinational logic device]] that has 2 32-bit inputs (which we call `A` and `B`) and produes one 32-bit output.

The arithmetic logic unit is the **heart** of a **CPU**; it is responsible for all sorts of **logic computations**. The basic family of operations that a general-purpose ALU should have include:
-   **Addition/subtraction** for basic arithmetic computation
-   **Comparison** for branching purposes
-   **Boolean** unit for boolean computation, like XOR, bit masking, etc
-   **Shifter** unit for division or multiplication by 2, or chopping data apart
-   **Multiplier** unit for multiplication

**Important Note:**
$ALUFN \neq OPCODE$ 
The ALUFN signals used to **control** the operation of the ALU circuitry use an encoding chosen to make the design of the ALU circuitry as simple as possible. This encoding is not the same as the one used to encode the 6-bit OPCODE field of Beta instructions. In Lab 5, you will build some logic (actually a ROM) that will translate the opcode field of an instruction into the appropriate ALUFN control bits.

### Adder/Subtractor
We will be using the “little-endian” bit numbering convention where bit 31 is the most-significant bit and bit 0 is the least-significant bit.

>An **adder/subtractor** unit that operates on 32-bit two’s complement (**SIGNED**) inputs (`A[31:0]`, `B[31:0]`) and generates a 32-bit output (`S[31:0]`) + 3-bit _other_ output signal (`Z, V, N`).

It will be useful to generate three other output signals to be used by the comparison logic in Part B:
-   `Z` which is true when the S outputs are all zero
-   `V` which is true when the addition operation overflows (i.e., the result is too large to be represented in 32 bits), and
-   `N` which is true when the S is negative (i.e., S31 = 1).

The following schematic is a big picture for how to go about the design:
![[Pasted image 20220221100810.png]]
-   The `ALUFN0` input signal selects whether the operation is an `ADD` or `SUBTRACT`.
    -   `ALUFN0` will be set to `0` for an `ADD (S = A + B)` and `1` for a `SUBTRACT (S = A – B)`;
    -   To do a `SUBTRACT`, the circuit first computes the two’s complement negation of the “B” operand by inverting “B” and then adding one (which can be done by forcing the carry-in of the 32-bit add to be 1).
-   `A[31:0]` and `B[31:0]` are the 32-bit two’s complement (SIGNED) **input** operands;
-   `S[31:0]` is the 32-bit **output**;
-   `Z/V/N` are the three **other output** code bits described above.

Start by implementing the 32-bit add using a ripple-carry architecture. You’ll have to construct the 32-input NOR gate required to compute Z using a tree of smaller fan-in gates (the parts library only has gates with up to 4 inputs).

#### #### Computing Overflow

**Overflow** can never occur when the two operands to the addition have **different** signs; if the two operands have the same sign, then overflow can be detected if the sign of the result differs from the **sign** of the operands (Note that `XA` and `XB` are just the input nodes of the `FA`, refer to the diagram above):
$$V=XA_{31}\cdot XB_{31} \cdot \overline{S_{31}}+\overline{XA_{31}}\cdot \overline{XB_{31}} \cdot S_{31}$$
Think about why is this so? Start by having a small example, let’s say a 4-bit RCA. If we have `A: 0111`, and `B: 0001`, adding both values will result in a **positive overflow**. The true answer to this should be `01000` (signed, means the decimal 8). However since the 4-bit RCA is signed, we have our output as just `1000`, and this means decimal -8 in a signed 4-bit output. Now think about other possible overflow cases (negative overflow, etc).

#### Detailed Schematic
![[Pasted image 20220221101157.png]]

### Compare Unit
> A 32-bit compare unit that generates one of two constants (`0` or `1`) depending on the `ALUFN` control signals (used to select the comparison to be performed) and the `Z`, `V`, and `N` outputs of the adder/subtractor unit.

Clearly the high order 31 bits of the output are **always zero** (use that connection to connect `0` in JSim to zero `cmp[31:1]`). The least significant bit of the output is determined by the answer to the **comparison** being performed.

![[Pasted image 20220221101243.png]]
-   `ALUFN[2:1]` are used to control the **compare unit**
-   Recall that we control the adder/subtractor unit using `ALUFN0` so we cannot use `ALUFN0` to control this compare unit too

**Performance note:**
-   The `Z`, `V` and `N` inputs to this circuit can only be calculated by the adder/subtractor unit **after** the 32-bit add is **complete**.
-   This means they arrive quite late (takes **tpd** of adder to compute valid `ZVN` signals) and then require further processing in this module, which in turn makes valid `cmp0` shows up after **tpd** of **both** adder and compare units.
-   You can speed things up considerably by thinking about the _relative_ timing of `Z`, `V` and `N` and then designing your logic to minimize delay paths involving late-arriving signals.

#### Detailed Compare Unit Schematic
![[Pasted image 20220221101310.png]]

### Boolean Unit
> A **32-bit Boolean unit** for the Beta’s logic operations. 
> One implementation of a 32-bit boolean unit uses a **32 copies of a 4-to-1 multiplexer** where `ALUFN0`, `ALUFN1`, `ALUFN2`, and `ALUFN3` **hardcode** the operation to be performed, and `Ai` and `Bi` are hooked to the multiplexer **`SELECT`** inputs. 
> This implementation can produce any of the 16 2-input Boolean functions; but we will only be using 4 of the possibilities: `AND`, `OR`, `XOR`, and `A`.

Note the ORDER of the multiplexer **control** signals and its corresponding **output**. See [stdcell documentation](https://drive.google.com/file/d/1ArkRewfiBqJGmVqzkiGzFxbS0fZ-2eWw/view?usp=sharing) on the 4-to-1 mux if you’re unsure how these are obtained.

General Schematic:
![[Pasted image 20220221101423.png]]

The following table shows the encodings for the `ALUFN[3:0]` control signals used by the test jig. If you choose a different implementation you should also include logic to **convert** the supplied control signals into signals appropriate for your design.
![[Pasted image 20220221101455.png]]

#### Detailed Schematic
![[Pasted image 20220221101513.png]]
In total, you should utilise 32 4-to-1 multiplexers to build the boolean unit. **Please use JSim iterator explained above for this!**

### Shifter
> A **32-bit shifter** that implements `SRA`, `SHR` and `SHL` instructions.
> - The `A[31:0]` input supplies the data to be shifted
> - The **low-order** 5 bits of the `B[4:0]` are used as the **shift count** (i.e., from 0 to 31 bits of shift)
> - We do not use the high 27 bits of the `B` input (meaning that `B[31:5]` is **ignored** in this unit)

For example, if `A: 0x0000 00F0` and we would like to **shift** A to the left by FOUR bits, the `B` input should be `0x0000 0004`

The desired operation will be encoded on `ALUFN[1:0]` as follows:
![[Pasted image 20220221101638.png]]
With this encoding, `ALUFN0` is `0` for a **left shift** (SHL) and `1` for a **right shift** (SHR) and `ALUFN1` controls the **sign extension** logic on **right shift**.

-   For `SHL` and `SHR`, 0’s are shifted into the vacated bit positions.
-   For `SRA` (“shift right arithmetic”), the vacated bit positions are all filled with A31, the sign bit of the original data so that the result will be the same as dividing the original data by the appropriate power of 2.

Here’s the condensed schematic of the left shifter. In total, you should use **32x5 = 160** 2-to-1 multiplexers.
![[Pasted image 20220221101649.png]]

#### Detailed Schematic
The simplest implementation is to build THREE shifters: one for shifting **left**, one for shifting **right**, and one for shifting **right arithmetic**. Then, we use a 4-way 32-bit multiplexer to select the appropriate answer as the unit’s output.

It’s easy to build a shifter after noticing that a **multi-bit shift** can be **accomplished** by **cascading** shifts by various powers of 2.

-   For example, a 13-bit shift can be implemented by a shift of 8, followed by a shift of 4, followed by a shift of 1.
-   So the shifter is just a cascade of multiplexers each controlled by one bit of the shift count.

| Shifter                  | Schematic                            |
| ------------------------ | ------------------------------------ |
| Left shifter             | ![[Pasted image 20220221101756.png]] |
| Right shifter            | ![[Pasted image 20220221101806.png]] |
| Right arithmetic shifter | ![[Pasted image 20220221101821.png]] |

Combined:
![[Pasted image 20220221101837.png]]

Another approach that **adds** latency but **saves** gates is to use the _left shift logic_ for **both** left and right shifts, but for right shifts, **reverse** the bits of the `A` input first on the way in and **reverse** the bits of the output on the way out.

### Multiplier
> This particular combinational multiplier accepts 32-bit operands (`A`, `B`) and produces a 32-bit output. **Multiplying two 32-bit numbers produces a 64-bit product;** the result we’re looking for is **just the low-order 32-bits of the 64-bit product.**

Here is a detailed bit-level description of how a **4-bit** by **4-bit** unsigned multiplication works. This diagram assumes **we only want the low-order 4 bits** of the 8-bit product.
![[Pasted image 20220221102023.png]]
This diagram can be **extended** in a straightforward way to 32-bit by 32-bit multiplication.

Remember again that since our machine is only 32-bit, that means we only can store the low-order 32-bits of the result, you don’t need to include the circuitry that generates the rest of the 64-bit product.

As you can see from the diagram above, forming the _partial products_ is easy. Multiplication of two bits can be implemented using an `AND` gate. The hard **and VERY TEDIOUS part** is adding up all the partial products **(there will be 32 partial products in your circuit)**

-   One can use full adders (FAs) hooked up in a ripple-carry configuration to add each partial product to the accumulated sum of the previous partial products (see the diagram below)
-   The circuit closely follows the diagram above but omits an FA module if two of its inputs are `0`

![[Pasted image 20220221102056.png]]

#### Analysis
The circuit above works with both **unsigned** operands and **signed** two’s complement operands. 
This may seem strange – don’t we have to worry about the most significant bit (MSB) of the operands? With unsigned operands the MSB has a weight of $2^{MSB}$ (assuming the bits are numbered 0 to MSB) but with signed operands the MSB has a weight of $-2^{MSB}$. Doesn’t our circuitry need to take that into account?

It does, but when we are only saving the lower half of the product, the differences don’t appear.

The multiplicand (`A` in the figure above) can be **either** unsigned or two’s complement (signed), and the FA circuits will perform correctly in either case.

-   When the multiplier (`B` in the figure above) is signed, we should **subtract** the final partial product instead of adding it.
-   But **subtraction** is the **same as adding the negative**, and the negative of a two’s complement number can be computed by taking its complement and adding 1.
-   When we work this through we see that the **low-order bit of the partial product is the same whether positive or negated**.
-   And the low-order bit is **ALL** that we need when saving only the lower half of the product
-   If we were building a multiplier that computed the full product, we’d see many differences between a multiplier that handles unsigned operands and one that handles two’s complement operands, but these differences only affect how the high half of the product is computed.

**Design Note:** Combinational multipliers implemented as described above are pretty slow! There are many design tricks we can use to speed things up – see the appendix on “Computer Arithmetic” in any of the editions of **Computer Architecture: A Quantitative Approach** by John Hennessy and David Patterson (Morgan Kauffmann publishers).

### Combine all units and make the ALU
Combine the outputs of the finished **adder**, **multiplier** (given), **compare**, **boolean** and **shift** units to produce a single `ALU` output: `ALU[31:0]`. The simplest approach is to use a 4-way 32-bit multiplexer as shown in the schematic below:
![[Pasted image 20220221102252.png]]
Two additional control signals (`ALUFN[5:4]`) have been introduced to select which unit will supply the value for the ALU output. The encodings for `ALUFN[5:0]` used by the test jig `lab3checkoff.jsim` are shown in the following table:
![[Pasted image 20220221102307.png]]
Note that the `Z`, `V`, and `N` signals from the adder/subtractor unit are **INCLUDED** in the terminal list for the alu subcircuit (counted as ALU’s output). **You should also have these signals as the ALU output for your 1D Project**. While these signals are NOT needed when using the ALU as part of the Beta, they are included here to make it easier for the test jig to pinpoint problems with your circuit.


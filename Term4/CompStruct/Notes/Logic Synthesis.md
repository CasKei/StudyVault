---
aliases: logic, logic gates, gates, boolean algebra
tags: #50.002
---
# Logic Synthesis
[Lecture](https://youtu.be/yXBAy432vT8)
[Notes](https://natalieagus.github.io/50002/notes/logicsynthesis)
[[CMOS Technology|Previous notes]]
[[Comp Struct|Course info]]

## Overview
![[Pasted image 20220202102655.png]]
Purpose of creating combinational devices: synthesise logic.
Create a device that is able to give a certain combination of output given a certain combination input.
In other words: a device that can adhere to a truth table i.e. its functional specification.

Any combinational device has to have a functional specification.
Functional specifications are represented with truth tables.

| NAND | A   | B   | Y   | AND | A   | B   | Y   |
| ---- | --- | --- | --- | --- | --- | --- | --- |
|      | 0   | 0   | 1   |     | 0   | 0   | 0   |
|      | 0   | 1   | 1   |     | 0   | 1   | 0   |
|      | 1   | 0   | 1   |     | 1   | 0   | 0   |
|      | 1   | 1   | 0   |     | 1   | 1   | 1   |

NAND is just short for NotAND.

## N-input Gates
![[Pasted image 20220202094302.png]]
There are 16 possible input gates.
There are $2^{2^x}$ possible x-input gates, but not all are useful in practice. 

## Sum of Products
Can have functional specifications in terms of boolean expression.
To convert truth table into boolean expressions,
1. Look for rows with Y=1. (e.g. NAND rows 1,2,3)
2. For each such row, if input 0, express with NOT
	1. NAND row 1: $\bar{A}\bar{B}$
	2. NAND row 2: $\bar{A}B$
	3. NAND row 3: $A\bar{B}$
3. Sum all expressions with Y=1
	1. NAND: $Y = \bar{A}\bar{B}  + \bar{A}B + A\bar{B}$
4. This expression is called the sum of products. Sometimes called canonical sum of products.

## Universal Gates
NAND, NOR are universal: each alone can implement any boolean function.
AND, OR and INV are insufficient, NANDs or NORs can make these 3, though these 3 can express any boolean expressions.
![[Pasted image 20220202102624.png]]
Therefore NAND and NOR are universal gates.

## Straightforward Logic Synthesis
Recall that the goal of combinational devices is that they are created to adhere to a certain functional specification.
We can make various logic gates and combine them to synthesise a more complex logic or truth table.
However, there are basic logics that can be used to synthesise any kinds of other (more complex) logic: like INV, AND and OR gates.

> ==Given a sum of products boolean expression, we can make a combinational device that has boolean expression as functional specification using these 3 types of logics: INV, AND and OR with arbitrary number of inputs.==

### Example:
Given the following sum of products expression,
$$Y=\bar{C}\bar{B}A + \bar{C}BA+CB\bar{A}+CBA$$
We can make a combinational device as such that it adheres to the expression above using these 3 logic devices only, as shown:
![[Pasted image 20220202113927.png]]
- Boolean expression of Y contains 4 terms that are summed together
- 4-input OR gate at Y represents summation of these 4 terms
- AND gates in second comlumn represent the combination of each input terms
- INV at input represent the NOT inputs.

Using these steps we can come up with the simplest, most straightforward logic synthesis.

Note: if expression contains many terms summer together, we need bigger OR gate at the output. This causes the size of our device to be bigger, and therefore more expensive.
Later we learn how to reduce the boolean expression such that we have less number of terms, and thus are able to synthesise the logic more effectively.

## Boolean Algebra Properties
[More FYI](https://www.electronics-tutorials.ws/boolean/bool_6.html)
To reduce or minimise boolean expressions, we need properties to manipulate boolean expressions.
A summary end up with simpler terms and reduce the terms, while still keeping the logic equivalent.

### OR
Simple properties
$$
\begin{align}
a + 1 &= 1\\
a + 0 &= a\\
a + a &= a
\end{align}
$$
### AND
Simple properties
$$
\begin{align}
a1&=a\\
a0&=0\\
aa&=a
\end{align}
$$
### COMPLEMENT
Simple properties
$$
\begin{align}
a+\bar{a}&=1\\
a\bar{a}&=0
\end{align}
$$
### Commutative
Adding on
$$
\begin{align}
a + b &= b + a\\
ab&=ba
\end{align}
$$
### Associative
Adding on
$$
\begin{align}
(a+b)+c &= a+ (b+c)\\
(ab)c &= a(bc)
\end{align}
$$
### Distributive
Adding on
$$
\begin{align}
a(b+c)&=ab+ac\\
a+bc&=(a+b)(a+c)
\end{align}
$$
### Absorption Law
Useful for boolean minimisation as we might end up with less number of terms while keeping the same logic
$$
\begin{align}
a+ab&=a\\
a+\bar{a}b&=a+b\\
\bar{a}+ab &= \bar{a} + b\\
a(a+b)&=a\\
\bar{a}(\bar{a}+\bar{b})&=\bar{a}\\
a(\bar{a}+b)&=ab\\
\end{align}
$$
### Reduction Law
Useful for boolean minimisation as we might end up with less number of terms while keeping the same logic
$$
\begin{align}
ab + \bar{a}b&=b\\
a\bar{b} + \bar{a}\bar{b}&=\bar{b}\\
(a+b)(\bar{a}+b)&=b
\end{align}
$$
### Consensus Theorem
Derived from above:
$$ab+\bar{a}c+bc=ab+\bar{a}c$$
Proof:
$$
\begin{align}
ab+\bar{a}c+bc &= ab+\bar{a}c+ (a+\bar{a})bc\\
&= ab+\bar{a}c+ abc+\bar{a}bc\\
&= ab(1+c) + \bar{a}c(1+b)\\
&= ab+\bar{a}c
\end{align}
$$
Pay attention to the relationship between each variables.
You can easily let $\bar{a}=x$ and find the formula applies as well for the inverted version.
### DeMorgan's Theorem
Useful to manipulate boolean equations as it converts between OR and AND and vice versa using INV
Basically NAND -> INV = NOR, NOR -> INV = NAND
$$
\begin{align}
\overline{a+b} &= \overline{a}\overline{b}\\
\overline{ab} &= \bar{a} + \bar{b}
\end{align}
$$
### Boolean Minimisation Example
$$
\begin{align}
Y&=\bar{C}\bar{B}A+\bar{C}BA+CB\bar{A}+CBA\\
&=\bar{C}\bar{B}A+\bar{C}BA+CB\\
&=\bar{C}A+CB
\end{align}
$$
### Karnaugh Map for Boolean Minimisation
Alternative method to perform boolean minimisation.
A method to easily perform boolean minimisation, and ultimately the end goal is to reduce the digital circuit to its minimum number of gates (save cost and save space).
Figure below shows 2-input, 3-input and 4-input Karnaugh Maps.
Do not change the order, they follow Gray code configuration to preserve adjacency so rules 1-6 below can apply.
![[Pasted image 20220202140350.png]]
Number of cells with $x$ inputs: $2^x$ cells.
Fill in `1` to all cells that represent `1`.
![[Pasted image 20220210151832.png]]
- Groups should contain as many `1` cells
- Can only contain powers of 2
- a `1` cell can only be grouped with adjacent `1` cell  without diagonal grouping
- groups of `1` cells can overlap
- the top/bottom and left/ right edges, and the 4 corners of the map are considered to be continuous.
	- larger grps can be made by grouping cells across the top and bottom or left and right edges
	- top and bottom row can form one grp
	- leftmost and rightmost column can form one grp
- there should be as few groups as possible

So the example above is groupes like this
![[Pasted image 20220210152257.png]]
To convert this back into boolean expression, we need some logic
- Blue group: output is `1` regardless of A and C, so it is just M
- Green: output is `1` regardless of M. So it is AC
So X = M + AC

## Logic Synthesisation with CMOS
We can create a combi logic device easily given the minimised boolean expression using any of the universal gates:
- NANDs only
- NORs only
- AND, INV, and OR

Each gate can be created usign transistors, PFETs and NFETs in a complementary way.
![[Pasted image 20220210153325.png]]
We can create the device  straight using CMOS recipe given the minimalised boolean expression, or the primitive way:
1. construct a pulldown circuitry
	1. for each OR we build parallel NFE
	2. Each AND build a series NFET
2. Add inverted at output if needed
3. Construct complementary pullup of PFETs and assemble

Does not guarantee minimal transistors, though more efficient than using just the expression and bruteforce.

## Special Combinational Logic Devices
### The Multiplexer
It is implemented using basic logic gates (INV, AND, and OR, or NANDs).
The mux is expensive to manufacture, but _universal_, meaning that it can **implement any boolean function because essentially it “hardcodes” the truth table**.
A mux **always** has **three** types of terminals:
-   2^k2k bits data inputs,
-   `k` bits selector signal(s) –_this is also an input, but we have a special name for them them: selector_– , and
-   1-bit output.

It's function components: the inputs, the selector signals, and the output.
It basically allows one of the input signals to pass trough when selected to be reflected at `OUT`.

E.g. 2 input mux. When S=0, it will reflect whatever A carries as output
![[Pasted image 20220210153905.png]]

You can build a 2-input multiplexer using basic gates
![[Pasted image 20220210153927.png]]

Properties:
- Muxes are universal: it can implement any boolean functions
- Mux can have $2^k$ data inputs, and $k$ bits select inputs, and only can have 1 output terminal

The following figure shows an example of a 4-input multiplexer, implemented as a big mux (left) or using a series of 2-input mux (right):
![[Pasted image 20220210154033.png]]
Similarly, you can build a 4-input mux using basic logic gates:
![[Pasted image 20220210154051.png]]


Full adder
Below is an example of how a mux can be used to implement a more complex combinational device, the full adder that we encounter in the lab. The truth table of a full adder is as shown, it is basically an addition (of three inputs) in base 2:
![[Pasted image 20220210154115.png]]
The multiplexer can simply implement the truth table by mapping each type of output bit $C_{out}$, and $S$ in each of the input terminals of the mux as illustrated below (for the carry out):
![[Pasted image 20220210154145.png]]

### Decoder / Demux
The Decoder (also known as “demux”) is a special combinational logic device that is also very commonly used in practice. It can have $k$ select inputs, and $2^k$ possible output combinations. The schematic of a 1-select input decoder is:
![[Pasted image 20220210154228.png]]
The schematic of a 2-select inputs decoder: $S_0$ and $S_1$ is (we omit the “IN”) because it is usually just VDD:
![[Pasted image 20220210154309.png]]

Properties of decoders
- Opposive of a multiplexer. Has $k$ select inputs, $2^k$ possible data outputs, and only 1 bit of input (typically VDD). The symbol is: ![[Pasted image 20220210154628.png]]
- This figure omits the 1 bit input to the decoder because it is always set to 1 in practice
- Therefore for a 4 bit decoder as shown in the figure above, the input signals are ony the two selector signals.
- At any given time only 1 bit of the $2^k$ output bits can be `1`. This is apparant when we try to draw the truth table for a $k$ input decoder.
1-selector bit:

| S   | O1  | O2  |
| --- | --- | --- |
| 0   | 1   | 0   |
| 1   | 0   | 1   |

2-selector bit:

| S1  | S0  | O0  | O1  | O2  | O3  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 0   | 0   | 0   |
| 0   | 1   | 0   | 1   | 0   | 0   |
| 1   | 0   | 0   | 0   | 1   | 0   |
| 1   | 1   | 0   | 0   | 0   | 1   |

In other words, only the selected output $i$ is `1` and the rest of $2^k - 1$ data output is `0`.

### Read-Only-Memories (ROM)
One of the application of a decoder is to create a read-only-memories (ROM).

For example, if we “hard-code” the Full-Adder using a decoder, we end up with the following schematic:
![[Pasted image 20220210155450.png]]
- At the output of the decoder, the littel circuit with inverted triangle symbol signifies a pulldown which will drain signal to 0
- Recall that at reach combi of select signal A,B,C, only one of the 8 outputs of the decoder will be `1`
- Note the presence of inverters by invention at the end of two vertical output lines for S and Cout, so the overall output is inverted to be `1` for S and `0` for Cout
- By invention, the location of the pulldown circuits correspond to a `1` in the truth table for that particular output.
- For $K$ inputs, decoder produces $2^K$ signals, only `1` which is asserted at a time.

Properties of ROM:
- ignores the structure of combinational functions (truth table is hardcoded)
- selectors are like addresses of an entry
- for an N-input boolean function, the size of ROM is roughly $2^n \times numOfOutputs$.

## Summary
Synthesizing combinational logic is not a simple task. There are many ways to realise a functionality, i.e: the **logic** (that the device should implement) represented by the truth table or boolean expression. We can use universal gates (only NANDS, or only NORS), a combination of gates (INV, AND, and OR), or many other ways (multiplexers, ROMs, etc).

Of course **hardcoding** a truth table using ROM and Multiplexers are convenient, because we do not need to think about simplifyfing the boolean expression of our truth table (which can get really difficult and complicated when the truth table is large, i.e: complicated functionality). However it comes at a cost: the **cost of the materials** to build the ROM / Multiplexers, and at the **cost of space** (we need use a lot of logic gates to build these).


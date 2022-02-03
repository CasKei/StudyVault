#50.002
# Logic Synthesis
[Lecture](https://youtu.be/yXBAy432vT8)
[Notes](https://natalieagus.github.io/50002/notes/logicsynthesis)
[[CMOS Technology|Previous notes]]
[[Comp Struct|Course info]]

## Overview
![[Pasted image 20220202102655.png]]
Purpose of creating combinational devices: synthesise logic.
Create a device that is able to give a certain combination of output given a certain combination input.
IOW: a device that can adhere to a truth table i.e. its functional specification.

Any combinational device has to have a functional specification.
Functional specifications are represented with truth tables.

|NAND|A|B|Y|AND|A|B|Y|
|---|---|---|---|---|---|---|---|
||0|0|1||0|0|0|
||0|1|1||0|1|0|
||1|0|1||1|0|0|
||1|1|0||1|1|1|

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


## Logic Synthesisation with CMOS
## Special Combinational Logic Devices
### The Multiplexer
### Decoder / Demux
### Read-Only-Memories (ROM)
## Summary

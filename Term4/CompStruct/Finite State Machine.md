---
aliases: FSM
tags: #50.002
---
Recall
[[State Machine]]

[[Comp Struct]]
[[Sequential Logic]]
[[Synchronisation]]

## Overview
Understand how we can utilise [[Digital Abstraction|combinational devices]] and [[Sequential Logic|sequential devices]] to create a specific device called the finite state machine (FSM).
The FSM is an abstract mathematical model of a [[Sequential Logic]] function.

We frequently use FSMs in our daily lives: traffic lights, vending machines, heating system, elevator, electronic locks, etc.

We can create an FSM by implementing the functionality of the [[State Machine]] using [[Digital Abstraction|combinational logic devices]], and assemble them with [[Sequential Logic#Edge-Triggered D Flip-Flop Register|memory devices]] to form a complete FSM circuitry.

FSM comes in 2 flavours: Moore and Mealy:
![[Pasted image 20220215180202.png]]

## Abstraction of FSM
> A FSM is formally defined to have:
> - A set of $k$ **==states==**, {$S_1, S_2, \dots, S_k$} (where one of them is the 'initial' state)
> - A set of $m$ **==inputs==**: {$I_1, I_2, \dots, I_m$}
> - A set of $n$ **==outputs==**: {$O_1, O_2, \dots, O_n$}
> - **==Transition==** rules $s'(S_i,I_i)$ for each of the $k$ states and $m$ inputs
> - **==Output==** rules: $f(S_i)$ for each of the $k$ states

## SM Diagram and the Truth Table
We can represent a state machine in 2 forms: [[#State transition diagram]] or [[#Truth table]].
### State transition diagram
Suppose we have a simple digital lock machine that will only open when we give the password `0110`.
![[Pasted image 20220215181206.png]]
Bolded node `sx` is the initial state.
Arrows are the possible transitions between states.
Numbers on arrows are the input required for the state transition to happen.
Number inside state is the output of each state.
In this case, `1` if unlocked.

There are 5 states in total and we can [[Basics of Information|encode]] them using 3 bits:

| State | `sx`  | `s0`  | `s1`  | `s2`  | `s3`  |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Code  | `000` | `001` | `010` | `011` | `110` |

Since we have 5 states, we need at least $\log_2{5} = 3$ (rounded up) bits to represent the states, any 5 values from `000` to `111`. This is called **encoded representation** of the states.

### Truth table
We can represent the functionality of the FSM in a truth table below:

| $S_i$ | In | $S_{i+1}$ | Out |
| ----- | ----- | --------- | --- |
| 000   | 0     | 001       | 0   |
| 000   | 1     | 000       | 0   |
| 001   | 0     | 001       | 0   |
| 001   | 1     | 010       | 0   |
| 010   | 0     | 001       | 0   |
| 010   | 1     | 011       | 0   |
| 011   | 0     | 110       | 0   |
| 011   | 1     | 000       | 0   |
| 110   | 0     | 001       | 1   |
| 110   | 1     | 010       | 1   |

> $s$ state bits allow us to encode up to $2^s$ different states.

Note: output column contains the output that depends on the current state only (Moore Machine)

## Moore and Mealy Machine
There are 2 types of FSM.

| Moore                                                                        | Mealy                                                             |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Output drawn on state                                                        | Output drawn on transition arrows                                 |
| Output depends on current state                                              | Output depends on both current input and current state            |
| ![[Pasted image 20220216201036.png]]                                         | ![[Pasted image 20220216200957.png]]                              |
| 4 states above: `00`, `01`, `10`, `11` for states `s0`, `s1`, `s2` and `s3`. | 3 states above: `00`, `01`, `10`, for states `s0`, `s1` and `s2`. |
| ![[Pasted image 20220216201503.png]]                                         | ![[Pasted image 20220216201515.png]]                              |
| Takes 1 cycle 'slower' to unlock than a Mealy lock                           | Takes less number of states to implement                          |

## Building a FSM
We can build an FSM using [[Sequential Logic|registers]], and [[Digital Abstraction|combinational logic units]] such as using [[Logic Synthesis#Read-Only-Memories ROM|ROMs]] or [[Logic Synthesis#The Multiplexer|multiplexers]], among others.

At first, we can transform the truth table for Moore into its [[Logic Synthesis#Boolean Algebra Properties|boolean equation]] form.
Since there are 2 state bits, we can label the MSB as $S_{0_i}$ and LSB as $S_{1_i}$ (at time step $i$).
We technically have 3 input bits: $S_{0_i}$, $S_{1_i}$, and $\text{In}$, and 3 output bits: $S_{0_{i+1}}$, $S_{1_{i+1}}$, and $\text{Out}$ in total for the [[Digital Abstraction#Combinational Device|combinational logic]] part of the FSM.

The boolean equation for Moore FSM truth table is
$$
\begin{align}
&S_{0_{i+1}} = \overline{S_{0_i}}\cdot S_{1_i} \cdot \text{In } + S_{0_i}\cdot\overline{S_{1_i}}\cdot \text{In }\\
&S_{1_{i+1}} = \overline{S_{0_i}}\cdot\overline{S_{1_i}}\cdot\overline{\text{In }} + \overline{S_{0_i}}\cdot S_{1_i}\cdot\overline{\text{In }}+
S_{0_i}\cdot\overline{S_{1_i}}\cdot\overline{\text{In }} + S_{0_i}\cdot\overline{S_{1_i}}\cdot \text{In }+S_{0_i}\cdot S_{1_i}\cdot\overline{\text{In }}\\
&\text{Out}= S_{0_i}\cdot S_{1_i}\cdot\overline{\text{In }}+S_{0_i}\cdot S_{1_i}\cdot \text{In }
\end{align}
$$
This can be minimised further. For output bits, its obvious that the current input does not matter since it is a Moore machine.

The boolean equation for Mealy FSM truth table is
$$
\begin{align}
&S_{0_{i+1}} = \overline{S_{0_i}}\cdot S_{1_i} \cdot \text{In }\\

&S_{1_{i+1}} = \overline{S_{0_i}}\cdot \overline{S_{1_i}} \cdot \overline{\text{In }}+ \overline{S_{0_i}}\cdot S_{1_i} \cdot \overline{\text{In }}
+S_{0_i}\cdot \overline{S_{1_i}} \cdot \overline{\text{In }}\\
&\text{Out} = S_{0_i}\cdot \overline{S_{1_i}} \cdot \text{In }
\end{align}
$$
Can also minimise further.

Now we have the boolean equations, we can simply construct the machine using 2-bit [[Sequential Logic#Edge-Triggered D Flip-Flop Register|registers]], and a [[Digital Abstraction#Combinational Device|combinational logic device]].

Possible schematics:

| Moore                                | Mealy                                |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20220216210612.png]] | ![[Pasted image 20220216210625.png]] |

Both diagrams are obtained after minimising the expression. There are other ways.

## Differences between Moore and Mealy
| Moore                                                                                                   | Mealy                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Output depends only on current state (regardless of input)                                              | Output is affected by both current state and current input                                                                                             |
| May require more states                                                                                 | Typically have less states and less transitions: can potentially use less registers and logic gates for the CL, potentially reducing its cost and size |
| Output is [[Synchronisation\|synchronised]] with the state change. Output given only in the next cycle. | React immediately with the presence of an input                                                                                                                                                       |

Mealy can seem faster or more responsive since the output can be produced in $\approx t_{pd}$ (or almost immediately if $t_{pd}$ of the last CL unit is small) after input arrives. However, the output of Moore is only obtained in the next CLK cycle.

One CLK period typically takes much longer than $t_{pd}$ of that smaller CL (at the output of the [[Sequential Logic|Flip-Flop]]) because:
- [[Sequential Logic#The Dynamic Discipline|Dynamic discipline]] has to be obeyed, thus $t_{pd}$ of that smaller than the CLK period.
- Logically, $t_{pd}$ of the smaller CL should be smaller than the $t_{pd}$ of a bigger CL, supporting the statement above.

## Enumerating FSM
After establishing the abstraction (specs) of the FSM, we want to make a physical machine that can conform to the funcitonal specification of our desinged FSM.
For any FSM, we can say that we need $i$ input bits, $s$ state bits, and $o$ output bits.

Truth table for arbitrary input, state and output bits:
![[Pasted image 20220216213631.png]]
In short, we need to create a [[Digital Abstraction|combinational logic device]] that conforms to the FSM's truth table. We have learned several ways to create such devices:
- By creating a [[Logic Synthesis#Read-Only-Memories ROM|ROM]]: use a [[Logic Synthesis#Decoder Demux|demultiplexer]], with each output bit soldered to conform to truth table
- By deriving the [[Logic Synthesis#Sum of Products|sum of products]] and use INV, AND, and OR gates
- By deriving the minimal boolean expression and create [[CMOS Technology#Complementary MOS circuitry|CMOS curcuitry]] using [[CMOS Technology#The CMOS Complements Recipe|CMOS recipe]]

Given $i$ input bits, $s$ state bits, and $o$ output bits we have a total combination of $2^{i+s}$ input-state combinations, and each input-state pair has $o$ bits as an output.

> Hence, the number of possible FSMs that can be captured with $i$ input bits, $o$ output bits, and $s$ state bits is
> $$2^{(o+s)^{2^{(i+s)}}}$$ FSMs
> Note: some FSMs in these many FSMs may be equivalent

Why?
- $2^{i+s}$ input-state combinations
- Each combination results in $o$ output bits and $s$ end-state bits.
- Total $(o+s)2^{i+s}$ bits to fill up in both the output and next-state column
- Each bit can take up 2 values, `1` and `0`.
- Thus we have $2^{(o+s)^{2^{(i+s)}}}$ different FSMs

Reason why we want to enumerate number of possible FSMs is because if we are going to make hardware for this FSM using some generic components, we want to know how many different FSMs can we program onto this particular hardware size which we probably mass produce.

## FSM Equivalence and Reduction
![[Pasted image 20220216215852.png]]
We need to find pairs of equivalent states and merge them.

Having less states will result in less bits to represent the states in the machine, and less transitions. This allows us to build the machine at a cheaper cost and smaller size.

## FSM Limitations and Summary
In this chapter, we have learned that we can build an FSM to compute many types of functions, such as implementing the _digital lock_.

Some problems however, cannot be computed using FSMs, so the notion of FSMs alone is not enough to be an _ultimate_ computing device that we need.

Remember that the goal of this course is to teach you how to build a **general-purpose computer** from the ground up. A _general-purpose computer_ is supposed to an _ultimate computing device,_ able to solve _various computational problems and tasks_ such as your math homework, running video games, rending graphics, playing music or video, browsing the web, and many more.

A classic simple example that cannot be computed using FSM is the **parenthesis checker** problem.

The reason that this classic problem cannot be solved by an FSM is because it requires **arbitrarily many states**, simply because **we do not know (prior)** how many parenthesis are there to check, or how many will be left balanced or unbalanced.

By definition, an FSM needs a **finite** amount of states. It is able to implement only tasks that require finite states, such as implementing junction traffic lights, line following robots, etc, but _not tasks that requires **arbitrarily many** number of states_ (i.e: states that depend on input length for example).

We know that we can definitely write a program that performs parenthesis checking easily, so we know that our computers aren’t just a _simple_ FSM. In the next chapter, we will learned another class of machine called the [[Turing Machine and Programmability|Turing Machine]] that can tackle this issue.
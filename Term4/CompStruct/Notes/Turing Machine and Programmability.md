---
aliases: Turing Machine, TM
tags: #50.002
---
[[Comp Struct]]
[Website notes](https://natalieagus.github.io/50002/notes/turingmachine)
[Video](https://youtu.be/cmfDBAiogA0)

## Overview
A [[Finite State Machine|FSM]] does not keep track of the number of states it visited, it is only aware of the current state it is in. Therefore it is unable to solve problems like detecting palindrome or checking balanced parenthesis.

> Turing Machine: a mathematical model of computation that defines an abstract machine: one that is able to implement any functionalities that FSM can implement, and doesn't face this limitation that FSM has.


## Basics of Turing Machine
A Turing Machine is often represented as an “arrow” and a series of input written on a “tape”, as drawn in the figure below:
![[Pasted image 20220216221723.png]]
### Properties
- Imagine we have a physical machine which can read a sequence of inputs written on an infinitely long tape
- We can write and read from the currently pointed location of the tape
- Like a [[Finite State Machine|FSM]], the Turing Machine also has a functional specification, illustrated by the truth table above. Building a TM with specification $K$ allows it to behave based on $K$ when fed any array of inputs.
- The pointer represents our current input read on the tape
- To operate the tape, we can move the tape or arrow left or right.
- There exists a HALT state where you reach the end state, and a START state as well

### Operation
From above:
- Start state $S_0$, arrow reading an input $1$
- Then look at functional specification table
	- Tell us to write $1$ to tape and more tape to right
	- ==Impt to read, write, then move==
- Repeat until we arrive at HALT state

## Increment Machine
Comsider a machine whose job is to add 1 to any arbitrary length input and present that as output.
[[Finite State Machine|FSM]] can do this well if number of bits input is finite, but if input bit is too large it will ahve problems.
An example of a 3-bit counter FSM is:
![[Pasted image 20220217091332.png]]

The key feature for a Turing Machine is this ==_infinite_ tape== (hence its ==capability of processing arbitrary input==).

A Turing Machine with the following specification can easily solve the problem and is capable to accept any **arbitrarily** long input with **less number of states**:
![[Pasted image 20220217091416.png]]
With this, the TM runs as follows:

| ![[Pasted image 20220217092330.png]] | START state = `s0`. Machine reading \* as input. It will write back a \*, then move the tape to the left. In fact it keeps moving the tape to the left until the end of the string (+) is found. |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![[Pasted image 20220217092535.png]] | + is found next.                                                                                                                                                                                 |
| ![[Pasted image 20220217092602.png]] | The machine then starts adding `1`, and moving the tape to the right, keeping track of the carry over value                                                                                      |
| ![[Pasted image 20220217092635.png]] | This continues until it reads back the beginning of the string (\*))                                                                                                                             |
| ![[Pasted image 20220217092700.png]] | The final output is written on the tape, and we should have this output in the end when the machine halts                                                                                        |

## Coin Counter Machine
We want to implement a machine that can receive a series of 10c coins, then a series of 20c coins. (for simplicity).
We can then press an END button in the end once we are done and the machine will 
- `ACCEPT(1)` if value of 10c == value of 20c
- `REJECT(0)` otherwise.

We cannot implement an [[Finite State Machine|FSM]] to solve this problem because there's no way an [[Finite State Machine|FSM]] can keep track of how many `10`s or `20`s are keyed in so far, and we can't possibly create a state for each possible scenario.
![[Pasted image 20220217094530.png]]

However, a TM with the following specification can solve this problem:
![[Pasted image 20220217094553.png]]

| ![[Pasted image 20220217094609.png]] | Given an input and starting state at `s0` at `t=0`                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| ![[Pasted image 20220217094635.png]] | State of machine is as follows at `t=2`                                                                  |
| ![[Pasted image 20220217094652.png]] | It will try to find the first `20`, and has this outcome and state at `t=5` once the first `20` is found |
| ![[Pasted image 20220217094727.png]] | It wil then try to find the leftmost unprocessed `10`                                                    |
| ![[Pasted image 20220217094743.png]] | The whole process is repeated until there is no more `10`. The machine will now try to find `END`        |
| ![[Pasted image 20220217094813.png]] | Once found it halts and writes the final value `ACCEPT`                                                                                                         |

## Turing Machine as a Function
Given a TM with specification $K$, symbolied as $T_K$, and a tape with paticular input sequence $x$, we can define $T_K[x]$ as running $T_K$ on tape $x$,
- We can produce $y=T_K[x]$ wher $y$ is the output of a series of binary numbers on that corresponding Tape $x$ after running $T_K$ on $x$
- Running $T_K[x]$ therefore can be seen as calling a function that takes in input $x$ and produces output $y$

Now we need to address what kind of functions can TM compute?
Or more generally, what can be computed and what type of machines can compute them?

## Church's Thesis and Computable Function
> The Church's Thesis: Every discrete fucntion computable by any realisable machine is computable by some Turing machine $i$.

> A function is computable is there exists an algorithm that can do the job of the function:
> i.e. given an input of the function domain it can return the correspoding output
> Any computable function can be incorporated into a program using while-loops.

> Inputs to these functions can be anything discrete:
> - A list of numbers (can be encoded large integer)
> - List of characters (same)
> - Matrix of pixels (same)
> - Etc 

Hence whatever inputs $x$ we put at the tape, we see them as a very large integer.

> A realisable machine is any machine that can help you sort, search, re-order objects, find min or max, perform mathematical operations, and so on.


### Uncomputable Function, Halting Problem
Just as there are infinitely many computable functions, there are also infinitely many comutable functions. Not every well-defined integer function is computable.

One example is the Halting function:
$$
\begin{align}
f_H(K, j) = 
\begin{cases}
&1 &\text{if $T_K[j]$ halts}\\
&0 &\text{otherwise}
\end{cases}
\end{align}
$$

The function determines whether Turing Machine that’s run with specification $K$ will halt when given a tape containing input $j$. What is “_halt_”? For example, we can write a program as an input to our machine (computers).

If computable, there should be a specification $H$ that can solve this.

Assume Turing machine with this specification as $T_H[K,j]$.

Since $j$ can also be a machine, let's have the same machine fed to it.
Define another specification $H'$ that implements this function:
$$
\begin{align}
f_{H'}(K, j) = f_H(K,K) =
\begin{cases}
&1 &\text{if $T_K[K]$ halts}\\
&0 &\text{otherwise}
\end{cases}
\end{align}
$$
Lets represent this as $f_{H'}(K)$ (no more $j$).

Finally, if we assume $f_{H'}(K)$ is computable, we can define another specification $M$ that implements the following:
$$
\begin{align}
f_M(K) = 
\begin{cases}
&\text{loops forever } &\text{if $f_{H'}(K) == 1$}\\
&\text{halts } &\text{otherwise}
\end{cases}
\end{align}
$$

Let a TM with specification $M$ be $T_M[K]$.
***
Now since $K$ is arbitrary, we can make $K=M$ and feed $f_M$ with itself:
$$
\begin{align}
f_M(M) = 
\begin{cases}
&\text{loops forever } &\text{if $f_{H'}(M) == 1$}\\
&\text{halts } &\text{otherwise}
\end{cases}
\end{align}
$$

There is a contradiction.
- If $T_M[M]$ halts, it will return `1` and loop forever and not halt.
- If it loops forever, it will return `0` and halt.

Neither can happen.
Thus, $M$ does not exist and is not realisable.
By extension, $H'$ and $H$ do not exist either.
Hence $f_H(K,j)$ is not computable.

## Universal Function
> The Universal Function is defined as
> $$f_U(K,J) = T_K[j]$$

>Say we write a specification $U$ that realises the function.
This means that a TM that runs $U$ is a machine capable of simulating an arbitrary TM on arbitrary input.
This is called a Universal Turing Machine.

The universal machine essentially achieves this by reading both the specification of the machine $K$ that we are going to simulate as well as the input $j$ to that machine from its own tape.

> The universal function is a model of a general purpose computer. Our computers are essentially a machine that simulates other machines.
> More importantly, out computer can emulate and be any machine when we task it to run any program and its input.

By definition, a computer can be realised using FSM, just that we probably need billions of states to do so.

## The Computer Science Revolution
It is a hassle to build a different physical machine each time we need to compute a new function.
In order to be efficient, we need to replace each of these hardwares with a coded description of that piece of hardware (software), then it is easy to modify them.
Writing programs is much easier than building a physical machine.
Also programs can easily receive another program as input and output other programs.

> Universal Turing Machine: a coded description of a pieve of hardware.

It allows us to migrate from the hardware paradigm into software paradigm.

Until this point, we have learned how a TM works, and its advantage over [[Finite State Machine|FSM]]. Our final goal is to realise a Universal Turing Machine, that is a machine that is programmable so it can be used for a general purpose.

## Programmability
> The concept of a universal TM is an ideal abstraction since we can never create a machine with an infinitely long tape.

If we manage to create a physical manifestation of Universal Turing Machine, we need to ensure that this machine is **programmable**. This can be achieved by designing an **instruction set** so that we can write “programs” / “algorithms” _using these instruction set_.
Hence allowing it to emulate the behavior of whatever machine $k$ when running the program with its corresponding input $j$ on this machine.

> An instruction set is a set of standard _basic_ commands that we can use as **building blocks** so that we can write a bigger programs that will cause the machine running it to emulate complex tasks.

>We can say that our computer is **programmable**, because the program that we wrote is translated into **a set of instructions** that our machine can understand.

Our (general purpose) computer is a (close enough) physical manifestation of a Universal Turing Machine (albeit with “finite” tape).

In the [[Designing an Instruction Set|next chapter]], we will learn further on how our general purpose computer is programmable by designing a proper instruction set for it.
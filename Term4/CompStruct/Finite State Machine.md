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
Understand how we cna utilise [[Digital Abstraction|combinational devices]] and [[Sequential Logic|sequential devices]] to create a specific device called the finite state machine (FSM).
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

### Truth table

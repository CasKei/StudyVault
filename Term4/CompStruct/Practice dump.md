---
tags: #50.002
---
This is a restatement of the bounded time arbiter problem, known to be unsolvable in theory. In practice we can build a circuit to solve this problem where the probability of failure is related to tpd. For large tpd, the probability of failure can be made very small, like one failure in billions of years.

A circuit that determines if A was pressed before a time.
Assume the circuit has an accurate internal signal that transitions from 0 to 1 when deadline is reached.
Output should be 1 if the button was pressed on or before the dadline. 0 if presed after the deadline. Output should be valid and stable within a specified tpd
Another restatement of the bounded time arbiter problem. Given sufficiently long time bounds, we can engineer practical approximate solutions

Circuit in bounded time indicates which of 2 game shouw contestants press button first if the rpesses were more than 0.1 sec apart, otehrwise tie

metastability
the decision as to whether presses were 0.1 s apart is subj  to metastab problems

at least one button has been presed. 
OR gate.

bounded
Exactly one has pressed button.XOR gate

A circuit that has 2 parts:
a subcircuit that indicates which of 2 game show participants pressed their button first,
a subcircuit that in bounded time lights a tie if
	subcircuit hasnt produced an answer after 1s
	tie light should stay lit even if a makes a d

game show 

A circuit that converts button preses from 2 contestants into the following 2 bit output encoding:
The circuit has 2 inputs AB, one for  each
Contestant input will transition from 0 to 1 when he/she presses his/her button
1. 00 neither
2. 01 A
3. 10 B
4. 11 both

Both valid stable within specified tpd.

Possible.
Nothing meta sable. Combinational logic enough.

SM
1. A moore: it has its output that depends only on the state: false
2. s1 s2 equivalent
What is the purpose of FSM?
To be able to compute sequential logic, values and outputs that depend not just on the input, but also on the state of the machine.

Incomplete SM
ACME
div by 3 fsm
accept binary number one bit at a time


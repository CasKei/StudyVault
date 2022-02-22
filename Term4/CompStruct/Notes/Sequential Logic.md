---
aliases: sequential logic, D-Latch, D Flip-Flop, memory device, register, SL
tags: #50.002
---
[[Comp Struct]]
[Lecture vid](https://youtu.be/HlizelEp4Yc)
[Notes](https://natalieagus.github.io/50002/notes/sequentiallogic)

## Overview
Recall [[Digital Abstraction#Combinational Device|a combinational logic device]]: a device that is capable to adhere to a given functional specification (truth table).

Output always depends on the current input.

However, external ouput is unreliable and there is no guarantee that the input will be available for at least $t_{pd}$ until the device produces meaningful results.

We need a way to synchronise the external input signal such that there's enough time for the entire circuit to finish its computation properly.

We also need to create another type of device called the sequential logic device, where outpput depends not only on the current input, but a series of past inputs as well.
If sequential logic device has a finite number of state, it is also known as the [[Finite State Machine]]. The FSM can be seen as an abstract mathematical model of a sequential logic function. [[State Machine|Recall DDW state machine]].
However, our knowledge so far is not enough to create sequential logic devices. To synchronise and remember the series of past inputs, we need to have some kind of storage (memory) device.

> Recap: simple combinational logic device does not remember its output value. Only gives output when there is input, and output stays stable for as long as input is stable.

> A memory device is a device which we can write new values to and is able to remember this value for a period of time.

We can connect memory devices tgt with combinational logic devices to form a sequential logic device. Notice presence of a CLK.
![[Pasted image 20220214084244.png]]
In the next few sections we will learn how to create this memory device labeled as **Registers** above (or more specifically, it is called _D Flip-Flop_).

## Storage Device: D-Latch
A D Flip-Flop (memory device) is made using another device called a D-Latch.
A D-Latch can be created with a [[Logic Synthesis#The Multiplexer|multiplexer]] with a feedback loop.
![[Pasted image 20220214084537.png]]
There are other ways to make a D-latch as well.

### How D-Latch Works
- G is CLK signal: periodically switch between `1` and `0`
- Q: output of latch
- D: External input placed at the second input port of the latch
- Q is fed back as Q', the first input port of the latch
- If G is `1`, then input signal on wire D will be reflected at output wire Q independent of signal on wire Q'
- If G is `0`, then output signal on Q reflects the signal on wire Q', independent of input wire D

> When G is `1`: this is the write mode.
> When G is `0`: this is the read mode.

![[Pasted image 20220214090550.png]]
4-bit input and 4-bit output.
Each device drawn as a rectangle is called a Flip-Flop, which are made of D-latches.

### Probems arising from using simple D-Latch without any contract
- **Storage of invalid information**: if G change from `1` to `0` at the exact moment when D just turned invalid from valid, we may store the invalid value of D when latch enters memory mode
- **Invalid/unstable output due to transition in input**: If existing stable input in D is flipped, value at D will be invalid (momentarily) during this transition
	- Voltage value at D can also be invalid due to any disturbance.
	- This will affect the output at Q if G is `1` because it will pass all input from D to Q res of whether it is valid or not. We end up with unstable/invalid input half the time.
	- Unacceptable in practice as we do not want out devices to have invalid input comuted at any time, even when D is transitioning.

### Solutions
Combinational component requires $t_{pd}$ to produce meaningful results, and over this timeframe we need to hold the input stable. However, external input is unreliable, so there is no guarantee that this requirement is fulfilled.
- Therefore we need to create a D Flip-Flop using D-latches, or more informally a register, to synchronise external input with the circuit's CLK, and switch between write and read mode as we intend it.
- A D Flip-Flop with the right CLK setup will be able to produce a valid and stable output for an entire clock period, log enough for any combinational logic connected downstream to finish its computation ($t_{pd}$) and produce meaningful output before the next output value is produced.

## The Dynamic Discipline
The _dynamic discipline_ is a contract that is made to address the first problem above: the possibility of **storing invalid information** in the memory device. It is imperative to never violate the dynamic discipline to ensure any sequential logic circuits to work properly.
[[CMOS Technology#Propagation delay t_ pd|Recall propagation delay.]]
[[CMOS Technology#Contamination delay t_ cd|Recall contamination delay.]]

> The dynamic discipline states that there are **two timing** **requirements for the input signal supplied at D**, named as $T_{setup}$ and $T_{hold}$, which lengths are:
> 1. $T_{setup} \approx 2 t_{pd}$ of the components that make up the D-Latch
> 2. $T_{hold} \approx t_{pd}$ of the components that make up the D-Latch

> $T_{setup}$: minimum time that voltage on wire D needs to be valid/stable BEFORE the clock edge changs from `1` to `0` (write to read)
> $T_{hold}$: minimum time that voltage on wire D nees to be valid/stable AFTER the clock edge reaches `0` from previous `1`

Informal: 
- $T_{setup}$: how long you should wait to ensure that output signal at Q reflects what was supplied at D ($t_{pd}$), and ensure this output at Q maintains this alue when CLK at G turns `0` (another $t_{pd}$)
- $T_{hold}$: CLK is an input, and device needs ($t_{pd}$) time to realise it is in read mode after CLK turns `0`. During this time, input at D must be held valid.

The **tpd** and **tcd** of a sequential circuit is counted from the **last** downstream register(s) (there can be more than one) in the circuit because our reference "input" is no longer IN but the CLK.

**ts** and **th** is concerning the path from **INPUT** until the **first** upstream register(s) (there can be more than one) in the circuit.
$$t_s = t_{s.R1} + t_{pd.CL1}$$
$$t_h= t_{h.R1} - t_{cd.CL1}$$
**The dynamic discipline is always obeyed in any middle path** between two DFFs or register in the circuit because of the hardware characteristics (tcds and CLK period) of the sequential circuit, so we don't need to worry about that. Therefore the definition of **ts** and **th** of the **entire** circuit is only concerning the first upstream register, because this is where we need need to be wary of its **ts** and **th** since it has to be fulfilled by the (unreliable) external input.

## Edge-Triggered D Flip-Flop (Register)
Addressing the [[#Probems arising from using simple D-Latch without any contract|second problem]] of the presence of unstable/invalid output during transition of input, we need to create another device called Edge-Triggered D Flip-Flop (Flip-Flop) by putting 2 D-Latches in series.
![[Pasted image 20220214094519.png]]
Flip-Flop: put D-Latches in series, and invert the CLK signal fed to the first latch.

In a Flip-Flop, the CLK input port is represented by the > symbol at its lower left corner.

### Structure of a Flip-Flop
- Master Latch: receives external input D
- Slave Latch: second latch
- Inverter: applied on G input on master, so master receives the inverted CLK signal
- $\star$ : symbol represents the intermediary output and is not observable outside the system
- Output of slave latch Q is the observable output of the Flip-Fop

### How does Flip-Flop prevent the presence of invalid/unstable output during transition/disturbance of input at D?
User:
- User only gets output from output wire of slave latch's Q port
- User supplies input only to master latch's D port

CLK:
- CLK is a signal that periodically changes from `0` to `1` and vice versa
- When `0`: `1` -> G of Master (inverted) and  `0` -> G of slave, at the same time.
	- Master is in 'write': lets signal from D through to Q
	- Slave is in 'read': depends on own memory Q' and unaffected by input on $\star$
- When `1`:  `0` -> G of Master (inverted) and  `1` -> G of slave, at the same time.
	- Master is in 'read': master's output depends on own memory Q' and is not affected by any value on input port D
	- Slave is in 'write': lets signal from $\star$ to be passed through its D

> Hence, only ONE of the 2 D-Latches is on 'write' mode at any time, and vice versa.
> Unlike a single D-Latch, this configuration prevents a direct reflection of the input of the system (from user) to the output of the system.

![[Pasted image 20220214101328.png]]

### Further Properties of Flip-Flop
- Unlike $\star$, signal at Q is stable throughout the entire clock period, and change only in the next clock period.
- $\star$ is only stable half the time when the master is at 'read', but reflects ever-changing D-input signal during 'write'.
- This configuration produces new value at Q from input at D at every rising edge of CLK

It is as if we capture the instantaneous vaue of D at each CLK rise edge, and reflect it at Q for that entire period of CLK.

Note: You can also make the slave be the one to receive the inverted CLK signal, and value at Q reflects the input at D at each falling edge of CLK.
Note: the name edge-triggered comes from the fact that the output at port Q of the slave changes only when the CLK edge changes

## Timing Specifications of Sequential Logic VS Combinational Logic Devices
[[CMOS Technology#Timing Specifications of Combinational Logic Devices|Recall timing specifications for combinational logic devices, and how to compute them.]]
For sequential logic devices,
### Propagation Delay $t_{pd}$
> Time taken for valid `1` CLK input to produce a valid final output of the SL device

### Contamination Delay $t_{cd}$
> Time taken for an invalid CLK input, as a result of transition from `0` to `1`, to produce an invalid output of the SL device.

### Comparing with Combinational Logic Devices
| Combinational Logic Devices                                                                                                | Sequential Logic Devices                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| No input CLK and units with feedback paths                                                                                 | Has CLK and feedback path                                                                                                       |
| $t_{pd}$: time measured from the moment a valid input is fed to the circuit to the moment a valid output is produced       | Input is CLK, not user input, inparticular only with CLK transition from `0` to `1`, where Flip-Flop captures a new input value <br>**tpd** and **tcd** of a sequential circuit is counted from the **last** downstream register(s)|
| $t_{cd}$: time measured from the moment an invalid input is fed to the circuit to the moment it produces an invalid output | Ditto: input is CLK                                                                                                                       |

The **tpd** and **tcd** of a sequential circuit is counted from the **last** downstream register(s) (there can be more than one) in the circuit because our reference "input" is no longer IN but the CLK.
## Flip-Flop Timing Constraint
[[#The Dynamic Discipline]] has to be obeyed to make sure we do not store invalid input signals.
Hence, the dynamic discipline for slave has to be obeyed by master, because the output of master is input to slave.

To obey this, there exists a timing constraint for the Flip-Flop configuration:
$$t_{cd_{master}} > t_{H_{slave}}$$
### Reason
Consider the scenario: 
INV CLK seen by master changes from `0` to `1`, and at the same time CLK seen by slave changes from `1` to `0`
- This transition is not immediate; there is a short time window where CLK goes from `1` to invalid value to `0`.
- => implies master goes to 'write' while slave goes to 'read' simultaneously
- However $\star$ at output of master cannot change immediately to fulfil $t_H$ requirement of slave
- $\star$ must retain its previous valid value (when clock invalid) and, before $t_H$ is fulfilled, cannot immediately:
	- become invalid due to CLK transition
	- reflect new input at D of master even though master is at 'write'
- This means the $t_{cd}$ of master (time taken on signal $\star$ is invalid after CLK at G becomes invalid) has to be larger than hold time of slave

## Sequential Logic Device Timing Constraint
We can now use a Flip-Flop in our circuit as a 'memory' device that we can put in series, either before or/and after any combinational logic circuit.

**The _dynamic discipline_ has to always be obeyed at any part of the sequential logic circuit/device.**

Due to this, we have **two** timing constraints called **$t_1$ and $t_2$** that should **always** apply for **any** path between two (one upstream and one downstream) connecting Flip-Flops (regardless of how many CLs are there in the middle of the two Flip-Flops) in a SL circuit.
Example:
![[Pasted image 20220214104159.png]]
![[Pasted image 20220214104242.png]]
From the above:
> $$
 \begin{align}
 t_1&: &t_{cd}R_1 + t_{cd}CL &\geq t_H R_2 \\
 t_2&: &t_{pd}R_1 + t_{pd}CL &\leq t_{CLK}
 \end{align}
 $$

 where $t_{CLK}$ is clock period.
 ### Explanation
 - $t_1$: ensures $t_H$ requirement of R2 is fulfilled by devices before it; that is CL and R1 in example above
	 - When CLK rises at $t_i$, both R1 and R2 are capturing different values simultaneously
	 - R1: receive input at $t_i$
	 - R2: receive computed old input produced from R1 at $t_{i-1}$
	 - Devices upstrea mof R2 has to help hold on to this old value for $t_H$ of R2 to be fulfilled before responding to the rising edge of the clock and producing new values
 - $t_2$: ensures clock period is long enough for 3 things to complete:
	 - Valid signal to be produced at the output of R1
	 - Signal to propagate through CL in between
	 - Signal to be setup at the downstream register R2 for read mode

Both must be fulfilled within any paths between 2 connecting registers in a circuit, in order for the overall circuit to obey the dynamic discipline.

We can call the $t_{pd}CL$ as the time taken to do actual work or logic computation

The propagation or contamination delays of a Flip-Flop is not considered a logic computation, because unlike combinational logic devices (that can be made to implement functionalities such as addition, subtraction, boolean expressions, etc), a Flip-Flop **does not implement** any other special functionalities except to function as a memory device.


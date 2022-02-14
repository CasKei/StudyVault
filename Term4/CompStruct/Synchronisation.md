---
aliases: 
tags: #50.002
---
[[Comp Struct]]
[Lecture vid](https://youtu.be/HlizelEp4Yc)
[Notes](https://natalieagus.github.io/50002/notes/sequentiallogic)
Cont. from [[Sequential Logic]]

## Synchronisation with Input
In any sequential logic circuit, we use a single synchronous clock.
> Single synchronous clock: one same clock used for any register in the device.

Our [[Sequential Logic#Flip-Flop Timing Constraint|timing constraints]] ensure that the CLs are given valid and stable input long enough for it to produce meaningful output.

### Problem
==The external input needs to obey the ***[[Sequential Logic#The Dynamic Discipline|dynamic discipline]]*** of the first upstream register (the one recieving external input) in the circuit.==

In practice, it is impossible for any arbitrary input to be synchronised with the clock and satisfy the [[Sequential Logic#The Dynamic Discipline|dynamic discipline]].

## Violation of [[Sequential Logic#The Dynamic Discipline|dynamic discipline]]
![[Pasted image 20220214111650.png]]
When one of the timing constraints ($t_H$ in this case)  is violated, we may end up storing the invalid values during 'read' mode.
This event of storing invalid value is called [[#The Metastable State]].

## The Metastable State
![[Pasted image 20220214084537.png]]
Due to the feedback loop in the [[Sequential Logic#Storage Device D-Latch|D-Latch]], it has a unique property where there exists a point in its voltage chacteristics functino where $V_{in} = V_{out}$.

We can plot $V_{in}$ (Q') VS  $V_{out}$ (Q)
![[Pasted image 20220214113152.png]]
- **Red line: feedback constraint**
	- $V_{in} = V_{out}$
	- This is the effect of connecting the output of the multiplexer to itself on the first input port
- **Green line: VTC of a 'closed latch' state**
	- When the selector bit of multiplexer receives a `0`

Notice that in 'closed latch' state, the D-Latch passes the value from $V_{in}$ as output at $V_{out}$, thus we have a shape that resembles a buffer.

==Notice 3 solutions formed by the intersection of red and green lines.
2 are valid voltages, and the middle point is metastable, denoted as $V_m$.==

We are creating a device which output is connected back as input, so we need to know where the system will tend towards.

**Stable Low:**
- If initial $V_{in} << V_m$, => produce an even lower $V_{out}$
- $V_{out}$ produced becomes new $V_{in_2}$, producing even lower $V_{out_2}$
- Traverse to stable low

**Stable High:**
 - If initial $V_{in} >> V_m$, => produce an even higher $V_{out}$
- $V_{out}$ produced becomes new $V_{in_2}$, producing even higher $V_{out_2}$
- Traverse to stable high

**Metastable:**
 - If initial $V_{in} = V_m$, => produce same $V_{out} = V_m$
- $V_{out}$ produced becomes new $V_{in_2}$, producing same $V_m$
- Stays at $V_m$ (invalid) in a noise free case.

Hence, without external disturbances, there is always a chance that we need to wait forever to settle to a valid stable value.

Noise may drive $V_{in}$ up or down and eventually may settle into a stable value but thsi is not guaranteed in bounded time.

> Metastable state: the state whereby your [[Sequential Logic|SL]] device is unable to settle to a stable/valid value for an unknown period of time.

We do not want this because output is invalid during this unknown timeframe and therefore rendered useless.

### Properties of Metastable State
- Corresponds to an invalid logic level - the switching threshold fo a device
- It is an unstable equilibrium, a small noise may cause it to accelerate towards either ends, but it also may not
- Depending on how close $V_{in}$ is to $V_m$ with noise, it may also take forever to settle to a stable value
- Every bistable system exhibits at least one metastable state

> Hence, the metastable state is an inevitable risk of synchronisation because our active device always have a fixed-point voltage $V_m$ such that $V_{in} = V_m$ implies $V_{out}=V_m$, caused inherently by the feedback loop constraint and the VTC of the multiplexer

The **violation of dynamic discipline** may put our feedback loop at some voltage _near_ $V_m$. The **time taken** for $V_{out}$ to eventually settle towards a stable `0` or `1` is **inversely** proportional to current $\|V_{out} - V_m\|$, and is _theoretically infinite_ for $V_{out} = V_m$.

Since there is **no lower bound** on $\|V_{out} - V_m\|$, then there is **no upper bound** for the settling time of eventual $V_{out}$ value.

**In other words, we cannot completely avoid the metastable state**.

## Solution
The only thing we can do is to **minimize** the metastable state's probability from happening. We can do that by introducing more **delays** between the first 'upstream' Flip-Flop and the CL devices downstream in the hopes that the signal will somehow settle towards either end before reaching the CL, as illustrated here:
![[Pasted image 20220214123311.png]]
Note that this comes at the cost of _responsiveness_ of the device.
#50.002
# CMOS Technology
[Lecture](https://youtu.be/JqgZcV_1IU4)
[Notes](https://natalieagus.github.io/50002/notes/cmostechnology)
[[Digital Abstraction|Previous notes]]
[[Comp Struct|Course info]]

## Overview
[[Digital Abstraction#Combinational Device|Recall]] that the ideal behaviours and characteristics of a combinational logic device are:
1. Can tolerate some amount of errors due to its **Noise Margins**. Noise margins exists if its VTC gain > 1
2. If have high [[Digital Abstraction#^21e7e9|gain]], can have more noise margin.
3. Device should be small and cheap
4. Device should have zero power dissipation when input voltages aren't changing, that's why it must have a nonlinear gain.
5. Otherwise when voltage is changing from `0` to `1` or otherwise, then power within the device has to dissipate easily.
6. Device has to be functional, conforming to the assigned truth table (logic) at all times.

In this chapter we are learning a particular component called the MOSFET that can be used as a building block for our combinational logic device. It has all the characteristics mentioned above.

## MOSFET
MOSFET: Metal-oxide semiconductor field effect transistors
- Main material used to make our combinational device.
- 4 terminal voltage-controlled switches

![[Pasted image 20220131172149.png]]
Current flows between the diffusion terminals (source and drain) if the voltage on the gate terminal is large enough to create a conducting channel (in pink) and the MOSFET is on. Otherwise the conducting chnnel does not form and the MOSFET is off: the diffusion terminals are not connected.

Notable parts and its function:
1. Switch `1`s and `0`s and vice versa so we can implement functionalities
2. Has 4 terminals. Input supplied at the gate, output obtained at the drain.
3. $I_{DS} \propto \dfrac{W}{L}$: Current flow between source and drain is prop to width and length of MOSFET
4. Source and drain is physically symmetrical, we name them depending on the type of the MOSFET.

Recap:
- Current flow from higher potential (+) to lower potential (-)
- Electrons flow from lower potential (-) to higher potential (+)

## Types of MOSFETs
With MOSFETs we can create a combinational logic device that represents our designed truth table or functional logic specification.
But before we learn to create such devices, we need to learn 2 basic types of MOSFETS.
1. **NFETs**:
	1. Bulk: majority of charge carriers are holes (p-type)
	2. Source and drain: majority of charge carriers are electrons (n-type)
	3. Bulk, S is connected to `GND` to keep PN junction reverse biased
2. **PFETS**:
	1. Bulk: majority of charge carriers are electrons (n-type)
	2. Source and drain: majority of charge carriers are holes (p-type)
	3. Bulk, S is connected to `VDD` to keep the PN junction reverse biased

Some terms:
- `VDD`: Voltage source
- $V_{TH}$: threshold voltage
- `GND`: ground
- Reverse biased: a state whereby D is insulated from S, so current cannot flow from D to S **in the presence of applied voltage**
- ON: a state whereby there exists a connection between D and S so that current can flow through them
- OFF: a state whereby there is no connection between D and S. Current cannot flow through them.

Circuit symbol for NFET and PFET are shown as below.
NFET bulk --> `GND`, PFET bulk --> `VDD`.
![[Pasted image 20220131175844.png]]
This figure explains how they operate. Top are PFET, left OFF right ON. Bottom NFET.
![[Pasted image 20220131175951.png]]
## NFETs switching
![[Pasted image 20220131204949.png]]
- Connections
	- Bulk --> GND: keep PN junction reverse biased: no current should flow or leak between S and bulk and between D and bulk
	- S --> GND: Current from D is drained to GND
- ON when $V_{GS} = V_G - V_S$ is **high** enough. Since S terminal is connected to GND:
	- $V_{GS} = V_G - 0 = V_G$
	- ON: $V_G$ is high enough, i.e. $> V_{TH}$.
	- When $V_G > V_{TH}$, it draws the electrons towards the gate. An n-channel made of electrons will be formed between S and D
	- $V_{TH} > 0$
- ON: current can pass through from D to S
	- Electrons (its majority charge carrier) flows from S to D: majority charge carrier is drained at D
	- Hence output of ON n-type is `0` at D terminal
- OFF: $V_{GS}$ is low, as it encourages depletion region to form further

## PFETs switching
![[Pasted image 20220131210610.png]]
- Symbol: similar to NFET except it has buble `o`
- Connections
	- Bulk --> VDD: keep PN junction reverse biased: no current should flow or leak between S and bulk and between D and bulk
	- S (also bulk) --> VDD: Current can flow from S to D
- ON when $V_{GS} = V_G - V_S$ is **low** enough. Since S terminal is connected to VDD,
	- $V_{GS} = V_G - VDD$
	- ON: $V_G - VDD$ is low enough. i.e. $< V_{TH}$
	- When $V_G < VDD + V{TH} \Leftrightarrow V_{GS} < V_{TH}$, it draws the holes towards the gate. A p-channel (made of holes) will be formed between S and D
	-  $V_{TH} < 0$
- ON: current can pass through from S to D
	- Holes (its majority charge carrier) flows from S to D: majority charge carrier is drained at D
	- Hence output of ON p-type is `1` at D terminal
- OFF: $V_{GS}$ is low, as it encourages depletion region to form further

## Summary of NFET and PFET
- MOSFETs operate using voltages
- No current flows from the gate to the S/D since the gate is insulated from S and D
- This is unlike common cheaper PNP and NPN transistor (standard bipolar junction transistor(BJT)) that operates using current
- The output that we get at the D of either PFET or NFET is a result of the connection between S and D due to the presence/absence of voltage in the gate.

## Supplementary Sections
### P-type and N-type Semiconductors
|P-type|N-type|
|---|---|
|Plenty of acceptor atoms|Plenty of extra electrons (donor atoms)|
|Majority charge carriers are holes|Majority charge carriers are electrons|

- Electron: one of the constituents of an atom, having a negative charge
- Acceptor atom: has for example 3 electrons in valence shell and can accept one electron to complete the covalent bonding. Thus it gains one extra electon and acquires negative charge
- Donor atom: has 5 electrons in valence shell and can donate one extra electron. It thus acquires unit positive charge in the process.

### Depletion Region
When [[#P-type and N-type Semiconductors]] are placed together, **the free electrons from n-type will flow over (diffuse) to the p-type and fill its holes (impurities).**
Filling up a hole results in a **negatively charged ion at the p-type** semiconductor. Equally, free electrons leaving the n-type leaves behind a **positively charged ion at the n-type** semiconductor.
Eventually, a space-charge builds up forming an electric field, preventing more free electrons from the n-type to  the p-type, thereby forming an insulating layer called depletion region

### P-channel or N-channel Formation
For NFETs, when there is a high (positive) voltage at the gate, it repels the extra holes at the p-type bulk. Basically a positive voltage applied to the gate attracts electrons (which are minority in the p-type substrate) to the interface between the gate dielectric and the 2 n-types semiconductors (D and S).

These electrons form a conducting n-type channel between the S and D, called the inversion layer. When there's poential difference between the D and S, the current will flow from S to D through this inversion layer.

For PFETs, the opposite happens. When there is a presence of low (negative) voltage at the gate, it repels the extra electrons at the n-type bulk. Basically holes (minority in n-type substrate) are majority in the region betweenthe gate dielectric and the 2 p-type semiconductors, forming a conducting p-type channel (inversion layer). When there's potential difference between D and S, then the current will flow from S to D through this inversion layer.

Note the position of S and D in PFET is switched, compared to NFET.

### Naming of Source and Drain
The naming of S and D terminal depends on the majority of the charge carrier.
==The majority charge carrier is always meant to be drained at D and sourced at S, so it flows from S to D.==

|PFET|NFET|
|---|---|
|Current flow from S to D|Current flow from D to S|
|Majority of charge carrier is holes (positively charge)|Majority of charge carrier is electrons (negatively charged)|

Note: Current cannot flow back out to the Gate because there is a capacitor there with infinite resistance. The function of the gate capacitor is to create electric field enough to pull either electrons up to the gate in NFETs or choles up to gate in PFETs to create a conductive n-type (electrons) or p-type (holes) channel.

### Reverse Bias in PN Junction
Bulk in PFET --> VDD
Bulk in NFET --> GND

We do this to keep the PN junction in each FET to stay in the reverse biased state by default, until they are switched ON.
	Why we need to keep them in reverse biased state by default: so that it encourages the presence of the depletion region hence preventing major current leaks across the junctino when the FET is OFF.
[Video about reverse biasness](https://youtu.be/cJxBlO5NMGs?t=295)

## Complementary MOS circuitry
To form a fully functional combinational logic device that implements a particular functionaity or logic, these PFETs and NFETs can be connected together to form a CMOS circuit. (Complementary Metal-Oxide Semiconductor)

There are 2 parts of CMOS: the pull-up circuit and the pull-down circuit. Its general schematic is below:
![[Pasted image 20220201155524.png]]
### Pull-up circuit
1. All FETs are PFETs
2. All bulks connected to VDD
3. All Sources connected to VDD
4. When there is a open connection from Source to Drain, output of the overall CMOS circuit is `1`.
5. ON: there exists any direct path for *current* to flow from any S of the PFETs to the logical output D
### Pull-down circuit
1. All FETs are NFETs
2. All bulks connected to GND
3. All Sources connected to GND
4. When there is a open connection from Source to Drain, output of the overall CMOS circuit is `0`.
5. ON: there exists any direct path for *electrons* to flow from any S of the NFETs to the logical output D

## The CMOS Complements Recipe
Imagine if both pull-up, pull-down, and overall are ON.
	Means there exists a direct open connection to GND from VDD
	--> source of pull-up -> source of pull-down
	--> VDD -> GND
	Results in **short circuit**.
Hence it is very **important for a CMOS circuit to contain complementary pull-ups and pull-downs.**
	This means that only one component, either the pull-up or the pull-down, is ON at any time.

==A combinational logic circuit can be made by **connecting two NFETs in series as a pull-down circuit**, and **two PFETs in parallel as a pull-up circuit**.==
![[Pasted image 20220201172615.png]]
For example, the following tis a CMOS circuitry for a NAND gate:
![[Pasted image 20220201172813.png]]
- 2 inputs, `A` and `B`
- Each input can take either high or low voltage: `1` or `0`.
- A --> PFET on left, NFET on top
- B --> PFET on right, NFET on bottom

1. Case 1: `A,B=1`
	1. A: PFET on left OFF, NFET on top ON
	2. B: PFET on right OFF, NFET on bottom ON
	3. Current from VDD cannot flow to the output through any of the left and right PFET
	4. Current at the output is drained down to the GND through both NFET on the top or NFET on the bottom
	5. Output is `0`
2. Case 2: `A=0`, `B=1`
	1. A: PFET on left ON, NFET on top OFF
	2. B: PFET on right OFF, NFET on bottom ON
	3. There is no connection between the output and the ground
	4. Current from VDD can still flow from the PFET on the left to the output
	5. Output is `1`

There are 4 cases. Construct own truth table as practice.

==Notice how there is parallel PFET in the pull-up, and series NFET in the pull-down.==
This is the **recipe** for **CMOS complement**, ensuring that there will be no combination of input that will cause both pull-up and pull-down circuits to be ON

## Logic Gates
==Gate: A combinational device with multiple inputs but only one output==
## Timing Specifications of Combinational Logic Devices
Recall that combinational devices have timing specifications that tell us the upper bound required propagation time to compute the specified output given a set of valid and stable input values.
#### Propagation delay $t_{pd}$
Propagation delay is a specification that a combinational logic device must have.
> Assume the output of a device is initially invalid.
> Propagation delay: time taken for the device to produce a valid output, measured the moment it was given a valid input.

The **effective** $t_{pd}$ of an entire circuit is the **maximum cumulative propagation delay over all paths** from inputs to outputs in the combinational logic circuit.
- Each component must wait for one another to produce a valid overall output.
- All components have to produce valid results 

#### Contamination delay $t_{cd}$
Contamination delay is a specification that is typically measured and indicated on a combinational logic device.
> Assume the output of a device is initially valid.
> Contamination delay: time taken for the device to produce an invalid output, measured from the moment it was given an invalid input.

The **effective** $t_{cd}$ of a circuit is the **minimum cumulative propagation delay over all paths** from inputs to outputs in the combinational logic circuit.
- It takes the fastest route to propagate invalid signal
- Finally contaminates any output (that is, to be invalid when initially valid)

## Exercise
CMOS gate: complementary [[#Pull-up circuit]] and [[#Pull-down circuit]]
With these gates, we can form a combinational logic circuit, example as shown
![[Pasted image 20220201192301.png]]
Given $t_{pd}$ and $t_{cd}$ for NAND gate: $t_{pd} = 4ns, t_{cd}=1ns$, we find:
- Overall $t_{pd} = 12ns$ (red path)
- Overall $t_{cd}=2ns$ (blue path)

## Summary
[Post lecture vid](https://youtu.be/cJxBlO5NMGs)
- Understand how a MOSFET can be used as the most basic building block (element) in digital circuits.
- There are 2 types of FETs (NFET and PFET), that can be 'activated' (switched on) or 'deactivated' (switched off) using proper voltages supplied at its gate.

- It takes time for FETs to work: to react to the input voltage at its gate and establish a low or high voltage value at its drain.
- Thus, it is important to specify the timing specifications of a combinational logic device so that users may know how long the device takes to react (either to a new valid input or to an invalid input).
	- This tells us at what rate we can supply new inputs to the device and how fast the device can compute/process a batch of input values.

- Assemble a few FETs to implement any truth table or Boolean functions (learn more next chapter), hence creating a combinational logic devices
- Gate: a specific type of combinational logic device that has one output bit.
- There are many types of gates depending on Boolean function that's function that's realised.
- An even larger combinational logic circuits (that realises more complicated Boolean functions) can be creatde by assembling many of these gates together.
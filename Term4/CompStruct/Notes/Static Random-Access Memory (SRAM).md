---
aliases: SRAM
tags: 50.002
---
[[Comp Struct|50.002]]
[[Memory Hierarchy]]

## Transistors
- Made up of 6 transistors
	- Commonly called a 6T-SRAM cell
	- 2 [[CMOS Technology|NFETs]] at side, one N one P per inverter --> total 6
- Each cell stores **1 bit**
- The loop formed by 2 inverters can store a bit for **as long as they are powered**.
	- Since it can only retain info when powered, SRAM is a *volatile memory device*

## Bit Lines
Note: **Word line** and **two complementary bit lines**


The two bit lines are connected to a **sense amplifier**.

A sense amplifier’s role is to *sense the low power signal difference* from both bitlines and *amplify the small voltage swing to recognizable logic level* so the data can be interpreted properly by logic outside the memory. It is commonly made using 2 to 6 transistors.



## Reading and Writing
![](https://lh3.googleusercontent.com/3cHSLmGCC7YZOAvK-adZSrRz-7aAL4vxwLiPb8NEybNjXaG2o-R-qI7_NcqWAjYt94mP6H8z8KaoWLeNEoygmwmSERWyP0jui0O_9cyJzhxlbusdV_Zd5Z3MbIZ-Ir4T-zCAPdHL)

| To Read                                                                                                                                                         | To Write                                                                                                   |     
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | 
| Supply high voltage to the _word line_. This will connect the source and the drain of both NFETs.                                                               | Similarly, supply high voltage to the _word line_.                                                         |     
| In turn, current flows to the bit line on the right and its complement on the left.                                                                             | Then, drive a **strong** high voltage or low voltage **through the bit line and its complement** as shown. |     
| The sense amp at the end of both bit-lines will compute the difference and amplify the small voltages to a normal 1-bit logic level.                            |                                                                                                            |     
| For example, if the sense amp computes a `+ve`difference between $V_{\text{bit}} - V_{\overline{\text{bit}}}$, then it corresponds to logic `1` and vice versa. |                                                                                                            |     
| In the figure above, the value of this cell is initially `1`.                                                                                                   | In this example, the value of the cell is written to be `0`.                                               |     

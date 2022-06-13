---
aliases: DRAM, physical memory, RAM, main memory
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Memory Hierarchy]]

## 50.005
### RAM
[[Dynamic Random-Access Memory (DRAM)|RAM]]
Ideal: permanent storage
Not possible:
- Main mem too smol
- Volatile and loses contents when powered off

Recall that the memory unit sees only a stream of memory addresses; it does not know how they are generated (by the instruction counter, indexing, indirection, literal addresses, or some other means) or what they are for (instructions or data).

## 50.002
![](https://dropbox.com/s/4wovmxsgb7896vd/dram.png?raw=1)
![A stick of RAM](https://lh6.googleusercontent.com/O_L9qNZezzm7XJCtTBBnSnWHASX7IBX6t1EcGGs7rvg1QvftQVQXaVVDJOATdiv_VL8FBSlUxkE_02Wdz78n7Hmt2Nosu-WYh3qEATOTIIXUJFYPPOQN9m4PpZNCV1E7U3xuYdZU)  
A stick of RAM

A single DRAM cell is capable of storing 1-bit of data by using just _single NFET_ and a _single capacitor_ **when powered**:

> This is often called as 1T-DRAM. DRAM is also a volatile memory device.

## Reading and Writing
| Read                                                                                                                                                                                                                                   | Write                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Supply high voltage to the word line, and this will switch the NFET `on`.                                                                                                                                                              | Supply high voltage to the word line, and this will switch the NFET `on`.                                                                |
| Charges can flow to the bit line when there’s direct connection between the capacitor and the bit-line.                                                                                                                                | Supply strong `1` or `0` through the bit line to charge or discharge the capacitor.                                                      |

## Gates/function
 Note: we don’t really need to dive into details of how capacitor work. The ability of the capacitor to store a charge is called _capacitance_, and it is affected by the dielectric materials of the plates and the plates’ dimension.

[[Sequential Logic\|D-Latch]] use 1 mux: 4 NAND gates = 16T\
[[Sequential Logic\|D Flip-Flop]] use 2 mux: 32T + 2T for the inverter

## Problem
>Capacitor will **lose charge over time**, so data stored in cells will fade over time.

To tackle this, each DRAM cell has to be **refreshed** very frequently to keep the data intact.

These refresh cycles cause DRAM to be **significantly slower** than [[Static Random-Access Memory (SRAM)|SRAM]], although a DRAM is **cheaper** due to fewer number of transistors in a cell.

## Physical Memory
We name the memory device that uses DRAM as its main technology the **physical memory**
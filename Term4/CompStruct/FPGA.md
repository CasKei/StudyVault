---
tags: #50.002
---

## What is FPGA
> Field Programmable Gate Arrays:
> Semicon devices based around a matrix configurable logic blocks (CLBs) connected via programmable interconnects.

Can be reprogrammed.
Are integrated circuits (ICs), which are groups of programmable logic gates, memory and other elements.

The user programs the hardware circuits.

## Basics -- Programmable Fabric and I/O
At their core, FPGAs are simply integrated circuits that connect a bunch of logic gates and I/O circuitry.
I/O circuitry takes in data from a source and spits out data at the other end into some other system.

The core of an FPGA is simply an array of logic gates and wires etched into an IC in a way that allows you to configure them.

## Alchitry Au
[More hardware specs](https://alchitry.com/boards/au)
- Xilinx Artix 7 FPGA
- 33280 logic cells
- CLK: 100MHz
- 102 IO pins at 3.3V, 20 can be switched to operate at 1.8V.
- DDR3: built in memory controller connected to 256MG of DDR3 RAM
- Power: USBC
- Peripherals: 8 general use LED, button for reset, 100MHz oscillator

[[Lucid]]
---
tags: #50.002
---
[[Comp Struct|50.002]]
[[FPGA]]

Mainly shows how to handle I/O units, namely *reset*, *input button presses*, and *rounting output to external LEDs*.
We will utilise all the parts we have learned before in [[First FPGA Project]], [[Toddler]], [[Synchronous logic for FPGA]] (CL, Seq, DFF and FSM, usage of counter to slow the clk, and ROM.)

Finally we try to write our own constraints `.acf` file to connect our board to the external LED outputs (or button/switch inputs).

_Note_: We won’t be discussing how to use the [7 segment](https://alchitry.com/io-element) here.
**The Io Element Base template** itself also already contain a sample on how to use the 7-segment, so please study it.
If you do buy an external 7-segment, please take note of the required **supply voltage**. Also pay attention whether you’re buying a [cathode or anode](https://www.electronics-tutorials.ws/blog/7-segment-display-tutorial.html) 7-segment.

The Au board can only supply up to 5V, so if it needs more than that then you need to use an **external power supply**. . Grab some BJT (NPN for Cathode type or PNP for Anode type typically, but either works) transistors to amplify the input signal from the Au Board. You can read some easy online tutorials on how to [use transistors as a switch](https://www.electronics-tutorials.ws/transistor/tran_4.html).

## Resetting Modules with Custom Clock
If you supply a custom clock to your synchornous logic units:
1. Standard `reset` button will not work anymore, you need a *manual reset*.
2. There is no easy way to synchronise the reset of this unit with custom clock and the rest of the units with the FPGA clock. Depending on your design, it might be problematic if some units come out of reset earlier / later than others.

==By definition, a system reset must reset ALL components synchronously==.
### Manual Reset with Another Button
In [[Toddler]], we declared `seq_plus_two.luc` with a slowclock so we can see the output change.
```verilog
counter slowclock(#SIZE(1),#DIV(26), .clk(clk), .rst(rst));
seq_plus_two seqplustwo(.clk(slowclock.value), .rst(rst));
```
Notice that 
### Manual Reset Issue

### Reset Conditioner

### Slowing the output rate and enabling system reset for `seq_plus_two.luc`
### Slowing the output rate and enabling system reset for `seq_plus_vary.luc`

## Conditioning Button Presses

## Using Button Presses as Triggers

## Storing Button Press Sequences

### Planning

### Declaring the module

### Test it

### I/O Error

## Summary

## Final note

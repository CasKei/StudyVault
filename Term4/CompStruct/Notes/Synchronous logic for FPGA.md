---
tags: #50.002
---
[[Comp Struct|50.002]]
[[FPGA]]

## Problem
No concept of time.
We need a flip flop.

## Clocks
A signal that toggles between 0 and 1.
Au: 100Mhz

## DFF
In practice, the only required signals are D, Q and clk. Forget about rst and en.
It copies the signal D to Q whenever there is a rising edge of the clk.
Since the FF remembers what the input was at D, it is actulaly one of the most basic memory elements.

## rst and en
rst is used to reset the FF to a known state.
In FPGA this signal is generally very flexible and allows you to reset the FF ot a 1 or 0 when signal is high or low.
Lucid uses high resets (rst 1 -> reset)

There are times when you want the FF to ignore the rising edges on the clk to preserve hte contents pf Q.
Thats when you use the enable signal. When en is 1, FF operates normally.
When it is 0, the contents of Q won't change on the rising edges of the clk.
If you see a FF without an en signal it is just assumed that hte FF is always enabled.
In Lucid DFFs don't have and explicit en signal, but rather will retain its contents if you don't write something new to it.

## Creating the Module
`blinker.luc`

## Writing the Blinker
```verilog
module blinker (
	input clk,    // clock
	input rst,    // reset
	output blink  // output to LED
  ) {
  
  dff counter[25](.clk(clk), .rst(rst));	

  always {
	blink = counter.q[24];
	counter.d = counter.q + 1;
  }
}
```
## Reset
When rst high, value of counter.q 0.
This is also the value that the counter is initialized to whne the FPGA first starts.

If we wanted the counter to initialise and reset to a different value, we can specify the value using the dff parameter `#INIT`.

The counter will now start with a value of 100 and reset to 100. 0 is the default value if not specified.

Notise that parameters are specified with `#NAME` instead of `.name`.
Parameters are always all capitalised.

If you don't need to reset a DFF for some reason, simply not connect anything to the rst input.
This is recommended since it doesn't force the tools to route the reset signal to the FF.

The DFF and FSM types are special in that the rst input is optional. All other inputs and all inputs to modules are required.

## Module connections
In Lucid, there are 3 ways to specify an input into a module, dff, or fsm.
First way is
```verilog
dff counter[25](.clk(clk)), .rst(rst));
```
Here we specify the connections in a set of parentheses directly after the name. These connections are only applied to this single module. However, we can use the next method to make the same connections to many modules.
```verilog
.clk(clk), .rst(rst) {
	dff counter1[12];
	dff counter2[7];
	dff counter3[8];
}
```
In this example, we connect the rst and clk inputs of all the modules contained in the curly braces. In this case, they contain 3 DFFs. This is convenient since most modules will require a clk and rst signal.

You can also nest this method.
```verilog
.clk(clk) {
	.rst(rst) {
		dff counter1[12];
		dff counter2[7];
	}
	dff counter3[8];
}
```
Here only counter1 and counter2 are connected to rst.

You can also mix this method with the first.
```verilog
.clk(clk) {
	dff counter1[12](.rst(rst));
	dff counter2[7];
	dff counter3[8];
}
```
Here only counter1 is connected to rst.

Finally the last way to specify an input is simply not connecting it when declaring, but rather inside the always block later.
That's what we did with counter.d.
Note DFFs and FSMs require you to specify clk and rst when declaring, and do not allow you to specify the d input then.

There is a diff when connecting an input at declaration time or in an always block.
The diff is only noticeable in arrays. If you have an array of a module and you specify an input at declaration time, that input will be copied to each element in the array individually.

If you specify an input in an always block, you can specify the input to each element separately. In this example, the clk signal is one bit, but it is getting copied to 25 one bit FFs. However, the d input, also one bit, is packed into a 25 bit array to use in the always block. That way we can use the d input as if it is really one big FF.

## Instantiating the module
Go au.top add it in.

## The reset conditioner
Now that we have actually used the reset signal for what it was intended for, we can talk about the _reset_conditioner_ module. The signal _rst_n_ comes from outside the FPGA. Signals from outside the FPGA are UNCLEAN! What I mean by this is that we don't know how external signals (especially from a button) will change in relation to the clock we are using. If the reset signal goes low really close to the rising edge of the clock, due to internal delays in the FPGA, some flip-flops may come out of reset before the rising edge while others could after. This means some flip-flops may stay reset for a cycle longer than others (NOT GOOD). Even worse, when signals change too close to a rising edge of a clock you run into metastability issues. This is covered later, but it basically means you aren't guaranteed the output of the flip-flop will be 1 or 0. It could be somewhere in between (0.5?) or even oscillate between values (BAD). This is where the reset conditioner comes in. It is a fairly simple circuit that synchronizes the reset signal to the FPGA's clock. This ensures that your entire design will come out of reset at once. If you want to read more than you'll ever want to know about resets, check out [this paper from Xilinx](http://www.xilinx.com/support/documentation/white_papers/wp272.pdf).
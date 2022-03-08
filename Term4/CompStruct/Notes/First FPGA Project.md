---
tags: #50.002
---
[[Comp Struct|50.002]]
[[FPGA]]

## Create a New project
haiz just finish being baby

top file: contains all external i/o of your design
Your future proj can be built out of many modules, but all must be submodules to this top module.

## Contents of a module
A module is a way to organise your project into smaller pieces broken apart by function. It is very similar to the concept of functions when programming when you break down your program into smaller, more manageable pieces. Modules are also nice because they can be reused in multiple parts of your design.

### Module Declaration
```verilog
module au_top (
	input clk,       // 100MHz clock
	input rst_n,     // reset button (active low)
	output led [8],  // 8 user controllable LEDs
	input usb_rx,    // USB -> Serial input
	output usb_tx    // USB -> Serial output
)
```
Always starts with `module` keyword followed by name of the module.
Convention to name module the same name as the file name.

After the module name comes an *optional parameter declaration*. (not in example here).

After that is *port declaration*. Where you specify all inputs, outputs and inouts.
An inout is a bi-directional port not covered here.

Most ports are single bit signals.
But `led` are multi-bit, This is declared by the `[8]` after the signal's names.

led has 8 LEDs on it.
rst_n has signal that is active low: typically 1 but when button is pressed it is 0.

### Always Block
Tis where all the magic happens. Where you can perform computation and read.write signals.
```verilog
always {
	reset_cond.in = -rst_n; // input raw inverted reset
	rst = reset_cond.out;   // conditioned reset
	led = 8h00;             // turn LEDs off
	usb_tx = usb_rx;        // echo the serial data
}
```
Notice I said the tools need to replicate the block's behaviour, not the block.
Inside an always block, lower statements have priority over earlier statements.
Similar in programming, and this abstraction makes it so much easier to prorgam complex logic.
Important to know this is an abstraction, you are not programming.

## Representing Values
A value is made of one or more bits.
Number of bits a value has is known as its width.
There are a few ways to specify a value, some use an implied width while others allow you to explicitly set a width.

The first way is to just type a decimal number.

Sometimes it is easier to specify a number with different radix. Lucid supports 3 different radix: 10, 2, 16.
To specify, prepend `d`, `b` , `h`.
For example `hFF`=255 and `b100`=4.
If no append, decimal assumed.

Important to remember that all numbers will be represented as bits in your circuit. When you specify a number this way, the width of the number will be the minimum number of bits required to represent that value for decimal. For binary, it is simply the number of digits, and for hex it is 4 times the number of digits.
Example: 7 is 3 bits wide (111), 1010 4 bits wide, hACB is 12 bits wide.

Sometimes you need more control over the exact width of a number. In those cases you can specify the number of bits by prepending the number of bits and radix to the value. For example 4b2 is 0010 instead of 10. You must specify the radix when specifying the width to separate the width from the value.

If you specify a width smaller than the minimum number of bits required, the number will drop the most significant bits. You will also get a warning.

## Z and X
When you specify a decimal number, all the bits in your value will either be a 0 or 1. However, each bit can actually be one of 4 values, 0, 1, x, or z. 

X means don't care. You want to assign a value but you don't care if it is 1 or 0. Useful for the synhesizer because circuit bay be simpler in one of the cases and it gives the tools the freedom to choose. During simulation x also means unknown.

Z means the bi is high-impedence or tri-stated. This means it is effectively disconnected. Note that FPGAs cannot realise high-impedance signals internally, so the only time you should use z is for the outputs of the top module.

Back to the `always` block, the first two lines connect te input `rst_n` to the input of the `reset_cond` module. Modules can be nested which makes it possible to reuse them and helps make your project manageable.

The next line assigns `led` output to all zeros. Turns off all LEDs.

On Alchitry, the last line connects the serial input pin to the serial output pin, effectively echoing anything that the FPGA receives over the serial port. We could also tie this pin to 1 to disable it.

There are no redundant assignments. So these signals will literally be connected to these values.

## Connecting the Button
We are going to modify the module to connect the reset button to the first LED.

Modify the line where led is assigned
```verilog
led = c{7h00, rst}; // connect rst to the fist LED
```
The output led is a 8 bit array. The signal rst is a single bit wide. To compensate, we use a concatenation operator.

To concaterate multiple arrays into one, you can use the concatenation operator `c{x,y,z}`.

We are concatenating 7 zeros with the rst.

Note that values are zero padded if the specified width is larger than the size required to store the value. 4b11 same as 4b0011.

If you don't care how many bits a value takes up, you don't have to specify it. The minimum number of bits that will still fit the value will be used. however when concatenating you should always specify a width.

## Building your project
Click the hammer.
First need to specify where you installed your builder.
Au: Settings -> Vivado Location... and point it to the Xilinx/Vivado/Year.Month folder.

Text will spit out. Just wait.

The important line is where it says Finished building project.
This means that the IDE was able to find a .bin file after, If you ever get a red message telling you the bin file coldn't be found, you should scroll up the buil messages for the error that caused it to fail.

## Loading your project
You have 2 options, the first is the hollow arrow, that will write your configuration driectly to the FPGA's RAM. The second is the solid arrow, that will write your configuration to the FLASH memory on the board. If to RAM, config lost wen FPGA loses power. If FLASH, config automatically loaded when the board is powered up.

If program to RAM then power cycle the board, the last config written to FLASH will be loaded.

If you want to stop the FPGA from being configured at power up, click eraser. Will wipe FLASH memory and clear FPGA current config.

## Duplication
What if we wnat all the LED to turn on and off with the button instead of just one?
```verilog
led = c{rst, rst, rst, rst, rst, rst, rst, rst};
```
Concatenation like before is long. There is a better way.
Duplication syntax `M x { A }`
M is number of times to duplicated A.
```verilog
led = 8x{rst};
```
Much cleaner!

## Array Indexing
Alternative way to write the code where we only want one LED to light. Assign the pats of the led array separately.
```verilog
led[7:1] = 7h0;
led[0] = rst;
```

There are 2 ways to select a group of bits. First (above) specify start and stop bits explicitly. Second, specify a start bit and total number of bits to einclude above or below start bit.

```verilog
led[7:1] = 7b0;  // select bits 7 to 1
led[7-:7] = 7b0; // select bits from 7 going down
led[1+:7] = 7b0; // select bits from 1 going up
```

benefi of using the start width syntax is the width is constant. This means you can use a signal to specify the start index.

## Always blocks
You can also rewrite
```verilog
led = 8b0;
led[0] = rst;
```
Since second statement has priority, led[0] will never be 0.

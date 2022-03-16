---
tags: 50.002, fpga
---
[[Comp Struct|50.002]]
[[FPGA]]

## Create Proj
Select *IO Element Base*

`io_led` connects to 24 LEDs, in a 2D array.
To turn all LEDs off,
```verilog
io_led = 3x{{8h00}};    // turn LEDs off
```
8h00 is base constant that is a single dimensional array of width 8.
x{} syntax duplicates.
We create a 1x8 array and duplicate 3 times.
This is equal to {8h00, 8h00, 8h00}

`io_seg` and `io_sel` controls the 4 segment LED displays. Active low.

`io_button` are the 5 push buttons.
_io_button[0]_ is up, _io_button[1]_ is center, _io_button[2]_ is down, _io_button[3]_ is left, and _io_button[4]_ is right.

`io_dip` is the 24 DIP switches. Arranged in 2D array.

## Reduction Operators
Similar to bit-wise operators but work on a single input array and always output one bit.
They reduce an array to a single bit.
```verilog
io_led[0][0] = &io_dip[0];
```
same as ANDing all the led individually
```verilog
io_led[0][0] = io_dip[0][0] & io_dip[0][1] & io_dip[0][2] & io_dip[0][3] & io_dip[0][4] & io_dip[0][5] & io_dip[0][6] & io_dip[0][7];
```
## Seven-Segment Displays
Has 4 seven seqment displays that are multiplexed.
 `io_seg` connects to the segments.
 ![[Pasted image 20220309130612.png]]
 `io_sel` selects which digit is active. Typically, only one digit will be active at any time. If you have more than one digit active, all active digits will show exactly the same thing since their segments are wired together.
 The way we are going to display four unique numbers is by cycling which digit is active really fast. If we can do this fast enough, our eyes can't tell and it looks like all four digits are always on.
## Indexing Segments
We set up modules that light one segment at a time.
**Project > Add Components > Miscellaneous** check off *Counter* and *Decoder*. **Add**.
Now this is in **Components**.
```verilog
.clk(clk) {
  // The reset conditioner is used to synchronize the reset signal to the FPGA
  // clock. This ensures the entire FPGA comes out of reset at the same time.
  reset_conditioner reset_cond;
  .rst(rst) {
    counter ctr (#SIZE(3), #DIV(25));
  }
}

decoder num_to_seg (#WIDTH(3));
```
Here we add the _counter_ and _decoder_ modules to the top level module. The _counter_ component requires both a clock and reset signal so we have it in the nested in both the _.clk_ and _.rst_ connection blocks. On the other hand, _decoder_ doesn't require either, so it is outside of both.

The counter is simply a counter. It will output a value starting from zero and increment to whatever the maximum value you set is. After that it will reset back to zero. It is also possible to configure it to count down from the max value to zero.

The counter has four parameters you can set to get it to operate how you want, but here we only need to change two. _SIZE_ dictates how wide the output of the counter is. In this case we need it to count from 0 to 7 for all 8 segments of our displays. Three bits is exactly 0 - 7. If we wanted to count to a value that wasn't conveniently a power of 2 minus one, we could set the parameter _TOP_ to control its maximum value.

The _DIV_ parameter is used to set how many bits to use to divide the clock. By setting this to 25 (or 24 on the Mojo), the counter will only increment its output every 225, or 33,554,432, clock cycles (16,777,216 on the Mojo). The clock runs at 100MHz (100,000,000 cycles per second) on the Au and Cu and 50MHz (50,000,000 cycles per second) on the Mojo. If the counter incremented every clock cycle it would be way too fast for us to see.

The decoder is a binary to one-hot decoder. If you need a refresher on one-hot representation check out the [encodings tutorial](https://alchitry.com/blogs/tutorials/encodings). Basically, the decoder will take our three bits and convert it to eight bits. If the input is 0, then the 0th bit of the output will be 1 and everything else will be 0. If the input is 4, the 4th bit will be 1 and everything else will be 0. This allows us to use the binary counter to light individual LEDs.

Note that the output of the decoder is 2_WIDTH_ bits wide. So in our case, 23 = 8 bits wide.

Now we can hook up the modules.
```verilog
always {
  reset_cond.in = ~rst_n; // input raw inverted reset signal
  rst = reset_cond.out;   // conditioned reset

  usb_tx = usb_rx;        // loop serial port

  led = 8h00;             // turn LEDs off

  num_to_seg.in = ctr.value;

  io_seg = ~num_to_seg.out; // connect segments to counter
  io_sel = 4h0;             // select all digits

  result = io_dip[1] * io_dip[0]; // multiply the switch values

  io_led = $build(result, 3); // convert result from a 24-bit array to a 3x8 array

}
```
We feed the binary counter value into the decoder and the output of the decoder to _io_seg_. Note that _io_seg_ and _io_sel_ are both **active low**. This means that when the signal is 0, it is active. To turn only one LED on we need to invert the output of the decoder with the bit-wise inversion, _~_, operator. This will make the signal zero-hot.

Also notice we need to set _io_sel_ to 0 so that the LED segments are selected. Setting all of them to 0 will turn them all on.

Build and load your project to your board. You should now see the segments of all 4 displays lighting one at time. Try to light only a single display by setting _io_sel_ to _~4h1_ instead.

## Getting Fancy with Numbers
asdfghjkl
## Decimal Counters

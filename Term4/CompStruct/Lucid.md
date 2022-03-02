---
tags: #50.002
---
[[Comp Struct]]
## Modules
When you create any design you will have a top-level module.
This is where inputs and outputs are actual inputs and outputs on the FPGA pins.
This is the only script that can interface with external I/O.
This is `au_top.luc`.

```verilog
module au_top (
    input clk,              // 100MHz clock
    input rst_n,            // reset button (active low)
    output led [8],         // 8 user controllable LEDs
    input usb_rx,           // USB->Serial input
    output usb_tx           // USB->Serial output
  ) {

  sig rst;                  // reset signal

  .clk(clk) {
    // The reset conditioner is used to synchronize the reset signal to the FPGA
    // clock. This ensures the entire FPGA comes out of reset at the same time.
    reset_conditioner reset_cond;
  }

  always {
    reset_cond.in = ~rst_n; // input raw inverted reset signal
    rst = reset_cond.out;   // conditioned reset

    led = 8h00;             // turn LEDs off

    usb_tx = usb_rx;        // echo the serial data
  }
}
```
### Port Declarations
First section of module: port declarations.
Declare inputs and outputs.
```verilog
    input clk,              // 100MHz clock
    input rst_n,            // reset button (active low)
    output led [8],         // 8 user controllable LEDs
    input usb_rx,           // USB->Serial input
    output usb_tx           // USB->Serial output
```
Notice `led` input has square brackets: this is 8 individual inputs bound tgt in an array.

### Before always block
Define other modules to be used like clock or reset signals, or simply intermediary connections using `sig`.

### Always block
Signifies a connection, sth that is always connected


### JSIM Syntax
Start with a capital case letter: the object type
`V`: voltage source
`M`: MOSFET, drain, gate, source, substrate(bulk) is specified in order
`NENH`: NFET
`PENH`: PFET

The thing on the right of the object type is the instance name 

Vds = 1.2V, Vgs = 5V, I = 841.804microA
R = V/I = 1.2/814.804microA = 1472.74682Ohm for W/L=1
For W/L = 2, multiply the above by 2

Vgs = 0V, Vds = 2.5V, I_leakage = 5.146pA
0.05pF capacitor
Q = CV
I/t=CV
t=CV/I=0.05p x 2.5 / 5.146p = 0.02429071123s
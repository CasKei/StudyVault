---
aliases: SVC
tags: 50.002
---
[[Comp Struct|50.002]]
[[Asynchronous Handling of IO Devices]]

> The SVC is a 32-bit instruction that triggers an ILLOP exception, hence [[Trap]]ping the process onto the [[OS Kernel]] whenever it is executed.

In beta [[Designing an Instruction Set|ISA]], the SVC has OPCODE `000001`.

Format:
`000001` `26 SVC-bits`, where up to lower 26 bits can be used to *index* the kernel service requested.

This instruction allows processes to "communicate" with the Kernel by interrupting its own operation and transferring [[Anatomy of the Beta CPU|CPU]] control to the Kernel (ILLOP handler).

The ILLOP handler saves the states of the calling process, before it checks if the OPCODE of the instruction that triggers the [[Trap]] is `000001`.

If so, it will branch to a generic `SVC_handler` (else branch to error exception handler).

`SVC_handler` does the following:
1. Examine the last faulting instruction
2. Extract its lower `N` bits
3. Branch to appropriate service routine as requested by the calling process based on the value of `N`:
```CPP
SVC_Handler: 
LD(XP, -4, R0)	| examine the faulting instruction
ANDC(R0, 0xN, R0) | mask out lower N bits
SHLC(R0, 2, R0) | make a word index
LD(R0, SVCtbl, R0) | load service table entry
JMP(R0) | jump to the appropriate handler
```

`SVCtbl` is a label for specific Kernel subroutines, such as writing output or fetching input from each devices.

`UUO` is a macro that directs the PC to each subroutine: `HaltH`, `WrMsgH`. You can read `lab8.uasm` to for more details.

```CPP
SVCTbl: UUO(HaltH) | SVC(0): User-mode HALT instruction
UUO(WrMsgH) | SVC(1): Write message
UUO(WrChH) | SVC(2): Write Character
UUO(GetKeyH) | SVC(3): Get Key
UUO(HexPrtH) | SVC(4): Hex Print
UUO(WaitH) | SVC(5): Wait(S), S in R3
UUO(SignalH) | SVC(6): Signal(S), S in R3
UUO(YieldH) | SVC(7): Yield()
```

## Example SVC
Processes running in [[Kernel mode and User mode|user mode]] do not have direct access to any hardware, so they cannot simply check the keyboard for new keystrokes. Moreover, the keyoard is shared for usage by many procesess running in the system.

One common example where `SVC` is made is when a process checks for keyboard input. E.g. the execution of `getchar()` in C.
- This means process needs to switch to [[Kernel mode and User mode|kernel mode]], and the [[OS Kernel]] helped to check if there's such input from the keyboard.
- The function `getchar()` is translated into `SVC(j)` (among other things) (value of `j` is OS dependent)
- `SVC(j)` [[Trap]]s the user process, switching it to [[Kernel mode and User mode|kernel mode]] and execute Kernel ILLOP handler.
- It eventually examines the value of `j` and branch to the appropriate service routine that is able to fetch the input for the keyboard: `GetKeyH`.
- Instructions in `GetKeyH` fetches the requested (assuming there's an input), and leave it in `Reg[R0]`
- `GetKeyH` returns the ILLOP handler. The handler restores the state of the calling process and resumes it.
- The process can now get the requested keyboard character from `Reg[R0]`.

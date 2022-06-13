---
aliases: stack
tags: #50.002
---
[[Comp Struct]]

## Overview
[[Assemblers and Compilers]]: we learned how to naively compile C into beta UASM. The beta UASM is an [[Assembler]].
Beta UASM provides a layer of [[Abstraction]] such that we don't need to bother with details on howto lead every byte of [[Beta Instruction Cycles|instruction]] onto the [[Anatomy of the Beta CPU|memory unit]], or keeping up with accounting matters suhc as physical memory address (we can replace these with labels instead)

This chaper: we learn about *function call procedures* and why we need to understand another concept called *stacks*.
Both allow us to have reusable code fragments that are *called* as needed.

We need blocks of code (functions) that we want to call over and over without rewriting them again. 

## Procedures and Functions
Consider the declaration and implementation of the function `fact`.
It receives one argument `int n` and returns an `int`.
```c
int fact(int n) {
	int r = 1;
	while (n > 0) {
		r = r * n;
		n = n - 1;	
	}
	return r;
}
```
When you have functions declared like this, there is *scoping*. This integer `r` is declared but is only accessible when this function is is executed. So once this function returns to the caller, there is no way to access what the value of `r` is anymore.
These are *local variables* to this fucntion.

The function is implemented as a fixed set of *procedure*/instructions. We can call it anywhere afterwards:
```c
int result_1 = fact(4);
int result_2 = fact(9);
```

If we were to naively assemble this, we can translate this into the following $\beta$ assembly source code:
```cpp
.include beta.uasm
|| we call fact(4) first
LD(R31, n_1, R1)	| load 4 to R1
ADDC(R31, 1, R2)    | instantiate r

check_while_fact_4: CMPLT(R31, R1, R0)	| compute whether n_1 > 0
BNE(R0, while_true_fact_4, R31)	| if R0 != 0, go to while_true_fact_4
ST(R2, result_1, R31)	| store to result_1

|| then we call fact(9)
LD(R31, n_2, R1) 	| load 9 to R1, rewriting its old value
ADDC(R31, 1, R2)    | reset r

check_while_fact_9: CMPLT(R31, R1, R0)	| compute whether n_1 > 0
BNE(R0, while_true_fact_9, R31)	| if R0 != 0, go to while_true_fact_9
ST(R2, result_2, R31)	| store to result_2

HALT() | stop

while_true_fact_9: MUL(R1, R2, R2)	| r = r*n
SUBC(R1, 1, R1)	| n = n-1
BEQ(R31, check_while_fact_9, R31)	| always go back to check_while_fact_9


while_true_fact_4: MUL(R1, R2, R2)	| r = r*n
SUBC(R1, 1, R1)	| n = n-1
BEQ(R31, check_while_fact_4, R31)	| always go back to check_while_fact_4

n_1 : LONG(4)
n_2 : LONG(9)
result_1 : LONG(1)
result_2 : LONG(1)
```

**There's obviously a few issues here:**
1.  The code is **not scalable**. What if we call the function `fact` many more times? How long the assembly code is going to be?
2. There's so many **repeated**, **boilerplate** code. We are **wasting memory** (RAM) space.
	-   `while_true_fact_4` and `while_true_fact_9` is technically identical for all 3 instructions `MUL`, `SUBC`, and `BEQ`, only differ in the second argument of `BEQ`: either branching to `check_while_fact_4` and `check_while_fact_9`.
	-   Same issue with `check_while_fact_4` and `check_while_fact_9` (the `CMPLT`, `BNE`, and `ST` instructions)
3. How do we know if we can _overwrite_ the existing contents on any register `Rx`?

In principle, a function:
-   Is a callable, _**reusable**_ series of instructions.
-   It has a single **NAMED entry point**. It means we know the address of first instruction for this function in memory.
-   **Parameterizable** (can access or receive a predefined number of arguments).
-   Has _**local variables,**_ which cannot be accessed anymore once the function returned.

Once a function returns, the CPU needs to know how to return to the _caller_, i.e: to know where is the return address of the caller.

For example,
```c
int fact(int n){         --- (2) 
	int r = 1;           --- (3) 
	while (n > 0){       --- (4) 
		r = r*n;         --- (5) 
		n = n-1;         --- (6) 
	}
	return r;            --- (7) 
}

int result_1 = fact(4);  --- (1) 
int result_2 = fact(9);  --- (8)
```

^132fe8

We know that we need to execute `fact` twice, the first with argument `4` and the second with argument `9`.
-   The first line of instruction that is executed is labeled with (1) above. We then enter the function, executing the lines labeled as (2) to (7) in sequence.
-   After (7), ==the CPU must know how to return to the caller, that is the address of instruction (1)==.
-   Instruction (8) tells the CPU to enter the function again for the **second run**, thus executing (2) to (7) for another round, before finally stopping.

## Procedure Linkage and Stack
Referring to the `fact` example in the [[#Procedures and Functions|previous section]], notice a few *accounting issues* that we need to address in order to have a scalable and memory efficient function call.

Assuming we have a single [[Anatomy of the Beta CPU|CPU]], and that instructions are loaded to the [[Anatomy of the Beta CPU|memory unit]] from address `0` and onwards sequentially,

We know that `r` and `n` are *local variables* within `fact`. We can no longer access them, e.g. print them outside of the function. This means ==we need to **clean them up** from any storage unit once the function returns==.

We also need to establish a ==location== where:
- A function can always *access its arguments*
- A function is expected to *put the return value*
- The [[Anatomy of the Beta CPU|CPU]] can *find the address of the caller*, i.e. where instruction (8) is in memory.

### Procedure Linkage Problem
In summary, the procedure linkage problems we need to solve are:
- A way to *pass arguments into procedures*
- Procedures need their *own local variables*
- Procedures need to be able to *use the [[Anatomy of the Beta CPU|CPU]] registers* without worrying about overwriting their original content
- Procedures might need to *call other procedures*, including themselves (recursion)

## Procedure Linkage Convention
The above issues can be solved by ==establishing a kind of procedure linkage convention==. We assume that the following is always obeyed when executing instructions within a function.
- *Return value* always stored at `R0`
- Arguments can be found in a *dedicated space in the [[Anatomy of the Beta CPU|memory unit]]* called the **Stack**.
	- `SP` (Stack pointer): Address at the top of the stack (first unused position) found in `R29`
	- `BP` (Base pointer): Address at the base of the stack can be found in `R27`
	- `LP` (Linkage pointer): Return address always stored at `R28`

==A **caller** must obey the following sequence==: ^d35458
1. Put arguments on **Stack**
2. Branch to target function, leaving return address in `LP`
3. Remove arguments on stack upon return
4. Obtain return value from `R0` if any

==A **callee** must obey the following sequence== ^04788a
1. Perform promised **computation**
2. Leave result in `R0` if any
3. Leave state of all [[Sequential Logic|register]]s in [[Anatomy of the Beta CPU|REGFILE]] except `R0` **unchanged** upon returning to the caller
4. Leave *stack data* **unchanged** upon returning to the caller.

## The "Stack" implementation
In general, a [[Stacks and Queues data structure|stack]] is a type of [[Data Types and Data Structures|data structure]] where you can perform two essential operations: `PUSH` and `POP`. Its principle is *last-in-first-out* (LIFO).

You always add item via `PUSH` operation to the top of the stack, and can only remove the topmost item in succession via `POP` operation from the top of the stack.

How to implement a [[Stacks and Queues data structure|stack]] [[Data Types and Data Structures|data structure]] to aid our function execution?

We ==**reserve** an arbitrary block of location== in our [[Anatomy of the Beta CPU|memory unit]] to be space for the stack.
Illustrated below is a block of [[Anatomy of the Beta CPU|memory unit]] from address `0x010C` to `0x0128` reserved as our [[Stacks and Queues data structure|stack]]:
![](https://dropbox.com/s/zwaa983jxrmq78n/stack_empty.png?raw=1)
We have ==conventions== as mentioned:
- `R29 (SP)`: contains address of top of stack (available location ot write to)
- Addresses increase *downwards*, hence stack grows *downwards*

We can `PUSH` to the stack via these 2 instructions:
-   `ADDC(SP, 4, SP)` (==increase== `SP`’s content by `4` so that it points to the next line address)
-   `ST(Rx, -4, SP)` (==store== content of chosen register `Rx` to address pointed by `Reg[SP]-4`).

To `POP` (remove data) from the stack, we can do so via these two instructions:
-   `LD(SP , -4, Rx)` (==load== the content pointed by `Reg[SP]-4` to a chosen `Rx`)
-   `SUBC(SP, 4, SP)` (==decrease== `SP`’s content by `4` so that it points to the previous line address)

In $\beta$ `uasm`, we simply create these macros for `PUSH` and `POP`:
-   `PUSH(Rx)` : ==push== `Reg[Rx]` onto the stack
-   `POP(Rx)`: ==pop== the value on top of the stack to `Reg[Rx]`

And also the following macros for easier ==stack management==:
-   `ALLOCATE(k) : ADDC(SP, 4*k, SP)`
-   `DEALLOCATE(k) : SUBC(SP, 4*k, SP)`

They’re both used to _move_ `SP` to a reserved location for the start of the stack.

## Example of Stack Usage
### Allocating the Stack
Assuming the initial content of `SP` is `0`, then in order for `SP` to point to the address `0x010C` shown in the figure above, we can write:
```c
.include beta.uasm
ALLOCATE(67)
```
`0x10C` is 268 in decimal. Since macro `ALLOCATE` will ==multiply the input by `4` before storing it at SP==, we need to put `268/4=67` as the input to `ALLOCATE`.

This is done to ==tell the CPU that the stack starts at address `0x010C` onwards==, so that whatever content stored in the earlier addresses will not be overwritten by the stack.

Otherwise, the stack will start at address 0. Typically what is stored address `0` is the **first executable instruction** (i.e: the beginning of our program). We usually don’t want to overwrite any instructions.

### Adding Items to the Stack
Suppose we put the following values: `16, 17, 18` to `R1`, `R2`, and `R3` respectively:
```cpp
ADDC(R31, 16, R1)
ADDC(R31, 17, R2)
ADDC(R31, 18, R3)
```
We can put these values into the stack by doing
```cpp
PUSH(R1)
PUSH(R2)
PUSH(R3)
```
Upon execution of these series of instruction, the state of the stack is:
![](https://dropbox.com/s/h6ra945bysxu8tb/stack_3.png?raw=1)

Notice that the “top” of the stack is at the _bottom_, and that the stack grows _downwards_ by convention.

**Heads up:** familiarize yourself and get used to tracking the “_state_” of the stack, `PC`, and all registers in the REGFILE after executing each line of instruction.

Now suppose we use `R1`, `R2`, `R3` for other stuffs and _overwrite_ its values:
```cpp
MULC(R1, 2, R1)
MULC(R2, 3, R2)
MULC(R3, 4, R3)
```
The **new** state of the registers are now written in red. **The stack stays the same,** and so does `SP`.\

We can now say that **the stack contains the old value of the registers** `R1, R2, R3`, as shown:
![](https://dropbox.com/s/4v4l61monn1ktwy/stack_new.png?raw=1)

### Removing Items from the Stack
To remove items from the top of the stack, we can use `POP` instruction:
```cpp
POP(R3)
POP(R2)
POP(R1)
```
The state of the stack and the registers is therefore as shown. Notice how `POP` instructions can be used to _restore_ the registers state to before as in **Step 1**.
![](https://dropbox.com/s/u5r91wv4dbfmxv4/stack_popped.png?raw=1)

The remnants of data that was pushed to the stack actually stays in memory, but its rendered _irrelevant_ because it can be overwritten again by other instructions (hence space is seen as _freed_). In fact, there’s no such thing as **erasing** contents in the memory unit unless we explicitly write a bunch of zeroes to make it disappear. We simply always _overwrite_ them.

### Resetting the stack
Finally, we reset a stack by simply changing the value `SP`. For example, we can return the state of `SP` to `0` as it was before **Step 1**.
```cpp
DEALLOCATE(67)
```
Try out these instructions in `bsim`, and observe the state of the stack and registers after executing each instruction as practice.

## Implementing Procedure Linkage Contract Using Stack
Recall ![[#^d35458]]
1. ==Put arguments== on the stack
	1. Put them in reverse order: Last argument pushed first, first arguemnt pushed last
2. ==Branch== to the target function, leaving return address in `LP`
3. ==Remove arguments== on stack upon return
	1. Use `DEALLOCATE(N)` where `N` is the number of arguments
4. ==Obtain return value== from `R0` (if any)
	1. E.g. `ST(R0, location, Rx)`

Refer back to our factorial function again:
![[#^132fe8]]
The function `fact` is called twice, so we have ==two callers==.
We can ==hand assemble the first caller== following the **caller procedure** above.

### 1. Allocate memory space for caller variables and instructions
To allocate memory for variables, either
- Write them after all instructions
- Use `.` operator to lead them at desired memory location e.g. `0x01B0`
	- Define labels and its values
	- Redirect instruction back at address `0` using the `.` operator again

To allocate memory for instructions, use `ALLOCATE`. (make `SP` point to some unused memory location)
```cpp
.include beta.uasm 
. = 0x01B0 | load values at fixed location
result_1 : LONG(0)
result_2 : LONG(0)

. = 0x0000 | load instructions from address 0 onwards
ALLOCATE(50) 
```

### 2. Implement calling sequence
```cpp
|| Calling sequence
ADDC(R31, 4, R1) | put 4 to R1 

|| (1) put argument on the stack
PUSH(R1) 

|| (2) branch to the function, storing return address at LP 
BEQ(R31, fact, LP) 

|| (3) remove argument from stack after function returns
DEALLOCATE(1) 

|| (4) obtain return value at R0 
ST(R0, result_1, R31) 
HALT()
```
We assume that `fact` is a label that contains the ==address of the first instruction== of the factorial function.

### 3. Implement callee entry sequence and computation (body of function)
Recall that a callee must:
![[#^04788a]]
1. Perform promised **computation**
2. Leave result in `R0` if any
3. Leave state of all [[Sequential Logic|register]]s in [[Anatomy of the Beta CPU|REGFILE]] except `R0` **unchanged** upon returning to the caller
4. Leave *stack data* **unchanged** upon returning to the caller.

This is possible by implementing two parts: *callee entry sequence* and *callee exit/return sequence*.

The entry sequence is consisted of five steps:
1.  `PUSH(LP)` : to preserve the state of `LP` which contains the return address to the caller of this function.
2.  `PUSH(BP)`: to preserve the state of `Reg[R27]`
3.  `ADD(SP, R31, BP)`: move the content of `SP` to `BP`. This is to set the **stack frame base** for this function call. *We have macro for this:* `MOVE(SP, BP)`
4. Push all registers that we will use for the computation (except `R0`)
5. Load arguments from the stack

Afterwards, we then proceed with actually implementing the function.

Continuing our assembly code, writing the entry procedure is straightforward.
```cpp
|| Callee entry sequence
fact: PUSH(LP) | (1) 
PUSH(BP) | (2) 
MOVE(SP, BP) | (3) 
```
Now to figure out (4), we need to know the registers that we will use for computation of `fact`.
Recall the _implementation_ of the function `fact`:
```cpp
|| Assume (value of) n in R1 and (value of) r in R2 
check_while_fact: CMPLT(R31, R1, R0)
BNE(R0, while_true_fact, R31)
BEQ(R31, done, R31)	

while_true_fact: MUL(R1, R2, R2)	
SUBC(R1, 1, R1)	
BEQ(R31, check_while_fact, R31)	
```
We can see that the registers that are used for the computation (apart from `R0`) are : `R1` and `R2`
> `R31` is “not counted” as it is always `0` and you cannot rewrite new values into it.

Therefore the next instructions for the callee should be:
```cpp
|| (4) Push the contents of all registers we will use for the computations onto to stack to preserve its old value
PUSH(R1) 
PUSH(R2) 
```
Then, we load the argument `n` onto `R1`, and put `1` in `R2`. `R1` holds the value of `n` and `R2` holds the value of `r`.
```cpp
|| (5) get arguments. 
LD(BP, -12, R1) | Note: the first argument is at memory address BP-12
ADDC(R31, 1, R2) 
```
Afterwards, we can continue with the implementation of `fact` above as it is.

> Think carefully about why the first argument is always at address pointed by `Reg[BP]-12`. This is a direct result of caller procedure and callee entry sequence (1) to (3).

### 4. Implement callee exit sequence
The exit sequence is consisted of six steps:
1.  Put return value at `R0`.
2.  Restore all registers’ state that were used by the function computations using `POP`, in **reverse** order.
3.  `ADD(BP, R31, SP)`: move the content of `BP` to `SP`. This is to set the stack pointer back to the **stack frame base** for this function call.
4. `POP(BP)` : restore `Reg[BP]` to its original value
5. `POP(LP)` : restore `Reg[LP]` to its original value – remember, this register **contains the caller’s _return_ address.**
6. `JMP(LP, R31)`: return to the **caller**.

Let’s write them out in assembly, continuing our `fact` example above:
```cpp
|| (1) put return value r (originally in R2) at R0
done: ADD(R2, R31, R0) 

|| (2) restore register contents
POP(R2) 
POP(R1) 

MOVE(BP, SP) | (3) 
POP(BP) | (4)
POP(LP) | (5)
JMP(LP, 0, R31) | (6)
```
Now to call `fact` for the second time, we can simply write another calling sequence. **The `fact` instructions remain intact and reusable.**

### Combining everything
```cpp
.include beta.uasm 

||| Space allocation for variables and instructions (set start of stack)
. = 0x01B0 | load values at fixed location
result_1 : LONG(0)
result_2 : LONG(0)

. = 0x0000 | load instructions from address 0 onwards
ALLOCATE(50) 

||| First caller "calling sequence" -- fact(4)
ADDC(R31, 4, R1) | put 4 to R1 
PUSH(R1) | step (1) 
BEQ(R31, fact, LP) | step (2) 
DEALLOCATE(1) | step (3) 
ST(R0, result_1, R31) | step (4) 

||| Second caller "calling sequence" -- fact(9)
ADDC(R31, 9, R1) | put 9 to R1 
PUSH(R1) | step (1) 
BEQ(R31, fact, LP) | step (2) 
DEALLOCATE(1) | step (3) 
ST(R0, result_2, R31) | step (4) 
HALT()

||| Callee entry sequence
fact: PUSH(LP) | step (1) 
PUSH(BP) | step (2) 
MOVE(SP, BP) |  step (3) 

| step (4) 
PUSH(R1) | n
PUSH(R2) | r

LD(BP, -12, R1) | step (5) 
ADDC(R31, 1, R2)

||| Computation 
check_while_fact: CMPLT(R31, R1, R0)
BNE(R0, while_true_fact, R31)	
BEQ(R31, done, R31)

while_true_fact: MUL(R1, R2, R2)	
SUBC(R1, 1, R1)	
BEQ(R31, check_while_fact, R31)	

||| Callee exit (return) sequence
done: ADD(R2, R31, R0) | step (1)
POP(R2) | step (2) 
POP(R1) 

MOVE(BP, SP) | step (3) 
POP(BP) | step (4) 
POP(LP) | step (5) 
JMP(LP,R31) | step (6) 
```
Run the program in `bsim` **step by step**. At each instruction, pay attention on the state of all registers, the stack, and PC.

In this course, you are expected to mentally run each instruction line by line and give the state of all registers involved, the PC, and the stack at all times. Lots of practice is definitely needed.

At the end of the program, you should see that you have each answer in the memory address `0x01B0` and `0x01B4`:
![](https://dropbox.com/s/g7l4l0tkcyl08jj/mem_Res.png?raw=1)

## Example: Recursion
Recursive factorial in C:
```c
int fact(int n){
	if (n > 1){
		return n * fact(n-1);
	}
	return 1;
}

int result_1 = fact(3);
```
The recursive function `fact` can be hand assembled into:
```cpp
||| callee entry procedure
fact: PUSH(LP)
PUSH(BP)
MOVE(SP, BP)

| Preserve old register values before using them
PUSH(R1)	| n
PUSH(R2)	| temp reg
PUSH(R3)	| temp reg
PUSH(R4) 	| for constant

LD(BP, -12, R1) | get first argument
ADDC(R31, 1, R4) | put 1 to R4 as a constant 

||| Computation Part 1
begin_fact_check: CMPLT(R4, R1, R2) | compare if 1 < n, store in R2
BNE(R2, if_true, R31) 
|| leave 1 in R0
ADDC(R31, 1, R0) 

||| Callee exit sequence
exit_sequence: POP(R4) | Pop registers in reverse order, to restore each old register value
POP(R3)
POP(R2)
POP(R1) 

MOVE(BP, SP)
POP(BP)
POP(LP)
JMP(LP, R31)

||| Computation Part 2 
if_true: SUBC(R1, 1, R3) | compute n-1, store at R3

||| Recursive calling sequence
PUSH(R3) 
BEQ(R31, fact, LP) | recurse

|| remove unused argument from stack when recursion returns
DEALLOCATE(1) 

|| compute n * fact(n-1), store at R0 before returning
MUL(R0, R1, R0) 

BEQ(R31, exit_sequence, R31) | return
```
The calling sequence is simple:
```cpp
.include beta.uasm

ALLOCATE(100)

ADDC(R31, 3, R1)
PUSH(R1)
BEQ(R31, fact, LP) | call fact(3) 
DEALLOCATE(1) 
HALT()
```

You can add `.breakpoint` in the code to allow for debugging, and observe the stack frame for each function call.

In this example, calling `fact(3)` will cause `fact(2)`, and `fact(1)` to be called recursively.

The state of the stack frame _right_ before `fact(3)` branching, _right_ before `fact(2)` branching, _right_ before `fact(1)` branching, and _right_ before `fact(1)`calls its `exit_sequence` is as follows:
![](https://dropbox.com/s/mu8aq0id2y1pir5/stack_states.png?raw=1)
Notice several things:
-   The *stack size* for each callee frame is *constant*.
    -   In this example, it is 7 **words** (1 word is 32 bits).
    -   This is caused by 1 argument `PUSH`, two `PUSH` from callee entry sequence, and four `PUSH` of registers (to be used for computation).
-   The current `BP` and `SP` (rendered in black) points to the **base** and the **top** of the stack of the _current_ caller.
	- **Base** of the stack _is not the start_ _of the stack frame_. It is defined as the location of the first item pushed into the stack by that caller after `MOVE(SP, BP)` step.
- The **location of the argument for the current callee** is always 3 lines above the location pointed by the current `BP`.
    -   It is the address pointed by the _current_ `BP` subtracted by 12 (bytes).
-   The **return address** of the current caller is always placed _after_ the argument in the stack.
    -   This is the direct result of `PUSH(LP)` as the first instruction in the callee entry sequence.
    -   For example, the return address for the first `fact` call: `fact(3)` is at `0x0014` (just look at the lower 16 bits for simplicity).
    -   This is the address of instruction: `DEALLOCATE(1)` **(see next section to understand why this is so).**

Again, test your understanding and sharpen your skills by mentally running each instruction one by one from the top and be aware of the current instruction, stack state, PC state, and register states **at all times.**

## Instruction Loading Address
To figure out the address of each instruction, we can assume (if not given) that the address of the first instruction is at `0x0000`.
-   Recall that each $\beta$ instruction is 32 bits long (4 bytes).
-   Therefore, the address of subsequent instructions are always increased by 4.

For instance, if we simply load this instruction into the memory unit starting from address `0x0000`:
```cpp
.include beta.uasm

ALLOCATE(100)

ADDC(R31, 3, R1)
PUSH(R1)
BEQ(R31, fact, LP) | call fact(3) 
DEALLOCATE(1) 
HALT()

||| callee entry procedure
fact: PUSH(LP)
PUSH(BP)
MOVE(SP, BP)

...
```
It will obtain the following addresses:

![](https://dropbox.com/s/ae8mgejz3jgyavo/instr_eg.png?raw=1)
This screenshot is taken from `bsim` just before we branch to `fact` for the first time with argument `3`. That is why the `PC` is pointing to address `0x0010`.

Notice that as mentioned, the address of instruction `DEALLOCATE(1)` (macro for `SUBC(SP, 4, SP)`) is `0x0014`.

### Detail: about PC
We have learned before that `PC` register always contain the address of the _next_ instruction to be executed.

There’s one subtle point to realise: when the `PC` is ==currently pointing== to an address `A`, the instruction at `A` is ==actually already **computed** in the current cycle==, but the _result_ (of this computation) ==hasn’t been stored== _yet_. The result will only be stored (in some register or memory address) only in the next cycle.

Remember that ==memory write is synchronized with the clock==.

Take for example this particular execution state in the $\beta$ CPU:
![](https://dropbox.com/s/raqf5k421kfi2i7/pc_state.png?raw=1)
-   The current content of register `PC` is `0x004`, that is where instruction: `ADDC(R31, 3, R1)` resides.
-   The output of `ADDC` **has already been computed** in this cycle, as denoted in the blue value at the output port of the ALU: `0x00000003`.
    -   All values in blue are computed values (in this cycle) due to this current instruction `ADDC`.
-   However, notice `Reg[R1]` still contains `0` and not the new result `3` _yet_. In this cycle, we are trying to **write** `3` into `R1`.
-   Only at the next cycle,`Reg[R1]` finally stores the new value `3`. The figure below shows the state of the $\beta$ CPU at the following cycle:
![](https://dropbox.com/s/qzf1rxs5rshfzeo/pc_state_2.png?raw=1)

Therefore, what we _actually mean_ when we say that the `PC` always point to the `next` instruction executed is precisely that the **result** will only be synchronized in the **next** cycle (but computation is done in the current cycle).

## Example: Multiple arguments
Consider the following function with multiple arguments:
```c
int y(int m, int x, int c){
	return m*x + c;
}

int result = y(2, 5, 3);
```
In order to call this function, we need to push each argument in the _reverse_ order:
```cpp
.include beta.uasm 
. = 0x0CC
result: LONG(0)

. = 0x000
ADDC(R31, 2, R1) | first argument
ADDC(R31, 5, R2) | second argument
ADDC(R31, 3, R3) | third argument

|| Calling Sequence
|| Push arguments in the reverse order
PUSH(R3) 
PUSH(R2)
PUSH(R1) 

|| Branch to the function
BEQ(R31, y, LP)
|| Deallocate the arguments
DEALLOCATE(3)
|| Store return value
ST(R0, result, R31)
HALT()
```
Then in the function `y`, we obtain the arguments sequentially, starting from `BP-12` for the first argument, `BP-16` for the second argument, and so on:
```cpp
||| Callee entry sequence
y : PUSH(LP)
PUSH(BP)
MOVE(SP, BP)

| Preserve old register values before using them
PUSH(R1)
PUSH(R2)
PUSH(R3)

| Load arguments
LD(BP, -12, R1) | m
LD(BP, -16, R2) | x
LD(BP, -20, R3) | c

| Computation
MUL(R1, R2, R1) 
ADD(R1, R3, R0) | leave the answer at R0

||| Callee exit sequence
| Return all register values (POP in reverse order)
POP(R3)
POP(R2)
POP(R1)

MOVE(BP, SP)
POP(BP)
POP(LP)
JMP(LP, R31)
```

## Limitations
The sequences that we learned don’t really solve all problems.
### Problem 1: Nested procedure definitions
In Python, we can define nested procedure as follows:
```python
def f(x):
	def g(y):
		return x+y;
	return g
```
This requires `g` to access _non-local variable_ `x`. We would require some kind of “static-links” in stack frames.

C avoids this problem by outlawing nested procedure declarations.

### Problem 2: Dangling references
```c
int *p; /* a pointer */ 
int h(x) { 
	int y = x*3; 
	p = &y;  // set p to be pointing to address of y, a local variable
	return 37; 
	} 
h(10); 
print(*p);
```
The C-code above will compile, but when executed, unexpected behavior can happen.
- Crash (segmentation fault), random stuffs being printed, etc.

In C/C++, _life is harsh_ and it is the responsibility of the programmer to ensure that mistakes like these do not happen.

Java and Python will _babysit_ and protect us from these mistakes, as there’s language restriction that forbids constructs that could lead to dangling references (we are also given automatic storage management, and lots of things are taken care of – garbage collection, variables allocation, etc).

## Summary
You may want to watch the post lecture videos here:
-   [Part 1: Stack and Procedures](https://youtu.be/sj7A-lpTgaI)
-   [Part 2: Common Mistakes in Stack and Procedures](https://youtu.be/QGR9n9TqYc0)

The calling and callee sequence is designed such that we have a fixed convention for **linking procedures**. The data structure needed for procedure linkage is a **stack**, and it can simply be implemented using macroinstructions: `PUSH` and `POP` on some unused memory block, which address is stored in register `R29: SP`.

It is extremely important to change the content of `SP` (reserved stack pointer register) to reflect a memory address where there isn’t any important instruction or data in it.

==Remember that `PUSH` and `POP` each require **two clock cycles to complete**, because each of them is consisted of two atomic $\beta$ instructions.==

We also **reserve** two other registers: `R27: BP` and `R28: LP` for this purpose, so that we know where to get the function arguments from the stack, and return address (back to the caller).

We do not use these registers `R27, R28, and R29` for other purposes.

The callee has to leave _stack data_ **unchanged** upon returning to the caller, that is to clear whatever data that was put in the stack during its execution. As a result, we might find **dangling pointers:**
(e.g: pointer that points to an address that is no longer used.)
when we try to access a function’s local variable long after the function has returned.

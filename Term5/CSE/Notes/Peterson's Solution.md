---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Critical section solutions]]
[[Software Mutex Algorithm]]

## Peterson's Solution
> A **software-based** approach that solves the [[Critical section problem]], but with 2 restrictions:
> - **Strictly 2 processes that alternate** execution between their [[Critical section]]s and remainder sections (can be generallised to `N` processes with proper data structures, out of syllabus)
> - [[Designing an Instruction Set|Architectures]] where `LD` and `ST` are **atomic** (executed in 1 clk cycle, or not interruptable)

The solution works by utilising 2 [[Shared Memory|shared]] global variables:
```csharp
int turn;
bool flag[2]
```
- `turn == i`: process `Pi` allowed to enter the [[Critical section]]. Similar otherwise.
- `flag[i] == true`: process `Pi` ready to enter [[Critical section]].

An operation acting on [[Shared Memory]] is **atomic** if it completes in a ==single step relative to other threads==. For example, when an atomic store is performed on a shared variable, no other thread/process can observe the modification half-complete.

## Initialisation
`flag` : `false` for all `i`\
`turn`: some arbitrary number (`i` or `j` to index 2 processes `Pi` and `Pj`)

## Algorithm
```c
do{
   flag[i] = true;
   turn = j;
   while (flag[j] && turn == j); // this is a while LINE
   // CRITICAL SECTION HERE
   // ...
   flag[i] = false;
   // REMAINDER SECTION HERE
   // ...
}while(true)
```
Solution for process `Pi`
- in `while`: `Pi` busy waits (try and keep retrying until succeed, thus wasting the quanta given to the process)
- `Pi` stuck at while line as long as `flag[i] == true` **and** `turn == j`

## Proof of Correctness
To prove correct, show:
- **Mutual exclusion preserved**
- **Progress** requirement satisfied
- **Bounded-waiting** requirement satisfied

Trace how it works.
- When `Pi` wants to enter critical section, it will set its own flag `flag[i] = true`.
- Then it sets `turn = j` instead of itself.

> You can think of a process as being **polite** hence requesting the _other one_ (`j`) to be executed **first**.

Now 2 things may happen:
### Scenario 1: Proceed to CS
`Pi` may break from `while` loop under 2 conditions:
1. `flag[j] == false`: other `Pj` is **not ready to enter** CS and **also not in the critical section**. This ensures [[Mutex]].
2. `flag[j] == true` **but** `turn == i`: other process `Pj` is also **about** to enter the CS. But it is `Pi` turn, so `Pi` gets to enter CS first (ensuring **==progress==**)
### Scenario 2: Busy-wait
`Pi` stuck at `while`-line if `flag[j] == true` **and** `turn == j`, meaning `Pj` is inside CS.
- [[Mutex]]: `flag[i] == flag[j] == true`, but `turn` is an **integer** and cannot be both `i` and `j`
	- No 2 processes can simultaneously execute CS
- **Bounded-waiting guaranteed**: After `Pj` done, it sets its own flag `flag[j] = false`, ensuring `Pi` to *break* out of the `while`-line and enter CS in the future.
	- `Pi` only needs to wait a **maximum** of 1 cycle before being able to enter CS

 >You might want to **interleave** the execution of instructions between `Pi` and `Pj`, and convince yourself that this solution is indeed a legitimate solution to the CS problem. Try to also modify some parts: not to use `turn`, set `turn` for `Pi` as itself (`i`) instead of `j`, not to use `flag`, etc and convince yourself whether the 3 **correctness** property for the original Peterson’s algorithm still apply.
 
 
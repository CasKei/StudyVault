---
tags:50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Critical section problem]]
[[Critical section solutions]]

## Requirements for critical section solution
- **Mutual exclusion** (mutex) [[Mutex]]: no other process can execute the [[Critical section]] if there was already one [[Week 4 - Processes and Thread management|process]] executing it (in the case of conddition synchronisation, this is adjusted accordingly)
- **Progress**: if there is no process in the [[Critical section]], and some other processes wish to enter, we need to grant this permission and we cannot postpone this permission indefinitely
- **Bounded waiting**: if process A requested to enter CS, there exists a bound on the number of times other processes are allowed to enter before A. This implies CS also has finite length; cannot loop forever, will exit after a finite number of instructions.

## Properties
- **Safety**: no [[Race condition]]
- **Liveness**: a program with a proper [[Critical section solutions]] will not hang forever (because technically no progress IS [[Mutex|mutex]])

## Solution template
```c
while(true) {
	[ENTRY SECTION]
		CRITICAL SECTION ...
		...
	[EXIT SECTION]
		REMAINDER SECTION ...
		...
}
```
The protocol to approach a [[Critical section]] in general causes the process to
- **Request** permission to enter the section (entry)
- **Execute** critical section when request granted
- **Exit** the critical section solution

There may exist a remainder section (the rest of the program that is not part of the critical section)
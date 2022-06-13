---
aliases:
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Week 5 - Process Synchronisation]]
[[Producer Consumer problem]]

![[Producer Consumer problem#What happens if there is no synchronisation]]

> Assume `buffer` and `counter` are [[Shared Memory|shared]] between the two [[Week 4 - Processes and Thread management|processes]] / [[Week 4 - Processes and Thread management|threads]]. The instructions `counter ++` and `counter --` are **not** implemented in a single clock cycle (it is **not atomic**).

## Non-atomic ++ and --
`counter++` may be implemented as follows in assembly:
```armasm
LDR(counter, R2)
ADDC(R2, 1, R2) || or SUBC for counter--
ST(R2, counter)
```

## Race Condition Outcomes
### Outcome 1
Assume original value of `counter` is `4` and there is only 1 CPU.
**One interleaved execution between `counter++` and `counter--`:**
```armasm
LDR(counter, R2) | Producer executes, then interrupted, R2’s content:4
...IRQ on producer, save state, restore consumer
LDR(counter, R2) | Consumer executes, R2 contains 4
SUBC(R2, 1, R2)  | R2 contains 3, then consumer is interrupted
...IRQ on consumer, save state, restore producer
ADDC(R2, 1, R2)  | R2 contains 5 
ST(R2, counter)  | value 5 is stored at counter, then IRQ
...IRQ on producer, save state, restore consumer 
ST(R2, counter)  | value 3 is stored at counter
```

Therefore the final value of the `counter` is `3`.

### Outcome 2
Another combination of **interleaved execution:**
```armasm
LDR(counter, R2) | Producer executes, then interrupted R2’s content:4
...IRQ on producer, save state, restore consumer
LDR(counter, R2) | Consumer executes, R2 contains 4
SUBC(R2, 1, R2)  | R2 contains 3, then consumer is interrupted
ST(R2, counter)  | value 3 is stored at counter
...IRQ on consumer, save state, restore producer
ADDC(R2, 1, R2)  | R2 contains 5 
ST(R2, counter)  | value 5 is stored at counter
```

Therefore in the case above, the final value of the `counter` is `5`.

### Outcome 3
You may easily find that the value of the counter can be 4 as well through other combinations of interleaved execution of `counter ++` and `counter --`.

## Conclusion
Value of `counter` **depends on the order of execution** that is out of the user's control.
(depends on the [[Example of basic kernel scheduler|kernel's scheduling handler]], unknown to the user)

> In such a situation where **several processes** ==access and manipulate the same data [[Concurrent Programming|concurrent]]ly== and the ==outcome of the execution depends on the particular order in which the access takes place==, is called a **race condition**.

A race condition is **undesirable**. We need to perform [[Week 5 - Process Synchronisation|process synchronisation]] and coordination among cooperating processes (or equivalently, threads cooeration) to avoid the race condition.
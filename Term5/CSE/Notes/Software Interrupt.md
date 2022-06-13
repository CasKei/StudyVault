---
aliases: trap
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Trap]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]

![](https://natalieagus.github.io/50005/assets/images/week1/10.png)

## Software interrupt via [[System Calls]]  (Trap)
### Programs requiring inputs
Sometimes user processes are **blocked** from execution because it requires inputs from IO devices, and it may **not be scheduled** until the presence of the required input arrives. For example, this is what happens if you wait for user input in Python:

```python
inp = input("Enter your name:")
print(inp)
```

Running it will just cause your program to be stuck in the console, _why_:

```shell
$ python3 test.py 
Enter your name:
```

### How to trap
> Traps are **software generated interrupts**, that is some special instructions that will **transfer** the mode of the program to the [[Kernel mode and User mode|kernel mode]]

User processes may **trap** themselves e.g: by executing an **illegal** operation (`ILLOP`) implemented as a system call, along with some value in designated registers to **indicate** which system call this program tries to make.

-   The details on _which register_, or _what value should be put_ into these registers depends on the architecture of your CPU. **This detail is not part of our syllabus**.

The CPU is forced to go to a special handler that does a state save and then execute (may not be immediate!) on the proper interrupt service routine to handle the **request** (e.g: fetch user input in the python example above) in kernel mode. Software interrupts generally have **low priority**, as they are not as urgent as devices with limited buffering space.

![](https://natalieagus.github.io/50005/assets/images/week1/11.png)

During the time between system call request until [[System calls|system call]] return, the program execution is **paused**. Examples of system calls are: `chmod(), chdir(), print()`. More Linux system calls can be found at [http://man7.org/linux/man-pages/man2/syscalls.2.html](http://man7.org/linux/man-pages/man2/syscalls.2.html)

## Combining [[Hardware Interrupt]] and [[Software Interrupt|trap]]
[[Combining Hardware Interrupt and Trap]]

## More on system call
[[System calls]]
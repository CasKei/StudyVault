---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[System calls]]

## System call implementation
An [[System call via API|API]] helps users make appropriate system calls by providing convenient wrapper functions. More often than not, we don’t need to know its detailed implementation as the API already provides convenient **abstraction**.

For most programming languages, the **run-time support system** (a set of functions built into libraries included with a compiler) provides a system call **interface** that serves as the link to system calls made available by the [[Operating System]]. The system-call **interface** intercepts function calls in the API and invokes the necessary system calls within the operating system.

## System Call Number
Typically, a **number** is associated with each [[System calls|system call]], and the system-call interface maintains a table indexed according to these numbers. For example, Linux system call tables and its associated numbers can be found [here](https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_64.tbl) and FreeBSD Kernel System call table can be found [here](https://opensource.apple.com/source/xnu/xnu-1504.3.12/bsd/kern/syscalls.master).

To further understand the points above, let’s see a sample assembly file to print `Hello World` to console.

#### Hello World in Assembly (Linux, x86-64)
```nasm
; hello_world.s
global _start

section .text

_start:
  mov rax, 1        ; system call number for write
  mov rdi, 1        ;    making file handle stdout
  mov rsi, msg      ;   passing adress of string to output
  mov rdx, msglen   ;   number of bytes
  syscall           ; invoking os to write

  mov rax, 60       ; sys call number for exit
  mov rdi, 0        ;   exit code 0 EXIT_SUCCESS
  syscall           ; invoke os to exit

section .rodata
  msg: db "Hello, world!", 10
  msglen: equ $ - msg
```

Compilation and execution:

```
nasm -f elf64 -o hello_world.o hello_world.s
ld -o hello_world hello_world.
./hello_world
```

#### Hello World in Assembly (macOS X, x86-64)

```nasm
; hello_world.s
global _main
section .text
_main:
  mov rax, 0x2000004 ; system call number for write
  mov rdi, 1 ; file descriptor 1 is stdout
  mov rsi, msg ; get string address
  mov rdx, msg.len ; number of bytes
  syscall ; exec syscall write
  mov rax, 0x2000001 ; syscall number for exit
  mov rdi, 0 ; exit code 0
  syscall ; exit program
section .data
msg:    db      "Hello, world!", 10
.len:   equ     $ - msg
```

Compilation and execution:

```
nasm -f macho64 hello_world.s
ld -lSystem -o hello_world hello_world.o
./hello_world
```

#### Hello World in Assembly (macOS X, M1)

```cs
// hello_world.s
.global _start             // Provide program starting address to linker
.align 2

// Setup the parameters to print hello world
// and then call Linux to do it.
_start: mov X0, #1     // 1 = StdOut
        adr X1, helloworld // string to print
        mov X2, #13     // length of our string
        mov X16, #4     // MacOS write system call
        svc 0     // Call linux to output the string

// Setup the parameters to exit the program
// and then call Linux to do it.

        mov     X0, #0      // Use 0 return code
        mov     X16, #1     // Service command code 1 terminates this program
        svc     0           // Call MacOS to terminate the program

helloworld:      .ascii  "hello, world!\n"
```

Compilation and execution:

```
as -g -o hello_world.o hello_world.s
ld -macosx_version_min 12.0.0 -o hello_world hello_world.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _start -arch arm64 
./hello_world
```

From the three examples above, it is obvious that system call numbers are **hardware dependent**. Note that the **registers used** are also machine specific. In x86-64 architecture, `rax` stands for the register to pass the system call id, `rdi` stands the register that should contain file descriptor (1 for `stdout` in your terminal), etc. In M1 architecture, the equivalent to `rax` is `X16`, and `rdi` is `X0`.

#### Hello World in C

In contrast, here’s an implementation in C, short and sweet.

```c
// hello_world.c
#include <stdio.h>
int main() {
   // printf() displays the string inside quotation
   printf("Hello, World!");
   return 0;
}
```

Compilation and execution:

```
gcc -o hello_world hello_world.c
./hello_world
```

Here’s the implementation in Python. Even shorter and sweeter:

```python
# hello_world.py
print('Hello, world!')
```

Execution: `python hello_world.py`

As you can see, the C program can be compiled for either OS, and so is the python program. The C system call **interface** then invokes the intended system call in the operating-system kernel by **[[Software Interrupt|trapping]]** itself and invoking the trap handler (runs in kernel mode from now onwards):

1.  The trap handler first **saves** the states of the process[6](https://natalieagus.github.io/50005/os_notes/week2_syscall#fn:8) and examines the system call index left in a certain register.
2.  It then refers to the standard system call table and **dispatches** the system service request accordingly, i.e: **branches** onto the address in the Kernel space that implements the system call service routine of the system call with that index and executes it.

When the system call service routine **returns** to the trap handler, the program execution can be **resumed**. If the system call does not return yet (e.g: block system call like `input()`), then the scheduler may be called to schedule another process, while this process is put to wait until the requested service is available.

The relationship between application program, API, System call interface, and the kernel is shown below (_image screenshot from SGG book)_:

![](https://natalieagus.github.io/50005/assets/images/week2/5.png)

Notice that `printf` is just a C function that will eventually calls the `write` C function, and will eventually invoke the `write` systemcall. We can also do the same thing by using `write` C function:

```c
// hello_world.c
#include <unistd.h>
int main()
{
    // write(fd, char*, #bytes)
    write(1, "hello, world!\n", 14);
    return 0;
}
```

For obvious reasons, `printf` is more convenient because we don’t have to care about arguments like “1” (file descriptor for stout) and “14” (bytes in the printed string) and having to read the manual page for your hardware to find out what these mean inside `write`.

`write` is actually a convenient and more human-friendly **wrapper** around the another C function: `syscall`. It utilises the symbol `SYS_write` to indicate the system call number which value varies depending on the OS.

```c
#include <unistd.h>
#include <sys/syscall.h>

int main()
{
    // write(fd, char*, #bytes)
    syscall(SYS_write, 1, "hello, world!\n", 14);
    return 0;
}
```

Many wrappers in APIs are named after the system call itself, just like `write` or `syscall` that’s meant to invoke the actual WRITE system call and invoke the `syscall` routine. In summary, making system calls **directly** in the application code is possible, but more complicated and may require embedded assembly code to be used (in C and C++) as well as knowledge of the low-level binary interface for the system call operation, which may be subject to **change** over time and thus not be part of the application binary interface; **the API is meant to abstract this away**.

You can find out more about Linux[7](https://natalieagus.github.io/50005/os_notes/week2_syscall#fn:6) system calls **API** (implemented in C) [here](http://man7.org/linux/man-pages/man2/syscalls.2.html)

## Parameter Passing
![[Pasted image 20220530121303.png]]
System call service **routines** are just like common functions, implemented in the kernel space. **We will do a little exercise with BSim soon to understand better.** They require **parameters** to run. For example, if we request a `write`, one of the most obvious parameters required are the bytes to write.

There are three general ways to pass the parameters required for system calls to the OS Kernel.

#### Registers

Pass parameters in **registers**:

-   For the example of `write` system call, Kernel examines certain special registers for bytes to print
-   Pros: Simple and **fast** access
-   Cons: There might be **more** parameters than registers

#### Stack

Push parameters to the program **stack**:

-   Pushed to the stack by process running in user mode, then invoke `syscall`
-   In kernel mode, **pops** the arguments from the calling program’s stack

#### Block or Table

Pass parameters that are stored in a persistent contiguous location (**table** or **block**) in the RAM (this is a **different** location from stack!) and pass the **pointer** (address) through registers, to be read by the system call routine:

-   As illustrated below, `x` represents the **address** of the parameters for the system call.
-   When system call `id` (e.g: `write`) is made, the kernel examines certain registers, in this example is `rsi` to obtain the address to the parameter (the bytes to write to `stdout`)
-   Given the **pointer**, Kernel can find the parameter for the system call in the RAM, as illustrated below:

![](https://natalieagus.github.io/50005/assets/images/week2/6.png)
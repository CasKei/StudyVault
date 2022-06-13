---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[System calls]]

## System calls via API
One of the most common ways to make system calls is through an **API** (Application Programming Interface). We can write a program in a particular language and conveniently perform several system calls through the provided APIs supported by the chosen language as needed.

> API is an **interface** that provides a way to interact with the underlying library that makes the system calls, often **named the same** as the system calls they invoke.

An API specifies:

-   a set of functions that are available to an application programmer
-   the parameters that are passed to each function and
-   the return values the programmer can expect

3 most common APIs available:

1.  Win32 API for Windows systems written in C++
2.  POSIX API for POSIX-based system (all versions of UNIX); mostly written in C. You can find the functions supported by the API here [https://pubs.opengroup.org/onlinepubs/9699919799/](https://pubs.opengroup.org/onlinepubs/9699919799/)
3.  Java API for programs running on Java Virtual Machine (JVM)

Behind the scenes, the **functions** that make up an API invoke the **actual** system calls on behalf of the application programmer.

Benefits of using an API to make system calls:

-   It adds another layer of **abstraction** hence simplifies the process of application development
-   Supports program **portability**

## Examples
### printf()
We always conveniently call `printf()` whenever we want to display our output to the console in C. `printf` itself is a POSIX system call **API**.

-   This function requires kernel service as it involves access to hardware: output display.
-   The function `printf` is actually making several other function calls to prepare the resources or requirements for this system call **and** finally make the actual system call that invokes the kernel’s help to display the output to the display.

![](https://natalieagus.github.io/50005/assets/images/week2/3.png)

The full implementation of `printf` in Mach OS can be found [here](https://opensource.apple.com/source/xnu/xnu-201/osfmk/kern/printf.c.auto.html). It calls other functions like `putc` and eventually `write` function that makes the system call to `stdout` file descriptor.

### CopyFile()
We also always conveniently copy one file into another location (be it programmatically or through the GUI). In Windows OS, this is supported by the `CopyFile` function (Win32 API):

```C
CopyFile(szFilePath.c_str(), szCopyPath.c_str(), FALSE );
```

The complete documentation can be found [here](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-copyfile). The instruction sequence that is made by this `CopyFile` function to complete the entire copy operation is actually pretty lengthy, involving **multiple** system calls. In `CopyFile` case alone, multiple system calls are made for writing to file, opening files, obtaining file name, reading from file, termination, etc (image below taken from SGG book)

![](https://natalieagus.github.io/50005/assets/images/week2/4.png)

The actual implementation details (source code) of OS functions like `CopyFile` are intentionally not documented and can be changed at any time. The API however is well documented and conformed to so others who rely on it will not have their programs broken due to internal OS updates.
---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W4]]

## What is Exception
Runtime/execution error occurs when a program is running and there is an operation that cannot be carried out
e.g. divide by 0

> Exception: an object that represents such execution error

The program throws an exception when such execution error occurs

Handle the exception or the program terminates abnormally

## Exception Handling
> When there is an exception, either the method handles it itself, or let the caller handle it

- Some code: `throw new Exception();`
- In the `try` block: code that is executed under normal circumstance
- In the `catch` block: code that is executed during the exception
- Then, the statement after the catch block is executed

![[Pasted image 20220212114633.png]]
![[Pasted image 20220212114711.png]]

## Exception Types
Exceptions are objects
Root class for exception is `Throwable`
Error: system error, not much you can handle;e.g. VirtualMachineError occurs when systemruns out of resource
![[Pasted image 20220212114800.png]]

`IOException`: opening a nonexisting file etc
`RuntimeException`: programming errors such as out-of-bounds array, numeric errors, etc
`ArithmticExpression`: div by 0
`IndexOutOfBoundsException`: index out of range

## Checked and Unchecked Exception
- `RuntimeException`, `Error` and their subclasses are unchecked exception

All others are checked exception

> Checked exception: compiler forces the programmer to explicitly check and handle them in a try-catch block, or declare in the method header to let caller handle (use `throw`s)

> Unchecked exception: e.g. `ArithmeticException` can occur anywhere in the program

## The finally clause
The `finally` clause is always executed regardless if an exception occurs or not, and if the exception is caught or not

Use case: file closing, cleanup
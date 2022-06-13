---
aliases:JX OS, JX
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]

## JX OS
The **JX OS** is written almost entirely in **Java**. Such a system, known as a **language-based extensible** system, and runs in a single address space (no [[Virtualisation]], no [[Pagetable|MMU]]), as such it will face difficulties in maintaining memory protection that is usually supported by hardwares in typical OS.

![](https://natalieagus.github.io/50005/assets/images/week2/14.png)

[[Week 1 - Static Typing]]

Language-based systems instead rely on **type-safety** features of the language. As a result, language-based systems are desirable on small hardware devices, which may lack hardware features that provide **memory protection**. Since Java is a type-safe language, JX is able to provide **isolation** between running Java applications without hardware memory protection.

This is called ==language based protection==, where [[System calls]] and IPC in JX does not require an address-space switch. In short, ==JX runs in a single address space==.

The architecture of the JX system is illustrated below (simplified representation[5](https://natalieagus.github.io/50005/os_notes/week2_designstructure#fn:15)):

-   JX organizes its system according to **domains**. ![](https://natalieagus.github.io/50005/assets/images/week2/15.png)
    
-   Each **domain** represents an independent **JVM** (Java Virtual Machine):
    -   JVM is an abstract virtual machine that can run on **any** OS
    -   There’s one instance of JVM per Java application
    -   JVM provides portable execution environment for Java-based apps
    -   It maintains a heap used for allocating memory during object creation and threads within itself, as well as for **garbage collection**. ![](https://natalieagus.github.io/50005/assets/images/week2/16.png)
-   ==Domain zero== is a [[Microkernel system structure|microkernel]] responsible for low-level details, such as system initialization and saving and restoring the state of the CPU.
    -   Domain zero is written in C and assembly language; all other domains are written entirely in Java.
    -   Communication between domains occurs through a specific mechanism called **portals**
-   Protection within and between domains relies on the type safety of the Java language.
    -   However, since domain zero is not written in Java, it **must be considered trusted** (built by trusted sources)
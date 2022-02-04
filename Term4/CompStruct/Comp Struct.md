---
aliases: computation structures, comp struct, 50.002
tags: #50.002
---
[Course Handout](https://docs.google.com/document/d/1Ye80CY1Ppvgr6_85lexZsFCkg7rU6UNwYrnt08IYAZo/edit#)
[Website](https://natalieagus.github.io/50002/)
# Contents
[[Basics of Information]]
[[Digital Abstraction]]
[[CMOS Technology]]
[[Logic Synthesis]]
[[Sequential Logic]]
[[Finite State Machine]]
[[Turing Machine and Programmability]]
[[Designing an Instruction Set]]
[[Building Beta CPU]]
[[Assemblers and Compilers]]
[[Stack and Procedures]]
[[Memory Hierarchy]]
[[Cache Design Issues]]
[[Virtual Memory]]
[[Virtual Machine]]
[[Asynchronous Handling of IO Devices]]
## FPGA
[[FPGA1 - Combinational Logic]]
[[FPGA2 - Sequential Logic and FSM]]
[[FPGA3 - Reset and I/O]]
[[FPGA4 - Building Beta CPU]]
[[Creating a Programmable Machine]]
## Textbook

[[The Digital Abstraction]]
[[Binary Representations and Notation]]
[[Combinatorial Devices and Circuits]]
[[Sequences and State]]
[[Synthesis of Digital Systems]]
[[Finite-State Machines]]
[[Control Structures and Disciplines]]
[[Performance Measures and Trade-Offs]]
[[Communication: Issues and Structures]]
[[Interpretation]]
[[Microinterpreter Architecture]]
[[Microprogramming and Microcode]]
[[Single-Sequence Machines]]
[[Stack Architectures: The S Machine]]
[[Register Architectures: The G Machine]]
[[Memory Architectures]]
[[Reduced-Instruction-Set Computers]]
[[Processes and Processor Multiplexing]]
[[Process Synchronisation]]
[[Interrupts, Priorities, and Real Time]]
[[Architectural Horizons]]
[[The C Language: A Brief Overview]]
[[MAYBE Microarchitecture Summary]]
[[MAYBE Microcode Support for Interpreters]]
[[S Machine Summary]]
[[G Machine Summary]]

## Extra
[[Structured Computer Organisation: Levels, Machines]]
[[Milestones in Computer Architecture]]
[[The Computer Zoo]]
[[Example Computer Families]]
[[Processors]]
[[Primary Memory]]
[[Secondary Memory]]
[[Input/Output]]
[[Gates and Boolean Algebra]]
[[Basic Digital Logic Circuits]]
[[Memory]]
[[CPU chips and buses]]
[[Example CPU chips]]
[[Example Buses]]
[[Interfacing]]
[[An Example Microarchitecture]]
[[An Example ISA: IJVM]]
[[An Example Implementation]]
[[Design of the Microarchitecture Level]]
[[Improving Performance]]
[[Examples of the Microarchitecture Level]]
[[Comparison of the I7, OMAP4430, and ATMEGA168]]
[[Overview of the ISA Level]]
[[Data Types]]
[[Instruction Formats]]
[[Addressing]]
[[Instruction Types]]
[[Flow of control]]
[[A detailed example: the towers of hanoi]]
[[The IA-64 Architecture and the Itanium 2]]
[[Virtual Memory]]
[[Hardware Virtualisation]]
[[OSM-Level I/O instructions]]
[[OSM-Level Instructions for parallel processing]]
[[Example Operating Systems]]
[[Introduction to Assembly Language]]
[[Macros]]
[[The Assembly Process]]
[[Linking and Loading]]
[[On-chip Paralellism]]
[[Coprocessors]]
[[Shared-Memory Multiprocessors]]
[[Message-Passing Multicomputers]]
[[Grid computing]]

## Problem Sets/ Tutorial/ Practice
[[Problem Set 1]]

## Lab
[[Lab 1 - CMOS]]

#### Course Description

This course introduces architecture of digital systems, emphasising structural principles common to a wide range of technologies. Topics include Multilevel implementation strategies; definition of new primitives (e.g., gates, instructions, procedures, and processes) and their mechanisation using lower-level elements. Analysis of potential concurrency; precedence constraints and performance measures; pipelined and multidimensional systems; instruction set design issues; architectural support for contemporary software structures.

#### Prerequisites

-   [10.009 The Digital World](https://smt.sutd.edu.sg/education/undergraduate/courses/10009-digital-world) (For AY2019) or [10.014 Computational Thinking for Design](https://sutd.edu.sg/Admissions/Undergraduate/Unique-Curriculum/Freshmore-Subjects/Computational-Thinking-for-Design) (For AY2020 and subsequent batches)

#### Learning Objectives

1.  State the role of abstraction in the design of large digital systems, and explain the major software and hardware abstractions in contemporary computer systems.
2.  Design simple hardware systems based on a variety of digital abstractions such as ROMs, logic arrays and state machines.
3.  Synthesize digital systems from a library of representative components and test the designs under simulation.
4.  Describe the operation of a moderately complex digital system — a simple RISC-based computer — down to the gate level, and be able to specify, implement and debug its components.
5.  Appreciate the technical skills necessary to be a capable digital systems engineer.
6.  Explain the fundamentals of modern operating systems.

#### Measurable Outcomes

1.  Identify flaws and limitations in simple systems implemented using the static discipline.
2.  Identify flaws and limitations in simple systems implemented using clocked registers with asynchronous inputs.
3.  Identify flaws and limitations in simple systems implemented using semaphores for process synchronization.
4.  Characterize the logic function of combinational devices using CMOS, ROM or PLA technologies.
5.  Explain synthesis issues for combinational devices using CMOS, ROM or PLA technologies from their functional specification.
6.  Explain synthsis of acyclic circuits from combinational components.
7.  Calculate performance characteristics of acyclic circuits with combinational components.
8.  Explain and calculate performance characteristics of single-clock sequential circuits.
9.  Implement a simple RISC-based CPU architecture.
10.  Explain the underlaying theory of memory hierarchy.
11.  Implement a device handler using interrupt and SVC.
12.  Implement a synchronization system for processes using semaphore.

#### Topics Covered

-   Course overview and mechanics, Basics of Information
-   The Digital Abstraction, CMOS Technology
-   Basic Hardware Lab (Combine with EPD)
-   Logic Synthesis
-   Logic Simplification, Multiplexer, ROM
-   SW Lab1 (CMOS)
-   Sequential Logic
-   Finite State Machines and Synchronization
-   SW Lab 2 (Adder)
-   Computers and Programs
-   The Assembly Language
-   SW Lab 3 (ALU)
-   The C language, Stacks and Procedures
-   Stacks and Procedures (II)
-   Building the Beta
-   Building the Beta (II)
-   SW Lab 5 (Assembly Language)
-   Memory Hierarchy
-   Cache Issues
-   SW Lab 6 (Beta)
-   Virtual Memory
-   Virtual Machines
-   SW Lab 6 (Beta)
-   Device Handlers and Bus
-   Processes, Synchronization, and Deadlock, OS summary
-   SW Lab 8 (Tiny OS)

#### Textbook(s) and/or Other Required Material

-   Stephen A. Ward, Robert H. Halstead, _Computation Structures_ (The MIT Electrical Engineering and Computer Science Series). Cambridge, MA: MIT Press. 1999.

---
aliases:
tags: #50.002
---
[[Comp Struct]]
[[Assemblers and Compilers]]

>Abstraction is a fundamental concept in software engineering and computer science. It refers to process of removing physical, spatial, or temporal details to allow us to focus our attention on matters of **greater importance.**

We can engineer various softwares to provide abstraction in a computer system. A central form of abstraction in computing is the ==language abstraction==.

> Language abstraction: generational development of programming languages from the _machine language_ to the _assembly language_ and the _high-level language._ Each stage can be used as a stepping stone for the next stage.
>
> We can also create new abstraction within a programming language, such as subroutines, modules, software components, polymorphism, and so on.

There are several **layers** to software abstraction, summarised below:

-   ==_Basic Layer_: compilation tool softwares such as _assemblers_, _interpreters_ and _compilers_:==
    -   **[[Assembler]] and [[Interpreter and Compiler|Interpreter]]**: hides bit-level representations, hex locations, and binary values
    -   **[[Interpreter and Compiler|Compiler]]:** hides machine instructions, registers, machine architecture. Convert a prog from high-end language into assembly.
-   ==_Higher Layers_: interpretive tool softwares such as Operating System and Applications (web browser, video player, text editors, etc):==
    -   **Operating System:** hides resources (memory, CPU, I/O devices) limitations and details.
    -   **Applications:** hides local parameters, network location, security details, etc.
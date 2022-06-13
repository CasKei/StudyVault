---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]
[[OS structures]]

## Layered OS structure
The [[Operating System]] is broken into a many number of **layers** (levels). The bottom layer (layer 0) is the hardware; the highest (layer N) is the user interface. The figure below shows a layered approach (layer names for illustration purposes). The programs in layer $N$ rely on services ONLY from the layer below it.

![](https://natalieagus.github.io/50005/assets/images/week2/10.png)

## Pros
-   **Simple** to construct and debug
-   Each **layer** is implemented only with operations provided by lower-level layers.
-   A layer **does not need to know** how these operations are implemented; it needs to know only what these operations do.
-   This **abstracts** and hides the existence of certain data structures, operations, and hardware from higher-level layers.

## Cons
-   **Appropriately** defining the various layers, and careful planning is necessary.
    -   If we are met with **bugs** in our program, we debug our program and not our compiler
    -   **We mostly assume that the layers beneath us are already made correct**
    -   Sometimes, this assumption is not always true and difficult to maintain with the growing size of the OS. Some OS is shipped with bugs on its lower layers that are very difficult for users to debug.
    -   Patches and updates are periodically given to fix these bugs.
-   They tend to be **less efficient** than other types.
    -   For instance, when a process running in user mode executes an I/O operation, it executes a system call that is trapped to the I/O layer, which calls the memory-management layer, which in turn calls the CPU-scheduling layer, which is then passed to the hardware.
    -   At each layer, the parameters may be modified, data may need to be passed, and so on.
    -   Each layer adds overhead to the [[System calls|system call]].
    -   The net result is a system call that takes longer than does one on a non layered system.

Example: Windows NT (the later version is actually a **hybrid** OS, combining between layered and monolithic aspects and benefits)[3](https://natalieagus.github.io/50005/os_notes/week2_designstructure#fn:13)

![](https://natalieagus.github.io/50005/assets/images/week2/11.png)
---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
[[Graph Directory Structure]]

The primary advantage of an acyclic graph is the relative simplicity of the algorithms to **traverse** the graph and to determine when there are no more references to a file. We want to avoid traversing shared sections of an acyclic graph twice, mainly for performance reasons.

![](https://natalieagus.github.io/50005/assets/images/week6/23.png)

If cycles are allowed to exist in the directory (red arrow above – can be either soft/symbolic link or hard link), we likewise want to _avoid_ searching any component twice, for reasons of correctness as well as performance.

A poorly designed algorithm might result in an infinite loop continually searching through the cycle and never terminating. One solution is to limit the number of directories traversed when searching.

### Self referencing

In a cyclic directory, using **reference count** to determine whether we need to delete a node might not work due to self referencing. You’d need other garbage-collection protocols.

For example, suppose we delete the reference edge as shown below.

-   This delete action will **reduce** the reference count of all the children of that edge (whatever node – file – that is pointed to by the edge).
-   However due to **self referencing nodes**, the directory containing {`User1`, `Guest`} has their reference count set to `2` (for simplicity, we ignore reference count due to “.” and “..”).
    -   Note that symbolic links **do not** increase reference count
-   As a result, the delete action **does not reduce** the reference count of this directory to _zero_.
-   We are left with three inaccessible directories as shown in the image below.

![](https://natalieagus.github.io/50005/assets/images/week6/24.png)

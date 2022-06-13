---
aliases: policy and mechanism separation
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 2, 3 - OS Structure]]

## OS Design and Implementation
>There’s no known ultimate solution when it comes to OS design. Internal structures of known operating systems can vary widely.

When one design an OS, it might be helpful to consider a few known things.

## User and System Goals
Start by defining **goals**:

| User goals                                                          | System goals                                                                                                                  |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| OS should be convenient to use, easy to learn, reliable, safe, fast | The system should be easy to design, implement, and maintain; and it should be flexible, reliable, error free, and efficient. |

## Policy and Mechanism Separation
Know the **difference** between **policy** and **mechanism** and separate them:

| Policy                       | Mechanism                      |
| ---------------------------- | ------------------------------ |
| Determines what will be done | Determines how to do something | 

The separation of policy and mechanism is important for **flexibility**:

-   ==Policies== are likely to **change** across **places** or over **time**.
-   In the worst case, each change in ==policy== would require a change in the underlying ==mechanism==.

A general ==mechanism== insensitive to changes in policy would be more desirable. A change in policy would then require redefinition of only certain **parameters** of the system.

Take for example: a **mechanism** for giving **priority** to certain types of programs over others. If the **mechanism** is properly **separated** from policy, it can be easily tweaked based on user requirements:

-   **Support** a policy decision that I/O-intensive programs should have priority over CPU-intensive ones
-   Or **support** the opposite policy whenever appropriate. Either way, no change in the instructions need to be made.


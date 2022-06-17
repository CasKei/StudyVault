---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

# Deadlock Recovery
To recover from [[Deadlock]], we can either:

1.  Abort **all** deadlocked processes, the resources held are preempted
2.  Abort deadlocked processes **one at a time**, until deadlock no longer occurs

The second method results in **overhead** since we need to run the detection algorithm over and over again each time we abort a process. There are a few design choices:

-   Which **order** shall we abort the processes in?
-   Which “victim” shall we select? We need to determine **cost** factors such as which processes have executed the longest, etc
-   If we select a “victim”, how much **rollback** should we do to the process?
-   How do we ensure that **starvation** does not occur?

Deadlock Recovery remains an open ended issue. Dealing with deadlock is also a difficult problem. Most operating systems do not prevent or resolve deadlock completely and users will deal with it when the need arises.
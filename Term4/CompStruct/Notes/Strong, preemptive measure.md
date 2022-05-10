---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Scheduling multiple interrupts]]

Allow interrupt handlers with lower priority to be interrupted only by handlers with higher priority level.

[[Handler Priority Level]]

Handlers of the same priority level cannot interrupt each other.
If [[Anatomy of the Beta CPU|CPU]] runs a handler of lower priority, it will be forced to perform a [[Context switch]] to run the handler with the higher priority (required to service the interrupt).

The interrupted handler can be resumed later after the interrupting higher has finishde execution.

We call this type of [[OS Kernel]] that permits [[Context switch]] even when [[Anatomy of the Beta CPU|CPU]] is running in [[Kernel mode and User mode|kernel mode]] as **preemptive kernel** (but not [[Re-entrancy|re-entrant]]) - and it requires complex development as opposed to non-preemptive ones.

A _reentrant_ kernel is made such that it allows multiple processes (running in different cores) to be executing in the kernel mode _at any given point of time_ without causing any consistency problems among the kernel data structures.
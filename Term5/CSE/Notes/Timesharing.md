---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Week 4 - Processes and Thread management]]
[[OS Kernel]]

## Timesharing
[[Multiprogramming]] allows for **timesharing**.

Users can interact with each program when it is running.

> [[Context switch]] that's performed so rapidly that users still see the system as interactive and seemingly capable to run multiple processes despite having limited number of CPUs.

Timesharing is the **logical extension of [[Multiprogramming]]**. It results in an **interactive** computer system, which provides **direct** communication between the user and the system.

## Timesharing support
Requires **interactivity**, done by performing rapid [[Context switch]]ing between executing of multiple [[Process vs Program|program]]s in the computer system.

When an [[Interrupt timeline|interrupt]] occurs, the [[OS Kernel]] needs to save the current [[Complete Process Context|context]] of the process running on the CPU so that it can restore that context when the processing is done, essentially **suspending** the process and then resuming it at the later time.

> The suspended [[Complete Process Context|process context]] is stored in the [[Process table and Process control block|PCB]] of that process.

## Context Switch
[[Context switch]]
Context switch is the routine of **saving** the state of a process, so that it can be **restored** and **resumed** at a later point in time. For more details on what this `state` comprised of, see Week 2 notes.
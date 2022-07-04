---
aliases: deadlock detection algorithm
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## Overview
In deadlock detection, we **allow** [[Deadlock]] to happen first (we don’t deny its possibility), and then detect it later.

It is different from [[Deadlock avoidance]]. The latter is one step ahead since will not grant requests that may lead to deadlocks in the first place.

Deadlock detection mechanism works by providing two things:
-   An algorithm that **examines** the state of the system to determine whether a deadlock **has occurred**
-   An algorithm to **recover**([[Deadlock recovery]]) from deadlock condition

## Deadlock Detection Algorithm

This algorithm works similarly Part 2 of the [[Banker's Algorithm]] (the [[Safety Algorithm]]), just that this algorithm is performed on the _actual_ system state (not the hypothetical `work`, `need` and `allocation`!)

Firstly, we need all the state information as in [[Banker's Algorithm]]: the `available`, `request`(renamed from `need`), and `allocation` matrices (no max/need). The only subtle difference is only that the `need` matrix (in safety algorithm) is replaced by the `request` matrix.

In a system that adapt deadlock **detection** as a solution to the deadlock problem, we don’t have to know the `max`(resource needed by a process), because we will _always_ grant a request whenever whatever’s requested is **available**, and invoke deadlock detection algorithm from time to time to ensure that the system is a good state and not deadlocked.

The `request` matrix contains current requests of resources made by **all** processes at the instance we decide to **detect** whether or not there’s (already) a deadlock occuring in the system.

-   Row `i` in the `request` matrix stands for: Process `i` requiring some **MORE** resources that’s what’s been allocated for it.

The deadlock detection algorithm goes as follows:

-   **Step 1**: Initialize these two vectors:
    -   `work` (length is number of resources `M`) initialized to be == `available`
    -   `finish` (length is number of processes `N`) initialized to be:
        -   `False` if `request[i]` != {0} (empty set)
        -   True `otherwise` (means process i doesn’t request for anything else anymore and can be resolved or finished)
    -   No update of `allocation, need` needed. We are checking whether the CURRENT state is safe, not whether a HYPOTHETICAL state is safe.
-   **Step 2**: find an index `i` such that **both** conditions below are fulfilled,
    -   `Finish[i] == False`
    -   `request[i] <= work` (elemet-wise comparison for these vectors)
-   **Step 3**:
    -   If Step 2 produces such index `i`, update `work` and `finish[i]`,
        -   `work += allocation[i]` (vector addition)
        -   `finish[i] = True`
        -   **Go back to Step 2**
    -   If Step 2 does not produce such index `i`, prepare for exit:
        -   If `finish[i] == False` for some `i`, then the system is **already** in a deadlock (caused by Process `i` getting deadlocked by another Process `j` where `finish[j] == False` too)
        -   Else if `finish[i] == True` for all `i<N`, then the system is **not in a [[Deadlock]]**.

## Complexity
$$O(MN^2)$$

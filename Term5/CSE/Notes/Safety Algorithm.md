---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## Overview
Checking if this request is safe (will/not result in [[Deadlock]])

This is called when we encounter a resource request, but only if we managed to enter **Step 3** of the [[Resource allocation algorithm|resource request algorithm]].

This algorithm receives a **copy** of `available` (named as `work`), `need`, and `allocation` data structures to perform a _hypothetical situation_ of whether the system **will** be in a safe state if the current request is granted.

If we find that all processes **can still finish** their task (the elements of the `finish` vector is all `True`), then the system is in a safe state and we can grant this current request.

-   If you store each value of index `i` acquired, you can compute the sequence of _possible_ process execution sequence

For example, given the following system state: ![](https://natalieagus.github.io/50005/assets/images/week5/4.png)

and current request `R_1` made by `P1`: `[1,0,2]`, you may find that granting this request leads to a **safe state** and there exist two possible execution sequence (depending on _how_ you iterate through the `finish` vector (from index 0 onwards or from index `N-1` backwards):

1.  `P1, P3, P4, P0, P2`, or
2.  `P1, P3, P4, P2, P0`

## Safety algorithm
Receives 5 parameters and returns a `bool`:
```python
def check_safe(self, customer_index, request, work, need, allocation):
    """
    Checks if the request will leave the bank in a safe state.

    Parameters
    ----------
    work, need, allocation : list[int], list[list[int]], list[list[int]]
        deep copy of available, need, and allocation matrices
    customer_index : int
        the customer's index (0-indexed)
    request : list[int]
        an array of the requested count for each resource

    Returns
    -------
    True : if the request resources will leave the bank in a safe state
    False : otherwise
    """
```

The algorithm goes as follows:

1.  Create a vector `finish: list[int]` of size `N`, initialised to be `False` for all elements in `finish`.
    -   Then, **hypothetically** grant the current request by customer `customer_index` by updating:
        -   `work[i] = work[i] - request[i]` for all `i<M`
        -   `need[customer_index][i] = need[customer_index][i] - request[i]` for all `i<M`
        -   `allocation[customer_index][i] = allocation[customer_index][] + request[i]` for all `i<M`
    -   This request granting is _hypothetical_ because `work` is a **copy** of `available` (not the actual `available`). Similar argument with `need, allocation`. In reality, we haven’t granted the request yet, we simply compute this hypothetical situation and decide whether it will be `safe` or `unsafe`.
2.  Find an index `i` (which is a _customer_) such that:
    -   `finish[i] == False` **and**
    -   `need[i][j] <= work[j]` for **all** `j<M`.
    -   The two above condition signifies that an incomplete Customer `i` can _complete_ even after this request by `customer_index` is granted
3.  If such index `i` from Step 2 exists do the following, else go to Step 4.
    -   Update: `work[j] = work[j] + allocation[i][j]` for **all** `j<M`.
        -   This signifies that a Customer `i` that can _complete_ will free its _currently_ allocated resources.
    -   Update: `finish[i] = True`
    -   **Then, REPEAT step 2**
        
        > You might want to store the values of `i` each time you execute this Step 3 elsewhere to backtrack a possible safe execution sequence, but that’s not required for this lab.
        
4.  If no such index `i` in Step 2 exists:
    -   If `finish[i] == True` for **all** `i<N`, then it means the system is in a **safe state**. Return `True`.
    -   Else, the system is **not in a safe state**. Return `False`.


==**Common careless mistake:==** A lot of people missed the “REPEAT step 3” instruction in step 3. Step 2 and 3 must be implemented in a `while` loop, as you **might NOT** necessarily obtain i in **sequential** (increasing) order.

> Why is that so? Does it mean we can have a **safe** execution sequence e.g: `1,0,2` for a 3-process system? Yes of course! That simply means `P1` can be executed first, then `P0`, then `P2`. Think about what `i` represents (just arbitrary naming of consumer processes), of course a safe execution sequence has nothing to do with their naming!
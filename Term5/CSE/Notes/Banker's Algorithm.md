---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## Deadlock Avoidance
> We need to spend some time to perform an algorithm to **check BEFORE granting** a resource request, ==even if the request is valid and the requested resources are now available.==

This algo is called the [[Banker's Algorithm]]. Its job is to **compute** whether or not the current request will lead to a deadlock.
- If yes, reject request for resource
- If no, grant request

This algorithm is run **each time** a process requests the shared resources.

## Banker's Algorithm
Comprises 2 parts:
- [[Safety Algorithm]]
- [[Resource allocation algorithm]]

The latter utilises the output of the former to determine whether the currently requested resource should be granted or not.

## Required Attributes
- Number of processes (customers/consumers) : `N`
- Number of resource *types* (`M`) along with *initial instances of each resource type at the start*
- *Max*imum number of resources required by each process (consumer) : `Need`

## System STATE
The algorithm maintains these 4 data structures representing the system **STATE**:
1. $\begin{bmatrix}A\end{bmatrix}_{1\times M}$ 
	1. `available[i]`:  available instances of resource `i`
2. $\begin{bmatrix}M\end{bmatrix}_{N\times M}$
	1. `max[i][j]`: maximum demand of process `i` for resource `j` instances
3. $\begin{bmatrix}A\end{bmatrix}_{N\times M}$
	1. `allocation[i][j]`: current allocation of resource `j` instances for process `i`
4. $\begin{bmatrix}N\end{bmatrix}_{N\times M}$
	1. `need[i][j]`: how much more of resource `j` instances might be needed by process `i`

Example:
![](https://natalieagus.github.io/50005/assets/images/lab3/1.png)

## Part 1: [[Resource allocation algorithm]]
## Part 2: [[Safety Algorithm]]

## Rejecting Requests
If a resource request is **rejected**, dont panic, it’s not the end of the world. The process/consumer just need to **try** to request it again in the future.

How can this be implemented? Usually schedulers are programmed to tackle this kind of cases; e.g: they can be placed to a special queue and will periodically prompt for resource request until granted, or there exists some kind of event-driven solution – it’s free-for-all to implement.

## Resource Release Caveat
We also assume that (for simplicity of this lab) a process will **not** release more than what has been allocated to them (that the value of `release` is valid). We wrote this detail under `release_resources` function:
```python
def release_resources(self, customer_index, release):
    """
    Releases resources borrowed by a customer. Assume release is valid for simplicity.

    Parameters
    ----------
    customer_index : int
        the customer's index (0-indexed)
    release : list[int]
        an array of the release count for each resource

    Returns
    -------
    None
    """
    print(f"Customer {customer_index} releasing\n{release}")

    bank_lock.acquire()
    # Release the resources from customer customer_number
    for idx, val in enumerate(release):
        self.allocation[customer_index][idx] -= val
        self.need[customer_index][idx] += val
        self.available[idx] += val
    bank_lock.release()
```

## [[Week 5 - Process Synchronisation|synchronisation]]
Finally, since `max, allocation, need` and `available` are shared data structures among all these methods, we protect each method that modifies these values using a **[[Reentrant Lock]]**: `bank_lock = threading.RLock()`.

We guard the [[Critical section]]s with `bank_lock.acquire()` and `bank_lock.release()` to make it **thread safe**.

## Complexity
Deadlock avoidance is **time-consuming**, since due to the expensive `while` loop in the safety algorithm. The time complexity of the safety algorithm is $O(MN^2)$ (which is also the complexity of the Banker’s Algorithm, since the complexity of the Resource Allocation Algorithm is way smaller).

Carefully think: _why_. Also, ask yourself: what is the space complexity of the Banker’s Algorithm?

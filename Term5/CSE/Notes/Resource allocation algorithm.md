---
aliases: resource request algorithm
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## For
Determine whether this request is `safe` and to be granted.

- If `granted`, update `available`, `allocation` and `need`.
- If not `granted`, ignore the request.

## Overview
As time progresses, more **resource request** or **resource release** can be invoked by any of the processes.

-   **Releasing** Resources is trivial, we simply update the `allocation`, `available`, and `need` data structures.
-   For each Resource Request received, the output of the algorithm can be either `Granted` or `Rejected` depending on whether the system will be in a **safe state** _if the resource is granted_

## Resource Request algorithm
Inside `request_resources` function in lab.
Algo is called each time we encounter a resource request. Function receives 2 parameters and returns a `bool`:
```python
def request_resources(self, customer_index, request):
    """
    Request resources for a customer loan.

    Parameters
    ----------
    customer_index : int
        the customer's index (0-indexed)
    request : list[int]
        an array of the requested count for each resource

    Returns
    -------
    True : if the requested resources can be loaned
    False : otherwise
    """
```

1. If `request[i] <= need[customer_index][i]` for all `i < M`, go to step 2. Else return `False` (reject request) since process has exceeded max claim
2. If `request[i] <= available[i]` for all `i < M`, go to step 3. Else return `False`. Process `i` must **wait** since its requested resources are not immediately available, (reject request)
3. Requested resources are available, but we **check** if granting the request is **safe** (does not lead to [[Deadlock]])
	1. Create `deepcopy` of `available`, `allocation`, and `need`
	2. Pass these new data structures to the [[Safety Algorithm]], which will return `True` (safe) or `False` (unsafe)
4. If outcome of step 3 is
	1. `True` (==request granted==): *Update* all system states concerning `Pi` 
		-   `available[i] = available[i] - request[i]` for all `i<M`
		-   `need[customer_index][i] = need[customer_index][i] - request[i]` for all `i<M`
		-   `allocation[customer_index][i] = allocation[customer_index][i] + request[i]` for all `i<M`
	2. `False` (==request rejected==): `Pi` has to try again in the future, because granting the request results in [[Deadlock]] in the future.

## System Update
Note that these requests are made sequentially in time, so don’t forget to update the system state as you grant each request. When considering subsequent new requests, we perform the resource allocation algorithm with the **UPDATED** states that’s modified if you have granted the previous request.

If the previous request is rejected however, no change in system state is made and you can leave it as is.
---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]
[[System resource]]

## Prevention
> Ensure that at least 1 of the [[Deadlock#Necessary conditions]] **never happens**.

## Prevent [[Mutex]]
Typically infeasible. Some resourcees are intrinsically non-sharable.

e.g. [[Mutex lock]] cannot be simultaneously shared by several processes.

## Prevent Hold and Wait
To ensure hold and wait never happens, guarantee that whenever a process requests for a resource, it **does not** currently hold any other resources.

|                                                                                                                               | Protocol 1                                                                                                                                                                                                                        | Protocol 2                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| What                                                                                                                          | Must have all resources at once before beginning execution, else wait empty handed                                                                                                                                                | Only can request new reources when it has none                                                                                                                        |
| E.g.: a process that needs to `write` from DVD drive to disk and then `print` a document from the disk to the printer machine | Process must acquire all resources: DVD drive, disk, printer, before beginning execution, though the task with dsk and drive has nothing to do with the printer. After it finishes both tasks, it releases both disk and printer. | Process requests for DVD drive and disk, and writes to disk. Then it releases both. Then it requests to disk (again) and printer, prints document, and releases both. |
| Disadvantages: Starvation                                                                                                     | Process **may never start** if resources are scarce and there are too many other processes requesting for it                                                                                                                      |                                                                                                                                                                       |
| Disadvantages: Low resource utilisation                                                                                       | Resources are allocated at once but it is likely that they **aren't used simultaneouly**                                                                                                                                          | Lots of time is **wasted** for requesting and releasing many resources in the **middle** of execution.                                                                                                                                                                      |

## Prevent No preemption (allow preemption)
> [[Preemption]]: the act of temporarily interrupting a task being carried out by a process or thread, without requiring its cooperation, and with the intention of resuming the task at a later time.

To **allow** preemption, we need a certain protocol in place to ensure **progress**.

A process is holding some resources and requests another resource that cannot be immediately allocated to it (process must wait). Then do either:

| Protocol 1                                                                              | Protocol 2                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All resources the process is currently holding are preempted -- ==implicitly released== | Check first if the resources requested are held by other waiting processes or not.                                                                                                                                  |
|                                                                                         | <ul><li>If held by other **waiting** process: preempts the waiting process and give resource to requesting process</li><li>If neither held by waiting process nor available, requesting process must wait</li></ul> |

```ad-note
This protocol is often applied to resources whose state can easily be **saved** and **restored** later, such as CPU registers and memory space. It cannot gennerally be applied to such resources as [[Mutex lock]]s and [[Sephamores]]
```

## Prevent Circular Wait
> To prevent circular wait, one must have a protocol that imposes a **total ordering of all resource types**, and require that each process requests resources ==according to that order==.

E.g.
Assign some `id` to each resource and design some acquiring protocols such as:
- **Highest** priority order of currently-held resources should be $\leq$ the current resource being requested, otherwise process must release the resources that violate this condition.
- Each process can request resources only in an **increasing order** of enumenration.

```ad-note
This burdens the programmer to ensure the order by design to ensure it doesn't sacrifice resource utilisation unnecessarity.
```



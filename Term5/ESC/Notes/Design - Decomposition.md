---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Software design]]

## What
*Divide et impera* (divide and rule) is a technique of mastering complexity in vogue since ancient times ~ Dijkstra 1979

Key idea:
- Break down a system into smaller and more manageable parts, so that the channel capacity of our comprehension is not breached

"Coupling" describes the relationships _between_ modules, and "cohesion" describes the relationships _within_ them. 

A reduction in interconnectedness between modules (or classes) is therefore achieved via a reduction in coupling. 

On the other hand, well-designed modules (or classes) should have some purpose; all the elements should be associated with a single task. This means that in a good design, the elements within a module (or class) should have internal cohesion.

## Coupling
Coupling between modules can arise for different reasons, some of which are more acceptable, or desirable, than others. A ranked list (from least desirable to most desirable) might look something like the following:
-   Internal data coupling (one module modifying the internals of another)
-   Global data coupling (modules sharing global data)
-   Control or sequence coupling (one module controlling the sequence of events in another)
-   Parameter coupling (one module passing information to another through parameters)
-   Subclass coupling (one module inheriting from another)

## Cohesion
As with coupling, cohesion can be ranked on a scale of the weakest (least desirable) to the strongest (most desirable) as follows:

-   Coincidental cohesion (elements are in the same module for no particular reason)
-   Logical cohesion (elements perform logically related tasks)
-   Temporal cohesion (elements must be used at approximately the same time)
-   Communication cohesion (elements share I/O)
-   Sequential cohesion (elements must be used in a particular order)
-   Functional cohesion (elements cooperate to carry out a single function)
-   Data cohesion (elements cooperate to present an interface to a hidden data structure)

One can often estimate the degree of cohesion within a module by writing a brief statement of the module's purpose.... The following tests are suggested by Constantine:

1.  If the sentence that describes the purpose of the module is a compound sentence containing a comma or more than one verb, the module is probably performing more than one function; therefore, it probably has sequential or communicational binding (or even less: temporal, logical, or coincidental)
2.  If the sentence contains words relating to time, such as "first," "next," "then," "after," "when," or "start," the module probably has sequential or temporal binding. An example is "Wait for the instant teller customer to insert a card, then prompt for the personal identification number."
3.  If the predicate of the sentence does not contain a single, specific object following the verb, the module is probably logically bound. For example, "Edit all data" has logical binding; Edit source data may have functional binding.
4.  If the sentence contains words such as "Initialize" or "Clean up," the module probably has temporal binding.
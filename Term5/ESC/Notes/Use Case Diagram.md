---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Languages of software development]]
[[UML]]

## Use Case
> "To my knowledge, no other software engineering language construct as significant as use cases has been adopted so quickly and so widely among practitioners. I beliweve this is because use cases play a role in so any different aspects of software engineering."
> ~ Ivar  Jacobson
> Founding father of UML
> Creator of Use Case Diagram

## Example
![[Pasted image 20220521220527.png]]

## Constraints
### Pre-conditions
Must have already occured before use case is run.
E.g. (create order) must precede (modify order)

### Post-conditions
Must be true once the use case is complete.
E.g. (order is modified and consistent)

### Invariants
Must be true throughout the time the use case opertes; for exampe, an order must always have a customer number.

## Flow of events
### Basic
Most common pathway.
Usually depicts a perfect situation, in which nothing goes wrong.

### Alternative
Still considered good; just not most heavily travelled

### Exception flow of events
Things don't always go as planned.
An exception is an error condition that is important enough to the application to capture.

## Use Case Diagram

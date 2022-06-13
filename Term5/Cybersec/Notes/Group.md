---
aliases: arithmetic group
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Modular Arithmetic]]

## Arithmetic groups
> A group consists of
> - A set of elements
> - An operation $\star$ that combines two elements to a third
> - Operation $\star$ must have the following properties:
> 	- [[Closure]]
> 	- [[Associativity (arithmetic)]]
> 	- [[Identity]]
> 	- [[Invertibility]]

## Example group (Additive group)
$$(\mathbb{Z}, +)$$
is called an additive group

- [x] [[Closure]]
- [x] [[Associativity (arithmetic)|associative]]
- [x] [[Identity]]: number 0
- [x] [[Invertibility]]: -a

## Finite groups
Above are infinite groups. But there are finite groups.
$$(\mathbb{Z}/2\mathbb{Z}) \text{ or } \mathbb{Z}_2$$
- Consists of remainders of modulo 2
- 2 elements $\set{0,1}$
- Possible operations on these elements:
	- Addition: same as XOR
	- MultiplicationL same as AND

## Order of a group
> Order of a group $G$ is $|G|$, the number of its elements

## Order of an element
> The order of an element $a$ of a group $(\mathbb{S}, \star)$ is the smallest positive integer $k$ such that $a^k = a \star a \dots \star a = i$ where $i$ is the [[Identity]] element

- Consider $G = (\mathbb{Z}_{12}, +)$
- What is the order of $G$? **12**
- What is the order of element 3? **4**

## Cyclic groups
Generated from one elemnet $g$ with [[Invertibility|invertible]] [[Associativity (arithmetic)|associative]] operation.
$$G=\set{g^n | n\in\mathbb{Z}}$$
- $g$ is called **primitive element** or **generator** of $G$.
- Order of $g$ is $|G|$

Example:
$$(\mathbb{Z}_n , +1)$$
is a cyclic group with generator 1
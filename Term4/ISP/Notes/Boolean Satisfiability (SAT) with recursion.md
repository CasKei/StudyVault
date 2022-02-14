---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W4]]
[[L02.01 - Sorting, solving recursion]]
[[Recursion]]
[[Logic Synthesis]]

## Logic and Truth Table
| P   | Q   | AND | OR  | P implies Q |
| --- | --- | --- | --- | ----------- |
| 0   | 0   | 0   | 0   | 1           |
| 0   | 1   | 0   | 1   | 1           |
| 1   | 0   | 0   | 1   | 0           |
| 1   | 1   | 1   | 1   | 1           |

## Distributive Law
![[Pasted image 20220212131224.png]]

## DeMorgan's Law
![[Pasted image 20220212131239.png]]
## Boolean Satisfiability (SAT)
> SAT: Decide whetehr there is an assignment to the variables of a Boolean formula such that the formula is true (satisfied)

- Yes: there exists such an assignment: satisfiable
- No: if all assignments cannot make the formula true

## Applications
- Scheduling under multiple constraints
	- A: only Mon, Wed, Thur
	- B: no Wed
	- C: no Fri
	- D: no Tues, Thurs
	- Boolean Formula: 
	- `(Mon ∨ Wed ∨ Thu) ∧ (¬Wed) ∧ (¬Fri) ∧ (¬Tue ∧ ¬Thu)`
	- Assignment (Mon,Tue,Wed,Thu,Fri)=(T,F,F,F,F) can satisfy the formula, i.e., meet Monday
- Hardware Verification
- Solving Sudoku

## Propositional (Boolean) Formula
Propositional formula $f$ is defined over a set of propositional variables $x_1, \dots, x_n$, using the standard connectives $\lnot, \land, \lor, \to$, and parentheses
- The domain of propositional variables is $\set{0, 1}$.

A formula $f$ in ==conjunctive normal form (CNF)== is a conjunction of disjunctions (clauses) of literals, where a literal is a variable or its complement
Example: f(x1, x2, x3) =(¬x1∨x3)∧(x2∨x3)∧(¬x2∨x3)
Can encode any Boolean formula into CNF

## SAT Solver
Program that takes a Boolean formula in CNF
Returns an assignment or says none exists

Straightforward approach:
Enumerate all assignments and check formula for each

For n variables, 2^n assignments!
***
Unfortunately, it is generally believed that we can't do better than the worst case.
SAT was the first known example of an "NP-complete" problem
- Cannot be solved in polynomial time in any known way

No known algo can efficiently solve all SAT instances
It is generally beleived that no such algo can exist
Fortunately, a large enough subset of SAT can be solved efficiently (but no solver can efficiently solve all SAT instances)

![[Pasted image 20220212134415.png]]

- Based on CNF or "product of sums"
- (P∨Q)∧(¬P∨R) is in conjunctive normal form
- set of clauses, each containing a set of literals {{P,Q}, {¬P, R}}
- literal is just a variable, maybe negated
- can only negate variables, and not clauses

## Basic Backtracking Algorithm using CNF
CNF is a product of sums: we need every clause true, and at least one literal in each clause
- Backtracking search: pick aliteral, try false then true
- If clause set empty, success
- If clause set contains empty clause, failure
- Systematic way of enumeration

Important observations
- In a CNF, if one clause is false, whole formula is false (back-tracking)
- In a clause, if one literal is true, the entire clause can be removed, as it does not affect the truth value of the entire formula (formula simplification)
- In a clause, if one literal is false, the literal can be removed, as it does not affect the truth value of the clause (formula simplifiation)

![[Pasted image 20220212134843.png]]
![[Pasted image 20220212134902.png]]
![[Pasted image 20220212134913.png]]

## DPLL: Classic SAT Algorithm
Key ideda: unit propagation on top of backtracking search
If a clause contains one literal, set that literal to true
- Necessary for any satisfiable assignment

![[Pasted image 20220212135010.png]]
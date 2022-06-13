---
aliases:
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Modular Arithmetic]]
[[Field]]
[[Galois Field|GF]]

## Definition
- an arithmetic structure that contains several instances of a basic [[Field]]

the basic [[Field]] is also a subfield of the extension field.

E.g. $GF(p^n)$ with $GF(p)$ as subfield

Same operation $\star, \times$ of the subfields are used in the extension field

Comminly a [[Polynomial]] representation is used for the elements

## Example $GF(2^2)$
- Subfield is $GF(2) = (\set{0,1} , + , *)$
- Elements represented as 2 bit value, e.g. $01$

Additions:
- XOR within respective subfield:
- $10 + 11 = 01$

Assume reduction [[Polynomial]]  $$P(x) = x^2 + x + 1$$
Multiplication:
- $10 * 11 = x(x+1) = x^2 + x$
- Modulo $P(x)$ : $x^2 + x = 1 \ mod \ P$
- So $10 * 11 = 01$

If different reduction polynomial used, result may be different.

## Example $GF(2^8)$ in [[AES]]
- $GF(2^8)$ was used for the S-box and MixColumns in [[AES]]
- With irreducible [[Polynomial]]: $$P(x) = x^8 + x^4 + x^3 + x + 1$$
- S-boxes are usually hard-coded, but also can be replaced by $GF(2^8)$ multiplication/division
- S-box:
	- byte substitution for $A_i$ requires the computation of the multiplicative [[Invertibility|inverse]] , and then an affine mapping
- Multiplicative inverse can be computed on-the-fly using the extended euclidean algorithm
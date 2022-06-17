---
aliases: 
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Modular Arithmetic]]
[[Field]]
[[Galois Field|GF]]
[[Extension field]]

## Polynomials
We represent elements of $GF(p^n)$ as coefficients of a polynomial of degree $n-1$.
- Coefficients are in $GF(p)$

Example: $GF(2^8)$
$$P(x) = a_7x^7 + a_6x^6 + a_5x^5 + a_4x^4 + a_3x^3 + a_2x^2 + a_1x_1 + a_0$$
- $x$ are placeholders.
- note result of multiplication and divition is modulo a fixed, irreducible polynomial of degree n.

## Irreducible polynomials
-   A irreducible polynomial is a polynomial that cannot be factored into the product of two polynomials of positive degree. The opposite is called reducible.
-   Irreducible polynomials allow us to construct the [[Galois Field|finite field]]s.
-   In order to compute some operations in a finite field of non prime order, one needs to generate an irreducible polynomial. Why? Take a look at the earlier mod 5 example for inspiration.
-   [[AES]] field uses the irreducible polynomial $P(x) = x^8 + x^4 + x^3 + x + 1$


---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Basic ciphers]]

## Overview
### Data processing
- Ciphers operate on streams or blocks
- [[Stream ciphers]] operate on single characters at a time
- Blocks have fixed length, and are processed in one go

### Basic operations
- Mostly XOR and shifts (performance reasons)
- Some ciphers use algebraic operations such as $(+ * \textasciicircum)$, $x \text{ mod } n$
- All operations are operating on finite sets of numbers

### Cipher can be symmetric or asymmetric
| Symmetric             | Asymmetric                                     |
| --------------------- | ---------------------------------------------- |
| same key for enc, dec | diff keys for enc, dec (aka public-key crypto) |

## Stream and Block Ciphers
[[Stream ciphers]]
[[Block ciphers]]

## Confusion
Key to ciphertext relationship should be very complicated. Cannot determine key based on ciphertext.

## Diffusion
Output should depend on the input in a complex way. Change one bit of the input and at least 50% of the output should be different.
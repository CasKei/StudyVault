---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Basic ciphers]]

## Character encodings (ASCII)
In practice, data is not represented by Latin alphabet

Computing systems use binary representations, e.g. ASCII

ASCII represents 128 Latin and control characters in 7 bits.
From now on, we will operate on binary data (=integers)

### Example
`0x61 = a`, `0x41 = A`, `"Hello" = 0x48656C6C6F`

## Substitutions on binary data
[[Substitution ciphers]]
How can the substitution principle be applied to binary data?

### Based on single bits
Inversion, 2 different keys possible (one encrypts as plaintext!)

### Based on double bits
Every two bits are replaced, $4!$ possible keys

### Based on $n$ bit blocks
$(2^n)!$ possible keys

### Frequency distribution
Possible! Depending on the character coding and $n$, some blocks might still be more frequent
This would enable attacks again.

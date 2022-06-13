---
aliases: Caesar's cipher, Vigenere cipher
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Basic ciphers]]

## History
Historical ciphers, used until middle of last century. Ancient af.

**Mono-alphabetic:** plaintext and ciphertext based on alphabet (A-Z).

**Bijection** (complete mapping) between both alphabets

Example: Caesar's cipher

## Caesar's cipher
Shift all characters by $k$ in alphabet  $k = 3$: ’SECURITY’ $\rightarrow$ ’VHFXULWB’ . Shift back to decrypt.

| System                                     | Attacker                                          | Requirements                                      |
| ------------------------------------------ | ------------------------------------------------- | ------------------------------------------------- |
| Alice and Bob share key, no secure channel | Has ciphertext, does not have key, want plaintext | Confidentiality of plaintext, need key to decrypt |

How to attack?
### Brute Force
- Try all possible values for keys (only 26)
- Derive which of the plaintexts is the correct one
- How to make attacks harder?

## Improving substitution ciphers
Keyspace of Caesar is smol.
Improve by a random mapping between the 26 in/output characters.

e.g. $A \to X$, $B \to D$, $C \to M$, ...

How many different mappings exists?

## Frequency analysis of ciphertext
Frequency of letters in english?
Language-specific distribution can be used to identify.
![[Pasted image 20220517174346.png]]

## Advanced substitution schemes
How to break up known frequency distribution:
- Have several alternative replacements for 'e', choose randomly
- Intentionally misspell or use dialect
- Insert 'red herring' characters to mislead analysis
- Treat 'et' as new character, map to new symbol $\alpha$
- Substitutions are still part of [[Modern ciphers]], but must operate on alphabets with uniform likelihood

## Vigenere cipher
Published in 1553 by Giovan Battista Bellaso

Changes the substitution mapping in period pattern

Key is a word that defines that pattern

![[Pasted image 20220517175052.png]]

### Breaking the Vigenere cipher
- Direct frequency analysis will not be useful anymore
- Frequent character "peaks" are distributed
- How to break?

Note that key has fixed length and is repeated. Say length is $n$:
- All ciphertexts at 0, n, 2n ... follow a shifted distribution
- All ciphertexts at 1, n+1, 2n+1, ... follow another shifted distribution
- So we break each element of the key individually, until we get enough data to get a frequency distribution

Effort is proportional to the length of the key

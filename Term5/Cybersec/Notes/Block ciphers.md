---
aliases: confusion, diffusion
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Basic ciphers]]
[[Modern ciphers]]

## Why
[[Substitution ciphers]], [[Transposition ciphers]]: **problem**: small keyspace, frequency analysis

[[Stream ciphers]]: **problem**: key stream generation

[[AES]] block cipher: built on substitution, transposition.

Block ciphers may also feature as building blocks in other cryptographic protocols, such as [[Universal hashing|universal hash functions]] and pseudorandom number generators.
***
[[Stream ciphers]]:
- easy implementation
- low latency
- rel low throughput
- *suffer from problem of key stream generation*

> We need more efficient algorithms to encrypt large datasets.
> - Leverage large word width of modern CPUs
> - Parallelise parts in cipher

## What
An encryption function for **fixed-size blocks of data**. Current block ciphers have block size 128 bits (16 bytes). They encrypt 128 bit plaintext and generate 128 bit ciphertext. They are **reversible**. Plaintext and ciphertext are always the same size, and this is called **block size** of the block cipher.

To encrypt, we need a secret key. Key is also a string of bits, commonly 128, 256 bits.
Notation:
$E(K,p)$ or $E_K(p)$ for the excryption of plaintext $p$ with key $K$, and
$D(K,c)$ or $D_K(c)$ for the decryption of ciphertext $c$ with key $K$.

Follow [[Kerckhoff design]] principle and assume that the algorithms for encryption and decryption are publicly known.

Clarification: a block cipher does not permute the bits of the input plaintext. Instead, it takes all the $2^k$ possible $k$ bit inputs and map each to a unique $k$ bit output.

## Design principles
### Confusion
> Key to ciphertext relationship should be obscured. Cannot determine key based on ciphertext.

- Can be achieved with [[Substitution ciphers]]
- e.g. the non-linear S-box in AES

### Diffusion
> Output should depend on the input in a complex way. Change one bit of the plaintext and at least 50% of the ciphertext  should be different.

- Can be achieved with [[Transposition ciphers]]/permutations

Example: [[AES]]
![[Pasted image 20220606182041.png]]
Changing a single byte (* in the picture) in the input will change the entire block (all the other bytes in the output) after 2 rounds.

### Substitution-permutation network
Both principles combined in block ciphers. Several iterations, with one confusion function followed by a diffusion function.

### Basic operations
- Mostly XOR shifts (performance reasons)
- Some ciphers use algebraic operations such as $(+ * \textasciicircum)$, $x \text{ mod } n$
- All operations are operating on finite sets of numbers

### Cipher is symmetric only
Not used in asymmetric encryption.

## Properties
- Operate on *fixed length blocks of input* (e.g. 256 bit)
- Well suited for packet-based communication
[[ARP - Address Resolution Protocol|packet]]

| Pro                                         | Con                                                        |
| ------------------------------------------- | ---------------------------------------------------------- |
| Parallelization possible, higher throughput | Data has to fit blocks, padding required, lower efficiency |

Ciphertext depends on plaintext **and** key
- Without $p$ AND $k$, $c$ is *unpredictable*
- Without $c$ AND $k$, $p$ is *unpredictable*

*Unpredictable*: uniform distribution, i.e. relations between plaintext is not preserved in ciphertext.

These properties can be used for more than just encryption:
- [[Key stream generation]]
- [[Cryptographic hashing]]
- [[Message authentication code]]

## Examples
[[DES]]
- [[Feistel network]]

[[AES]]
[[PRESENT]]

[[Serpent]]
[[Twofish]]
[[RC6]]
[[MARS]]

## Block Cipher Modes
![[Pasted image 20220607170025.png]]
- Cut into block-sized chunks
- Padding is used for last block if required
- Mode determines how plaintext is cut and the key is used

Another name for an encryption function built using a block cipher.
So far we consider input size of same size as block size (e.g. 128 bit)
How to use a block cipher to encrypt larger datasets?

https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation

These do not provide authentication. They prevent an eavesdropper from reading the traffic, but attacker can still change the message in any way. The decryption function of an encryption mode simply decrypts the data. It might produce nonsense, but it still decrypts a modified ciphertext to some plaintext. 

[[Cryptographic padding]]

### Confidentiality only modes
Many modes of operation have been defined. Some of these are described below. The purpose of cipher modes is to mask patterns which exist in encrypted data, as illustrated in the description of the [weakness of ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#ECB-weakness).

[[Electronic Code Book (ECB)]]

Say Alice and Bob share a short key $k$ (128 bit). They want to exchange $80 * 128$ bits of data. Reusing the key is a bad idea.

[[Cipher-Block-Chaining mode (CBC)]]

The latter 3 uses the block cipher as a building block for a [[Stream ciphers]].

[[Counter-mode CTR]]
[[Output-Feedback-Mode OFB]]
[[Cipher-Feedback-Mode CFB]]

### Confidentiality and Authentication
In practice we not only want Confidentiality, but also Authentication.
[[Galois/Counter mode (GCM)]]

## Other uses
- Constructing [[Hash functions]]
[[Message authentication code|MAC]]



Ex1
$$
\begin{align}
MAC_k(a||c) &= AES(k, c \oplus AES(k,a))\\
MAC_k(b||c) &= AES(k, c \oplus AES(k, b))\\
\text{The above are equal.}&\text{ Hence, we have:}\\
AES(k,a) &= AES(k,b)
\end{align}
$$

Ex2

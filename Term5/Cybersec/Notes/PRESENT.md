---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
An academic [[Block ciphers]]
- Optimised for low cost hardware (compact size: 2.5 times smaller than [[AES]])
- 64-bit block size, 80/128 bit key
- Only a few rounds
- Efficient S-Box implementation: The non-linear layer is based on a single 4-bit S-box which was designed with hardware optimizations in mind.

Intended to be used in situations where low-power consumption and high chip efficiency is desired.


![[Pasted image 20220607164908.png]]

```php
generateRoundKeys()
for i=1 to 31 do
	addRoundKey(state, K_i)
	sBoxLayer(state)
	pLayer(state)
end for
addRoundKey(state, K_32)
```

## Cryptanalysis
A truncated [differential attack](https://en.wikipedia.org/wiki/Differential_cryptanalysis "Differential cryptanalysis") on 26 out of 31 rounds of _PRESENT_ was suggested in 2014.

Several full-round attacks using [biclique cryptanalysis](https://en.wikipedia.org/wiki/Biclique_attack "Biclique attack") have been introduced on _PRESENT_.

By design all block ciphers with a block size of 64 bit can have problems with block collisions if they are used with large amounts of data. Therefore, implementations need to make sure that the amount of data encrypted with the same key is limited and rekeying is properly implemented.

## Performance
PRESENT uses bit-oriented permutations and is not software-friendly. It is clearly targeted at hardware, where bit-permutations are possible with simple wiring. Performance of PRESENT when evaluated in microcontroller software environment using FELICS (Fair Evaluation of Lightweight Cryptographic Systems), a benchmarking framework for evaluation of software implementations of lightweight cryptographic primitives.


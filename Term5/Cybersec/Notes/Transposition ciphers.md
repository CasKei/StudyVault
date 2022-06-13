---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Basic ciphers]]

## What
Letters don't get replaced, but their sequence is changed.

Shared key determines new sequence.

## Example
Message: "This is secret"
Password: "bar"

| key   | B   | A   | R   |
| ----- | --- | --- | --- |
| order | 2   | 1   | 3   |
| text  | T   | H   | I   |
|       | S   | I   | S   |
|       | S   | E   | C   |
|       | R   | E   | T   |
|       |     |     |     |

Ciphertext is "HIEETSSRISCT"

## How to attack


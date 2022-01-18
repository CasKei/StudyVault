[Lecture Video](https://youtu.be/IicB30kA3pY)
# Basics of Information
## Overview
Computer: general-purpose digital device
In this course we learn how to build a computer from the bottom up.

We will start with understanding how we can **encode information** in terms of **voltages**, and how to utilise **transistors** to **synthesise logic**.
We can then use them to create a bigger -- more complex programmable system, and eventually with a properly designed instruction set, we can understand how a general purpose programmable machine is made.

2 main things: how to represent and encode information, and how to store this info in a tangible form using voltages [[Digital Abstraction|(next week)]].

## Information
> **Information**: *knowledge* communicated or received concerning a particular fact or circumstance.

- Resolves uncertainty.

Quantify information in electronic devices in terms of *bits* (binary digits).
Strings of bits can represent integer values.
Therefore we can use them in a way so that our devices can perform mathematical computation using this form of quantified information.

## Binary Number System
Computers are electronic devices that can only store information in terms of electrical signals: high signal and low signal.
Therefore, we need to work using the binary system and not the decimal number system.
```001101```
means $(0 \times 2^5) + (0 \times 2^4) + (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 13$ (in decimal)

## Hex and Octal Number System
What if encoding in binary is too long on paper or text editor?
We can use other number systems: encode in **octal** (base 8) or **hex** (base 16) to shorten its representation, so that it is more human friendly to write.

After some practice, it should be easy to naturally guess the deciman value of any 4-bit number without computing them from scratch.

|**Decimal**|**Binary**|**Octal**|**Hex**|
|---|---|---|---|
|0|0|0|0|
|1|1|1|1|
|2|10|||
|3|11|||
|4|100|||
|5|101|||
|6|110|||
|7|111|||
|8|1000|||
|9|1001|||
|10|1010|||
|11|1011|||
|12|1100|||
|13|1101|||
|14|1110|||
|15|1111|||
|16|1 0000|||
|17|1 0001|||
|36||||
|94||||
|256||||
|1000||||
|4096||||
|64206||||
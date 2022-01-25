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
|0|0     |0|0|
|1|1     |1|1|
|2|10     |2|2|
|3|11    |3|3|
|4|100    |4|4|
|5|101|5|5|
|6|110|6|6|
|7|111|7|7|
|8|1000|10|8|
|9|1001|11|9|
|10|1010|12|A|
|11|1011|13|B|
|12|1100|14|C|
|13|1101|15|D|
|14|1110|16|E|
|15|1111|17|F|
|16|1 0000|20|10|
|17|1 0001|21|11|
|36|10 0100|44|24|
|94|101 1110|136|5E|
|256|1 0000 0000|400|100|
|1000|11 1110 1000|1750|3E8|
|4096|1 0000 0000 0000|10000|1000|
|64206|1111 1010 1100 1110|175316|FACE|

Note:
- Prefix `0x` indicates the number system is encoded in hex and not decimal.
- Prefix `0b` indicates binary, but optional as it is obvious.
- Suffix `8` indicates numbers ecoded in oct.

### Example
Binary: $101\ 101\ 101\ 111$
Decimal: $2927$
Oct: $5557_8$
Hex: 0xB6F

## 2's Complement
![[Pasted image 20220124090819.png]]
This is the way most computers or electronic machines choose to represent signed integers.
Given a string of bits, we can compute its negative representation using 2's Complement.

Most computers use MSB (most significant bit) as the indicator of whether a particular integer is positive or negative.

> You can't tell whether a device supports signed or unsigned bits by staring at its output bits. This information has to be given beforehand.

To compute the 2's Complement representation of 5 and represent a negative version of it in a computer, we need to apply the following to the original bits:
1. inverse all 0 into 1 and 1 into 0 on the original binary number
2. add 1 to the number in step 1
### Example 0011=3
We want to turn this to -3.
Inverse: 1100
Add 1: 1100 + 0001 = 1101: $-2^3 + 2^2 + 2^0 = -3$
This is an operation that can be applied to either numbers, positive or negative, and will yield its counterpart.

## Bonus: Decimal Encoding
How to encode decimal in binary?
We extend our prior knowledge.
Suppose we have sigend binary number
1001.0011
This means $-1 \times 2^3 + 1 \times 2^0 + 1 \times 2^{-3} + 1 \times 2^{-4}$.

# Encoding
Encoding is the process of assigning representations to information.
Strings of bits can mean some value of integers, but we can also assign a fixed representation to them.

Fixed length encoding: when all choices are equally probable.
There is also variable length encoding but we will not learn that in this course.

- Number encoding: 4-bits to represent each number 1 to 10
- 7-bit ASCII encoding for English characters
- 16-bit Unicode (UTF-16) for other language alphabets that are fixed, e.g. Russian, Korean.

We can create electronic devices that can map (decode) a given encoded information, perform computations based on the received information, and encode back the output so that the results can be interpreted by users or other devices.

# Information and Uncertainty
The amount of information held by an event is inversely proportional to the probabiity p of that evewnt happening.
Information is proportiopnal to the uncertainty of that event happening.
$$Information \propto Uncertainty \propto \frac{1}{p}$$
More precisely, information is proportional to the logarithm of uncertainty of the event happening. However, since log is an increasing function, the sense of proportionality remains the same.

> In laymen terms, if an event is bound to happen, then the fact that it happens does not give any information.

For discrete events $(x_1, x_2, \dots , x_{N})$ with probability of occurence $(p_1, p_2, \dots , p_N)$, the basic measure of information for all these events is the bit.

The number of bits needed to reveal that a random variable is $x_i$ is $$I(X)=\log_2{\frac{1}{p_i}} \text{bits}$$ where $I(X)$ is the amount of information received in bits learning that the choice was $x_i$.

# Narrowing Down Choices
With $N$ equally probable choices, if it is narrowed down to $M$ choices where ($N > M$), then we can say that we are given
$$I_{N \to M}(X) = \log_2{\frac{N}{M}} \text{ bits}$$

# Summary
Given $X$ bits,
1. We can encode $2^X$ choices, or random variables
2. If insigned, can represent the number ranged from $0$ to $2^X - 1$ 
3. If signed, can representthe number ranged from $-2^{X-1}$ to $2^{X-1} -1$
Equivalently, given $Y$ choices, we need to use at least $\log_2{Y}$ bits to encode them, rounded to the nearest integer.
The prior knowledge of whether a device support signed or unsigned bits must be given to you.

# Post Conclusion
Finally, you might be wondering why we are counting the number of bits required to encode some amount of information, and why do we bother with encoding information in terms of bits at all.
As said in the introduction, our goal is to learn how to build a general-purpose device.

We begin with trying to create a digital device that is for a specific purpose:
- a simple device that can perform 1-bit addition (Mini Hardware project)
- a simple device that can perform basic logic computation: addition, subtraction, bitshift, boolean operation (SW Lab 3: ALU) 
- a simple electronic game device that can take input from players, compute it, and determine the winner (1D project)

Regardless of the specific purpose, we need a way to implement the logic for the machine.
If we were to explain the workings of an adder, it will be easy with the English language.
Explaining this t oa machine requires us to carry information in bits and get used to encoding logic.

Once we are comfortable with carrying information in bits, we have to start finding components that can manipulate voltages, called a transistor.
The transistor is not the first tool created to manipulate voltages: triode vacuum tubes and electro-mechanical relays were used in pre-1950s. Before electricity was discovered, people used mechanical gears and punch cards to encode digital data.

Triode vacuum tubes and electro-mechanical relays or even the early transistors are not cheap, they cost about a billion times more than they are now.

With this in mind, if someone in the past were to make a digital device from scratch, he/she has to be mindful with the size and cost of the device, and therefore has to be mindful with counting how many bits are needed to contain all information and logic necessary for the intended device to work.

But having a digital device that can only do a specific job is not enough. We do not want to:
- Have so many devices to carry
- Spend so much money to buy 1 device for each task

Therefore towards the middle of the term,we will learn how to create a better digital device: a programmable one that is suitab;e to be used for a plethora of purposes without any hardware changes -- and can manipulate, store and produce digital data.

We will consider all things necessary to create this programmable device that can tend to various general purposes -- meaning to create a device that can emulate the behaviour of many other devices, so that we simply need one device to perform many tasks and computations.
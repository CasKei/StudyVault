# Basics of Information
## Warm Up (Basic)
Suppose that you are to guess the value of a 16-bit number: $0x Z_1Z_2Z_3Z_4$ You are told that the value of $Z_1$ is B. Thus you have been given [N] bits of information. **What is the value of [N]?**

---
The variable $Z_x$ represents strings of 4 bits since these are in hexadecimal number system (indicated with prefix 0x)
We are literally told the first hex digit is B = 1011.
Hence we are given 4 bits of information.
There are still other 12 bits which values we still do not know.

## Keyboard Presses (Basic)
**(a).** Bob used an enhanced keyboard that was made up of 101 keys. He told Alice that he pressed one of the letter keys. **How much information did Bob give to Alice?** Hint: There are 26 letters in an alphabet.

---
## ISTD Prize (Intermediate)
Your cohort in ISTD contains 100 students:
-   51 of whom are male and 49 are female.
-   There are 31 male students who are above 19 years old.
-   On the other hand, there are 19 female students who are above 19 years old.
-   There are one male student and three female students who like to have a final exam

> You can assume that students either _like_ or _hate_ a final exam and **no indifference**.
 -   Two students like exam and is above 19 years old.
Now someone in your class won “the first to join ISTD” prize. Answer the following questions:
**(a.)** If you are told the student ID of this winner, how much **information** did you receive in bits?

**(b.)** If you are told the student ID of the last 33 students who joined ISTD, how much **information** did you receive in bits?

**(c.)** If you are told that the student who won the “first to join ISTD prize” is a male, how much **information** did you receive in bits?

**(d.)** If you are told that the student who won the “first to join ISTD prize” is above 19 years old instead, how much **information** did you receive in bits?

**(e.)** If you are told that the student who won the “first to join ISTD prize” hated a final exam and is below 19 years old, how much **information** did you receive in bits?


## Bits of Information (Intermediate)
**(a.)** Someone picks a name out of a hat known to contain the names of 5 women and 3 men, and tells you a man has been selected. **How much information have they given you about the selection?**

**(b.)** You’re given a standard deck of 52 playing cards that you start to turn face up, card by card. So far as you know, they’re in completely random order. How many **new bits of information** do you get when the **first** card is flipped over? The **fifth** card? The **last** card?

**(c.)** X is an _unknown_ N-bit binary number $(N>3)$. You are told that the first three bits of X are 011. How many bits of _information_ have you been given?

**(d.)**. X is an _unknown_ 8-bit binary number. You are given another 8-bit binary number, Y, and told that the _Hamming_ distance (number of different bits) between X and Y is one. How many **bits of information** about X have you been given when Y is presented to you?

## Measuring Information (Basic)
After spending the afternoon in the dentist’s chair, Ben has invented a new language called DDS made up entirely of vowels (the only sounds he could make with someone’s hand in his mouth). The DDS alphabet consists of the five letters: A, E, I, U, O, which occur with the following probabilities,
|Letter|Probability|
|---|---|
|A|P(A) = 0.15|
|E|P(E) = 0.4|
|I|P(I) = 0.15|
|O|P(O) = 0.15|
|U|P(U) = 0.15|

If you’re told that the first letter of the message is “A”, **give an expression for the number of bits of information you have received**.

## Modular arithmetic and 2’s complement representation (Basic)
Most computers choose a particular word length (measured in bits) for representing integers and provide hardware that performs various arithmetic operations on word-size operands. The current generation of processors have word lengths of 32 bits; restricting the size of the operands and the result to a single word means that the arithmetic operations are actually performing arithmetic modulo $2^{32}$.

Almost all computers use a 2’s complement representation for integers since the 2’s complement addition operation is the same for both positive and negative numbers. In 2’s complement notation, one negates a number by forming the 1’s complement (i.e: for each bit, changing 0 to a 1 and vice versa) representation of the number and then adding 1. **By convention**, we write 2’s complement integers with the most-significant bit (MSB) on the left and the least-significant bit (LSB) on the right. Also, **by convention**, if the MSB is 1, the number is negative, otherwise it’s non-negative.

**(a.)** How many **different** values can be encoded in a 32-bit word?

**(b.)** Please use a _32-bit 2’s complement representation_ (signed bits) to answer the following questions. What are the **representations** for:
1.  Zero
2.  The most positive integer that can be represented
3.  The most negative integer that can be represented

**(c.)** What are the **decimal values** for the most positive and the most negative number that can be represented by this signed 32-bit machine?

**(d.)** Since writing a string of 32 bits gets tedious, it’s often convenient to use hexadecimal representation where a single digit in the range of 0-9 or A-F is used to represent groups of 4 bits. Give the **8-digit hexadecimal equivalent** of the following decimal and binary numbers:

1.  Base 10: $37_{10}$
2.  Base 10: $-32768_{10}$
3.  Base 2: `1101 1110 1010 1101 1011 1110 1110 1111`

**(e).** **Calculate** the following using 6-bit 2’s complement arithmetic (which is just a fancy way of saying to do ordinary addition in base 2, keeping only 6 bits of your answer). Show your work using binary notation. Remember that subtraction can be performed by negating the second operand and then adding to the first operand.

1.  13 + 10
2.  15 - 18
3.  27 - 6

## Dice Throwing Game (Intermediate)
A group of five friends are playing a game that requires them to generate random numbers using 10 fair dice in the beginning before proceeding with the game. They each will throw the 10 dice and sum up all the outcomes of the dice to get the random number. Answer the following questions:

**(a.)** How many bits at the **minimum** (so round up your answer to the nearest integer) are required to encode all distinct numeric outcomes of 10?

**(b.)** Someone in the group suggests that they can just use a die and throw it 10 times to get the random number required for the game. This way, they don’t have to deal with carrying so many dice. The game began and then he proceeded with throwing the die. His first 3 throws are: 1, 3, and 4. **How many bits of information has been given so far?** Give your answer in 3 decimal places.

**(c.)** After throwing the die 9 times in total, how many **new bits** of information did he get from making the last (the 10th) throw? Give your answer in 3 decimal places.

**(d.)** Finally, he found that the number he got in total from all 10 throws is 53. **Express this number in 3-digit hex**, formatted as 0xZZZ where Z is your answer.

## Another Base Conversion (Basic)
Consider an 8-bit **signed** number systems. **Do the following base conversion**, and indicate with a `0b` prefix for binary systems and `0x` prefix for hexadecimal systems. Octal and decimal systems do not have prefixes.

1.  76 (decimal) to binary
2.  0b10000001 (binary) to decimal
3.  0b10011101 (binary) to hexadecimal
4.  0xBF (hexadecimal) to binary
5.  0xC6 (hexadecimal) to octal

## Representing -32 on different number systems (Basic)
Which of the following signed numbers is **the representation** of number -32 for either an 8-bit or 16-bit system? _Note: the answer must be either 8-bit or 16-bit long._

1.  `0b1010 0000`
2.  `0b1110 0000`
3.  `0b0001 0000`
4.  `0xE0`
5.  `0x80E0`
6.  `0xFFE0`
7.  `0x10E0`
8.  `0x800000E0`
9.  `0xFFFFFFE0`

## Proof of 2’s Complement (Challenging)
At first blush, “Complement and add 1” doesn’t seem like an obvious way to negate a two’s complement number. By manipulating the expression $A + (-A) = 0$, **show** that “complement and add 1” does produce correct representation for the negative of a two’s complement number.

_Hint: express 0 as (-1 + 1) and rearrange the terms to get -A on one side and ZZZ+1 on the other and then think about how the expression ZZZ is related to A using only logical operations (AND, OR, NOT)._

Also, see how binary subtraction ‘borrow’ method works [here](https://www.wikihow.com/Subtract-Binary-Numbers) if you dont know how it works.

# The Digital Abstraction
## VTC Plot (Basic)
The behavior of a 1-input 1-output device is measured by hooking a voltage source to its input and measuring the voltage at the output for several different input voltages, resulting in the following VTC plot,
![[Pasted image 20220127092808.png]]
We’re interested in whether this device can serve as a legal combinational device that obeys the **static discipline**. For this device, obeying the static discipline means that,
$$
\begin{align}
\text{If } V_{IN}&\leq V_{IL} &\text{ then } V_{OUT}&\geq V_{OH},\\
\text{and if } V_{IN}&\geq V_{IH} &\text{ then } V_{OUT}&\leq V_{OL}
\end{align}$$
When answering the questions below, assume that all voltages are constrained to be in the range of 0V to 5V,
1.  Can one choose a **Vol** of 0V for this device? **Explain**.
2.  **What’s the smallest** **Vol** one can choose and still the device obey the static discipline?
3.  Assuming that we want to have 0.5V noise margins for both “0” and “1” values, **what are the appropriate voltage levels** for Vol, Vil, Vih, and **Voh** so that the device obeys the static discipline? _Hint: there are many choices. Just choose the one that obeys the static discipline and the NM constraint._
4.  **What device** is this called?
## Inverter Madness (Intermediate)
**(a).** The following graph plots the VTC for a device with one input and one output. **Can this device be used** as a combinational device in logic family with 0.75 noise margins?
![[Pasted image 20220127093252.png]]

**(b).** You are designing a new logic family and trying to decide on values of the four parameters: Vol, Vil, Vih, and **Voh** that lead to non-zero noise margins for various possible inverter designs. Four proposed inverter designs exhibit the VTC shown in the diagrams below. **For each design, either specify four suitable values** of Vol, Vil, Vih, and **Voh** or **explain why no values can obey the static discipline.**

_Hint: you may want to start by choosing NM to be 0.5V for ease of computation._
![[Pasted image 20220127093411.png]]

## Static Discipline (Basic)
**(a).** Consider a combinational _buffer_ with one input and one output. Suppose we set its input to some voltage $V_{IN}$, wait for the device to reach a steady state, then measure the voltage on its output **Vout** and find out $V_{OUT} < V_{OL}$. **What can we deduce about the value of $V_{IN}$?**

**(b).** Now consider an inverter. Suppose we set its input to some voltage $V_{IN}$, wait for the device to reach a steady state, then measure the voltage on its output Vout, and find $V_{OUT} > V_{OH}$. **What can we deduce about the value of $V_{IN}$?**

## VTC Analysis (Intermediate)
![[Pasted image 20220127093536.png]]
Which of the following specification(s) **does not obey** the static discipline? Select all that apply.
1.  $V_{IL} = 0.4V, V_{IH} = 3.1V, V_{OL} = 0.2V, V_{OH} = 4.2V$
2.  $V_{IL} = 0.5V, V_{IH} = 3V, V_{OL} = 0.3V, V_{OH} = 4V$
3.  $V_{IL} = 0.2V, V_{IH} = 3V, V_{OL} = 0.4V, V_{OH} = 4.2V$
4.  $V_{IL} = 0.5V, V_{IH} = 4V, V_{OL} = 0V, V_{OH} = 3.5V$
5.  $V_{IL} = 0.5V, V_{IH} = 3.5V, V_{OL} = 0V, V_{OH} = 4V$
# Defense in Depth
There will always be bugs, so system architects employ a strategy called defense in depth, which uses may layers of varying security mechanisms to frustrate attackers.
# Cryptography
One of the most common defences against cyber attacks.
In order to make information secret, you use a cipher - an algorithm that converts plain text into ciphertext, which is gibberish unless you have a key that lets you undo the cipher.
The process of making text secret is called encryption, and the reverse process is called decryption.
Ciphers have been used long before computers showed up.
To decipher the message, recipients had to know both the algo and the number to shift by, which acted as the key.
The caesar cipher is one exampleof a larger class of techniques called substitution ciphers. These replace every letter in a mesage with something else according to a translation.
A big drawback of basic substitution ciphers is that letter frequencies are preserved.
A skilled cryptanalyst can work backwards from these kinds of statistics to figure out the message.

Another fundamental class of techniques are permutation ciphers
One simple example is called a columnar transposition cipher.
Put a message in columns, then encrypt by reading through another perspective, hence forming the encrypted message.
The ordering direction, as well as the 5 by 5 grid size, serves as the key.
Like before, if the cipher and key are known, a recipient can reverse the process to reveal the original mesage.

In 1900s, encryption was mechanised by machines. The most famous was the German Enigma, used by the Nazis to encrypt their wartime communications.
Has Enigma Rotors, wherewire connects top tabs to lower tabs, swapping letters like a substitutiton cipher. Uses 3 or more rotors in a row, each feeding into the next, so it is reaaally complicated. Rotors can also be rotated or inserted in different orders, providing a lot of differnet substitution mappings. Following the rotors was a special circuit called a reflector. Instead of passing the signal on to another rotor, it connected every pin to another, and sent the electrical signal back throgh the rotors. Finally, there was a plugboard at the front of the machine that allowed letters coming from the keyboard to be optionally swapped, adding another level of complexity.
If you look at the circuit, it is impossible for a letter to be encrypted as itself, which turned out to be a fatal cryptographic weakness.
Finally, to prevent the Enigma from being a simple substitution cipher, every single time a letter was entered, the rotors advanced by one spot, sort of like an odometer in a car.

But now cryptography moved from hardware to software.
One of the earliest software ciphers to become widespread was the Data Encryption Standard developed by IBM and the NSA in 1977.
DES, as it was known, originally used binary keys that were 56 bits long,, which means that there are 2 to 56, so about 72 quadrillion different keys.
Back in 1977, that nobody meant that nobody - except perhaps the NSA - had enough computing power to brute-force all possible keys.

But by 1999, a qarter-million dollar computer could try every possible DES key in just 2 days, rendering the cipher insecure.

So, in 2001, the Advanced Encryption Standard (AES) was finalised and published.
AES is designed to use uch bigger keys - 128, 192 or 256 bits in size - making brute force attacks much much harder.
For a 128-bit keys, you'd need trillions of years to try every combination, even if you used every single computer on the planet today.
AES chops data up into 16-byte blocks, and then applies a series of substitutions and permutations, based on the key value, plus some other operations to obscure the message, and this process is repeated ten or more times for each block.
Why only 16 byte and 128-bit? It is a performance tradeoff.
If it took hours to encrypt and send an email, or minutes to connect to a secure website, people wouldn't use it.
AES balances performance and security to provide practical cryptography.
Today, AES is used everywhere, from encrypting files on iPhones and transmitting data over Wifi with WPA2, to accessing websites using HTTPS.

These depended on sender and recipient having the same key.
What's needed is a way for a server to send a secret key over the public internet to a user wishing to connect securely.
It seems like that wouldn't be secure, because if the key is sent in the open and intercepted by a hacker, couldn't they use that to decrypt all communication between the two?

The solution is key exchange! -- An algorithm that lets 2 computers agree on a key without ever sending one.
We can do this with one-way functions -- mathematical operations that are very easy to do in one direction, but hard to reverse.
Mathematical one-way functions are perfect, and this is what the Diffie-Hellman key exchange uses.
The one-way function is modular exponentiation.
This means taking one number, the base, to the power of another number, the exponent, and taking the remainder when dividing by a third number, the modulus.
The hard part is figuring out the exponent given only the result and base.
If we make these numbers big, say hundreds of digits long, then finding the secret exponent is nearly impossible.
The Diffie-Hellman uses modular exponentiation to calculate a shared key.
First, there's a set of public values -- the base and the modulus, that everyone gets to know. To send a message securely to recipient, sender will need to pick a secret exponent X. Then sender calculates B^X mod M and send this big number over to recipient.
Recipient deos the same, sending B^Y mod M.
To create a shared secret key, sender takes what recipient sent, and take it to the power of X, sender's secret exponent.
This is mathematically equal to B^{XY} mod M
Recipient does the same and ends up with the same.
This big number can be used as a shared key for encrypted communication, using something like AES for encryption. Diffie-Hellman key exchange is one method for establishing a shared key. These keys that can be used by both sender and receiver, to encrypt and decrypt messages, are called symmetric keys because the key is the same on both sides.

The Caesar Cipher, Enigma and AES are all symmetric encryption.
There's alo asymmetric encryption, where there are two different keys, most often one that's public and another that's private.
So people can encrypt a message using a public key that only the recipient, with their private key, can decrypt.
In other words, knowing the public key only lets you encrypt, but not decrypt -- it's asymmetric!
A digital public key can encrypt something that can only be decrypted with a private key.
The reverse is possible too: encrypting something with a private key that can be decrypted with a public key.
This is used for signing, where a server encrypts data using their private key. Anyone can decrypt it using the server's public key.
This acts like an unforgeable signature, as only the owner, using their private key, can encrypt.
It proves that you're getting data from the right server or person, and not an imposter.

The most popular asymmetric encryption techique used today is RSA, named after its inventors: Rivest, Shamir and Adleman.

The lock symbol on website browser thingy means that your computer has used public key cryptography to verfy the server, key exchange to establish a secret temporary key, and symmetric encryption to protect all the back-and-forth communication from prying eyes.

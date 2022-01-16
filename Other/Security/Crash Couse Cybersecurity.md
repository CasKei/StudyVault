# Cybersecurity
A set of techniques to protect the [[#secrecy]], [[#integrity]], and [[#availability]] of computer systems and data against threats.

## Secrecy
AKA Confidentiality
Only authorised people should be able to access of read specific computer systems and data.

Attacks on secrecy: data breaches, hackers reveal people's information
## Integrity
Only authorised people should have the ability to use or modify systems and data

Attacks on integrity: Hackers learn your password and send emails masquerading as you
## Availability
Authorised people should always have access to their systems and data.

Attacks on availability: Denial of Service Attack, where hackers overload a website with fake requests to make it slow or unavailable for others.

# Attack Vector
Security experts start with a specification of who your "enemy" is, at an abtract level, called a `threat model`.

This profiles attackers: their capabilities, goals, and probable means of attack -- what's called an `attack vector`.

Threat models lets you prepare against specific threats, rather than being overwhelmed by all the way hackers could get to your systems and data. 

How a system is secured depends heavily on who it is being secured against.

Often threat models are specified in terms of technical capabilities: e.g. `Someone who has physical access to your laptop along with unlimited time`

With a given threat model, security architects need to come up with a solution that keeps a system secure -- as long as certain assumptions are met, like no one reveals their password to the attacker.

There are many methods for protecting computer systems, networks and data.

# Two Main Security Questions
1. Who are you?
2. What should you have access to?

Clearly, access should be given to the right people, but refused to the wrong people.

# Authentication
To differentiate between right and wrong people, we use authentication -- the process by which a computer understands who it's interacting with.

Generally there are 3 types, each with their own pros and cons
## What you know
Based on knowledge of a secret that should only be known by the real user and the computer, e.g. a username and password.
Most widely used because easiest to implement.

Can be compromised if hackers guess or otherwise come to know yoru secret

Some passwords are easy to guess for a human, others are easy to guess for a computer.
Human easy: 123456, password, etc
Computer easy: 2580
Seems difficult for human, but there are only 10000 possible combinations of 4 digit pins, so easy for computer
### Brute Force Attack
Computer tries all combinations systematically to get the password.
There's nothing clever to the algo
Some computer systems lock you out or make you wait after a few wrong attempts.
This is a common and reasonable strategy, and it does make it harder for less sophisticated attackers.

But if hackers have already taken over tens of thousands of computers, forming a botnet.
Using all these computers, the same pin -- 2580 -- can be tried on many tens of thousands of bank accounts simultaneously.
Even in just one attempt, they might have already found one or more accounts that happen to use that pin.

Increasing the lengths of PINs and passwords can help, but even 8 digit PINs are pretty easy to crack.
This is why so many websites now require you to use a mix of lower and upper case letters, special symbols, and so on -- it explodes the number of possible password combinations.
An 8 digit numerical PIN only has a hundren million combinations -- computers easy.
But an 8 character password with all those weird stuff mixed in has more than 600 trillion combinations.

Of course these passwords are hard for us mere mortals to remember, so a better approach is for websites to let us pick something more memorable, like 3 words joined together. 
## What you have
Based on possession of a secret token that only the real user has, e.g. a physical key and lock.
You can only unlock the door if you have the key. This escapes the problem of being "guessable".
Typically require physical presence, so much harder for remote attackers to gain access.

Can be compromised if attacker is physically close. Keys can be copied, phones stolen, locks picked.
## What you are
Depends on you. You authenticate yourself by presenting yourself to the computer.
e.g. Biometric authenticators, like fingerprint readers and iris scanners.
Can be very secure, but the best technlogies are still quite expensive.

Data from sensors varies over time. [[#What you know]] and [[#What you have]] authentication have the nice property of being deterministic--either correct or incorrect (always producing the same predictable result from the given input).
If you know the secret or have the key, you are granted access 100% of the time.
If you don't, you get access 0% of the time.

OTOH, biometric authentication is probabilistic. There's some chance the system won't recognise you.
Worse, there's some chance the system will recognise the wrong person as you.
Of course, in production systems, these chances are low, but not 0.

Another issue with biometric authentication is that it can't be reset.
You only have so many fingers, so what happens if an attacker compromises your fingerprint data?
Recently, researchers have showed it is possible to forge your iris just by capturing a photo.

## 2FA
All forms of authentication have strengths and weaknesses, and all can be compromised in some way.
So security experts suggest using 2 or more forms of authentication for important accounts.

This is known as two-factor or multi-factor authentication.
An attacker may be able to guess your password or steal your phone, but it's much harder to do both.

# Access Control
After [[#Authentication]] comes access control.
Once a system knows who you are, it needs to know what you should be able to access, and for that, there is a specification of who should be able to see, modify and use what.

This is done through **Permissions** or **Access Control Lists** (ACL), which describe what access each user has for every file, folder and program on a computer.
### Read
Allows user to see the contents of a file
### Write
Allows a user to modify its contents
### Execute
Allows a user to run a file

## Bell-LaPadula Model
Formulated for the US Department of Defense's Multi-Level Security policy.

The first general rule of thumb is that people shouldn't be able to 'read up'
The second general rule of thumb is that people shouldn't be able to 'write down' (guarantees that there is no accidental leakage of top secret info into bottom)

## Chinese Model
## BIBA Model
# Malware
Malicious software
If the attacker installs malware -- compromising the host computer's OS, how can we be sure security programs don't have a backdoor that let's attacekrs in.
We don't.
We can't prevent implementation error.

To reduce implementation error, reduce implementation.

One of the holy grails of system level security is a security kernel or a trusted computing base: a minimal set of operating system software that's close to provably secure.

A challenge in constructing these security kernels is deciding what should go into it. RMB the less code the better.

# Independent Verification and Validation
Even after minimizing code bloat, it would be great to 'guarantee' that code as written is secure.
Formally verifying the security of code is an active area of research.
Best process we have now is [[#Independent Verification and Validation]].
This works by having code audited by a crowd of security-minded developers. This is why security code is almost always open-sourced.

It's often difficult for people who wrote the original code to find bugs, but external developers, with fresh eyes and different expertise, can spot problems.

There are also conferences where like-minded hackers and security experts can mingle and share ideas, the biggest of which is DEF CON, held annually in Las Vegas.

# Isolation
Finally, even after reducing code and auditing it, clever attackers are bound to find tricks that let them in.
With this in mind, good developers should take the approach that, not if, but when their programs are compromised, the damage should be limited and contained, and not let it compromise other things running on the computer. This principle is called **isolation**.

To achieve isolation, we can 'sandbox' applications.
Operating Systems attempt to sandbox applications by giving each their own block of memory that other programs can't touch.

It's also possible for a single computer to run multiple Virtual Machines, essentially simulated computers, that each live in their own sandbox.
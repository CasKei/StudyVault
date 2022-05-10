---
tags: CC, Security
---
# Social Engineering
The most common way of hacking into people's accounts isn't hacking, but tricking people.
This is called social engineering, where a person is manipulated into divulging confidential information, or configuring a computer system so that it permits entry by attackers.

## Phishing
The most common type of attack is phishing, which you most often encounter as an email asking you to login to an account on a website, say your bank.
You'll be asked to click a link in the email, which takes you to a site that looks legit to the casual observer, but is really an evil clone.
When you enter your credentials, that information goes straight to the hackers, who can then login to the real website as you. 

## Pretexting
Another social engineering attack is pretexting, where attackers call up, let's say a company, and then confidently pretend to be from their IT department.
Often attackers will call a first number, and then ask to be transferred to a second, so that the phone number appears to be internal to the company.
Then, the attacker can instruct an unwitting user to configure their computer in a compromising way, or get them to reveal confidential details, like passwords or network configurations.

# Trojan Horses
Emails are also a common delivery mechanism for trojan horses, programs that masquerade as harmless attachements, like a photo or invoice, but actually contain malware.

# Malware
[[Crash Couse Cybersecurity#Malware|Malware]] can take many forms: some might steal your data, like your banking credentials. Others migh encrypt your files and demand a ranson, known as a ransomware.
If they can't run malware or get a user to let them in, attackers have to force their way in through other means.

# Brute Force
One method discussed previously is to [[Crash Couse Cybersecurity#Brute Force Attack|brute force]] a password, try every combination of password until you gain entry.

Most modern systems defend against this type of attack by having you wait incrementally longer periods of time following each failed attempt, or even lock you out entirely after a certain number of tries.

## NAND Mirroring
One recent hack to get around this is called NAND Mirroring, where if you have physical access to the computer, you can attach wires to the device's memory chip and make a perfect copy of its contents.

With this setup, you can try a series of passwords, until the device starts making you wait.

When this happens, you just reflash the memory with the orignal memory you made, essentially resetting it, allowing you to try more passwords immediately, with no waiting.

This technique was shown to be successful on an iPhone 5C , but many newer devices include mechanisms to thwart this type of attack.

# Remote Hacking (Exploit)
If you don't have physical access to a device, you ahve to find a way to hack it remotely, like over te Internet.
In general, this requires an attacker to find and take advantage of a bug in a system, and successfully utilising a bug to gain capailities or access is called an exploit.

### Buffer Overflow
One common type of exploit is buffer overflow.
Buffers are a general term fo a block of memory reserved for storing data.
![[Pasted image 20220116161022.png]]
Overflow the buffer with adjacent memory. Sometimes this will just cause a program or OS to crash, because important values are overwritten with alskdjfha.

Attacekrs can also exploit this bug more cleverly by injecting purposeful new values into a program's memory.

With the ability to arbitrality manipulate a program's memory, hackers can bypass things like login prompts, and sometimes even use that program to hijack the whole system.

### Bounds Checking
There are many methods to combat buffer overflow attacks.
The easiest is to always test the length of inpput before copying it into a buffer, called bounds checking.

Many modern programming languages implement bounds checking automatically.
 
Programs can also randomise the memory location of variables, like our hypothetical "is admin" flag, so that hackers don't know what memory location to overwrite, and are more likely to crash the program than gain access.

Programs can also leave unused space after buffers, ane keep an eye on those values to see if they change; if they do, they know an attacker is monkeying around with memory.
These regions are called canaries, named after the small birds miners used to take underground to warn them of dangerous conditions.

# Code Injection
Most commonly used to attack websites that use databases, which pretty much all big websites do.

# Sanitising
Good servers sanitise input by removing or modifying special characters before running database queries.
# Botnet
Hackers take over multiple computers to form a botnet.
This can have many purposes, like sending huge volumes of spam, mining bitcoins using other people's computing power and electricity, and launching Distributed Denial of Service (DDoS) attacks against servers.
## DDoS
DDoS is where all the computers in the botnet send a flood of dummy messages. This can knock services offline, either to force owners to pay a ransom or just to be evil.


Despite all of the hard working white hats, exploits wroking online, and software engineering best practices, cyberattacks happen on a daily basis.
They cost the global economy roughly half a trillion dollars annually, and that figure will only increase as we become more reliant on computing systems.
This is especially worrying to governments, as infrastructure is increasingly comuter-driven, like powerplants, the electrical grid, traffic lights, water treatment plants, oil refineries, air traffic control, and lots of other key systems.

Many experts predict that the next major war will be fought in cyberspace, where nations are brought to their knees not by physical attack, but rather crupplied econoically and infrastructurally through cyberwarfare
---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

> This protects the information from **detection, deletion or creation** by an unauthorized users and guarantees the **accuracy, preciseness and completeness** of the information.

## Data Manipulation attacks
Alice sends Bob a message:  
- ”Hi Bob, I’m Alice, please buy 100 stocks of Company A”  

The message sent in plaintext.\
Attacker Eve wants to manipulate Alice’s stock trade.
- Eve can jam, eavesdrop and insert  

What kind of attacks are possible here?

### Attack
Attack example: Eve eavesdrops, jams, spoofs similar  
message:  
- ”Hi Bob, I’m Alice, please buy 999 stocks of Company B”  

Bob assumes the message is from Alice, buys stocks for her  

Problems? 
> Secure **authentication** and **integrity** of the message

## Protecting the message
### One Idea: encrypt the message
e.g. use [[Stream ciphers|One-Time Pad]]

E.g. using OTP to encrypt "buy100"

| Thing    | Encrypted         |
| -------- | ----------------- |
| "buy100" | 0x6275793130300a  |
| Key      | 0xa29c7b1e0e3aee  |
| Result   | 0xc0e9022f 3e0ae4 | 

Can Eve:
- Break confidentiality of the message?
- Change the message's content?

### Other measures
- [[Block ciphers]] are not always enough
- We need a dedicated tool to validate message integrity [[Message authentication code|MACs]]

## Does Symmetric Encryption protect data integrity?
### Attack
| Thing                             | Encrypted        |
| --------------------------------- | ---------------- |
| "buy100"                          | 0x6275793130300a |
| Key                               | 0xa29c7b1e0e3aee |
| Result                            | 0xc0e9022f3e0ae4 |
| Mask ("buy100" $\oplus$ "buy999") | 0x00000008090900 |
| Result                            | 0xc0e902273703e4 |
| Plaintext ("buy999")              | 0x9275793939390a |

No integrity means no authenticity either
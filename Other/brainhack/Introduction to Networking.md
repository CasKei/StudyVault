[[BH22]]

## How to communicate between 2 devices
### Address
[[Mac and IP]]
### Port
Multiple server can share single IP
### Protocol
How to understand what sender is saying? some rules to communicate

## OSI 7 layer
[[OSI Model / Internet Protocol Suite]]
### En/Decapsulation
![[Pasted image 20220619150604.png]]
### What is OSI 7 layer
![[Pasted image 20220619150622.png]]
### Each Layer

| Layer           | Thing                                                                                                                                                                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7. Application  | The only layer that interacts diectly wit hdata from user. Softwre apps like browsers ad email clients rely on this to initiate comunications.                                                                                                                                                        |
| 6. Presentation | Primarily responsible for preparing data s it can be used by application layer. Makes data presentable for apps to consume. Responsible for translation, encryption and compression of data.                                                                                                          |
| 5. Session      | Responsible for opening and closing communication between 2 devices. Time when communication is opened and closed is called session.                                                                                                                                                                  |
| 4. Transport    | Responsible for end-to-end communication between two devices. Includes taking data from session layer and breaking it into chunks called segments before sending it to layer 3. Transpot layer on receiving device responsible for reassembling the segments into data the session layer can consume. |
| 3. Network      | Responsible for facilitating data transfer between 2 different networks. If 2 devices communicating are on the same network, then this layer is unnecessary                                                                                                                                           |
| 2. Data Link    | Facilitates data transfer between 2 devices on the same network                                                                                                                                                                                                                                       |
| 1. Physical     | Physical equipment involved in the data transfer such as cables and switches. Also the layer where data is converted into a bit stream, which is a string of 1s and 0s.                                                                                                                                                                                                                                                                                                      |

## TCP/UDP Protocol
[[Transport Control (TCP UDP)]]
### TCP and UDP
![[Pasted image 20220619151322.png]]

### Handshake
[[Handshake]]
![[Pasted image 20220619151517.png]]
![[Pasted image 20220619151538.png]]
![[Pasted image 20220619151607.png]]

## Well-Known Network services
### ARP
[[ARP - Address Resolution Protocol|ARP]]
### DHCP
[[DHCP]]
### HTTP
[[HTTP]]
### DNS
[[DNS]]
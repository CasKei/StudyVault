---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]
[[Interprocess Communication]]
[[Message Passing]]

## Socket

Socket is one of message passing **interfaces**.

A socket is one endpoint of a **two-way communication link** between two programs running on the network with the help of the **kernel**:

-   It is a **concatenation** of an [[Mac and IP|IP]] address, e.g: 127.0.0.1 for localhost
-   And **TCP** (connection-oriented) or **UDP** (connectionless) **port**, e.g: 8080.
    -   We will learn more about UDP and TCP as network communication protocols in the later part of the semester.
-   When concatenated together, they form a **socket**, e.g: 127.0.0.1:8080
-   All socket connection between two communicating processes must be **unique**.

For processes in the same machine as shown in the figure above, both processes communicate through a socket with IP `localhost` and a **unique**, unused port number. Processes can `read()`or `send()`data through the socket through [[System calls]]:

1.  For example, when P1 tries to send a message (data) to P2 using socket, it has to copy the message from **its own space** to the kernel space first through the socket via `write` system call.
2.  Then, when P2 tries to read from the socket, that message in the kernel space is copied again to P2’s space via `read` system call.

The diagram below illustrates how socket works in general: ![](https://natalieagus.github.io/50005/assets/images/week3/15.png)

![](https://natalieagus.github.io/50005/assets/images/week3/14.png)

### Program: IPC using Socket

One process has to create a socket and listens for incoming connection. We call this process the **server**. After a listening socket is created, another process can connect to it. We call this process the **client**.

Server process has to be run first, followed by the client process. The code below implements both versions: **blocking** and **non blocking** `read()`. Try blocking version, then nonblocking.

**Server** program:

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <fcntl.h> /* Added for the nonblocking socket */

#define PORT 12345

int main(int argc, char const *argv[])
{
   int server_fd, new_socket, valread;
   int opt = 1;
   struct sockaddr_in address;
   int addrlen = sizeof(address);

   char buffer[1024] = {0};
   char *message = "Hello from server";

   // Creating socket, and obtain the file descriptor
   // Option:
   //      - SOCK_STREAM (TCP -- Week 11)
   //      - AF_INET (IPv4 Protocol -- Week 11)
   if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
   {
       perror("socket failed");
       exit(EXIT_FAILURE);
   }

   // Attaching socket to  port 12345
   if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEPORT,
                  &opt, sizeof(opt)))
   {
       perror("setsockopt");
       exit(EXIT_FAILURE);
   }
   address.sin_family = AF_INET;
   address.sin_addr.s_addr = INADDR_ANY;
   address.sin_port = htons(PORT);

   // Assign name to the socket
   /**
    When a socket is created with socket(2), it exists in a name
    space (address family) but has no address assigned to it.  bind()
    assigns the address specified by addr to the socket referred to
    by the file descriptor sockfd.  addrlen specifies the size, in
    bytes, of the address structure pointed to by addr.
    Traditionally, this operation is called "assigning a name to a
    socket".
   **/

   if (bind(server_fd, (struct sockaddr *)&address,
            sizeof(address)) < 0)
   {
       perror("bind failed");
       exit(EXIT_FAILURE);
   }

   // server listens for new connection (blocking system call)
   if (listen(server_fd, 3) < 0)
   {
       perror("listen");
       exit(EXIT_FAILURE);
   }

   // accept incoming connection, creating a 1-to-1 socket connection with this client
   if ((new_socket = accept(server_fd, (struct sockaddr *)&address,
                            (socklen_t *)&addrlen)) < 0)
   {
       perror("accept");
       exit(EXIT_FAILURE);
   }

   // Choose between blocking and nonblocking read
   // Blocking read
   valread = read(new_socket, buffer, 1024);

   // Nonblocking read
   // fcntl(new_socket, F_SETFL, O_NONBLOCK); /* Change the socket into non-blocking state */
   // valread = recv(new_socket, buffer, 1024, 0);

   printf("%s\n", buffer);
   send(new_socket, message, strlen(message), 0);
   printf("Hello message sent to client\n");
   return 0;
}
```

**Client** program:

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <fcntl.h> /* Added for the nonblocking socket */
#include <arpa/inet.h>

#define PORT 12345

int main(int argc, char const *argv[])
{
   struct sockaddr_in address;
   int sock = 0, valread;
   struct sockaddr_in serv_addr;

   char *message = "Hello from client";
   char buffer[1024] = {0};

   // create a socket
   if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
   {
       printf("\n Socket creation error \n");
       return -1;
   }

   // fill block of memory 'serv_addr' with 0
   memset(&serv_addr, '0', sizeof(serv_addr));

   // setup server address
   serv_addr.sin_family = AF_INET;
   serv_addr.sin_port = htons(PORT);

   // Convert IPv4 addresses from text to binary form and store it at serv_addr.sin_addr
   if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0)
   {
       printf("\nInvalid address/ Address not supported \n");
       return -1;
   }

   // connect to the socket with defined serv_addr setting
   if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
   {
       printf("\nConnection Failed \n");
       return -1;
   }

   // send some data over
   send(sock, message, strlen(message), 0);
   printf("Hello message sent to server\n");

   // read from server back
   valread = read(sock, buffer, 1024);
   printf("%s\n", buffer);

   return 0;
}
```
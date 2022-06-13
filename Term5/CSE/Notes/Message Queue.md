---
aliases: ftok, msgget, msgsnd, msgrcv
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]
[[Interprocess Communication]]
[[Message Passing]]

## Message Queue
**Message Queue** is just another **interface** for message passing (another example being [[Socket]] as shown in the previous section). It uses [[System calls]] `ftok, msgget, msgsnd, msgrcv` each time data has to be passed between the processes. [`msgrcv` and `msgsnd`](https://man7.org/linux/man-pages/man2/msgsnd.2.html) can be made [[Types of system calls|blocking or non-blocking]] depending on the setup.

The figure below illustrates the general idea of Message Queue. The queue data structure is maintained by the Kernel, and processes may write into the queue at any time. If there are more than 1 writer and 1 reader at any instant, careful planning has to be made to ensure that the **right** message is obtained by the right process. ![](https://natalieagus.github.io/50005/assets/images/week3/16.png)

**Writer** process program:

```c
// C Program for Message Queue (Writer Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#define MAX 10

// structure for message queue
struct mesg_buffer 
{
   long mesg_type;
   char mesg_text[100];
} message;
 
int main()
{
   key_t key;
   int msgid;

   // ftok to generate unique key
   // key_t ftok (const char *pathname, int proj_id);
   // pathname to existing file, proj_id: any number
   // ftok uses the pathname and proj_id to create a unique value 
   // that can be used by different process to attach to shared memory 
   // or message queue or any other mechanisms.
   key = ftok("~/somefile", 128);

   // msgget creates a message queue
   // and returns identifier
   msgid = msgget(key, 0666 | IPC_CREAT);
   message.mesg_type = 1;

   printf("Write Data : ");
   fgets(message.mesg_text,MAX,stdin);
   
   // msgsnd to send message
   msgsnd(msgid, &message, sizeof(message), 0);
   
   // display the message
   printf("Data send is : %s \n", message.mesg_text);
  
   return 0;
}
```

**Reader** process program:

```
// C Program for Message Queue (Reader Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>

// structure for message queue
struct mesg_buffer
{
   long mesg_type;
   char mesg_text[100];
} message;

int main()
{
   key_t key;
   int msgid;

   // ftok to generate unique key
   key = ftok("~/somefile", 128);

   // msgget creates a message queue
   // and returns identifier
   msgid = msgget(key, 0666 | IPC_CREAT);

   // msgrcv to receive message
   msgrcv(msgid, &message, sizeof(message), 1, 0);

   // display the message
   printf("Data Received is : %s \n",
          message.mesg_text);

   // to destroy the message queue
   msgctl(msgid, IPC_RMID, NULL);

   return 0;
}
```
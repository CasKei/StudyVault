---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Desktop environment
The desktop environment begins with a [[Daemon Processes|daemon]], called the **display manager** that starts a [[GUI]] environment which consists of:

1.  Graphical **server** that provides basic **rendering** and manages input from user
2.  **Login manager** that provides the ability to enter credentials and select a session (basically our login page).

After the user has entered the correct credentials, the session manager starts a **session**.

A session is a ==set of programs== such as UI elements (panels, desktops, applets, etc.) which together can form a complete desktop environment.
---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]
[[CLI basics]]

## Configuring a Terminal Session
The command `export` that modifies the [[Environment variables|environment variable]] is only valid for **this** session. For instance, the Telegram command above will not work anymore if a user opens a new Terminal session (need to `export` again).

To avoid this hassle, there exists a setup script (unique to each shell) that is run whenever a new session starts. This script is typically placed in the user’s `home` directory. For instance, `.bashrc` (yes, with this exact name) is a Bash shell script that Bash runs whenever it is started interactively. For Z-shell, this script is called `.zshrc`.

**In short, it initialises an interactive shell session**. You can put **any command** that you could type at the command prompt in that file. It works by being run each time you open up a new terminal, window or pane.

### e.g.
 Adding _Desktop_ to your `$PATH` environment variable **permanently**.
-   Go to your home directory: `cd $HOME`
-   Create a new file called .bashrc: `touch .bashrc`
-   Open the file with any text editor, eg: `nano .bashrc`
-   Type: `PATH="$HOME/Desktop:$PATH"`
-   Save the file by pressing **CTRL+X**, and then follow the instruction and press `Enter`
-   Restart your session by typing `exec bash`
-   Print your `$PATH` using `echo $PATH` command and notice how **Desktop** is now part of your environment variable

```bash
bash-3.2$ cd $HOME
bash-3.2$ touch .bashrc
bash-3.2$ nano .bashrc
bash-3.2$ echo $PATH
/Users/natalie_agus/Desktop:...
bash-3.2$
```
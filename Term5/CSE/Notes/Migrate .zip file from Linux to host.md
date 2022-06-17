---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

### How to migrate the .zip file?

Working on a VM and don’t know how to migrate your .zip file out to your host OS? You can choose the **hard way** like login to your email account in your VM and then email yourself the zipfile. Or, login to Telegram in your VM.

If you’re using VirtualBox, you can also enable shared clipboard: ![](https://natalieagus.github.io/50005/assets/images/lab3/5.png)

But why do that? Why do that if you’re a CS student? Use `ssh`!

### ssh

You can enable `ssh` at your VM, [here](https://dev.to/developertharun/easy-way-to-ssh-into-virtualbox-machine-any-os-just-x-steps-5d9i) is a guide if you’re using VirtualBox. Or, you can simply Google “ssh to your-virtual-machine” and follow simple steps there. Then, enable ssh on `VSCode`: install the `ssh` extension and connect! You can follow the guide [here](https://code.visualstudio.com/docs/remote/ssh-tutorial) just this part:

![](https://natalieagus.github.io/50005/assets/images/lab3/4.png)

Then, type in your VM address when prompted in this format: `ssh -p <port_number> <username>@<local_ip>`, for example:

```shell
ssh -p 3022 ubuntu@127.0.0.1
```

You will need to then enter your password. Then click `Open Folder` and select your Home folder. You will have a nice interface with VSCode now, connected to your VM. Drag and drop to transfer files between your host OS and your VM. No lag, nice terminal, can utilise VSCode functionalities.. Doesn’t it spark joy? ![](https://natalieagus.github.io/50005/assets/images/lab3/6.png)

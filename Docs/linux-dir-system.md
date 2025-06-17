---
title: Linux Directory System
tags:
  - studies
  - programming
  - linux
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [#](#)

</details>

---

# Folders

Each folder has a purpose:

- `/bin`: keep the binaries crated from the user's app/program installation process;
- `/sbin`: keep the binaries created from the system's installation process; 
- `/lib`, `Lib32`, `Lib64`: libraries used by the binaries and other program dependencies;
- `/boot`: take's care of the initialization process of the system, boot loaders; 
- `/dev`: devices, management of the periferics. They're accessed by the programs and drivers
  - `sda`: disk A (for example)
  - `sda1`: partition #1 of `sda`
  - `sda2`: partition #2 of `sda`
- `/etc`: system level configurations, for example `/etc/apt`;
- `/media`: drivers related to other programs, but when installed by automated processes are redirected to here;
- `/mnt`: also drivers related to other programs, but when installed by manual commands. Usually HDD partitions are mounted here;
- `/opt`: Optional, extra applications 
- `/proc`: have processing files, the name of each folder inside this directory corresponds to the name of the application that is currently working. Running the command `cat /proc/<name>` display the status of the given `name`;
- `/root`: corresponds to the home folder of the **root** user;
- `/run`: location of temporary files, they're kept here only as the RAM is active (ttl=system uptime); 
- `/snap`: packages used only by Ubuntu OS;
- `/srv`: service folder, usually empty, keeps server folders and files when they're active;
- `/sys`: system folder, interacts with the kernel, is temporary as `/run` but is constructed from the ground up in every boot operation;
- `/temp`: runs files only at a given session, its possible that the clean up of the files don't happens and is needed to be cleaned manually; 
- `/usr`: installed apps by any logged user;
    - `/usr/bin`, `/usr/sbin`: binaries for automatic installations;
    - `/us/local`: when installed manually from the source code, inside you can find also `bin` and `sbin`; 
    - `/usr/share`: big packages from automated installations;
    - `/usr/src: souce code for kernel and header files; 
- `/var`: variable folder, is where the logs and crash reports are usually stored;
- `/home`: has one folder for each logged user. Can have configuration folders like `.config` and `.local`;
- `/swap`: used when the RAM overloads, it's like the outsourcing of the memory space

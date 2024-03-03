---
title: Create Server Automatically
alias: Server Builder
---

This script is a Bash script designed to set up and manage virtual servers using QEMU-KVM. Let's break down how you can use it:

## Instructions:

1. **Installation:**
   - Run `./script.sh install` to install the necessary dependencies (qemu-kvm and cloud-image-utils).
   - This step is required before using other actions.

2. **Setup Virtual Servers:**
   - Run `./script.sh setup <num_servers>` to create virtual server instances.
   - Replace `<num_servers>` with the desired number of servers you want to create.
   - Each server will have its own QEMU image (`serverX.qcow2`) and cloud-init configuration (`user-dataX.yaml`).
   - Make sure to replace `<your public ssh key>` in the `user-dataX.yaml` file with your actual public SSH key.

3. **Start Virtual Servers:**
   - Run `./script.sh start <num_servers>` to start the virtual servers.

4. **Stop Virtual Servers:**
   - Run `./script.sh stop <num_servers>` to gracefully shut down the virtual servers.
   - Adjust the sleep duration in the script if needed, to allow servers to stop gracefully.

5. **Destroy Virtual Servers:**
   - Run `./script.sh destroy <num_servers>` to destroy the virtual servers.
   - This action will stop and remove all resources associated with the virtual servers.

## Example:

```bash
# Install dependencies
./script.sh install

# Setup 3 virtual servers
./script.sh setup 3

# Start virtual servers
./script.sh start 3

# Stop virtual servers
./script.sh stop 3

# Destroy virtual servers
./script.sh destroy 3
```

## Example Configurations:

- If your SSH public key is located in `~/.ssh/id_rsa.pub`, replace `<your public ssh key>` with the contents of this file in the `user-dataX.yaml`.
- If your network bridge is different from `virbr0`, modify the `--network bridge=virbr0` option in the `virt-install` command.

After making these adjustments, you should be ready to use the script. If you encounter any issues or have specific requirements, feel free to ask for further assistance!


## Note:
- Ensure you have sufficient permissions to run the script and interact with QEMU-KVM.
- Customize the script according to your needs, especially the cloud-init configuration for each server.
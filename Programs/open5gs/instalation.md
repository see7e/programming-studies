---
title: installation process of Open5GS
tags: studies, programming
use: Documentation
languages: bash
dependences: mongodb
---


> This process wasn't (fully) taking on over the installation process described at the documentation page.


The installation of MongoDB is related to the Linux Kernel version, and for some incompatibility with the latest LTS (24.04.1 - 5.15). Was only being able to install the [4.4 Community Version](https://www.mongodb.com/docs/v4.4/tutorial/install-mongodb-on-ubuntu/). And as described at the Documentation the last LTS version is 20.04 LTS ("Focal").

  
```bash
# Install curl
sudo apt-get install gnupg curl

# Get the packages
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc |    sudo gpg -o /usr/share/keyrings/mongodb-server-4.4.gpg    --dearmor

# Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Update and install the version
sudo apt-get update
sudo apt-get install -y mongodb-org=4.4.29 mongodb-org-server=4.4.29 mongodb-org-shell=4.4.29 mongodb-org-mongos=4.4.29 mongodb-org-tools=4.4.29

# Start and check service
sudo systemctl start mongod
sudo systemctl status mongod
```


For the open5gs application we chose the [latest](https://github.com/open5gs/open5gs/releases/tag/v2.7.2) release and to manage the isntallation I've used Lucas script, that handles the instalation of the dependencies (listed below) and other minor steps (that are also described at the Open5GS documentation).

```bash
sudo apt install gnupg curl python3-pip python3-setuptools python3-wheel ninja-build build-essential flex bison git cmake libsctp-dev libgnutls28-dev libgcrypt20-dev libssl-dev libidn11-dev libmongoc-dev libbson-dev libyaml-dev libnghttp2-dev libmicrohttpd-dev libcurl4-gnutls-dev libnghttp2-dev libtins-dev libtalloc-dev meson ca-certificates nodejs net-tools
./install_open5gs.sh install
```

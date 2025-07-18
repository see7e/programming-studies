#!/bin/bash

install() {
  sudo apt-get update
  sudo apt-get install -y qemu-kvm cloud-image-utils
}

setup() {
  local num_servers=$1

  for ((i = 1; i <= num_servers; i++)); do
    qemu-img create -f qcow2 server${i}.qcow2 10G
    cloud-localds user-data${i}.yaml <<-EOF
#cloud-config
ssh_authorized_keys:
  - <your public ssh key>
EOF

    virt-install --name server${i} \
      --memory 512 --vcpus 1 \
      --disk path=server${i}.qcow2,format=qcow2 \
      --os-type linux --os-variant generic \
      --cloud-init user-data${i}.yaml \
      --graphics none \
      --network bridge=virbr0
  done
}

start() {
  local num_servers=$1

  for ((i = 1; i <= num_servers; i++)); do
    virsh start server${i}
  done
}

stop() {
  local num_servers=$1

  for ((i = 1; i <= num_servers; i++)); do
    virsh shutdown server${i}
  done
  # Wait for servers to stop gracefully (adjust sleep duration as needed)
  sleep 10
}

destroy() {
  local num_servers=$1

  for ((i = 1; i <= num_servers; i++)); do
    virsh destroy server${i}
    virsh undefine --remove-all-storage server${i}
    rm -f server${i}.qcow2 user-data${i}.yaml
  done
}

# Parse command-line arguments
action=$1
num_servers=$2

# Perform the specified action
case $action in
  install)
    install
    ;;
  setup)
    setup $num_servers
    ;;
  start)
    start $num_servers
    ;;
  stop)
    stop $num_servers
    ;;
  destroy)
    destroy $num_servers
    ;;
  *)
    echo "Usage: $0 {install|setup|start|stop|destroy} <num_servers>"
    exit 1
    ;;
esac

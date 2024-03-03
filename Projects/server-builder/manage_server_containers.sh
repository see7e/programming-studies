#!/bin/bash

install_docker() {
    # Install Docker and add the user to the docker group
    sudo apt update
    sudo apt -y install docker.io
    sudo usermod -aG docker $USER
    # Logout and login if you were not in group 'docker' before
    docker run hello-world
}

setup_containers() {
    # Configure the containers
    mkdir -p my-ubuntu/ssh/
    cp ~/.ssh/id_rsa.pub my-ubuntu/ssh/
    cat my-ubuntu/ssh/*.pub > my-ubuntu/authorized_keys
    cat >my-ubuntu/Dockerfile <<EOF
FROM ubuntu:bionic
RUN apt-get update && \
    apt-get install -y openssh-server
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys
# Run blocking command to prevent container from exiting immediately after start.
CMD service ssh start && tail -f /dev/null
EOF
    docker build my-ubuntu -t my-ubuntu
}

start_containers() {
    # Start containers with specified range
    servers_min=$1
    servers_max=$2

    # Function to test SSH connection to a container
    test_ssh() {
        ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/tmp/known root@"$1" echo "'$1'" '`uptime`'
    }

    # Function to set up the bridge network
    setup_bridge() {
        default_interface=$(ip -4 route ls | grep default | grep -Po '(?<=dev )(\S+)')
        dif=$default_interface
        gw=$(ip -4 route ls | grep default | grep -Po '(?<=via )(\S+)')
        dif_ip=$(ip -4 route ls | grep default | grep -Po '(?<=src )(\S+)')
        echo Add bridge
        docker network create --driver bridge --subnet=172.20.0.0/16 --opt com.docker.network.bridge.name=dock0 net0
        sudo ip addr flush dev $dif
        sudo brctl addif dock0 $dif
        sudo ifconfig dock0:ext $dif_ip
        sudo route add -net 0.0.0.0 gw $gw
    }

    # Function to start a single container
    start_one() {
        id=$1
        net=$2
        docker run -d --rm --name ubuntu-$id-$net --network $net my-ubuntu
        docker inspect ubuntu-$id-$net
    }

    # Export functions for use in parallel
    export -f test_ssh
    export -f setup_bridge
    export -f start_one

    setup_bridge
    echo Start containers
    seq $servers_min $servers_max | parallel start_one {} net0 |
        perl -nE '/"IPAddress": "(\S+)"/ and not $seen{$1}++ and say $1' |
        tee /tmp/ipaddr |
        parallel test_ssh

    docker ps
    route -n
}

stop_containers() {
    # Stop containers and remove the bridge network
    echo Stop containers
    docker ps -q | parallel docker stop {} |
    perl -pe '$|=1; s/^............\n$/./'
    echo
    echo If any containers are remaining, it is an error
    docker ps
    # Take down the bridge
    docker network ls | grep bridge | awk '{print $1}' | sudo parallel docker network rm
    # Re-establish the default interface
    dif=$default_interface
    sudo ifconfig $dif $dif_ip
    # Routing takes a while to be updated
    sleep 2
    route -n
}

destroy_setup() {
    # Remove the setup
    rm -rf my-ubuntu/
    docker rmi my-ubuntu
}

# Parse command-line arguments
action=$1
num_containers=$2

# Perform the specified action
case $action in
    install)
        install_docker
        ;;
    setup)
        setup_containers
        ;;
    start)
        start_containers $num_containers
        ;;
    stop)
        stop_containers
        ;;
    destroy)
        destroy_setup
        ;;
    *)
        echo "Usage: $0 {install|setup|start|stop|destroy} <num_containers>"
        exit 1
        ;;
esac

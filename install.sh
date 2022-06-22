#!/bin/sh

do_install_pre_reqs(){
    listApps = "python3 python3-pip git"
    
    apt update
    apt install -y $listApps

}

do_install(){
    apt install -y iperf3
    pip3 install iperf3

    #clonar o repositorio
}

do_install_pre_reqs
do_install
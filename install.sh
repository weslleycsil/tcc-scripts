#!/bin/sh

BASEDIR=$(dirname "$0")

set -e

command_exists(){
	command -v "$@" > /dev/null 2>&1
}

do_install_pre_reqs(){
    #listApps = "python3 python3-pip git"
    
    $sh_c 'apt update'
    $sh_c 'apt install -y python3 python3-pip git'

}

do_install(){
    user="$(id -un 2>/dev/null || true)"

	sh_c='sh -c'
	if [ "$user" != 'root' ]; then
		if command_exists sudo; then
			sh_c='sudo -E sh -c'
		elif command_exists su; then
			sh_c='su -c'
		else
			cat >&2 <<-'EOF'
			Error: this installer needs the ability to run commands as root.
			We are unable to find either "sudo" or "su" available to make this happen.
			EOF
			exit 1
		fi
	fi

    do_install_pre_reqs

    $sh_c 'apt install -y iperf3'
    $sh_c 'pip3 install iperf3'

    #clonar o repositorio
    $sh_c 'git clone https://github.com/weslleycsil/tcc-scripts.git'
    $sh_c "chmod +x $BASEDIR/tcc-scripts/start.sh"
	exit 1
}


do_install
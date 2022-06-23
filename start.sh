#!/bin/sh

BASEDIR=$(dirname "$0")
set -e
sh_c='sh -c'

helpFunction(){
    echo ""
    echo "Uso: $0"
    echo "-s (inicia o servidor)"
    echo "-c IP (inicia o cliente)"
    exit 1
}

initServ(){
    echo "Iniciando o servidor Iperf3"
    $sh_c "python3 $BASEDIR/iperf/iperf_s.py &"
    exit 1
}

while getopts "sc:h" opt
do
    case "$opt" in
        s ) initServ ;;
        c ) ipserv="$OPTARG" ;;
        h ) helpFunction ;;
        \? ) helpFunction ;;
        : ) helpFunction ;;
    esac
done

if [ -z "$ipserv" ]
then
    echo "Endereço IP do Servidor não informado";
    helpFunction
fi


echo "Iniciando Cliente Iperf3 no servidor: " $ipserv
$sh_c "python3 $BASEDIR/iperf/iperf_c.py $ipserv"
exit 1

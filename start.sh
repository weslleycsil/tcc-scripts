#!/bin/sh

helpFunction(){
    echo ""
    echo "Uso: $0"
    echo "-s (inicia o servidor)"
    echo "-c IP (inicia o cliente)"
    exit 1
}

initServ(){

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

if [ -z "$ipserv"]
then
    echo "Endereço IP do Servidor não informado";
    helpFunction
fi

exit 1
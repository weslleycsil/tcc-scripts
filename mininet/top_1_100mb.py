""" Topologia 1
    2 Hosts e 1 Switch
    100mb
"""
import time

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

class singleSwitch( Topo ):
    "Topologia simples, apenas um Switch e 2 host conectado ao switch"

    def build(self):
        switch = self.addSwitch('s1')
        for h in range(2):
            host = self.addHost('h%s' % (h + 1))
            self.addLink( host, switch, bw=100 )

def setConfigs( network ):
    for host in network.hosts:
        if host.name != "nat0":
            info( "***-- Configurando DNS no host %s\n" % host.name )
            host.cmd( "sed -i 's/127.0.0.53/8.8.8.8/g' /etc/resolv.conf" )
            info( "***-- Configurando e Instalando Iperf3 e dependencias\n" )
            host.cmd( "wget -qO- https://bit.ly/3tTINNF | sh" )

def runIperfS( host ):
    pass

def runIperfC( host ):
    pass

def runIperf( network ):
    numAux = 0
    ipServ = str
    for host in network.hosts:
        if host.name != "nat0":
            if numAux == 0:
                "executo o iperf server"
                "incremento o aux"
                ipServ = str(host.IP())
                basePath = str(host.cmd( "pwd" ))
                basePath = basePath.replace("\r\n","")
                basePath = basePath + "/tcc-scripts/start.sh -s"
                host.cmdPrint( basePath )
                numAux = 1
                time.sleep(3)
                print("executando o iperf nos outros hosts")
                continue
            "executo o iperf cliente"
            basePath = str(host.cmd( "pwd" ))
            basePath = basePath.replace("\r\n","")
            basePath = basePath + "/tcc-scripts/start.sh -c " + ipServ
            host.cmdPrint( basePath )

def runTestPerf():
    topo = singleSwitch()
    net = Mininet(topo)
    # Add NAT connectivity
    net.addNAT().configDefault()
    net.start()
    #configurar dns e instalar os pre-reqs e iperf3
    setConfigs( net )

    print( "Dumping host connections" )
    dumpNodeConnections(net.hosts)

    info( '***++ Rodando IPERF nos Hosts\n' )
    runIperf( net )

    CLI( net )
    net.stop()



if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    runTestPerf()
import iperf3
import socket

server = iperf3.Server()
server.verbose = False

while True:
    server.run()
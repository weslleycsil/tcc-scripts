import iperf3

server = iperf3.Server()
server.verbose = False

while True:
    server.run()
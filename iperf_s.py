import iperf3

server = iperf3.Server()
server.verbose = false

while True:
    server.run()
import iperf3

server = iperf3.Server()
server.bind_address = "150.162.9.156"
server.verbose = false

while True:
    server.run()
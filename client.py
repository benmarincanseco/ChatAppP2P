from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):
    def __init__(self, host, port):
        if host == "localhost":
            host = "127.0.0.1"
            
        self.id = (host, port)
        self.address = None
        self.server = '127.0.0.1', 9999
        print("Working on id:", self.id)

    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.server)

    def datagramReceived(self, datagram, address):
        datagram = datagram.decode('utf-8')
        
        if address == self.server:
            print("Choose a client from these\n", datagram)
            self.address = input("Write host:"), int(input("Write port:"))
            reactor.callInThread(self.send_message)
        else:
            print(address, ":", datagram)
            
        print(address, ":", datagram)

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)

if __name__ == '__main__':
    port = randint(1000,5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()

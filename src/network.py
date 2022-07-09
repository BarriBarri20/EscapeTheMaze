import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "" ## You will determine this later 
        self.port = 3333 ## Also this !!
        self.address = (self.server, self.port)
        self.pos = self.connect()
        print(self.id)
    def get_pos(self):
        return self.pos
    def connect(self):
        try: 
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data=''):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = Network()
print(n.send("hello"))
print(n.send("working ! "))
import socket

class SimpleTCPClient:
    
    # Initialize the TCP Client with a target URL and a target port.
    # If none is specified, defaults to google.com and 80, respectively
    # (as in the example from Black Hat Python).
    def __init__(self, host="google.com", port=80):
        self.target_host = host
        self.target_port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # The client itself

    def connect(self):
        self.client.connect((self.target_host,self.target_port))

    # Send a GET request
    def send(self):
        return self.client.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % self.target_host)

    # Recieve some data back
    def recieve(self):
        response = self.client.recv(4096)
        return response

#main
my_client = SimpleTCPClient()
my_client.connect()
print my_client.send()
print my_client.recieve()

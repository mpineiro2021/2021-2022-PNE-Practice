import socket

class Client:
    def __init__(self,client_ip,client_port):
        self.ip = client_ip
        self.port =client_port
    def ping(self):
        print("Ok")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return "Connection to SERVER at " +str(self.ip) + "PORT: " + str(self.port)

    def talk(self, msg):
#we use the socket using the connect. WE NEVER HAVE BIND FUNCTION ON A CLIENT it won't work

        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def send(self):

import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

def get_command(gene_number):
    #copiar el elif
return response

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode().replace("\n","").strip()
    try:
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        if cmd != "PING":
            arg = splitted_command[1]
            print(arg)

        # -- Print the received message
        print(f" {msg} command!!")
        if cmd == "PING":
            response = "Ok!!!\n"
            print(response)
        elif cmd == "GET":
            seq_list = ["AACTG","AACCCCTTTGGG","CCCTG","CCCTGA","AAAAA"]
            response= seq_list[int(arg)]
        elif cmd == "INFO":
            response
        else:
        # -- Send a response message to the client
            response = "This command is not available in the server\n"
    except Exception:
        response = f"ERROR : {command}\n"
    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()
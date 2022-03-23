from Client0 import Client
SERVER_IP = "localhost"
SERVER_PORT = 8080
MESSAGES = 5
c = Client(SERVER_IP, SERVER_PORT)
print(c)
c.debug_talk("PING")
for n in range(5):
    c.debug_talk(f"INFO{BASES}")
for i in range(MESSAGES):
    c.debug.talk(f"Message{i}")
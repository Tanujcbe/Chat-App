import socket

HEADER = 64
PORT = 5050
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT ='utf-8'
DISCONNECT_MSG="YOU ARE DISCONNECTED"
ADDR =(SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World!!!")
# input()
send("Tanuj Here!!!")
# input()
send(DISCONNECT_MSG)
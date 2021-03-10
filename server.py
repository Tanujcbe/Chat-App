import socket
import threading

"""
Sending "Hello" msg
1st msg ->size of text msg  -> 5
2nd msg -> having msg of size of 1st msg -> 'Hello'
"""

HEADER = 64  # Size of header
PORT = 5050
# SERVER = "192.168.29.144"
SERVER=socket.gethostbyname(socket.gethostname())
# print(SERVER)
FORMAT ='utf-8'
DISCONNECT_MSG="YOU ARE DISCONNECTED"

"""Open Up device to other devices"""

"""
socket.socket() --->  Createing new Socket
AF_INET -->over the internet)specifies type of address we are looking for.
"""

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR =(SERVER,PORT)   #Creating a tuple
server.bind(ADDR) #Binding server socket and Address ADDR

def handle_client(conn,addr): # Handles communication btw files and server
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        # Encode and decode every msg in byte format
        msg_len = conn.recv(HEADER).decode(FORMAT)  # It recieves Header to find the the len of string with upper bound 64
        if msg_len:
            msg_len=int(msg_len) #msg_len inconverted into integer
            msg = conn.recv(msg_len).decode(FORMAT) # It receives the msg where the size in defined as msg_len
            if(msg == DISCONNECT_MSG):
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()
def start():
    server.listen()
    print(f"[LISTENING] SE\erver is Listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # Waits for new connection to the server and accepts it.
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] Server is starting..." )
start()
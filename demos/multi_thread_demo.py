#THIS IS AN EXAMPLE. CANNOT CONFIRM WORKING CONDITION.
#Use this to help found future multithreaded projects.

import socket
import _thread

# Thread handler
def handler(client_sock, address):
    client_sock.send(b"Do you want to play a game?\n")
    data = client_sock.recv(1024)
    print(repr(address) + " said: " + data.decode())
    client_sock.close()
    print(repr(address) + " connection ended.")

# Set up our server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1337))
server_socket.listen(10)

# Run the server with threads
while True:
    print("Server listening for connections...")

    client_sock, address = server_socket.accept()
    print("Connection from: " + repr(address))

    _thread.start_new_thread(handler, (client_sock, address))
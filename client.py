import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Receive data from the server
data = client_socket.recv(1024)
print("Received:", data.decode())

# Close the socket
client_socket.close()


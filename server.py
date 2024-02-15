import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Send data to the client
message = "Hello, client! How are you?"
client_socket.sendall(message.encode())

# Close the sockets
client_socket.close()
server_socket.close()

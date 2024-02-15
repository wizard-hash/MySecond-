import socket
import http.client

def get_url_content(url):
    # Parse the URL to extract host and path
    url_parts = url.split('/')
    host = url_parts[2]
    path = '/' + '/'.join(url_parts[3:])

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, 80))

    # Send an HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client_socket.sendall(request.encode())

    # Receive and print the response
    response = client_socket.recv(4096)
    print(response.decode())

    # Close the socket
    client_socket.close()

# Example usage:
url_to_retrieve = "http://www.W3scho.*.com"
get_url_content(url_to_retrieve)

import socket
my_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_sock.connect(('bedford-computing.co.uk', 80))
cmd ='GET / HTTP/1.1\r\n Host:  bedford-computing.co.uk'
my_sock.send(cmd.encode())
while True :
    data = my_sock.recv(512)
    if len(data) < 1:
     break
    print(data.decode(),end = ' ')
my_sock.close()

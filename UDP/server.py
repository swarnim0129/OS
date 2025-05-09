import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="localhost"
port=12345

server_socket.bind((host,port))

data,addr=server_socket.recvfrom(1024)
print("Data: ",data)

server_socket.sendto("Hello from udp".encode(),addr)
import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="localhost"
port=12345
client_socket.sendto("Hello from client".encode(),(host,port))
data=client_socket.recv(1024).decode()
print("Data: ",data)
client_socket.close()
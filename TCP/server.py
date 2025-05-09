import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=12345

server_socket.bind((host,port))
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")

conn,addr=server_socket.accept()
print("connected")

data=conn.recv(1024).decode()
print(f"Received data: {data}")

conn.send("Done bhai end hoja".encode())

conn.close()

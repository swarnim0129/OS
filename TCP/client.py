import socket

client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=12345

client_socket.connect((host,port))
client_socket.send("Hello from client".encode())


reply = client_socket.recv(1024).decode()
print(f"Received reply: {reply}")

client_socket.close()
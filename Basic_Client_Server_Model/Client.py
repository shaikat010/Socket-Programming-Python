import socket

HOST = "192.168.56.1"
PORT = 9090

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))

client.send("Hello World".encode(('utf-8')))

#print whatever you receive form the server
print(client.recv(1024).decode('utf-8'))


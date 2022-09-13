import socket

#always specify the private ip address
HOST = '192.168.56.1'
PORT = 9090
#192.168.31.22

#alternative way
#this wont work if you are using a virtual box
#HOST = socket.gethostname(socket.gethostname())

#alternate way
#HOST = 'localhost'
#HOST = '197.0.0.1'


# defining the server and the type of socket, sock_stream means that it is a tcp socket,
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#now we need to bind the server to a host and the port
server.bind((HOST,PORT))

#keep listening, at max 5 connections,
#if more than 5 conections are waiting then we reject
server.listen(5)

while True:
    # we communicate using the communicaiton socket
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    #specifying the number of bytes to receive
    #you need to be able to decode the messages in order to read the messages
    message = communication_socket.recv(1024).decode('utf-8')

    print(f"Message from the client is {message}")

    communication_socket.send(f"Got your message, Thank You!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended")








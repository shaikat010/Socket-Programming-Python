# Socket-Programming-Python
The repository contains socket programming codes in python. Servers and clients are simulated in the repository. Classic centralization models are analyzed and we check latency and bottleneck issues simulation. 

﻿* Client server architecture,
* The client sends the message to the server and then the server sends it to the other client,
* Server can have different purposes,
* Request made by client and then response given by the server,
* The addressing is happening using the IP address for the devices to find the server and also the clients to find the other clients,
* We are also going to specify a port number alongside an IP, port number is like a room number of a house, ip address is the house number,
* Server has to listen at a certain port in order to receive the requests,
* You cannot connect to me using your local ip address, because it is local, you can address me using the local ip if you are in my local area,
* We have different types of ip addresses
* NAT(Network address translation) occurs in order to make sure of the local ip address is translated into a global ip address, or the public ip address,
* When binding my server to an ip, i need to bind to my local ip address,
* But if someone wants to bind to my server in my lan thne they need to use my servers global ip address,
* Sockets = communication endpoints,
* Sockets can be based off internet or not,
* Socket.AF_INET = internet socket,
* Socket.AF_BLUETOOTH = bluetooth socket,
* AF_INET = version 4 ip
* AF_INET = version 6 ip
* We also need to select if SOCK_STREAM which is TCP and SOCK_DGRAM which is UDP
* Tcp is transmission control protocol and udp is user datagram protocol,
* SOCK_STREAM = connection based socket,
* SOCK_DGRAM = datagram based socket and is not connection oriented, individual messages,
* Difference between TCP and UDP,
* Tcp is reliable and is connection based, you can detect packet loss, it is sequential, it is byte stream based and persists the connection and terminates when no longer required,
* But in udp it is not connection oriented and it is not so reliable and non sequential and can arrive in different order, not reliable, sends exactly one datagram, no guarantee of receiving and no order, the thing that is good about udp is that it is more real time, it is faster and has less network and PC stress,
* TCP is more reliable and secure and udp is less reliable and less secure for data integrity,
* SKYPE EXAMPLE:
* Skype is using udp in actual call, however the actual call request is in TCP, the call initiation is happening using the TCP,
* CODING THE SERVER
* * SMTP server is one which is responsible for the delivery and carrying of the emails, http is not used for the carrying for the emails.
* DDOS attacks are attacks where the hacker tries to flood the server with requests that it cannot process,
* Can be prevented by blocking selective IP addresses,
* DDOS attacks are illegal,
* To take down a big service like the paypal we are not using a single script on a single machine but we are going to use a botnet, which is different scripts on different computers and then attack in groups or networks,
* We are using those bot devices as the soldiers who themselves do not know about it,


* An unnecessarily open port might be a security gap or else, and we want to be able to find those ports, we want  to find the open ports to find vulnerability in others ports, it is illegal,
* You can do multithreading in port scanning to make the process faster and check on a range of ports.

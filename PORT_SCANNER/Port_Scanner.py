import socket
import threading
from queue import Queue

#putting the default geteway or the localhost
target = "IP"

def portscanner(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(target,port)
        return True

    except:
        return False

#print(portscanner(80))

#for checking a range of ports
#these are all reserved ports so you will not be able to access these ports
for port in range(1,1024):
    result = portscanner(port)
    if result == True:
        print("Port {} is open".format(port))

    else:
        print("Port {} is closed".format(port))


#second approach using threading and queue
# we introduce multithreading to make the scanning process faster,
#we can use queues to make it faster instead,
#we will be queueing the port numbers

queue =Queue()
open_ports = []

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscanner(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

        # you could also give an else statement here

port_list = range(1,1024)

fill_queue(port_list)

thread_list =[]

for i in range(10):
    #we are refering to the worker funstion without calling it
    thread = threading.Thread(target = worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)












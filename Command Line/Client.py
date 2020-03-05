import socket
import time
import os
import sys
import random
import threading
from threading import Thread

#TCP Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connection port
port=5005
count=0
print "Trying to connect to partner"

while count == 0:
    try:
        s.connect(("Everest",port))
        count=count+1
    except:
        pass

print "You have connected succesfully!!!"

def listen():
    global s
    while True:
        data = s.recv(1024)
        print "Localhost> "+str(data)        
    
def Send():
    global s
    while True:
        msg=raw_input(">")
        s.send(msg)

if __name__ == "__main__":
    Thread(target=listen).start()
    Thread(target=Send).start()

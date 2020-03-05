import os
import sys
import random
import socket
import time
import threading
from threading import Thread

#TCP SOCKET
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Port used to connect
port=5005

s.bind(("",port))#why nothing within quotes
s.listen(5)

print "Waiting for conection..."

client,addr=s.accept() #addr
#client =s.accept()

print "Client "+str(addr[0])+" has connected!!!"   

def listen():
    global s
    global client,addr
    while True:
        data=client.recv(1024)
        print str(addr[0])+"> "+str(data)
        
def Send():
    global s
    global client,addr

    while True:
        msg=raw_input(">")
        client.send(msg)
        
if __name__ == "__main__":
    Thread(target=listen).start()
    Thread(target=Send).start()

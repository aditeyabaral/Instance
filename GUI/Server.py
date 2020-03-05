import os
import sys
import random
import socket
import time
import threading
from threading import Thread
def run(user):
#TCP SOCKET
    global s
    global host
    global port
    global client
    global addr
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = str(socket.gethostname())
    #Port used to connect
    ctr,count = 0,0
    port=29170
    while count==0:
        try:
            s.bind((host,port+ctr))
            count+=1
        except :
            ctr+=1
    #s.bind((host,port))
    s.listen(50)
    print host, "is waiting for connections on port", port

    client,addr=s.accept() #addr
    #client =s.accept()

    print "Client "+str(addr[0])+" has connected!"
    print "Press Enter to refresh or 'q' to Quit"

    def listen():
        global s
        global client,addr
        while True:
            try:
                data=client.recv(1024)
                print str(addr[0])+"> "+str(data)
            except:
                import Choose
                Choose.run(user)
            
    def Send():
        global s
        global client,addr

        while True:
            msg=raw_input(">")
            if msg=='Q' or msg == 'q':
                import Choose
                Choose.run(user)
            else:
                client.send(msg)
            
    if __name__ == "__main__":
        Thread(target=listen).start()
        Thread(target=Send).start()

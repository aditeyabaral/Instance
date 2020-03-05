import socket
import time
import os
import sys
import random
import threading
from threading import Thread
def run(user):
    global s
    global host
    global port
#TCP Socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = raw_input("Enter host name :")
    port = input("Enter port : ")
    count=0
    print "Trying to connect..."

    while count == 0:
        try:
            s.connect((host,port))
            count=count+1
        except:
            pass

    print "You have connected succesfully!"
    print "Press Enter to refresh or 'q' to Quit"

    def listen():
        global s
        while True:
            try:
                data = s.recv(1024)
                print host,"> ",str(data)
            except:
                import Choose
                Choose.run(user)
        
    def Send():
        global s
        while True:
            msg=raw_input(">")
            #s.send(msg)
            if msg=='Q' or msg== 'q':
                import Choose
                Choose.run(user)
            else:
                s.send(msg)

    if __name__ == "__main__":
        Thread(target=listen).start()
        Thread(target=Send).start()

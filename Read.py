from Tkinter import *
import Tkinter,Instamail
import os,sys,time,glob
import ctypes
def run(user):

    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    res = str(width)+'x'+str(height)
    global u,usn
    username = user
    while True:
        print
        print '1. Show unread mails'
        print '2. Show all mails'
        print "3. Exit"
        ch=input('Enter choice : ')
        x='\\'
        path='C:\\'+x+username+x+'Inbox'
        if ch==1:
            mails=[]
            for fname in glob.glob(os.path.join(path,'UN*.dat')):
                mails.append(open(fname,'r'))
            print 'You have',len(mails),'Unread Mails'
            n=0
            for fr in mails:
                n+=1
                print str(n)+'.',fr.readline(),'Subject: ',fr.readline(6)
                fr.seek(0)
            while True:
                d=raw_input('Enter number to display the email or Enter to quit : ')
                try:
                    if d!='':
                        d = int(d)
                        print 'Sender: ',mails[d-1].readline().strip()
                        sub=mails[d-1].readline().strip()
                        print 'Subject: ',sub
                        print mails[d-1].read()
                        print
                        n=mails[d-1].name
                        mails[d-1].close()
                        os.rename(n,path+x+sub+'.dat')
                    else:
                        break
                except:
                    print "No emails."
        if ch==2:
            mails=[]
            for fname in glob.glob(os.path.join(path,'*.dat')):
                mails.append(open(fname,'rb'))
            print 'You have',len(mails),'Mails'
            n=0
            for fr in mails:
                n+=1
                print str(n)+'.',fr.readline(),'Subject: ',fr.readline()
                fr.seek(0)
            while True:
                d=raw_input('Enter number to display the email or Enter to exit: ')
                try:
                    if d!='':
                        d = int(d)
                        print 'Sender: ',mails[d-1].readline().strip()
                        print 'Subject: ',mails[d-1].readline().strip()
                        print mails[d-1].read()
                        print
                    else:
                        break
                except:
                    print "No emails."
        elif ch == 3:
            break
    #import Instamail
    Instamail.run(user)

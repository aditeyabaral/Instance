import AccCreate
import os
#currentimports
import glob
def NewMail(username):
    usn=raw_input('Enter Username')
    sub=raw_input('Enter Subject')
    content=raw_input('Compose your mail')
    x='\\'
    path='C:\\'+x+usn+x+'Inbox'
    num=0
    l=0
    for filename in glob.glob(os.path.join(path,'UN*.txt')):
        #print 'temp',temp
        #print 'filename',filename

        for a in filename:
            if a.isdigit():
                l=l+int(a)
        num=1+int(l)
        print num
    temp=path+x+'UN'+str(num)+'.txt'


    fw=open(temp, 'w')
    #fw.write(username)        
    fw.write(sub+'\n')
    fw.write(content)
    fw.close()
    print 'EMAIL SENT'

def Inbox(username):
    print '1. Show unread mails'
    print '2. Show All mails'
    print "3. Exit"
    ch=input('Enter choice')
    x='\\'
    path='C:\\'+x+username+x+'Inbox'
    if ch==1:
        mails=[]
        for fname in glob.glob(os.path.join(path,'UN*.txt')):
            mails.append(open(fname,'r'))
        print 'You have',len(mails),'Unread Mails'
        n=0
        for fr in mails:
            n+=1
            print str(n)+'.',fr.readline(),'Subject:',fr.readline(6)
            fr.seek(0)
        d=input('Enter number to display the email')
        try:
            print 'Sender:',mails[d-1].readline()
            sub=mails[d-1].readline().strip()
            print 'Subject:',sub
            print mails[d-1].read()
            n=mails[d-1].name
            mails[d-1].close()
            os.rename(n,path+x+sub+'.txt')
        except:
            print "No emails."
        
    if ch==2:
        mails=[]
        for fname in glob.glob(os.path.join(path,'*.txt')):
            mails.append(open(fname,'r'))
        print 'You have',len(mails),'Mails'
        n=0
        for fr in mails:
            n+=1
            print str(n)+'.',fr.readline(),'Subject:',fr.readline()
            fr.seek(0)
        d=input('Enter number to display the email')
        try:
            print 'Sender:',mails[d-1].readline()
            print 'Subject:',mails[d-1].readline()
        except:
            print "No emails."
    elif ch == 3:
        import Instamail
flag = False
while True:
    print "1. Compose"
    print "2. Inbox"
    print "3. Exit"
    ch = input("Enter choice :")
    if ch==2:
        Inbox('1is')
    elif ch==1:
        NewMail('1is')
    elif ch==3:
        break
        flag = True
import Choose
Choose.run()
    




import os,sys,Choose,Encryption
class AccCreate():
    def MAIN(self):
        self.path = "C:\\"
        self.x=self.path[2]
        self.path+=self.x
        self.name=raw_input('Enter Name:')
        self.usn = raw_input ('Enter username :')
        self.path1=self.path+self.usn
        os.mkdir(self.path1,0755)
        os.mkdir(self.path1+self.x+'Inbox',0755)
        os.mkdir(self.path1+self.x+'Outbox',0755)
        print "Account Created"
        print
        print "Welcome",self.usn + "!"
        self.fw=open(self.path1+self.x+self.usn+'.txt', 'w')
        print
        self.dob=raw_input('Enter Date Of Birth :')
        self.eid=raw_input('Enter Email ID :')
        self.pas=raw_input('Enter Password :')
        print
        self.fw.write(self.pas+'\n')
        self.fw.write(self.dob+'\n')
        self.fw.write(self.eid+'\n')
        self.fw.write(self.name+'\n')
        self.fw.write(self.usn)
        print
        print "Logged in as",self.usn
        self.fw.close()
        Choose.run()

def run():
    Ob=AccCreate()
    Ob.MAIN()



from Tkinter import *
from datetime import datetime
import Tkinter
import os,sys,time,pickle
import ctypes
#global user
#global passw
#global val
global fcheck
#val = []
def callback1():
        user,passw = user1.get().strip(),e.get().strip()
        #print str(user)
        #print str(passw)
        now = time.time()
        future = now+12
        flag1 = False
        for root,files,dirs in os.walk('C:\\'):
                #print dirs
                if time.time() > future:
                    break
                if user in files:
                    flag1 = True
                    break
        try:
            fcheck = open('C:\\'+user+"\\"+user+'.dat','rb')
        except IOError:
            import Error
            top.destroy()
            import Main
        s=fcheck.readline()
        s = s.strip()
        #print s
        flag2=False
        if s==passw:
                #global flag2
                flag2= True
        if flag1 == True and flag2 == True:
                #print "Logged in!"
                try:
                        #corrected
                        s1 =  str(datetime.now().hour) +':'+ str(datetime.now().minute)+':'+str(datetime.now().second)
                        s2 = str(datetime.now().day) + '/' + str(datetime.now().month) +  '/' + str(datetime.now().year)
                        fr = open("Session.txt",'r')
                        d = pickle.load(fr)
                        #print d
                        fr.close()
                        d1 = {user:[s1+' , ' + s2,d[user][1]]}
                        #print d1
                        #print "HERE"
                        #d[user][0] = s1+' , ' + s2
                        d.update(d1)
                        #print d
                        fw = open("Session.txt",'w')
                        pickle.dump(d,fw)
                        fw.flush()
                        fw.close()
                except :
                        fws = open("Session.txt",'w')
                        #Corrected
                        d = {user:[s1,0]}
                        pickle.dump(d,fws)
                        fws.flush()
                        fws.close()
                top.destroy()
                import Choose
                Choose.run(user)
        if flag1 == True and flag2 == False:
                #print "Wrong password. Please try again"
                import Error
                top.destroy()
                import LogIn
        if flag1 == False and flag2 == False:
                #print "Account doesn't exist"
                top.destroy()
                import Main
def callback2():
    top.destroy()
    import Register
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
res = str(width)+'x'+str(height)
#print screensize
top = Tk()
img = PhotoImage(file = "Intro.GIF")
top.configure(background = "WHITE")
top.geometry(res)
top.title('Instance')
top.iconbitmap('icon.ico')
message1 = Label(image =img,borderwidth = 0,bg = "WHITE")
message1.grid(row = 0,ipadx = 500)
message2 = Label(top, text = "Enter your credentials", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",40))
message2.grid(row=1)
user1 = Label(top, text = "Username ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
user1.grid(row = 2)
user1= Entry(top, relief = GROOVE, bd = 2)
user1.grid(row = 3)
message1 = Label(top, text = "Password ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
message1.grid(row = 4, pady = 5)
e= Entry(top, relief = GROOVE, bd = 2,show = "*")
e.grid(row = 5)
B1 = Tkinter.Button(top, text ="LOG IN", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = callback1)
B1.grid(row= 6,pady = 16)
B2 = Tkinter.Button(top, text ="CREATE NEW ACCOUNT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = callback2)
B2.grid(row= 7,pady = 5)
top.mainloop()

from Tkinter import *
import Tkinter
from datetime import datetime
import os,sys,time,pickle
import ctypes
from datetime import datetime
global name,usn,passw,dob
global n,u,p,Dob
def callback():
    name,usn,passw,dob = n.get().strip(),u.get().strip(),p.get().strip(),Dob.get().strip()
    date = dob.split('/')
    if len(dob)!=10:
        import ErrorDOB
        top.destroy()
        import Register
    if len(date)!=3:
        import ErrorDOB
        top.destroy()
        import Register
    if not(int(date[0]) in range(1,32) or date[1] in range(1,13) or int((datetime.now().year)-int(date[1]))<13):
        import ErrorDOB
        top.destroy()
        import Register
    if name == '' or any(str.isdigit(x) for x in name):
             import ErrorName
             top.destroy()
             import Register
    if usn == '':
             import ErrorName
             top.destroy()
             import Register
    path = "C:\\"
    x=path[2]
    path+=x
    path1=path+usn
    try:
        os.mkdir(path1,0755)
        os.mkdir(path1+x+'Inbox',0755)
        os.mkdir(path1+x+'Outbox',0755)
    except:
        top.destroy()
        import Register
    fw=open(path1+x+usn+'.dat', 'wb')
    fw.write(passw+'\n')
    fw.write(dob+'\n')
    fw.write(name+'\n')
    fw.write(usn)
    fw.close()
    
#CORRECTED AREA
    try :
        global s1,s2
        s1 =  str(datetime.now().hour) +':'+ str(datetime.now().minute)+':'+str(datetime.now().second)
        s2 = str(datetime.now().day) + '/' + str(datetime.now().month) +  '/' + str(datetime.now().year)
        d1 = {usn:[s1+','+s2,0]}
        
        frs = open("Session.txt",'r')
        d = pickle.load(frs)
        #d.update(d1)
        d[usn] = [s1+','+s2,0]
        frs.close()
        fws = open("Session.txt",'w')
        pickle.dump(d,fws)
        fws.flush()
        frs.close()
    except :
              fws = open("Session.txt",'w')
              d = {usn:[s1,',',s2,0]}
              pickle.dump(d,fws)
              fws.flush()
              fws.close()
    top.destroy()
    import Choose
    Choose.run(usn)
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
res = str(width)+'x'+str(height)
#print screensize
#global top
top= Tk()
img = PhotoImage(file = "Intro.GIF")
top.configure(background = "WHITE")
top.geometry(res)
top.title('Instance')
top.iconbitmap('icon.ico')
message1 = Label(image =img,borderwidth = 0,bg = "WHITE",compound = TOP)
message1.grid(row = 0,ipadx = 500)
message2 = Label(top, text = "Create an account", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",30))
message2.grid(row=1)
user1 = Label(top, text = "Name ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
user1.grid(row = 2)
n= Entry(top, relief = GROOVE, bd = 2)
n.grid(row = 3)
message1 = Label(top, text = "Username ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
message1.grid(row = 4, pady = 5)
u= Entry(top, relief = GROOVE, bd = 2)
u.grid(row = 5)
message1 = Label(top, text = "Password ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
message1.grid(row = 6)
p= Entry(top, relief = GROOVE, bd = 2,show = "*")
p.grid(row = 7)
message1 = Label(top, text = "Date Of Birth (DD/MM/YYYY)", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
message1.grid(row = 8)
Dob= Entry(top, relief = GROOVE, bd = 2)
Dob.grid(row = 9)
B1 = Tkinter.Button(top, text ="REGISTER", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = callback)
B1.grid(row=10,pady = 5)
top.mainloop()

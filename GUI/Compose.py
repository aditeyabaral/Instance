from Tkinter import *
import Tkinter,datetime
import os,sys,time
import ctypes,glob,os
def run(user):
    user = user
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    res = str(width)+'x'+str(height)
    def send():
            usn,sub,content = u.get(),s.get(),c.get("1.0",'end-1c')
            x='\\'
            path='C:\\'+x+usn+x+'Inbox'
            num=0
            l=0
            for filename in glob.glob(os.path.join(path,'UN*.dat')):
            #print 'temp',temp
            #print 'filename',filename
                    for a in filename:
                        if a.isdigit():
                            l=l+int(a)
                    num=1+int(l)
                    #print num
            temp=path+x+'UN'+str(num)+'.dat'
            try:
                fw=open(temp, 'wb')
                fw.write(str(user)+'\n')        
                fw.write(sub+'\n')
                fw.write(content)
                fw.close()

                path='C:\\'+x+usn+x+'Outbox'
                num=0
                l=0
                for filename in glob.glob(os.path.join(path,'UN*.dat')):
                #print 'temp',temp
                #print 'filename',filename
                        for a in filename:
                            if a.isdigit():
                                l=l+int(a)
                        num=1+int(l)
                        #print num
                temp=path+x+'UN'+str(num)+'.dat'
                fw=open(temp, 'wb')
                fw.write(str(user)+'\n')       
                fw.write(sub+'\n')
                fw.write(content)
                fw.close()
                top.destroy()
                import Instamail
                Instamail.run(user)
            except:
                import ErrorName
                top.destroy()
                import Compose
                Compose.run(user)
    	
    top = Tk()
    top.configure(background = "WHITE")
    top.geometry(res)
    top.iconbitmap('icon.ico')
    top.title("Instance")
    message1 = Label(top, text = "Username ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
    message1.pack()
    u= Entry(top, relief = GROOVE, bd = 2)
    u.pack()
    message1 = Label(top, text = "Subject ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
    message1.pack()
    s= Entry(top, relief = GROOVE, bd = 2)
    s.pack()
    message1 = Label(top, text = "Compose ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
    message1.pack()
    c= Text(top, relief = GROOVE, bd = 2)
    c.pack()
    message1 = Label(top,bg = "WHITE")
    message1.pack()
    B1 = Tkinter.Button(top, text ="SEND", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = send)
    B1.pack()
    top.mainloop()
run('')

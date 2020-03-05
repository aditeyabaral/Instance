from Tkinter import *
import Tkinter
from datetime import datetime
import os,sys,time
import ctypes
def run(user,name,dob,passw):
        global usn
        usn,name,dob,passw = user,name,dob,passw
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        res = str(width)+'x'+str(height)

        def callback():
                nname,npassw,ndob = n.get().strip(),p.get().strip(),Dob.get().strip()
                if nname == '' or any(str.isdigit(x) for x in nname):
                        import ErrorName
                        top.destroy()
                        import Edit
                        Edit.run(usn,name,dob,passw)
                date = ndob.split('/')
                #print len(ndob)
                if len(ndob)!=10:
                        import ErrorDOB
                        top.destroy()
                        import Edit
                        Edit.run(usn,name,dob,passw)
                if len(date)!=3:
                        import ErrorDOB
                        top.destroy()
                        import Edit
                        Edit.run(usn,name,dob,passw)
                if not(int(date[0]) in range(1,32) or date[1] in range(1,13) or int((datetime.now().year)-int(date[1]))<13):
                        import ErrorDOB
                        top.destroy()
                        import Edit
                        Edit.run(usn,name,dob,passw)
                path = "C:\\"
                path+=usn
                x=path[2]
                path+=x
                path1=path+usn+'.dat'
                #os.remove(path1)
                fw1 = open(path1,"wb")
                fw1.write(npassw+'\n')
                fw1.write(ndob+'\n')
                fw1.write(nname+'\n')
                fw1.write(usn)
                fw1.close()
                top.destroy()
                import Profile
                Profile.run(usn)

        top = Tk()
        img = PhotoImage(file = "Intro.GIF")
        top.configure(background = "WHITE")
        top.geometry(res)
        top.iconbitmap('icon.ico')
        top.title("Instance")
        message1 = Label(image =img,borderwidth = 0,bg = "WHITE",compound = TOP)
        message1.grid(row = 0,ipadx = 500)
        message2 = Label(top, text = "Enter new details", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",30))
        message2.grid(row=1)
        user1 = Label(top, text = "Name ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
        user1.grid(row = 2)
        n= Entry(top, relief = GROOVE, bd = 2)
        n.insert(0,name)
        n.grid(row = 3)
        message1 = Label(top, text = "Password ", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
        message1.grid(row = 4)
        p= Entry(top, relief = GROOVE, bd = 2,show = "*")
        p.insert(0,passw)
        p.grid(row = 5)
        message1 = Label(top, text = "Date Of Birth (DD/MM/YYYY)", bg = "WHITE", fg = "#FF5800",font = ("Comfortaa",15))
        message1.grid(row = 6)
        Dob= Entry(top, relief = GROOVE, bd = 2)
        Dob.insert(0,dob)
        Dob.grid(row = 7)
        B1 = Tkinter.Button(top, text ="SAVE", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = callback)
        B1.grid(row=8,pady = 5)
        top.mainloop()

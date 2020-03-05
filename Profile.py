from Tkinter import *
import Tkinter
import os,sys,time
import ctypes
def run(user):
        global usn
        global name
        global dob
        global email
        global passw
        usn = user
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        res = str(width)+'x'+str(height)
        path = "C:\\"
        x=path[2]
        path+=x
        path1=path+usn
        global dct
        dct = path1+x+user+'.dat'
        fw = open(dct,'rb')
        lines = fw.readlines()
        passw = (lines[0]).rstrip()
        dob = (lines[1]).rstrip()
        username = (lines[3]).rstrip()
        name = (lines[2]).rstrip()
        fw.close()
        def leave():
                top.destroy()
                import Settings
                Settings.run(usn)
        def display():             
                sub = Tk()
                sub.title("Instance")
                sub.iconbitmap('icon.ico')
                sub.configure(background = "WHITE")     
                message = Label(sub, text = "Username : "+username, fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",20))
                message.pack()
                message = Label(sub, text = "DOB : "+ dob, fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",20))
                message.pack()
                message = Label(sub, text = "Name : "+name, fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",20))
                message.pack()
                message = Label(sub, text = "Password : "+passw, fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",20))
                message.pack()
                sub.mainloop()
        def edit():
                top.destroy()
                import Edit
                Edit.run(usn,name,dob,passw)
        top = Tk()
        img = PhotoImage(file = "Intro.GIF")
        top.configure(background = "WHITE")
        top.geometry(res)
        top.title('Instance')
        top.iconbitmap('icon.ico')
        messageimg1 = Label(image =img,borderwidth = 0)
        messageimg1.pack()
        message = Label(top, text = "What would you like to do today?", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",40))
        message.pack()
        message1 = Label(bg = "WHITE")
        message1.pack()
        B1 = Tkinter.Button(top, text ="VIEW DETAILS", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = display)
        B1.pack()
        message1 = Label(bg = "WHITE")
        message1.pack()
        B2 = Tkinter.Button(top, text ="EDIT DETAILS", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = edit)
        B2.pack()
        message1 = Label(bg = "WHITE")
        message1.pack()
        B3 = Tkinter.Button(top, text ="SETTINGS", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = leave)
        B3.pack()
        top.mainloop()

from Tkinter import *
import Tkinter
import os,sys,time
import ctypes
def run(user):
        user = user
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        res = str(width)+'x'+str(height)
        def chat():
	        root.destroy()
	        import InstaChat
	        InstaChat.run(user)
	        
        def mail():
                root.destroy()
                import Instamail
                Instamail.run(user)
        def setting():
	        root.destroy()
	        import Settings
	        Settings.run(user)
        root = Tk()
        img = PhotoImage(file = "Intro.GIF")
        root.configure(background = "WHITE")
        root.geometry(res)
        root.iconbitmap('icon.ico')
        root.title("Instance")
        messageimg1 = Label(image =img,borderwidth = 0)
        messageimg1.pack()
        message = Label(root, text = "What would you like to do today?", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",40))
        message.pack()
        message1 = Label(bg = "WHITE")
        message1.pack()
        B1 = Tkinter.Button(root, text ="INSTAMAIL", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = mail)
        B1.pack()
        message1 = Label(bg = "WHITE")
        message1.pack()
        B2 = Tkinter.Button(root, text ="INSTACHAT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = chat)
        B2.pack()
        message1 = Label(bg = "WHITE")
        message1.pack()
        B3 = Tkinter.Button(root, text ="SETTINGS", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = setting)
        B3.pack()
        root.mainloop()

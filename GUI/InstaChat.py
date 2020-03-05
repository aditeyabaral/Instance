from Tkinter import *
import Tkinter
import os,sys,time
import ctypes
def run(user):
	user= user
	user32 = ctypes.windll.user32
	width = user32.GetSystemMetrics(0)
	height = user32.GetSystemMetrics(1)
	res = str(width)+'x'+str(height)
	def server():
		top.destroy()
		import Server
		Server.run(user)
	def client():
		top.destroy()
		import Client
		Client.run(user)	
	def leave():
		top.destroy()
		import Choose
		Choose.run(user)
	top = Tk()
	img = PhotoImage(file = "Intro.GIF")
	top.configure(background = "WHITE")
	top.geometry(res)
	top.iconbitmap('icon.ico')
	top.title("Instance")
	message2 = Label(image =img,borderwidth = 0)
	message2.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B1 = Tkinter.Button(top, text ="SERVER", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = server)
	B1.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B2 = Tkinter.Button(top, text ="CLIENT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = client)
	B2.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B3 = Tkinter.Button(top, text ="EXIT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = leave)
	B3.pack()
	top.mainloop()

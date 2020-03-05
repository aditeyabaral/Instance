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
	global u,usn
	def compose():
	        top.destroy()
	        import Compose
	        Compose.run(user)
	def inbox():
		top.destroy()
		import Read
		Read.run(user)
		#import Choose
		#Choose.run(user)
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
	message1 = Label(image =img,borderwidth = 0)
	message1.pack()
	B1 = Tkinter.Button(top, text ="COMPOSE", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = compose)
	B1.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B2 = Tkinter.Button(top, text ="INBOX", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = inbox)
	B2.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B3 = Tkinter.Button(top, text ="EXIT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = leave)
	B3.pack()
	top.mainloop()

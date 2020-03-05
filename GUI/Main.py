from Tkinter import *
import Tkinter
import ctypes,pickle
def login():
	top.destroy()
	import LogIn
def register():
        top.destroy()
        import Register
def exit():
	top.destroy()
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
res = str(width)+'x'+str(height)
top = Tk()
img = PhotoImage(file = "Intro.GIF")
top.configure(background = "WHITE")
top.geometry(res)
top.iconbitmap('icon.ico')
top.title("Instance")
message = Label(top, text = "Welcome to Instance!", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",40))
message.pack()
message1 = Label(image =img,borderwidth = 0)
message1.pack()
message1 = Label(bg = "WHITE")
message1.pack()
B1 = Tkinter.Button(top, text ="LOG IN", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = login)
B1.pack()
message1 = Label(bg = "WHITE")
message1.pack()
B2 = Tkinter.Button(top, text ="REGISTER", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = register)
B2.pack()
message1 = Label(bg = "WHITE")
message1.pack()
B3 = Tkinter.Button(top, text ="EXIT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = exit)
B3.pack()
top.mainloop()


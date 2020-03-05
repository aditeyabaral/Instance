from Tkinter import *
import Tkinter
def exit():
	sub.destroy()
sub = Tk()
sub.title("Instance")
sub.iconbitmap('icon.ico')
sub.configure(background = "WHITE")     
message = Label(sub, text = "Enter valid Date Of Birth", fg = "#FF5800",bg = "WHITE",font = ("Comfortaa",20))
message.pack()
message1 = Label(bg = "WHITE")
message1.pack()
B1 = Tkinter.Button(sub, text ="ACCEPT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 35,height = 2,font = ("Comfortaa"),command = exit)
B1.pack()
sub.mainloop()

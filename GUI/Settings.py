from Tkinter import *
import Tkinter
import os,sys,time,pickle
from datetime import datetime
import ctypes
def run(user):
	user = user
	user32 = ctypes.windll.user32
	width = user32.GetSystemMetrics(0)
	height = user32.GetSystemMetrics(1)
	res = str(width)+'x'+str(height)

	def profile():
		top.destroy()
		import Profile
		Profile.run(user)
	def out():
                        
                        s1 =  str(datetime.now().hour) +':'+ str(datetime.now().minute)+':'+str(datetime.now().second)
                        s2 = str(datetime.now().day) + '/' + str(datetime.now().month) +  '/' + str(datetime.now().year)
                        try:
                                fr = open("Session.txt",'r')
                                d = pickle.load(fr)
                                fr.close()
                                d[user][1] = s1+' , ' + s2
                                
                                fw = open("Session.txt",'w')
                                pickle.dump(d,fw)
                                fw.flush()
                                fw.close()
                        except:
                                fws = open("Session.txt",'w')
                                d = {user:[0,s1+','+s2]}
                                pickle.dump(d,fws)
                                fws.flush()
                                fws.close()
                        top.destroy()
                        import Main
	def leave():
		top.destroy()
		import Choose
		Choose.run(user)
	top = Tk()
	img = PhotoImage(file = "Intro.GIF")
	top.configure(background = "WHITE")
	top.geometry(res)
	top.iconbitmap('icon.ico')
	top.title('Instance')
	messageimg1 = Label(image =img,borderwidth = 0)
	messageimg1.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B1 = Tkinter.Button(top, text ="PROFILE", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = profile)
	B1.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B2 = Tkinter.Button(top, text ="LOGOUT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = out)
	B2.pack()
	message1 = Label(bg = "WHITE")
	message1.pack()
	B3 = Tkinter.Button(top, text ="EXIT", relief=FLAT,  bg = "#FF5800", fg="WHITE", highlightcolor = "WHITE",width = 50,height = 2,font = ("Comfortaa"),command = leave)
	B3.pack()
	top.mainloop()

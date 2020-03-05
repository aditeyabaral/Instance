def run():
	while True:
		print "1. Server"
		print "2. Client"
		ch = input("Enter :")
		if ch==1:
			import Server
		elif ch==2:
			import Client
		elif ch==3:
			import Choose
			Choose.run()
		else:
			print "Invalid Choice"
run()

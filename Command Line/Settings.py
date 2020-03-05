#Settings
import os,sys
import random
def run():
    print "Welcome to your Settings page!"
    print
    while True:
        print "1. Profile"
        print "2. Logout"
        print "3. Exit"
        print
        ch = input("Enter choice : ")
        if ch == 1:
            profile()
        elif ch == 2:
            import Main
        elif ch == 3:
            import Choose
            Choose.run()
            break
        else :
            print "Invalid Choice"
        print

def profile():
    global user
    user = raw_input("Enter username for verification : ")
    print
    path = "C:\\"
    x=path[2]
    path+=x
    path1=path+user
    #print path1
    #print x
    #print user
    global dct
    dct = path1+x+user+'.txt'
    #print dct
    
    while True:
        print "1. View details"
        print "2. Edit details"
        print "3. Exit"
        print
        ch = input("Enter choice : ")
        if ch == 1:
            fw = open(dct,'r')
            lines = fw.readlines()
            passw = (lines[0]).rstrip()
            dob = (lines[1]).rstrip()
            name = (lines[3]).rstrip()
            email = (lines[2]).rstrip()
            print "Name :", name
            print "Email ID :", email
            print "Date of Birth :", dob
            print "Password :", passw
            
        elif ch == 2:
            fw = open(dct,'r')
            lines = fw.readlines()
            passw = (lines[0]).rstrip()
            dob = (lines[1]).rstrip()
            name = (lines[3]).rstrip()
            email = (lines[2]).rstrip()
            print "1. Name"
            print "2. Date of Birth"
            print "3. Password"
            print "4. Email ID"
            choice = input("Enter choice :")
            fw.close()
            if choice == 1:
                nname = raw_input("Enter new name :")
                path = "C:\\"
                path+=user
                x=path[2]
                path+=x
                path1=path+user+'.txt'
                #print path1
                os.remove(path1)
                fw1 = open(path1,"w")
                fw1.write(passw+'\n')
                fw1.write(dob+'\n')
                fw1.write(email+'\n')
                fw1.write(nname+'\n')
                fw1.write(user)
                print "Name successfully changed!"
                print
                fw1.close()
            elif choice == 2:
                ndob = raw_input("Enter new DOB :")
                path = "C:\\"
                path+=user
                x=path[2]
                path+=x
                path1=path+user+'.txt'
                #print path1
                os.remove(path1)
                fw1 = open(path1,"w")
                fw1.write(passw+'\n')
                fw1.write(ndob+'\n')
                fw1.write(email+'\n')
                fw1.write(name+'\n')
                fw1.write(user)
                print "Date of birth successfully changed!"
                print
                fw1.close()
            elif choice == 3:
                npassw = raw_input("Enter new password :")
                path = "C:\\"
                path+=user
                x=path[2]
                path+=x
                path1=path+user+'.txt'
                #print path1
                os.remove(path1)
                fw1 = open(path1,"w")
                fw1.write(npassw+'\n')
                fw1.write(dob+'\n')
                fw1.write(email+'\n')
                fw1.write(name+'\n')
                fw1.write(user)
                print "Password successfully changed!"
                print
                fw1.close()
            elif choice == 4:
                nemail = raw_input("Enter new email :")
                path = "C:\\"
                path+=user
                x=path[2]
                path+=x
                path1=path+user+'.txt'
                #print path1
                os.remove(path1)
                fw1 = open(path1,"w")
                fw1.write(passw+'\n')
                fw1.write(dob+'\n')
                fw1.write(nemail+'\n')
                fw1.write(name+'\n')
                fw1.write(user)
                print "Email successfully changed!"
                print
                fw1.close()
        elif ch == 3:
            run()

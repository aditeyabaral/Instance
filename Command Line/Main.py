#main
import AccCreate
import os,Choose,random,time
from os.path import join
print  "Welcome to Instance!"
print
print "1. Login"
print "2. Register"
print
ch = input("Enter choice :")
if ch == 1:
    user = raw_input("Enter username :")
    #SEARCHING USING FILES
    look = user
    now = time.time()
    future = now+12
    flag1 = False
    for root,files,dirs in os.walk('C:\\'):
        if time.time() > future:
                break
        #print dirs
        if look in files:
            flag1 = True
            break
    passw = raw_input("Enter password :")+'\n'
    try:
            fcheck = open('C:\\'+user+"\\"+user+'.txt','r')
    except IOError:
            if flag1 == False:
                    print "Account doesn't exist."
                    import Main
    s=fcheck.readline()
    flag2=0
    if s==passw:
        flag2= True
    if flag1 == True and flag2 == True:
        print "Logged in!"
        print
        Choose.run()
    if flag1 == True and flag2 == False:
        print "Wrong password. Please try again" + '\n'
        import Main
    if flag1 == False and flag2 == False:
        print "Account doesn't exist. Please register." + '\n' 
elif ch == 2:
    AccCreate.run()

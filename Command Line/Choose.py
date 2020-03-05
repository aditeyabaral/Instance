import Settings
def run():
    print "1. Instamail"
    print "2. InstaChat"
    print "3. Settings"
    print
    ch = input("Enter your choice :")
    if ch == 1:
        import Instamail
    elif ch == 2:
        import Chat
        Chat.run()
    elif ch == 3:
        print Settings.run()
    else:
        print "Invalid Choice"
run()

def run():
        while True:
                print "1. Online"
                print "2. Offline"
                print "3. Exit"
                ch = input ("Enter choice :")
                if ch == 1:
                        import InstaChat
                        for i in range(1000):
                                 pass
                        import webbrowser
                        webbrowser.open('http://127.0.0.1:5000/')
                elif ch == 2:
                        import ChatOff
                        ChatOff.run()
                elif ch == 3:
                        import Choose
                        Choose.run()
                else:
                        print "Invalid Choice."


run()

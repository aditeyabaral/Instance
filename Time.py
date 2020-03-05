from datetime import datetime
s1 =  str(datetime.now().hour) +':'+ str(datetime.now().minute)+':'+str(datetime.now().second)
s2 = str(datetime.now().day) + '/' + str(datetime.now().month) +  '/' + str(datetime.now().year)
print s1 + ' , ' + s2

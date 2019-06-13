import datetime 

#here we will extract the current hour only to a vriable
curDate=datetime.datetime.now().hour

name=input("Enter your name ")

print("Current time hour",curDate)

''' now imp : 00:00 to 11:59   morning
              12:00 to 16:59   afternoon
              17:00 to 19:59   evening
              20:00 to 23:59   night
'''

if curDate>5 and curDate<12:
    print("Good morning ",name)

elif curDate>=12 and curDate<17:
    print("Good afternoon",name)

elif curDate>=17 and curDate<20:
    print("Good evening",name)

else:
    print("Good night",name)

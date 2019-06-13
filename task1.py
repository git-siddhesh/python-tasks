import datetime

name=input("Enter name :  ")
age=int(input("Enter age :  "))

x=(95-age)+datetime.datetime.now().year

print("You will be/was of 95 in ",x)

import os


def check(str1):
	return any(char.isdigit() for char in str1 )

str1=input('Enter String :')

if not check(str1):
	print("hii"+str1)
	passw="hello{"+str1+"}"
	cmd="useradd -p $(openssl passwd -1 "+passw+") "+str1
	os.system(cmd)
else :
	print("user can't created")	
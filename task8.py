import os

command = " "
while (command != "exit"):
    command =input("Command: ")
    handle = os.popen(command)
    exit_code=os.popen("echo $?")
    x=exit_code.read()
    print(x)
    #f=open("a.txt","a")
    if x==0 :
        print("Boo Yah! Command Exist")
        line =" "
        while line:
            line = handle.read()
            print(line)
       #     f.write(line+'\n')
    handle.close()
    exit_code.close()
    #f.close()
print("Ciao that's it!")

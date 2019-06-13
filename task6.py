file2="none"
opt="none"
string=input("Enter the file name and option as(file opt [file] )")
list=string.split( )
length=len(list)
if length>=1:
    file1=list[0]
if length>=2:
    opt=list[1]
if length>=3:
    file2=list[2]

#similar to cat file cmd
if opt=="none":
    with open("file1","r") as f:
        print(f.read())

# similar to cat > file cmd        
elif opt==">" and file2=="none":
    print("Enter !x to exit in new line")
    with open("file1","w") as f:
        str1=input()
        while str1!="":
            f.write(str1)
            f.write('\n')
            str1=input()

# similar to cat -E file cmd            
elif opt=="E" and file2=="none":
    with open("file1","r") as f:
        line=f.readline()
        while line :
            print(line,"$")
            line=f.readline()

# similar to cat -n file_name cmd
elif opt=="n" and file2=="none":
    with open("file1","r") as f :
        cnt=1
        line=f.readline()
        while line:
            print(cnt," ",line)
            line=f.readline()
            cnt+=1

#similar to cat file1 > file2
elif opt==">" and file2!="none":
    f1=open("file1","r")
    f2=open("file2","w")
    f2.write(f1.read())
    f1.close()
    f2.close()




import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostip="127.0.0.1"
hostport=2222
s.bind((hostip,hostport))
s.listen()
conn,addr=s.accept()
choice=conn.recvfrom(500)
print("Enter 'exit' to end the chat!")
if choice[0].decode('ascii')=='1':
    data=conn.recvfrom(500)
    data2=data[0].decode('ascii')
    while data2!='exit':
        print(data2)
        data2=input("Enter the  message : ")
        data=data2.encode('ascii')
        conn.sendall(data)
        if data2=='exit': break
        data=conn.recvfrom(500)
        data2=data[0].decode('ascii')
else:
    data=conn.recvfrom(500)
    data2=data[0].decode('ascii')
    while data2!='exit':
        print(data2)
        data=conn.recvfrom(500)
        data2=data[0].decode('ascii')
print('client conection closed')
conn.close()
s.close()
        

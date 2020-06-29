import socket

hostip='127.0.0.1'
hostport=2222
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hostip,hostport))
print("\nEnter 'exit' to end the chat!\n\n")
choice= input("Press 1 for bidirection chatting and 2 for unidirectional ")
s.sendall(choice.encode('ascii'))
if choice==1:
    data=input("Enter messg: ")
    data2=data.encode('ascii')
    s.sendall(data2)
    while data!='exit':
        data2=s.recvfrom(500)
        data=data2[0].decode('ascii')
        print(data)
        if data=='exit':
            print("connection terminating")
            break;
        data=input("Enter messg: ")
        data2=data.encode('ascii')
        s.sendall(data2)
else:
    data=input("Enter messg: ")
    data2=data.encode('ascii')
    s.sendall(data2)
    while data!='exit':
        data=input("Enter messg: ")
        data2=data.encode('ascii')
        s.sendall(data2)
    
s.close()
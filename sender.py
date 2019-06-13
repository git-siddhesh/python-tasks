#!/usr/bin/python2

import socket

recv_ip="127.0.0.1"
recv_port=4444            # you can check free udp port using  #netstat -nulp

#creating udp socket (ip type, tcp/udp)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#fitting ip and port with  udp socket

s.sendto("HEllo",(recv_ip,recv_port))


s.close()

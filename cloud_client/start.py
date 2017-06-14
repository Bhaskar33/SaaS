#!/usr/bin/python
import os,sys,socket,commands,time,getpass

s_IP="192.168.122.211"
s_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

username=raw_input("enter your username:")
#Taking username from user

password=getpass.getpass("enter your password:")
#Taking password from user

s.sendto(username,(s_IP,s_port))
s.sendto(password,(s_IP,s_port))
#sending username and password to server

z=s.recvfrom(100)
if z[0]=="ok":
	print "connected"
	execfile('saas.py')
else:
	print"authentication error"

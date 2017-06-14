#!/usr/bin/python
import os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

c_data=s.recvfrom(100)
c_data1=s.recvfrom(100)

if c_data[0]=="root" and c_data1[0]=="redhat":
	s.sendto("ok",c_data[1])


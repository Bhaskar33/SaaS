#!/usr/bin/python
import os,sys,socket,commands,time

s_IP="192.168.122.211"
s_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

x="""
	press 1 to get firefox:
	press 2 to get vlc:
	press 3 to get calculator:
	press 4 to get office:
	press 5 to get Screenshot of your screen:
	press 6 to open your webcam:
	press 7 to open ImangeViewer:
	press 8 to get gedit:
"""
print x

ch=raw_input("enter your choice:")

if ch=='1':
	print "wait for a sec!!"
	execfile('firefox.py')
elif ch=='2':
	print "wait for a sec!!"
	execfile('vlc.py')
elif ch=='3':
	print "wait for a sec!!"
	execfile('calculator.py')
elif ch=='4':
	print "wait for a sec!!"
	execfile('office.py')
elif ch=='5':
	print "wait for a sec!!"
	execfile('screenshot.py')
elif ch=='6':
	print "wait for a sec!!"
	execfile('webcam.py')
elif ch=='7':
	print "wait for a sec!!"
	execfile('imageviewer.py')
elif ch=='8':
	print "wait for a sec!!"
	execfile('gedit.py')
else:
	print "Please type correct input!! "
	execfile('saas.py')

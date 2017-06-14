#!/usr/bin/python
import os,sys,socket,commands,time

s_IP="192.168.122.211"
s_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system('sshpass -p "q" ssh -X root@'+s_IP+' gnome-screenshot')
execfile('saas.py')

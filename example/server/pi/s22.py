# -*- coding: UTF-8 -*-
import socket            
from _thread import *         
import threading

new_value = 0      # pi--->phone (string)

print_lock = threading.Lock() 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #afinte-->local net , sock-->tcp 
#host = socket.gethostname() 
host = "192.168.43.141"
port = 5000               
s.bind((host, port))      #ip <-->port

s.listen(5)         #server

print("server (ip:port):", s.getsockname())   #print ip

def recv_threaded(c):                         #recive 
	while True:
		data = c.recv(1024)           #size 1024 byte
		if not data:                  #exit
			break
		print(data.decode('utf-8'))

	c.close() 

def send_threaded(c):                         #send
	while True:
		new_value = input()                    #wait input
		c.send(new_value.encode('utf-8'))      #(string)
	     

	c.close() 

while True:
	c, addr = s.accept()                        #wait phone send ip
	print("ip:",addr)            
	start_new_thread(recv_threaded, (c,))
	start_new_thread(send_threaded, (c,))

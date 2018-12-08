# -*- coding: UTF-8 -*-
import socket    
from _thread import *         
import threading

new_value = 0
old = 0

print_lock = threading.Lock() 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
#host = socket.gethostname() 
host = "192.168.43.141"
port = 5000               
s.bind((host, port))      

s.listen(5)  

print("server (ip:port):", s.getsockname())   

def recv_threaded(c): 
	while True:
		data = c.recv(1024)
		if not data:
			break
		print(data.decode('utf-8'))

	c.close() 

def send_threaded(c): 
	while True:
		new_value = input()
		c.send(new_value.encode('utf-8'))
	     

	c.close() 

while True:
	c, addr = s.accept()
	print("ip:",addr)
	start_new_thread(recv_threaded, (c,))
	start_new_thread(send_threaded, (c,))

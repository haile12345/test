# importing required modules
from cmd import Cmd
import random
import socket	
import datetime

# initializing socket
s = socket.socket()	
host = socket.gethostname()
port = 12345

# binding port and host
s.bind((host, port))

# waiting for a client to connect
s.listen(5)
		
while True:
# accept connection
    c, addr = s.accept()
    w = c.recv(1024).decode()
    print ('got connection from addr', addr)
    f = open("selam.txt", "r")
    d = str(f.read())
    
    # sending data type should be string and encode before sending
    c.send(d.encode())
    f = open("selam.txt", "w")
    f.write(str(w))
    f.close()
    c.close()

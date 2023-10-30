# keep diffrent file name then module name because it might break the code ,, 


import sys 
import socket

Host = "127.0.0.1"
port = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket "S" with 2 arguments AF_INET = ipv4 , SOCK_STREAM = TCP 
s.connect((Host, port)) # binding socket with host and port


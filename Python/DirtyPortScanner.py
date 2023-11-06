#!/bin/python3 

import sys 
import socket 
from datetime import datetime 



# This code is responsible for determining the target IP address for the port scanning operation.
target = "0.0.0.0"
if len(sys.argv) == 2: 
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

# Add a pretty banner
print('-'*50)   
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print('-'*50)

# The code is performing a port scanning operation on the target IP address. It uses a for loop to
# iterate through a range of port numbers (from 0 to 60179) and creates a socket object for each port.
try:
    for port in range (0,60179):
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            # print(target,port)
            result = s.connect_ex((target,port)) # return 0 or 1 , if port is open it throw 0 , otherwise 1 
            if result == 0 :
                 print(f"{port} is open")
            # else :
            #      print(f"{port} is closed")
            s.close()


except KeyboardInterrupt :
    print("\nExiting process\n")
    sys.exit() 

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

    
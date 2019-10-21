# Importing the socket module
import socket

# Importing the devices class
from devices import device

# Create a socket object 
sock = socket.socket()          
  
# Define the port on which you want to connect 
port = 1013                
  
# Connect to the server on local computer 
sock.connect(('127.0.0.1', port))

# Sockname
sockname = sock.getsockname()

# Send sockname to the server
sock.send(str(sockname[1]).encode('utf-8')) 

# Create a device object and encode it
current_device = device.get_dummy_vals(json_response=True).encode('utf-8')

# Loop and close connection on condition
while(True):    
    # Receive data from the server 
    data = sock.recv(1024).decode('utf-8')
    print(data)

    # Send device details
    if(data=='SEND_DEVICE_INFO'):
        sock.send(current_device)

    if(data=='CLOSE'):
        break

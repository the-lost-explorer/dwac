# Importing the socket module
import socket,json                

# Import the wireless module
from wireless import environment

# Create environment object
wireless_environment = environment()

# Create a socket object 
sock = socket.socket()          
  
# Reserving a port for socket binding
port = 1013                
  
# Bind the port the socket
sock.bind(('', port))         
print("Socket bound to %s" %(port)) 
  
# Put the socket into listening mode 
sock.listen(5)      
print("Socket is currently listening")
  
# List of client socknames
clients = []

# Just to limit stuff
n = 3


while(n>0): 
  
   # Establish connection with client 
   client, addr = sock.accept()      
   print('DEBUG : Got connection from', addr)

   # Receive peer name from client
   peer_name = client.recv(1024).decode('utf-8')
   print("DEBUG : Peer name : %s" %peer_name)

   # Send some messages back to client
   client.send('SEND_DEVICE_INFO'.encode('utf-8'))
   
   # Receive device data from client
   device_data = json.loads(client.recv(1024).decode('utf-8'))
   wireless_environment.collection_of_nodes[peer_name] = device_data

   client.send("CLOSE".encode('utf-8'))
   
   n-=1

print(wireless_environment.collection_of_nodes)
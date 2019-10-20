# Importing the socket module
import socket                
  
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
n = 5


while(n>0): 
  
   # Establish connection with client. 
   client, addr = sock.accept()      
   print('Got connection from', addr[0])

   # Receive data from client
   data = client.recv(1024).decode('utf-8')
   print(data)

   # Add client to client list
   clients.append(client.getpeername()[1])

   # Send some messages back to client
   client.send('TEST'.encode('utf-8'))
   client.send("CLOSE".encode('utf-8'))
   
   n-=1

print(clients)
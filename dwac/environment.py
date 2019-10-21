# Importing the socket module
import socket
import json
import threading
import subprocess
# Import the wireless module
from wireless import wireless

# Create environment object 
wireless_environment = wireless()


def handle_client(client):
   '''@params: client
      @description: Handle incoming clients'''
   
   '''
   Initializing connection with the node here
   '''

   request = json.loads(client.recv(255).decode('utf8'))
   print(request, type(request))
   response = 'Your device detected in the wireless medium.'
   client.send(response.encode('utf8'))
   
   '''
   Main loop here
   '''
   while(True):
      pass
   
   
   client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 15558))
server.listen(8)

try:
    while True:
        client, _ = server.accept()
        threading.Thread(target=handle_client, args=(client,)).start()
except KeyboardInterrupt:
    server.close()

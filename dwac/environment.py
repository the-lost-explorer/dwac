# Import
import socket, json, threading, subprocess

# Import the wireless module
from wireless import wireless

# Create environment object 
wireless_environment = wireless()

# Master collection of nodes
node_collection = {}


def handle_client(client):
   '''@params: client
      @description: Handle incoming clients'''
   
   '''
   Initializing connection with the node here
   '''

   request = json.loads(client.recv(255).decode('utf8'))
   node_collection[request['id']] = request

   print(node_collection)

   response = 'Your device detected in the wireless medium.'
   client.send(response.encode('utf8'))
   
   '''
   Main loop here
   '''
   try:
      while(True):
         request = client.recv(255).decode('utf-8')
         print("MAIN LOOP:",request)
         if(request.split()[0]=='EXIT'):
            del node_collection[int(request.split()[1])]
            break
         else:
            pass
         print(node_collection)
   except KeyboardInterrupt:
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

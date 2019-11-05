# Import
import socket, json, threading, subprocess

# Import the wireless module
from wireless import wireless

# Create environment object 
wireless_environment = wireless()

# Master collection of nodes
node_collection = {}

#Device params
MAX_BATTERY = 100
MAX_PROCESSOR = 1024
MAX_MEMORY = 1024

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

def prioritise_devices(devices):
    left_tree = []
    right_tree = []

    # Sort according to charging
    for device in devices:
        if int(device['battery']) > (0.2*MAX_BATTERY) or device['charging'] == 1:
            left_tree.append(device)
        else:
            right_tree.append(device)

    # Sort according to processing speed and memory
    left_tree = sorted(left_tree, key = lambda i: i['processor_speed']+i['free_memory'], reverse = True)
    right_tree = sorted(right_tree, key = lambda i: i['processor_speed']+i['free_memory'], reverse = True)

    combined_tree = left_tree + right_tree
    # Dictonary of priority
    priority_dict = {}
    for i in range(len(combined_tree)):
        priority_dict[i+1] = combined_tree[i]

    return priority_dict

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 15558))
server.listen(8)

try:
    while True:
        client, _ = server.accept()
        threading.Thread(target=handle_client, args=(client,)).start()
except KeyboardInterrupt:
   server.close()

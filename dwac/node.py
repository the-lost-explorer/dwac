# Import
import socket, devices, json, time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 15558))

current_device = json.loads(devices.device.get_dummy_vals())
print(current_device,type(current_device))

try:
    '''
    Initializing connection with the environment
    '''
    request = json.dumps(current_device)
    server.send(request.encode('utf8'))
    response = server.recv(255).decode('utf8')
    print(response)

    '''
    Main loop here
    '''
    while(True):
        



        # after whatever is done, wait for 2 seconds, then update
        time.sleep(2.0)
        if(current_device['charging']==0):
            current_device['battery'] -= 1
            if(current_device['battery']<=20):
                raise KeyboardInterrupt
        print(current_device)

except KeyboardInterrupt:
    exit_message = "EXIT "+str(current_device['id'])
    server.send(exit_message.encode('utf-8'))
    server.close()
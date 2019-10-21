import socket, devices

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 15558))
request = None
current_device = devices.device.get_dummy_vals()
try:
    '''
    Initializing connection with the environment
    '''
    request = current_device
    server.send(request.encode('utf8'))
    response = server.recv(255).decode('utf8')
    print(response)


    '''
    Main loop here
    '''
    while(True):
        pass

except KeyboardInterrupt:
    server.close()
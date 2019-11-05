# Import
import socket, devices, json, time

from timer import RepeatedTimer

current_device = json.loads(devices.device.get_dummy_vals())
print(current_device,type(current_device))

def update_device(current_device):
    try:
        if(current_device['charging']==0):
            current_device['battery'] -= 1
            if(current_device['battery']<=20):
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        message = "EXIT "+str(current_device['id'])
        server.send(message.encode('utf-8'))
        server.close()
        rt.stop()
    finally:        
        print(current_device)

rt = RepeatedTimer(5, update_device, current_device )

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 15558))

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
        
        # Slow things down
        time.sleep(2)
        
        # Update the device info
        print("Sending update")
        message = "UPDATE "+str(current_device['id'])
        server.send(message.encode('utf-8'))
        request = json.dumps(current_device)
        server.send(request.encode('utf-8'))

        # Check if it's successfully updated
        response = server.recv(255).decode('utf-8')
        print(response)

        

except KeyboardInterrupt:
    message = "EXIT "+str(current_device['id'])
    server.send(message.encode('utf-8'))
    server.close()
    rt.stop()

except OSError:
    server.close()

finally:
    rt.stop()
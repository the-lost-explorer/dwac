"""
    id - uniquely identify a device (Android has Android ID)
    status - whether user is currently using it right now (0/1)
    battery - battery percentage (0 to 100)
    charging - whether the device is being charged right now (0/1)
    free_memory - RAM available in MB (variable)
    processor_speed - processor speed in MHz (variable)
"""
""" Sample devices
"""
d1 = {'status':0,'battery':'85','charging':1,'free_memory':870,'processor_speed':512}
d2 = {'status':0,'battery':'78','charging':1,'free_memory':500,'processor_speed':202}
d3 = {'status':0,'battery':'56','charging':1,'free_memory':432,'processor_speed':256}
d4 = {'status':0,'battery':'43','charging':1,'free_memory':329,'processor_speed':640}
d5 = {'status':0,'battery':'56','charging':1,'free_memory':123,'processor_speed':156}
d6 = {'status':0,'battery':'37','charging':1,'free_memory':1024,'processor_speed':270}
d7 = {'status':0,'battery':'23','charging':1,'free_memory':650,'processor_speed':1024}
d8 = {'status':0,'battery':'12','charging':1,'free_memory':400,'processor_speed':45}
d9 = {'status':0,'battery':'5','charging':0,'free_memory':260,'processor_speed':56}
d10 = {'status':0,'battery':'59','charging':0,'free_memory':170,'processor_speed':700}
d11 = {'status':0,'battery':'29','charging':0,'free_memory':127,'processor_speed':314}
d12 = {'status':0,'battery':'32','charging':0,'free_memory':56,'processor_speed':900}
d13 = {'status':0,'battery':'92','charging':0,'free_memory':150,'processor_speed':750}
d14 = {'status':0,'battery':'100','charging':0,'free_memory':270,'processor_speed':280}
d15 = {'status':0,'battery':'69','charging':0,'free_memory':50,'processor_speed':340}

d = {1:d1,2:d2,3:d3,4:d4,5:d5,6:d6,7:d7,8:d8,9:d9,10:d10,11:d11,12:d12,13:d13,14:d14,15:d15}

MAX_BATTERY = 100

def prioritise_devices(devices):
    device_keys = list(devices.keys())
    device_values = list(devices.values())

    for i in range(len(device_keys)):
        device_values[i]['id'] =  device_keys[i]

    left_tree = []
    right_tree = []

    # Sort according to charging
    for device in device_values:
        if int(device['battery']) > (0.5*MAX_BATTERY) or device['charging'] == 1:
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
        d_id = combined_tree[i]['id']
        priority_dict[i+1] = combined_tree[i]

    return priority_dict 

print(prioritise_devices(d))


        






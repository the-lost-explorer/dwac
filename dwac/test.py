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
d1 = {'id':'1','status':0,'battery':'85','charging':1,'free_memory':870,'processor_speed':512}
d2 = {'id':'2','status':0,'battery':'78','charging':1,'free_memory':500,'processor_speed':202}
d3 = {'id':'3','status':0,'battery':'56','charging':1,'free_memory':432,'processor_speed':256}
d4 = {'id':'4','status':0,'battery':'43','charging':1,'free_memory':329,'processor_speed':640}
d5 = {'id':'5','status':0,'battery':'56','charging':1,'free_memory':123,'processor_speed':156}
d6 = {'id':'6','status':0,'battery':'37','charging':1,'free_memory':1024,'processor_speed':270}
d7 = {'id':'7','status':0,'battery':'23','charging':1,'free_memory':650,'processor_speed':1024}
d8 = {'id':'8','status':0,'battery':'12','charging':1,'free_memory':400,'processor_speed':45}
d9 = {'id':'9','status':0,'battery':'5','charging':0,'free_memory':260,'processor_speed':56}
d10 = {'id':'10','status':0,'battery':'59','charging':0,'free_memory':170,'processor_speed':700}
d11 = {'id':'11','status':0,'battery':'29','charging':0,'free_memory':127,'processor_speed':314}
d12 = {'id':'12','status':0,'battery':'32','charging':0,'free_memory':56,'processor_speed':900}
d13 = {'id':'13','status':0,'battery':'92','charging':0,'free_memory':150,'processor_speed':750}
d14 = {'id':'14','status':0,'battery':'100','charging':0,'free_memory':270,'processor_speed':280}
d15 = {'id':'15','status':0,'battery':'69','charging':0,'free_memory':50,'processor_speed':340}

d = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]


print(prioritise_devices(d))


        






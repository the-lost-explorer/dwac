# """Purely for testing stuff."""
# from devices import device
# a = []
# d1 = device.get_dummy_vals()
# print(d1)

from twisted.internet import task, reactor

update_time = 2.0 # seconds

def update_device_info():
    print('ya')
    


l = task.LoopingCall(update_device_info)
l.start(update_time) # call every timeout seconds
reactor.run()